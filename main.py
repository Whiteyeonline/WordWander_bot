import telebot
from googletrans import Translator

BOT_TOKEN = "7803094882:AAG2WfOA0gvK5deA44s1BZr-USIzFEkAKYY"
bot = telebot.TeleBot(BOT_TOKEN)
translator = Translator()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to WordWander Bot!\nSend any text and I’ll translate it to English automatically.")

@bot.message_handler(func=lambda m: True)
def translate_message(message):
    try:
        translated = translator.translate(message.text, dest='en')
        response = f"🌍 Detected: {translated.src.upper()} ➡️ EN\n\n🗣️ {translated.text}"
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, "❌ Translation failed.")

bot.infinity_polling()