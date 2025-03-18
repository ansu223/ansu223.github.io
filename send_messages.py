import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Replace with your bot token
BOT_TOKEN = '7432253073:AAEXeDaKZ5SnYPkLlGy6GH-N11GzLXxS4Yg'

# Define the message text
message_text = (
    "Congratulations! 🎉 Player spin your ticket 🎟️\n\n"
    "🚨Big box 🎟🔥▫️4000 | 0.0222 LTC\n"
    "💰~2.072746 (USDT)"
)

# Define the inline keyboard
keyboard = [
    [
        InlineKeyboardButton("Claim Your Reward 🎁", url="https://t.me/redpacket_gift_bot/giftbox"),
        InlineKeyboardButton("Join Our Community 👥", url="https://t.me/redpacket_box"),
    ]
]
reply_markup = InlineKeyboardMarkup(keyboard)

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text=message_text,
        reply_markup=reply_markup,
    )

# Main function to run the bot
async def main():
    # Create the Application instance
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    await application.run_polling()

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
