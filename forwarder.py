import asyncio
import logging
from pyrogram import Client, filters
from info import API_ID, API_HASH, BOT_TOKEN

# Logging setup
logging.basicConfig(level=logging.INFO)

# Aapka bot client
app = Client(
    "FireflixForwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Yahan apna Source Channel ID likhein jahan se movies aayengi (e.g., -100xxxxxxxxxx)
SOURCE_CHANNEL = -1001234567890 

# Aapka Fireflix Database Channel ID jahan movies bhejni hain
TARGET_CHANNEL = -1004469539914

@app.on_message(filters.chat(SOURCE_CHANNEL) & (filters.document | filters.video))
async def auto_forward(client, message):
    try:
        # File ko target database channel mein copy/forward kar dega
        await message.copy(chat_id=TARGET_CHANNEL)
        logging.info(f"Successfully forwarded file: {message.id}")
    except Exception as e:
        logging.error(f"Error forwarding file: {e}")

if __name__ == "__main__":
    print("Auto-Forwarder Worker Started...")
    app.run()
