from telegram import Bot

# Replace with your bot token
BOT_TOKEN = '7432253073:AAFTts6hbQ0ehD9D_uyGG9MBeYiLBsO4HOg'

# Replace with your chat ID
YOUR_CHAT_ID = '823543373'  # Your chat ID

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

def send_message():
    # Simple text message
    message_text = "This is a test message."

    # Send the message to your chat ID
    try:
        bot.send_message(chat_id=YOUR_CHAT_ID, text=message_text)
        print(f"Message sent to {YOUR_CHAT_ID}")
    except Exception as e:
        print(f"Failed to send message to {YOUR_CHAT_ID}: {e}")

    print("Test completed.")

if __name__ == '__main__':
    send_message()
