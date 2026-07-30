import logging
import traceback

from telegram import Update
from telegram.ext import ContextTypes


logger = logging.getLogger(__name__)


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
):

    logger.error(
        "========== ZEUS ERROR =========="
    )

    logger.error(
        "".join(
            traceback.format_exception(
                None,
                context.error,
                context.error.__traceback__,
            )
        )
    )

    if isinstance(update, Update):

        if update.effective_user:

            logger.error(
                f"User: {update.effective_user.id}"
            )

        if update.effective_message:

            await update.effective_message.reply_text(
                "⚠️ Произошла ошибка.\n\n"
                "Разработчик уже увидит её в логах.\n"
                "Попробуйте ещё раз через несколько секунд."
            )