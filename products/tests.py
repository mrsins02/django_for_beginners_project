from django.test import TestCase
from django.urls import reverse
from .models import Product, Category, Color, Size, Brand


class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(category="test category")
        cls.brand = Brand.objects.create(brand="test brand")
        cls.color = Color.objects.create(color_name="test color",
                                         color_code="#111111")
        cls.size = Size.objects.create(size="test size")
        cls.product = Product.objects.create(name="test product name",
                                             category_id=1,
                                             brand_id=1)

    def test_slug(self):
        self.assertEqual(self.category.slug, "test-category")
        self.assertEqual(self.brand.slug, "test-brand")
        self.assertEqual(self.color.slug, "test-color")
        self.assertEqual(self.size.slug, "test-size")
        self.assertEqual(self.product.slug, "test-product-name")

    def test_product_list(self):
        response = self.client.get("/shop/")
        reverse_response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "products/product-list.html")
