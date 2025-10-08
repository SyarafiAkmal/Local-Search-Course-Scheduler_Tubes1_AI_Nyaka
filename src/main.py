from Kelas import Kelas
from Algoritma import HC_SA, SimulatedAnnealing, GeneticAlgorithm

hill_climbing_large_sample = HC_SA(
    input = {
        "kelas_mata_kuliah": [
            # 6 Mata Kuliah Wajib Semester 5 - Max 3 sections each
            {"kode": "IF3071_K01", "jumlah_mhs": 65, "sks": 4, "random_seed": 46},
            {"kode": "IF3071_K02", "jumlah_mhs": 60, "sks": 4, "random_seed": 47},
            {"kode": "IF3071_K03", "jumlah_mhs": 58, "sks": 4, "random_seed": 48},
            
            {"kode": "IF3130_K01", "jumlah_mhs": 48, "sks": 2, "random_seed": 50},
            {"kode": "IF3130_K02", "jumlah_mhs": 45, "sks": 2, "random_seed": 51},
            {"kode": "IF3130_K03", "jumlah_mhs": 50, "sks": 2, "random_seed": 52},
            
            {"kode": "IF3110_K01", "jumlah_mhs": 72, "sks": 2, "random_seed": 19},
            {"kode": "IF3110_K02", "jumlah_mhs": 70, "sks": 2, "random_seed": 32},
            {"kode": "IF3110_K03", "jumlah_mhs": 68, "sks": 2, "random_seed": 33},
            
            {"kode": "IF3140_K01", "jumlah_mhs": 58, "sks": 3, "random_seed": 46},
            {"kode": "IF3140_K02", "jumlah_mhs": 56, "sks": 3, "random_seed": 27},
            {"kode": "IF3140_K03", "jumlah_mhs": 54, "sks": 3, "random_seed": 28},
            
            {"kode": "IF3150_K01", "jumlah_mhs": 52, "sks": 3, "random_seed": 60},
            {"kode": "IF3150_K02", "jumlah_mhs": 49, "sks": 3, "random_seed": 61},
            {"kode": "IF3150_K03", "jumlah_mhs": 51, "sks": 3, "random_seed": 62},
            
            {"kode": "IF3170_K01", "jumlah_mhs": 55, "sks": 2, "random_seed": 70},
            {"kode": "IF3170_K02", "jumlah_mhs": 53, "sks": 2, "random_seed": 71},
            {"kode": "IF3170_K03", "jumlah_mhs": 54, "sks": 2, "random_seed": 72},
        ],
        "ruangan": [
            {"kode": "7601", "kuota": 50},
            {"kode": "7602", "kuota": 50},
            {"kode": "7603", "kuota": 45},
            {"kode": "7606", "kuota": 80},
            {"kode": "7609", "kuota": 60},
            {"kode": "7610", "kuota": 75},
            {"kode": "multimedia", "kuota": 40},
            {"kode": "labtek_v", "kuota": 55},
            {"kode": "auditorium", "kuota": 100},
        ],
        "mahasiswa": [
            # Mahasiswa dengan 4 MK
            {"nim": "13520001", "daftar_mk": ["IF3071_K01", "IF3130_K01", "IF3110_K01", "IF3150_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520002", "daftar_mk": ["IF3071_K01", "IF3140_K01", "IF3170_K01", "IF3110_K02"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520003", "daftar_mk": ["IF3071_K02", "IF3130_K02", "IF3110_K01", "IF3150_K02"], "prioritas": [1, 3, 2, 4]},
            {"nim": "13520004", "daftar_mk": ["IF3071_K02", "IF3140_K02", "IF3170_K02", "IF3110_K03"], "prioritas": [1, 2, 4, 3]},
            {"nim": "13520005", "daftar_mk": ["IF3071_K03", "IF3130_K03", "IF3110_K02", "IF3150_K03"], "prioritas": [2, 1, 3, 4]},
            {"nim": "13520006", "daftar_mk": ["IF3071_K03", "IF3140_K03", "IF3170_K03", "IF3110_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520007", "daftar_mk": ["IF3110_K01", "IF3130_K01", "IF3150_K01", "IF3170_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520008", "daftar_mk": ["IF3110_K02", "IF3140_K01", "IF3071_K01", "IF3150_K02"], "prioritas": [1, 3, 2, 4]},
            {"nim": "13520009", "daftar_mk": ["IF3110_K03", "IF3130_K02", "IF3170_K02", "IF3071_K02"], "prioritas": [2, 1, 3, 4]},
            {"nim": "13520010", "daftar_mk": ["IF3140_K01", "IF3150_K01", "IF3130_K01", "IF3170_K01"], "prioritas": [1, 2, 3, 4]},
            
            {"nim": "13520011", "daftar_mk": ["IF3140_K02", "IF3110_K01", "IF3071_K01", "IF3130_K02"], "prioritas": [1, 2, 4, 3]},
            {"nim": "13520012", "daftar_mk": ["IF3140_K03", "IF3150_K03", "IF3170_K03", "IF3110_K02"], "prioritas": [2, 1, 3, 4]},
            {"nim": "13520013", "daftar_mk": ["IF3150_K01", "IF3130_K01", "IF3110_K01", "IF3071_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520014", "daftar_mk": ["IF3150_K02", "IF3140_K02", "IF3170_K02", "IF3110_K03"], "prioritas": [1, 3, 2, 4]},
            {"nim": "13520015", "daftar_mk": ["IF3150_K03", "IF3071_K03", "IF3130_K03", "IF3140_K03"], "prioritas": [2, 1, 3, 4]},
            {"nim": "13520016", "daftar_mk": ["IF3170_K01", "IF3110_K02", "IF3071_K02", "IF3150_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520017", "daftar_mk": ["IF3170_K02", "IF3140_K01", "IF3130_K02", "IF3110_K01"], "prioritas": [1, 3, 2, 4]},
            {"nim": "13520018", "daftar_mk": ["IF3170_K03", "IF3150_K02", "IF3071_K03", "IF3140_K02"], "prioritas": [2, 1, 4, 3]},
            {"nim": "13520019", "daftar_mk": ["IF3071_K01", "IF3110_K03", "IF3130_K01", "IF3140_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520020", "daftar_mk": ["IF3071_K02", "IF3150_K03", "IF3170_K01", "IF3110_K02"], "prioritas": [1, 2, 4, 3]},
            
            # Mahasiswa dengan 3 MK
            {"nim": "13520021", "daftar_mk": ["IF3071_K01", "IF3130_K01", "IF3110_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520022", "daftar_mk": ["IF3071_K01", "IF3140_K01", "IF3150_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520023", "daftar_mk": ["IF3071_K02", "IF3170_K02", "IF3110_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520024", "daftar_mk": ["IF3071_K02", "IF3130_K02", "IF3140_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520025", "daftar_mk": ["IF3071_K03", "IF3150_K03", "IF3110_K03"], "prioritas": [1, 3, 2]},
            {"nim": "13520026", "daftar_mk": ["IF3071_K03", "IF3170_K03", "IF3130_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520027", "daftar_mk": ["IF3110_K01", "IF3140_K01", "IF3150_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520028", "daftar_mk": ["IF3110_K01", "IF3130_K02", "IF3170_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520029", "daftar_mk": ["IF3110_K02", "IF3071_K01", "IF3140_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520030", "daftar_mk": ["IF3110_K02", "IF3150_K02", "IF3130_K01"], "prioritas": [1, 2, 3]},
            
            {"nim": "13520031", "daftar_mk": ["IF3110_K03", "IF3170_K03", "IF3071_K03"], "prioritas": [1, 3, 2]},
            {"nim": "13520032", "daftar_mk": ["IF3110_K03", "IF3140_K03", "IF3150_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520033", "daftar_mk": ["IF3130_K01", "IF3140_K01", "IF3150_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520034", "daftar_mk": ["IF3130_K01", "IF3170_K01", "IF3071_K02"], "prioritas": [1, 3, 2]},
            {"nim": "13520035", "daftar_mk": ["IF3130_K02", "IF3110_K01", "IF3140_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520036", "daftar_mk": ["IF3130_K02", "IF3150_K02", "IF3170_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520037", "daftar_mk": ["IF3130_K03", "IF3071_K01", "IF3140_K03"], "prioritas": [1, 3, 2]},
            {"nim": "13520038", "daftar_mk": ["IF3130_K03", "IF3110_K02", "IF3150_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520039", "daftar_mk": ["IF3140_K01", "IF3150_K01", "IF3170_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520040", "daftar_mk": ["IF3140_K01", "IF3071_K03", "IF3110_K03"], "prioritas": [1, 3, 2]},
            
            {"nim": "13520041", "daftar_mk": ["IF3140_K02", "IF3130_K03", "IF3150_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520042", "daftar_mk": ["IF3140_K02", "IF3170_K02", "IF3071_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520043", "daftar_mk": ["IF3140_K03", "IF3110_K01", "IF3130_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520044", "daftar_mk": ["IF3140_K03", "IF3150_K03", "IF3170_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520045", "daftar_mk": ["IF3150_K01", "IF3170_K01", "IF3071_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520046", "daftar_mk": ["IF3150_K01", "IF3110_K02", "IF3130_K02"], "prioritas": [1, 3, 2]},
            {"nim": "13520047", "daftar_mk": ["IF3150_K02", "IF3140_K01", "IF3071_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520048", "daftar_mk": ["IF3150_K02", "IF3170_K03", "IF3110_K03"], "prioritas": [1, 2, 3]},
            {"nim": "13520049", "daftar_mk": ["IF3150_K03", "IF3130_K03", "IF3140_K02"], "prioritas": [1, 3, 2]},
            {"nim": "13520050", "daftar_mk": ["IF3150_K03", "IF3071_K02", "IF3170_K02"], "prioritas": [2, 1, 3]},
            
            # Mahasiswa dengan 2 MK
            {"nim": "13520051", "daftar_mk": ["IF3071_K01", "IF3110_K01"], "prioritas": [1, 2]},
            {"nim": "13520052", "daftar_mk": ["IF3071_K01", "IF3130_K01"], "prioritas": [2, 1]},
            {"nim": "13520053", "daftar_mk": ["IF3071_K02", "IF3140_K02"], "prioritas": [1, 2]},
            {"nim": "13520054", "daftar_mk": ["IF3071_K02", "IF3150_K02"], "prioritas": [2, 1]},
            {"nim": "13520055", "daftar_mk": ["IF3071_K03", "IF3170_K03"], "prioritas": [1, 2]},
            {"nim": "13520056", "daftar_mk": ["IF3071_K03", "IF3110_K03"], "prioritas": [2, 1]},
            {"nim": "13520057", "daftar_mk": ["IF3110_K01", "IF3130_K01"], "prioritas": [1, 2]},
            {"nim": "13520058", "daftar_mk": ["IF3110_K01", "IF3140_K01"], "prioritas": [2, 1]},
            {"nim": "13520059", "daftar_mk": ["IF3110_K02", "IF3150_K01"], "prioritas": [1, 2]},
            {"nim": "13520060", "daftar_mk": ["IF3110_K02", "IF3170_K02"], "prioritas": [2, 1]},
            
            {"nim": "13520061", "daftar_mk": ["IF3110_K03", "IF3130_K02"], "prioritas": [1, 2]},
            {"nim": "13520062", "daftar_mk": ["IF3110_K03", "IF3140_K03"], "prioritas": [2, 1]},
            {"nim": "13520063", "daftar_mk": ["IF3130_K01", "IF3150_K03"], "prioritas": [1, 2]},
            {"nim": "13520064", "daftar_mk": ["IF3130_K02", "IF3170_K01"], "prioritas": [2, 1]},
            {"nim": "13520065", "daftar_mk": ["IF3130_K03", "IF3140_K01"], "prioritas": [1, 2]},
            {"nim": "13520066", "daftar_mk": ["IF3140_K01", "IF3150_K02"], "prioritas": [2, 1]},
            {"nim": "13520067", "daftar_mk": ["IF3140_K02", "IF3170_K03"], "prioritas": [1, 2]},
            {"nim": "13520068", "daftar_mk": ["IF3140_K03", "IF3071_K01"], "prioritas": [2, 1]},
            {"nim": "13520069", "daftar_mk": ["IF3150_K01", "IF3130_K03"], "prioritas": [1, 2]},
            {"nim": "13520070", "daftar_mk": ["IF3150_K02", "IF3110_K01"], "prioritas": [2, 1]},
            
            {"nim": "13520071", "daftar_mk": ["IF3150_K03", "IF3170_K01"], "prioritas": [1, 2]},
            {"nim": "13520072", "daftar_mk": ["IF3170_K01", "IF3071_K02"], "prioritas": [2, 1]},
            {"nim": "13520073", "daftar_mk": ["IF3170_K02", "IF3130_K01"], "prioritas": [1, 2]},
            {"nim": "13520074", "daftar_mk": ["IF3170_K03", "IF3140_K02"], "prioritas": [2, 1]},
            {"nim": "13520075", "daftar_mk": ["IF3071_K01", "IF3150_K01"], "prioritas": [1, 2]},
            {"nim": "13520076", "daftar_mk": ["IF3071_K02", "IF3170_K01"], "prioritas": [2, 1]},
            {"nim": "13520077", "daftar_mk": ["IF3071_K03", "IF3130_K02"], "prioritas": [1, 2]},
            {"nim": "13520078", "daftar_mk": ["IF3110_K01", "IF3150_K02"], "prioritas": [2, 1]},
            {"nim": "13520079", "daftar_mk": ["IF3110_K02", "IF3140_K01"], "prioritas": [1, 2]},
            {"nim": "13520080", "daftar_mk": ["IF3110_K03", "IF3170_K02"], "prioritas": [2, 1]},
        ]
    }
)

hill_climbing_medium_sample = HC_SA(
    input = {
        "kelas_mata_kuliah": [
            # Semester 5
            {"kode": "IF3071_K01", "jumlah_mhs": 60, "sks": 4, "random_seed": 46},
            {"kode": "IF3071_K02", "jumlah_mhs": 55, "sks": 4, "random_seed": 47},
            {"kode": "IF3130_K01", "jumlah_mhs": 45, "sks": 2, "random_seed": 50},
            {"kode": "IF3130_K02", "jumlah_mhs": 40, "sks": 2, "random_seed": 51},
            {"kode": "IF3110_K01", "jumlah_mhs": 70, "sks": 2, "random_seed": 19},
            {"kode": "IF3110_K02", "jumlah_mhs": 70, "sks": 2, "random_seed": 32},
            {"kode": "IF3110_K03", "jumlah_mhs": 65, "sks": 2, "random_seed": 33},
            {"kode": "IF3140_K01", "jumlah_mhs": 55, "sks": 3, "random_seed": 46},
            {"kode": "IF3140_K02", "jumlah_mhs": 55, "sks": 3, "random_seed": 27},
            {"kode": "IF3140_K03", "jumlah_mhs": 50, "sks": 3, "random_seed": 28},
            
            # Additional courses
            {"kode": "IF3150_K01", "jumlah_mhs": 48, "sks": 3, "random_seed": 60},
            {"kode": "IF3150_K02", "jumlah_mhs": 45, "sks": 3, "random_seed": 61},
            {"kode": "IF3170_K01", "jumlah_mhs": 52, "sks": 2, "random_seed": 70},
            {"kode": "IF3170_K02", "jumlah_mhs": 50, "sks": 2, "random_seed": 71},
            {"kode": "IF3210_K01", "jumlah_mhs": 58, "sks": 4, "random_seed": 80},
            {"kode": "IF3210_K02", "jumlah_mhs": 55, "sks": 4, "random_seed": 81},
            {"kode": "IF3230_K01", "jumlah_mhs": 43, "sks": 2, "random_seed": 90},
            {"kode": "IF3250_K01", "jumlah_mhs": 60, "sks": 3, "random_seed": 100},
            {"kode": "IF3260_K01", "jumlah_mhs": 38, "sks": 2, "random_seed": 110},
            {"kode": "IF3270_K01", "jumlah_mhs": 42, "sks": 3, "random_seed": 120},
        ],
        "ruangan": [
            {"kode": "7609", "kuota": 60},
            {"kode": "7606", "kuota": 80},
            {"kode": "7602", "kuota": 50},
            {"kode": "7603", "kuota": 45},
            {"kode": "7610", "kuota": 70},
            {"kode": "multimedia", "kuota": 40},
            {"kode": "labtek_v", "kuota": 55},
            {"kode": "auditorium", "kuota": 100},
        ],
        "mahasiswa": [
            # Students taking IF3071
            {"nim": "13520001", "daftar_mk": ["IF3071_K01", "IF3130_K01", "IF3110_K02", "IF3150_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520002", "daftar_mk": ["IF3071_K01", "IF3140_K01", "IF3170_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520003", "daftar_mk": ["IF3130_K01", "IF3110_K02", "IF3071_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520004", "daftar_mk": ["IF3071_K01", "IF3130_K01", "IF3140_K01", "IF3210_K01"], "prioritas": [3, 1, 2, 4]},
            {"nim": "13520005", "daftar_mk": ["IF3071_K02", "IF3110_K01", "IF3150_K02"], "prioritas": [1, 2, 3]},
            
            # Students taking IF3110
            {"nim": "13520006", "daftar_mk": ["IF3110_K01", "IF3140_K02", "IF3170_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520007", "daftar_mk": ["IF3110_K03", "IF3130_K02", "IF3250_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520008", "daftar_mk": ["IF3110_K02", "IF3071_K01", "IF3230_K01"], "prioritas": [2, 1, 3]},
            {"nim": "13520009", "daftar_mk": ["IF3110_K01", "IF3210_K02", "IF3150_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520010", "daftar_mk": ["IF3110_K02", "IF3140_K03", "IF3260_K01"], "prioritas": [1, 2, 3]},
            
            # Students taking IF3140
            {"nim": "13520011", "daftar_mk": ["IF3140_K01", "IF3130_K01", "IF3210_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520012", "daftar_mk": ["IF3140_K02", "IF3110_K03", "IF3170_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520013", "daftar_mk": ["IF3140_K03", "IF3071_K02", "IF3250_K01"], "prioritas": [2, 1, 3]},
            {"nim": "13520014", "daftar_mk": ["IF3140_K01", "IF3210_K02", "IF3270_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520015", "daftar_mk": ["IF3140_K02", "IF3130_K02", "IF3150_K02"], "prioritas": [1, 3, 2]},
            
            # Students taking IF3130
            {"nim": "13520016", "daftar_mk": ["IF3130_K01", "IF3110_K01", "IF3071_K01"], "prioritas": [2, 1, 3]},
            {"nim": "13520017", "daftar_mk": ["IF3130_K02", "IF3140_K03", "IF3210_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520018", "daftar_mk": ["IF3130_K01", "IF3170_K02", "IF3260_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520019", "daftar_mk": ["IF3130_K02", "IF3110_K02", "IF3250_K01"], "prioritas": [3, 1, 2]},
            {"nim": "13520020", "daftar_mk": ["IF3130_K01", "IF3071_K02", "IF3230_K01"], "prioritas": [1, 2, 3]},
            
            # Students with diverse schedules
            {"nim": "13520021", "daftar_mk": ["IF3210_K01", "IF3150_K01", "IF3110_K03"], "prioritas": [1, 2, 3]},
            {"nim": "13520022", "daftar_mk": ["IF3210_K02", "IF3140_K01", "IF3170_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520023", "daftar_mk": ["IF3150_K02", "IF3071_K01", "IF3130_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520024", "daftar_mk": ["IF3170_K01", "IF3110_K01", "IF3250_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520025", "daftar_mk": ["IF3170_K02", "IF3140_K02", "IF3260_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520026", "daftar_mk": ["IF3250_K01", "IF3210_K01", "IF3071_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520027", "daftar_mk": ["IF3260_K01", "IF3130_K01", "IF3110_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520028", "daftar_mk": ["IF3270_K01", "IF3140_K03", "IF3150_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520029", "daftar_mk": ["IF3230_K01", "IF3071_K01", "IF3210_K02"], "prioritas": [3, 1, 2]},
            {"nim": "13520030", "daftar_mk": ["IF3210_K01", "IF3110_K03", "IF3170_K02"], "prioritas": [1, 2, 3]},
            
            # Additional students with 2-3 courses
            {"nim": "13520031", "daftar_mk": ["IF3071_K02", "IF3140_K01"], "prioritas": [1, 2]},
            {"nim": "13520032", "daftar_mk": ["IF3110_K01", "IF3130_K02"], "prioritas": [1, 2]},
            {"nim": "13520033", "daftar_mk": ["IF3150_K01", "IF3210_K02", "IF3250_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520034", "daftar_mk": ["IF3170_K02", "IF3260_K01"], "prioritas": [1, 2]},
            {"nim": "13520035", "daftar_mk": ["IF3140_K02", "IF3071_K01", "IF3110_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520036", "daftar_mk": ["IF3210_K01", "IF3130_K01"], "prioritas": [1, 2]},
            {"nim": "13520037", "daftar_mk": ["IF3250_K01", "IF3170_K01", "IF3071_K02"], "prioritas": [1, 3, 2]},
            {"nim": "13520038", "daftar_mk": ["IF3110_K03", "IF3270_K01"], "prioritas": [1, 2]},
            {"nim": "13520039", "daftar_mk": ["IF3140_K03", "IF3150_K02", "IF3230_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520040", "daftar_mk": ["IF3071_K01", "IF3210_K02"], "prioritas": [1, 2]},
        ]
    }
)

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
                "random_seed": 46
            },
            {
                "kode": "IF3110_K01",
                "jumlah_mhs": 70,
                "sks": 2,
                "random_seed": 19
            },
            {
                "kode": "IF3140_K02",
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

genetic = GeneticAlgorithm(
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
                "random_seed": 46
            },
            {
                "kode": "IF3110_K01",
                "jumlah_mhs": 70,
                "sks": 2,
                "random_seed": 19
            },
            {
                "kode": "IF3140_K02",
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

genetic_large_sample = GeneticAlgorithm(
    input = {
        "kelas_mata_kuliah": [
            # 6 Mata Kuliah Wajib Semester 5 - Max 3 sections each
            {"kode": "IF3071_K01", "jumlah_mhs": 65, "sks": 4, "random_seed": 46},
            {"kode": "IF3071_K02", "jumlah_mhs": 60, "sks": 4, "random_seed": 47},
            {"kode": "IF3071_K03", "jumlah_mhs": 58, "sks": 4, "random_seed": 48},
            
            {"kode": "IF3130_K01", "jumlah_mhs": 48, "sks": 2, "random_seed": 50},
            {"kode": "IF3130_K02", "jumlah_mhs": 45, "sks": 2, "random_seed": 51},
            {"kode": "IF3130_K03", "jumlah_mhs": 50, "sks": 2, "random_seed": 52},
            
            {"kode": "IF3110_K01", "jumlah_mhs": 72, "sks": 2, "random_seed": 19},
            {"kode": "IF3110_K02", "jumlah_mhs": 70, "sks": 2, "random_seed": 32},
            {"kode": "IF3110_K03", "jumlah_mhs": 68, "sks": 2, "random_seed": 33},
            
            {"kode": "IF3140_K01", "jumlah_mhs": 58, "sks": 3, "random_seed": 46},
            {"kode": "IF3140_K02", "jumlah_mhs": 56, "sks": 3, "random_seed": 27},
            {"kode": "IF3140_K03", "jumlah_mhs": 54, "sks": 3, "random_seed": 28},
            
            {"kode": "IF3150_K01", "jumlah_mhs": 52, "sks": 3, "random_seed": 60},
            {"kode": "IF3150_K02", "jumlah_mhs": 49, "sks": 3, "random_seed": 61},
            {"kode": "IF3150_K03", "jumlah_mhs": 51, "sks": 3, "random_seed": 62},
            
            {"kode": "IF3170_K01", "jumlah_mhs": 55, "sks": 2, "random_seed": 70},
            {"kode": "IF3170_K02", "jumlah_mhs": 53, "sks": 2, "random_seed": 71},
            {"kode": "IF3170_K03", "jumlah_mhs": 54, "sks": 2, "random_seed": 72},
        ],
        "ruangan": [
            {"kode": "7601", "kuota": 50},
            {"kode": "7602", "kuota": 50},
            {"kode": "7603", "kuota": 45},
            {"kode": "7606", "kuota": 80},
            {"kode": "7609", "kuota": 60},
            {"kode": "7610", "kuota": 75},
            {"kode": "multimedia", "kuota": 40},
            {"kode": "labtek_v", "kuota": 55},
            {"kode": "auditorium", "kuota": 100},
        ],
        "mahasiswa": [
            # Mahasiswa dengan 4 MK
            {"nim": "13520001", "daftar_mk": ["IF3071_K01", "IF3130_K01", "IF3110_K01", "IF3150_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520002", "daftar_mk": ["IF3071_K01", "IF3140_K01", "IF3170_K01", "IF3110_K02"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520003", "daftar_mk": ["IF3071_K02", "IF3130_K02", "IF3110_K01", "IF3150_K02"], "prioritas": [1, 3, 2, 4]},
            {"nim": "13520004", "daftar_mk": ["IF3071_K02", "IF3140_K02", "IF3170_K02", "IF3110_K03"], "prioritas": [1, 2, 4, 3]},
            {"nim": "13520005", "daftar_mk": ["IF3071_K03", "IF3130_K03", "IF3110_K02", "IF3150_K03"], "prioritas": [2, 1, 3, 4]},
            {"nim": "13520006", "daftar_mk": ["IF3071_K03", "IF3140_K03", "IF3170_K03", "IF3110_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520007", "daftar_mk": ["IF3110_K01", "IF3130_K01", "IF3150_K01", "IF3170_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520008", "daftar_mk": ["IF3110_K02", "IF3140_K01", "IF3071_K01", "IF3150_K02"], "prioritas": [1, 3, 2, 4]},
            {"nim": "13520009", "daftar_mk": ["IF3110_K03", "IF3130_K02", "IF3170_K02", "IF3071_K02"], "prioritas": [2, 1, 3, 4]},
            {"nim": "13520010", "daftar_mk": ["IF3140_K01", "IF3150_K01", "IF3130_K01", "IF3170_K01"], "prioritas": [1, 2, 3, 4]},
            
            {"nim": "13520011", "daftar_mk": ["IF3140_K02", "IF3110_K01", "IF3071_K01", "IF3130_K02"], "prioritas": [1, 2, 4, 3]},
            {"nim": "13520012", "daftar_mk": ["IF3140_K03", "IF3150_K03", "IF3170_K03", "IF3110_K02"], "prioritas": [2, 1, 3, 4]},
            {"nim": "13520013", "daftar_mk": ["IF3150_K01", "IF3130_K01", "IF3110_K01", "IF3071_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520014", "daftar_mk": ["IF3150_K02", "IF3140_K02", "IF3170_K02", "IF3110_K03"], "prioritas": [1, 3, 2, 4]},
            {"nim": "13520015", "daftar_mk": ["IF3150_K03", "IF3071_K03", "IF3130_K03", "IF3140_K03"], "prioritas": [2, 1, 3, 4]},
            {"nim": "13520016", "daftar_mk": ["IF3170_K01", "IF3110_K02", "IF3071_K02", "IF3150_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520017", "daftar_mk": ["IF3170_K02", "IF3140_K01", "IF3130_K02", "IF3110_K01"], "prioritas": [1, 3, 2, 4]},
            {"nim": "13520018", "daftar_mk": ["IF3170_K03", "IF3150_K02", "IF3071_K03", "IF3140_K02"], "prioritas": [2, 1, 4, 3]},
            {"nim": "13520019", "daftar_mk": ["IF3071_K01", "IF3110_K03", "IF3130_K01", "IF3140_K01"], "prioritas": [1, 2, 3, 4]},
            {"nim": "13520020", "daftar_mk": ["IF3071_K02", "IF3150_K03", "IF3170_K01", "IF3110_K02"], "prioritas": [1, 2, 4, 3]},
            
            # Mahasiswa dengan 3 MK
            {"nim": "13520021", "daftar_mk": ["IF3071_K01", "IF3130_K01", "IF3110_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520022", "daftar_mk": ["IF3071_K01", "IF3140_K01", "IF3150_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520023", "daftar_mk": ["IF3071_K02", "IF3170_K02", "IF3110_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520024", "daftar_mk": ["IF3071_K02", "IF3130_K02", "IF3140_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520025", "daftar_mk": ["IF3071_K03", "IF3150_K03", "IF3110_K03"], "prioritas": [1, 3, 2]},
            {"nim": "13520026", "daftar_mk": ["IF3071_K03", "IF3170_K03", "IF3130_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520027", "daftar_mk": ["IF3110_K01", "IF3140_K01", "IF3150_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520028", "daftar_mk": ["IF3110_K01", "IF3130_K02", "IF3170_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520029", "daftar_mk": ["IF3110_K02", "IF3071_K01", "IF3140_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520030", "daftar_mk": ["IF3110_K02", "IF3150_K02", "IF3130_K01"], "prioritas": [1, 2, 3]},
            
            {"nim": "13520031", "daftar_mk": ["IF3110_K03", "IF3170_K03", "IF3071_K03"], "prioritas": [1, 3, 2]},
            {"nim": "13520032", "daftar_mk": ["IF3110_K03", "IF3140_K03", "IF3150_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520033", "daftar_mk": ["IF3130_K01", "IF3140_K01", "IF3150_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520034", "daftar_mk": ["IF3130_K01", "IF3170_K01", "IF3071_K02"], "prioritas": [1, 3, 2]},
            {"nim": "13520035", "daftar_mk": ["IF3130_K02", "IF3110_K01", "IF3140_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520036", "daftar_mk": ["IF3130_K02", "IF3150_K02", "IF3170_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520037", "daftar_mk": ["IF3130_K03", "IF3071_K01", "IF3140_K03"], "prioritas": [1, 3, 2]},
            {"nim": "13520038", "daftar_mk": ["IF3130_K03", "IF3110_K02", "IF3150_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520039", "daftar_mk": ["IF3140_K01", "IF3150_K01", "IF3170_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520040", "daftar_mk": ["IF3140_K01", "IF3071_K03", "IF3110_K03"], "prioritas": [1, 3, 2]},
            
            {"nim": "13520041", "daftar_mk": ["IF3140_K02", "IF3130_K03", "IF3150_K02"], "prioritas": [2, 1, 3]},
            {"nim": "13520042", "daftar_mk": ["IF3140_K02", "IF3170_K02", "IF3071_K02"], "prioritas": [1, 2, 3]},
            {"nim": "13520043", "daftar_mk": ["IF3140_K03", "IF3110_K01", "IF3130_K01"], "prioritas": [1, 3, 2]},
            {"nim": "13520044", "daftar_mk": ["IF3140_K03", "IF3150_K03", "IF3170_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520045", "daftar_mk": ["IF3150_K01", "IF3170_K01", "IF3071_K01"], "prioritas": [1, 2, 3]},
            {"nim": "13520046", "daftar_mk": ["IF3150_K01", "IF3110_K02", "IF3130_K02"], "prioritas": [1, 3, 2]},
            {"nim": "13520047", "daftar_mk": ["IF3150_K02", "IF3140_K01", "IF3071_K03"], "prioritas": [2, 1, 3]},
            {"nim": "13520048", "daftar_mk": ["IF3150_K02", "IF3170_K03", "IF3110_K03"], "prioritas": [1, 2, 3]},
            {"nim": "13520049", "daftar_mk": ["IF3150_K03", "IF3130_K03", "IF3140_K02"], "prioritas": [1, 3, 2]},
            {"nim": "13520050", "daftar_mk": ["IF3150_K03", "IF3071_K02", "IF3170_K02"], "prioritas": [2, 1, 3]},
            
            # Mahasiswa dengan 2 MK
            {"nim": "13520051", "daftar_mk": ["IF3071_K01", "IF3110_K01"], "prioritas": [1, 2]},
            {"nim": "13520052", "daftar_mk": ["IF3071_K01", "IF3130_K01"], "prioritas": [2, 1]},
            {"nim": "13520053", "daftar_mk": ["IF3071_K02", "IF3140_K02"], "prioritas": [1, 2]},
            {"nim": "13520054", "daftar_mk": ["IF3071_K02", "IF3150_K02"], "prioritas": [2, 1]},
            {"nim": "13520055", "daftar_mk": ["IF3071_K03", "IF3170_K03"], "prioritas": [1, 2]},
            {"nim": "13520056", "daftar_mk": ["IF3071_K03", "IF3110_K03"], "prioritas": [2, 1]},
            {"nim": "13520057", "daftar_mk": ["IF3110_K01", "IF3130_K01"], "prioritas": [1, 2]},
            {"nim": "13520058", "daftar_mk": ["IF3110_K01", "IF3140_K01"], "prioritas": [2, 1]},
            {"nim": "13520059", "daftar_mk": ["IF3110_K02", "IF3150_K01"], "prioritas": [1, 2]},
            {"nim": "13520060", "daftar_mk": ["IF3110_K02", "IF3170_K02"], "prioritas": [2, 1]},
            
            {"nim": "13520061", "daftar_mk": ["IF3110_K03", "IF3130_K02"], "prioritas": [1, 2]},
            {"nim": "13520062", "daftar_mk": ["IF3110_K03", "IF3140_K03"], "prioritas": [2, 1]},
            {"nim": "13520063", "daftar_mk": ["IF3130_K01", "IF3150_K03"], "prioritas": [1, 2]},
            {"nim": "13520064", "daftar_mk": ["IF3130_K02", "IF3170_K01"], "prioritas": [2, 1]},
            {"nim": "13520065", "daftar_mk": ["IF3130_K03", "IF3140_K01"], "prioritas": [1, 2]},
            {"nim": "13520066", "daftar_mk": ["IF3140_K01", "IF3150_K02"], "prioritas": [2, 1]},
            {"nim": "13520067", "daftar_mk": ["IF3140_K02", "IF3170_K03"], "prioritas": [1, 2]},
            {"nim": "13520068", "daftar_mk": ["IF3140_K03", "IF3071_K01"], "prioritas": [2, 1]},
            {"nim": "13520069", "daftar_mk": ["IF3150_K01", "IF3130_K03"], "prioritas": [1, 2]},
            {"nim": "13520070", "daftar_mk": ["IF3150_K02", "IF3110_K01"], "prioritas": [2, 1]},
            
            {"nim": "13520071", "daftar_mk": ["IF3150_K03", "IF3170_K01"], "prioritas": [1, 2]},
            {"nim": "13520072", "daftar_mk": ["IF3170_K01", "IF3071_K02"], "prioritas": [2, 1]},
            {"nim": "13520073", "daftar_mk": ["IF3170_K02", "IF3130_K01"], "prioritas": [1, 2]},
            {"nim": "13520074", "daftar_mk": ["IF3170_K03", "IF3140_K02"], "prioritas": [2, 1]},
            {"nim": "13520075", "daftar_mk": ["IF3071_K01", "IF3150_K01"], "prioritas": [1, 2]},
            {"nim": "13520076", "daftar_mk": ["IF3071_K02", "IF3170_K01"], "prioritas": [2, 1]},
            {"nim": "13520077", "daftar_mk": ["IF3071_K03", "IF3130_K02"], "prioritas": [1, 2]},
            {"nim": "13520078", "daftar_mk": ["IF3110_K01", "IF3150_K02"], "prioritas": [2, 1]},
            {"nim": "13520079", "daftar_mk": ["IF3110_K02", "IF3140_K01"], "prioritas": [1, 2]},
            {"nim": "13520080", "daftar_mk": ["IF3110_K03", "IF3170_K02"], "prioritas": [2, 1]},
        ]
    },
    population_size=10
)

# genetic.show_population()
genetic_large_sample.run(verbose=True, n_generasi=2000)
genetic_large_sample.fungsi_objektif(verbose=True, state=genetic_large_sample.population[0])
print([genetic_large_sample.fitness(genetic_large_sample.population[i]) for i in range(len(genetic_large_sample.population))])
# print(len(genetic.select_parents()))

# hill_climbing.show_state()
# hill_climbing_large_sample.run(verbose=True)
# hill_climbing_large_sample.fungsi_objektif(verbose=True)
# hill_climbing_large_sample.show_state()