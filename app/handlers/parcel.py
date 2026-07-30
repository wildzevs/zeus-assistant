from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.parcel_menu import parcel_menu
from app.services.parcel_service import ParcelService


async def parcel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "📦 Посылки":

        context.user_data["waiting_track"] = False

        await update.message.reply_text(
            "📦 <b>Посылки</b>\n\n"
            "Выберите действие:",
            reply_markup=parcel_menu,
            parse_mode="HTML",
        )
        return

    if text == "➕ Добавить посылку":

        context.user_data["waiting_track"] = True

        await update.message.reply_text(
            "Введите трек-номер\n\n"
            "Например:\n"
            "<code>RR123456789CN</code>",
            parse_mode="HTML",
        )
        return

    if text == "📋 Мои посылки":

        parcels = await ParcelService.get_user_parcels(
            update.effective_user.id
        )

        if not parcels:
            await update.message.reply_text(
                "📭 У вас пока нет посылок."
            )
            return

        message = "📦 <b>Мои посылки</b>\n\n"

        for i, parcel in enumerate(parcels, start=1):
            message += (
                f"{i}. <code>{parcel.track_number}</code>\n"
                f"Статус: {parcel.status}\n\n"
            )

        await update.message.reply_text(
            message,
            parse_mode="HTML",
        )