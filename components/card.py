"""Komponen kartu website. Gambar kartu bisa diklik dan membuka website."""

from html import escape

import streamlit as st

from utils.helper import (
    clickable_image,
    favicon_url,
    is_favorite,
    toggle_favorite,
)


def render_card(site, key_prefix="card"):
    """Satu kartu: gambar (klik = buka web), nama, deskripsi, tombol buka + favorit."""
    fav = is_favorite(site["id"])
    img = clickable_image(
        favicon_url(site["domain"]),
        site["url"],
        alt=f"Buka {site['name']}",
        css_class="site-icon",
    )

    with st.container(border=True):
        st.markdown(
            f"""
            <div class="site-card">
              <div class="site-top">
                <span class="site-num">{site['id']}</span>
                <span class="site-emoji">{site['emoji']}</span>
              </div>
              <div class="site-icon-wrap">{img}</div>
              <div class="site-name">{escape(site['name'])}</div>
              <a class="site-domain" href="{escape(site['url'])}" target="_blank"
                 rel="noopener noreferrer">{escape(site['domain'])}</a>
              <div class="site-desc">{escape(site['deskripsi'])}</div>
              <div class="site-cat">{escape(site['category'])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col_open, col_fav = st.columns([4, 1])
        with col_open:
            st.link_button("🔗 Buka website", site["url"])
        with col_fav:
            label = "⭐" if fav else "☆"
            help_text = "Hapus dari favorit" if fav else "Tambah ke favorit"
            if st.button(label, key=f"{key_prefix}_fav_{site['id']}", help=help_text):
                toggle_favorite(site["id"])
                st.rerun()


def render_grid(sites, columns=3, key_prefix="grid"):
    """Tampilkan daftar website sebagai grid kartu."""
    if not sites:
        st.info("Tidak ada website yang cocok. Coba kata kunci lain 🙂")
        return
    for start in range(0, len(sites), columns):
        row = sites[start:start + columns]
        cols = st.columns(columns)
        for col, site in zip(cols, row):
            with col:
                render_card(site, key_prefix=key_prefix)
