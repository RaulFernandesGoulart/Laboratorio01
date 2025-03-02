import os

token = os.getenv("GITHUB_TOKEN")
if token:
    print("✅ Token carregado com sucesso!")
else:
    print("❌ Erro: Token não encontrado.")
    
