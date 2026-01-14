import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Page Config
st.set_page_config(page_title="SENTINEL-X GLOBAL EMPIRE", layout="wide")

# Custom UI Styling (Bright & High-Tech)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; color: #1e1e1e; }
    .metric-card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 4px solid #007bff; }
    .news-box { background: #ffffff; border-radius: 8px; border: 1px solid #d1d9e6; padding: 15px; margin-bottom: 10px; border-left: 5px solid #ff4b4b; }
    .stButton>button { background-color: #0056b3; color: white; border-radius: 8px; height: 3em; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- 1. LOGIN SCREEN (The Scan Gateway) ---
if not st.session_state["logged"]:
    st.title("🛡️ SENTINEL-X GLOBAL ACCESS")
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("### AUTHORIZATION REQUIRED")
        id_founder = st.text_input("FOUNDER ID", placeholder="Enter ID...")
        key_founder = st.text_input("SECURITY KEY", type="password", placeholder="••••••••")
        # The Blue Scan Button
        if st.button("🔵 EXECUTE GLOBAL SURVEILLANCE SCAN"):
            if id_founder and key_founder:
                st.session_state["logged"] = True
                st.rerun()
            else:
                st.error("Access Denied: Please enter valid credentials.")
else:
    # --- 2. THE DASHBOARD ---
    st.sidebar.title("🛡️ SENTINEL-X")
    st.sidebar.info("FOUNDER: ISMAIL (ONLINE)")
    menu = st.sidebar.radio("Command Center", ["Empire Intelligence", "Surveillance Map", "Threat Logs"])
    
    if st.sidebar.button("System Logout"):
        st.session_state["logged"] = False
        st.rerun()

    # --- EMPIRE INTELLIGENCE (Storage + Health + News) ---
    if menu == "Empire Intelligence":
        st.title("🧠 EMURAL CORE & LIVE METRICS")
        
        # Exact Metrics
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown("<div class='metric-card'><b>🔋 SYSTEM BATTERY</b><br><h2>89%</h2><p style='color:green'>Optimized</p></div>", unsafe_allow_html=True)
        with m2:
            st.markdown("<div class='metric-card'><b>💿 STORAGE CAPACITY</b><br><h2>1.2 TB / 2.0 TB</h2><p style='color:blue'>65% Used</p></div>", unsafe_allow_html=True)
        with m3:
            st.markdown("<div class='metric-card'><b>📡 GLOBAL NODES</b><br><h2>52 Active</h2><p style='color:red'>Live Scan</p></div>", unsafe_allow_html=True)

        st.divider()
        st.subheader("📡 Real-Time Global News Feed")
        
        # Real Clickable News System (50 News)
        for i in range(1, 51):
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            with st.expander(f"📍 NEWS NODE-{i} | SOURCE: SATELLITE-X | {time_now}"):
                st.markdown(f"**Headline:** Breach Attempt Detected in Sector-{i}")
                st.write(f"**Detail:** Intelligence indicates a localized data surge. Empire Shield has successfully diverted the traffic. No action required by Founder.")
                st.button(f"Mark as Read (Node {i})", key=f"read_{i}")

    # --- MAP (With Meaning) ---
    elif menu == "Surveillance Map":
        st.title("🌍 GLOBAL SURVEILLANCE SCANNER")
        st.warning("🔴 RED DOTS = Active Sentinel Nodes tracking global encrypted traffic.")
        
        map_data = pd.DataFrame({
            'lat': np.random.uniform(-50, 70, 200),
            'lon': np.random.uniform(-160, 160, 200)
        })
        st.map(map_data)

    elif menu == "Threat Logs":
        st.title("🚨 SECURITY INTERCEPTIONS")
        st.table({"Timestamp": ["16:45", "17:10"], "Source": ["EU-Proxy", "Asia-Node"], "Threat Level": ["High", "Medium"], "Action": ["BLOCKED", "DIVERTED"]})
