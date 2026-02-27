
# 🛡️ Assets Sentry

> 🚧 **Status:** Em desenvolvimento (Work in Progress)

**Assets Sentry** é um dashboard interativo focado no monitoramento e análise de ativos do mercado financeiro. A aplicação permite rastrear dados históricos de ações, calcular métricas de desempenho em tempo real e visualizar a evolução das cotações de forma simples e organizada.

---

## 🚀 Tecnologias e Arquitetura

Este projeto está sendo desenvolvido em Python, utilizando um ecossistema focado em dados e interfaces ágeis:

* **Interface e Dashboard:** [Streamlit](https://streamlit.io/)
* **Dados Financeiros:** `yfinance` (Yahoo Finance API)
* **Manipulação de Dados:** `pandas`
* **Autenticação:** Lógica customizada (`auth.py`)

---

## ⚙️ Estrutura do Repositório

A arquitetura do projeto foi dividida para manter o código limpo e escalável:

* `app.py` - Ponto de entrada do dashboard no Streamlit.
* `finance.py` - Módulo responsável pela extração de dados do Yahoo Finance e cálculo de métricas (cotação máxima, mínima e variação percentual).
* `auth.py` - Controle de acesso e segurança de usuários.
* `pages/` - Telas adicionais e relatórios do dashboard.
* `views/` - Componentes visuais isolados.
* `utils/` - Funções auxiliares.

---

## 🔧 Como Testar Localmente

Siga os passos abaixo para rodar o dashboard na sua máquina:

### 1. Clonar o repositório
~~~bash
git clone https://github.com/AntDavid/assets_sentry.git
cd assets_sentry
~~~

### 2. Criar e ativar o ambiente virtual (Recomendado)
~~~bash
python -m venv venv

# Ativar no Windows:
venv\Scripts\activate

# Ativar no Linux/Mac:
source venv/bin/activate
~~~

### 3. Instalar as dependências
Certifique-se de instalar as bibliotecas principais do projeto:
~~~bash
pip install streamlit pandas yfinance
~~~

### 4. Iniciar o Dashboard
Como a aplicação utiliza o Streamlit, o comando de inicialização é diferente de um script Python comum:
~~~bash
streamlit run app.py
~~~
O seu navegador abrirá automaticamente na página `http://localhost:8501`.

---

## 🗺️ Roadmap (Próximos Passos)

- [x] Extração de dados históricos com `yfinance`.
- [x] Cálculo de métricas e variação percentual de ativos.
- [ ] Construção dos gráficos e tabelas no Streamlit.
- [ ] Integração do sistema de Login (`auth.py`).
- [ ] Cadastro e gestão de portfólios customizados por usuário.

---

## 📄 Licença

Projeto em desenvolvimento.
