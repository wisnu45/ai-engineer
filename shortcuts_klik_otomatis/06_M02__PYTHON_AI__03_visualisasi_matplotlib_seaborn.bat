@echo off
REM ============================================================
REM SHORTCUT AUTO RUN: 06_M02__PYTHON_AI__03_visualisasi_matplotlib_seaborn.bat
REM DI-GENERATE OTOMATIS — TINGGAL DOUBLE KLIK .BAT INI!
REM ============================================================
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
title MODUL 02 - PYTHON AI | 03_visualisasi_matplotlib_seaborn.py
echo.
echo ======================================================================
echo  🚀 MENJALANKAN SCRIPT: modul_02_python_ai\03_visualisasi_matplotlib_seaborn.py
echo ======================================================================
echo.

REM Step 1: Masuk ke folder project
cd /d c:i-engineer

REM Step 2: Aktivasi virtual environment venv_bnsp
echo [1/3] Aktivasi virtual environment venv_bnsp...
call venv_bnsp\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ GAGAL AKTIVASI VENV! Cek folder venv_bnsp ada di c:i-engineer    echo.
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
echo    python "modul_02_python_ai\03_visualisasi_matplotlib_seaborn.py"
echo.
python "modul_02_python_ai\03_visualisasi_matplotlib_seaborn.py"
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
