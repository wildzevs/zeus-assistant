from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.tools_menu import tools_menu


async def tools(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "🛠 <b>Инструменты</b>\n\n"
        "Выберите нужный раздел:",
        reply_markup=tools_menu,
        parse_mode="HTML",
    )