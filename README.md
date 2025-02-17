CAPSTONE PROJECT MODUL 1 

GUDANG ELEKTRONIK - MANAJEMEN STOK PRODUK

Nama: Zulfi Nadhia Cahyani

Program: Data Science Online Program JCDSOL-018 Class A

E-mail: zulfinadhiac@gmail.com



DESKRIPSI PROJECT

Project ini adalah sebuah mini aplikasi berbasis Python untuk mengelola daftar produk barang elektronik dalam gudang bernama Gudang Elektronik Nadhia. 
Aplikasi ini memungkinkan pengguna untuk menampilkan daftar produk, menambahkan produk ke daftar produk, mengubah data di dalam daftar produk, serta menghapus data produk yang sudah ada di daftar produk. 
Aplikasi ini juga dapat membantu pengguna untuk menampilkan data produk yang sudah difilter berdasarkan kode, kategori, dan brand produk, serta menampilkan data dalam bentuk tabel menggunakan tabulate.

DATA

Data dummy yang digunakan untuk kebutuhan project ini terdiri dari 15 data dictionary yang disimpan dalam bentuk tipe data list. 
Data-data tersebut terdiri dari 6 kolom (key), di mana key ‘KODE’ merupakan primary key-nya. Kelima kolom lainnya yaitu kategori, brand, tahun rilis, stok, dan harga.

FITUR UTAMA
1.	Menu Utama (Main Menu)
Menu utama membantu pengguna untuk menjalankan menu lainnya, yaitu display menu, add menu, update menu, dan delete menu.
Pengguna juga bisa memilih untuk keluar program melalui menu utama ini.
2.	Menampilkan Daftar Produk (Display Menu)
-	Menampilkan seluruh daftar produk elektronik yang tersedia di gudang
-	Menampilkan produk berdasarkan kode produk
-	Menampilkan produk berdasarkan kategori produk
-	Menampilkan produk berdasarkan brand produk
-	Menampilkan daftar produk dalam format tabel untuk kemudahan membaca
3.	Menambahkan Produk (Add Menu)
Menu ini memungkinkan pengguna untuk menambahkan produk baru ke daftar produk.
4.	Mengubah Data Produk (Update Menu)
Menu ini memungkinkan pengguna untuk mengubah atau memperbarui data produk ke daftar produk, yang terdiri dari data kategori, brand, tahun rilis, stok, dan harga barang elektronik.
Namun, pengguna tidak bisa mengubah data di dalam kolom kode produk karena merupakan primary key.
5.	Menghapus Produk (Delete Menu)
Menu ini memungkinkan pengguna untuk menghapus produk yang sudah ada di daftar produk.

TEKNOLOGI YANG DIGUNAKAN
-	Python
-	Tabulate untuk tampilan tabel
