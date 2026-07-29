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
from app.handlers.current_weather import current_weather
from app.handlers.set_city import set_city_handler
from app.handlers.start import start
from app.handlers.weather import change_city, weather


async def city_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("waiting_city"):
        context.user_data["waiting_city"] = False
        await set_city_handler(update, context)


async def post_init(application: Application):
    await init_db()
    print("✅ База данных готова")


def main():
    if not settings.bot_token:
        raise ValueError("BOT_TOKEN не указан в файле .env")

    application = (
        Application.builder()
        .token(settings.bot_token)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", start))

    application.add_handler(
        MessageHandler(filters.Regex("^🌤 Погода$"), weather)
    )

    application.add_handler(
        MessageHandler(filters.Regex("^📍 Изменить город$"), change_city)
    )

    application.add_handler(
        MessageHandler(filters.Regex("^☀ Сейчас$"), current_weather)
    )

    application.add_handler(
        MessageHandler(filters.Regex("^⬅ Назад$"), back)
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            city_router,
        )
    )

    print("🚀 Zeus Assistant запускается...")

    application.run_polling()


if __name__ == "__main__":
    main()