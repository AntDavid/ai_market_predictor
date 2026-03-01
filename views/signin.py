import streamlit as st
from utils.db import verify_user
import datetime

def login(cookie_manager):
    _, col, _ = st.columns([1, 1.2, 1])
    
    with col:
        st.title("Sign In")
        
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Sign In", use_container_width=True)
            
        if submit:
            if verify_user(username, password):
                validade = datetime.datetime.now() + datetime.timedelta(minutes=5)
                cookie_manager.set("auth_user", username, expires_at=validade)
                
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.rerun()
            else:
                st.error("Invalid username or password")
                
        if st.button("Create an account", use_container_width=True):
            st.session_state["page"] = "Signup"
            st.rerun()