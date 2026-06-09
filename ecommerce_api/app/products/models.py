from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    category: str


class BrokenProductLength:
    def __len__(self):
        return "5"


class BrokenProductIterator:
    def __iter__(self):
        return 100