from datetime import datetime

from aiogram import Bot

from config_date.config import Config, load_config

config: Config = load_config()


async def send_message(bot: Bot, chat_id: int, message: str, message_thread_id: int):
    await bot.send_message(chat_id, message, message_thread_id)
