import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from tgbot.config import load_config
from tgbot.database.engine import get_session_maker
from tgbot.services.house import HouseService
from tgbot.services.residential_complex import ResidentialComplexService

logger = logging.getLogger(__name__)


def register_all_services(
    db: sessionmaker,
):
    ResidentialComplexService(db)
    HouseService(db)


def register_all_middlewares(dp, config):
    from tgbot.middlewares.admin import AdminIdsMiddleware

    dp.update.middleware(AdminIdsMiddleware(config.tg_bot.admin_ids))


def register_all_filters(dp):
    ...


def register_all_handlers(dp):
    from tgbot.handlers.user.router import user_router
    from tgbot.handlers.common.handlers import common_router
    from tgbot.handlers.admin.router import admin_router

    dp.include_router(admin_router)
    dp.include_router(user_router)
    dp.include_router(common_router)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Starting bot')
    config = load_config('.env')

    postgres_url = URL.create(
        'postgresql+asyncpg',
        username=config.db.user,
        password=config.db.password,
        host=config.db.host,
        database=config.db.database,
        port=config.db.port,
    )

    engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(engine)

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    register_all_services(session_maker)
    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
