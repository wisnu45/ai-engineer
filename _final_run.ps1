$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
$py = "c:\ai-engineer\venv_bnsp\Scripts\python.exe"

Write-Host "=== Step 1: Verify packages ==="
& $py "c:\ai-engineer\_ps_check.py"

Write-Host ""
Write-Host "=== Step 2: Run Modul 03 Bagian 1 ==="
& $py "c:\ai-engineer\modul_03_data_prep\01_data_understanding_cleaning.py"

Write-Host ""
Write-Host "=== LASTEXITCODE = $LASTEXITCODE ==="
