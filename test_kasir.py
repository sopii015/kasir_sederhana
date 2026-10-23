"""Unit test untuk logika kasir (kasir.py)."""

import unittest

from kasir import Keranjang, hitung_diskon, hitung_kembalian
from produk import Produk


class TestHitungDiskon(unittest.TestCase):
    """Pengujian aturan diskon."""

    def test_tanpa_diskon_jika_total_di_bawah_batas(self):
        self.assertEqual(hitung_diskon(100000), 0)

    def test_tanpa_diskon_jika_total_tepat_di_batas(self):
        self.assertEqual(hitung_diskon(500000), 0)

    def test_diskon_10_persen_jika_total_melebihi_batas(self):
        self.assertEqual(hitung_diskon(600000), 60000)


class TestKeranjang(unittest.TestCase):
    """Pengujian keranjang belanja."""

    def setUp(self):
        self.beras = Produk("P001", "Beras 5 kg", 65000, 20)
        self.keranjang = Keranjang()

    def test_keranjang_baru_kosong(self):
        self.assertTrue(self.keranjang.kosong())

    def test_hitung_total_beberapa_produk(self):
        mie = Produk("P005", "Mie Instan", 3500, 100)
        self.keranjang.tambah_produk(self.beras, 2)
        self.keranjang.tambah_produk(mie, 10)
        self.assertEqual(self.keranjang.hitung_total(), 130000 + 35000)

    def test_produk_sama_ditambah_dua_kali_jumlahnya_digabung(self):
        self.keranjang.tambah_produk(self.beras, 1)
        self.keranjang.tambah_produk(self.beras, 2)
        self.assertEqual(self.keranjang.hitung_total(), 65000 * 3)

    def test_tolak_jumlah_nol(self):
        with self.assertRaises(ValueError):
            self.keranjang.tambah_produk(self.beras, 0)

    def test_tolak_jumlah_melebihi_stok(self):
        with self.assertRaises(ValueError):
            self.keranjang.tambah_produk(self.beras, 21)

    def test_kurangi_stok_setelah_pembelian(self):
        self.keranjang.tambah_produk(self.beras, 5)
        self.keranjang.kurangi_stok()
        self.assertEqual(self.beras.stok, 15)


class TestHitungKembalian(unittest.TestCase):
    """Pengujian perhitungan kembalian."""

    def test_kembalian_benar(self):
        self.assertEqual(hitung_kembalian(80000, 100000), 20000)

    def test_uang_pas_kembalian_nol(self):
        self.assertEqual(hitung_kembalian(80000, 80000), 0)

    def test_uang_kurang_menimbulkan_error(self):
        with self.assertRaises(ValueError):
            hitung_kembalian(80000, 50000)


if __name__ == "__main__":
    unittest.main()
