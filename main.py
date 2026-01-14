import streamlit as st
import pandas as pd
import numpy as np

# Page Config for Dark Theme
st.set_page_config(page_title="Sentinel-X Hub", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR DARK MAP & THEME ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #1a1c24; }
    </style>
    """, unsafe_allow_html=True)

if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- SYSTEM ACCESS ---
if not st.session_state["logged"]:
    st.sidebar.title("🔒 Sentinel-X Access")
    action = st.sidebar.selectbox("Action", ["Login", "Signup"])
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Execute"):
        st.session_state["logged"] = True
        st.rerun()
else:
    # --- FOUNDER SIDEBAR ---
    st.sidebar.markdown("## 👑 Solo Founder")
    st.sidebar.markdown("**ISMAIL: The Sentinel X**")
    st.sidebar.markdown("---")
    
    page = st.sidebar.selectbox("Command Center", ["Intelligence Hub", "Global Map", "Threat Tracker"])
    
    if st.sidebar.button("Logout"):
        st.session_state["logged"] = False
        st.rerun()

    # --- MAIN DASHBOARD ---
    if page == "Intelligence Hub":
        st.title("🧠 SENTINEL-X AI BRAIN")
        st.info("System Analysis: Scanning Global News & Satellite Data...")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("AI Risk Report")
            st.metric(label="Global Threat Level", value="24%", delta="-2%")
            st.write("AI Suggestion: Monitoring Active Nodes in India Region.")
        with col2:
            st.subheader("System Health")
            st.success("🟢 Neural Core: ACTIVE")
            st.success("🟢 Security Protocols: ENCRYPTED")

    elif page == "Global Map":
        st.title("🛡️ GLOBAL SURVEILLANCE")
        st.write("Current Surveillance Nodes (Red Dots represent Active Interceptors)")
        # Map Data
        map_data = pd.DataFrame(
            np.random.randn(100, 2) / [20, 20] + [20.59, 78.96],
            columns=['lat', 'lon']
        )
        st.map(map_data, use_container_width=True)

    elif page == "Threat Tracker":
        st.title("🚨 LIVE THREAT ALERTS")
        st.error("Cyber Attack Blocked: IP 192.168.1.1")
        st.warning("Attempted Data Breach: North Server Cluster")
