from aiogram import types
from aiogram.filters import BaseFilter


class IsAdminFilter(BaseFilter):
    async def __call__(self, message: types.Message, admin_ids: list[int]) -> bool:
        return message.from_user.id in admin_ids
