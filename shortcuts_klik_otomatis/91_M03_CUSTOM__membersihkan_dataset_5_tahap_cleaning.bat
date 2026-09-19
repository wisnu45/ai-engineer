@echo off
REM ============================================================
REM SHORTCUT AUTO: M03 CUSTOM | membersihkan_dataset.py (5 Tahap Cleaning)
REM DI-GENERATE OTOMATIS — TINGGAL DOUBLE KLIK!
REM ============================================================
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
title M03 CUSTOM | 5 Tahap Data Cleaning (BNSP)
echo.
echo ======================================================================
echo  🚀 M03 LATIHAN CUSTOM: membersihkan_dataset.py
echo     Tujuan: 5 Tahap Cleaning — Duplikat → Format → Invalid → Missing → Outlier
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
echo    python modul_03_data_prep\membersihkan_dataset.py
echo.
python modul_03_data_prep\membersihkan_dataset.py
set EXITCODE=%ERRORLEVEL%
echo.
echo ======================================================================
if %EXITCODE% EQU 0 (
    echo ✅ SELESAI! Exit Code = 0 (BERHASIL)
) else (
    echo ❌ TERJADI ERROR! Exit Code = %EXITCODE%
)
echo ======================================================================
echo.
pause
