from Kelas import Kelas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


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
        # self.show_state()


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

        neighbor_tukar = copy.deepcopy(self.state)
        neighbor_pindah = copy.deepcopy(self.state)
        # print(len(neighbor_tukar), "length neighbor")

        i, j = random.sample(range(len(neighbor_tukar)), 2)
        # print(i, j, "tukar")
        self.tukar_jadwal(neighbor_tukar[i], neighbor_tukar[j])

        hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
        jam_mulai_range = list(range(7, 16)) # jam 7 - 18
        i = random.randint(0, len(neighbor_pindah)-1)
        h = random.choice(hari)
        j = random.choice(jam_mulai_range)
        # print(i, j, "pindah")
        jadwal_baru = {
            "jadwal_mulai": [h, j],
            "jadwal_selesai": [h, j + neighbor_pindah[i].mata_kuliah['sks']]
        }

        while self.cek_konflik_jadwal(neighbor_pindah[i], jadwal_baru):
            h = random.choice(hari)
            j = random.choice(jam_mulai_range)
            jadwal_baru = {
                "jadwal_mulai": [h, j],
                "jadwal_selesai": [h, j + neighbor_pindah[i].mata_kuliah['sks']]
            }
        
        self.pindah_jadwal(neighbor_pindah[i], jadwal_baru)

        return max([neighbor_pindah, neighbor_tukar], key=lambda s: self.fungsi_objektif(s))



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

    def visualize_state(self, name="Jadwal_Kuliah_", state=None):
        # Sample array (list of lists)
        if state is None:
            state = self.state

        data = [
            ["Waktu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
            ["07:00-08:00", "", "", "", "", ""],
            ["08:00-09:00", "", "", "", "", ""],
            ["09:00-10:00", "", "", "", "", ""],
            ["10:00-11:00", "", "", "", "", ""],
            ["11:00-12:00", "", "", "", "", ""],
            ["12:00-13:00", "", "", "", "", ""],
            ["13:00-14:00", "", "", "", "", ""],
            ["14:00-15:00", "", "", "", "", ""],
            ["15:00-16:00", "", "", "", "", ""],
            ["16:00-17:00", "", "", "", "", ""],
            ["17:00-18:00", "", "", "", "", ""],
        ]

        jam_mulai_mapping = {
            7: 1,
            8: 2,
            9: 3,
            10: 4,
            11: 5,
            12: 6,
            13: 7,
            14: 8,
            15: 9,
            16: 10,
            17: 11,
        }

        hari_mapping = {
            "Senin": 1,
            "Selasa": 2,
            "Rabu": 3,
            "Kamis": 4,
            "Jumat": 5,
        }    

        for kelas in state:
            # print(kelas.mata_kuliah['kode'], kelas.jadwal, kelas.ruangan)
            hari, jam_mulai = kelas.jadwal['jadwal_mulai'][0], kelas.jadwal['jadwal_mulai'][1]
            sks = kelas.mata_kuliah['sks']
            value = kelas.mata_kuliah['kode'] + " (" + kelas.ruangan['kode'] + ")"
            idx_jam, idx_hari = jam_mulai_mapping[jam_mulai], hari_mapping[hari]

            for j in range(sks):
                if idx_jam + j < len(data):
                    if data[idx_jam + j][idx_hari] == "":
                        data[idx_jam + j][idx_hari] = value
                    else:
                        data[idx_jam + j][idx_hari] += f"\n{value}"



        # Create a PDF document
        pdf_path = f"output/{name}.pdf"
        pdf = SimpleDocTemplate(pdf_path, pagesize=A4)

        # Create table from data
        col_widths = [70, 85, 85, 85, 85, 85]  # adjust as needed

        table = Table(data, colWidths=col_widths)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 6),  # smaller text helps fit
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ])
        table.setStyle(style)

        # Add the table to the PDF and build it
        elements = [table]
        pdf.build(elements)

import time
class HC_SA(ParentAlgorithm):
    def __init__(self, input):
        super().__init__(input)

    def run(self, verbose=False):
        start_time = time.time()
        current_score = self.fungsi_objektif()

        self.visualize_state("HC_Awal_")
        if verbose:
            print(f"Initial score: {current_score:.4f}")
        iteration = 0
        history = [current_score]
        while True:
            iteration += 1
            if verbose:
                print(f"Iterasi ke-{iteration}")
            neighbors = self.get_semua_neighbor()
            if not neighbors:
                if verbose:
                    print("Tidak ada neighbor yang tersedia.")
                break

            best_neighbor = max(neighbors, key=lambda s: self.fungsi_objektif(s))
            best_neighbor_score = self.fungsi_objektif(best_neighbor)
            if verbose:
                print(f"Skor saat ini : {current_score:.4f}, Skor neighbor terbaik: {best_neighbor_score:.4f}")
            if best_neighbor_score > current_score:
                self.state = best_neighbor
                current_score = best_neighbor_score
                history.append(current_score)
                if verbose:
                    print(f"Ditemukan state yang lebih baik dengan skor baru: {current_score:.4f}")
            else:
                if verbose:
                    print("Tidak ada perbaikan, telah mencapai" + "global optimum" if self.fungsi_objektif() == 0 else "lokal optimum")
                break
        end_time = time.time()
        duration = end_time - start_time
        self.visualize_state("HC_Akhir_")
        return self.state, current_score

import math
import random

class SimulatedAnnealing(ParentAlgorithm):
    def __init__(self, input, initial_temp=1000, cooling_rate=0.01, min_temp=1e-3):
        super().__init__(input)
        self.input = input
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp
        
        self.current_state = self.get_random_neighbor()
        self.best_state = self.current_state
        self.best_score = self.fungsi_objektif(self.current_state)

    def run(self, verbose=False):
        current_state = self.current_state
        current_score = self.best_score
        T = self.initial_temp

        self.visualize_state("SA_Awal_")
        
        if verbose:
            print(f"Initial score: {current_score:.4f}")

        while T > self.min_temp:
            neighbor = self.get_random_neighbor()
            neighbor_score = self.fungsi_objektif(neighbor)
            
            delta = neighbor_score - current_score

            if delta > 0:
                current_state = neighbor
                current_score = neighbor_score
            else:
                if random.random() < math.exp(delta / T):
                    current_state = neighbor
                    current_score = neighbor_score

            if current_score > self.best_score:
                self.best_state = current_state
                self.best_score = current_score

            T *= (1 - self.cooling_rate)
            
            if verbose:
                print(f"T={T:.4f} | Current Score={current_score:.2f} | Best={self.best_score:.2f}")

        if verbose:
            print(f"\nFinal best score: {self.best_score:.4f}")
        
        self.visualize_state("SA_Akhir_", state=self.best_state)
        # self.fungsi_objektif(state=self.best_state, verbose=True)

        return self.best_state, self.best_score


class GeneticAlgorithm(ParentAlgorithm):
    def __init__(self, input, population_size=100):
        super().__init__(input)
        self.population_size = population_size
        self.input = input
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

        self.population = sorted(population, key=lambda ind: self.fitness(ind), reverse=True)

    def crossover(self, parent1, parent2):
        import copy
        import random
        
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        
        num_crossover_points = random.randint(2, 4)
        crossover_points = sorted(random.sample(range(1, len(parent1)), num_crossover_points))
        
        swap = False
        prev_point = 0
        
        for point in crossover_points + [len(parent1)]:
            if swap:
                for i in range(prev_point, point):
                    child1[i].jadwal = copy.deepcopy(parent2[i].jadwal)
                    child1[i].ruangan = copy.deepcopy(parent2[i].ruangan)
                    child2[i].jadwal = copy.deepcopy(parent1[i].jadwal)
                    child2[i].ruangan = copy.deepcopy(parent1[i].ruangan)
            swap = not swap
            prev_point = point
        
        return child1, child2
    
        
    def mutate(self, individual, mutation_rate=0.3):
        import random
        import copy
        
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                max_attempts = 50
                for _ in range(max_attempts):
                    h = random.choice(self.hari)
                    j = random.choice(self.range_waktu)
                    r = random.choice(self.ruangan)
                    
                    jadwal_baru = {
                        "jadwal_mulai": [h, j],
                        "jadwal_selesai": [h, j + individual[i].mata_kuliah['sks']]
                    }
                    
                    old_jadwal = copy.deepcopy(individual[i].jadwal)
                    old_ruangan = copy.deepcopy(individual[i].ruangan)
                    
                    individual[i].jadwal = jadwal_baru
                    individual[i].ruangan = r
                    
                    if not self.cek_konflik_jadwal(individual[i], jadwal_baru):
                        break
                    else:
                        individual[i].jadwal = old_jadwal
                        individual[i].ruangan = old_ruangan

    def select_parents(self, tournament_size=5):
        """
        Tournament selection
        """
        import random
        
        parents = []
        for _ in range(self.population_size // 2):
            # Select parent 1
            tournament1 = random.sample(self.population, tournament_size)
            parent1 = max(tournament1, key=lambda ind: self.fitness(ind))
            
            # Select parent 2
            tournament2 = random.sample(self.population, tournament_size)
            parent2 = max(tournament2, key=lambda ind: self.fitness(ind))
            
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

    def run(self, verbose=False, n_generasi=10):
        import random

        self.visualize_state("GA_Awal_")

        bin_individiu = []
        for generasi in range(n_generasi):
            parents = self.select_parents()
            next_generation = []
            print(len(parents))
            for parent1, parent2 in parents:
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                next_generation.extend([child1, child2])

            fitnesses = [self.fitness(ind) for ind in self.population]

            from collections import Counter
            counter = Counter(fitnesses)
            most_common_count = counter.most_common(1)[0][1]
            is_stagnant = most_common_count / len(fitnesses) > 0.3

            if is_stagnant:
                # print("Stagnasi populasi, menambah variasi populasi")
                # time.sleep(2)
                self.population = self.population + next_generation
            
                sorted_pop = sorted(self.population, key=lambda ind: self.fitness(ind), reverse=True)
                top_10 = sorted_pop[:10]
                random_30 = random.sample(bin_individiu, min(10, len(bin_individiu)))
                self.population = top_10 + random_30
            else:
                self.population += next_generation
                bin_individiu += sorted(self.population, key=lambda ind: self.fitness(ind), reverse=True)[20:]
                self.population = sorted(self.population, key=lambda ind: self.fitness(ind), reverse=True)[:20]

            if verbose:
                print(f"Generasi {generasi + 1}:")
                print("Best fitness:", self.fitness(self.population[0]))
                print([self.fitness(ind) for ind in self.population])
                print(len(bin_individiu))
        
        print(self.fungsi_objektif(self.population[0], verbose=True))
        self.visualize_state("GA_Akhir_MutationLama", state=self.population[0])