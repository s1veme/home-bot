from dataclasses import asdict

from sqlalchemy import insert, select
from sqlalchemy.orm import sessionmaker

from tgbot.database import HouseModel
from tgbot.models.house import House
from tgbot.services.base import SingletonService


class HouseService(SingletonService):
    def __init__(self, session_maker: sessionmaker) -> None:
        self.session_maker = session_maker

    async def get_houses_by_residential_complex(self, residential_complex_id: int) -> list[House]:
        query = select(HouseModel).filter(HouseModel.residential_complex_id == residential_complex_id)

        async with self.session_maker() as session:
            models: list[HouseModel] = await session.scalars(query)

        return self.models_to_domain(models)

    async def get_house_by_id(self, house_id: int) -> House:
        query = select(HouseModel).filter(HouseModel.id == house_id)

        async with self.session_maker() as session:
            model: HouseModel = await session.scalar(query)

        return self.model_to_domain(model)

    async def create(self, house: House) -> None:
        query = insert(HouseModel)

        async with self.session_maker() as session:
            await session.execute(query, asdict(house))
            await session.commit()

    @classmethod
    def models_to_domain(cls, models: list[HouseModel], **kwargs) -> list[House]:
        return [cls.model_to_domain(model) for model in models]

    @staticmethod
    def model_to_domain(model: HouseModel) -> House:
        return House(
            id=model.id,
            start_house=model.start_house,
            end_house=model.end_house,
            link_chat=model.link_chat,
            residential_complex_id=model.residential_complex_id,
        )
