from dataclasses import dataclass
from typing import Optional


@dataclass
class House:
    start_house: int
    end_house: int
    link_chat: str
    residential_complex_id: int

    id: Optional[int] = None
