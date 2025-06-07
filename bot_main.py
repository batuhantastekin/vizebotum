import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("7319867151:AAFze7S9G_ebE9LJpfdY7iYSOSwdG1SfnAg")
CHAT_ID = os.getenv("7229823870")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Randevu botu çalışıyor.")

async def test_notify(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="Bot başarıyla başladı!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    async def on_startup(app):
        await test_notify(app)

    app.post_init = on_startup

    print("Bot çalışıyor...")
    app.run_polling()
