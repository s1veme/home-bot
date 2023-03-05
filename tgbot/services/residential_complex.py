from dataclasses import asdict

from sqlalchemy import delete, insert, select
from sqlalchemy.orm import selectinload, sessionmaker

from tgbot.database.models.residential_complex import ResidentialComplexModel
from tgbot.models.residential_complex import ResidentialComplex
from tgbot.services.base import SingletonService
from tgbot.services.house import HouseService


class ResidentialComplexService(SingletonService):
    def __init__(self, session_maker: sessionmaker) -> None:
        self.session_maker = session_maker

    async def get_all_residential_complex_by_district(self, district: str) -> list[ResidentialComplex]:
        query = (
            select(ResidentialComplexModel)
            .filter(ResidentialComplexModel.district == district)
            .options(selectinload(ResidentialComplexModel.house))
        )

        async with self.session_maker() as session:
            models: list[ResidentialComplexModel] = await session.scalars(query)

        return self.models_to_domain(models)

    async def create(self, residential_complex: ResidentialComplex) -> None:
        query = insert(ResidentialComplexModel)

        async with self.session_maker() as session:
            await session.execute(query, asdict(residential_complex))
            await session.commit()

    async def delete(self, residential_complex_id: int) -> None:
        query = delete(ResidentialComplexModel).filter(ResidentialComplexModel.id == residential_complex_id)

        async with self.session_maker() as session:
            await session.execute(query)
            await session.commit()

    async def get_residential_complex_by_id(self, id: int) -> ResidentialComplex:
        query = select(ResidentialComplexModel).filter(ResidentialComplexModel.id == id)

        async with self.session_maker() as session:
            model: ResidentialComplex = await session.scalar(query)

        return self.model_to_domain(model)

    @classmethod
    def models_to_domain(cls, models: list[ResidentialComplexModel], **kwargs) -> list[ResidentialComplex]:
        return [cls.model_to_domain(model, **kwargs) for model in models]

    @staticmethod
    def model_to_domain(model: ResidentialComplexModel, is_house: bool = True) -> ResidentialComplex:
        model = ResidentialComplex(
            id=model.id,
            district=model.district,
            title=model.title,
            house=model.house,
        )

        if is_house:
            model.house = HouseService.models_to_domain(model.house)

        return model
