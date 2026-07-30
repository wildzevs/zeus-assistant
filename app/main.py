import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from app.config import settings
from app.database.init_db import init_db

from app.handlers.back import back
from app.handlers.converter import converter
from app.handlers.currency import currency
from app.handlers.current_weather import current_weather
from app.handlers.district_weather import district_weather
from app.handlers.error_handler import error_handler
from app.handlers.set_city import set_city_handler
from app.handlers.start import start
from app.handlers.today_weather import today_weather
from app.handlers.weather import change_city, weather
from app.handlers.week_weather import week_weather


logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def city_router(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if context.user_data.get("waiting_city"):
        context.user_data["waiting_city"] = False
        await set_city_handler(update, context)
        return

    if context.user_data.get("waiting_converter"):
        await converter(update, context)
        return


async def post_init(application: Application):
    await init_db()
    logger.info("✅ База данных готова")


def main():

    if not settings.bot_token:
        raise ValueError("BOT_TOKEN не указан")

    application = (
        Application.builder()
        .token(settings.bot_token)
        .post_init(post_init)
        .build()
    )

    application.add_error_handler(error_handler)

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^🌤 Погода$"),
            weather,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^☀ Сейчас$"),
            current_weather,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^📅 Сегодня$"),
            today_weather,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^🗓 Неделя$"),
            week_weather,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^🗺 Районы$"),
            district_weather,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^📍 Изменить город$"),
            change_city,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^💱 Валюты$"),
            currency,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^💱 Конвертер$"),
            converter,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^📊 Курсы ЦБ РФ$"),
            currency,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^🏠 Главное меню$"),
            start,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.Regex("^⬅ Назад$"),
            back,
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            city_router,
        )
    )

    logger.info("🚀 Zeus Assistant запускается...")

    application.run_polling()


if __name__ == "__main__":
    main()