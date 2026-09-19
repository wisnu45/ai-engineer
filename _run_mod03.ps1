Set-StrictMode -Off
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$py = "c:\ai-engineer\venv_bnsp\Scripts\python.exe"
$script = "c:\ai-engineer\modul_03_data_prep\01_data_understanding_cleaning.py"
$stdout = "c:\ai-engineer\_mod03_stdout.log"
$stderr = "c:\ai-engineer\_mod03_stderr.log"

Write-Host "=== RUN MODUL 03 BAGIAN 1 (UTF-8 MODE) ==="
Write-Host "PYTHONUTF8=$env:PYTHONUTF8, PYTHONIOENCODING=$env:PYTHONIOENCODING"
Write-Host "PY      : $py"
Write-Host "SCRIPT  : $script"

$proc = Start-Process -PassThru -Wait -NoNewWindow -FilePath $py -ArgumentList @($script) -RedirectStandardOutput $stdout -RedirectStandardError $stderr

Write-Host ""
Write-Host "EXIT_CODE: $($proc.ExitCode)"
Write-Host ""
Write-Host "--- STDOUT (upto 300 lines) ---"
if (Test-Path $stdout) {
    Get-Content $stdout -TotalCount 300 -Encoding UTF8 -ErrorAction SilentlyContinue
} else {
    Write-Host "[no stdout file]"
}
Write-Host ""
Write-Host "--- STDERR ---"
if (Test-Path $stderr) {
    Get-Content $stderr -Encoding UTF8 -ErrorAction SilentlyContinue
} else {
    Write-Host "[no stderr file]"
}
