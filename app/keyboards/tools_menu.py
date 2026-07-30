from telegram import ReplyKeyboardMarkup

tools_menu = ReplyKeyboardMarkup(
    [
        ["💱 Валюты"],
        ["🌐 Переводчик"],
        ["📏 Конвертер"],
        ["⬅ Назад"],
    ],
    resize_keyboard=True,
)