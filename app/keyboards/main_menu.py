from telegram import ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    [
        ["🌤 Погода"],
        ["🛠 Инструменты"],
        ["⚙ Настройки", "ℹ️ О боте"],
    ],
    resize_keyboard=True,
)