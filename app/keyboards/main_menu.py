from telegram import ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    [
        ["🌤 Погода"],
        ["🛠 Инструменты"],
        ["📦 Посылки"],
        ["⚙ Настройки", "ℹ️ О боте"],
    ],
    resize_keyboard=True,
)