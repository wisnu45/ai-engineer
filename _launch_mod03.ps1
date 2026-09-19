$ErrorActionPreference = "SilentlyContinue"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
$py = "c:\ai-engineer\venv_bnsp\Scripts\python.exe"

Write-Host "START WRAPPER MODUL 03..."
& $py "c:\ai-engineer\_mod03_WRAPPER_EXEC.py"
$rc = $LASTEXITCODE
Write-Host "PYTHON LASTEXITCODE= $rc"

if (Test-Path "c:\ai-engineer\_mod03_output_FINAL.txt") {
    Write-Host ""
    Write-Host "=== _mod03_output_FINAL.txt (300 lines) ==="
    Get-Content "c:\ai-engineer\_mod03_output_FINAL.txt" -TotalCount 300 -Encoding UTF8
} else {
    Write-Host "FILE _mod03_output_FINAL.txt TIDAK ADA."
}
