# Kasir Sederhana

Program kasir sederhana berbasis terminal, dibuat dengan Python untuk
Tugas 8 mata kuliah Rekayasa Perangkat Lunak (Coding Standard dan
Version Control).

## Fitur

- Melihat daftar produk beserta harga dan stok
- Menambahkan produk ke keranjang (dengan pengecekan stok)
- Melihat isi keranjang dan total belanja
- Diskon 10% otomatis jika total belanja lebih dari Rp 500.000
- Pembayaran, perhitungan kembalian, dan struk belanja

## Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan:

```
python main.py
```

## Menjalankan Unit Test

```
python -m unittest -v
```

## Struktur Proyek

- `produk.py`: class `Produk` dan data produk awal
- `kasir.py`: logika keranjang, diskon, dan kembalian
- `main.py`: menu dan tampilan di terminal
- `test_kasir.py`: unit test untuk logika di `kasir.py`

## Coding Standard yang Dipakai

Standar yang dipakai adalah PEP 8 (Python):

- Nama class memakai `PascalCase`, contoh `Produk`, `Keranjang`
- Nama fungsi dan variabel memakai `snake_case`, contoh `hitung_diskon`
- Konstanta memakai `UPPER_CASE`, contoh `BATAS_DISKON`
- Indentasi 4 spasi dan panjang baris maksimal 79 karakter
- Setiap fungsi hanya punya satu tanggung jawab
- Logika (`kasir.py`) dipisah dari tampilan (`main.py`)
- Tidak ada angka ajaib (magic number); nilai ditulis sebagai konstanta
- Komentar menjelaskan alasan ("mengapa"), bukan sekadar isi kode
