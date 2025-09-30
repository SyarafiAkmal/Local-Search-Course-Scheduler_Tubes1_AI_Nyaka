class Kelas:
    def __init__(self, mata_kuliah, ruangan):
        """
        Inisialisasi kelas dengan mata kuliah dan ruangan.
        mata_kuliah: dict -> {"kode": str, jumlah_mhs: int, sks: int}
        ruangan: dict -> {"kode": str, kuota: int}
        """
        self.mata_kuliah = mata_kuliah
        self.ruangan = ruangan
        self.randomize_jadwal()

    def randomize_jadwal(self):
        import random
        hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
        jam_mulai = random.randint(7, 17)
        self.jadwal = {
            "jadwal_mulai": [hari[random.randint(0, 4)], jam_mulai],
            "jadwal_selesai": [hari[random.randint(0, 4)], jam_mulai + self.mata_kuliah["sks"]]
            }