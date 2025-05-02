class Karyawan :
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen
    
    def info (self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}")


class Karyawan_Tetap (Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
       print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}, Tunjangan: {self.tunjangan}")


class Karyawan_Harian (Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}, Jam Kerja: {self.jam_kerja} jam/hari")


class Manajemen_Karyawan :
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

# Membuat objek Manajemen Karyawan
manajemen = Manajemen_Karyawan()

# membuat daftar karyawan tetap
karyawan1 = Karyawan_Tetap ("Sodikin", 8000000, "IT", 2000000)
karyawan2 = Karyawan_Tetap ("Amin", 6000000, "HRD", 1500000)
karyawan3 = Karyawan_Tetap ("Mita", 4000000, "Marketing", 1000000)
karyawan4 = Karyawan_Tetap ("Dina", 4000000, "Marketing", 1000000)

# membuat daftar karyawan harian
karyawan5 = Karyawan_Harian ("Indah", 3000000, "Produksi", 8)
karyawan6 = Karyawan_Harian ("Agus", 3000000, "Produksi", 8)
karyawan7 = Karyawan_Harian ("Lintang", 2500000, "Seles", 6)
karyawan8 = Karyawan_Harian ("Mimin", 2500000, "Seles", 6)

# menambahkan karyawan kedalam manajemen karyawan
manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)
manajemen.tambah_karyawan(karyawan4)
manajemen.tambah_karyawan(karyawan5)
manajemen.tambah_karyawan(karyawan6)
manajemen.tambah_karyawan(karyawan7)
manajemen.tambah_karyawan(karyawan8)

# menampilkan informasi karyawan
manajemen.tampilkan_semua_karyawan()