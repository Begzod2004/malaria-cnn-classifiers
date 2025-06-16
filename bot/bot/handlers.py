from telegram import Update
from telegram.ext import ContextTypes

from src.predict import predict_image
import os

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.photo[-1].get_file()
    if not os.path.exists("media"):
        os.makedirs("media")
    file_path = f"media/{file.file_unique_id}.jpg"
    await file.download_to_drive(file_path)
    result = predict_image(file_path)
    await update.message.reply_text(f"🔬 Tahlil natijasi: {result}")
