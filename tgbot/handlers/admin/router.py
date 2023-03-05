from aiogram import Router
from aiogram.filters import Command

from tgbot.filters.admin import IsAdminFilter
from tgbot.handlers.admin.residential_complex.handlers import router as residential_complex_router
from tgbot.handlers.admin.house.handlers import router as house_router
from tgbot.handlers.admin.start import start

admin_router = Router()


admin_router.message.register(start, Command('start'))

admin_router.include_router(residential_complex_router)
admin_router.include_router(house_router)

admin_router.message.filter(IsAdminFilter())
admin_router.callback_query.filter(IsAdminFilter())
