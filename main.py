"""
Aplikasi deteksi gempa terkini
Modulasi Data dengan Function
"""


def ekstraksi_data():
    """
    Tanggal: 05 Oktober 2021
    Waktu: 18:00:27 WIB
    Magnitudo: 4.5
    Kedalaman: 20 km
    Lokasi: LS: 8.15 BT: 118.10
    Pusat: gempa berada di darat 58 km Barat Laut Dompu
    Dirasakan: (Skala MMI): II Dompu
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '05 Oktober 2021'
    hasil['waktu'] = '18:00:27 WIB'
    hasil['magnitudo'] = 4.5
    hasil['kedalaman'] = 20
    hasil['lokasi'] = {'ls': 1.48, 'bt': 134.01}
    hasil['pusat'] = 'gempa berada di darat 58 km Barat Laut Dompu'
    hasil['dirasakan'] = '(Skala MMI): II Dompu'

    return hasil

def tampilkan_data(result):
    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS= {result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat: {result['pusat']}")
    print(f"Dirasakan: {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result=ekstraksi_data()
    tampilkan_data(result)