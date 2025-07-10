from data import baca_data            # Baca list transaksi dari CSV
from collections import defaultdict   # Dict yang otomatis mulai dari 0
from saldo import cek_saldo           # Menampilkan saldo terkini
def laporan_bulanan_tahunan() -> None:
    """
    - Hitung total pemasukan & pengeluaran per bulan dan per tahun
    - Tampilkan tabel bulanan & tahunan
    - Tampilkan saldo akhir (cek_saldo)
    """
    # 1) Baca semua transaksi
    data = baca_data()
    if not data:
        print("Belum ada data.")
        return

    # 2) Tempat nyimpen total
    bulanan_in  = defaultdict(int)    # total pemasukan tiap bulan
    bulanan_out = defaultdict(int)    # total pengeluaran tiap bulan
    tahunan_in  = defaultdict(int)    # total pemasukan tiap tahun
    tahunan_out = defaultdict(int)    # total pengeluaran tiap tahun

    # 3) Kelompokkan + jumlahkan
    for d in data:
        tahun, bulan, *_ = d["tanggal"].split("-")

        if d["jenis"] == "masuk":
            bulanan_in[f"{tahun}-{bulan}"] += d["nominal"]
            tahunan_in[tahun]              += d["nominal"]

        elif d["jenis"] == "keluar":
            # Tambah pengeluaran bulan itu
            bulanan_out[f"{tahun}-{bulan}"] += d["nominal"]
            # Tambah pengeluaran tahun itu
            tahunan_out[tahun]              += d["nominal"]

    # 4) Laporan Bulanan
    print("\nLaporan Bulanan:")
    print(f"{'Bulan':<10} | {'masuk':>12} | {'keluar':>13}")
    print("-" * 42)

    semua_bulan = sorted(set(bulanan_in) | set(bulanan_out))
    for bln in semua_bulan:
        masuk  = bulanan_in.get(bln, 0)   # 0 kalau belum ada
        keluar = bulanan_out.get(bln, 0)  # 0 kalau belum ada
        print(f"{bln:<10} | Rp{masuk:>10,} | Rp{keluar:>11,}")

    # 5) Laporan Tahunan
    print("\nLaporan Tahunan:")
    print(f"{'Tahun':<6} | {'masuk':>12} | {'keluar':>13}")
    print("-" * 42)

    # Gabungkan daftar tahun yang muncul di pemasukan atau pengeluaran, lalu urutkan
    semua_tahun = sorted(set(tahunan_in) | set(tahunan_out))
    for thn in semua_tahun:
        # Ambil total pemasukan tahun ini (0 kalau tidak ada)
        masuk  = tahunan_in.get(thn, 0)
        # Ambil total pengeluaran tahun ini (0 kalau tidak ada)
        keluar = tahunan_out.get(thn, 0)
        print(f"{thn:<6} | Rp{masuk:>10,} | Rp{keluar:>11,}")

    # 6) Saldo Akhir
    print("\nSaldo Akhir:")
    cek_saldo() #print total saldo