
# Projeto de Ciência de Dados com NBA Stats API

Este projeto tem como objetivo realizar análises exploratórias, estatísticas e visuais com dados obtidos da API oficial da NBA (https://documenter.getpostman.com/view/24232555/2s93shzpR3).

## Objetivos

- Coletar dados dinâmicos de jogadores e partidas da NBA
- Analisar estatísticas de desempenho (pontos, assistências, rebotes, etc.)
- Criar visualizações interativas e dashboards
- Identificar padrões e tendências entre jogadores, times e temporadas

## Tecnologias Utilizadas

- Python 3.x
- Requests
- Pandas
- Matplotlib / Seaborn / Plotly
- Jupyter Notebook

## Estrutura

```
nba_stats_api_project/
├── data/                 # Dados salvos localmente
├── notebooks/            # Notebooks exploratórios
├── src/                  # Scripts Python para coleta, processamento e visualização
├── output/plots/         # Gráficos e resultados
└── README.md
```

## Primeiros Passos

1. Instale as dependências:

```
pip install requests pandas matplotlib seaborn plotly
```

2. Execute o script de coleta de dados em `src/api_request.py`

## Possíveis Expansões

- Comparação entre jogadores por temporada
- Evolução de estatísticas por time
- Previsão de desempenho futuro com machine learning
- Dashboard interativo com Streamlit ou Dash

## Licença

MIT License
