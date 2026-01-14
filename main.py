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
    .news-card { background: #1c
