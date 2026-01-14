import streamlit as st
import sqlite3
import hashlib
from datetime import datetime

# Database logic
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, password TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS waitlist (email TEXT UNIQUE, joined_at TIMESTAMP)')
conn.commit()

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Branding & Page Config
st.set_page_config(page_title="Sentinel-X Hub", layout="wide")

# Sidebar - Login/Founder Section
if "logged" not in st.session_state:
    st.session_state["logged"] = False

if not st.session_state["logged"]:
    st.sidebar.title("🔐 Sentinel-X Access")
    choice = st.sidebar.selectbox("Action", ["Login", "Signup"])
    email = st.sidebar.text_input("Email")
    pw = st.sidebar.text_input("Password", type="password")
    
    if choice == "Signup" and st.sidebar.button("Create Account"):
        try:
            c.execute("INSERT INTO users VALUES (?,?)", (email, hash_pass(pw)))
            conn.commit()
            st.sidebar.success("Account Created!")
        except: st.sidebar.error("User exists")
    
    if choice == "Login" and st.sidebar.button("Login"):
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hash_pass(pw)))
        if c.fetchone():
            st.session_state["logged"] = True
            st.rerun()
        else: st.sidebar.error("Invalid Credentials")
else:
        st.sidebar.markdown("## 👑 Solo Founder")
    st.sidebar.markdown("**ISMAIL: The Sentinel X**")
    st.sidebar.markdown("---")

    page = st.sidebar.selectbox("Command Center", ["Global Map", "Threat Tracker"])

    if st.sidebar.button("Logout"):
        st.session_state["logged"] = False
        st.rerun()

    if page == "Global Map":
        st.title("🛡️ SENTINEL-X SURVEILLANCE")
        import pandas as pd
        import numpy as np
        map_data = pd.DataFrame(np.random.randn(50, 2) / [10, 10] + [20.59, 78.96], columns=['lat', 'lon'])
        st.map(map_data)
    
    elif page == "Threat Tracker":
        st.title("🚨 LIVE THREAT ALERTS")
        st.error("Cyber Attack Blocked: IP 192.168.1.1")
