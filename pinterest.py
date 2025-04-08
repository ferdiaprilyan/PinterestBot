# ------------
# Telegram : @GoodayFreeze
# Group Support : @SharingUserbot
# ------------

import os
import subprocess
import json
import asyncio
from pyrogram import Client

# Konfigurasi
PINTEREST_URL = "https://id.pinterest.com/akunmu/bot-telegram/"
API_ID = "API_ID"
API_HASH = "API_HASH"
BOT_TOKEN = "BOT_TOKEN"
CHANNEL_ID = -100

ALLOWED_EXTENSIONS = {'.jpg', '.png', '.mp4', '.gif'}
SENT_FILES_JSON = 'sent_files.json'
GALLERY_DL_CONF = 'gallery-dl.conf'
DOWNLOAD_DIR = "gallery-dl/pinterest"

def load_sent_files():
    if not os.path.exists(SENT_FILES_JSON):
        with open(SENT_FILES_JSON, 'w') as f:
            json.dump([], f)
    with open(SENT_FILES_JSON, 'r') as f:
        return set(json.load(f))

def save_sent_files(sent_files):
    with open(SENT_FILES_JSON, 'w') as f:
        json.dump(list(sent_files), f)

def download_pinterest_files(url):
    try:
        subprocess.run(["gallery-dl", "--config", GALLERY_DL_CONF, url], check=True)
        print("File berhasil diunduh (HD jika tersedia).")
    except subprocess.CalledProcessError as e:
        print(f"Gagal mengunduh file: {e}")

async def send_to_telegram(file_path, sent_files, app):
    file_name = os.path.basename(file_path)

    if file_name in sent_files:
        print(f"File {file_name} sudah pernah dikirim, dilewati.")
        return

    try:
        await app.send_document(chat_id=CHANNEL_ID, document=file_path)
        print(f"File {file_name} berhasil dikirim.")
        sent_files.add(file_name)
        save_sent_files(sent_files)
    except Exception as e:
        print(f"Gagal kirim {file_path}: {e}")

async def main():
    app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

    while True:
        sent_files = load_sent_files()
        download_pinterest_files(PINTEREST_URL)

        async with app:
            for root, _, files in os.walk(DOWNLOAD_DIR):
                for file in files:
                    file_path = os.path.join(root, file)
                    if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                        await send_to_telegram(file_path, sent_files, app)

        print("Menunggu 5 detik sebelum scrape ulang...")
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
