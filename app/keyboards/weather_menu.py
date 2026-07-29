from telegram import ReplyKeyboardMarkup

weather_menu = ReplyKeyboardMarkup(
    [
        ["☀ Сейчас"],
        ["📅 Сегодня", "🗓 Неделя"],
        ["📍 Изменить город"],
        ["⬅ Назад"],
    ],
    resize_keyboard=True,
)