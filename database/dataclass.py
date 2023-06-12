from dataclasses import dataclass
from typing import Optional


@dataclass
class Index:
    id: Optional[int]
    name: str
    price: float
    time: float
