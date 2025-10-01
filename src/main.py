from Kelas import Kelas
from Algoritma import HC_SA, SimulatedAnnealing, GeneticAlgorithm


hill_climbing = HC_SA(
    input={
        "kelas_mata_kuliah": [
            {
                "kode": "IF3071_K01",
                "jumlah_mhs": 60,
                "sks": 4,
                "random_seed": 46
            },
            {
                "kode": "IF3130_K01",
                "jumlah_mhs": 45,
                "sks": 2,
                "random_seed": 50
            },
            {
                "kode": "IF3110_K02",
                "jumlah_mhs": 70,
                "sks": 2,
                "random_seed": 32
            },
            {
                "kode": "IF3140_K01",
                "jumlah_mhs": 55,
                "sks": 3,
                "random_seed": 12
            },
            {
                "kode": "IF3110_K02",
                "jumlah_mhs": 70,
                "sks": 2,
                "random_seed": 19
            },
            {
                "kode": "IF3140_K01",
                "jumlah_mhs": 55,
                "sks": 3,
                "random_seed": 27
            }
        ],
        "ruangan": [
            {
                "kode": "7609",
                "kuota": 60
            },
            {
                "kode": "7606",
                "kuota": 80   
            },
            {
                "kode": "multimedia",
                "kuota": 40   
            }
        ],
        "mahasiswa": [
            {
                "nim": "13520001",
                "daftar_mk": ["IF3071_K01", "IF3130_K01", "IF3110_K02"],
                "prioritas": [1, 2, 3]
            },
            {
                "nim": "13520002",
                "daftar_mk": ["IF3071_K01", "IF3140_K01"],
                "prioritas": [1, 2]
            },
            {
                "nim": "13520003",
                "daftar_mk": ["IF3130_K01", "IF3110_K02"],
                "prioritas": [1, 2]
            },
            {
                "nim": "13520004",
                "daftar_mk": ["IF3071_K01", "IF3130_K01", "IF3140_K01"],
                "prioritas": [3, 1, 2]
            }
        ]
    }
)

hill_climbing.show_state()