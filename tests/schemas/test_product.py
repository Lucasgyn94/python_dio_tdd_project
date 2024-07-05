from uuid import UUID

from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_validated():
    data = product_data()
    #product = ProductIn(**data)
    product = ProductIn.model_validate(data)

    assert product.name == "Samsung S20"


def test_schemas_return_raise():
    data = {"name": "Samsung S20", "quantity": 10, "price": 4.500}

    with pytest.raises(ValidationError) as err:
        ProductIn(**data)  

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Samsung S20", "quantity": 10, "price": 4.5},
        "url": "https://errors.pydantic.dev/2.8/v/missing"
    }