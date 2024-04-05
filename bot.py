import asyncio
import logging
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from background import keep_alive
from Handlers import other_handlers
from time_message import send_message
from datetime import datetime
from config_date.config import *
from lexicon_ru import LEXICON_TIME, LEXICON_MAIN_THREADS, LEXICON_QA_THREADS, LEXICON_CHAT_ID

logger = logging.getLogger(__name__)


async def main() -> None:
    # Логирование

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s'
        '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Start bot work')
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.tg_token)
    dp: Dispatcher = Dispatcher()

    scheduler = AsyncIOScheduler(timezone="Asia/Tomsk")
    scheduler.add_job(send_message, trigger='cron', day_of_week='mon-fri', hour=11, minute=30,
                      start_date=datetime.now(), kwargs={'bot': bot,
                                                         'chat_id': LEXICON_CHAT_ID['OFFICE_TOMSK'],
                                                         'message': LEXICON_TIME['time'],
                                                         'message_thread_id': LEXICON_MAIN_THREADS['General'],
                                                         })
    scheduler.add_job(send_message, trigger='cron', day_of_week='mon-fri', hour=9, minute=59,
                      start_date=datetime.now(), kwargs={'bot': bot,
                                                         'chat_id': LEXICON_CHAT_ID['OFFICE_TOMSK'],
                                                         'message': LEXICON_TIME['window'],
                                                         'message_thread_id': LEXICON_MAIN_THREADS['General'],
                                                         })
    scheduler.add_job(send_message, trigger='cron', day_of_week='mon-fri', hour=10, minute=59,
                      start_date=datetime.now(), kwargs={'bot': bot,
                                                         'chat_id': LEXICON_CHAT_ID['OFFICE_TOMSK'],
                                                         'message': LEXICON_TIME['charge'],
                                                         'message_thread_id': LEXICON_MAIN_THREADS['General'],
                                                         })
    # scheduler.add_job(send_message, trigger='cron', day_of_week='mon-fri', hour=12, minute=30,
    #                     start_date=datetime.now(), kwargs={'bot': bot,
    #                                                          'chat_id': LEXICON_CHAT_ID['OFFICE_TOMSK'],
    #                                                          'message': LEXICON_TIME['window'],
    #                                                          'message_thread_id': LEXICON_MAIN_THREADS['General'],
    #                                                          })
    scheduler.add_job(send_message, trigger='cron', day_of_week='mon-fri', hour=19, minute=10,
                      start_date=datetime.now(), kwargs={'bot': bot,
                                                         'chat_id': LEXICON_CHAT_ID['OFFICE_TOMSK'],
                                                         'message': LEXICON_TIME['notification'],
                                                         'message_thread_id': LEXICON_MAIN_THREADS['General'],
                                                         })
    scheduler.add_job(send_message, trigger='cron', day_of_week='mon-fri', hour=16, minute=59,
                      start_date=datetime.now(), kwargs={'bot': bot,
                                                         'chat_id': LEXICON_CHAT_ID['OFFICE_TOMSK'],
                                                         'message': LEXICON_TIME['window'],
                                                         'message_thread_id': LEXICON_MAIN_THREADS['General'],
                                                         })
    scheduler.add_job(send_message, trigger='cron', day_of_week='fri', hour=19, minute=00,
                      start_date=datetime.now(), kwargs={'bot': bot,
                                                         'chat_id': LEXICON_CHAT_ID['OFFICE_TOMSK'],
                                                         'message': LEXICON_TIME['bye'],
                                                         'message_thread_id': LEXICON_MAIN_THREADS['General'],
                                                         })
    scheduler.start()

    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

keep_alive()


if __name__ == '__main__':
    asyncio.run(main())