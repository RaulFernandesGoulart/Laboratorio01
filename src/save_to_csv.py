import os
import requests
import pandas as pd
import time

# Obter o token do ambiente
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Verificar se o token está definido
if not GITHUB_TOKEN:
    print("❌ Erro: GITHUB_TOKEN não está definido. Configure a variável de ambiente antes de continuar.")
    exit(1)

# URL da API GraphQL do GitHub
GITHUB_API_URL = "https://api.github.com/graphql"

# Cabeçalhos da requisição
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

# Caminho do arquivo CSV
OUTPUT_FILE = "data/repositories.csv"

# Query GraphQL com paginação (50 repositórios por requisição)
QUERY_TEMPLATE = """
{
  search(query: "stars:>10000", type: REPOSITORY, first: 20, after: AFTER_CURSOR) {
    pageInfo {
      hasNextPage
      endCursor
    }
    edges {
      node {
        ... on Repository {
          nameWithOwner
          createdAt
          pullRequests {
            totalCount
          }
          releases {
            totalCount
          }
          updatedAt
          primaryLanguage {
            name
          }
          issues {
            totalCount
          }
          closedIssues: issues(states: CLOSED) {
            totalCount
          }
        }
      }
    }
  }
}
"""

def fetch_repositories(max_repos=1000, wait_time=5):
    """ Coleta até `max_repos` repositórios populares do GitHub com paginação. """
    repositories = []
    after_cursor = "null"
    total_fetched = 0

    while total_fetched < max_repos:
        print(f"📡 Buscando repositórios {total_fetched+1} até {total_fetched+50}...")

        # Substituir cursor na query
        query = QUERY_TEMPLATE.replace("AFTER_CURSOR", after_cursor if after_cursor != "null" else "null")

        try:
            response = requests.post(GITHUB_API_URL, json={"query": query}, headers=HEADERS, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
            else:
                print(f"⚠️ Erro {response.status_code} - Aguardando {wait_time}s antes de tentar novamente...")
                time.sleep(wait_time)
                continue  # Tenta novamente

        except requests.exceptions.RequestException as e:
            print(f"❌ Erro de conexão: {e}. Tentando novamente em {wait_time}s...")
            time.sleep(wait_time)
            continue  # Tenta novamente

        # Verificar estrutura dos dados
        if "data" not in data or "search" not in data["data"]:
            print("❌ Erro: Estrutura inesperada da resposta da API.")
            print(data)
            return None
        
        search_data = data["data"]["search"]
        
        # Processar repositórios
        for repo in search_data["edges"]:
            node = repo["node"]
            repositories.append({
                "name": node["nameWithOwner"],
                "created_at": node["createdAt"],
                "pull_requests": node["pullRequests"]["totalCount"],
                "releases": node["releases"]["totalCount"],
                "updated_at": node["updatedAt"],
                "language": node["primaryLanguage"]["name"] if node["primaryLanguage"] else "Unknown",
                "total_issues": node["issues"]["totalCount"],
                "closed_issues": node["closedIssues"]["totalCount"]
            })

        total_fetched += len(search_data["edges"])

        # Verificar se há mais páginas para buscar
        if not search_data["pageInfo"]["hasNextPage"]:
            break
        after_cursor = f'"{search_data["pageInfo"]["endCursor"]}"'

        # Aguardar para evitar limite da API
        time.sleep(wait_time)

    return repositories

def save_to_csv(repositories):
    """ Salva os dados em um arquivo CSV """
    df = pd.DataFrame(repositories)

    # Criar pasta 'data' se não existir
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Salvar CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Dados salvos em {OUTPUT_FILE}")

if __name__ == "__main__":
    repositories = fetch_repositories()
    if repositories:
        save_to_csv(repositories)
