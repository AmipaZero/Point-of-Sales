# 🧾 Point of Sales (POS) Backend System

Aplikasi backend **Point of Sales (POS)** untuk mengelola proses penjualan secara terstruktur.  
Aplikasi ini menggunakan **RESTful API** dengan mekanisme autentikasi **JWT (JSON Web Token)**.  
Setiap pengguna wajib login untuk mendapatkan token, dan token tersebut harus disertakan pada setiap request ke endpoint API.

---
## ⚡ Fitur

### 🔐 Autentikasi
- **Register** pengguna baru  
- **Login** menggunakan username & password untuk mendapatkan token  
- **Logout** untuk menghapus token aktif  

### 👥 Role & Hak Akses
- **Admin**
- **Kasir**

### 📦 Produk
- Menambahkan produk baru  
- Melihat daftar produk  
- Mengupdate dan menghapus produk  
- Mengelola stok produk  

### 🧾 Transaksi Penjualan
- Membuat transaksi penjualan  
- Mendukung lebih dari satu produk dalam satu transaksi  
- Mengurangi stok produk secara otomatis  
- Menyimpan riwayat transaksi penjualan  

### 📊 Laporan Transaksi
- Melihat daftar transaksi penjualan  
- Filter laporan berdasarkan tanggal  
- Hak akses laporan hanya tersedia untuk **Admin**

---
## 🛠️ Teknologi yang Digunakan
- **Python** (Backend API)  
- **Flask** (Web Framework)  
- **PostgreSQL** (Database)  
- **SQLAlchemy** (ORM)  
- **JWT** (JSON Web Token untuk autentikasi)  
