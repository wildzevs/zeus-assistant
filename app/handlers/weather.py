from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.weather_menu import weather_menu


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["waiting_city"] = False

    await update.message.reply_text(
        "🌤 Модуль погоды\n\n"
        "Выберите действие:",
        reply_markup=weather_menu,
    )


async def change_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["waiting_city"] = True

    await update.message.reply_text(
        "📍 Введите название города.\n\n"
        "Например:\n"
        "Москва\n"
        "Санкт-Петербург\n"
        "Ростов-на-Дону"
    )