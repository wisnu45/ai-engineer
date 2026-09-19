@echo off
REM ============================================================
REM SHORTCUT AUTO RUN: 25_M11_PROYEK_E2E__RUN_FASTAPI_HOUSE_8100.bat
REM DI-GENERATE OTOMATIS — TINGGAL DOUBLE KLIK .BAT INI!
REM ============================================================
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
title M11 | FastAPI House Prediction Server :8100
echo.
echo ======================================================================
echo  🚀 MENJALANKAN SCRIPT: app_house_prediction_TEMPLATE:app --host 0.0.0.0 --port 8100 --reload
echo ======================================================================
echo.

REM Step 1: Masuk ke folder project
cd /d c:\ai-engineer\modul_11_proyek_end_to_end

REM Step 2: Aktivasi virtual environment venv_bnsp
echo [1/3] Aktivasi virtual environment venv_bnsp...
call ..\venv_bnsp\Scripts\activate.bat
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
echo    python "app_house_prediction_TEMPLATE:app --host 0.0.0.0 --port 8100 --reload"
echo.
python -m uvicorn "app_house_prediction_TEMPLATE:app --host 0.0.0.0 --port 8100 --reload"
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
