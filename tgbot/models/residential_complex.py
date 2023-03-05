from dataclasses import dataclass
from typing import Optional

from tgbot.models.house import House


@dataclass
class ResidentialComplex:
    title: str
    district: str

    house: Optional[list[House]] = None
    id: Optional[int] = None
