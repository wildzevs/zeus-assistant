from telegram import Update
from telegram.ext import ContextTypes

from app.providers.weather.open_meteo import get_coordinates
from app.services.user_service import UserService


async def set_city_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    city = update.message.text.strip()

    location = await get_coordinates(city)

    if not location:
        await update.message.reply_text(
            "❌ Город не найден.\n"
            "Попробуйте ввести название еще раз."
        )
        return

    await UserService.update_city(
        telegram_id=update.effective_user.id,
        city=location["name"],
        latitude=location["latitude"],
        longitude=location["longitude"],
        timezone=location["timezone"],
    )

    await update.message.reply_text(
        f"✅ Город изменен на: {location['name']}\n\n"
        "Теперь нажмите ☀ Сейчас."
    )