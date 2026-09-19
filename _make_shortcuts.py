import os

ROOT = r"c:\ai-engineer"
SC_DIR = os.path.join(ROOT, "shortcuts_klik_otomatis")
os.makedirs(SC_DIR, exist_ok=True)

VENV_ACTIVATE = r"call venv_bnsp\Scripts\activate.bat"
PYTHON = "python"
CD = "cd /d c:\ai-engineer"

MODUL = [
    ("MODUL 01 - FUNDAMENTAL AI", "modul_01_fundamental_ai", [
        "01_konsep_dasar_ai.py",
        "02_ai_lifecycle_etika.py",
        "03_responsible_ai_bias_fairness.py"
    ]),
    ("MODUL 02 - PYTHON AI", "modul_02_python_ai", [
        "01_numpy_fundamental.py",
        "02_pandas_dataframe.py",
        "03_visualisasi_matplotlib_seaborn.py",
        "04_function_oop_exception.py"
    ]),
    ("MODUL 03 - DATA PREPARATION", "modul_03_data_prep", [
        "01_data_understanding_cleaning.py",
        "02_transformation_encoding_scaling.py",
        "03_eda_splitting.py"
    ]),
    ("MODUL 04 - MACHINE LEARNING", "modul_04_machine_learning", [
        "01_klasifikasi_logreg_svm_dt_rf.py",
        "02_regresi_linreg_ridge_lasso_gbm.py",
        "03_clustering_kmeans_dbscan_hierarchical.py"
    ]),
    ("MODUL 05 - EVALUASI & TUNING", "modul_05_ml_evaluation_tuning", [
        "01_metrics_evaluation_class_imbalance.py",
        "02_cross_validation_tuning_grid_random_search.py"
    ]),
    ("MODUL 06 - DEEP LEARNING", "modul_06_deep_learning", [
        "01_ann_mlp_perceptron_backprop.py",
        "02_cnn_classification_mnist.py"
    ]),
    ("MODUL 07 - COMPUTER VISION", "modul_07_computer_vision", [
        "01_image_processing_classification.py"
    ]),
    ("MODUL 08 - NLP", "modul_08_nlp", [
        "01_text_preprocessing_tfidf_sentiment.py"
    ]),
    ("MODUL 09 - GENERATIVE AI", "modul_09_generative_ai", [
        "01_generative_ai_llm_prompt_engineering_rag.py"
    ]),
    ("MODUL 10 - DEPLOYMENT", "modul_10_deployment", [
        "01_model_serialization_fastapi_docker_mlops.py"
    ]),
    ("MODUL 11 - PROYEK E2E", "modul_11_proyek_end_to_end", [
        "01_proyek_e2e_harga_rumah_portfolio.py"
    ]),
    ("MODUL 12 - PERSIAPAN BNSP", "modul_12_persiapan_bnsp", [
        "01_simulasi_asesmen_checklist_soal_bnsp.py"
    ])
]

bat_template = """@echo off
REM ============================================================
REM SHORTCUT AUTO RUN: {nama_file}
REM DI-GENERATE OTOMATIS — TINGGAL DOUBLE KLIK .BAT INI!
REM ============================================================
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
title {title}
echo.
echo ======================================================================
echo  🚀 MENJALANKAN SCRIPT: {script_path}
echo ======================================================================
echo.

REM Step 1: Masuk ke folder project
{cd_cmd}

REM Step 2: Aktivasi virtual environment venv_bnsp
echo [1/3] Aktivasi virtual environment venv_bnsp...
{venv_cmd}
if errorlevel 1 (
    echo ❌ GAGAL AKTIVASI VENV! Cek folder venv_bnsp ada di c:\ai-engineer\
    echo.
    pause
    exit /b 1
)

REM Step 3: Verifikasi python interpreter
echo [2/3] Verifikasi interpreter:
where python | findstr /i "venv_bnsp" >nul
if errorlevel 1 (
    echo ⚠️  WARNING: Python BUKAN dari venv_bnsp! Lanjutkan anyway...
    where python
) else (
    echo ✅ Python venv_bnsp OK:
    where python
)
python --version
echo.

REM Step 4: Jalankan script!
echo [3/3] Menjalankan script (jika exit code 0 = BERHASIL):
echo    python "{script_path}"
echo.
{python_cmd} "{script_path}"
set EXITCODE=%ERRORLEVEL%

echo.
echo ======================================================================
if %EXITCODE% EQU 0 (
    echo ✅ SELESAI! Exit Code = 0 (BERHASIL)
    echo    Output charts / file tersimpan di folder modul masing-masing.
) else (
    echo ❌ TERJADI ERROR! Exit Code = %EXITCODE%
    echo    Scroll ke atas untuk melihat error message.
    echo.
    echo    💡 Tips untuk memperbaiki:
    echo    1. Install dependensi: python -m pip install -r requirements.txt
    echo    2. Jika Jupyter error, HINDARI tombol Run Interactive di IDE
    echo    3. Gunakan Python interpreter dari venv_bnsp\Scripts\python.exe
)
echo ======================================================================
echo.
pause
"""

count = 0
for label, folder, files in MODUL:
    for fname in files:
        script_path = f"{folder}\\{fname}"
        safe_label = label.replace("MODUL ", "M").replace(" - ", "__").replace(" ", "_")
        num = f"{count+1:02d}"
        bat_name = f"{num}_{safe_label}__{fname.replace('.py', '.bat')}"
        bat_content = bat_template.format(
            nama_file=bat_name,
            title=f"{label} | {fname}",
            cd_cmd=CD,
            venv_cmd=VENV_ACTIVATE,
            python_cmd=PYTHON,
            script_path=script_path
        )
        with open(os.path.join(SC_DIR, bat_name), "w", encoding="utf-8", errors="replace") as f:
            f.write(bat_content)
        count += 1
        print(f"✅ [{count:02d}] {bat_name:<80} -> {script_path}")

# ---- FASTAPI SERVER SHORTCUTS ----
count += 1
fast_bat = bat_template.format(
    nama_file=f"{count:02d}_M10_DEPLOYMENT__RUN_FASTAPI_CHURN_8000.bat",
    title="M10 | FastAPI Churn Prediction Server :8000",
    cd_cmd="cd /d c:\\ai-engineer\\modul_10_deployment",
    venv_cmd=r"call ..\venv_bnsp\Scripts\activate.bat",
    python_cmd="python -m uvicorn",
    script_path="fastapi_churn_app_TEMPLATE:app --host 0.0.0.0 --port 8000 --reload"
)
# Adjust: Jangan tambah .bat extension di folder path
with open(os.path.join(SC_DIR, f"{count:02d}_M10_DEPLOYMENT__RUN_FASTAPI_CHURN_SERVER_8000.bat"), "w", encoding="utf-8", errors="replace") as f:
    f.write(fast_bat)
print(f"✅ [{count:02d}] M10_DEPLOYMENT__RUN_FASTAPI_CHURN_SERVER_8000.bat")

count += 1
fast_bat2 = bat_template.format(
    nama_file=f"{count:02d}_M11_PROYEK_E2E__RUN_FASTAPI_HOUSE_8100.bat",
    title="M11 | FastAPI House Prediction Server :8100",
    cd_cmd="cd /d c:\\ai-engineer\\modul_11_proyek_end_to_end",
    venv_cmd=r"call ..\venv_bnsp\Scripts\activate.bat",
    python_cmd="python -m uvicorn",
    script_path="app_house_prediction_TEMPLATE:app --host 0.0.0.0 --port 8100 --reload"
)
with open(os.path.join(SC_DIR, f"{count:02d}_M11_PROYEK_E2E__RUN_FASTAPI_HOUSE_PRICE_8100.bat"), "w", encoding="utf-8", errors="replace") as f:
    f.write(fast_bat2)
print(f"✅ [{count:02d}] M11_PROYEK_E2E__RUN_FASTAPI_HOUSE_PRICE_8100.bat")

count += 1
cmd_bat = """@echo off
chcp 65001 >nul
title CMD Terminal (venv_bnsp AKTIF)
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
cd /d c:\ai-engineer
call venv_bnsp\Scripts\activate.bat
echo.
echo ======================================================================
echo  ✅ Terminal siap pakai! venv_bnsp SUDAH AKTIF (ada prefix (venv_bnsp))
echo ======================================================================
echo.
echo  🚀 Perintah Cepat (copy paste + ENTER):
echo     python modul_02_python_ai\\01_numpy_fundamental.py
echo     python modul_03_data_prep\\01_data_understanding_cleaning.py
echo     python modul_10_deployment\\01_model_serialization_fastapi_docker_mlops.py
echo.
echo  📖 Tips:
echo     • deactivate = keluar dari venv_bnsp
echo     • cls = bersihkan layar
echo     • exit = tutup terminal
echo.
cmd /k
"""
with open(os.path.join(SC_DIR, f"{count:02d}_OPEN_CMD_TERMINAL_AKTIF_venv_bnsp.bat"), "w", encoding="utf-8", errors="replace") as f:
    f.write(cmd_bat)
print(f"✅ [{count:02d}] OPEN_CMD_TERMINAL_AKTIF_venv_bnsp.bat")

print("\n" + "="*80)
print(f"🎉 TOTAL {count} SHORTCUT DIBUAT di FOLDER: {SC_DIR}")
print("="*80)
print("""
CARA PAKAI:
1. BUKA FILE EXPLORER WINDOWS (WIN+E)
2. MASUK KE FOLDER:  c:\\ai-engineer\\shortcuts_klik_otomatis\\
3. DOUBLE KLIK FILE .bat YANG ANDA INGINKAN:
   • Contoh:  05_M02__PYTHON_AI__03_visualisasi_matplotlib_seaborn.bat
   • Contoh:  09_M03__DATA_PREPARATION__01_data_understanding_cleaning.bat
   • Contoh:  25_M10_DEPLOYMENT__RUN_FASTAPI_CHURN_SERVER_8000.bat
   • Contoh:  27_OPEN_CMD_TERMINAL_AKTIF_venv_bnsp.bat  (buka terminal siap pakai)
4. ✅ Terminal CMD terbuka OTOMATIS -> Aktivasi venv -> Jalankan script -> PAUSE

TIDAK USAH KETIK APA-APA, TINGGAL KLIK DUA KALI! 🖱️
""")
