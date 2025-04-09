class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

daftar_mahasiswa = []
for i in range(3):
    print(f"Masukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    jurusan = input("Prodi: ")
    alamat = input("Alamat: ")
    data_mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    daftar_mahasiswa.append(data_mahasiswa)

print("Data Mahasiswa:")
for mahasiswa in daftar_mahasiswa:
    print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Prodi: {mahasiswa.prodi}, Alamat: {mahasiswa.alamat}")