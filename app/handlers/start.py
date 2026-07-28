from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.main_menu import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Я Zeus Assistant.\n"
        "Пока я умею немного, но скоро научусь:\n\n"
        "🌤 Показывать погоду\n"
        "💰 Показывать курсы валют\n"
        "📦 Отслеживать посылки\n\n"
        "Выбери действие:",
        reply_markup=main_menu,
    )