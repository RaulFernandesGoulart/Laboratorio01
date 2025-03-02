import pandas as pd
from datetime import datetime
import os

# Caminho dos arquivos
INPUT_FILE = "data/repositories.csv"
OUTPUT_FILE = "data/processed_repositories.csv"

def load_data():
    """ Carrega os dados do CSV e retorna um DataFrame. """
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Erro: Arquivo {INPUT_FILE} não encontrado! Execute save_to_csv.py primeiro.")
        exit(1)
    
    df = pd.read_csv(INPUT_FILE)
    print(f"📂 Dados carregados com sucesso! Total de repositórios: {len(df)}")
    return df

def process_data(df):
    """ Calcula as métricas para responder as RQs. """
    # Converter datas para o formato datetime (removendo fuso horário)
    df["created_at"] = pd.to_datetime(df["created_at"]).dt.tz_convert(None)
    df["updated_at"] = pd.to_datetime(df["updated_at"]).dt.tz_convert(None)

    # Calcular a idade do repositório (anos)
    df["repo_age_years"] = (datetime.now() - df["created_at"]).dt.days / 365

    # Calcular tempo desde a última atualização (dias)
    df["days_since_update"] = (datetime.now() - df["updated_at"]).dt.days

    # Calcular percentual de issues fechadas
    df["closed_issue_percentage"] = (df["closed_issues"] / df["total_issues"]) * 100
    df["closed_issue_percentage"] = df["closed_issue_percentage"].fillna(0)  # Substituir NaN por 0%

    print("✅ Processamento concluído!")
    return df


def save_processed_data(df):
    """ Salva os dados processados em um novo CSV. """
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"📁 Dados processados salvos em {OUTPUT_FILE}")

if __name__ == "__main__":
    df = load_data()
    df = process_data(df)
    save_processed_data(df)
