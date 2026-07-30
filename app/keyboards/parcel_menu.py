from telegram import ReplyKeyboardMarkup

parcel_menu = ReplyKeyboardMarkup(
    [
        ["➕ Добавить посылку"],
        ["📋 Мои посылки"],
        ["❌ Удалить посылку"],
        ["⬅ Назад"],
    ],
    resize_keyboard=True,
)