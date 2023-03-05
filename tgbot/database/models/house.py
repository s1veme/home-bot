from sqlalchemy import Column, ForeignKey, Integer, Text

from tgbot.database.base import BaseModel


class HouseModel(BaseModel):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)

    start_house = Column(Integer, nullable=False)
    end_house = Column(Integer, nullable=False)
    link_chat = Column(Text, nullable=False)
    residential_complex_id = Column(Integer, ForeignKey('residential_complexes.id', ondelete='CASCADE'))
