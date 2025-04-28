# fastapi_app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np

# Load scaler dan model Random Forest
scaler = joblib.load("scaler (1).pkl")  # pastikan ini scaler untuk Random Forest kamu
model = joblib.load("best_random_forest_model.pkl")  # model Random Forest terbaik kamu

# FastAPI instance
app = FastAPI()

# Definisikan struktur inputan
class InputData(BaseModel):
    Mengulang: float = Field(..., example=1200.0)
    Putus_Sekolah: float = Field(..., example=800.0)
    Rasio_Siswa_per_Guru: float = Field(..., example=20.5)
    Rasio_Siswa_per_Sekolah: float = Field(..., example=350.0)
    Persentase_Guru_belum_S1: float = Field(..., example=0.02)
    Persentase_Ruang_Rusak: float = Field(..., example=0.17)
    Total_Tenaga_Kependidikan: float = Field(..., example=8000.0)
    Persentase_Ruang_Baik: float = Field(..., example=0.82)
    Rasio_Rombel_per_Sekolah: float = Field(..., example=12.5)
    Provinsi_encoded: float = Field(..., example=6.0)  # tetap didefinisikan tapi tidak dipakai di scaler

@app.post("/predict")
def predict_target(data: InputData):
    try:
        # Masukkan input ke dalam array
        input_features = np.array([[ 
            data.Mengulang,
            data.Putus_Sekolah,
            data.Rasio_Siswa_per_Guru,
            data.Rasio_Siswa_per_Sekolah,
            data.Persentase_Guru_belum_S1,
            data.Persentase_Ruang_Rusak,
            data.Total_Tenaga_Kependidikan,
            data.Persentase_Ruang_Baik,
            data.Rasio_Rombel_per_Sekolah
        ]])
        # ⚡ Notice: Provinsi_encoded tidak masuk scaling!

        # Normalisasi input
        scaled_features = scaler.transform(input_features)

        # Prediksi
        prediction = model.predict(scaled_features)

        return {
            "predicted_target": int(prediction[0])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
