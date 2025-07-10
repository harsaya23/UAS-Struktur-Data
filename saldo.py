from data import baca_data  # Ambil fungsi untuk membaca semua data transaksi dari file CSV

def cek_saldo():
    # Baca seluruh data transaksi (list of dict) dari file
    data = baca_data()

    # Jumlahkan semua nominal dengan jenis 'pemasukan'
    masuk = sum(d["nominal"] for d in data if d["jenis"] == "masuk")

    # Jumlahkan semua nominal dengan jenis 'pengeluaran'
    keluar = sum(d["nominal"] for d in data if d["jenis"] == "keluar")

    # Hitung selisih antara pemasukan dan pengeluaran
    saldo = masuk - keluar

    # Tampilkan hasil saldo akhir dengan format ribuan
    print(f"\nSaldo Saat Ini: Rp{saldo:,}")