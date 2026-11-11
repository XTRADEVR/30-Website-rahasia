"""Halaman Tentang."""

import streamlit as st

from utils.helper import (
    ASSETS_DIR,
    clickable_image,
    image_to_data_uri,
    init_state,
    inject_css,
)

st.set_page_config(page_title="Tentang", page_icon="ℹ️", layout="wide")
init_state()
inject_css()

logo_path = ASSETS_DIR / "logo.png"
if logo_path.exists():
    st.logo(str(logo_path), link="https://theuselessweb.com/")

st.title("ℹ️ Tentang")

col_img, col_txt = st.columns([1, 3])
with col_img:
    if logo_path.exists():
        st.markdown(
            clickable_image(
                image_to_data_uri(str(logo_path)),
                "https://streamlit.io/",
                alt="Dibuat dengan Streamlit",
                css_class="site-icon",
            ),
            unsafe_allow_html=True,
        )
with col_txt:
    st.markdown(
        """
**30 Websites Seru** adalah kumpulan 30 website unik buat kamu yang lagi gabut jam 2 pagi:
jendela random dunia, planetarium, kamera satwa liar, peta kuno, arsip buku, museum virtual, dan banyak lagi.

**Fitur**
- Semua gambar dan nama domain bisa diklik, langsung membuka website di tab baru
- Pencarian + filter kategori
- Favorit (bisa diunduh dan diimpor lagi)
- Tombol “Kejutkan aku” untuk pilihan acak
- Seluruh data ada di `data/websites.json`, tinggal edit untuk menambah website
"""
    )

st.subheader("Catatan")
st.markdown(
    """
- Judul “terasa ilegal” hanya gaya clickbait. Semua website di sini publik dan legal.
- Semua website adalah milik pihak ketiga. Project ini tidak berafiliasi dengan mereka;
  isi dan ketersediaan mereka bisa berubah sewaktu-waktu.
- Ikon website diambil dari layanan favicon Google, jadi perlu koneksi internet.
"""
)

st.subheader("Teknologi")
st.markdown("Python · Streamlit · JSON · lisensi MIT (lihat file `LICENSE`).")
