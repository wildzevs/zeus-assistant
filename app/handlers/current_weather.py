from telegram import Update
from telegram.ext import ContextTypes

from app.providers.weather.open_meteo import get_current_weather
from app.services.user_service import UserService


async def current_weather(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user = await UserService.get_user(
        update.effective_user.id
    )

    if user is None:
        await update.message.reply_text(
            "❌ Пользователь не найден.\n"
            "Нажмите /start."
        )
        return

    weather = await get_current_weather(
        user.latitude,
        user.longitude,
    )

    current = weather["current"]

    await update.message.reply_text(
        f"📍 {user.city}\n\n"
        f"🌡 Температура: {current['temperature_2m']}°C\n"
        f"🤚 Ощущается: {current['apparent_temperature']}°C\n"
        f"💧 Влажность: {current['relative_humidity_2m']}%\n"
        f"💨 Ветер: {current['wind_speed_10m']} м/с"
    )