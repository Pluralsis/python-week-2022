# from dataclasses import dataclass # Define objectos empython como class de dados
from datetime import datetime
from statistics import mean
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel


# @dataclass
class Beer(SQLModel, table=True):  # ORM - SALOuckmi
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @classmethod
    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @classmethod
    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=10)
