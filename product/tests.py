from django.test import TestCase, RequestFactory
from product.models import Product
from product.viewset import ProductViewset


class ProductTest(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(
            name="Test product",
            description="Test description",
            price=450,
        )
        self.product2 = Product.objects.create(
            name="Test product 2",
            description="Test description 2",
            price=5500,
        )

        self.factory = RequestFactory()

    def test_list_products(self):
        request = self.factory.get("/products/")
        response = ProductViewset.as_view({"get": "list"})(request)

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], self.product.name)
        self.assertEqual(response.data[1]["name"], self.product2.name)
