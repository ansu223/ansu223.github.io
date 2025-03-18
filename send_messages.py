from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import logging

# Enable logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Replace with your bot token
BOT_TOKEN = "7432253073:AAEXeDaKZ5SnYPkLlGy6GH-N11GzLXxS4Yg"

# Replace with your chat ID (Remove quotes, it should be an integer)
YOUR_CHAT_ID = 823543373  

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

def send_messages():
    message_text = "Run the bot and spin the wheel!"

    # Create an inline keyboard with a button
    keyboard = [[InlineKeyboardButton("Click Here", url="https://t.me/redpacket_gift_bot/giftbox")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message
    try:
        logger.info(f"🚀 Sending message to chat ID: {YOUR_CHAT_ID}")
        response = bot.send_message(chat_id=YOUR_CHAT_ID, text=message_text, reply_markup=reply_markup)
        logger.info(f"✅ Message successfully sent: {response}")
    except Exception as e:
        logger.error(f"❌ Failed to send message: {e}")

    logger.info("📢 Broadcast completed.")

if __name__ == "__main__":
    send_messages()
