import telebot
import requests

TOKEN = "8046659043:AAEZlTTPKRNd7Fvmdb0Ikj8fO9iBb2XaNDo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def get_id(message):
    print("Chat ID:", message.chat.id)
    bot.reply_to(message, "تم تسجيل الـ ID!")

print("Bot is running...")

while True:
    try:
        bot.polling(timeout=60, long_polling_timeout=60, none_stop=True)
    except requests.exceptions.ReadTimeout:
        print("Timeout… إعادة الاتصال…")
        continue
    except Exception as e:
        print("Error:", e)
        continue
