from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5697209080:AAHpmmDRb-fVmwI59wOctTdr5VkiFTDq-5I")

API_ID = int(os.environ.get("API_ID",14699743))

API_HASH = os.environ.get("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()
