from django.test import TestCase
from django.urls import reverse

class MainViewTests(TestCase):
    def test_show_main_view(self):
        # Mengirimkan request ke halaman utama
        response = self.client.get(reverse('show_main'))

        # Memastikan response status adalah 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Memastikan template yang digunakan adalah 'main.html'
        self.assertTemplateUsed(response, 'main.html')

        # Memastikan produk-produk dikirimkan ke template
        self.assertIn('products', response.context)

        # Memastikan produk yang diharapkan ada di dalam context
        expected_products = [
            {
                'name': 'Microscope X200',
                'price': 2000000,
                'description': 'High-quality microscope suitable for research and education purposes.'
            },
            {
                'name': 'Centrifuge 3000 RPM',
                'price': 5000000,
                'description': 'High-speed centrifuge for separating fluids and gases based on density.'
            },
            {
                'name': 'Autoclave Sterilizer',
                'price': 7000000,
                'description': 'Compact autoclave for sterilization in laboratories.'
            },
        ]
        self.assertEqual(response.context['products'], expected_products)
