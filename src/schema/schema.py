
#  ---------------------------------------------------------------------------------
from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    Product Name: str
    product Description: str
    Product Category: str
    Product Price: str

class ProductAdd(ProdcutBase):
    product_id: str

    Used_for: Optional[str] = None
    In_use: bool

    class Config:
        orm_mode = True


class Product(ProductAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateProduct(BaseModel):

    Used_for: Optional[str] = None
    In_use: bool

    class Config:
        orm_mode = True