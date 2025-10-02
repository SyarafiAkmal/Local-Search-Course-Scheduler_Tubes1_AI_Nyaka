from Kelas import Kelas

class ParentAlgorithm:
    def __init__(self, input):
        """
        Inisialisasi kelas parent algoritma dengan state awal dan data mahasiswa dan juga inisialisasi state awal
        state: list of Kelas    
        mahasiswa: list of dict -> {"nim": str, "daftar_mk": list of str, "prioritas": list of int}
        NOTE: prioritas posisinya respective terhadap daftar_mk [1 itu prioritas tertinggi, dst]
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

    def get_semua_neighbor(self):
        """
        Fungsi untuk mendapatkan semua neighbor dari state saat ini: List[List[Kelas]]
        State dan Neighbor: List[Kelas]
        Neighbor di-generate dengan dua cara: tukar_jadwal() dan pindah_jadwal(), keduanya akan digunakan untuk akumulasi neighbor
        """
        import copy

        neighbor_tukar = []
        neighbor_pindah = []

        # Tukar Jadwal
        for i in range(len(self.state)):
            for j in range(i+1, len(self.state)):
                # Buat salinan state
                new_state = copy.deepcopy(self.state)
                # Tukar jadwal kelas i dan j
                self.tukar_jadwal(new_state[i], new_state[j])
                # print("Tukar Jadwal Kelas", new_state[i].mata_kuliah['kode'], "dan", new_state[j].mata_kuliah['kode'])
                neighbor_tukar.append(new_state)

        # Pindah Jadwal
        hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
        jam_mulai_range = list(range(7, 16)) # jam 7 - 18
        for i in range(len(self.state)):
            # Buat salinan state
            for h in hari:
                for j in jam_mulai_range:
                    new_state = copy.deepcopy(self.state)
                    jadwal_baru = {
                        "jadwal_mulai": [h, j],
                        "jadwal_selesai": [h, j + new_state[i].mata_kuliah['sks']]
                    }
                    # Pindah jadwal kelas i ke jadwal baru
                    self.pindah_jadwal(new_state[i], jadwal_baru)
                    neighbor_pindah.append(new_state)


        # debug purposes
        # self.show_state(neighbor_pindah[0])
        print(len(neighbor_tukar))
        print(len(neighbor_pindah))

        return neighbor_pindah

    def tukar_jadwal(self, kelas1: Kelas, kelas2: Kelas):
        """
        Fungsi untuk menukar jadwal dua kelas (menukar jadwal: dict -> {'jadwal_mulai': [hari, jam], 'jadwal_selesai': [hari, jam]})
        """
        import copy

        jadwal_kelas1 = copy.deepcopy(kelas1.jadwal)
        jadwal_kelas2 = copy.deepcopy(kelas2.jadwal)

        kelas1.jadwal['jadwal_mulai'], kelas1.jadwal['jadwal_selesai'] = jadwal_kelas2['jadwal_mulai'], [jadwal_kelas2['jadwal_selesai'][0], jadwal_kelas2['jadwal_mulai'][1] + kelas1.mata_kuliah['sks']]
        kelas2.jadwal['jadwal_mulai'], kelas2.jadwal['jadwal_selesai'] = jadwal_kelas1['jadwal_mulai'], [jadwal_kelas1['jadwal_selesai'][0], jadwal_kelas1['jadwal_mulai'][1] + kelas2.mata_kuliah['sks']]

    def pindah_jadwal(self, kelas: Kelas, jadwal_baru):
        """
        Fungsi untuk memindah jadwal kelas ke jadwal baru jika tidak ada konflik jadwal kelas lain (jadwal tabrakan dan ruangan sama)
        """
        if not self.cek_konflik_jadwal(kelas, jadwal_baru):
            kelas.jadwal = jadwal_baru
            # debug purposes
            # print("Pindah Jadwal Kelas", kelas.mata_kuliah['kode'], "ke", jadwal_baru)
        

    def cek_konflik_jadwal(self, kelas: Kelas, jadwal_baru):
        """
        Fungsi untuk mengecek apakah jadwal baru konflik dengan jadwal kelas lain (jadwal tabrakan dan ruangan sama)
        """
        konflik = False
        for kls in self.state:
            if kls.jadwal['jadwal_mulai'][0] == jadwal_baru['jadwal_mulai'][0] and max(kls.jadwal['jadwal_mulai'][1], jadwal_baru['jadwal_mulai'][1]) < min(kls.jadwal['jadwal_selesai'][1], jadwal_baru['jadwal_selesai'][1]) and kls.ruangan['kode'] == kelas.ruangan['kode']:
                konflik = True
                # debug purposes
                # print("Konflik Jadwal Kelas", kelas.mata_kuliah['kode'], 'di', jadwal_baru, "ruangan:", kelas.ruangan, "dengan Kelas", kls.mata_kuliah['kode'], "jadwal-ruangan:", kls.jadwal, kls.ruangan)
                break

        return konflik

    def fungsi_objektif(self, state=None, verbose=False):
        # TODO: implement objective function logic
        # BONUS: tambah komponen jadwal dosen, bentuk input jadwal dosen bebas (harusnya bikin variabel baru kayak mahasiswa)

        if state is None:
            state = self.state

        obj_jadwal_kelas = 0
        obj_kuota_kelas = 0
        obj_jadwal_mahasiswa = 0

        # Cek jadwal kelas
        for i in range (len(state)):
            for j in range (i+1, len(state)):
                if state[i].jadwal['jadwal_mulai'][0] == state[j].jadwal['jadwal_mulai'][0] and max(state[i].jadwal['jadwal_mulai'][1], state[j].jadwal['jadwal_mulai'][1]) < min(state[i].jadwal['jadwal_selesai'][1], state[j].jadwal['jadwal_selesai'][1]) and state[i].ruangan['kode'] == state[j].ruangan['kode']:
                    # Mata Kuliah Saling Tabrakan Jadwal
                    # debug purposes
                    if verbose:
                        print("\nTabrakan")
                        state[i].get_info()
                        print("-----")
                        state[j].get_info()
                        print("-----")

                    obj_jadwal_kelas -= 3

            kuota = state[i].ruangan['kuota']
            jumlah_mhs_daftar = state[i].mata_kuliah['jumlah_mhs']

            if jumlah_mhs_daftar > kuota:
                # Ruangan Kelebihan Kapasitas
                # debug puporses
                # print(f"\nKelebihan Kapasitas Kelas {state[i].mata_kuliah['kode']}: Kuota {kuota}, Jumlah Mahasiswa {jumlah_mhs_daftar}")

                obj_kuota_kelas -= (jumlah_mhs_daftar - kuota) * 2
        
        # Cek jadwal mahasiswa
        for mhs in self.mahasiswa:
            daftar_mk = mhs['daftar_mk']
            kelas = []
            
            for mk in daftar_mk:
                kelas += self.get_kelas_by_kode(mk, state)
            
            # print(f"\nMahasiswa {mhs['nim']} mengambil mata kuliah {[kls.mata_kuliah['kode'] for kls in kelas]}")
            
            for i in range(len(kelas)):
                for j in range(i+1, len(kelas)):
                    if kelas[i].jadwal['jadwal_mulai'][0] == kelas[j].jadwal['jadwal_mulai'][0] and max(kelas[i].jadwal['jadwal_mulai'][1], kelas[i].jadwal['jadwal_mulai'][1]) < min(kelas[i].jadwal['jadwal_selesai'][1], kelas[i].jadwal['jadwal_selesai'][1]):
                        # debug purposes
                        if verbose:
                            print(f"mhs {mhs['nim']} tabrakan jadwal {kelas[i].mata_kuliah['kode']} dan {kelas[j].mata_kuliah['kode']}")

                        obj_jadwal_mahasiswa -= 2

        # Debug purposes
        if verbose:
            print("Objektif:", obj_jadwal_mahasiswa + obj_kuota_kelas + obj_jadwal_kelas)
            print("Objektif Jadwal Kelas:", obj_jadwal_kelas)
            print("Objektif Kuota Kelas:", obj_kuota_kelas)
            print("Objektif Jadwal Mahasiswa:", obj_jadwal_mahasiswa)

        return obj_jadwal_mahasiswa + obj_kuota_kelas + obj_jadwal_kelas


    def get_kelas_by_kode(self, kode, state=None):
        if state is None:
            state = self.state
        result = []
        for kelas in state:
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
            # random.seed(input['kelas_mata_kuliah'][i]['random_seed'])
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

    def show_state(self, state=None):
        if state is None:
            state = self.state

        for kelas in state:
            kelas.get_info()
            print("\n")

class HC_SA(ParentAlgorithm):
    def __init__(self, input):
        super().__init__(input)

    def run(self):
        # TODO: implementasi algoritmanya di sini, bisa langsung panggil semua metode yang ada di ParentAlgorithm
        # contoh:
        self.tukar_jadwal()
        self.pindah_jadwal()
        self.hitung_fungsi_objektif()
        self.show_state()
        pass

class SimulatedAnnealing(ParentAlgorithm):
    def __init__(self, input):
        super().__init__(input)
    
    def run(self):
        # TODO: implementasi algoritmanya di sini, bisa langsung panggil semua metode yang ada di ParentAlgorithm
        # contoh:
        self.tukar_jadwal()
        self.pindah_jadwal()
        self.hitung_fungsi_objektif()
        self.show_state()
        pass

class GeneticAlgorithm(ParentAlgorithm):
    def __init__(self, input):
        super().__init__(input)
    
    def run(self):
        pass