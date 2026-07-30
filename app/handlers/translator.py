from telegram import Update
from telegram.ext import ContextTypes


async def translator(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "🌐 <b>Переводчик</b>\n\n"
        "Выберите язык:\n\n"
        "🇬🇧 Английский\n"
        "🇫🇷 Французский\n"
        "🇨🇳 Китайский\n\n"
        "🚧 Раздел находится в разработке.",
        parse_mode="HTML",
    )