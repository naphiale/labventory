# Labventory

**Labventory** is an e-commerce platform designed to streamline the procurement of laboratory equipment, supplies, and safety gear for educational institutions, research facilities, hospitals, and biotechnology companies. Our goal is to provide high-quality, reliable lab equipment with a seamless shopping experience.

## Features

- **Comprehensive Catalog**: A wide range of laboratory equipment and supplies, categorized for easy browsing.
- **Custom Orders**: Flexible options to customize your orders based on your specific lab needs.
- **Bulk Purchase Discounts**: Special pricing for bulk orders and laboratory setup packages.
- **Expert Consultation**: Access to expert guidance to help you choose the right products.
- **Secure Checkout**: Multiple payment options, including secure transactions via Stripe or PayPal.
- **Order Tracking**: Track your orders from purchase to delivery in real-time.
- **Customer Support**: Dedicated customer support to assist with inquiries, warranties, and product issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or support, please contact us at [support@labventory.com](mailto:support@labventory.com).

---

# Menjawab Pertanyaan

## 1. Langkah-Langkah Implementasi

Berikut adalah langkah-langkah untuk mengimplementasikan aplikasi web berbasis Django:

### Langkah 1: Membuat Proyek Django
Jalankan perintah berikut:
```bash
django-admin startproject Labventory
```
Perintah ini akan membuat struktur dasar dari proyek Django.

### Langkah 2: Membuat Aplikasi Django
Buat aplikasi baru di dalam proyek dengan perintah:
```bash
python manage.py startapp labventory
```

### Langkah 3: Menentukan Model di `models.py`
Buat model yang sesuai dengan struktur tabel database. Sebagai contoh, berikut adalah model untuk `Product`:
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
```

### Langkah 4: Menjalankan Migrasi
Untuk mengupdate skema database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Langkah 5: Menentukan URL di `urls.py`
Hubungkan pola URL ke views.
```python
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.show_main, name='show_main'),
]
```

### Langkah 6: Membuat Views di `views.py`
Buat views untuk menangani request dan me-render template.
```python
from django.shortcuts import render

def show_main(request):
    products = [
        {'name': 'Microscope X200', 'price': 2000000, 'description': 'Mikroskop berkualitas tinggi untuk penelitian dan pendidikan.'},
        {'name': 'Centrifuge 3000 RPM', 'price': 5000000, 'description': 'Centrifuge berkecepatan tinggi untuk memisahkan cairan.'},
        {'name': 'Autoclave Sterilizer', 'price': 7000000, 'description': 'Autoclave kompak untuk sterilisasi di laboratorium.'},
    ]
    return render(request, "main.html", {'products': products})
```

### Langkah 7: Menyusun Template HTML
Buat file `main.html` di dalam direktori template untuk menampilkan data dari views.

---

## 2. Alur Request-Response di Django

Berikut adalah alur permintaan (request) dari klien hingga mendapatkan respon dari server Django:



### Penjelasan Alur:
- **urls.py**: Memetakan URL yang diminta oleh klien ke fungsi yang sesuai di `views.py`.
- **views.py**: Fungsi yang menangani logika bisnis dan pengambilan data dari model, kemudian me-render template HTML.
- **models.py**: Berfungsi untuk menghubungkan Django dengan database, mengelola data yang dibutuhkan oleh views.
- **HTML (Template)**: Menampilkan data yang telah diproses oleh views kepada klien.

---

## 3. Fungsi Git dalam Pengembangan Perangkat Lunak

Git berfungsi sebagai sistem version control yang membantu:
- Melacak perubahan dalam kode selama pengembangan.
- Memfasilitasi kolaborasi antara banyak pengembang.
- Mengembalikan versi sebelumnya dari kode jika terjadi kesalahan.
- Mengelola branch untuk mengembangkan fitur baru secara paralel.

---

## 4. Mengapa Django Cocok untuk Pembelajaran?

Django dipilih sebagai framework pembelajaran pengembangan perangkat lunak karena:
- *Django sudah menyediakan banyak fitur bawaan seperti autentikasi, manajemen admin, dan ORM sehingga developer dapat fokus pada pengembangan logika bisnis.
- *Memisahkan logika data, tampilan, dan kontrol sehingga mempermudah pemahaman dan pengelolaan kode.
- Django memiliki dokumentasi yang sangat lengkap dan komunitas yang besar.

---

## 5. Mengapa Model di Django Disebut ORM?

Model di Django disebut sebagai **ORM (Object-Relational Mapping)** karena Django secara otomatis mengubah objek Python menjadi tabel di database relasional. ORM memungkinkan developer bekerja dengan database menggunakan konsep object-oriented, tanpa perlu menulis kueri SQL secara langsung.

--- 