# Project Random Forest - Kelayakan Penerima Beasiswa

**Nama:** Bayu Muhammad Ramadhan  
**NIM:** 301240008  
**Kelas:** 5A

## Isi project
- `data/dataset_beasiswa.csv`: 14 data contoh untuk klasifikasi.
- `train_model.py`: melatih 3 decision tree dengan Random Forest.
- `model_random_forest.json`: representasi pohon hasil pelatihan.
- `web/index.html`: antarmuka simulasi.
- `web/model.json`: model yang dibaca oleh halaman web.
- `Laporan_Project_dan_Tutorial.docx`: laporan dan tutorial.

## Menjalankan web secara lokal
Pastikan Python 3 terpasang. Dari folder utama project:

```bash
python -m http.server 8000
```

Buka `http://localhost:8000/web/` di browser. Jangan membuka `index.html` langsung melalui `file://`, karena browser dapat memblokir pemuatan `model.json`.

## Melatih ulang model (opsional)
```bash
pip install -r requirements.txt
python train_model.py
```

## Deploy gratis dengan GitHub Pages
1. Buat repository GitHub baru, misalnya `random-forest-beasiswa`.
2. Upload seluruh isi folder project ini ke branch `main`.
3. Buka **Settings > Pages** pada repository.
4. Pada **Build and deployment**, pilih **Deploy from a branch**.
5. Pilih branch `main` dan folder `/web`, lalu klik **Save**.
6. Tunggu proses selesai. URL web akan berbentuk `https://USERNAME.github.io/NAMA-REPOSITORY/`.
7. Uji URL tersebut dan pastikan halaman simulasi serta hasil voting tampil.

## Catatan
Dataset adalah data simulasi untuk kebutuhan pembelajaran, bukan data penerima beasiswa nyata. Akurasi yang dicantumkan di laporan adalah akurasi pada data latih, bukan jaminan performa pada data baru. Ganti tautan GitHub, deployment, dan YouTube pada laporan setelah masing-masing benar-benar dibuat.
