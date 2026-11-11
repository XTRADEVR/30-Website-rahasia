# 🌐 30 Websites Seru

Kumpulan **30 website unik** buat kamu yang lagi gabut jam 2 pagi — dibuat dengan **Streamlit**.
Semua gambar, nama domain, dan tombol di kartu bisa diklik dan langsung membuka website-nya.

## ✨ Fitur

- 🖱️ Semua gambar & link bisa diklik (buka di tab baru)
- 🔍 Pencarian + filter kategori (Indonesia / Inggris)
- ⭐ Favorit, bisa diunduh dan diimpor lagi (`.json`)
- 🎲 Tombol “Kejutkan aku” untuk pilihan acak
- 🎨 Tema biru + emas, dark mode
- 🗂️ Semua data di `data/websites.json` — tambah website tanpa menyentuh kode

## 🚀 Jalankan di komputer

```bash
git clone https://github.com/<username-kamu>/30-websites-app.git
cd 30-websites-app
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Buka http://localhost:8501

## ☁️ Deploy gratis (Streamlit Community Cloud)

1. Push repo ini ke GitHub (set **Public**).
2. Buka https://share.streamlit.io lalu login dengan GitHub.
3. Pilih repo, branch `main`, file utama `app.py`, lalu **Deploy**.

## 🗂️ Struktur

```
30-websites-app/
├── app.py                 # Halaman utama
├── pages/                 # Cari Website, Favorit, Tentang
├── components/card.py     # Komponen kartu
├── utils/helper.py        # Fungsi bantu
├── data/websites.json     # Data 30 website
├── assets/                # logo.png, banner.png, style.css
└── .streamlit/config.toml # Tema
```

## ➕ Menambah website

Tambahkan satu objek baru di `data/websites.json`:

```json
{"id": 31, "name": "Nama", "domain": "contoh.com", "url": "https://contoh.com/",
 "category": "Jelajah Dunia", "emoji": "🌍",
 "description": "English description.", "deskripsi": "Deskripsi Indonesia."}
```

## 📝 Catatan

Website di daftar ini milik pihak ketiga dan tidak berafiliasi dengan project ini. Judul “terasa ilegal” hanya gaya clickbait; semuanya publik dan legal.

## 📄 Lisensi

MIT — lihat [LICENSE](LICENSE).
