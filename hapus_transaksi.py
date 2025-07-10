from data import baca_data, simpan_data
from tampilkan_transaksi import tampilkan_transaksi

def hapus_transaksi():
    data = baca_data()
    tampilkan_transaksi()
    if not data:
        return

    try:
        idx = int(input("\nNomor yang dihapus: ")) - 1
        if 0 <= idx < len(data):
            data.pop(idx)
            simpan_data(data)
            print("Transaksi terhapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")
