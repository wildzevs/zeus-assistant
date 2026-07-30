from telegram import ReplyKeyboardMarkup

weather_menu = ReplyKeyboardMarkup(
    [
        ["☀ Сейчас", "📅 Сегодня"],
        ["🗓 Неделя", "🗺 Районы"],
        ["📍 Изменить город"],
        ["🏠 Главное меню"],
    ],
    resize_keyboard=True,
)