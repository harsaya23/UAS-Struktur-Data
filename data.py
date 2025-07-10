import csv, os          # csv: baca/tulis file CSV; os: cek/mengelola file di sistem

FILENAME   = 'keuangan.csv'                                           # nama file data
FIELDNAMES = ['tanggal', 'jenis', 'kategori', 'deskripsi', 'nominal'] # header kolom

def baca_data():
    """
    Membaca seluruh transaksi dari keuangan.csv dan
    mengembalikan list berisi dict untuk tiap baris.
    Jika file belum ada, fungsi cukup mengembalikan list kosong.
    """

    if not os.path.exists(FILENAME):      # file belum dibuat
        return []

    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data   = []

        for row in reader:
            # Pastikan semua kolom yang diharapkan memang ada
            if all(k in row for k in FIELDNAMES):
                try:
                    # Ubah kolom nominal dari string → int agar bisa dihitung
                    row['nominal'] = int(row['nominal'])
                    data.append(row)
                except ValueError:
                    # Lewati baris jika nominal‑nya bukan angka valid
                    continue
        return data


def simpan_data(data):
    """
    Menimpa (overwrite) keuangan.csv dengan `data`,
    di mana `data` adalah list of dict transaksi.
    """
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()            # baris header
        for row in data:
            writer.writerow(row)        # tulis setiap transaksi


def tambah_data_baru(data_baru):
    """
    Menambahkan satu transaksi (dict) ke dalam file.
    Bila file belum ada atau kosong, header akan dibuat dulu.
    """
    file_baru = (not os.path.exists(FILENAME)) or os.path.getsize(FILENAME) == 0

    with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if file_baru:
            writer.writeheader()        # tulis header jika file masih kosong

        writer.writerow(data_baru)      # tambahkan baris transaksi baru
