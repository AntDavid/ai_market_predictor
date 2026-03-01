<div align="center">

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
  <img src="https://img.shields.io/badge/Yahoo%20Finance-6001D2?style=for-the-badge&logo=yahoo&logoColor=white" alt="yfinance" />

  <br /><br />

  <h1>📈 AI Market Predictor</h1>

  <p><em>Previsão e Monitorização Inteligente de Ativos Financeiros.</em></p>
  <p>Uma plataforma interativa para análise técnica, simulação de portfólios e projeções de mercado em tempo real.</p>

  <br />

  <img src="https://img.shields.io/github/last-commit/AntDavid/ai_market_predictor?style=flat-square&color=4CAF50" alt="Last Commit" />
  <img src="https://img.shields.io/github/stars/AntDavid/ai_market_predictor?style=flat-square&color=FFD700" alt="Stars" />
  <img src="https://img.shields.io/badge/status-active-brightgreen?style=flat-square" alt="Status" />

</div>

<br />

---

## 🚀 Sobre o Projeto

O **AI Market Predictor** é uma evolução do projeto *Assets Sentry*, redesenhado para oferecer uma experiência de utilizador premium no monitoramento do mercado financeiro.

A aplicação resolve problemas críticos de **persistência de sessão em ambientes Streamlit**, garantindo que o investidor permaneça conectado mesmo após atualizações de página (F5).

<br />

### 💎 Funcionalidades Principais

| Feature | Descrição |
|---|---|
| 📊 **Dashboard Preditivo** | Análise técnica detalhada via API do Yahoo Finance |
| 💼 **Simulador de Portfólio** | Ferramenta de alocação de ativos para testes de estratégia |
| 🔐 **Persistência Avançada** | Login com *CookieManager* — sessão mantida por 30 minutos |
| 🧭 **Navegação Fluida** | Interface *Wide* com roteamento dinâmico entre abas |

<br />

---

## 🛠️ Tecnologias e Arquitetura

<table>
  <tr>
    <td align="center"><b>🐍 Backend</b></td>
    <td>Python 3.10+, SQLite</td>
  </tr>
  <tr>
    <td align="center"><b>🎨 Frontend</b></td>
    <td>Streamlit, Plotly, CSS Customizado</td>
  </tr>
  <tr>
    <td align="center"><b>📉 Finance Data</b></td>
    <td>yfinance, Pandas, NumPy</td>
  </tr>
  <tr>
    <td align="center"><b>🔒 Segurança</b></td>
    <td>Extra Streamlit Components (Cookies)</td>
  </tr>
</table>

<br />

---

## 📂 Estrutura de Pastas

```text
ai_market_predictor/
│
├── app.py              # Lógica principal e gestão de cookies
├── database.db         # Banco de dados SQLite
├── requirements.txt    # Dependências do sistema
│
├── utils/              # Conexão DB e funções auxiliares
│   └── db.py
│
└── views/              # Telas da aplicação
    ├── login.py
    ├── dashboard.py
    └── simulator.py
```

<br />

---

## 🔧 Instalação Local

### 1. Clonar e Acessar

```bash
git clone https://github.com/AntDavid/ai_market_predictor.git
cd ai_market_predictor
```

### 2. Ambiente Virtual e Dependências

```bash
python -m venv venv

# No Windows:
.\venv\Scripts\Activate.ps1

# No Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Executar

```bash
streamlit run app.py
```

<br />

---

## 🌐 Deploy & Secrets

Para rodar no **Streamlit Cloud**, configure o arquivo de Segredos no painel da plataforma:

```toml
# .streamlit/secrets.toml
DATABASE_URL = "database.db"
```

<br />

---

## 🗺️ Roadmap

- [x] Login com persistência de cookies *(F5 fix)*
- [x] Integração completa com Yahoo Finance
- [x] Simulador de portfólio interativo
- [ ] Modelos de ML para previsão de tendência *(LSTM)*
- [ ] Alertas automatizados via e-mail
- [ ] Suporte a múltiplos utilizadores

<br />

---

## 📜 Script de Setup Rápido

```bash
#!/bin/bash
# setup.sh — Configuração automática do ambiente

echo "📦 Clonando repositório..."
git clone https://github.com/AntDavid/ai_market_predictor.git
cd ai_market_predictor

echo "🐍 Criando ambiente virtual..."
python -m venv venv
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\Activate.ps1  # Windows

echo "📥 Instalando dependências..."
pip install -r requirements.txt

echo "🚀 Iniciando aplicação..."
streamlit run app.py
```

<br />

---

<div align="center">
  <p>Desenvolvido por <a href="https://github.com/AntDavid"><b>António David</b></a></p>
  <sub>© 2025 AI Market Predictor — Todos os direitos reservados.</sub>
</div>
