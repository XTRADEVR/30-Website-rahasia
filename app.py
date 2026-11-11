"""30 Websites — halaman utama (Home)."""

import random

import streamlit as st

from components.card import render_card, render_grid
from utils.helper import (
    ASSETS_DIR,
    clickable_image,
    get_categories,
    image_to_data_uri,
    init_state,
    inject_css,
    load_websites,
    search_websites,
)

st.set_page_config(
    page_title="30 Websites Seru",
    page_icon="🌐",
    layout="wide",
)

init_state()
inject_css()

logo_path = ASSETS_DIR / "logo.png"
if logo_path.exists():
    st.logo(str(logo_path), link="https://theuselessweb.com/")

sites = load_websites()

# ---------- Hero: banner bisa diklik (lompat ke website acak yang aneh) ----------
banner_path = ASSETS_DIR / "banner.png"
if banner_path.exists():
    st.markdown(
        clickable_image(
            image_to_data_uri(str(banner_path)),
            "https://theuselessweb.com/",
            alt="Klik untuk lompat ke website acak",
            css_class="hero-banner",
        ),
        unsafe_allow_html=True,
    )
else:
    st.title("🌐 30 Websites Seru")

st.markdown("### 30 website yang terasa “ilegal” untuk diketahui — padahal 100% legal ✨")
st.caption("Klik gambar atau tombol di kartu mana pun untuk membuka website-nya di tab baru.")

c1, c2, c3 = st.columns(3)
c1.metric("Total website", len(sites))
c2.metric("Kategori", len(get_categories(sites)))
c3.metric("Favoritmu", len(st.session_state["favorites"]))

# ---------- Kejutkan aku ----------
st.divider()
left, right = st.columns([1, 3])
with left:
    if st.button("🎲 Kejutkan aku!", type="primary"):
        st.session_state["surprise"] = random.choice(sites)["id"]
with right:
    surprise_id = st.session_state.get("surprise")
    if surprise_id:
        pick = next(s for s in sites if s["id"] == surprise_id)
        st.success(f"Coba buka: **{pick['name']}** — {pick['deskripsi']}")
        st.link_button(f"Buka {pick['domain']}", pick["url"])

# ---------- Filter kategori + grid ----------
st.divider()
selected = st.multiselect(
    "Filter kategori",
    get_categories(sites),
    placeholder="Semua kategori",
)
render_grid(search_websites(sites, "", selected), columns=3, key_prefix="home")

st.divider()
st.caption("Simpan daftar ini dan berterima kasihlah nanti ⭐ — pakai menu di kiri untuk Cari, Favorit, dan Tentang.")
