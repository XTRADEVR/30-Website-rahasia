"""Fungsi bantu: load data, favorit, pencarian, CSS, dan gambar yang bisa diklik."""

import base64
import json
from html import escape
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "websites.json"
ASSETS_DIR = ROOT / "assets"

GOLD = "#F5B301"


@st.cache_data
def load_websites():
    """Baca semua website dari data/websites.json."""
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def get_categories(sites):
    """Daftar kategori unik, urutan sesuai kemunculan."""
    seen = []
    for s in sites:
        if s["category"] not in seen:
            seen.append(s["category"])
    return seen


def favicon_url(domain, size=128):
    """Ikon website lewat layanan favicon Google."""
    return f"https://www.google.com/s2/favicons?domain={domain}&sz={size}"


@st.cache_data
def image_to_data_uri(path_str):
    """Ubah file gambar lokal jadi data URI supaya bisa dipakai di <img> HTML."""
    path = Path(path_str)
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def clickable_image(src, href, alt="", css_class="clickable-img"):
    """HTML gambar yang jika diklik membuka link di tab baru."""
    return (
        f'<a href="{escape(href)}" target="_blank" rel="noopener noreferrer" '
        f'title="{escape(alt)}">'
        f'<img class="{css_class}" src="{src}" alt="{escape(alt)}" loading="lazy"></a>'
    )


# ---------- Favorit (disimpan di session_state) ----------

def init_state():
    st.session_state.setdefault("favorites", [])


def is_favorite(site_id):
    return site_id in st.session_state.get("favorites", [])


def toggle_favorite(site_id):
    favs = st.session_state.setdefault("favorites", [])
    if site_id in favs:
        favs.remove(site_id)
    else:
        favs.append(site_id)


def favorites_to_json():
    return json.dumps({"favorites": sorted(st.session_state.get("favorites", []))})


def favorites_from_json(raw, valid_ids):
    """Parse file favorit hasil export. Kembalikan list id yang valid."""
    data = json.loads(raw)
    ids = data.get("favorites", []) if isinstance(data, dict) else []
    return [i for i in ids if isinstance(i, int) and i in valid_ids]


# ---------- Pencarian ----------

def search_websites(sites, query="", categories=None):
    q = (query or "").strip().lower()
    result = []
    for s in sites:
        if categories and s["category"] not in categories:
            continue
        haystack = " ".join(
            [s["name"], s["domain"], s["category"], s["description"], s["deskripsi"]]
        ).lower()
        if q and q not in haystack:
            continue
        result.append(s)
    return result


# ---------- Tampilan ----------

def inject_css():
    css = ASSETS_DIR / "style.css"
    if css.exists():
        st.markdown(f"<style>{css.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
