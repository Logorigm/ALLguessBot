import logging

from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

TOKEN = ""

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request
    try:
        await req.approve()
        logger.info(
            "Принята заявка: %s (id=%s) в чат %s",
            req.from_user.full_name,
            req.from_user.id,
            req.chat.title,
        )
    except Exception as e:
        logger.error("Не удалось принять заявку %s: %s", req.from_user.id, e)


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(approve_request))
    logger.info("Бот запущен")
    app.run_polling(allowed_updates=[Update.CHAT_JOIN_REQUEST])


if __name__ == "__main__":
    main()
