from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.converter_menu import converter_menu


async def unit_converter(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = update.message.text

    if text == "📏 Конвертер":

        context.user_data["waiting_converter"] = False

        await update.message.reply_text(
            "📏 <b>Конвертер единиц</b>\n\n"
            "Выберите категорию:",
            reply_markup=converter_menu,
            parse_mode="HTML",
        )

        return

    if text == "🌡 Температура":

        await update.message.reply_text(
            "🌡 <b>Температура</b>\n\n"
            "Скоро будет доступно.\n\n"
            "Первой появится конвертация:\n"
            "• °C\n"
            "• °F\n"
            "• K",
            parse_mode="HTML",
        )
        return

    if text == "📏 Длина":

        await update.message.reply_text(
            "📏 <b>Длина</b>\n\n"
            "Скоро будет доступно.",
            parse_mode="HTML",
        )
        return

    if text == "⚖ Вес":

        await update.message.reply_text(
            "⚖ <b>Вес</b>\n\n"
            "Скоро будет доступно.",
            parse_mode="HTML",
        )
        return

    if text == "🧴 Объём":

        await update.message.reply_text(
            "🧴 <b>Объём</b>\n\n"
            "Скоро будет доступно.",
            parse_mode="HTML",
        )
        return

    if text == "🚗 Скорость":

        await update.message.reply_text(
            "🚗 <b>Скорость</b>\n\n"
            "Скоро будет доступно.",
            parse_mode="HTML",
        )
        return

    if text == "⏱ Время":

        await update.message.reply_text(
            "⏱ <b>Время</b>\n\n"
            "Скоро будет доступно.",
            parse_mode="HTML",
        )
        return