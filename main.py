import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Page Configuration
st.set_page_config(page_title="SENTINEL-X GLOBAL EMPIRE", layout="wide")

# CUSTOM BRIGHT THEME CSS
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #1E1E1E; }
    .news-box-green { background: #F0FFF4; border: 2px solid #38A169; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .news-box-blue { background: #EBF8FF; border: 2px solid #3182CE; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .metric-card { background: #FFFFFF; border: 1px solid #E2E8F0; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .stButton>button { background-color: #0056b3; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

if "logged" not in st.session_state:
    st.session_state["logged"] = False

# --- 1. LOGIN SCREEN (The Guard) ---
if not st.session_state["logged"]:
    st.title("🛡️ SENTINEL-X: GLOBAL EMPIRE ACCESS")
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("### ENTER FOUNDER CREDENTIALS")
        id_user = st.text_input("FOUNDER ID", placeholder="Admin ID")
        key_user = st.text_input("ACCESS KEY", type="password", placeholder="••••••••")
        if st.button("🔵 EXECUTE GLOBAL SURVEILLANCE SCAN"): # Blue Button Restore
            if id_user and key_user:
                st.session_state["logged"] = True
                st.rerun()
else:
    # --- 2. DASHBOARD ---
    st.sidebar.title("🛡️ SENTINEL-X")
    st.sidebar.success("ONLINE: FOUNDER ISMAIL")
    menu = st.sidebar.radio("Navigation", ["Empire Intelligence", "Surveillance Map", "Security Logs"])

    if menu == "Empire Intelligence":
        st.title("🧠 NEURAL CORE & LIVE METRICS")
        
        # Exact Metrics Restoration
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown("<div class='metric-card'><b>🔋 SYSTEM BATTERY</b><br><h2>89%</h2><p style='color:green'>Status: Optimized</p></div>", unsafe_allow_html=True)
        with m2:
            st.markdown("<div class='metric-card'><b>💿 STORAGE CAPACITY</b><br><h2>1.2 TB / 2.0 TB</h2><p style='color:blue'>65% Used</p></div>", unsafe_allow_html=True)
        with m3:
            st.markdown("<div class='metric-card'><b>📡 GLOBAL NODES</b><br><h2>52 Active</h2><p style='color:red'>Live Monitoring</p></div>", unsafe_allow_html=True)

        st.divider()
        st.subheader("📡 Real-Time Intelligence Feed (Click for Full Report)")
        
        # Modern Colorful Clickable News (50 Unique Items)
        for i in range(1, 51):
            box_style = "news-box-green" if i % 2 == 0 else "news-box-blue"
            with st.expander(f"📍 NEWS NODE-{i} | {datetime.datetime.now().strftime('%H:%M:%S')}"):
                st.markdown(f"**INTEL REPORT:** Breach detected in Sector {i}.")
                st.write(f"**ACTUAL NEWS:** Satellite-X has intercepted an unauthorized packet from an unknown IP. The Empire Shield has successfully isolated the threat at Node-{i}.")
                st.info(f"Verdict: Node {i} remains 100% operational under Founder's command.")

    elif menu == "Surveillance Map":
        st.title("🌍 GLOBAL SURVEILLANCE SCANNER")
        st.info("🔴 RED DOTS = Active Satellite Interceptors tracking global threats.")
        map_data = pd.DataFrame({'lat': np.random.uniform(-50, 70, 200), 'lon': np.random.uniform(-160, 160, 200)})
        st.map(map_data)

    elif menu == "Security Logs":
        st.title("🚨 RECENT INTERCEPTIONS")
        st.write("Current blocked threats from around the world:")
        st.table({"Time": ["16:45", "17:10"], "Source": ["EU-Server", "Asia-Gate"], "Status": ["BLOCKED", "DIVERTED"]})

    if st.sidebar.button("Logout"):
        st.session_state["logged"] = False
        st.rerun()
