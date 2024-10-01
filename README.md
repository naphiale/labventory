
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

# Menjawab Pertanyaan Tugas 2

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

## 2. Alur Request-Response di Django

Berikut adalah alur permintaan (request) dari klien hingga mendapatkan respon dari server Django:

![R-R Model](https://github.com/user-attachments/assets/9262801b-fbdb-44cd-93c5-c28a3121030f)

### Penjelasan Alur:
- **urls.py**: Memetakan URL yang diminta oleh klien ke fungsi yang sesuai di `views.py`.
- **views.py**: Fungsi yang menangani logika bisnis dan pengambilan data dari model, kemudian me-render template HTML.
- **models.py**: Berfungsi untuk menghubungkan Django dengan database, mengelola data yang dibutuhkan oleh views.
- **HTML (Template)**: Menampilkan data yang telah diproses oleh views kepada klien.

## 3. Fungsi Git dalam Pengembangan Perangkat Lunak

Git berfungsi sebagai sistem version control yang membantu:
- Melacak perubahan dalam kode selama pengembangan.
- Memfasilitasi kolaborasi antara banyak pengembang.
- Mengembalikan versi sebelumnya dari kode jika terjadi kesalahan.
- Mengelola branch untuk mengembangkan fitur baru secara paralel.

## 4. Mengapa Django Cocok untuk Pembelajaran?

Django dipilih sebagai framework pembelajaran pengembangan perangkat lunak karena:
- Django sudah menyediakan banyak fitur bawaan seperti autentikasi, manajemen admin, dan ORM sehingga developer dapat fokus pada pengembangan logika bisnis.
- Memisahkan logika data, tampilan, dan kontrol sehingga mempermudah pemahaman dan pengelolaan kode.
- Django memiliki dokumentasi yang sangat lengkap dan komunitas yang besar.

## 5. Mengapa Model di Django Disebut ORM?

Model di Django disebut sebagai **ORM (Object-Relational Mapping)** karena Django secara otomatis mengubah objek Python menjadi tabel di database relasional. ORM memungkinkan developer bekerja dengan database menggunakan konsep object-oriented, tanpa perlu menulis kueri SQL secara langsung.

---

# Menjawab Pertanyaan Tugas 3

## 1. Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Sebuah Platform?**

Data delivery penting untuk memungkinkan komunikasi antara client dan server. Ini memastikan bahwa aplikasi dapat mengambil, mengirim, dan menampilkan data secara real-time, seperti hasil pencarian, status pengguna, atau konten dinamis lainnya. Tanpa mekanisme ini, platform tidak bisa berfungsi secara efektif dalam memberikan informasi yang diperbarui kepada pengguna.

## 2. Mana yang Lebih Baik antara XML dan JSON? Mengapa JSON Lebih Populer Dibandingkan XML?**

- **JSON lebih baik dalam konteks web modern** karena lebih ringan dan mudah dibaca, baik oleh manusia maupun mesin. Parsing JSON juga lebih cepat karena lebih sederhana dibandingkan XML.
- **JSON lebih populer** karena secara alami kompatibel dengan JavaScript, yang banyak digunakan di aplikasi web. Sementara XML lebih kompleks dan memerlukan lebih banyak resource untuk diproses.

## 3. Fungsi `is_valid()` pada Form Django**

`is_valid()` digunakan untuk memvalidasi data yang dikirimkan melalui form. Jika data sesuai dengan aturan yang sudah ditentukan, fungsi ini mengembalikan `True`, dan `False` jika tidak. Fungsinya untuk memastikan integritas data sebelum disimpan ke database, mencegah input yang salah atau tidak lengkap.

## 4. Mengapa Kita Membutuhkan `csrf_token` pada Form di Django?**

`csrf_token` melindungi aplikasi dari serangan **Cross-Site Request Forgery (CSRF)**, di mana penyerang mencoba memanipulasi request yang dikirim oleh pengguna. Jika tidak ada `csrf_token`, aplikasi rentan terhadap serangan yang bisa mengakibatkan tindakan berbahaya seperti perubahan data atau transaksi yang tidak sah.

## 5. Implementasi Checklist Step-by-Step**

1. **Pahami Kebutuhan**: Mulai dengan memahami kebutuhan menampilkan data dalam format XML dan JSON.
2. **Mengimplementasikan Fungsi Serialisasi di `views.py`**: Menulis fungsi `show_xml`, `show_json`, dan fungsi serupa untuk mengambil data dan mengonversinya ke format yang sesuai.
3. **Tambahkan URL Patterns**: Menambahkan URL yang mengarah ke fungsi-fungsi tersebut di `urls.py`.

---

# Menjawab Pertanyaan Tugas 4

## 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?
`HttpResponseRedirect()` adalah kelas dasar untuk membuat objek respons yang mengalihkan ke URL lain. Di sisi lain, `redirect()` adalah fungsi pembungkus (wrapper) yang lebih tinggi yang menyederhanakan pembuatan pengalihan. `redirect()` secara otomatis menangani URL dan juga dapat menerima objek model, mengembalikan pengalihan ke detail model tersebut. Penggunaan `redirect()` lebih umum karena lebih ringkas dan lebih mudah dibaca.

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model `Product` dengan `User` dilakukan dengan menambahkan foreign key di model `Product`. Misalnya, jika kita memiliki model `Product`, kita dapat menambahkan field `user` yang merujuk ke model `User`. Ini memungkinkan setiap produk memiliki pemilik yang dapat diidentifikasi. Contoh implementasinya seperti ini:

```python
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Field lain untuk model Product
```

Dengan cara ini, kita dapat dengan mudah melacak produk yang dibuat oleh pengguna tertentu.

## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login?
Authentication adalah proses verifikasi identitas pengguna, memastikan bahwa pengguna yang masuk adalah mereka yang mereka klaim. Authorization, di sisi lain, adalah proses menentukan hak akses yang dimiliki pengguna setelah mereka berhasil diautentikasi. Saat pengguna login, sistem memverifikasi kredensial mereka (authentication), dan setelah itu menentukan apa yang boleh mereka lakukan (authorization) berdasarkan peran atau izin yang diberikan kepada mereka.

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan session. Ketika pengguna berhasil login, Django menyimpan informasi sesi di server dan mengirimkan cookie ke browser pengguna. Cookie ini berisi ID sesi yang digunakan untuk mengidentifikasi pengguna di setiap permintaan berikutnya. Selain itu, cookies dapat digunakan untuk menyimpan informasi lain seperti preferensi pengguna atau data login terakhir. Namun, tidak semua cookies aman; cookies yang menyimpan data sensitif harus dienkripsi dan hanya boleh diakses melalui HTTPS untuk mencegah potensi penyalahgunaan.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Berikut adalah langkah-langkah untuk membuat fungsi-fungsi autentikasi dan menggunakan data dari cookies, serta menghubungkan model dengan user:

### 1. **Membuat Fungsi dan Form Registrasi**
   - **Form Registrasi**: Buat form menggunakan `UserCreationForm` bawaan Django yang memudahkan pembuatan user baru. Lalu tambahkan logika di view untuk menangani input form.
   - **URL Registrasi**: Tambahkan path untuk registrasi di `urls.py`

### 2. **Membuat Fungsi Login**
   - Gunakan `authenticate()` dan `login()` dari Django untuk memverifikasi kredensial pengguna, lalu login.

### 3. **Membuat Fungsi Logout**
   - Gunakan `logout()` untuk menghapus session pengguna.
   - **URL Logout**: Tambahkan path untuk logout di `urls.py`:

### 4. **Merestriksi Akses Halaman Main**
   - Gunakan dekorator `login_required` untuk memastikan pengguna hanya bisa mengakses halaman jika mereka telah login.
   - **Login URL**: Jangan lupa untuk menambahkan URL login di `settings.py`:

### 5. **Menggunakan Data Dari Cookies**
   - Saat pengguna berhasil login, tambahkan cookie `last_login` untuk mencatat kapan terakhir kali mereka login.
   - **Menampilkan Data dari Cookies**: Di halaman `main`, ambil cookie `last_login` untuk ditampilkan.

### 6. **Menghubungkan Model MoodEntry dengan User**
   - Tambahkan foreign key di model `MoodEntry` untuk mengaitkan mood dengan user yang login.
   - Saat menyimpan data, pastikan mood yang dibuat terkait dengan user yang sedang login.

![user2](https://github.com/user-attachments/assets/361a5af6-1e3f-41f5-9946-068f2f914abb)
![user1](https://github.com/user-attachments/assets/28efaf33-ace3-44d7-996f-9c787e77fb75)

# Menjawab Pertanyaan Tugas 5

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas pengambilan CSS selector (yang dikenal dengan istilah **Specificity**) adalah sebagai berikut:

1. **Inline Styles**: CSS yang ditulis langsung di elemen HTML (misalnya, `<div style="color: red;">`) memiliki prioritas tertinggi.
2. **ID Selector**: Selector yang menggunakan ID (misalnya, `#my-id`) memiliki prioritas lebih tinggi dibandingkan class atau tag.
3. **Class, Attribute, dan Pseudo-class Selector**: Selector yang menggunakan class (misalnya, `.my-class`), attribute (misalnya, `[type="text"]`), atau pseudo-class (misalnya, `:hover`) memiliki prioritas yang lebih rendah dari ID.
4. **Tag Selector**: Selector yang menggunakan tag HTML (misalnya, `div`, `p`) memiliki prioritas paling rendah.
5. **Universal Selector**: Selector yang menggunakan asterisk (`*`) memiliki prioritas terendah dan akan mengambil semua elemen.

Dengan mengetahui urutan ini, kita dapat mengelola styling dengan lebih efektif.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web?

Responsive design adalah konsep yang sangat penting karena membantu menciptakan pengalaman pengguna yang baik di berbagai perangkat. Dalam dunia saat ini, orang mengakses web menggunakan perangkat yang berbeda seperti ponsel, tablet, dan desktop. Jika sebuah aplikasi web tidak responsif, pengguna akan mengalami kesulitan dalam menavigasi, yang dapat mengurangi kepuasan dan membuat mereka meninggalkan situs.

Contoh aplikasi yang menerapkan responsive design dengan baik adalah **Twitter** dan **Instagram**. Keduanya menyesuaikan konten dan tata letak berdasarkan ukuran layar, sehingga pengguna mendapatkan pengalaman yang optimal di perangkat apa pun.

Sebaliknya, contoh aplikasi yang belum menerapkan responsive design adalah banyak situs web perusahaan lama yang hanya terlihat baik di desktop dan sangat sulit digunakan di perangkat mobile.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

- **Margin**: Ruang di luar elemen yang menciptakan jarak antara elemen tersebut dan elemen lainnya. Margin tidak mempengaruhi ukuran elemen itu sendiri. Kita dapat mengatur margin dengan menggunakan properti CSS seperti `margin: 20px;`.

- **Border**: Garis yang mengelilingi elemen, yang dapat kita sesuaikan ketebalan, warna, dan gayanya. Border mempengaruhi ukuran total elemen. Contoh implementasi: `border: 1px solid black;`.

- **Padding**: Ruang di dalam elemen, antara konten dan border. Padding meningkatkan ukuran elemen, karena menambah ruang di dalamnya. Kita dapat mengatur padding dengan menggunakan `padding: 10px;`.

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

**Flexbox**: Flexbox adalah model layout satu dimensi yang memungkinkan kita untuk menyusun elemen dalam satu baris (horizontal) atau kolom (vertikal). Flexbox sangat berguna untuk menciptakan layout yang responsif dan dapat menyesuaikan ukuran konten. Dengan Flexbox, kita dapat dengan mudah mengatur perataan, arah, dan urutan elemen dalam kontainer.

**Grid Layout**: Grid adalah model layout dua dimensi yang memungkinkan kita untuk menyusun elemen dalam baris dan kolom. Grid sangat berguna untuk membuat desain yang lebih kompleks dan teratur. Dengan Grid, kita dapat mengontrol ukuran kolom dan baris, serta menciptakan tata letak yang lebih terstruktur.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. **Implementasi Fungsi CRUD**: Menggunakan Django, saya membuat views untuk mengedit dan menghapus produk. Saya juga memastikan data ditangani dengan aman dengan menambahkan konfirmasi saat menghapus.

2. **Desain Halaman**: Saya memilih untuk menggunakan Bootstrap untuk kemudahan responsivitas dan konsistensi. Saya menulis CSS kustom untuk menyesuaikan tampilan dengan kebutuhan aplikasi.

3. **Membuat Halaman Daftar Produk**: Saya membuat logika untuk memeriksa apakah ada produk yang tersimpan. Jika tidak ada, menampilkan gambar dan pesan. Jika ada, menampilkan produk dalam format kartu yang responsif.

4. **Membuat Navbar**: Saya mendesain navbar responsif dengan menggunakan kelas Bootstrap dan beberapa logika JavaScript untuk menampilkan menu hamburger di perangkat mobile.
