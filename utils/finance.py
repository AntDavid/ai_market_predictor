import streamlit as st
import pandas as pd
import yfinance as yf
import requests

# Catálogo Global de Ativos
GLOBAL_STOCKS = {
    "🇧🇷 Brasil (B3)": ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'WEGE3.SA', 'BBAS3.SA', 'MGLU3.SA', 'BOVA11.SA', 'BBDC4.SA', 'RENT3.SA', 'B3SA3.SA', 'SUZB3.SA', 'JBSS3.SA', 'RADL3.SA', 'PRIO3.SA', 'IVVB11.SA'],
    "🇺🇸 EUA (Tech & Growth)": ['AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'AMD', 'INTC'],
    "🇺🇸 EUA (S&P 500)": ['JNJ', 'JPM', 'V', 'PG', 'MA', 'HD', 'CVX', 'MRK', 'KO', 'PEP', 'MCD', 'WMT'],
    "🇪🇺 Europa (Blue Chips)": ['MC.PA', 'ASML.AS', 'SAP.DE', 'NVO', 'SIE.DE', 'SAN.MC', 'OR.PA', 'RACE'],
    "🌏 Ásia & Emergentes": ['TSM', 'BABA', 'TCEHY', 'SONY', 'TM', 'RELIANCE.NS'],
    "🪙 Criptomoedas": ['BTC-USD', 'ETH-USD', 'SOL-USD', 'BNB-USD', 'XRP-USD', 'ADA-USD', 'DOGE-USD'],
    "🌐 Índices Globais (ETFs)": ['SPY', 'QQQ', 'DIA', 'EWZ'],
    "🔍 Outro (Pesquisa Livre)": []
}

@st.cache_data(ttl=3600)
def get_exchange_rates():
    """Busca as cotações reais de câmbio usando a AwesomeAPI."""
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,EUR-USD"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        usd_brl = float(data['USDBRL']['bid'])
        eur_brl = float(data['EURBRL']['bid'])
        eur_usd = float(data['EURUSD']['bid'])
    except Exception as e:
        usd_brl, eur_brl, eur_usd = 0.00, 0.00, 0.00 
        
    return {"USD_BRL": usd_brl, "EUR_BRL": eur_brl, "EUR_USD": eur_usd}

@st.cache_data 
def download_stock_data(stock, start_date, end_date):
    dataframe = yf.download(stock, start=start_date, end=end_date, progress=False)
    
    if not dataframe.empty:
        if isinstance(dataframe.columns, pd.MultiIndex):
            dataframe.columns = dataframe.columns.droplevel(1)
            
        dataframe.reset_index(inplace=True)
        dataframe['Date'] = pd.to_datetime(dataframe['Date']).dt.date
        dataframe.set_index('Date', inplace=True)
        dataframe.index = pd.to_datetime(dataframe.index)
        dataframe.index = dataframe.index.tz_localize(None)
        
    return dataframe

def calculate_metrics(dataframe):
    col_name = 'Close' if 'Close' in dataframe.columns else dataframe.columns[0]
    
    last_update = dataframe.index.max().date()
    last_quote = dataframe[col_name].iloc[-1]
    first_quote = dataframe[col_name].iloc[0]
    min_quote = dataframe[col_name].min()
    max_quote = dataframe[col_name].max()

    change = round(((last_quote - first_quote) / first_quote) * 100, 2) if first_quote != 0 else 0.0
    
    return last_update, last_quote, first_quote, min_quote, max_quote, change