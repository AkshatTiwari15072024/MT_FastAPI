
from pydantic import BaseModel

# Schema for creating a new product
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

# Schema for returning a product, includes an ID
class Product(ProductCreate):
    id: int
