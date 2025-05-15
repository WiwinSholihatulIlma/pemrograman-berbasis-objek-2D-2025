class RekeningBank:
    def __init__(self, no_rek, nama, saldo):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo

    def get_no_rek(self):
        return self.__no_rek

    def get_nama(self):
        return self.__nama

    def get_saldo(self):
        return self.__saldo

    def set_nama(self, nama):
        self.__nama = nama

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("Saldo tidak boleh mines.")

    def setor(self, jumlah):
        if jumlah > 0:
            saldo_baru = self.get_saldo() + jumlah
            self.set_saldo(saldo_baru)
        else:
            print("Jumlah setor harus lebih dari 0.")

    def tarik(self, jumlah):
        if jumlah <= self.get_saldo():
            saldo_baru = self.get_saldo() - jumlah
            self.set_saldo(saldo_baru)
        else:
            print("Saldo tidak cukup!")

class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)

    def cari_rekening(self, no_rek):
        for rek in self.rekening_list:
            if rek.get_no_rek() == no_rek:
                return rek
        return None

    def tampilkan_rekening(self):
        for rek in self.rekening_list:
            print(f"No Rek: {rek.get_no_rek()} | Nama: {rek.get_nama()} | Saldo: {rek.get_saldo()}")

bank = Bank()

while True:
    print("\nMenu:")
    print("1. Tambah Rekening")
    print("2. Setor")
    print("3. Tarik")
    print("4. Tampilkan Rekening")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        no = input("No Rekening: ")
        nama = input("Nama Pemilik: ")
        saldo = float(input("Saldo Awal: "))
        bank.tambah_rekening(RekeningBank(no, nama, saldo))

    elif pilihan == "2":
        no = input("No Rekening: ")
        rekening = bank.cari_rekening(no)
        if rekening:
            jumlah = float(input("Jumlah Setor: "))
            rekening.setor(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    elif pilihan == "3":
        no = input("No Rekening: ")
        rekening = bank.cari_rekening(no)
        if rekening:
            jumlah = float(input("Jumlah Tarik: "))
            rekening.tarik(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    elif pilihan == "4":
        bank.tampilkan_rekening()

    elif pilihan == "5":
        print("Terimakasih")
        break

    else:
        print("Pilihan tidak valid.")