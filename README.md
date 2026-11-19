# Garis demi Garis

Aplikasi belajar menggambar langkah demi langkah untuk anak SD dan SMP. Garis biru mencontohkan tiap goresan, lalu anak menelusurinya dengan jari (mode **Layar**) atau menirunya di kertas sungguhan (mode **Kertas**).

## Cara pakai

Buka `index.html` di browser, di HP atau komputer. Tidak perlu instalasi atau internet; semuanya ada dalam satu file.

## Fitur

- **2 jenjang, 12 kategori, 144 gambar.** Tiap kategori berisi 12 gambar.
- **SD:** garis sederhana, 4–6 langkah per gambar.
- **SMP:** garis bantu (dihapus otomatis di akhir), garis utama, arsiran gelap-terang, dan perspektif. 5–8 langkah per gambar.
- **Bintang 1–3** sesuai ketepatan garis. Di mode Kertas, anak menilai sendiri.
- **Warnai** hasil gambar dengan krayon, dan **putar ulang** goresan dari awal.
- Konfeti, suara (bisa dimatikan), dan pujian kecil tiap langkah selesai.
- Bintang dan gambar terakhir tersimpan di browser perangkat itu.

## Daftar gambar

### SD

- **Binatang**: Ikan, Katak, Beruang, Kucing, Kelinci, Anak Ayam, Bebek, Siput, Lebah, Kura-kura, Paus, Kupu-kupu
- **Kue & Jajan**: Donat, Kukis, Lolipop, Permen, Es Loli, Es Krim, Cupcake, Puding, Potongan Kue, Kue Ulang Tahun, Kue Lapis, Roti Tawar
- **Tanaman**: Daun, Tulip, Cemara, Wortel, Tunas di Pot, Pohon, Bunga, Bunga Matahari, Kaktus, Pohon Kelapa, Jamur, Apel
- **Kendaraan**: Perahu Layar, Mobil, Bus, Truk, Kereta, Kapal Selam, Roket, Balon Udara, Pesawat, Sepeda, Helikopter, Kapal Laut
- **Benda**: Bola, Balon, Layang-layang, Kado, Mahkota, Payung, Rumah, Cangkir, Jam Weker, Robot, Pensil, Buku
- **Princess**: Tiara, Wajah Putri, Gaun Putri, Istana, Tongkat Ajaib, Sepatu Putri, Kereta Labu, Unicorn, Pangeran Kodok, Cermin Ajaib, Kalung Hati, Angsa

### SMP

- **Bentuk 3D**: Bola, Telur, Kubus, Balok, Tabung, Kerucut, Limas, Prisma, Tumpukan Kubus, Kotak Terbuka, Tabung Rebah, Gabungan Bentuk
- **Buah & Sayur**: Apel, Pir, Jeruk, Pisang, Ceri, Stroberi, Anggur, Semangka, Wortel, Terong, Jamur, Tomat
- **Alam Benda**: Gelas, Mangkuk, Cangkir, Botol, Vas, Teko, Kaleng, Lilin, Bohlam, Pensil, Buku, Jam Pasir
- **Hewan**: Burung Hantu, Burung Pipit, Penguin, Ikan Koi, Kucing Duduk, Kelinci Duduk, Tikus, Kura-kura, Siput, Kupu-kupu, Gajah, Kepala Anjing
- **Pemandangan**: Jalan Lurus, Rel Kereta, Lorong, Rumah Perspektif, Gedung Kota, Gunung & Danau, Pantai Senja, Pohon Rindang, Mercusuar, Jembatan Batu, Tenda Kemah, Kincir Angin
- **Princess**: Tiara, Wajah Putri, Putri Berdiri, Gaun di Manekin, Istana, Menara Putri, Kereta Kencana, Unicorn, Sepatu Kaca, Cermin Antik, Mawar, Kotak Perhiasan

## Struktur

| File | Isi |
|---|---|
| `index.html` | Aplikasi jadi, satu file mandiri. |
| `src/data.js` | Semua gambar: koordinat garis, langkah, dan instruksinya (ruang 320 × 320). |
| `src/shell.html` | Tampilan dan logika aplikasi, dengan penanda `/*DATA*/`. |
| `build.py` | Menggabungkan `src/` menjadi `index.html`. |

## Menambah atau mengubah gambar

1. Sunting `src/data.js`. Tiap gambar dibuat dengan `L(id, nama, ...langkah)`.
   - SD: tiap langkah berupa `['Instruksi.', garis1, garis2, ...]`.
   - SMP: `K(...)` untuk garis bantu, `G(...)` untuk garis utama, `S(...)` untuk area arsiran.
2. Jalankan `python3 build.py`.
3. Buka `index.html` untuk mencoba.

Semua gambar adalah desain asli, tidak meniru karakter atau merek tertentu.
