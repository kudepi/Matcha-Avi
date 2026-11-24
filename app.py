"""Matcha Avı - Gabar Dağları Efsanesi (Streamlit + HTML5 canvas)."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Matcha Avı · Gabar Dağları Efsanesi",
    page_icon="🍵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0.6rem 0.6rem 0 0.6rem; max-width: 100%;}
      .stApp {background: #0d1a12;}
      iframe {border-radius: 14px;}
    </style>
    """,
    unsafe_allow_html=True,
)

GAME_HTML = (Path(__file__).parent / "game.html").read_text(encoding="utf-8")
components.html(GAME_HTML, height=800, scrolling=False)
