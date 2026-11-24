"""Matcha Avı - Gabar Dağları Efsanesi (Streamlit + HTML5 canvas)."""
import json
import os
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


def _secret(name):
    """Önce ortam değişkeni, sonra st.secrets (yoksa None)."""
    v = os.environ.get(name)
    if v:
        return v
    try:
        return st.secrets.get(name)
    except Exception:
        return None


# İsteğe bağlı TURN: WebRTC'nin direkt bağlanamadığı ağlarda (okul/kurumsal) direkt hattı kurtarır.
# Tanımlı değilse yalnızca STUN kullanılır; direkt hat olmazsa oyun otomatik yedek hatta geçer.
turn_cfg = None
if _secret("TURN_URLS"):
    turn_cfg = {
        "urls": [u.strip() for u in str(_secret("TURN_URLS")).split(",") if u.strip()],
        "username": _secret("TURN_USERNAME") or "",
        "credential": _secret("TURN_CREDENTIAL") or "",
    }
elif _secret("METERED_APP") and _secret("METERED_KEY"):
    turn_cfg = {"metered": {"app": _secret("METERED_APP"), "key": _secret("METERED_KEY")}}

HERE = Path(__file__).parent
GAME_HTML = (HERE / "game.html").read_text(encoding="utf-8")
inject = ""
if turn_cfg:
    inject += "<script>window.TURN_CFG=" + json.dumps(turn_cfg) + ";</script>"
PEER_JS = HERE / "peerjs.min.js"
if PEER_JS.exists():  # çevrimiçi co-op için PeerJS'i oyunun içine göm
    inject += "<script>" + PEER_JS.read_text(encoding="utf-8") + "</script>"
GAME_HTML = GAME_HTML.replace("<!--PEERJS-->", inject)
components.html(GAME_HTML, height=800, scrolling=False)
