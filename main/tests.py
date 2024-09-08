from django.test import TestCase, Client
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get("/")
        self.assertTemplateUsed(response, "main.html")

    def test_nonexistent_page(self):
        response = Client().get("/nonexistent/")
        self.assertEqual(response.status_code, 404)

    def test_product_model(self):
        product = Product.objects.create(
            name="Product Name",
            price=1000000.00,
            description="Product Description",
            stock=10,
        )

        product2 = Product.objects.get(pk=product.id)
        self.assertEqual(product, product2)

    def test_product_is_available(self):
        product = Product.objects.create(
            name="Product Name",
            price=1000000.00,
            description="Product Description",
            stock=10,
        )

        self.assertTrue(product.is_available)