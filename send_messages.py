from telegram import Bot
import logging

# Enable logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Replace with your bot token
BOT_TOKEN = "7432253073:AAEXeDaKZ5SnYPkLlGy6GH-N11GzLXxS4Yg"  

# Replace with your chat ID (must be an integer)
YOUR_CHAT_ID = 823543373  

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

def send_messages():
    message_text = "Hello! This is a simple message from your bot."

    # Send the message
    try:
        logger.info(f"🚀 Sending message to chat ID: {YOUR_CHAT_ID}")
        bot.send_message(chat_id=YOUR_CHAT_ID, text=message_text)
        logger.info(f"✅ Message successfully sent to {YOUR_CHAT_ID}")
    except Exception as e:
        logger.error(f"❌ Failed to send message: {e}")
        logger.error(f"Details: {str(e)}")  # Log the full error details

    logger.info("📢 Broadcast completed.")

if __name__ == "__main__":
    send_messages()
