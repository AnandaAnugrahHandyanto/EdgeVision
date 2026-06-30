# Laporan Audit Keamanan - EdgeVision

## Ringkasan Eksekutif
Audit keamanan aplikasi EdgeVision dilakukan untuk mengidentifikasi celah keamanan. Aplikasi saat ini beroperasi dalam mode debug aktif dan memiliki beberapa risiko potensial terkait penanganan file dan input pengguna.

## Temuan
### 1. Mode Debug Aktif
Aplikasi dijalankan dengan `debug=True` dalam `app.py`. Hal ini memungkinkan eksekusi kode arbitrer melalui debugger interaktif (Werkzeug) jika diekspos secara publik.

### 2. Validasi File yang Tidak Memadai
Aplikasi menggunakan `Image.open(file.stream)` dari input `request.files['file']` tanpa memvalidasi tipe file (MIME type) atau melakukan sanitasi file yang diunggah. Hal ini berpotensi menyebabkan serangan *Remote Code Execution* (RCE) melalui file yang dibuat khusus (misal: gambar yang dimanipulasi).

### 3. Tidak Ada Pembatasan Ukuran File
Tidak ada batasan ukuran file yang diunggah, yang dapat menyebabkan serangan *Denial of Service* (DoS) melalui pengunggahan file berukuran sangat besar.

### 4. Penanganan Error yang Terlalu Informatif
Blok `try-except` di `process_image` mengembalikan `str(e)` kepada pengguna dalam respons JSON. Ini dapat membocorkan informasi sistem atau path internal kepada penyerang.

## Rekomendasi
- Nonaktifkan mode debug di produksi.
- Implementasikan validasi file (ekstensi dan MIME type).
- Gunakan pustaka pengolah gambar yang aman dan lakukan sanitasi input.
- Batasi ukuran file unggahan menggunakan `MAX_CONTENT_LENGTH`.
- Gunakan pesan error umum dan log kesalahan di sisi server.
