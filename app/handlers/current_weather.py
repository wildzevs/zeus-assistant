from telegram import Update
from telegram.ext import ContextTypes

from app.providers.weather.open_meteo import (
    get_coordinates,
    get_current_weather,
)
from app.services.user_settings import get_city


async def current_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    city = get_city(user_id)

    if city is None:
        await update.message.reply_text(
            "📍 Сначала выберите город через «Изменить город»."
        )
        return

    place = await get_coordinates(city)

    if place is None:
        await update.message.reply_text(
            "❌ Не удалось найти такой город."
        )
        return

    weather = await get_current_weather(
        place["latitude"],
        place["longitude"],
    )

    current = weather["current"]

    await update.message.reply_text(
        f"🌤 {place['name']}\n\n"
        f"🌡 Температура: {current['temperature_2m']}°C\n"
        f"🤚 Ощущается: {current['apparent_temperature']}°C\n"
        f"💧 Влажность: {current['relative_humidity_2m']}%\n"
        f"💨 Ветер: {current['wind_speed_10m']} м/с"
    )