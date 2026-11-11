"""Halaman pencarian website."""

import streamlit as st

from components.card import render_grid
from utils.helper import (
    ASSETS_DIR,
    get_categories,
    init_state,
    inject_css,
    load_websites,
    search_websites,
)

st.set_page_config(page_title="Cari Website", page_icon="🔍", layout="wide")
init_state()
inject_css()

logo_path = ASSETS_DIR / "logo.png"
if logo_path.exists():
    st.logo(str(logo_path), link="https://theuselessweb.com/")

sites = load_websites()

st.title("🔍 Cari Website")
st.caption("Cari berdasarkan nama, domain, kategori, atau deskripsi (Indonesia / Inggris).")

col_q, col_c, col_s = st.columns([3, 3, 2])
query = col_q.text_input("Kata kunci", placeholder="contoh: peta, buku, space, radio…")
cats = col_c.multiselect("Kategori", get_categories(sites), placeholder="Semua kategori")
order = col_s.selectbox("Urutkan", ["Nomor", "Nama A–Z"])

results = search_websites(sites, query, cats)
if order == "Nama A–Z":
    results = sorted(results, key=lambda s: s["name"].lower())

st.write(f"Ditemukan **{len(results)}** dari {len(sites)} website.")
render_grid(results, columns=3, key_prefix="search")
