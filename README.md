# Tugas Besar IF3170 Inteligensi Artifisial
> Implementasi Scheduler Mata Kuliah Menggunakan Local Search

## Daftar Isi

- [Deskripsi Umum](#deskripsi-umum)
- [Setup dan Instalasi](#setup-dan-instalasi)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Kontributor dan Pembagian Tugasnya](#kontributor-serta-pembagian-tugasnya)

## Deskripsi Umum

Local Search adalah metode optimasi yang mencari solusi terbaik dengan memperbaiki solusi awal secara bertahap melalui perubahan kecil. Metode ini efektif untuk masalah penjadwalan (scheduling), di mana tujuan utamanya adalah meminimalkan konflik antar mata kuliah, ruangan, dan dosen.

Algoritma Hill Climbing bekerja dengan selalu memilih solusi tetangga yang lebih baik, sehingga cepat mencapai hasil optimal lokal, namun mudah terjebak di local optimum. Simulated Annealing mengatasi hal ini dengan sesekali menerima solusi yang lebih buruk pada awal proses agar dapat keluar dari jebakan lokal dan mencari solusi yang lebih global. Sementara itu, Genetic Algorithm menggunakan konsep evolusi seperti seleksi, crossover, dan mutasi untuk menghasilkan populasi solusi baru dan mengeksplorasi ruang solusi lebih luas.

Dalam konteks penjadwalan, Hill Climbing cocok untuk perbaikan cepat, Simulated Annealing membantu mencari solusi lebih global, dan Genetic Algorithm unggul dalam menghasilkan jadwal yang lebih optimal secara keseluruhan.

## Dependencies

- reportlab
- matplotlib

Instalasi dengan menggunakan `pip`
```bash
pip install matplotlib reportlab
```

## Setup dan Instalasi

Clone Repository ini dengan menjalankan perintah berikut pada terminal Anda

```bash
  git clone https://github.com/SyarafiAkmal/Local-Search-Course-Scheduler_Tubes1_AI_Nyaka.git
```

## Cara Menjalankan Program

- Buka folder di code editor
- Masuk ke direktori src
- Jalankan:
```bash
  python Main.py
```

## Kontributor serta Pembagian Tugasnya

| NIM      | Nama                    | Tugas                                           |
|----------|-------------------------|-------------------------------------------------|
| 10122057 | Farrell Jabaar Altafataza | Hill Climbing, laporan |
| 13122003 | Raudah Yahya Kuddah | Simulated Annealing, laporan |
| 13522076 | Muhammad Syarafi Akmal  | Base code parent algoritma, Genetic Algorithm, Utilities |


