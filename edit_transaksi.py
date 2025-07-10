from data import baca_data, simpan_data
from tambah_transaksi import input_tanggal, input_nominal
from tampilkan_transaksi import tampilkan_transaksi

def edit_transaksi():
    data = baca_data()
    tampilkan_transaksi()
    if not data:
        return

    try:
        idx = int(input("\nNomor yang diubah: ")) - 1
        if 0 <= idx < len(data):
            print("\nMasukkan data baru:")
            data[idx] = {
                "tanggal"  : input_tanggal(),
                "jenis"    : input("Jenis transaksi (masuk/keluar): ").lower(),
                "kategori" : input("Kategori: "),
                "deskripsi": input("Deskripsi: "),
                "nominal"  : input_nominal()
            }
            simpan_data(data)
            print("Transaksi berhasil diubah.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")
