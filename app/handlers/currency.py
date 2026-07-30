from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.currency_menu import currency_menu
from app.providers.currency.cbr import get_rates


async def currency(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    context.user_data["waiting_converter"] = False

    text = update.message.text

    if text in ("💰 Валюты", "💱 Валюты"):

        await update.message.reply_text(
            "💱 <b>Валюты</b>\n\n"
            "Выберите действие:",
            reply_markup=currency_menu,
            parse_mode="HTML",
        )
        return

    if text == "📊 Курсы ЦБ РФ":

        rates = await get_rates()

        await update.message.reply_text(
            "💱 <b>Курсы ЦБ РФ</b>\n\n"
            f"🇺🇸 <b>USD</b> — {rates['USD']:.2f} ₽\n"
            f"🇪🇺 <b>EUR</b> — {rates['EUR']:.2f} ₽\n"
            f"🇨🇳 <b>CNY</b> — {rates['CNY']:.2f} ₽\n"
            f"🇰🇿 <b>KZT</b> — {rates['KZT']:.2f} ₽\n\n"
            f"🕒 Обновлено:\n"
            f"{rates['updated']}",
            parse_mode="HTML",
        )