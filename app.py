import streamlit as st
import extra_streamlit_components as stx
from utils.db import init_db, get_user_name
import datetime
import time

st.set_page_config(page_title="AI Market Predictor", page_icon="📈", layout="wide", initial_sidebar_state="collapsed")

st.markdown("<style>header {display:none;} [data-testid='stSidebar'] {display:none;} .block-container {padding-top:1.5rem;}</style>", unsafe_allow_html=True)

init_db()

cookie_manager = stx.CookieManager(key="cookie_manager_v8")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "Landing"
if "aba_atual" not in st.session_state:
    st.session_state["aba_atual"] = "Dashboard"

if not st.session_state["authenticated"]:
    auth_user_cookie = cookie_manager.get(cookie="auth_user")
    
    if auth_user_cookie:
        st.session_state["authenticated"] = True
        st.session_state["username"] = auth_user_cookie
        st.session_state["aba_atual"] = "Dashboard"
        st.rerun()


if st.session_state["authenticated"]:
    nome_completo = get_user_name(st.session_state.get("username", ""))
    primeiro_nome = nome_completo.split()[0] if nome_completo else "Investidor"

    c_dash, c_sim, c_space, c_user, c_sair = st.columns([2.5, 2.5, 3.5, 2.5, 1.2])
    
    with c_dash:
        if st.button("📈 Dashboard Preditivo", use_container_width=True, type="primary" if st.session_state["aba_atual"] == "Dashboard" else "secondary"):
            st.session_state["aba_atual"] = "Dashboard"; st.rerun()
    with c_sim:
        if st.button("🧮 Simulador Preditivo", use_container_width=True, type="primary" if st.session_state["aba_atual"] == "Simulador" else "secondary"):
            st.session_state["aba_atual"] = "Simulador"; st.rerun()
            
    with c_user:
        st.markdown(f"<div style='text-align:right; padding-top:8px;'>👤 Olá, <b>{primeiro_nome}</b></div>", unsafe_allow_html=True)
    
    with c_sair:
        if st.button("🚪 Sair", use_container_width=True):
            cookie_manager.set("auth_user", "", expires_at=datetime.datetime(2000, 1, 1))
            st.session_state.clear()
            st.rerun()

    st.divider()
    if st.session_state.get("aba_atual") == "Simulador":
        from views.wallet import wallet; wallet()
    else:
        from views.stock_analysis import stock_analysis; stock_analysis()

else:
    if st.session_state["page"] == "Landing":
        from views.landing import landing_page
        landing_page()
    elif st.session_state["page"] == "Login":
        from views.signin import login
        login(cookie_manager)
    elif st.session_state["page"] == "Signup":
        from views.signup import signup
        signup()