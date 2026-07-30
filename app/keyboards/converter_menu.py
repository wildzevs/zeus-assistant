from telegram import ReplyKeyboardMarkup

converter_menu = ReplyKeyboardMarkup(
    [
        ["🌡 Температура", "📏 Длина"],
        ["⚖ Вес", "🧴 Объём"],
        ["🚗 Скорость", "⏱ Время"],
        ["⬅ Назад"],
    ],
    resize_keyboard=True,
)