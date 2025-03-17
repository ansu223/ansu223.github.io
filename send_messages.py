from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Replace with your bot token
BOT_TOKEN = '7432253073:AAFTts6hbQ0ehD9D_uyGG9MBeYiLBsO4HOg'

# Replace with your chat ID
YOUR_CHAT_ID = '823543373'  # Your chat ID

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

def send_messages():
    # Message text
    message_text = "Hello! Check out this link:"

    # Create an inline keyboard with a button
    keyboard = [
        [InlineKeyboardButton("Visit My Website", url="https://t.me/redpacket_box")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message to your chat ID
    try:
        bot.send_message(chat_id=YOUR_CHAT_ID, text=message_text, reply_markup=reply_markup)
        print(f"Message sent to {YOUR_CHAT_ID}")
    except Exception as e:
        print(f"Failed to send message to {YOUR_CHAT_ID}: {e}")

    print("Broadcast completed.")

if __name__ == '__main__':
    send_messages()
