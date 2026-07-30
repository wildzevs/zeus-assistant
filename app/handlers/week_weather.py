from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

from app.providers.weather.open_meteo import get_week_weather
from app.services.user_service import UserService
from app.utils.weather_codes import WEATHER_CODES


MONTHS = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря",
]


async def week_weather(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user = await UserService.get_user(
        update.effective_user.id
    )

    if user is None:
        await update.message.reply_text(
            "❌ Пользователь не найден.\nНажмите /start."
        )
        return

    if user.latitude is None or user.longitude is None:
        await update.message.reply_text(
            "📍 Сначала выберите город."
        )
        return

    weather = await get_week_weather(
        user.latitude,
        user.longitude,
    )

    daily = weather["daily"]

    weekdays = [
        "Пн",
        "Вт",
        "Ср",
        "Чт",
        "Пт",
        "Сб",
        "Вс",
    ]

    text = (
        f"📅 <b>Прогноз на неделю</b>\n"
        f"📍 <b>{user.city}</b>\n\n"
    )

    for i in range(len(daily["time"])):

        date = datetime.strptime(
            daily["time"][i],
            "%Y-%m-%d",
        )

        if i == 0:
            day = "Сегодня"
        elif i == 1:
            day = "Завтра"
        else:
            day = weekdays[date.weekday()]

        date_text = f"{date.day} {MONTHS[date.month-1]}"

        code = daily["weather_code"][i]

        emoji, description = WEATHER_CODES.get(
            code,
            ("🌤", "Неизвестно"),
        )

        temp_max = round(
            daily["temperature_2m_max"][i]
        )

        temp_min = round(
            daily["temperature_2m_min"][i]
        )

        rain = daily[
            "precipitation_probability_max"
        ][i]

        text += (
            f"{emoji} <b>{day}</b>, {date_text}\n"
            f"└ {description}\n"
            f"🌡 {temp_max}° / {temp_min}°"
            f"   ☔ {rain}%\n\n"
        )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
    )