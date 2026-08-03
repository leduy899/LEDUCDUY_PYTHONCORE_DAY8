from pydantic import BaseModel, ConfigDict
from decimal import Decimal

class BookBase(BaseModel):
    code: str
    title: str
    price: Decimal
    pages: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
