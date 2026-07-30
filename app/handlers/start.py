from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.main_menu import main_menu
from app.services.user_service import UserService


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_user = update.effective_user

    user = await UserService.get_or_create(
        telegram_id=telegram_user.id,
        first_name=telegram_user.first_name,
    )

    city = user.city if user.city else "не выбран"

    text = (
        "⚡ <b>ZEUS ASSISTANT</b>\n\n"
        f"Добро пожаловать, <b>{telegram_user.first_name}</b>!\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"📍 Город: <b>{city}</b>\n"
        "🌤 Погода\n"
        "💱 Валюты\n"
        "📏 Конвертер\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Выберите раздел:"
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu,
        parse_mode="HTML",
    )