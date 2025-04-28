# DATMIN_POST_TEST

# 📊 FastAPI Random Forest Prediction API

API ini dibuat menggunakan **FastAPI** untuk melakukan prediksi berdasarkan model **Random Forest** yang sudah dilatih. Data input akan dinormalisasi menggunakan scaler, lalu diprediksi targetnya.

---

## 🚀 Fitur

- Endpoint `/predict` untuk prediksi.
- Scaling input otomatis menggunakan `scaler (1).pkl`.
- Model prediksi: `best_random_forest_model.pkl`.
- Validasi input menggunakan **Pydantic**.
- Dokumentasi API otomatis di Swagger UI dan ReDoc.

---

## 📥 Input JSON Format

Format input yang diterima:

```json
{
  "Mengulang": 1200.0,
  "Putus_Sekolah": 800.0,
  "Rasio_Siswa_per_Guru": 20.5,
  "Rasio_Siswa_per_Sekolah": 350.0,
  "Persentase_Guru_belum_S1": 0.02,
  "Persentase_Ruang_Rusak": 0.17,
  "Total_Tenaga_Kependidikan": 8000.0,
  "Persentase_Ruang_Baik": 0.82,
  "Rasio_Rombel_per_Sekolah": 12.5,
  "Provinsi_encoded": 6.0
}

## 🛠️ Cara Menjalankan Project

Berikut langkah-langkah untuk menjalankan project ini secara lokal:

1. **Clone repository:**

   Clone repositori GitHub ke komputer lokal kamu:
   ```bash
   git clone https://github.com/username/your-repo-name.git
   cd your-repo-name

2. **Install dependencies:**

   Install semua library yang diperlukan menggunakan `requirement.txt`:
   ```bash
   pip install -r requirement.txt

3. **Pastikan file model dan scaler tersedia:**

   Pastikan file berikut tersedia di direktori project (satu folder dengan `app.py`):
   - `best_random_forest_model.pkl` → file model Random Forest yang sudah dilatih.
   - `scaler (1).pkl` → file scaler untuk preprocessing input data.

   > **Catatan:** Nama file harus sama persis agar aplikasi bisa menemukan dan memuat file dengan benar.

4. **Jalankan server FastAPI:**

   Gunakan perintah berikut untuk menjalankan server API:
   ```bash
   uvicorn app:app --reload

5. **Akses API melalui browser:**

   Setelah server FastAPI berjalan, kamu bisa mengakses dokumentasi API melalui browser di alamat berikut:

   - **Swagger UI** (dokumentasi interaktif):
     [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

   - **ReDoc** (dokumentasi terstruktur):
     [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

