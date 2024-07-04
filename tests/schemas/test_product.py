from store.schemas.product import ProductIn


def test_schemas_validated():
    product = ProductIn(name="Samsung S20", quantity=10, price=4.500, status=True)

    assert product.name == "Samsung S20"