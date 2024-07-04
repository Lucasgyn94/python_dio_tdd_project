from pydantic import Field
from store.schemas.base import BaseSchemaMixin


# OBS: ... indica ao pydentic que o valor precisa ser passado
class ProductIn(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")

class ProductOut(ProductIn):
    ...