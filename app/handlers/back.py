from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.main_menu import main_menu


async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["waiting_city"] = False

    await update.message.reply_text(
        "🏠 Главное меню",
        reply_markup=main_menu,
    )