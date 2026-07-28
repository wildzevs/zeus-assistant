from telegram import Update
from telegram.ext import ContextTypes

from app.services.user_settings import set_city


async def set_city_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text.strip()

    set_city(update.effective_user.id, city)

    await update.message.reply_text(
        f"✅ Город сохранён: {city}\n\n"
        "Теперь нажмите «☀ Сейчас»."
    )