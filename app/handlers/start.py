from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.main_menu import main_menu
from app.services.user_service import UserService


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user = update.effective_user

    await UserService.get_or_create(
        telegram_id=user.id,
        first_name=user.first_name,
    )

    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!\n\n"
        "Я Zeus Assistant.\n"
        "Пока я умею немного, но скоро научусь:\n\n"
        "🌤 Показывать погоду\n"
        "💰 Показывать курсы валют\n"
        "📦 Отслеживать посылки\n\n"
        "Выбери действие:",
        reply_markup=main_menu,
    )