@echo off
REM ============================================================
REM SHORTCUT AUTO RUN — M04 CUSTOM: churn-prediction.py
REM Churn Prediction Pipeline + 4 Model + Feature Importance
REM ============================================================
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
title M04 CUSTOM | Churn Prediction (4 Model Classifier)
echo.
echo ======================================================================
echo  🚀 M04 LATIHAN CUSTOM: churn-prediction.py
echo     Tujuan: Klasifikasi Churn Pelanggan (Tetap vs Pindah)
echo     Model: LogReg | Decision Tree d=5 | Random Forest 100 | Gradient Boosting
echo ======================================================================
echo.
cd /d c:\ai-engineer
echo [1/3] Aktivasi virtual environment venv_bnsp...
call venv_bnsp\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ GAGAL AKTIVASI VENV! Cek folder: c:\ai-engineer\venv_bnsp\
    pause
    exit /b 1
)
echo [2/3] Verifikasi interpreter & scikit-learn:
where python | findstr /i "venv_bnsp" >nul
if errorlevel 1 (
    echo ⚠️  WARNING: Python BUKAN dari venv_bnsp. Lanjut anyway...
)
python --version
python -c "import sklearn, pandas, numpy; print('scikit-learn =', sklearn.__version__, '| pandas =', pandas.__version__, '| numpy =', numpy.__version__)"
if errorlevel 1 (
    echo ❌ DEPENDENSI TIDAK LENGKAP! Jalankan ini dulu: python -m pip install -r requirements.txt
    pause
    exit /b 1
)
echo.
echo [3/3] Menjalankan script (Catatan: Mode input manual akan me-request input Anda):
echo    python modul_04_machine_learning\churn-prediction.py
echo.
echo ======================================================================
echo  📌 CATATAN TENTANG MODE INPUT MANUAL (Bagian Akhir Script):
echo    • Script akan meminta input 4 nilai: Umur, Gaji, Skor_Kredit, Jml_Pinjaman
echo    • Jika Anda langsung tekan ENTER = pakai DEFAULT value (mudah!)
echo    • Jika ingin skip seluruh input manual = tekan Ctrl+C (lanjut ke soal latihan)
echo ======================================================================
echo.
python modul_04_machine_learning\churn-prediction.py
set EXITCODE=%ERRORLEVEL%
echo.
echo ======================================================================
if %EXITCODE% EQU 0 (
    echo ✅ SELESAI! Exit Code = 0 (BERHASIL)
    echo    📊 Visualisasi chart disimpan ke:
    echo       c:\ai-engineer\modul_04_machine_learning\output_charts\M04_CUSTOM_01_top10_feature_importance.png
    echo       c:\ai-engineer\modul_04_machine_learning\output_charts\M04_CUSTOM_02_roc_curve_best_model.png
) else (
    echo ❌ TERJADI ERROR! Exit Code = %EXITCODE%
    echo    Scroll ke ATAS untuk melihat pesan error.
    echo    💡 Tips: Jika ModuleNotFoundError sklearn → pip install scikit-learn==1.4.2
)
echo ======================================================================
echo.
pause
