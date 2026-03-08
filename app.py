import os
import telebot

BOT_TOKEN = "7926174608:AAH9pLyUHwLwCGsYj9xdXwEJYMwUxHTPfK0"

bot = telebot.TeleBot(BOT_TOKEN)

# .py file receive
@bot.message_handler(content_types=['document'])
def handle_file(message):
    file_info = bot.get_file(message.document.file_id)

    if not message.document.file_name.endswith(".py"):
        bot.reply_to(message, "❌ Only .py files allowed")
        return

    downloaded = bot.download_file(file_info.file_path)

    file_path = f"uploads/{message.document.file_name}"

    os.makedirs("uploads", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(downloaded)

    bot.reply_to(message, "✅ File received. Running...")

    # run python file
    os.system(f"python3 {file_path}")

bot.infinity_polling()
