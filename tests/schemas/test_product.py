from pydantic import ValidationError

import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Samsung S40 Pro Max"


def test_schemas_return_raise():
    data = {"name": "Samsung S40 Pro Max", "quantity": 10, "price": 8.500}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Samsung S40 Pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.8/v/missing",
    }