import psycopg2
import streamlit as st
from werkzeug.security import generate_password_hash, check_password_hash

def create_connection():
    try:
        return psycopg2.connect(st.secrets["DATABASE_URL"])
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def init_db():
    conn = create_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
            """)
        conn.commit()
        conn.close()

def add_user(name, email, username, password):
    conn = create_connection()
    if not conn:
        return False
        
    hashed_pwd = generate_password_hash(password)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s)",
                (name, email, username, hashed_pwd)
            )
        conn.commit()
        return True
    except psycopg2.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    conn = create_connection()
    if not conn:
        return False
        
    with conn.cursor() as cursor:
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
    conn.close()
    
    if user and check_password_hash(user[0], password):
        return True
    return False


def get_user_name(username):
    conn = create_connection()
    if not conn:
        return "Investidor"
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT name FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
        return user[0] if user else "Investidor"
    finally:
        conn.close()