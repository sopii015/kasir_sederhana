"""Logika perhitungan kasir. Modul ini tidak berisi kode tampilan."""

BATAS_DISKON = 500000
PERSEN_DISKON = 0.1


class Keranjang:
    """Keranjang belanja berisi produk beserta jumlahnya."""

    def __init__(self):
        # Bentuk isi: {kode_produk: (objek_produk, jumlah)}
        self.item = {}

    def tambah_produk(self, produk, jumlah):
        """Tambahkan produk ke keranjang.

        Jumlah harus lebih dari 0 dan total di keranjang tidak boleh
        melebihi stok produk.
        """
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")

        jumlah_sekarang = self.item.get(produk.kode, (produk, 0))[1]
        jumlah_baru = jumlah_sekarang + jumlah
        if jumlah_baru > produk.stok:
            raise ValueError("Stok tidak cukup.")

        self.item[produk.kode] = (produk, jumlah_baru)

    def hitung_total(self):
        """Hitung total harga semua produk di keranjang."""
        total = 0
        for produk, jumlah in self.item.values():
            total += produk.harga * jumlah
        return total

    def kosong(self):
        """Kembalikan True jika keranjang belum berisi produk."""
        return len(self.item) == 0

    def kurangi_stok(self):
        """Kurangi stok setiap produk sesuai jumlah yang dibeli."""
        for produk, jumlah in self.item.values():
            produk.stok -= jumlah


def hitung_diskon(total):
    """Hitung diskon berdasarkan total belanja."""
    # Diskon hanya untuk belanja besar supaya toko tetap untung
    # pada transaksi kecil.
    if total > BATAS_DISKON:
        return round(total * PERSEN_DISKON)
    return 0


def hitung_kembalian(total_bayar, uang_diterima):
    """Hitung uang kembalian. Error jika uang yang diterima kurang."""
    if uang_diterima < total_bayar:
        raise ValueError("Uang yang diterima kurang.")
    return uang_diterima - total_bayar
