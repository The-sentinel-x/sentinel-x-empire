import streamlit as st
import psutil
import shutil
import requests
import os
import xml.etree.ElementTree as ET

# 1. Advanced Page Config
st.set_page_config(page_title="SENTINEL-X COMMAND", page_icon="🕵️‍♂️", layout="wide")

# Custom Cyber Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ffcc; }
    .stMetric { background-color: #161b22; border: 1px solid #00ffcc; padding: 15px; border-radius: 10px; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #00ffcc; color: black; font-weight: bold; }
    .news-card { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #00ffcc; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

if not os.path.exists("Empire_Records"):
    os.makedirs("Empire_Records")

# 2. Sidebar Controls
st.sidebar.title("⚡ COMMAND CENTER")
if st.sidebar.button("📡 SCAN GLOBAL INTELLIGENCE"):
    with st.spinner("Intercepting Satellite Feeds..."):
        try:
            r = requests.get("https://news.google.com/rss", timeout=10)
            root = ET.fromstring(r.content)
            news_data = ""
            for item in root.findall('.//item')[:50]:
                title = item.find('title').text
                link = item.find('link').text
                news_data += f"TITLE: {title}||LINK: {link}\n"
            with open("Empire_Records/news_report.txt", "w", encoding="utf-8") as f:
                f.write(news_data)
            st.sidebar.success("DATA INTERCEPTED!")
            st.rerun()
        except Exception as e:
            st.sidebar.error(f"SCAN FAILED: {e}")

# 3. Dashboard UI
st.title("🛡️ SENTINEL-X : GLOBAL SURVEILLANCE")
st.markdown("---")

col1, col2, col3 = st.columns(3)
_, _, free = shutil.disk_usage("/")
battery = psutil.sensors_battery()

with col1:
    st.metric("💾 DISK CAPACITY", f"{free // (2**30)} GB FREE")
with col2:
    if battery:
        st.metric("🔋 CORE ENERGY", f"{battery.percent}%", "CHARGING" if battery.power_plugged else "STABLE")
with col3:
    st.metric("🌐 UPLINK STATUS", "ENCRYPTED")

st.markdown("---")

# 4. Intelligence Feed
st.header("🕵️ LIVE INTELLIGENCE STREAM")
if os.path.exists("Empire_Records/news_report.txt"):
    with open("Empire_Records/news_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if "||" in line:
                t, l = line.split("||")
                clean_link = l.strip().replace("LINK: ", "")
                st.markdown(f"""
                <div class="news-card">
                    <h4 style='color: #00ffcc;'>{t.replace("TITLE: ", "")}</h4>
                    <a href='{clean_link}' target='_blank'>
                        <button style='background-color: #00ffcc; border: none; padding: 5px 15px; border-radius: 5px; cursor: pointer; color: black; font-weight: bold;'>Read Full Intel</button>
                    </a>
                </div>
                """, unsafe_allow_html=True)
else:
    st.warning("SYSTEM IDLE. AWAITING SCAN COMMAND.")