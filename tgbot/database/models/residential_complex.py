from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType

from tgbot.database.base import BaseModel


class ResidentialComplexModel(BaseModel):
    __tablename__ = 'residential_complexes'

    DISTRICTS = [
        ('Заельцовский', 'Заельцовский'),
        ('Калининский', 'Калининский'),
        ('Центральный', 'Центральный'),
        ('Дзержинский', 'Дзержинский'),
        ('Октябрьский', 'Октябрьский'),
        ('Ленинский', 'Ленинский'),
        ('Кировский', 'Кировский'),
        ('Первомайский', 'Первомайский'),
        ('Советский', 'Советский'),
        ('Железнодорожный', 'Железнодорожный'),
    ]

    id = Column(Integer, primary_key=True)

    title = Column(Text, nullable=False)
    house = relationship('HouseModel')

    district = Column(ChoiceType(DISTRICTS), nullable=False)
