import streamlit as st

def landing_page():
    st.title(" AI Market Predictor")
    st.markdown("### Preveja tendências do mercado financeiro com Inteligência Artificial.")
    
    st.write("""
    A plataforma de nível institucional para simulação e análise.
    -  **Histórico:** Analise dezenas de ativos globais.
    -  **IA Preditiva:** Modelos de Machine Learning para estimar tendências futuras e backtesting.
    -  **Simulador Preditivo:** Teste estratégias e conversão de câmbio sem risco.
    """)
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Acessar o Sistema (Login)", use_container_width=True, type="primary"):
            st.session_state["page"] = "Login"
            st.rerun()
    with col2:
        if st.button("Criar minha Conta", use_container_width=True):
            st.session_state["page"] = "Signup"
            st.rerun()