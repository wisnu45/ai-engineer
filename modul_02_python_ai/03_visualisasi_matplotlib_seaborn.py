import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Setup gaya visual
sns.set_style("whitegrid")

# Simulasi Data Ujian untuk contoh
data_survey = pd.DataFrame({
    "Jam_Belajar": np.random.normal(5, 2, 200).clip(0.5, 12),
    "Nilai_Ujian": np.random.normal(70, 15, 200).clip(30, 100)
})
# Menambahkan korelasi buatan
data_survey["Nilai_Ujian"] = (data_survey["Jam_Belajar"] * 4 + data_survey["Nilai_Ujian"] * 0.5).clip(30, 100)


# --- 1. Histogram & KDE (Melihat Distribusi Data) ---
# Penting untuk tahu apakah data kita 'miring' (skewed) atau normal.
plt.figure(figsize=(8, 4))
sns.histplot(data=data_survey, x="Nilai_Ujian", kde=True, color="#0891b2")
plt.title("Distribusi Nilai Ujian", fontweight="bold")
plt.show()

# --- 2. Scatter Plot & Regresi (Melihat Hubungan/Korelasi) ---
# Apakah jam belajar mempengaruhi nilai ujian?
plt.figure(figsize=(8, 4))
sns.regplot(data=data_survey, x="Jam_Belajar", y="Nilai_Ujian", color="#dc2626", scatter_kws={'alpha':0.5})
plt.title("Korelasi Jam Belajar vs Nilai Ujian", fontweight="bold")
plt.show()

# --- 3. Heatmap Korelasi (Cek Multikolinearitas) ---
# Sangat penting saat memilih fitur untuk model Machine Learning.
plt.figure(figsize=(6, 5))
sns.heatmap(data_survey.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Heatmap Korelasi", fontweight="bold")
plt.show()