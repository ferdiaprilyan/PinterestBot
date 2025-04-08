# 🤖 Pinterest Scraper Telegram Bot

Bot Telegram otomatis yang:
- 🖼️ Mengunduh gambar & video dari Pinterest (HD kalau tersedia)
- 📤 Mengirim konten ke Channel Telegram
- ♻️ Anti duplikat — gak bakal kirim konten yang sama dua kali
- 🔁 Berjalan terus-menerus

---

## ✨ Fitur
- ✅ Auto scraping dari Pinterest Board
- ✅ Kirim otomatis ke Channel
- ✅ Duplikat check via nama file
- ✅ Kualitas gambar terbaik (HD Mode)
- ✅ Loop tiap 5 detik

---

## ⚙️ Prasyarat

Pastikan sudah install:

- Python 3.9+
- `gallery-dl`
- `pyrogram` & `tgcrypto`
- `ffmpeg`

### 💾 Cara install dependensi:
```bash
pip install -U pyrogram tgcrypto gallery-dl ffmpeg
```

---

## 🔧 Setup

### 1. Buat Bot Telegram
- Chat [@BotFather](https://t.me/BotFather)
- `/newbot` → ikuti instruksinya
- Simpan `BOT_TOKEN`

### 2. Ambil API ID & HASH
- Kunjungi: [https://my.telegram.org](https://my.telegram.org)
- Login → `API Development Tools`
- Simpan `API_ID` dan `API_HASH`

### 3. Edit Konfigurasi di Script
Ganti variabel berikut di dalam file Python kamu:

```python
PINTEREST_URL = "https://id.pinterest.com/enzypinterest/bot-telegram/"  # Ganti dengan board kamu
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = -1001234567890  # Ganti dengan ID channel kamu
```

> ℹ️ Untuk dapatkan `CHANNEL_ID`, forward pesan dari channel ke @userinfobot

---

### 4. Buat File `gallery-dl.conf`
Di folder yang sama, buat file `gallery-dl.conf`:

```json
{
    "extractor": {
        "pinterest": {
            "image-quality": "original"
        }
    },
    "archive": "archive.txt",
    "cache": {
        "mode": "none"
    }
}
```

File ini biar scraping-nya gak ngulang & hasilnya HD.

---

## ▶️ Cara Menjalankan

```bash
python bot.py
```

> Bot akan:
> - Scrape konten dari Pinterest
> - Upload ke Channel Telegram
> - Ulangi proses tiap 5 detik

---

## ✅ Tips & Trik
- ❌ Hapus `sent_files.json` kalau mau reset riwayat kiriman
- 📁 File hasil scrape ada di `gallery-dl/`
- 🔒 Gunakan channel pribadi buat eksperimen dulu

---

## 🧠 Kenapa Bikin Ini?
> Awalnya cuma scroll Pinterest sambil rebahan,  
> lalu kepikiran: *"Kenapa gak bikin bot aja yang save otomatis?"*  
>  
> Gabut sih... tapi terarah.  

---

## ©️ License
Feel free to fork, modif, dan upload ulang. Kasih ⭐⭐⭐⭐⭐ untuk repository ini.

---

## Made with Kafein by:  
**Orang yang terlalu mager buat save manual dari Pinterest.** [ENZY](https://t.me/GoodayFreeze)