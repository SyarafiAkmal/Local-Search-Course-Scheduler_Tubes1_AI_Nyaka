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

    def tukar_jadwal(self):
        # TODO: implement swap schedule logic, masih nunggu revisi spek
        pass

    def pindah_jadwal(self):
        # TODO: implement move schedule logic, masih nunggu revisi spek
        pass

    def fungsi_objektif(self):
        # TODO: implement objective function logic, masih nunggu revisi spek
        # BONUS: tambah komponen jadwal dosen, bentuk input jadwal dosen bebas (harusnya bikin variabel baru kayak mahasiswa)
        pass

    def convert_input_to_state(self, input):
        import random
        if not input['kelas_mata_kuliah'] or not input['ruangan']:
            raise ValueError("Input tidak valid: kelas_mata_kuliah atau ruangan kosong")
        
        self.state = []

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