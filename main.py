"""Program kasir sederhana berbasis menu di terminal."""

from kasir import Keranjang, hitung_diskon, hitung_kembalian
from produk import buat_daftar_produk

LEBAR_GARIS = 44


def format_rupiah(angka):
    """Ubah angka menjadi teks rupiah, contoh: 1500000 -> Rp 1.500.000."""
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


def minta_angka(pesan):
    """Minta angka bulat dari pengguna. Kembalikan None jika tidak valid."""
    teks = input(pesan).strip()
    if not teks.isdigit():
        return None
    return int(teks)


def tampilkan_menu():
    """Tampilkan pilihan menu utama."""
    print("=" * LEBAR_GARIS)
    print("KASIR SEDERHANA")
    print("=" * LEBAR_GARIS)
    print("1. Lihat daftar produk")
    print("2. Tambah produk ke keranjang")
    print("3. Lihat keranjang")
    print("4. Bayar")
    print("0. Keluar")


def tampilkan_produk(daftar_produk):
    """Tampilkan semua produk beserta harga dan stoknya."""
    print(f"{'Kode':<6}{'Nama':<20}{'Harga':>12}{'Stok':>6}")
    for produk in daftar_produk.values():
        harga = format_rupiah(produk.harga)
        print(f"{produk.kode:<6}{produk.nama:<20}{harga:>12}{produk.stok:>6}")


def tampilkan_keranjang(keranjang):
    """Tampilkan isi keranjang dan total belanja."""
    if keranjang.kosong():
        print("Keranjang masih kosong.")
        return

    for produk, jumlah in keranjang.item.values():
        subtotal = format_rupiah(produk.harga * jumlah)
        print(f"{produk.nama:<20}{jumlah:>4} x {subtotal:>14}")
    print("-" * LEBAR_GARIS)
    print(f"{'Total':<24}{format_rupiah(keranjang.hitung_total()):>20}")


def proses_tambah(daftar_produk, keranjang):
    """Minta kode dan jumlah produk, lalu masukkan ke keranjang."""
    kode = input("Kode produk: ").strip().upper()
    produk = daftar_produk.get(kode)
    if produk is None:
        print("Kode produk tidak ditemukan.")
        return

    jumlah = minta_angka("Jumlah: ")
    if jumlah is None:
        print("Jumlah harus berupa angka bulat.")
        return

    try:
        keranjang.tambah_produk(produk, jumlah)
    except ValueError as pesan_error:
        print(f"Gagal: {pesan_error}")
    else:
        print(f"{produk.nama} x{jumlah} ditambahkan ke keranjang.")


def tampilkan_struk(keranjang, total, diskon, uang, kembalian):
    """Cetak struk belanja setelah pembayaran berhasil."""
    print("=" * LEBAR_GARIS)
    print("STRUK BELANJA")
    print("=" * LEBAR_GARIS)
    tampilkan_keranjang(keranjang)
    print(f"{'Diskon':<24}{format_rupiah(diskon):>20}")
    print(f"{'Total bayar':<24}{format_rupiah(total - diskon):>20}")
    print(f"{'Uang diterima':<24}{format_rupiah(uang):>20}")
    print(f"{'Kembalian':<24}{format_rupiah(kembalian):>20}")
    print("Terima kasih sudah berbelanja.")


def proses_bayar(keranjang):
    """Proses pembayaran. Kembalikan True jika pembayaran berhasil."""
    if keranjang.kosong():
        print("Keranjang masih kosong.")
        return False

    total = keranjang.hitung_total()
    diskon = hitung_diskon(total)
    total_bayar = total - diskon
    print(f"Total belanja : {format_rupiah(total)}")
    print(f"Diskon        : {format_rupiah(diskon)}")
    print(f"Total bayar   : {format_rupiah(total_bayar)}")

    uang = minta_angka("Uang diterima: ")
    if uang is None:
        print("Uang harus berupa angka bulat.")
        return False

    try:
        kembalian = hitung_kembalian(total_bayar, uang)
    except ValueError as pesan_error:
        print(f"Gagal: {pesan_error}")
        return False

    keranjang.kurangi_stok()
    tampilkan_struk(keranjang, total, diskon, uang, kembalian)
    return True


def main():
    """Jalankan program kasir sampai pengguna memilih keluar."""
    daftar_produk = buat_daftar_produk()
    keranjang = Keranjang()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_produk(daftar_produk)
        elif pilihan == "2":
            proses_tambah(daftar_produk, keranjang)
        elif pilihan == "3":
            tampilkan_keranjang(keranjang)
        elif pilihan == "4":
            if proses_bayar(keranjang):
                # Keranjang baru untuk pelanggan berikutnya.
                keranjang = Keranjang()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Menu tidak dikenali.")


if __name__ == "__main__":
    main()
