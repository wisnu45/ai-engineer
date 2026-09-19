import pandas as pd
import numpy as np

# --- Membuat DataFrame ---
# Data seringkali dimulai dari dictionary atau file eksternal (CSV/Excel)
data_karyawan = {
    "Nama": ["Andi", "Budi", "Citra", "Dewi", "Eko"],
    "Departemen": ["IT", "Marketing", "IT", "Finance", "IT"],
    "Kota": ["Jakarta", "Bandung", "Surabaya", "Jakarta", "Bandung"],
    "Gaji": [8500000, 12000000, 7000000, 15000000, 9500000],
    "Rating_Kinerja": [4.2, 3.8, 4.5, 4.0, 4.3]
}
df = pd.DataFrame(data_karyawan)

# --- Inspeksi Data Awal ---
print("Info Struktur Data:")
df.info() # Sangat penting untuk cek tipe data dan missing value

# --- Filtering Kompleks ---
# Mencari karyawan IT dengan gaji di atas 9 juta
kondisi_it_senior = (df["Departemen"] == "IT") & (df["Gaji"] > 9000000)
print("\nKaryawan IT Senior (>9jt):")
print(df[kondisi_it_senior])

# --- GroupBy & Aggregation (Pivot Table ala Python) ---
# "Berapa rata-rata gaji di setiap departemen?"
rata_gaji_dept = df.groupby("Departemen")["Gaji"].mean().astype(int)
print("\nRata-rata gaji per Departemen:")
print(rata_gaji_dept)

# --- Feature Engineering Sederhana dengan apply() ---
# Membuat fitur baru berdasarkan data yang sudah ada
def kategori_gaji(gaji):
    return "High" if gaji >= 12000000 else "Medium" if gaji >= 8000000 else "Low"

df["Kategori_Gaji"] = df["Gaji"].apply(kategori_gaji)
print("\nData dengan fitur baru 'Kategori_Gaji':")
print(df[["Nama", "Gaji", "Kategori_Gaji"]].head(3))