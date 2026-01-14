import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config - Wahi classic feel
st.set_page_config(page_title="SENTINEL-X", layout="wide")

# 2. Professional Theme (Not Pitch Black, but Dark Blue-Grey)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .news-card { background: #1c2128; padding: 10px; border-radius: 5px; border: 1px solid #30363d; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Secure Session State
if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- SIGN-IN SYSTEM (Restored & Simple) ---
if not st.session_state["logged"]:
    st.title("🛡️ SENTINEL-X GLOBAL ACCESS")
    st.info("System Status: WAITING FOR FOUNDER AUTHORIZATION...")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        id_input = st.text_input("FOUNDER ID")
        key_input = st.text_input("ACCESS KEY", type="password")
        if st.button("AUTHORIZE SYSTEM"):
            if id_input and key_input: # Simple check
                st.session_state["logged"] = True
                st.rerun()
else:
    # --- CLASSIC SIDEBAR ---
    st.sidebar.title("🛡️ SENTINEL-X")
    st.sidebar.markdown(f"**FOUNDER: ISMAIL**")
    st.sidebar.divider()
    
    # Navigation
    menu = st.sidebar.radio("Command Menu", ["Intelligence Hub", "World Surveillance", "System Security"])
    
    # Simple Logout
    st.sidebar.divider()
    if st.sidebar.button("Logout"):
        st.session_state["logged"] = False
        st.rerun()

    # --- INTELLIGENCE HUB (News + Storage) ---
    if menu == "Intelligence Hub":
        st.title("🧠 NEURAL CORE INTELLIGENCE")
        
        # Metrics & Storage Meter
        m1, m2, m3 = st.columns(3)
        with m1: st.metric("Global Threat", "24%", "-2%")
        with m2: 
            st.write("Storage Used")
            st.progress(65)
        with m3: st.success("AI Core: ACTIVE")
        
        st.divider()
        st.subheader("📡 Global News Feed (Clickable Analysis)")
        # Making news clickable using Expanders
        for i in range(1, 51):
            with st.expander(f"🔴 Node-X{i}: Satellite Signal Intercepted"):
                st.write(f"Deep Analysis for Node-X{i}: No immediate threat detected. Tracking data packets from Sector-7.")

    # --- WORLD SURVEILLANCE (Proper Dots) ---
    elif menu == "World Surveillance":
        st.title("🌍 GLOBAL INTERCEPTOR MAP")
        # Spreading dots globally
        map_data = pd.DataFrame({
            'lat': np.random.uniform(-60, 80, 200),
            'lon': np.random.uniform(-180, 180, 200)
        })
        st.map(map_data)

    # --- SYSTEM SECURITY ---
    elif menu == "System Security":
        st.title("🚨 SECURITY LOGS")
        st.table({"Timestamp": ["16:45", "17:10"], "Source": ["Node-EU", "Node-Asia"], "Action": ["BLOCKED", "DELETED"]})
