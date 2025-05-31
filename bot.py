import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from googletrans import Translator

TOKEN = "7803094882:AAG2WfOA0gvK5deA44s1BZr-USIzFEkAKYY"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

translator = Translator()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌍 Welcome to WordWander Translator Bot! Just send me a message, and I'll translate it into English.")

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_text = update.message.text
    translated = translator.translate(input_text, dest='en')
    await update.message.reply_text(f"🔤 Translation:
{translated.text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

    app.run_polling()

if __name__ == "__main__":
    main()
