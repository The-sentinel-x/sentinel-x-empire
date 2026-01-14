import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="SENTINEL-X", layout="wide", page_icon="🛡️")

# --- GLOBAL STYLING (Founder's Theme) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #ff4b4b; }
    .stMetric { border: 1px solid #ff4b4b; padding: 10px; border-radius: 5px; background: #111; }
    </style>
    """, unsafe_allow_html=True)

if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- SYSTEM ACCESS ---
if not st.session_state["logged"]:
    st.sidebar.title("🔒 Sentinel-X Access")
    email = st.sidebar.text_input("Founder ID")
    password = st.sidebar.text_input("Key", type="password")
    if st.sidebar.button("EXECUTE"):
        st.session_state["logged"] = True
        st.rerun()
else:
    # --- PERMANENT BRANDING (Decision: Red & White Shield) ---
    st.sidebar.markdown("## 🛡️ SENTINEL-X") # Permanent Logo Text
    st.sidebar.markdown(f"**ISMAIL: THE FOUNDER**")
    st.sidebar.markdown("---")
    
    page = st.sidebar.radio("Navigation", ["AI Brain", "Global Surveillance", "Threat Log"])
    
    if st.sidebar.button("Shutdown System"):
        st.session_state["logged"] = False
        st.rerun()

    if page == "AI Brain":
        st.title("🧠 NEURAL CORE ANALYSIS")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Global Threat Level", value="24%", delta="-2%")
        with col2:
            st.success("🟢 Neural Core: ACTIVE")
            st.success("🟢 Security Protocols: ENCRYPTED")
        st.write("---")
        st.subheader("AI Prediction: *Scanning Satellites...*")
        st.progress(65)

    elif page == "Global Surveillance":
        st.title("🛡️ GLOBAL INTERCEPTORS")
        # Map with 150 Active Nodes
        map_data = pd.DataFrame(np.random.randn(150, 2) / [25, 25] + [20.59, 78.96], columns=['lat', 'lon'])
        st.map(map_data)

    elif page == "Threat Log":
        st.title("🚨 RECENT INTERCEPTIONS")
        st.table({"Time": ["14:20", "15:45", "16:10"], 
                  "Source": ["Unknown IP", "Proxy-X", "Internal Probe"], 
                  "Status": ["BLOCKED", "VAPORIZED", "QUARANTINED"]})
