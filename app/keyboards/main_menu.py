from telegram import ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    [
        ["🌤 Погода", "💱 Валюты"],
        ["📏 Конвертер", "⚙ Настройки"],
        ["ℹ️ О боте"],
    ],
    resize_keyboard=True,
)