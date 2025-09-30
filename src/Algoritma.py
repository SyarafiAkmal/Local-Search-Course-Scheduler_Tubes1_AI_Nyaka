class ParentAlgorithm:
    def __init__(self, state, mahasiswa):
        """
        Inisialisasi kelas parent algoritma dengan state awal dan data mahasiswa.
        state: list of Kelas
        mahasiswa: list of dict -> {"nim": str, "daftar_mk": list of str, "prioritas": list of int}
        NOTE: prioritas posisinya respective dengan daftar_mk
        """
        self.state = state
        self.mahasiswa = mahasiswa

    def tukar_jadwal(self):
        # TODO: implement swap schedule logic
        pass

    def pindah_jadwal(self):
        # TODO: implement move schedule logic
        pass

    def fungsi_objektif(self):
        # TODO: implement objective function logic
        pass

class HC_SA(ParentAlgorithm):
    def __init__(self, state, mahasiswa):
        super().__init__(state)
        self.state = state
        self.mahasiswa = mahasiswa

class SimulatedAnnealing(ParentAlgorithm):
    def __init__(self, state, mahasiswa):
        super().__init__(state)
        self.state = state
        self.mahasiswa = mahasiswa

class GeneticAlgorithm(ParentAlgorithm):
    def __init__(self, state, mahasiswa):
        super().__init__(state)
        self.state = state
        self.mahasiswa = mahasiswa