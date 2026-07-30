from telegram import ReplyKeyboardMarkup

tools_menu = ReplyKeyboardMarkup(
    [
        ["💱 Валюты"],
        ["📏 Конвертер"],
        ["⬅ Назад"],
    ],
    resize_keyboard=True,
)