class Kelas:
    def __init__(self, mata_kuliah, ruangan):
        """
        Inisialisasi kelas dengan mata kuliah dan ruangan.
        mata_kuliah: dict -> {"kode": str, jumlah_mhs: int, sks: int, random_seed: int}
        ruangan: dict -> {"kode": str, kuota: int}
        jadwal: dict -> {"jadwal_mulai": [hari: str, jam: int], "jadwal_selesai": [hari: str, jam: int]}
        """
        self.mata_kuliah = mata_kuliah
        self.ruangan = ruangan
        self.randomize_jadwal()

    def randomize_jadwal(self):
        import random
        random.seed(self.mata_kuliah["random_seed"])
        hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
        jam_mulai = random.randint(7, 16) # jam 7 - 18
        hari_random = hari[random.randint(0, 4)]
        self.jadwal = {
            "jadwal_mulai": [hari_random, jam_mulai],
            "jadwal_selesai": [hari_random, jam_mulai + self.mata_kuliah["sks"]]
            }
        
    def get_info(self):
        print(f"Mata Kuliah: {self.mata_kuliah['kode']}\nSKS: {self.mata_kuliah['sks']}\nJumlah Mahasiswa: {self.mata_kuliah['jumlah_mhs']}\nRuangan: {self.ruangan['kode']}\nKuota Ruangan: {self.ruangan['kuota']}\nJadwal Mulai: {self.jadwal['jadwal_mulai'][0]} jam {self.jadwal['jadwal_mulai'][1]}\nJadwal Selesai: {self.jadwal['jadwal_selesai'][0]} jam {self.jadwal['jadwal_selesai'][1]}")