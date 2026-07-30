from telegram import Update
from telegram.ext import ContextTypes

from app.providers.weather.open_meteo import get_current_weather
from app.services.user_service import UserService


async def today_weather(
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

    if (
        user.latitude is None
        or user.longitude is None
    ):
        await update.message.reply_text(
            "📍 Сначала выберите город."
        )
        return

    weather = await get_current_weather(
        user.latitude,
        user.longitude,
    )

    current = weather["current"]
    daily = weather["daily"]

    sunrise = daily["sunrise"][0][11:16]
    sunset = daily["sunset"][0][11:16]

    text = (
        f"📍 <b>{user.city}</b>\n\n"
        f"📅 <b>Сегодня</b>\n\n"
        f"🌡 Сейчас: <b>{current['temperature_2m']}°C</b>\n"
        f"⬆ Максимум: {daily['temperature_2m_max'][0]}°C\n"
        f"⬇ Минимум: {daily['temperature_2m_min'][0]}°C\n\n"
        f"🌧 Осадки: {daily['precipitation_probability_max'][0]}%\n"
        f"💨 Ветер: {current['wind_speed_10m']} м/с\n\n"
        f"🌅 Восход: {sunrise}\n"
        f"🌇 Закат: {sunset}"
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
    )