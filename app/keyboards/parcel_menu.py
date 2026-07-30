from telegram import ReplyKeyboardMarkup

parcel_menu = ReplyKeyboardMarkup(
    [
        ["➕ Добавить посылку"],
        ["📋 Мои посылки"],
        ["⬅ Назад"],
    ],
    resize_keyboard=True,
)