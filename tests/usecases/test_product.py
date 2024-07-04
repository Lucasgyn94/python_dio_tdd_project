from store.schemas.product import ProductOut
from store.usecases.product import product_usecase

async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Samsung S20"

async def test_usecases_get_should_return_success(inserted_product, product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Samsung S20"
