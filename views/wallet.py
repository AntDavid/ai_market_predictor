import streamlit as st
import datetime as dt
from utils.finance import download_stock_data, get_exchange_rates, GLOBAL_STOCKS
from utils.ai_model import predict_future_trend

def wallet():
    st.title("Simulador Preditivo")
    st.info("Descubra a projeção de rendimento de um investimento baseado nos cálculos da Inteligência Artificial.")
    
    rates = get_exchange_rates()
    
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            regiao = st.selectbox("Mercado:", options=list(GLOBAL_STOCKS.keys()), key="sim_regiao")
        with col2:
            if regiao == "🔍 Outro (Pesquisa Livre)":
                ativo = st.text_input("Ticker:", value="AAPL").upper()
            else:
                opcoes_limpas = [opt.split(' ')[0] for opt in GLOBAL_STOCKS[regiao]]
                ativo = st.selectbox("Ativo:", options=opcoes_limpas, key="sim_ativo")
        with col3:
            investimento = st.number_input("Valor Investido (Na Moeda Local do Ativo):", min_value=10.0, value=1000.0, step=100.0)
        with col4:
            dias_futuro = st.slider("Tempo (Dias):", min_value=7, max_value=365, value=30, step=7)

    if st.button("🔮 Calcular Projeção de Lucro", type="primary", use_container_width=True):
        if ativo:
            with st.spinner("Acessando mercado e projetando..."):
                end_date = dt.date.today()
                start_date = end_date - dt.timedelta(days=365)
                df = download_stock_data(ativo, start_date, end_date)
                
                if not df.empty:
                    future_df = predict_future_trend(df, days_to_predict=dias_futuro)
                    
                    preco_atual = df['Close'].iloc[-1]
                    preco_futuro = future_df['Tendência IA'].dropna().iloc[-1]
                    
                    qtd_acoes = investimento / preco_atual
                    valor_final_bruto = qtd_acoes * preco_futuro
                    lucro_percentual = ((preco_futuro - preco_atual) / preco_atual) * 100
                    
                    is_brl = "BRL" in regiao or "Brasil" in regiao
                    is_eur = "EUR" in regiao or "Europa" in regiao
                    moeda_origem = "BRL" if is_brl else ("EUR" if is_eur else "USD")

                    if moeda_origem == "BRL":
                        v_brl, v_usd, v_eur = valor_final_bruto, valor_final_bruto / rates['USD_BRL'], valor_final_bruto / rates['EUR_BRL']
                    elif moeda_origem == "EUR":
                        v_brl, v_usd, v_eur = valor_final_bruto * rates['EUR_BRL'], valor_final_bruto * rates['EUR_USD'], valor_final_bruto
                    else: 
                        v_brl, v_usd, v_eur = valor_final_bruto * rates['USD_BRL'], valor_final_bruto, valor_final_bruto / rates['EUR_USD']

                    st.divider()
                    st.markdown(f"### Resultado da Projeção para **{ativo}** em {dias_futuro} dias:")
                    
                    c_price1, c_price2, c_lucro = st.columns(3)
                    c_price1.metric("Preço Atual", f"{preco_atual:,.2f}")
                    c_price2.metric("Preço Estimado (IA)", f"{preco_futuro:,.2f}")
                    
                    c_lucro.metric("Crescimento Projetado", f"{lucro_percentual:,.2f}%", delta=f"{lucro_percentual:,.2f}%", delta_color="normal")
                    
                    st.markdown("#### Capital Final Convertido (Projeção):")
                    res1, res2, res3 = st.columns(3)
                    res1.info(f"**Reais (BRL)**\nR$ {v_brl:,.2f}")
                    res2.success(f"**Dólar (USD)**\n$ {v_usd:,.2f}")
                    res3.warning(f"**Euro (EUR)**\n€ {v_eur:,.2f}")

                else:
                    st.error("Ativo não encontrado ou dados indisponíveis.")