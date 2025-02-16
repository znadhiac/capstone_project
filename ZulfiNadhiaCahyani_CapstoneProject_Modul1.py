# Name      : Zulfi Nadhia Cahyani
# Program   : Data Science (JCDSOL-018 Class A)
# E-mail    : zulfinadhiac@gmail.com
# CAPSTONE PROJECT MODUL 1 - FUNDAMENTAL PROGRAMMING

# GUDANG ELEKTRONIK NADHIA

# DAFTAR PRODUK ELEKTRONIK
electronic_list = [    
    {'KODE': 'HP01', 'KATEGORI': 'HANDPHONE', 'BRAND': 'SAMSUNG', 'TAHUN': 2023, 'STOK': 15, 'HARGA': 15000000},
    {'KODE': 'HP02', 'KATEGORI': 'HANDPHONE', 'BRAND': 'APPLE', 'TAHUN': 2024, 'STOK': 12, 'HARGA': 20000000},
    {'KODE': 'HP03', 'KATEGORI': 'HANDPHONE', 'BRAND': 'XIAOMI', 'TAHUN': 2022, 'STOK': 20, 'HARGA': 5000000},
    {'KODE': 'KB01', 'KATEGORI': 'KEYBOARD', 'BRAND': 'LOGITECH', 'TAHUN': 2023, 'STOK': 25, 'HARGA': 150000},
    {'KODE': 'KB02', 'KATEGORI': 'KEYBOARD', 'BRAND': 'REXUS', 'TAHUN': 2022, 'STOK': 18, 'HARGA': 280000},
    {'KODE': 'KB03', 'KATEGORI': 'KEYBOARD', 'BRAND': 'AJAZZ', 'TAHUN': 2024, 'STOK': 22, 'HARGA': 750000},
    {'KODE': 'LP01', 'KATEGORI': 'LAPTOP', 'BRAND': 'ASUS', 'TAHUN': 2023, 'STOK': 7, 'HARGA': 15000000},
    {'KODE': 'LP02', 'KATEGORI': 'LAPTOP', 'BRAND': 'LENOVO', 'TAHUN': 2022, 'STOK': 6, 'HARGA': 12500000},
    {'KODE': 'LP03', 'KATEGORI': 'LAPTOP', 'BRAND': 'ACER', 'TAHUN': 2024, 'STOK': 10, 'HARGA': 9800000},      
    {'KODE': 'PR01', 'KATEGORI': 'PRINTER', 'BRAND': 'CANON', 'TAHUN': 2023, 'STOK': 5, 'HARGA': 8000000},
    {'KODE': 'PR02', 'KATEGORI': 'PRINTER', 'BRAND': 'EPSON', 'TAHUN': 2022, 'STOK': 4, 'HARGA': 7200000},
    {'KODE': 'PR03', 'KATEGORI': 'PRINTER', 'BRAND': 'HP', 'TAHUN': 2024, 'STOK': 6, 'HARGA': 8900000},
    {'KODE': 'TV01', 'KATEGORI': 'TELEVISI', 'BRAND': 'SAMSUNG', 'TAHUN': 2023, 'STOK': 10, 'HARGA': 7500000},
    {'KODE': 'TV02', 'KATEGORI': 'TELEVISI', 'BRAND': 'LG', 'TAHUN': 2022, 'STOK': 8, 'HARGA': 6800000},
    {'KODE': 'TV03', 'KATEGORI': 'TELEVISI', 'BRAND': 'SONY', 'TAHUN': 2024, 'STOK': 5, 'HARGA': 8500000}
]

from tabulate import tabulate

#1. MENAMPILKAN DAFTAR PRODUK

#1a. Function untuk menampilkan seluruh daftar produk
def display_all_products():
     
    # Memeriksa apakah daftar produk kosong
    if not electronic_list:
        print('\nTidak ada produk di dalam daftar.')
        return
    
    # Menampilkan seluruh daftar produk
    print('\nDAFTAR PRODUK DI GUDANG ELEKTRONIK NADHIA')

    headers = electronic_list[0].keys()
    data = []
    for item in electronic_list:
        data.append(item.values())
    print(tabulate(data, headers=headers, tablefmt='grid'))


#1b. Function untuk menampilkan daftar produk berdasarkan kode produk (primary key)
def filter_code():

    # Memeriksa apakah daftar produk kosong
    if not electronic_list:
        print('\nTidak ada produk di dalam daftar.')
        return
    
    # Mencari produk berdasarkan kode produk
    while True:
        check_code = input('\nMasukkan kode produk yang Anda cari (harus 4 karakter): ').strip().upper()
        
        if len(check_code) != 4:
            print('Kode produk harus mempunyai 4 karakter. Silakan coba lagi.')
        else:
            break
        
    filter_code_list = []
    for item in electronic_list:
        if item['KODE'].upper() == check_code:
            filter_code_list.append(item)

    # Menampilkan daftar produk yang sesuai dengan kode produk yang dicari
    if filter_code_list:
        headers = electronic_list[0].keys()
        data = []
        for item in filter_code_list:
            data.append(item.values())     
        print(f'\nHasil pencarian kode produk "{check_code}": ')
        print(tabulate(data, headers=headers, tablefmt='grid'))
    else:
        print(f'\nProduk dengan kode "{check_code}" tidak ditemukan.')


#1c. Function untuk menampilkan daftar produk berdasarkan kategori produk
def filter_category():

    # Memeriksa apakah daftar produk kosong
    if not electronic_list:
        print('\nTidak ada produk di dalam daftar.')
        return
    
    # Mencari produk berdasarkan kategori produk
    check_category = input('\nMasukkan kategori produk yang Anda cari: ').strip().upper()
    
    filter_category_list = []
    for item in electronic_list:
        if item['KATEGORI'].upper() == check_category:
            filter_category_list.append(item)

    # Menampilkan daftar produk yang sesuai dengan kategori produk yang dicari
    if filter_category_list:
        headers = electronic_list[0].keys()
        data = []
        for item in filter_category_list:
            data.append(item.values())    
        print(f'\nHasil pencarian kategori "{check_category}": ')
        print(tabulate(data, headers=headers, tablefmt='grid'))
    else:
        print(f'\nProduk dengan kategori "{check_category}" tidak ditemukan.')


#1d. Function untuk menampilkan daftar produk berdasarkan brand produk
def filter_brand():

    # Memeriksa apakah daftar produk kosong
    if not electronic_list:
        print('\nTidak ada produk di dalam daftar.')
        return
    
    # Mencari produk berdasarkan brand produk
    check_brand = input('\nMasukkan brand produk yang Anda cari: ').strip().upper()
    
    filter_brand_list = []
    for item in electronic_list:
        if item['BRAND'].upper() == check_brand:
            filter_brand_list.append(item)

    # Menampilkan daftar produk yang sesuai dengan brand produk yang dicari
    if filter_brand_list:
        headers = electronic_list[0].keys()     
        data = []
        for item in filter_brand_list:
            data.append(item.values())
        print(f'\nHasil pencarian brand "{check_brand}": ')
        print(tabulate(data, headers=headers, tablefmt='grid'))
    else:
        print(f'\nProduk dengan brand "{check_brand}" tidak ditemukan.')


# Menu Menampilkan Daftar Produk
def display_menu():
    while True:
        print('\nMENU 1: MENAMPILKAN DAFTAR PRODUK')
        print('Pilihan menu:')
        print('1. Tampilkan seluruh daftar produk')
        print('2. Tampilkan data berdasarkan kode produk')  # (kode produk adalah primary key)
        print('3. Tampilkan data berdasarkan kategori produk')
        print('4. Tampilkan data berdasarkan brand produk')
        print('5. Kembali ke menu utama\n')

        display_menu_options = input('Masukkan kode menu yang ingin dijalankan (1-5): ')

        if (display_menu_options == '1'):
            display_all_products()  
        elif (display_menu_options == '2'):
            filter_code()
        elif (display_menu_options == '3'):
            filter_category()
        elif (display_menu_options == '4'):
            filter_brand()
        elif (display_menu_options == '5'):
            return
        else:
            print('\nKode menu yang Anda masukkan tidak valid.\n')


#2. MENAMBAHKAN PRODUK

# Function untuk menambahkan produk baru
def add_product():

    # Memeriksa data duplikat berdasarkan kode produk (primary key)
    while True:
        check_code = input('\nMasukkan kode produk yang ingin Anda tambahkan (harus 4 karakter): ').strip().upper()
    
        if len(check_code) != 4:
            print('Kode produk harus mempunyai 4 karakter. Silakan coba lagi.')
        else:
            break
    
    for product in electronic_list:
        if product['KODE'].upper() == check_code:
            print(f'\nProduk dengan kode "{check_code}" sudah ada.')
            return

    # Melengkapi detail produk yang akan ditambahkan
    print('\nSilakan melengkapi detail produk berikut.')
    print(f'Kode produk: {check_code}')

    # Input kategori
    while True:
        category = input('Masukkan kategori produk: ').strip().upper()
        if category:
            break
        print('Kategori tidak boleh kosong. Silakan coba lagi.')

    # Input brand
    while True:
        brand = input('Masukkan brand produk: ').strip().upper()
        if brand:
            break
        print('Brand tidak boleh kosong. Silakan coba lagi.')

    # Input tahun
    while True:
        try:
            year = int(input('Masukkan tahun rilis produk: '))
            if year >= 2000 and year <= 2025:
                break
            else:
                print(f'Tahun harus di antara 2000 dan 2025. Silakan coba lagi.')
        except ValueError:
            print('Masukkan angka yang valid untuk tahun.')

    # Input stok
    while True:
        try:
            stock = int(input('Masukkan stok produk: '))
            if stock > 0:
                break
            elif stock == 0:
                print('Stok tidak boleh 0. Silakan coba lagi.')
            else:
                print('Stok tidak boleh negatif. Silakan coba lagi.')
        except ValueError:
            print('Masukkan angka yang valid untuk stok.')

    # Input harga
    while True:
        try:
            price = int(input('Masukkan harga produk per unit: Rp'))
            if price > 0:
                break
            else:
                print('Harga harus lebih dari 0. Silakan coba lagi.')
        except ValueError:
            print('Masukkan angka yang valid untuk harga.')
    
    # Menampilkan detail produk yang akan ditambahkan
    new_product = {
        'KODE' : check_code,
        'KATEGORI' : category,
        'BRAND' : brand,
        'TAHUN' : year,
        'STOK' : stock,
        'HARGA' : price
    }
    
    headers = new_product.keys()
    data = [list(new_product.values())]
    print(f'\nDetail produk yang Anda input: ')
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Konfirmasi untuk menyimpan data
    while True:
        print('\nPastikan data yang Anda masukkan benar.')
        print('Apakah Anda yakin ingin menyimpan data ini?')
        print('1. Ya')
        print('2. Tidak')
        confirm_save = input('Pilih (1/2): ')

        if (confirm_save == '1'):
            electronic_list.append(new_product)
            print(f'\nProduk dengan kode "{check_code}" berhasil ditambahkan.\n')      
            break      
        elif (confirm_save == '2'):
            print(f'\nData yang Anda masukkan tidak disimpan.\n')
            return
        else:
            print('\nKode menu yang Anda masukkan tidak valid. Silakan coba lagi.')


# Menu Menambahkan Produk
def add_menu():
    while True:
        print('\nMENU 2: MENAMBAHKAN PRODUK')
        print('Pilihan menu:')
        print('1. Tambah produk')
        print('2. Kembali ke menu utama\n')

        display_menu_options = input('Masukkan kode menu yang ingin dijalankan (1/2): ')

        if (display_menu_options == '1'):
            add_product()
        elif (display_menu_options == '2'):
            return
        else:
            print('\nKode menu yang Anda masukkan tidak valid.\n')


#3. MENGUBAH DATA PRODUK

# Function untuk mengubah data produk
def update_product():
  
    # Memeriksa data existing berdasarkan kode produk (primary key)
    while True:
        check_code = input('\nMasukkan kode produk yang datanya ingin Anda ubah (harus 4 karakter): ').strip().upper()
    
        if len(check_code) != 4:
            print('Kode produk harus mempunyai 4 karakter. Silakan coba lagi.')
        else:
            break

    # Menampilkan data berdasarkan kode produk (primary key)
    product = None

    for item in electronic_list:
        if item['KODE'] == check_code:
            product = item
            break

    if product:
        print(f'\nHasil pencarian kode produk "{check_code}": ')
        headers = electronic_list[0].keys()
        data_before = [list(product.values())]
        print(tabulate(data_before, headers=headers, tablefmt='grid'))
    else:
        print(f'\nProduk dengan kode "{check_code}" tidak ditemukan.')
        return
        
    # Konfirmasi untuk melanjutkan ubah data
    while True:
        print('\nApakah Anda ingin melanjutkan untuk mengubah data ini?')
        print('1. Ya')
        print('2. Tidak')
        continue_update = input('Pilih (1/2): ')
    
        if continue_update == '1':  
            break
        elif continue_update == '2':
            print(f'\nAnda tidak melanjutkan untuk mengubah data.\n')
            return
        else:
            print('\nKode menu yang Anda masukkan tidak valid. Silakan coba lagi.') 
    
    # Memasukkan nama kolom yang datanya ingin diubah
    while True:
        print(f'\nAnda akan mengubah data pada produk dengan kode "{check_code}".')    
        update_key = input('Masukkan nama kolom yang datanya ingin Anda ubah (KATEGORI/BRAND/TAHUN/STOK/HARGA): ').strip().upper()

        # User tidak bisa mengubah primary key (KODE)
        if update_key == 'KODE':
            print('\nAnda tidak dapat mengubah kode produk. Silakan pilih kolom lain.')
            continue

        # Mengecek apakah kolom yang dimasukkan valid
        if update_key in product:
            break
        else:
            print('\nKolom yang Anda masukkan tidak valid. Silakan coba lagi.')


    # Proses mengubah data
    old_value = product[update_key]     # (menyimpan data produk yang lama)

    while True:
        if update_key == 'KATEGORI':
            new_value = input('\nMasukkan kategori baru: ').strip().upper()
            if not new_value:
                print('Kategori tidak boleh kosong. Silakan coba lagi.')
            elif new_value == old_value:
                print('Kategori baru tidak boleh sama dengan yang lama. Silakan coba lagi.')
            else:
                break

        elif update_key == 'BRAND':
            new_value = input('\nMasukkan brand baru: ').strip().upper()
            if not new_value:
                print('Brand tidak boleh kosong. Silakan coba lagi.')
            elif new_value == old_value:
                print('Brand baru tidak boleh sama dengan yang lama. Silakan coba lagi.')
            else:
                break
        
        elif update_key == 'TAHUN':
            try:
                new_value = int(input('\nMasukkan tahun rilis baru: '))
                if new_value == old_value:
                    print('Tahun rilis baru tidak boleh sama dengan yang lama. Silakan coba lagi.')
                elif new_value >= 2000 and new_value <= 2025:
                    break
                else:
                    print('Tahun harus di antara 2000 dan 2025. Silakan coba lagi.')
            except ValueError:
                print('Masukkan angka yang valid untuk tahun.')

        elif update_key == 'STOK':
            try:
                new_value = int(input('\nMasukkan stok baru: '))
                if new_value == old_value:
                    print('Stok baru tidak boleh sama dengan yang lama. Silakan coba lagi.')
                elif new_value > 0:
                    break
                elif new_value == 0:
                    print('Stok tidak boleh 0. Silakan coba lagi.')
                else:
                    print('Stok tidak boleh negatif. Silakan coba lagi.')
            except ValueError:
                print('Masukkan angka yang valid untuk stok.')     
   
        elif update_key == 'HARGA':
            try:
                new_value = int(input('\nMasukkan harga produk per unit yang baru: Rp'))
                if new_value == old_value:
                    print('Harga baru tidak boleh sama dengan yang lama. Silakan coba lagi.')
                elif new_value > 0:
                    break
                else:
                    print('Harga harus lebih dari 0. Silakan coba lagi.')
            except ValueError:
                print('Masukkan angka yang valid untuk harga.')
                
    
    # Konfirmasi untuk update data
    while True:
        print(f'\nAnda akan mengubah data "{update_key}" dari "{old_value}" menjadi "{new_value}".')
        print('Pastikan data yang Anda masukkan benar.')
        print('Apakah Anda yakin ingin memperbarui data ini?')
        print('1. Ya')
        print('2. Tidak')
        confirm_update = input('Pilih (1/2): ')

        if (confirm_update == '1'):
            product[update_key] = new_value     # (menyimpan data produk yang baru)
            print(f'\nData "{update_key}" untuk kode produk "{check_code}" berhasil diperbarui.')

            # Menampilkan data produk sebelum dan setelah diubah
            data_after = [list(product.values())]
            print('\nData produk sebelum perubahan: ')
            print(tabulate(data_before, headers=headers, tablefmt='grid'))           
            print('\nData produk setelah perubahan: ')
            data_after = [product.values()]
            print(tabulate(data_after, headers=headers, tablefmt='grid'))
            break                

        elif (confirm_update == '2'):
            print(f'\nData yang Anda pilih tidak jadi diperbarui.\n')
            return
        else:
            print('\nKode menu yang Anda masukkan tidak valid. Silakan coba lagi.')


# Menu Mengubah Data Produk
def update_menu():
    while True:
        print('\nMENU 3: MENGUBAH DATA PRODUK')
        print('Pilihan menu:')
        print('1. Ubah data produk')
        print('2. Kembali ke menu utama\n')

        display_menu_options = input('Masukkan kode menu yang ingin dijalankan (1/2): ')

        if (display_menu_options == '1'):
            update_product()
        elif (display_menu_options == '2'):
            return
        else:
            print('\nKode menu yang Anda masukkan tidak valid.\n')


#4. MENGHAPUS PRODUK

# Function untuk menghapus produk
def delete_product():
  
    # Memeriksa data existing berdasarkan kode produk (primary key)
    while True:
        check_code = input('\nMasukkan kode produk yang datanya ingin Anda hapus (harus 4 karakter): ').strip().upper()
    
        if len(check_code) != 4:
            print('Kode produk harus mempunyai 4 karakter. Silakan coba lagi.')
        else:
            break

    # Menampilkan data berdasarkan kode produk (primary key)
    product = None

    for item in electronic_list:
        if item['KODE'] == check_code:
            product = item
            break

    if product:
        print(f'\nHasil pencarian kode produk "{check_code}": ')
        headers = electronic_list[0].keys()
        data = [product.values()]
        print(tabulate(data, headers=headers, tablefmt='grid'))
    else:
        print(f'\nProduk dengan kode "{check_code}" tidak ditemukan.')
        return
    
    # Konfirmasi untuk melanjutkan hapus data
    while True:
        print('\nApakah Anda yakin ingin menghapus data ini?')
        print('1. Ya')
        print('2. Tidak')
        confirm_delete = input('Pilih (1/2): ')
    
        if confirm_delete == '1':
            electronic_list.remove(product)
            print(f'\nProduk dengan kode "{check_code}" berhasil dihapus.\n')          
            break
        elif confirm_delete == '2':
            print(f'\nData yang Anda pilih tidak jadi dihapus.\n')
            return
        else:
            print('\nKode menu yang Anda masukkan tidak valid. Silakan coba lagi.')


# Menu Menghapus Produk
def delete_menu(): 
    while True:
        print('\nMENU 4: MENGHAPUS PRODUK')
        print('Pilihan menu:')
        print('1. Hapus produk')
        print('2. Kembali ke menu utama\n')

        display_menu_options = input('Masukkan kode menu yang ingin dijalankan (1/2): ')

        if (display_menu_options == '1'):
            delete_product()
        elif (display_menu_options == '2'):
            return
        else:
            print('\nKode menu yang Anda masukkan tidak valid.\n')


# KATA SAMBUTAN
def greetings():
    print('\n')
    print('=' * 81)
    print('Selamat datang di Gudang Elektronik Nadhia!')
    print('Kami menyediakan berbagai produk elektronik berkualitas dengan harga terjangkau.')
    print('=' * 81)

# MAIN MENU
def main_menu():
    greetings()
    while True:
        print('\nMENU UTAMA')
        print('Pilihan menu:')
        print('1. Tampilkan daftar produk')
        print('2. Tambah produk')
        print('3. Ubah data produk')
        print('4. Hapus produk')
        print('5. Keluar program\n')

        main_menu_options = input('Masukkan kode menu yang ingin dijalankan (1-5): ')

        if (main_menu_options == '1'):
            display_menu()
        elif (main_menu_options == '2'):
            add_menu()
        elif (main_menu_options == '3'):
            update_menu()
        elif (main_menu_options == '4'):
            delete_menu()
        elif (main_menu_options == '5'):
            print('\nTerima kasih telah menggunakan aplikasi Gudang Elektronik Nadhia.')
            print('Sampai jumpa!')
            break
        else:
            print('\nKode menu yang Anda masukkan tidak valid.\n')

main_menu()