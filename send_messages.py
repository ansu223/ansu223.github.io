from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import os

# Replace with your bot token
BOT_TOKEN = '7432253073:AAFTts6hbQ0ehD9D_uyGG9MBeYiLBsO4HOg'

# Full path to chat_ids.txt
CHAT_IDS_FILE = 'C:\\Users\\Administrator\\Documents\\New folder\\chat_ids.txt'

# Debugging: Check if the file exists
if not os.path.exists(CHAT_IDS_FILE):
    print(f"Error: The file '{CHAT_IDS_FILE}' does not exist.")
    print(f"Current working directory: {os.getcwd()}")
else:
    print(f"The file '{CHAT_IDS_FILE}' exists. Proceeding...")

    # Initialize the bot
    bot = Bot(token=BOT_TOKEN)

    def send_messages():
        # Message text
        message_text = "Hello! Check out this link:"

        # Create an inline keyboard with a button
        keyboard = [
            [InlineKeyboardButton("Visit My Website", url="https://t.me/redpacket_gift_bot/giftbox")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Read chat IDs from the file
        with open(CHAT_IDS_FILE, 'r') as file:
            chat_ids = file.read().splitlines()

        # Remove duplicates (optional, if you want to send only one message per user)
        chat_ids = list(set(chat_ids))

        # Send the message to all chat IDs
        for chat_id in chat_ids:
            try:
                bot.send_message(chat_id=chat_id, text=message_text, reply_markup=reply_markup)
                print(f"Message sent to {chat_id}")
            except Exception as e:
                print(f"Failed to send message to {chat_id}: {e}")

        print("Broadcast completed.")

    if __name__ == '__main__':
        send_messages()
