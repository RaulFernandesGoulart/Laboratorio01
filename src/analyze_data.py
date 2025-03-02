import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho do arquivo processado
INPUT_FILE = "data/processed_repositories.csv"
OUTPUT_FOLDER = "reports/"

def load_data():
    """ Carrega os dados processados do CSV. """
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Erro: Arquivo {INPUT_FILE} não encontrado! Execute process_data.py primeiro.")
        exit(1)
    
    df = pd.read_csv(INPUT_FILE)
    print(f"📂 Dados carregados! Total de repositórios: {len(df)}")
    return df

def plot_and_save(df, column, title, xlabel, ylabel, filename, kind="hist", bins=20):
    """ Gera e salva gráficos automaticamente. """
    plt.figure(figsize=(8, 5))
    
    if kind == "hist":
        df[column].hist(bins=bins, edgecolor="black")
    elif kind == "bar":
        df[column].value_counts().plot(kind="bar", color="royalblue")
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    # Criar pasta reports se não existir
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Salvar gráfico
    path = os.path.join(OUTPUT_FOLDER, filename)
    plt.savefig(path)
    print(f"📊 Gráfico salvo em: {path}")

def generate_graphics(df):
    """ Gera gráficos para análise dos dados. """
    plot_and_save(df, "repo_age_years", "Idade dos Repositórios", "Idade (anos)", "Número de Repositórios", "repo_age.png")
    plot_and_save(df, "pull_requests", "Distribuição de Pull Requests", "Total de PRs", "Número de Repositórios", "pull_requests.png")
    plot_and_save(df, "releases", "Distribuição de Releases", "Total de Releases", "Número de Repositórios", "releases.png")
    plot_and_save(df, "days_since_update", "Tempo desde Última Atualização", "Dias", "Número de Repositórios", "update_days.png")
    plot_and_save(df, "closed_issue_percentage", "Percentual de Issues Fechadas", "Percentual (%)", "Número de Repositórios", "closed_issues.png")

    # Linguagens mais populares
    plot_and_save(df, "language", "Linguagens Mais Usadas", "Linguagens", "Número de Repositórios", "languages.png", kind="bar")

if __name__ == "__main__":
    df = load_data()
    generate_graphics(df)
