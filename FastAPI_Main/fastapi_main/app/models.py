
from pydantic import BaseModel

# Product model representing the product entity

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
