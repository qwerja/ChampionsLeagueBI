Champions League BI - Power BI Dashboard  
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=black)  

Bem-vindo ao repositório do projeto de análise de dados da **Champions League**, desenvolvido como parte do portfólio de Lucca Ferreira Marques. Este projeto utiliza Power BI para explorar insights estratégicos sobre times, estádios, público e desempenho ao longo de duas décadas (2003-2024).  

---

## ✨ Funcionalidades Principais  
- **Dashboards Dinâmicos:** Visualizações interativas de KPIs como valor do elenco, idade média, convocações e análise de público.  
- **Seleção de Equipes:** Filtragem em tempo real para explorar métricas específicas de cada time (estádio, valor do elenco, gols, público médio).  
- **Análise de Público:** Detecção de padrões de audiência por estádio, temporada, mês e horário.  
- **Modelagem Star Schema:** Estrutura otimizada para performance e clareza com tabelas fato e dimensão.  
- **Web Scraping:** Automação com Python para coleta de logos de times e estádios.  

---

## 🛠️ Tecnologias e Conceitos  
**Ferramentas:**  
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=flat&logo=Power%20BI&logoColor=black)
![Google BigQuery](https://img.shields.io/badge/GoogleBigQuery-4285F4?style=flat&logo=google-cloud&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)  

**Modelagem de Dados:**  
- ETL (Extract, Transform, Load)  
- Staging Area e Data Mart  
- Star Schema (Tabela Fato: `Fact_Performance`, Dimensões: `Dim_Teams`, `Dim_Stadiums`)  

**Bibliotecas Python:**  
- `Pandas` para manipulação de dados  
- `BeautifulSoup` para web scraping de imagens  

---

## 📥 Instalação e Uso  
1. **Clone o repositório:**  
   ```bash  
   git clone https://github.com/qwerja/ChampionsLeagueBI.git  
Abra o arquivo Champions League Projeto.pbix no Power BI Desktop (requer instalação prévia).

Explore os dashboards:

Geral: Visão macro dos dados históricos.

Equipe: Análise detalhada por time.

Público: Comportamento do público em diferentes contextos.


📚 Documentação
Para detalhes técnicos, consulte a Documentação Completa.


Abordagem de Storytelling: Definição de problemas, objetivos e narrativa visual.

ETL: Processo de limpeza, transformação e modelagem no Power Query.

Limitações: Base de dados com informações parcialmente estáticas (2003-2024).



📄 Licença
Este projeto está sob licença MIT. Veja o arquivo LICENSE para detalhes.

Desenvolvido com  por Lucca Ferreira Marques.
