from telegram import Update
from telegram.ext import ContextTypes

from app.services.currency_converter import convert
from app.services.currency_parser import parse_currency


async def converter(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = update.message.text

    if text == "💱 Конвертер":

        context.user_data["waiting_converter"] = True

        await update.message.reply_text(
            "💱 <b>Конвертер валют</b>\n\n"
            "Введите сумму вместе с валютой.\n\n"
            "Например:\n\n"
            "100$\n"
            "250€\n"
            "15000₽\n"
            "1000 юаней",
            parse_mode="HTML",
        )

        return

    parsed = parse_currency(text)

    if not parsed:

        await update.message.reply_text(
            "❌ Не удалось распознать сумму.\n\n"
            "Примеры:\n"
            "100$\n"
            "250€\n"
            "15000₽\n"
            "1000 юаней"
        )

        context.user_data["waiting_converter"] = True

        return

    amount, currency = parsed

    result = await convert(amount, currency)

    flags = {
        "RUB": "🇷🇺",
        "USD": "🇺🇸",
        "EUR": "🇪🇺",
        "CNY": "🇨🇳",
        "KZT": "🇰🇿",
    }

    symbols = {
        "RUB": "₽",
        "USD": "$",
        "EUR": "€",
        "CNY": "¥",
        "KZT": "₸",
    }

    def fmt(value):
        return f"{value:,.2f}".replace(",", " ").replace(".", ",")

    text = (
        "💱 <b>Конвертация</b>\n\n"
        f"{flags[currency]} <b>{fmt(amount)} {symbols[currency]}</b>\n\n"
    )

    for code in ["RUB", "USD", "EUR", "CNY", "KZT"]:

        if code == currency:
            continue

        text += (
            f"{flags[code]} "
            f"{fmt(result[code])} {symbols[code]}\n"
        )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
    )