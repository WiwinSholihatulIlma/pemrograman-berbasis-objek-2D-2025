class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_halaman(self):
        return self.__halaman

    def set_judul(self, judul):
        self.__judul = judul

    def set_penulis(self, penulis):
        self.__penulis = penulis

    def set_halaman(self, halaman):
        if halaman > 0:
            self.__halaman = halaman
        else:
            print("Jumlah halaman harus lebih dari 0.")


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        for buku in self.daftar_buku:
            print(f"Judul: {buku.get_judul()} | Penulis: {buku.get_penulis()} | Halaman: {buku.get_halaman()}")


perpus = Perpustakaan()
jumlah = int(input("Berapa buku yang ingin ditambahkan? "))

for i in range(jumlah):
    print(f"\nTambah Buku ke-{i+1}")
    judul = input("Judul Buku: ")
    penulis = input("Penulis: ")
    halaman = int(input("Jumlah Halaman: "))

    buku = Buku(" ", " ", 0) 
    buku.set_judul(judul)
    buku.set_penulis(penulis)
    buku.set_halaman(halaman)

    perpus.tambah_buku(buku)

print("\n=== Daftar Buku di Perpustakaan ===")
perpus.tampilkan_buku()