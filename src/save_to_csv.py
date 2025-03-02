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

# Query GraphQL para buscar os 50 repositórios mais populares (reduzimos para evitar falhas)
QUERY = """
{
  search(query: "stars:>10000", type: REPOSITORY, first: 50) {
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

def fetch_repositories(retries=5, wait_time=15):
    """ Faz a requisição para a API do GitHub com tentativas automáticas. """
    for attempt in range(retries):
        response = requests.post(GITHUB_API_URL, json={"query": QUERY}, headers=HEADERS)
        print(f"📡 Tentativa {attempt+1}/{retries} - Status da Requisição: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            if "data" in data and "search" in data["data"]:
                return data
            else:
                print("❌ Erro: Resposta inesperada da API do GitHub")
                print(data)
                return None
        elif response.status_code in [502, 503, 504]:  # Erros temporários da API
            print(f"⚠️ Erro {response.status_code} - Tentando novamente ({attempt+1}/{retries}) em {wait_time} segundos...")
            time.sleep(wait_time)
        else:
            print(f"❌ Erro: {response.status_code}")
            print(response.text)
            return None
    print("❌ Erro: Todas as tentativas falharam.")
    return None

def save_to_csv(data, filename="data/repositories.csv"):
    """ Salva os dados em um arquivo CSV """
    repositories = []
    
    for repo in data["data"]["search"]["edges"]:
        node = repo["node"]
        if node:  # Garantir que o node não seja None
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
    
    # Criar DataFrame do Pandas
    df = pd.DataFrame(repositories)

    # Criar pasta 'data' se não existir
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Salvar em CSV
    df.to_csv(filename, index=False)
    print(f"✅ Dados salvos em {filename}")

if __name__ == "__main__":
    data = fetch_repositories()
    
    if data:
        save_to_csv(data)
