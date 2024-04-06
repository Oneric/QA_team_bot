from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config_date.config import Config, load_config
from keyboard.keyboards import create_key
from lexicon_ru import LEXICON_MENU, LEXICON_TIME, LEXICON_CHAT_ID, LEXICON_MAIN_THREADS, LEXICON_QA_THREADS
from time_message import send_message

config: Config = load_config()

router: Router = Router()
keyboard_start = create_key(2, **LEXICON_MENU)

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Погнали.. ', reply_markup=keyboard_start)

@router.message(Command("время"))
async def deach(bot: Bot, message: Message):
    await send_message(bot, LEXICON_CHAT_ID['OFFICE_TOMSK'], LEXICON_TIME['time'], LEXICON_MAIN_THREADS['General'])

@router.message(Command("душно"))
async def deach(bot: Bot):
    await send_message(bot, LEXICON_CHAT_ID['OFFICE_TOMSK'], LEXICON_TIME['window'], LEXICON_MAIN_THREADS['General'])

@router.message(Command("пока"))
async def deach(bot: Bot):
    await send_message(bot, LEXICON_CHAT_ID['OFFICE_TOMSK'], LEXICON_TIME['bye'], LEXICON_MAIN_THREADS['General'])

@router.message(Command("предупреждение"))
async def deach(bot: Bot):
    await send_message(bot, LEXICON_CHAT_ID['OFFICE_TOMSK'], LEXICON_TIME['notification'], LEXICON_MAIN_THREADS['General'])

@router.message(Command("зарядка"))
async def deach(bot: Bot):
    await send_message(bot, LEXICON_CHAT_ID['OFFICE_TOMSK'], LEXICON_TIME['charge'], LEXICON_MAIN_THREADS['General'])

@router.message(Command("тест"))
async def deach(bot: Bot):
    await send_message(bot, LEXICON_CHAT_ID['QA_TEAM'], LEXICON_TIME['test'], LEXICON_QA_THREADS['Флудильня'])