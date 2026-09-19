import subprocess
import sys
import os

PACKAGES = [
    "pip==24.0",
    "numpy==1.26.4",
    "pandas==2.2.1",
    "matplotlib==3.8.4",
    "seaborn==0.13.2",
    "scikit-learn==1.4.2",
    "scipy==1.12.0",
    "Pillow==10.3.0",
    "openpyxl==3.1.2",
    "joblib==1.4.2",
]

log_path = r"c:\ai-engineer\_install_log.txt"
with open(log_path, "w", encoding="utf-8") as log:
    log.write("START INSTALL\n")
    log.write(f"PYTHON EXE: {sys.executable}\n\n")
    log.flush()

    for pkg in PACKAGES:
        log.write(f"\n{'='*60}\nINSTALL: {pkg}\n{'='*60}\n")
        log.flush()
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", pkg, "--no-input",
                 "--disable-pip-version-check"],
                capture_output=True, text=True, timeout=600,
            )
            log.write(f"EXIT CODE: {result.returncode}\n")
            log.write("--- STDOUT ---\n")
            log.write(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)
            log.write("\n--- STDERR ---\n")
            log.write(result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)
        except Exception as e:
            log.write(f"EXCEPTION: {type(e).__name__}: {e}\n")
        log.flush()

    log.write("\n\nDONE INSTALL. VERIFY IMPORT:\n")
    for mod in ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "scipy", "PIL", "openpyxl", "joblib"]:
        try:
            m = __import__(mod)
            ver = getattr(m, "__version__", "OK")
            log.write(f"  ✅ {mod:12s} version={ver}\n")
        except Exception as e:
            log.write(f"  ❌ {mod:12s} ERROR: {type(e).__name__}: {e}\n")
        log.flush()

print("INSTALL LOG SAVED TO:", log_path)
