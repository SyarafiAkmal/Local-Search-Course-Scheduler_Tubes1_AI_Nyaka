from Kelas import Kelas

class ParentAlgorithm:
    def __init__(self, input):
        """
        Inisialisasi kelas parent algoritma dengan state awal dan data mahasiswa dan juga inisialisasi state awal

        input: dict -> {"kelas_mata_kuliah": list of dict, "ruangan": list of dict, "mahasiswa": list of dict}
        kelas_mata_kuliah: list of dict -> {"kode": str, "jumlah_mhs": int, "sks": int, "random_seed": int}
        ruangan: list of dict -> {"kode": str, "kuota": int}   
        mahasiswa: list of dict -> {"nim": str, "daftar_mk": list of str, "prioritas": list of int}

        NOTE: prioritas posisinya respective terhadap daftar_mk [1 itu prioritas tertinggi, dst]
        """

        if not input['mahasiswa']:
            raise ValueError("Input tidak valid: mahasiswa kosong")
        
        self.mahasiswa = input['mahasiswa']
        self.ruangan = input['ruangan']
        # self.dosen = input['dosen'] buat bonus
        self.convert_input_ke_state(input)


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
                new_state = copy.deepcopy(self.state)
                self.tukar_jadwal(new_state[i], new_state[j])
                # print("Tukar Jadwal Kelas", new_state[i].mata_kuliah['kode'], "dan", new_state[j].mata_kuliah['kode'])
                neighbor_tukar.append(new_state)

        # Pindah Jadwal
        hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
        jam_mulai_range = list(range(7, 16)) # jam 7 - 18
        for i in range(len(self.state)):
            for h in hari:
                for j in jam_mulai_range:
                    for r in self.ruangan:
                        new_state = copy.deepcopy(self.state)
                        jadwal_baru = {
                            "jadwal_mulai": [h, j],
                            "jadwal_selesai": [h, j + new_state[i].mata_kuliah['sks']]
                        }

                        if r['kode'] != new_state[i].ruangan['kode']:
                            new_state[i].ruangan = r

                        if not self.cek_konflik_jadwal(new_state[i], jadwal_baru):
                            self.pindah_jadwal(new_state[i], jadwal_baru)
                            neighbor_pindah.append(new_state)


        # debug purposes
        # self.show_state(neighbor_pindah[0])
        # print(len(neighbor_tukar))
        # print(len(neighbor_pindah))

        return neighbor_tukar + neighbor_pindah
    
    def get_random_neighbor(self):
        """
        Fungsi untuk mendapatkan satu neighbor secara acak dari state saat ini: List[Kelas]
        """
        import copy
        import random

        neighbor = copy.deepcopy(self.state)
        metode = random.choice(['tukar', 'pindah'])

        if metode == 'tukar':
            i, j = random.sample(range(len(neighbor)), 2)
            self.tukar_jadwal(neighbor[i], neighbor[j])
            # print("Tukar Jadwal Kelas", neighbor[i].mata_kuliah['kode'], "dan", neighbor[j].mata_kuliah['kode'])

        else: # metode == 'pindah'
            hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
            jam_mulai_range = list(range(7, 16)) # jam 7 - 18
            i = random.randint(0, len(neighbor)-1)
            h = random.choice(hari)
            j = random.choice(jam_mulai_range)
            jadwal_baru = {
                "jadwal_mulai": [h, j],
                "jadwal_selesai": [h, j + neighbor[i].mata_kuliah['sks']]
            }

            while self.cek_konflik_jadwal(neighbor[i], jadwal_baru):
                h = random.choice(hari)
                j = random.choice(jam_mulai_range)
                jadwal_baru = {
                    "jadwal_mulai": [h, j],
                    "jadwal_selesai": [h, j + neighbor[i].mata_kuliah['sks']]
                }
            
            self.pindah_jadwal(neighbor[i], jadwal_baru)
            # print("Pindah Jadwal Kelas", neighbor[i].mata_kuliah['kode'], "ke", jadwal_baru)
        
        return neighbor



    def tukar_jadwal(self, kelas1: Kelas, kelas2: Kelas):
        """
        Fungsi untuk menukar jadwal dua kelas (menukar jadwal: dict -> {'jadwal_mulai': [hari, jam_mulai], 'jadwal_selesai': [hari, jam_mulai + sks]})
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
                    durasi_tabrakan = min(state[i].jadwal['jadwal_selesai'][1], state[j].jadwal['jadwal_selesai'][1]) - max(state[i].jadwal['jadwal_mulai'][1], state[j].jadwal['jadwal_mulai'][1])
                    list_bobot = self.get_mahasiswa_prioritas_by_kelas(state[i].mata_kuliah['kode'])
                    list_bobot += self.get_mahasiswa_prioritas_by_kelas(state[j].mata_kuliah['kode'])
                    bobot = 0

                    if verbose:
                        print("\nTabrakan")
                        state[i].get_info()
                        print("-----")
                        state[j].get_info()
                        print("-----")
                        print(f"Durasi Tabrakan: {durasi_tabrakan} jam")
                        print(f"Prioritas Mahasiswa di Kelas {state[i].mata_kuliah['kode']}: {list_bobot}")
                        print("-----\n")

                    for prioritas in list_bobot:
                        if prioritas == 1:
                            bobot += 1.75
                        elif prioritas == 2:
                            bobot += 1.5
                        elif prioritas == 3:
                            bobot += 1.25
                        else:
                            bobot += 1

                    obj_jadwal_kelas -= durasi_tabrakan * bobot

                    # obj_jadwal_kelas -= 3

            kuota = state[i].ruangan['kuota']
            jumlah_mhs_daftar = state[i].mata_kuliah['jumlah_mhs']

            if jumlah_mhs_daftar > kuota:
                # Ruangan Kelebihan Kapasitas
                # debug puporses
                if verbose:
                    print(f"\nKelebihan Kapasitas Kelas {state[i].mata_kuliah['kode']}: Kuota {kuota}, Jumlah Mahasiswa {jumlah_mhs_daftar}")

                obj_kuota_kelas -= (jumlah_mhs_daftar - kuota) * 2
        
        # Cek jadwal mahasiswa
        for mhs in self.mahasiswa:
            daftar_mk = mhs['daftar_mk']
            kelas = []
            
            for mk in daftar_mk:
                kelas += self.get_kelas_by_kode(mk, state)
            
            for i in range(len(kelas)):
                for j in range(i+1, len(kelas)):
                    if kelas[i].jadwal['jadwal_mulai'][0] == kelas[j].jadwal['jadwal_mulai'][0] and max(kelas[i].jadwal['jadwal_mulai'][1], kelas[j].jadwal['jadwal_mulai'][1]) < min(kelas[i].jadwal['jadwal_selesai'][1], kelas[j].jadwal['jadwal_selesai'][1]):
                        # debug purposes
                        if verbose:
                            print(f"mhs {mhs['nim']} tabrakan jadwal {kelas[i].mata_kuliah['kode']} dan {kelas[j].mata_kuliah['kode']}")

                        obj_jadwal_mahasiswa -= 2

        # debug purposes
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
    
    def get_mahasiswa_prioritas_by_kelas(self, kode_kelas):
        result = []
        for mhs in self.mahasiswa:
            for i, mk in enumerate(mhs['daftar_mk']):
                if mk in kode_kelas:
                    result.append(mhs['prioritas'][i])
                    break
        
        return result

    def convert_input_ke_state(self, input):
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

    def run(self, verbose=False):
        # TODO: implementasi algoritmanya di sini, bisa langsung panggil semua metode yang ada di ParentAlgorithm
        # contoh:
        self.get_semua_neighbor() # list[list[Kelas] -> State]
        self.get_random_neighbor() # list[Kelas] -> State (random neighbor)
        self.fungsi_objektif() # integer, kalo gaada param state dia ngembaliin nilai objektif self.state
        self.show_state()
        pass
        
class SimulatedAnnealing(ParentAlgorithm):
    def __init__(self, input):
        super().__init__(input)
    
    def run(self):
        # TODO: implementasi algoritmanya di sini, bisa langsung panggil semua metode yang ada di ParentAlgorithm
        # contoh:
        self.get_random_neighbor()
        self.fungsi_objektif()
        self.show_state()
        pass

class GeneticAlgorithm(ParentAlgorithm):
    def __init__(self, input, population_size=4, n_generasi=10):
        super().__init__(input)
        self.population_size = population_size
        self.input = input
        self.n_generasi = n_generasi
        self.hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
        self.range_waktu = list(range(7, 16))
        self.inisialisasi_populasi()

    def inisialisasi_populasi(self):
        import random
        import copy
        population = [self.state]
        
        for _ in range(self.population_size - 1):
            new_state = copy.deepcopy(self.state)
            for kelas in new_state:
                kelas.randomize_jadwal(seed=random.randint(0, 10000))
            
            population.append(new_state)

        self.population = population
    
    def crossover(self, parent1, parent2):
        import copy
        import random

        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        crossover_point = random.randint(1, len(parent1) - 1)
        for i in range(crossover_point, len(parent1)):
            child1[i].jadwal, child2[i].jadwal = child2[i].jadwal, child1[i].jadwal
            child1[i].ruangan, child2[i].ruangan = child2[i].ruangan, child1[i].ruangan
        
        return child1, child2

    def mutate(self, individual, mutation_rate=0.1):
        import random
        hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
        jam_mulai_range = list(range(7, 16)) # jam 7 - 18

        random_index = random.randint(0, len(individual)-1)

        if random.random() < mutation_rate:
            random_index = random.randint(0, len(individual) - 1)

        for h in hari:
            for j in jam_mulai_range:
                for r in self.ruangan:
                    jadwal_baru = {
                        "jadwal_mulai": [h, j],
                        "jadwal_selesai": [h, j + individual[random_index].mata_kuliah['sks']]
                    }

                    if r['kode'] != individual[random_index].ruangan['kode']:
                        individual[random_index].ruangan = r

                    if not self.cek_konflik_jadwal(individual[random_index], jadwal_baru):
                        self.pindah_jadwal(individual[random_index], jadwal_baru)
                        return
        

    def select_parents(self):
        """
        Seleksi parent dengan metode roulette wheel selection
        """
        import random
        parents = []
        for _ in range(self.population_size // 2):
            fitnesses = [self.fitness(ind) for ind in self.population]
            total_fitness = sum(fitnesses)
            probabilities = [f / total_fitness for f in fitnesses]
            roulette_wheel = [round(sum(probabilities[:i+1]), 3) for i in range(len(probabilities))]
            
            random_value1 = round(random.uniform(0, 1), 3)
            random_value2 = round(random.uniform(0, 1), 3)

            parent1 = None
            parent2 = None

            for i, value in enumerate(roulette_wheel):
                if random_value1 <= value and parent1 is None:
                    parent1 = self.population[i]
                if random_value2 <= value and parent2 is None:
                    parent2 = self.population[i]
                if parent1 is not None and parent2 is not None:
                    break
            parents.append((parent1, parent2))
        
        return parents
        

    def fitness(self, individual):
        """
        Fungsi fitness dengan pemanfaatan fungsi objektif (selalu bernilai negatif)
        Semakin besar nilai fitness, semakin baik individu tersebut
        """
        # print(len(self.input['kelas_mata_kuliah']) + len(self.input['ruangan']) + len(self.input['mahasiswa']))
        return 100 * (len(self.input['kelas_mata_kuliah']) + len(self.input['ruangan']) + len(self.input['mahasiswa'])) + self.fungsi_objektif(individual)
    
    def show_population(self):
        for i, individual in enumerate(self.population):
            print(f"Individu {i+1}:")
            self.show_state(individual)
            print("Fitness:", self.fitness(individual))
            print("====================================\n")

    def run(self, verbose=False):
        # Inisialisasi semua parent
        for generasi in range(self.n_generasi):
            # Seleksi parent
            parents = self.select_parents()
            # Crossover dan Mutasi untuk menghasilkan anak
            next_generation = []
            for parent1, parent2 in parents:
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                next_generation.extend([child1, child2])
            self.population += next_generation
            self.population = sorted(self.population, key=lambda ind: self.fitness(ind), reverse=True)[:40]

            if verbose:
                print(f"Generasi {generasi + 1}:")
                print("Fitness:", self.fitness(self.population[0]))
                print(len(self.population))
                # self.show_population()