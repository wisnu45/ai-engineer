@echo off
REM ============================================================
REM SHORTCUT AUTO: M03 CUSTOM | fitur_baru.py (Latihan FE + Encoding + Scaling)
REM DI-GENERATE OTOMATIS — TINGGAL DOUBLE KLIK!
REM ============================================================
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
title M03 CUSTOM | Feature Engineering + Encoding + Scaling
echo.
echo ======================================================================
echo  🚀 M03 LATIHAN CUSTOM: fitur_baru.py
echo     Tujuan: Feature Engineering, Categorical Encoding, Feature Scaling
echo ======================================================================
echo.
cd /d c:\ai-engineer
echo [1/3] Aktivasi virtual environment venv_bnsp...
call venv_bnsp\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ GAGAL AKTIVASI VENV!
    pause
    exit /b 1
)
echo [2/3] Verifikasi interpreter:
where python | findstr /i "venv_bnsp" >nul
if errorlevel 1 (
    echo ⚠️  WARNING: Python BUKAN dari venv_bnsp! Lanjut anyway...
)
python --version
echo.
echo [3/3] Menjalankan script:
echo    python modul_03_data_prep\fitur_baru.py
echo.
python modul_03_data_prep\fitur_baru.py
set EXITCODE=%ERRORLEVEL%
echo.
echo ======================================================================
if %EXITCODE% EQU 0 (
    echo ✅ SELESAI! Exit Code = 0 (BERHASIL)
) else (
    echo ❌ TERJADI ERROR! Exit Code = %EXITCODE%
    echo.
    echo    💡 Tips perbaiki:
    echo    1. Jika KeyError xxx not in index: lihat baris print data_final[..]
    echo    2. Jika ModuleNotFoundError: install paket via pip install -r requirements.txt
)
echo ======================================================================
echo.
pause
