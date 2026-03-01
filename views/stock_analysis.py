import streamlit as st
import datetime as dt
from utils.finance import download_stock_data, calculate_metrics, GLOBAL_STOCKS, get_exchange_rates
from utils.ai_model import predict_future_trend

def stock_analysis():
    st.title('📈 Análise de Mercado e Previsão IA')
    
    rates = get_exchange_rates()
    st.markdown(f"**💱 Câmbio Atual:** USD/BRL: `R$ {rates['USD_BRL']:.2f}` | EUR/BRL: `R$ {rates['EUR_BRL']:.2f}` | EUR/USD: `$ {rates['EUR_USD']:.2f}`")
    st.divider()

    end_date = dt.date.today()
    start_date = dt.date(end_date.year - 1, end_date.month, end_date.day)
    
    c_regiao, c_ativo, c_start, c_end = st.columns([1.5, 1.5, 1, 1])

    with c_regiao:
        regiao = st.selectbox("Mercado / Categoria:", options=list(GLOBAL_STOCKS.keys()))
    
    with c_ativo:
        if regiao == "🔍 Outro (Pesquisa Livre)":
            selected_stock = st.text_input("Digite o Ticker (Ex: DIS, INTC):", value="DIS").upper()
        else:
            opcoes_limpas = [opt.split(' ')[0] for opt in GLOBAL_STOCKS[regiao]]
            selected_stock = st.selectbox("Selecione o Ativo:", options=opcoes_limpas)
            
    with c_start:
        selected_start_date = st.date_input("Data Inicial:", start_date)
    with c_end:
        selected_end_date = st.date_input("Data Final:", end_date)

    if selected_stock:
        dataframe = download_stock_data(selected_stock, selected_start_date, selected_end_date)

        if not dataframe.empty:
            last_update, last_quote, first_quote, min_quote, max_quote, change = calculate_metrics(dataframe)

            is_brl = "BRL" in regiao or "Brasil" in regiao
            is_eur = "Europa" in regiao
            moeda_simbolo = "R$" if is_brl else ("€" if is_eur else "$")

            if is_brl:
                usd_last, usd_max, usd_min = last_quote / rates['USD_BRL'], max_quote / rates['USD_BRL'], min_quote / rates['USD_BRL']
            elif is_eur:
                usd_last, usd_max, usd_min = last_quote * rates['EUR_USD'], max_quote * rates['EUR_USD'], min_quote * rates['EUR_USD']
            else:
                usd_last, usd_max, usd_min = last_quote, max_quote, min_quote

            st.markdown("### Métricas do Período")
            c1, c2, c3 = st.columns(3)
            
            with c1:
                st.metric(f"Última Atualização ({last_update})", f"{moeda_simbolo} {last_quote:,.2f}", f"{change}%")
                if moeda_simbolo != "$": st.caption(f"🇺🇸 Em Dólar: **$ {usd_last:,.2f}**")
                
            with c2:
                st.metric("Maior Preço", f"{moeda_simbolo} {max_quote:,.2f}")
                if moeda_simbolo != "$": st.caption(f"🇺🇸 Em Dólar: **$ {usd_max:,.2f}**")
                
            with c3:
                st.metric("Menor Preço", f"{moeda_simbolo} {min_quote:,.2f}")
                if moeda_simbolo != "$": st.caption(f"🇺🇸 Em Dólar: **$ {usd_min:,.2f}**")

            st.markdown("### Projeção de Tendência")
            comparar_realidade = st.toggle("🔍 Testar IA contra dados reais (Backtest dos últimos 30 dias)")
            
            with st.spinner('Analisando padrões matemáticos...'):
                if comparar_realidade:
                    predictive_df = predict_future_trend(dataframe, days_to_predict=30, backtest=True)
                    if predictive_df is not None:
                        st.info("A IA previu os últimos 30 dias às cegas. Linha Verde = Mercado Real, Linha Laranja = Previsão IA.")
                        st.line_chart(predictive_df, color=["#1f77b4", "#ff7f0e", "#2ca02c"])
                    else:
                        st.warning("Dados insuficientes para fazer o teste.")
                else:
                    predictive_df = predict_future_trend(dataframe, days_to_predict=30, backtest=False)
                    st.line_chart(predictive_df, color=["#1f77b4", "#ff7f0e"])
                
        else:
            st.error("Dados não encontrados para esta pesquisa.")