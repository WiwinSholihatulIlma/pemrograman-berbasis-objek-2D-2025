class Pengiriman :
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5
    
class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        
    def estimasi_waktu(self):
        if self.jenis_kendaraan == 'motor':
            return 3
        elif self.jenis_kendaraan == 'mobil':
            return 5
        elif self.jenis_kendaraan == 'truk':
            return 7
        else:
            return super().estimasi_waktu()

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
        
    def estimasi_waktu(self):
        if self.maskapai == 'Garuda':
            return 2
        elif self.maskapai == 'Lion Air':
            return 3
        else:
            return super().estimasi_waktu()

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai
        
    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        waktu_tercepat = min(waktu_darat, waktu_udara)
        
        if self.tujuan.lower() != 'indonesia':
            return waktu_tercepat + 3
        return waktu_tercepat


pengiriman1 = PengirimanInternasional('Jakarta', 'Indonesia', 'truk', 'Lion Air')
pengiriman2 = PengirimanInternasional('Bandung', 'Malaysia', 'motor', 'Garuda')
pengiriman3 = PengirimanInternasional('Surabaya', 'Singapura', 'mobil', 'Lion Air')

print(f"Estimasi waktu pengiriman 1: {pengiriman1.estimasi_waktu()} hari")
print(f"Estimasi waktu pengiriman 2: {pengiriman2.estimasi_waktu()} hari")
print(f"Estimasi waktu pengiriman 3: {pengiriman3.estimasi_waktu()} hari")
print(f"Tujuan {pengiriman1.tujuan}")