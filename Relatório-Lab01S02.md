# **Relatório - Lab01S02**

## **1. Introdução**

Este relatório apresenta a segunda etapa do projeto, **Lab01S02**, cujo objetivo foi realizar a **coleta, processamento e análise de 1000 repositórios populares do GitHub**. Para isso, foi implementada **paginação** na API GraphQL do GitHub e os dados foram armazenados em um arquivo `.csv`. Além disso, foram formuladas **hipóteses informais** com base nos dados coletados e nos gráficos gerados.

---

## **2. Metodologia**

### **2.1 Coleta de Dados**

A coleta de dados foi realizada por meio da **API GraphQL do GitHub**, onde foram extraídos **1000 repositórios** populares, considerando aqueles com **mais de 10.000 estrelas**. Para evitar erros **502 (Bad Gateway)**, foi implementada uma estratégia de paginação, coletando **20 repositórios por requisição**.

Os dados extraídos incluíram:

- **Idade do repositório** (data de criação)
- **Número total de Pull Requests aceitos**
- **Número total de Releases**
- **Data da última atualização**
- **Linguagem principal do repositório**
- **Total de Issues e percentual de Issues fechadas**

Os dados foram armazenados no arquivo **`data/repositories.csv`** para posterior análise.

### **2.2 Processamento dos Dados**

Os dados foram processados para extrair as seguintes métricas:

- **Idade do repositório (anos)** = Diferenca entre a data atual e a data de criação.
- **Tempo desde a última atualização (dias)** = Diferenca entre a data atual e a última atualização.
- **Percentual de Issues fechadas** = (Total de issues fechadas / Total de issues) * 100.

As informações processadas foram armazenadas em **`data/processed_repositories.csv`**.

### **2.3 Análise dos Dados**

Foram gerados gráficos para visualizar padrões e relações entre as métricas analisadas. Os seguintes gráficos foram produzidos:

- **Distribuição da Idade dos Repositórios** (`repo_age.png`)
- **Distribuição de Pull Requests** (`pull_requests.png`)
- **Distribuição de Releases** (`releases.png`)
- **Tempo desde a última atualização** (`update_days.png`)
- **Percentual de Issues Fechadas** (`closed_issues.png`)
- **Linguagens mais usadas** (`languages.png`)

Com base nessas informações, foram formuladas as seguintes hipóteses informais:

---

## **3. Hipóteses Informais**

### **Hipótese 1: Repositórios populares tendem a ser mais antigos**

🔹 A distribuição da idade dos repositórios sugere que muitos dos projetos populares foram criados há **vários anos**. Isso indica que repositórios bem estabelecidos têm mais chances de ganhar popularidade.

### **Hipótese 2: Repositórios populares recebem muitas contribuições externas**

🔹 O gráfico de **Pull Requests** mostra que a maioria dos repositórios possui um alto número de contribuições externas, mas apenas um pequeno grupo tem valores extremamente altos.

### **Hipótese 3: Repositórios populares lançam releases com frequência**

🔹 O gráfico de **Releases** indica que, embora muitos repositórios lançem releases regularmente, nem todos seguem um padrão rígido de lançamento.

### **Hipótese 4: Repositórios populares são atualizados com frequência**

🔹 A maioria dos repositórios tem **atualizações recentes**, sugerindo que projetos populares continuam sendo mantidos.

### **Hipótese 5: Linguagens populares dominam os repositórios mais famosos**

🔹 O gráfico de **Linguagens mais usadas** mostra que a maioria dos repositórios populares é escrita em **Python, JavaScript, TypeScript e C++**, indicando que essas linguagens possuem uma grande comunidade de desenvolvedores.

### **Hipótese 6: Repositórios populares possuem um alto percentual de issues fechadas**

🔹 A distribuição das **issues fechadas** mostra que muitos repositórios possuem um percentual superior a **80%**, sugerindo que a comunidade e os mantenedores estão ativos na resolução de problemas.

---

## **4. Conclusão**

Os resultados indicam que:
✅ A maioria dos repositórios populares é **antiga e bem estabelecida**.
✅ **A maioria recebe muitas contribuições**, mas um pequeno grupo tem um volume extremamente alto.
✅ **As releases não são tão frequentes quanto esperado**.
✅ **A maioria dos projetos é frequentemente atualizada**.
✅ **As linguagens mais populares dominam os repositórios mais famosos**.
✅ **Os repositórios populares geralmente possuem alto percentual de issues fechadas**.

