import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="SENTINEL-X HUB", layout="wide", page_icon="🛡️")

# --- CUSTOM CSS (Professional Look Only) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #ff4b4b; }
    .news-box { background-color: #161b22; padding: 10px; border-radius: 5px; border-left: 3px solid #ff4b4b; margin-bottom: 5px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- LOGIN SCREEN (Restoring Classic Scan Feel) ---
if not st.session_state["logged"]:
    st.title("🛡️ SENTINEL-X GLOBAL SURVEILLANCE")
    st.markdown("### SYSTEM STATUS: **SCANNING FOR FOUNDER...**")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        id_input = st.text_input("ENTER FOUNDER ID")
        key_input = st.text_input("ACCESS KEY", type="password")
        if st.button("AUTHORIZE ACCESS"):
            st.session_state["logged"] = True
            st.rerun()
else:
    # --- CLEAN SIDEBAR ---
    st.sidebar.markdown("# 🛡️ SENTINEL-X")
    st.sidebar.markdown("### ISMAIL: THE FOUNDER")
    st.sidebar.divider()
    page = st.sidebar.radio("Command Menu", ["Intelligence Hub", "World Surveillance", "Security Logs"])
    
    # Logout is now a simple button at the bottom
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        st.session_state["logged"] = False
        st.rerun()

    # --- INTELLIGENCE HUB (Restoring 50+ News & Storage) ---
    if page == "Intelligence Hub":
        st.title("🧠 NEURAL CORE & SYSTEM HEALTH")
        c1, c2 = st.columns([1,1])
        with c1:
            st.write("Disk Storage Used")
            st.progress(65)
        with c2:
            st.metric("Global Threat Level", "24%", "-2%")
        
        st.divider()
        st.subheader("📡 Global Intelligence Stream (50+ Active Nodes)")
        # Real 50 News Lines
        for i in range(1, 51):
            st.markdown(f"<div class='news-box'>Node-{i:02d}: Fetching Encrypted Satellite Stream... [STATUS: SECURE]</div>", unsafe_allow_html=True)

    # --- WORLD MAP (Fixing Dots Spacing) ---
    elif page == "World Surveillance":
        st.title("🌍 GLOBAL INTERCEPTOR MAP")
        # Spreading dots across the WHOLE world
        map_data = pd.DataFrame({
            'lat': np.random.uniform(-60, 80, 200),
            'lon': np.random.uniform(-180, 180, 200)
        })
        st.map(map_data)
        st.caption("Tracking 200+ Active Global Nodes across all continents.")

    # --- LOGS ---
    elif page == "Security Logs":
        st.title("🚨 RECENT INTERCEPTIONS")
        st.table({"Time": ["16:45", "17:10", "18:05"], "Threat": ["Brute Force", "Malware", "DDoS"], "Status": ["BLOCKED", "DELETED", "SHIELDED"]})
