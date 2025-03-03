# **Relatório Final - Lab01S03**

## **1. Introdução**

Este relatório apresenta a última etapa do projeto, **Lab01S03**, que tem como objetivo realizar uma análise aprofundada e visualização dos dados coletados sobre os **1000 repositórios mais populares do GitHub**. Além disso, este documento consolida os achados das etapas anteriores e organiza os resultados finais da pesquisa.

---

## **2. Metodologia**

### **2.1 Coleta e Processamento de Dados**

Os dados foram coletados por meio da **API GraphQL do GitHub**, utilizando um critério de popularidade baseado na quantidade de estrelas (**stars > 10.000**). Devido a restrições da API, foi aplicada uma estratégia de **paginação** para coletar **1000 repositórios** em lotes de **20 por requisição**, garantindo que não ocorressem erros como **502 (Bad Gateway)**.

Após a coleta, os dados foram processados para extrair as seguintes métricas:
- **Idade do repositório (anos)**
- **Número total de Pull Requests aceitos**
- **Número total de Releases**
- **Tempo desde a última atualização (dias)**
- **Linguagem principal do repositório**
- **Total de Issues e percentual de Issues fechadas**

Os dados coletados foram armazenados nos seguintes arquivos:
- **Dados brutos**: `data/repositories.csv`
- **Dados processados**: `data/processed_repositories.csv`

### **2.2 Visualização de Dados**
Para facilitar a análise, foram gerados gráficos que ilustram os principais aspectos dos repositórios populares no GitHub. Estes gráficos foram produzidos usando a biblioteca **Matplotlib** e representam padrões e tendências identificadas nos dados.

Os seguintes gráficos foram criados:

1. **Distribuição da Idade dos Repositórios** (`repo_age.png`)
2. **Distribuição de Pull Requests** (`pull_requests.png`)
3. **Distribuição de Releases** (`releases.png`)
4. **Tempo desde a última atualização** (`update_days.png`)
5. **Percentual de Issues Fechadas** (`closed_issues.png`)
6. **Linguagens mais usadas** (`languages.png`)

A seguir, cada um desses gráficos será analisado em detalhes.

---

## **3. Análise dos Dados e Resultados**

### **3.1 Idade dos Repositórios**
![Idade dos Repositórios](repo_age.png)

🔹 A maioria dos repositórios populares tem vários anos de existência. Isso indica que **repositórios bem estabelecidos tendem a ser mais populares**, possivelmente devido ao tempo necessário para ganhar tração na comunidade.

### **3.2 Contribuições via Pull Requests**
![Distribuição de Pull Requests](pull_requests.png)

🔹 A distribuição mostra que **a maioria dos repositórios recebe um volume moderado de contribuições**, enquanto um pequeno grupo tem um número extremamente alto de Pull Requests.

### **3.3 Frequência de Releases**
![Distribuição de Releases](releases.png)

🔹 Nem todos os repositórios populares lançam releases frequentemente. **Enquanto alguns projetos têm centenas de releases, a maioria fica abaixo de 100**.

### **3.4 Tempo desde a Última Atualização**
![Tempo desde a Última Atualização](update_days.png)

🔹 O tempo desde a última atualização mostra que **grande parte dos repositórios é mantida ativamente**, sendo atualizada com frequência.

### **3.5 Percentual de Issues Fechadas**
![Percentual de Issues Fechadas](closed_issues.png)

🔹 Um grande número de repositórios tem mais de **80% das issues fechadas**, o que indica **uma comunidade ativa e um bom suporte ao usuário**.

### **3.6 Linguagens mais Utilizadas**
![Linguagens Mais Usadas](languages.png)

🔹 As linguagens mais comuns nos repositórios populares são **Python, JavaScript, TypeScript e C++**, mostrando que esses ecossistemas possuem forte adoção e suporte da comunidade.

---

## **4. Conclusão**

Os resultados desta análise indicam que:
✅ **Repositórios populares tendem a ser antigos**, pois precisam de tempo para ganhar reconhecimento.
✅ **A maioria recebe muitas contribuições via Pull Requests**, mas apenas alguns possuem um volume extremamente alto.
✅ **Lançamento de releases não é um fator determinante para popularidade** – alguns projetos lançam frequentemente, outros não.
✅ **A maioria dos repositórios é frequentemente atualizada**, mostrando manutenção ativa.
✅ **A alta taxa de fechamento de issues indica boa governança e suporte comunitário.**
✅ **Python, JavaScript e C++ são as linguagens predominantes entre os projetos populares.**

Essa análise final consolida as descobertas das etapas anteriores e responde às principais perguntas levantadas sobre os repositórios mais populares do GitHub.

---

## **5. Considerações Finais**

Este relatório encerra o **Lab01S03**, concluindo a análise de repositórios populares do GitHub. O estudo demonstrou a relação entre popularidade, tempo de existência, colaboração da comunidade e linguagens utilizadas. Os resultados obtidos podem servir como base para futuras pesquisas sobre o ecossistema de desenvolvimento open-source.

Com isso, todas as etapas do laboratório foram concluídas com sucesso! 

