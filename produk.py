"""Data produk untuk program kasir sederhana."""


class Produk:
    """Satu produk yang dijual di toko."""

    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok


def buat_daftar_produk():
    """Buat daftar produk awal dalam bentuk dictionary {kode: Produk}."""
    daftar = [
        Produk("P001", "Beras 5 kg", 65000, 20),
        Produk("P002", "Minyak Goreng 2 L", 38000, 15),
        Produk("P003", "Gula Pasir 1 kg", 17000, 30),
        Produk("P004", "Kopi Bubuk 200 g", 22000, 25),
        Produk("P005", "Mie Instan", 3500, 100),
    ]
    # Dictionary dipakai agar produk bisa dicari cepat lewat kodenya.
    return {produk.kode: produk for produk in daftar}
