from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.current_weather import current_weather
from app.keyboards.weather_menu import weather_menu
from app.providers.weather.open_meteo import get_coordinates
from app.services.user_service import UserService


async def set_city_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    city = update.message.text.strip()

    location = await get_coordinates(city)

    if not location:

        context.user_data["waiting_city"] = True

        await update.message.reply_text(
            "❌ <b>Город не найден.</b>\n\n"
            "Попробуйте ещё раз.\n\n"
            "Например:\n"
            "Москва\n"
            "Санкт-Петербург\n"
            "Ростов-на-Дону",
            parse_mode="HTML",
            reply_markup=weather_menu,
        )
        return

    context.user_data["waiting_city"] = False

    await UserService.update_city(
        telegram_id=update.effective_user.id,
        city=location["name"],
        latitude=location["latitude"],
        longitude=location["longitude"],
        timezone=location["timezone"],
    )

    await update.message.reply_text(
        f"✅ <b>Город изменён:</b> {location['name']}\n\n"
        "🌤 Загружаю текущую погоду...",
        parse_mode="HTML",
        reply_markup=weather_menu,
    )

    await current_weather(update, context)