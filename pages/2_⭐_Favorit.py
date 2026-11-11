"""Halaman favorit. Disimpan di sesi browser; bisa di-export/import sebagai JSON."""

import streamlit as st

from components.card import render_grid
from utils.helper import (
    ASSETS_DIR,
    favorites_from_json,
    favorites_to_json,
    init_state,
    inject_css,
    load_websites,
)

st.set_page_config(page_title="Favorit", page_icon="⭐", layout="wide")
init_state()
inject_css()

logo_path = ASSETS_DIR / "logo.png"
if logo_path.exists():
    st.logo(str(logo_path), link="https://theuselessweb.com/")

sites = load_websites()
valid_ids = {s["id"] for s in sites}

st.title("⭐ Favorit")
st.caption(
    "Favorit tersimpan selama sesi browser berjalan. Mau dipakai lagi nanti? "
    "Unduh file favorit lalu unggah kembali."
)

favs = [s for s in sites if s["id"] in st.session_state["favorites"]]

if favs:
    render_grid(favs, columns=3, key_prefix="fav")
else:
    st.info("Belum ada favorit. Tekan ☆ di kartu website mana pun untuk menambahkannya.")

st.divider()
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.download_button(
        "⬇️ Unduh favorit (.json)",
        data=favorites_to_json(),
        file_name="favorit-30-websites.json",
        mime="application/json",
        disabled=not favs,
    )

with col_b:
    uploaded = st.file_uploader("Impor favorit", type=["json"], label_visibility="collapsed")
    if uploaded is not None:
        try:
            ids = favorites_from_json(uploaded.getvalue().decode("utf-8"), valid_ids)
            st.session_state["favorites"] = ids
            st.success(f"{len(ids)} favorit berhasil dimuat.")
        except (ValueError, UnicodeDecodeError):
            st.error("File tidak valid. Pakai file hasil unduhan dari halaman ini.")

with col_c:
    if st.button("🗑️ Kosongkan favorit", disabled=not favs):
        st.session_state["favorites"] = []
        st.rerun()
