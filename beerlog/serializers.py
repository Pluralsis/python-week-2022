from datetime import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class BeerOut(BaseModel):
    """BeerOut Class Object"""
    id: int
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime


class BeerIn(BaseModel):
    name: str
    style: str
    flavor: int
    image: int
    cost: int

    @validator("flavor", "image", "cost")
    @classmethod
    def validate_ratings(cls, v, field):
        """Validate"""
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return v
