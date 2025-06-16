from telegram.ext import ApplicationBuilder, MessageHandler, filters
from bot.handlers import handle_image

TOKEN = "7517383844:AAGMyr0Z12ly0iqsvbbIKkYLU2H55hwRNRg"  # <-- BOT TOKENINGIZNI shu yerga joylang

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, handle_image))
print("🤖 Bot ishga tushdi...")
app.run_polling()
