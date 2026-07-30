from telegram import ReplyKeyboardMarkup

currency_menu = ReplyKeyboardMarkup(
    [
        ["💱 Конвертер"],
        ["📊 Курсы ЦБ РФ"],
        ["🏠 Главное меню"],
    ],
    resize_keyboard=True,
)