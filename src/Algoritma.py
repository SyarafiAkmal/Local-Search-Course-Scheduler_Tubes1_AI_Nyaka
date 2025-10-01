from Kelas import Kelas

class ParentAlgorithm:
    def __init__(self, input):
        """
        Inisialisasi kelas parent algoritma dengan state awal dan data mahasiswa dan juga inisialisasi state awal
        state: list of Kelas    
        mahasiswa: list of dict -> {"nim": str, "daftar_mk": list of str, "prioritas": list of int}
        NOTE: prioritas posisinya respective dengan daftar_mk
        """
        if not input['mahasiswa']:
            raise ValueError("Input tidak valid: mahasiswa kosong")
        
        self.mahasiswa = input['mahasiswa']
        # self.dosen = input['dosen'] buat bonus
        self.convert_input_to_state(input)


        # debug_kls = self.get_kelas_by_kode("IF3140_K01_S2")
        # debug_kls[0].jadwal = {"jadwal_mulai": ['Selasa', 9], "jadwal_selesai": ['Selasa', 11]}
        # debug_kls[0].ruangan = {"kode": "7606", "kuota": 60}
        # debug_kls[0].get_info()

    def tukar_jadwal(self):
        # TODO: implement swap schedule logic, masih nunggu revisi spek
        pass

    def pindah_jadwal(self):
        # TODO: implement move schedule logic, masih nunggu revisi spek
        pass

    def hitung_fungsi_objektif(self):
        # TODO: implement objective function logic
        # BONUS: tambah komponen jadwal dosen, bentuk input jadwal dosen bebas (harusnya bikin variabel baru kayak mahasiswa)

        obj_jadwal_kelas = 0
        obj_kuota_kelas = 0
        obj_jadwal_mahasiswa = 0

        # Cek jadwal kelas
        for i in range (len(self.state)):
            for j in range (i+1, len(self.state)):
                # print(max(self.state[i].jadwal['jadwal_mulai'][1], self.state[j].jadwal['jadwal_mulai'][1]), min(self.state[i].jadwal['jadwal_selesai'][1], self.state[j].jadwal['jadwal_selesai'][1]), "compare", self.state[i].mata_kuliah['kode'], self.state[j].mata_kuliah['kode'], self.state[i].ruangan['kode'], self.state[j].ruangan['kode'])
                if self.state[i].jadwal['jadwal_mulai'][0] == self.state[j].jadwal['jadwal_mulai'][0] and max(self.state[i].jadwal['jadwal_mulai'][1], self.state[j].jadwal['jadwal_mulai'][1]) < min(self.state[i].jadwal['jadwal_selesai'][1], self.state[j].jadwal['jadwal_selesai'][1]) and self.state[i].ruangan['kode'] == self.state[j].ruangan['kode']:
                    # Mata Kuliah Saling Tabrakan Jadwal
                    print("\nTabrakan")
                    self.state[i].get_info()
                    print("\n")
                    self.state[j].get_info()
                    obj_jadwal_kelas -= 3

            kuota = self.state[i].ruangan['kuota']
            jumlah_mhs_daftar = self.state[i].mata_kuliah['jumlah_mhs']

            if jumlah_mhs_daftar > kuota:
                # Ruangan Kelebihan Kapasitas
                obj_kuota_kelas -= (jumlah_mhs_daftar - kuota) * 2
        
        # Cek jadwal mahasiswa
        for mhs in self.mahasiswa:
            daftar_mk = mhs['daftar_mk']
            kelas = []
            
            for mk in daftar_mk:
                kelas += self.get_kelas_by_kode(mk)
            
            for i in range(len(kelas)):
                for j in range(i+1, len(kelas)):
                    if kelas[i].jadwal['jadwal_mulai'][0] == kelas[j].jadwal['jadwal_mulai'][0] and max(kelas[i].jadwal['jadwal_mulai'][1], kelas[i].jadwal['jadwal_mulai'][1]) < min(kelas[i].jadwal['jadwal_selesai'][1], kelas[i].jadwal['jadwal_selesai'][1]):
                        print(f"mhs {mhs['nim']} tabrakan jadwal {kelas[i].mata_kuliah['kode']} dan {kelas[j].mata_kuliah['kode']}")
                        obj_jadwal_mahasiswa -= 2

        # Debug purposes
        print("Objektif:", obj_jadwal_mahasiswa + obj_kuota_kelas + obj_jadwal_kelas)
        print("Objektif Jadwal Kelas:", obj_jadwal_kelas)
        print("Objektif Kuota Kelas:", obj_kuota_kelas)
        print("Objektif Jadwal Mahasiswa:", obj_jadwal_mahasiswa)


    def get_kelas_by_kode(self, kode):
        result = []
        for kelas in self.state:
            if kode in kelas.mata_kuliah['kode']:
                result.append(kelas)

        if result:
            return result
        
        return None

    def convert_input_to_state(self, input):
        import random
        if not input['kelas_mata_kuliah'] or not input['ruangan']:
            raise ValueError("Input tidak valid: kelas_mata_kuliah atau ruangan kosong")
        
        self.state: list[Kelas] = []

        for i in range(len(input['kelas_mata_kuliah'])):
            if input['kelas_mata_kuliah'][i]['sks'] > 2:
                kelas_sesi_1 = Kelas(
                    mata_kuliah={
                        "kode": input['kelas_mata_kuliah'][i]['kode'] + "_S1",
                        "jumlah_mhs": input['kelas_mata_kuliah'][i]['jumlah_mhs'] // 2,
                        "sks": 2,
                        "random_seed": input['kelas_mata_kuliah'][i]['random_seed']
                    },
                    ruangan=input['ruangan'][random.randint(0, len(input['ruangan'])-1)]
                )
                kelas_sesi_2 = Kelas(
                    mata_kuliah={
                        "kode": input['kelas_mata_kuliah'][i]['kode'] + "_S2",
                        "jumlah_mhs": input['kelas_mata_kuliah'][i]['jumlah_mhs'] - (input['kelas_mata_kuliah'][i]['jumlah_mhs'] // 2),
                        "sks": input['kelas_mata_kuliah'][i]['sks'] - 2,
                        "random_seed": input['kelas_mata_kuliah'][i]['random_seed'] + 1
                    },
                    ruangan=input['ruangan'][random.randint(0, len(input['ruangan'])-1)]
                )
                self.state.append(kelas_sesi_1)
                self.state.append(kelas_sesi_2)
            else:
                kelas = Kelas(
                    mata_kuliah=input['kelas_mata_kuliah'][i], 
                    ruangan=input['ruangan'][random.randint(0, len(input['ruangan'])-1)]
                )
                self.state.append(kelas)


    def show_state(self):
        for kelas in self.state:
            kelas.get_info()
            print("\n")

class HC_SA(ParentAlgorithm):
    def __init__(self, input):
        super().__init__(input)

class SimulatedAnnealing(ParentAlgorithm):
    def __init__(self, input):
        super().__init__(input)

class GeneticAlgorithm(ParentAlgorithm):
    def __init__(self, input):
        super().__init__(input)