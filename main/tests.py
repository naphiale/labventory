from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        # Set up two test products
        Product.objects.create(
            name="Microscope X200",
            price=2000000,
            description="High-quality microscope suitable for research and education purposes.",
            rating=4
        )
        Product.objects.create(
            name="Centrifuge 3000 RPM",
            price=5000000,
            description="High-speed centrifuge for separating fluids and gases based on density.",
            rating=5
        )

    def test_product_str(self):
        # Test the string representation of a product
        product = Product.objects.get(name="Microscope X200")
        self.assertEqual(str(product), "Microscope X200")

    def test_product_formatted_price(self):
        # Test the formatted price property
        product = Product.objects.get(name="Centrifuge 3000 RPM")
        self.assertEqual(product.formatted_price, "Rp 5,000,000")

    def test_product_rating_stars(self):
        # Test the rating_stars property
        product = Product.objects.get(name="Microscope X200")
        self.assertEqual(product.rating_stars, "⭐⭐⭐⭐")

class ProductViewTest(TestCase):
    def setUp(self):
        # Create a test product for the view test
        Product.objects.create(
            name="Autoclave Sterilizer",
            price=7000000,
            description="Compact autoclave for sterilization in laboratories.",
            rating=4
        )

    def test_show_main_view(self):
        # Test that the main view renders correctly
        response = self.client.get(reverse('show_main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, "Autoclave Sterilizer")
