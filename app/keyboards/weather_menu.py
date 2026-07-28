from telegram import ReplyKeyboardMarkup

weather_menu = ReplyKeyboardMarkup(
    [
        ["📅 Сегодня", "🗓 Неделя"],
        ["📍 Сменить город"],
        ["⬅ Назад"],
    ],
    resize_keyboard=True,
)