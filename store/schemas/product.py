from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import UUID4, AfterValidator, Field
from store.schemas.base import BaseSchemaMixin, OutMixin

class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")

class ProductIn(ProductBase, BaseSchemaMixin):
    ...

class ProductOut(ProductIn, OutMixin):
    ...

def convert_decimal_128(v):
    if isinstance(v, Decimal128):
        return Decimal(str(v.to_decimal()))
    return v

Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]

class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal_] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")

class ProductUpdateOut(ProductUpdate):
    ...
