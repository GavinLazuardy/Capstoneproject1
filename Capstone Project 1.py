from tabulate import tabulate
from datetime import datetime
from operator import itemgetter

data = [
    {"Nama": "Budi", "Usia": 25, "Tanggal Masuk": datetime(2023, 6, 5), "Kategori": "1"},
    {"Nama": "Putri", "Usia": 19, "Tanggal Masuk": datetime(2023, 6, 23), "Kategori": "2"},
    {"Nama": "Adi", "Usia": 38, "Tanggal Masuk": datetime(2023, 6, 18), "Kategori": "1"},
    {"Nama": "Siti", "Usia": 46, "Tanggal Masuk": datetime(2023, 6, 21), "Kategori": "2"},
    {"Nama": "Fajar", "Usia": 22, "Tanggal Masuk": datetime(2023, 6, 12), "Kategori": "2"}
]

kode_kategori = {"1": "Parah", "2": "Tidak"}

for entry in data:
    entry["Kategori"] = kode_kategori.get(entry["Kategori"], entry["Kategori"])

def valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def read_data():
    for entry in data:
        if isinstance(entry["Tanggal Masuk"], datetime):
            entry["Tanggal Masuk"] = (entry["Tanggal Masuk"]).strftime("%d-%m-%Y")
    print(tabulate(data, headers='keys', tablefmt='pretty'))

def create_data():
    print('''
    SILAHKAN MASUKKAN DATA PASIEN BARU!
    ''')
    while True:
        nama = input("Masukkan Nama Pasien: ")
        nama = nama.capitalize()
        if nama.isalpha():
            break
        else:
            print("Input yang anda masukkan salah.")
    while True:
        usia_input = input("Masukkan Usia Pasien: ")
        if usia_input.isdigit():
            usia = int(usia_input)
            break
        else:
            print("Input yang anda masukkan salah.")
    while True:
        tanggal_masuk = input("Masukkan Tanggal: (DD-MM-YYYY) ")
        if valid_date(tanggal_masuk):
            tanggal_masuk_baru = datetime.strptime(tanggal_masuk, "%d-%m-%Y").date()
            tanggal_masuk_baru_str = tanggal_masuk_baru.strftime("%d-%m-%Y")
            break
        else:
            print("Input yang anda masukkan salah. (DD-MM-YYYY).")
    while True:
        kategori = input("Masukkan Kategori Pasien: (1: Parah, 2: Tidak) ")
        if kategori.isdigit() and kategori in kode_kategori:
            kategori = kode_kategori[kategori]
            break
        else:
            print("Kategori harus 1 (Parah) atau 2 (Tidak)")
    new_data = {"Nama": nama, "Usia": usia, "Tanggal Masuk": tanggal_masuk_baru_str, "Kategori": kategori}
    data.append(new_data)
    print("Data Pasien berhasil ditambah.")

def erase_data():
    while True:
        read_data()
        nama_yang_dihapus = input("Masukkan Nama yang Akan Dihapus (kosongkan untuk batal): ")

        if not nama_yang_dihapus:
            print("Penghapusan data dibatalkan.")
            break

        found = False
        for i, entry in enumerate(data):
            if entry.get("Nama", "") == nama_yang_dihapus:
                data.pop(i)
                print(f"Data Pasien {nama_yang_dihapus} berhasil dihapus.")
                found = True
                break

        if not found:
            print(f"Tidak ada pasien dengan nama {nama_yang_dihapus}. Silakan coba lagi.")
        else:
            break


def update_data():
    read_data()
    nama_to_update = input("Masukkan Nama data yang ingin diupdate: ")
    index_to_update = None

    for i, entry in enumerate(data):
        if entry['Nama'] == nama_to_update:
            index_to_update = i
            break

    if index_to_update is not None:
        entry = data[index_to_update]

        tanggal_masuk_baru = entry["Tanggal Masuk"]

        print(f'''
        DATA YANG AKAN DIUPDATE
        Nama: {entry["Nama"]}
        Usia: {entry["Usia"]} tahun
        Tanggal Masuk: {entry["Tanggal Masuk"]}
        Kategori: {entry["Kategori"]}
        ''')
        
        while True:
            new_nama = input("Masukkan Nama Baru (kosongkan untuk tidak diubah): ")
            if new_nama == '' or new_nama.isalpha():
                new_nama = new_nama.capitalize() if new_nama != '' else entry["Nama"]
                break
            else:
                print("Input yang anda masukkan salah.")

        while True:
            usia_input = input("Masukkan Usia Baru (kosongkan untuk tidak diubah): ")
            if usia_input == '' or (usia_input.isdigit() and int(usia_input) >= 0):
                new_usia = int(usia_input) if usia_input != '' else entry["Usia"]
                break
            else:
                print("Input yang anda masukkan salah.")
        
        while True:
            tanggal_masuk = input("Masukkan Tanggal Baru (DD-MM-YYYY, kosongkan untuk tidak diubah): ")
            if tanggal_masuk == '':
                break
            elif valid_date(tanggal_masuk):
                tanggal_masuk_baru = datetime.strptime(tanggal_masuk, "%d-%m-%Y").strftime("%d-%m-%Y")
                break
            else:
                print("Input yang anda masukkan salah. (DD-MM-YYYY).")
            
        while True:
            new_kategori = input("Masukkan Kategori Baru (1: Parah, 2: Tidak, kosongkan untuk tidak diubah): ")
            if new_kategori == '':
                new_kategori = entry["Kategori"]
                break 
            if new_kategori.isdigit() and new_kategori in ["1", "2"]:
                new_kategori = "Parah" if new_kategori == "1" else "Tidak"
                break
            else:
                print("Pilihan Kategori Hanya ada 1 atau 2.")

        data[index_to_update] = {"Nama": new_nama, "Usia": new_usia, "Tanggal Masuk": tanggal_masuk_baru, "Kategori": new_kategori}
        print("Data berhasil diupdate.")
    else:
        print(f"Data dengan nama {nama_to_update} tidak ditemukan.")

def sort_data():
    print('''
    PILIH KRITERIA SORTING:
    1. Nama
    2. Usia
    3. Tanggal Masuk
    4. Kategori
    ''')

    choice = input("Masukkan nomor kriteria sorting: ")

    if choice == '1':
        key = 'Nama'
    elif choice == '2':
        key = 'Usia'
    elif choice == '3':
        key = 'Tanggal Masuk'
    elif choice == '4':
        key = 'Kategori'
    else:
        print("Pilihan tidak valid.")
        return

    sorted_data = sorted(data, key=itemgetter(key))

    print("\nDATA SETELAH DIURUTKAN:")
    headers = ["Nama", "Usia", "Tanggal Masuk", "Kategori"]
    rows = []
    for i, entry in enumerate(sorted_data):
        if isinstance(entry['Tanggal Masuk'], datetime):
            formatted_date = entry['Tanggal Masuk'].strftime("%d-%m-%Y")
        else:
            formatted_date = entry['Tanggal Masuk']
        rows.append((entry['Nama'], entry['Usia'], formatted_date, entry['Kategori']))
    
    print(tabulate(rows, headers=headers, tablefmt='pretty'))
    print()

def main():
    while True:
        print('''
        ####### HALO SELAMAT DATANG! ######

        Menu Utama
        1. Data Pasien
        2. Pasien Baru
        3. Hapus Data Pasien
        4. Update Data Pasien
        5. Urutkan Data Pasien
        6. Batal
        ''')

        opsi = input("Pilih menu:")
        if opsi == '1':
            read_data()
        elif opsi == '2':
            create_data()
        elif opsi == '3':
            erase_data()
        elif opsi == '4':
            update_data()
        elif opsi == '5':
            sort_data()
        elif opsi == '6':
            break
        else:
            print("Input anda invalid!")

main()    