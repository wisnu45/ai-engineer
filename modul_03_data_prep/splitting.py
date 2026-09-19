import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# --- Simulasi Dataset Churn Nasabah ---
np.random.seed(42)
n = 1000
# Fitur
X_data = pd.DataFrame({
    "Umur": np.random.randint(20, 60, n),
    "Skor_Kredit": np.random.normal(650, 100, n),
    "Saldo": np.random.exponential(5000000, n)
})
# Target: Churn (1=Pindah, 0=Tetap). Kita buat agak tidak seimbang (imbalanced)
# Peluang churn lebih tinggi jika saldo rendah dan umur muda
peluang = (1 / (X_data["Saldo"] + 1e-9)) * 1e6 + (1 / X_data["Umur"]) * 10
y_target = (np.random.rand(n) < peluang.clip(0.1, 0.8)).astype(int)

print(f"Total Data: {len(X_data)}")
print(f"Distribusi Target Churn Awal:\n{y_target.value_counts(normalize=True)}")

# --- EDA Sederhana (Visualisasi Korelasi) ---
# Menggabungkan sementara untuk melihat korelasi
df_eda = X_data.copy()
df_eda['Churn'] = y_target
plt.figure(figsize=(6, 4))
sns.heatmap(df_eda.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Korelasi Fitur dengan Target Churn")
plt.tight_layout()
plt.show() # Di notebook akan muncul plot


# --- DATA SPLITTING STRATEGY (Sangat Penting!) ---

# Langkah 1: Pisahkan Test Set (Kunci di lemari, jangan disentuh!)
# PENTING: Gunakan 'stratify=y' agar rasio Churn di data Test sama dengan data asli.
X_trainval, X_test, y_trainval, y_test = train_test_split(
    X_data, y_target, test_size=0.15, random_state=42, stratify=y_target
)

# Langkah 2: Pisahkan Train dan Validation dari sisa data
# Kita ambil ~15% dari total awal untuk validasi (0.15 / 0.85 ≈ 0.176)
X_train, X_val, y_train, y_val = train_test_split(
    X_trainval, y_trainval, test_size=0.1765, random_state=42, stratify=y_trainval
)

print("\n--- Hasil Splitting (Perhatikan proporsi stratify terjaga) ---")
print(f"Train Set : {len(y_train)} baris | Churn Rate: {y_train.mean():.3f}")
print(f"Val Set   : {len(y_val)} baris | Churn Rate: {y_val.mean():.3f}")
print(f"Test Set  : {len(y_test)} baris | Churn Rate: {y_test.mean():.3f}")