import streamlit as st
from utils.db import add_user

def signup():
    _, col, _ = st.columns([1, 1.5, 1])
    
    with col:
        st.markdown("<h2 style='text-align: center;'>Sign Up</h2>", unsafe_allow_html=True)
        
        with st.form("signup_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Create Account", use_container_width=True)
            
        if submit:
            if add_user(name, email, username, password):
                st.success("Account created successfully! Please log in.")
                st.session_state["page"] = "Login"
                st.rerun()
            else:
                st.error("Username or Email already exists.")
                
        if st.button("Back to Login", use_container_width=True):
            st.session_state["page"] = "Login"
            st.rerun()