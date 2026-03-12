# F109 - Ferramentas para Ciência de Dados

## 📋 Sobre o Projeto

Este é um projeto de demonstração para a disciplina de Ferramentas de Data Science (F109). O objetivo é demonstrar o uso de ferramentas modernas de ciência de dados para carregar, processar, visualizar e analisar dados de e-commerce utilizando Python, Streamlit e Docker.

O projeto utiliza o dataset público **Olist Brazilian E-Commerce**, que contém informações sobre pedidos, clientes, produtos, pagamentos e avaliações de uma plataforma de e-commerce brasileira.

## 🚀 Tecnologias Utilizadas

- **Python 3.12** - Linguagem de programação
- **Streamlit** - Framework para criação de aplicações web interativas
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Computação numérica
- **Scikit-learn** - Machine learning e processamento de dados
- **Matplotlib/Seaborn/Plotly** - Visualização de dados
- **Docker** - Containerização da aplicação
- **Jupyter** - Notebooks para análise exploratória

## 📁 Estrutura do Projeto

```
f109-ferramentas-ds/
├── app.py                  # Aplicação principal Streamlit
├── data/                   # Datasets (CSV files)
├── utils/                  # Módulos utilitários
│   ├── data_processing.py  # Funções de processamento de dados
│   └── data_loading.py     # Funções de carregamento de dados
├── notebooks/              # Jupyter notebooks para análise
├── Dockerfile             # Configuração da imagem Docker
├── docker-compose.yml     # Orquestração dos containers
├── requirements.txt       # Dependências Python
└── README.md             # Este arquivo
```

## 🐳 Como Executar com Docker Compose

### Pré-requisitos

- Docker instalado ([Download Docker](https://www.docker.com/get-started))
- Docker Compose instalado (geralmente já vem com Docker Desktop)

### Passo a Passo

1. **Clone o repositório** (se ainda não tiver feito):
```bash
git clone <url-do-repositorio>
cd f109-ferramentas-ds
```

2. **Construa e inicie os containers**:
```bash
docker compose up --build
```

3. **Acesse a aplicação**:
   - Streamlit: [http://localhost:8501](http://localhost:8501)
   - Jupyter Notebook (opcional): [http://localhost:8888](http://localhost:8888)

4. **Para parar a aplicação**:
```bash
# Pressione Ctrl+C no terminal ou em outro terminal execute:
docker compose down
```