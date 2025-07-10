from data import baca_data, simpan_data, tambah_data_baru  # Ambil fungsi bantu CSV

# Fungsi bantu untuk input tanggal dengan format valid YYYY-MM-DD
def input_tanggal(prompt="Tanggal (YYYY-MM-DD): "):
    while True:
        t = input(prompt).strip()         # Ambil input dan hapus spasi
        p = t.split("-")                  # Pisahkan tahun-bulan-tanggal
        # Cek format: ada 3 bagian, semuanya angka, dan panjang sesuai
        if len(p) == 3 and all(s.isdigit() for s in p) \
           and len(p[0]) == 4 and len(p[1]) == 2 and len(p[2]) == 2:
            return t
        print("Format salah. Contoh: 2025-06-28")

# Fungsi bantu untuk input nominal angka (harus bilangan bulat positif)
def input_nominal(prompt="Nominal: "):
    while True:
        try:
            n = int(input(prompt))
            if n >= 0:
                return n
            print("Nominal tidak boleh negatif.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Fungsi untuk menambahkan transaksi baru
def tambah_transaksi():
    row = {
        "tanggal"   : input_tanggal(),
        "jenis"     : input("Jenis transaksi (masuk/keluar): ").lower(),
        "kategori"  : input("Kategori: "),
        "deskripsi" : input("Deskripsi: "),
        "nominal"   : input_nominal()
    }
    tambah_data_baru(row)       # Simpan transaksi ke file
    print("Transaksi berhasil ditambahkan.\n")