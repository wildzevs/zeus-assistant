from telegram import Update
from telegram.ext import ContextTypes


async def district_weather(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "🚧 Погода по районам находится в разработке."
    )