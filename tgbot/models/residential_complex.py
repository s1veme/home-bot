from dataclasses import dataclass
from typing import Optional

from tgbot.models.house import House


@dataclass
class ResidentialComplex:
    title: str
    house: list[House]
    district: str

    id: Optional[int] = None
