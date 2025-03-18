import logging
from telegram import Bot
import asyncio

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Replace with your bot token and chat ID
BOT_TOKEN = '7432253073:AAEXeDaKZ5SnYPkLlGy6GH-N11GzLXxS4Yg'  # Your bot token
YOUR_CHAT_ID = 823543373  # Replace with your chat ID

# Create the bot instance
bot = Bot(token=BOT_TOKEN)

# Define an async function to send the message
async def send_message():
    message_text = "Hello, this is a test message!"
    logging.info(f"🚀 Sending message to chat ID: {YOUR_CHAT_ID}")
    try:
        await bot.send_message(chat_id=YOUR_CHAT_ID, text=message_text)
        logging.info(f"✅ Message successfully sent to {YOUR_CHAT_ID}")
    except Exception as e:
        logging.error(f"❌ Failed to send message: {e}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(send_message())
