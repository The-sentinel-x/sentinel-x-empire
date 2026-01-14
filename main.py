import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="SENTINEL-X | THE EMPIRE", layout="wide", page_icon="🛡️")

# Styling: Classic Professional Dark Mode
st.markdown("""<style>.stApp { background-color: #0b0e14; color: #ffffff; }</style>""", unsafe_allow_html=True)

if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- 1. LOGIN SYSTEM (Clean & Simple) ---
if not st.session_state["logged"]:
    st.title("🛡️ SENTINEL-X SECURE ENTRY")
    email = st.text_input("Founder ID")
    password = st.text_input("Access Key", type="password")
    if st.button("AUTHORIZE ACCESS"):
        st.session_state["logged"] = True
        st.rerun()
else:
    # --- 2. SIDEBAR (Permanent Classic Branding) ---
    st.sidebar.markdown("# 🛡️ SENTINEL-X")
    st.sidebar.markdown("### ISMAIL: THE FOUNDER")
    st.sidebar.divider()
    page = st.sidebar.radio("Command Menu", ["Intelligence Hub", "Global Map", "Security Logs"])

    # --- 3. INTELLIGENCE HUB (Storage + News + AI) ---
    if page == "Intelligence Hub":
        st.title("🧠 NEURAL CORE & SYSTEM HEALTH")
        
        # Metrics Row
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("System Load", "34%", "+2%")
        with col2:
            st.write("Disk Storage Used")
            st.progress(65) # The storage meter you missed
        with col3:
            st.success("AI Core: NOMINAL")

        st.divider()
        # The AI Feature: News Analysis
        st.subheader("📡 Global Satellite Intelligence (50+ Live Nodes)")
        for i in range(1, 11): # Showing 10 grouped nodes (compact look)
            st.info(f"Node-X{i}: Scanning Satellite Stream... All Systems Green.")
        
    # --- 4. GLOBAL MAP (Restored) ---
    elif page == "Global Map":
        st.title("🌍 GLOBAL SURVEILLANCE SCANNER")
        map_data = pd.DataFrame(np.random.randn(100, 2) / [20, 20] + [20.59, 78.96], columns=['lat', 'lon'])
        st.map(map_data)
        st.write("Red Dots represent Active Sentinel Interceptors.")

    # --- 5. LOGS (Simple Table) ---
    elif page == "Security Logs":
        st.title("🚨 SECURITY INTERCEPTIONS")
        st.table({"Timestamp": ["16:45", "17:10"], "Threat": ["Brute Force", "Malware Probe"], "Status": ["BLOCKED", "DELETED"]})

    if st.sidebar.button("System Shutdown"):
        st.session_state["logged"] = False
        st.rerun()
