class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        pass
    
    def berjalan(self):
        return f"{self.nama} sedang berjalan"
    
    def berlari(self):
        return f"{self.nama} sedang berlari"

manusia1 = Manusia("Wiwin", 19, "Gresik")
manusia2 = Manusia("Adiy", 20, "Surabaya")
manusia3 = Manusia("Afta", 20, "Medan")
manusia4 = Manusia("Putri", 18, "Lamongan")
manusia5 = Manusia("Riza", 19, "Jombang")

print(f"{manusia1.berjalan()}")
print(f"{manusia2.berjalan()}")
print(f"{manusia3.berlari()}")
print(f"{manusia4.berlari()}")
print(f"{manusia5.berlari()}")