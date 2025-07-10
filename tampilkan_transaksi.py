from data import baca_data

def tampilkan_transaksi():
    data = baca_data()
    if not data:
        print("Belum ada transaksi.")
        return

    print("\nDaftar Transaksi:")
    for i, d in enumerate(data, 1):
        print(f"{i}. {d['tanggal']} | {d['jenis']} | {d['kategori']} | "
              f"{d['deskripsi']} | Rp{d['nominal']:,}")
