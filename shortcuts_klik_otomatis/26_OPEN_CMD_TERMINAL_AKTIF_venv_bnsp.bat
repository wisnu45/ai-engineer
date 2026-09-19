@echo off
chcp 65001 >nul
title CMD Terminal (venv_bnsp AKTIF)
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
cd /d c:i-engineer
call venv_bnsp\Scriptsctivate.bat
echo.
echo ======================================================================
echo  ✅ Terminal siap pakai! venv_bnsp SUDAH AKTIF (ada prefix (venv_bnsp))
echo ======================================================================
echo.
echo  🚀 Perintah Cepat (copy paste + ENTER):
echo     python modul_02_python_ai\01_numpy_fundamental.py
echo     python modul_03_data_prep\01_data_understanding_cleaning.py
echo     python modul_10_deployment\01_model_serialization_fastapi_docker_mlops.py
echo.
echo  📖 Tips:
echo     • deactivate = keluar dari venv_bnsp
echo     • cls = bersihkan layar
echo     • exit = tutup terminal
echo.
cmd /k
