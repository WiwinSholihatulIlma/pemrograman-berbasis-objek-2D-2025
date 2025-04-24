class Kucing:
    hewan_list = [] 

    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
        Kucing.hewan_list.append(self)  

    def bersuara(self):
        return f"{self.nama} adalah kucing {self.jenis} dan bersuara: {self.suara}"

    def tampilkan_kucing(self):
        print("Daftar Kucing:")
        for kucing in Kucing.hewan_list:
            print(kucing.bersuara())

kucing1 = Kucing("Clo", "Persia", "Meow")
kucing2 = Kucing("Choco", "Anggora", "Meow Meow")
kucing3 = Kucing("Kitty", "Bengal", "Miaw")

class Anjing:
    hewan_list = []  

    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
        Anjing.hewan_list.append(self)  

    def bersuara(self):
        return f"{self.nama} adalah anjing {self.jenis} dan bersuara: {self.suara}"

    def tampilkan_anjing(self):
        print("Daftar Anjing:")
        for anjing in Anjing.hewan_list:
            print(anjing.bersuara())

anjing1 = Anjing("Buddy", "Golden Retriever", "Guk Guk")
anjing2 = Anjing("Molly", "Bulldog", "Woof Woof")
anjing3 = Anjing("Bella", "Beagle", "Arf Arf")

class Ular:
    hewan_list = []  

    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
        Ular.hewan_list.append(self)  

    def bersuara(self):
        return f"{self.nama} adalah ular {self.jenis} dan bersuara: {self.suara}"

    def tampilkan_ular(self):
        print("Daftar Ular:")
        for ular in Ular.hewan_list:
            print(ular.bersuara())

ular1 = Ular("Leon", "Python", "Hiss")
ular2 = Ular("Sellena", "Cobra", "Hiss Hiss")
ular3 = Ular("Jupiter", "Viper", "Hiss Hiss Hiss")

kucing1.tampilkan_kucing()
print()  
anjing1.tampilkan_anjing()
print()  
ular1.tampilkan_ular()
print()