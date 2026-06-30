# Perbaikan Celah Keamanan (Backend)

- Matikan `debug=True` pada `app.run` (sudah dilakukan).
- Tambahkan validasi tipe file untuk `/api/process` (sudah dilakukan).
- Tambahkan limit `MAX_CONTENT_LENGTH` (5 MB) (sudah dilakukan).

## Artefak Perbaikan
- `app.py` telah diperbarui dengan validasi input dan konfigurasi produksi.
