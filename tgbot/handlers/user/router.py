from aiogram import Router
from aiogram.filters import Command

from tgbot.handlers.user.handlers import router
from tgbot.handlers.user.start import start

user_router = Router()
user_router.message.register(start, Command('start'))

user_router.include_router(router)
