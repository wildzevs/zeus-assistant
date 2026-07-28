from telegram import ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    [
        ["🌤 Погода", "💰 Валюты"],
        ["📦 Посылки"],
        ["⚙ Настройки", "ℹ️ О боте"],
    ],
    resize_keyboard=True,
)