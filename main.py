import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config - Bright & Professional
st.set_page_config(page_title="SENTINEL-X EMPIRE", layout="wide")

# 2. Custom CSS - WHITE & BRIGHT THEME
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #000000; }
    .stButton>button { background-color: #007BFF; color: white; border-radius: 5px; width: 100%; border: none; font-weight: bold; }
    .stMetric { background-color: #F8F9FA; border: 1px solid #DEE2E6; padding: 15px; border-radius: 8px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    .news-card { border-bottom: 1px solid #EEE; padding: 10px; cursor: pointer; }
    </style>
    """, unsafe_allow_html=True)

if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- 3. THE GUARD (Login Screen) ---
if not st.session_state["logged"]:
    st.title("🛡️ SENTINEL-X: THE GLOBAL EMPIRE")
    st.markdown("### SYSTEM STATUS: **READY FOR AUTHORIZATION**")
    
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        st.info("Authorized Personnel Only")
        id_user = st.text_input("FOUNDER ID")
        key_user = st.text_input("EMPIRE ACCESS KEY", type="password")
        if st.button("BLUE SCAN: AUTHORIZE SYSTEM"): # The Blue Button you wanted
            if id_user and key_user:
                st.session_state["logged"] = True
                st.rerun()
else:
    # --- 4. THE EMPIRE HUB (Main Dashboard) ---
    st.sidebar.title("🛡️ SENTINEL-X")
    st.sidebar.success(f"ONLINE: FOUNDER ISMAIL")
    st.sidebar.divider()
    page = st.sidebar.radio("Command Center", ["Global Intelligence", "Surveillance Map", "Security Logs"])

    if page == "Global Intelligence":
        st.title("🧠 NEURAL NETWORK & SYSTEM HEALTH")
        
        # Performance Cards
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.metric("Global Threat", "24%", "-2%")
        with c2: 
            st.write("💿 **Storage Capacity**")
            st.progress(65)
        with c3: 
            st.write("🔋 **System Health**")
            st.progress(98)
        with c4: st.metric("Active Nodes", "50+", "Live")

        st.divider()
        st.subheader("📡 Global News Feed (Clickable Analysis)")
        # 50 Clickable News Lines
        for i in range(1, 51):
            with st.expander(f"🔴 Node-X{i}: Satellite Stream Intercepted"):
                st.write(f"Empire Analysis: Data packet from Sector-{i} is SECURE. No threats detected.")

    elif page == "Surveillance Map":
        st.title("🌍 WORLD SURVEILLANCE SCANNER")
        # Global Spread Map
        map_data = pd.DataFrame({
            'lat': np.random.uniform(-50, 70, 200),
            'lon': np.random.uniform(-160, 160, 200)
        })
        st.map(map_data)
        st.caption("Tracking 200+ Active Empire Nodes Globally.")

    if st.sidebar.button("Logout"):
        st.session_state["logged"] = False
        st.rerun()
