# Museum of the Year 3000

Label museum fiktif dari tahun 3000 untuk artefak masa kini: sebuah
QR Code dari sekitar tahun 2023.

## Teks entry

> QR Code, c. 2023. Sacred maze, printed on tables. Humans pointed
> their glowing slabs at it and waited, faithfully, for food to appear.

Satu baris, 134 karakter — persis seperti yang ditulis program ke
`entry.txt`.

## Cara menjalankan

```sh
python3 main.py
```

Program membaca direktori keluaran dari variabel lingkungan
`MAKEFUN_OUTPUT_DIR` dan menulis satu berkas di sana:

- `entry.txt` — teks label di atas, satu baris.

Kalau direktori keluaran tidak bisa ditulis, program tetap selesai
dengan tenang (exit 0) tanpa crash.

## Kebutuhan

- Python 3.13, standard library saja. Tanpa dependensi, tanpa jaringan.
