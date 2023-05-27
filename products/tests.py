from django.test import TestCase
from django.urls import reverse
from .models import Product, Category, Brand


class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(category="test category")
        cls.brand = Brand.objects.create(brand="test brand")
        cls.product = Product.objects.create(name="test product name",
                                             category_id=1,
                                             brand_id=1)

    def test_slug(self):
        self.assertEqual(self.category.slug, "test-category")
        self.assertEqual(self.brand.slug, "test-brand")
        self.assertEqual(self.product.slug, "test-product-name")

    def test_product_list(self):
        response = self.client.get("/shop/")
        reverse_response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "products/product-list.html")

    def test_product_detail(self):
        response = self.client.get("/shop/products/test-product-name/")
        reverse_response = self.client.get(reverse("product_detail", kwargs={"slug": self.product.slug}))

        # for no response testing
        no_response = self.client.get("/shop/products/test-product-name404/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse_response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(reverse_response, "products/product-detail.html")
