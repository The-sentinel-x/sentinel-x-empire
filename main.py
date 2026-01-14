import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Config
st.set_page_config(page_title="SENTINEL-X HUB", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41; }
    .ticker { background: #111; padding: 10px; border-bottom: 2px solid #00FF41; overflow: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- LIVE NEWS TICKER (Decision 1) ---
st.markdown("<div class='ticker'><marquee>🚨 SYSTEM ALERT: Global Threat Level at 24% | 🛡️ ENCRYPTION: 256-bit Active | 📡 SATELLITE LINK: India-Sector-7 Online...</marquee></div>", unsafe_allow_html=True)

if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- ACCESS CONTROL ---
if not st.session_state["logged"]:
    st.sidebar.title("🔒 Sentinel-X Login")
    user = st.sidebar.text_input("Founder ID")
    key = st.sidebar.text_input("Access Key", type="password")
    if st.sidebar.button("ENTER HUB"):
        st.session_state["logged"] = True
        st.rerun()
else:
    # --- COMMAND CENTER ---
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/9415/9415254.png", width=50) # New Icon
    st.sidebar.markdown(f"### ISMAIL: THE SENTINEL X")
    page = st.sidebar.radio("Navigation", ["AI Brain", "Surveillance Map", "Threat Log"])
    
    if st.sidebar.button("Shutdown System"):
        st.session_state["logged"] = False
        st.rerun()

    if page == "AI Brain":
        st.title("🧠 NEURAL CORE ANALYSIS")
        st.write("### AI Prediction: *Analyzing Satellite Data...*")
        st.progress(45)
        st.success("🟢 AI Suggestion: Secure Northern Servers Immediately.")
        
    elif page == "Surveillance Map":
        st.title("🛡️ GLOBAL INTERCEPTORS")
        map_data = pd.DataFrame(np.random.randn(150, 2) / [25, 25] + [20.59, 78.96], columns=['lat', 'lon'])
        st.map(map_data)
        
    elif page == "Threat Log":
        st.title("🚨 RECENT INTERCEPTIONS")
        st.table({"Time": ["14:20", "15:45"], "Source": ["Unknown IP", "Proxy-X"], "Status": ["BLOCKED", "VAPORIZED"]})
