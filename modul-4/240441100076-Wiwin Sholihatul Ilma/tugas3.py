class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def get_keluhan(self):
        return self.__keluhan

    def set_nama(self, nama):
        self.__nama = nama

    def set_umur(self, umur):
        if umur > 0:
            self.__umur = umur
        else:
            print("Umur tidak boleh kurang dari 1.")

    def set_keluhan(self, keluhan):
        self.__keluhan = keluhan

class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.daftar_pasien.append(pasien)

    def tampilkan_pasien(self):
        for p in self.daftar_pasien:
            print(f"Nama: {p.get_nama()} | Umur: {p.get_umur()} | Keluhan: {p.get_keluhan()}")


klinik = Klinik()
jumlah = int(input("Berapa pasien yang ingin diperiksa? "))

for i in range(jumlah):
    print(f"\nTambah Data Pasien ke-{i+1}")
    nama = input("Nama Pasien: ")
    umur = int(input("Umur: "))
    keluhan = input("Keluhan: ")

    pasien = Pasien(" ", 0, " ")  
    pasien.set_nama(nama)
    pasien.set_umur(umur)
    pasien.set_keluhan(keluhan)

    klinik.tambah_pasien(pasien)

print("\n=== Daftar Pasien Klinik ===")
klinik.tampilkan_pasien()