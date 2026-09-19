import os, sys, time, subprocess
OUT = r"c:\ai-engineer\_venv_check.txt"
with open(OUT, "w", encoding="utf-8", buffering=1) as f:
    f.write("="*70 + "\n")
    f.write(f"VERIFIKASI VENV_BNSP - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*70 + "\n")

    # 1. Cek direktori Scripts
    scripts_dir = r"c:\ai-engineer\venv_bnsp\Scripts"
    f.write(f"\n1. CEK DIRECTORY Scripts: {scripts_dir}\n")
    if os.path.isdir(scripts_dir):
        files = sorted(os.listdir(scripts_dir))
        interesting = [x for x in files if x.lower().startswith(("activate","python","pip","numpy"))]
        f.write(f"   ✅ ADA. Total {len(files)} file. File penting:\n")
        for name in interesting[:30]:
            full = os.path.join(scripts_dir, name)
            size = os.path.getsize(full) if os.path.isfile(full) else 0
            f.write(f"        - {name:35s} {size:>8d} bytes\n")
    else:
        f.write("   ❌ TIDAK ADA\n")

    # 2. Cek python.exe di Scripts
    py_exe = os.path.join(scripts_dir, "python.exe")
    pip_exe = os.path.join(scripts_dir, "pip.exe")
    activate_bat = os.path.join(scripts_dir, "activate.bat")
    activate_ps1 = os.path.join(scripts_dir, "Activate.ps1")

    f.write(f"\n2. CEK FILE PENTING:\n")
    for label, p in [("python.exe", py_exe), ("pip.exe", pip_exe), ("activate.bat", activate_bat), ("Activate.ps1", activate_ps1)]:
        if os.path.isfile(p):
            sz = os.path.getsize(p)
            f.write(f"   ✅ {label:18s} ADA ({sz:,} bytes) -> {p}\n")
        else:
            f.write(f"   ❌ {label:18s} TIDAK ADA di {p}\n")

    # 3. Jalankan python version & pip list
    f.write(f"\n3. JALANKAN PYTHON VERSION:\n")
    try:
        r = subprocess.run([py_exe, "--version"], capture_output=True, text=True, timeout=30)
        f.write(f"   EXIT={r.returncode}\n")
        f.write(f"   STDOUT: {r.stdout.strip()}\n")
        f.write(f"   STDERR: {r.stderr.strip()}\n")
    except Exception as e:
        f.write(f"   EXCEPTION: {type(e).__name__}: {e}\n")

    f.write(f"\n4. JALANKAN PIP LIST (paket inti saja):\n")
    try:
        r = subprocess.run([py_exe, "-m", "pip", "list", "--format=columns"], capture_output=True, text=True, timeout=120)
        f.write(f"   EXIT={r.returncode}\n")
        lines = r.stdout.splitlines()
        for line in lines:
            low = line.lower()
            if any(k in low for k in ["numpy","pandas","matplotlib","seaborn","scikit","scipy","joblib","pillow","openpyxl","pip","setuptools","package","----"]):
                f.write(f"   {line}\n")
        if r.stderr.strip():
            f.write(f"   STDERR: {r.stderr.strip()[:1000]}\n")
    except Exception as e:
        f.write(f"   EXCEPTION: {type(e).__name__}: {e}\n")

    # 5. Test import package via subprocess
    f.write(f"\n5. TEST IMPORT PACKAGE via subprocess venv_python:\n")
    test_code = ";".join([
        "import sys",
        "print('PYEXE='+sys.executable)",
        "import numpy; print('numpy='+numpy.__version__)",
        "import pandas; print('pandas='+pandas.__version__)",
        "try:\n import matplotlib; print('matplotlib='+matplotlib.__version__)\nexcept Exception as e: print('matplotlib_ERR='+repr(e))",
        "try:\n import seaborn; print('seaborn='+seaborn.__version__)\nexcept Exception as e: print('seaborn_ERR='+repr(e))",
        "import sklearn; print('sklearn='+sklearn.__version__)",
        "import scipy; print('scipy='+scipy.__version__)",
        "import joblib; print('joblib='+joblib.__version__)",
        "import PIL; print('Pillow='+PIL.__version__)",
    ])
    try:
        r = subprocess.run([py_exe, "-c", test_code], capture_output=True, text=True, timeout=60)
        f.write(f"   EXIT={r.returncode}\n")
        for line in (r.stdout+r.stderr).strip().splitlines():
            f.write(f"   {line}\n")
    except Exception as e:
        f.write(f"   EXCEPTION: {type(e).__name__}: {e}\n")

    f.write(f"\n{'='*70}\n")
    f.write(f"SELESAI - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

print(f"HASIL DISIMPAN KE: {OUT}")
