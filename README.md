📊 Análise de Dados das 100 Cidades Mais Populosas do Mundo

Projeto em Python para análise de dados das 100 cidades mais populosas do mundo.
A aplicação permite carregar uma planilha com os dados das cidades, calcular a densidade demográfica, identificar as cidades mais densas e gerar gráficos para visualização dos dados.

O objetivo do projeto é praticar manipulação de dados com Pandas, visualização com Matplotlib e organização de código em módulos Python.



🚀 Funcionalidades

✔ Carregamento de planilha com dados das cidades
✔ Renomeação das colunas para português
✔ Cálculo da densidade demográfica (habitantes por km²)
✔ Listagem das cidades mais densas
✔ Geração de gráficos de análise

📈 Exemplos de Gráficos

O projeto gera gráficos utilizando Matplotlib, como:

Ranking das cidades mais densas

Comparação de densidade populacional


🗂 Estrutura do Projeto
```bash
analise-dados-100-cidades-mais-populosas
│
├── data/
│   └── Top 100 Worlds Largest Cities.xlsx
│
├── src/
│   ├── analise.py
│   └── loader.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

🛠 Tecnologias Utilizadas

```bash
Python
Pandas
Matplotlib
```

⚙️ Como Executar o Projeto
1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/analise-dados-100-cidades-mais-populosas.git
```

2️⃣ Entrar na pasta do projeto
```bash
cd analise-dados-100-cidades-mais-populosas
```


3️⃣ Criar ambiente virtual (opcional)
```bash
python -m venv venv
```

Ativando ambiente virtual:
```bash
Windows

    venv\Scripts\activate

Linux/Mac

    source venv/bin/activate

```

4️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

5️⃣ Executar o projeto
```bash
python main.py
```

## 📖 Como Usar

Ao executar `main.py`, o programa apresenta um **menu interativo** no terminal.

O usuário pode escolher entre as opções disponíveis para realizar diferentes análises dos dados das cidades, como:

- Visualizar resumo da tabela
- Calcular densidade demográfica
- Listar cidades mais densas
- Gerar gráficos