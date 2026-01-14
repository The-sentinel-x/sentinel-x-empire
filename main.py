import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Sentinel-X Hub", layout="wide")

# Simple Database Simulation
if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- LOGIN / SIGNUP SYSTEM ---
if not st.session_state["logged"]:
    st.sidebar.title("🔒 Sentinel-X Access")
    action = st.sidebar.selectbox("Action", ["Login", "Signup"])
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Execute"):
        st.session_state["logged"] = True
        st.rerun()
else:
    # --- LOGGED IN CONTENT (Founder Dashboard) ---
    st.sidebar.markdown("## 👑 Solo Founder")
    st.sidebar.markdown("**ISMAIL: The Sentinel X**")
    st.sidebar.markdown("---")

    # Command Center Dropdown
    page = st.sidebar.selectbox("Command Center", ["Global Map", "Threat Tracker", "Intelligence Feed"])

    if st.sidebar.button("Logout"):
        st.session_state["logged"] = False
        st.rerun()

    # --- MAIN HUB DASHBOARD ---
    if page == "Global Map":
        st.title("🛡️ SENTINEL-X GLOBAL SURVEILLANCE")
        map_data = pd.DataFrame(np.random.randn(50, 2) / [10, 10] + [20.59, 78.96], columns=['lat', 'lon'])
        st.map(map_data)
        st.success("Tracking 50+ Global Nodes... All Systems Green.")

    elif page == "Threat Tracker":
        st.title("🚨 LIVE THREAT ALERTS")
        st.error("Cyber Attack Blocked: IP 192.168.1.1 (Security Level: HIGH)")
        st.warning("Unauthorized Access Attempt: North Server - Intercepted.")

    elif page == "Intelligence Feed":
        st.title("📊 SENTINEL INTELLIGENCE")
        st.write("Current Global Risk Level: **LOW**")
        st.progress(15)
