class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.cek_sks(sks):
            print(f"[PERINGATAN] SKS tidak valid untuk {nama}, harus 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def cek_sks(sks):
        return sks in [2, 3]

class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            print(f"[PERINGATAN] NIM {nim} tidak valid. Harus diawali '23' dan 10 digit.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah Diambil:")
        for mk in self.matkul_diambil:
            print(f"  - {mk.nama} ({mk.kode}, {mk.sks} SKS)")
        print()

    @classmethod
    def get_total_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return len(nim) == 10 and nim[0:2] == "23"

class Kampus:
    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            print(f"[PERINGATAN] Nama kampus '{nama}' tidak valid. Tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info_kampus(cls, nama):
        print(f"Nama Kampus: {nama}")
        print(f"Total Mahasiswa: {Mahasiswa.get_total_mahasiswa()}")

    @staticmethod
    def validasi_nama_kampus(nama):
        angka = "0123456789"
        for karakter in nama:
            if karakter in angka:
                return False
        return True

# --- Objek Mata Kuliah (8) ---
mk1 = MataKuliah("MK001", "DMJ", 3)
mk2 = MataKuliah("MK002", "PBO", 3)
mk3 = MataKuliah("MK003", "PAI", 2)
mk4 = MataKuliah("MK004", "PBW", 3)
mk5 = MataKuliah("MK005", "PBD", 3)
mk6 = MataKuliah("MK006", "BING", 2)
mk7 = MataKuliah("MK007", "EBC", 3)
mk8 = MataKuliah("MK008", "APB", 3)

# --- Objek Mahasiswa (6) ---
mh1 = Mahasiswa("Wiwin", "2312345678", "Sistem Informasi")
mh2 = Mahasiswa("Adiy", "2312345679", "Sistem Informasi")
mh3 = Mahasiswa("Citra", "2312345680", "Informatika")
mh4 = Mahasiswa("Dedi", "2312345681", "Teknik Komputer")
mh5 = Mahasiswa("Eka", "2312345682", "Informatika")
mh6 = Mahasiswa("Fani", "2312345683", "Sistem Informasi")

# --- Tambahkan mata kuliah ke masing-masing mahasiswa (min 4) ---

mh1.tambah_matkul(mk1)
mh1.tambah_matkul(mk2)
mh1.tambah_matkul(mk4)
mh1.tambah_matkul(mk5)

for m in [mh2]:
    m.tambah_matkul(mk1)
    m.tambah_matkul(mk2)
    m.tambah_matkul(mk3)
    m.tambah_matkul(mk5)

for m in [mh3]:
    m.tambah_matkul(mk1)
    m.tambah_matkul(mk2)
    m.tambah_matkul(mk3)
    m.tambah_matkul(mk4)

for m in [mh4]:
    m.tambah_matkul(mk1)
    m.tambah_matkul(mk2)
    m.tambah_matkul(mk5)
    m.tambah_matkul(mk6)

for m in [mh5]:
    m.tambah_matkul(mk1)
    m.tambah_matkul(mk2)
    m.tambah_matkul(mk4)
    m.tambah_matkul(mk5)

for m in [mh6]:
    m.tambah_matkul(mk1)
    m.tambah_matkul(mk2)
    m.tambah_matkul(mk3)
    m.tambah_matkul(mk4)

# --- Objek Kampus ---
kampus = Kampus("Universitas Trunojoyo Madura", "Bangkalan")

# --- Tampilkan Semua Info Mahasiswa dan Matkul ---
print("===== INFO MAHASISWA =====\n")
for m in [mh1, mh2, mh3, mh4, mh5, mh6]:
    m.tampilkan_biodata()

# --- Tampilkan Info Kampus ---
print("===== INFO KAMPUS =====\n")
Kampus.tampilkan_info_kampus(kampus.nama)
print("Nama kampus valid:", Kampus.validasi_nama_kampus(kampus.nama))