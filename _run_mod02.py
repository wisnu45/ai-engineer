import os, sys, time, traceback, io
from contextlib import redirect_stdout, redirect_stderr

os.environ.setdefault("PYTHONUTF8", "1")
OUT = r"c:\ai-engineer\_mod02_numpy_result.txt"
fp = open(OUT, "w", encoding="utf-8", buffering=1)
fp.write(f"WRAPPER START {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
fp.write(f"PY={sys.executable}\n")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True)

fp.write("CHECK_IMPORT numpy...\n")
fp.flush()
try:
    import numpy as np
    fp.write(f"IMPORT_OK numpy={np.__version__}\n")
except Exception as e:
    fp.write(f"IMPORT_FAIL numpy: {type(e).__name__}: {e}\n")
    fp.write(traceback.format_exc())
    fp.close()
    sys.exit(1)

SCRIPT = r"c:\ai-engineer\modul_02_python_ai\01_numpy_fundamental.py"
if not os.path.isfile(SCRIPT):
    fp.write(f"SCRIPT_NOT_FOUND: {SCRIPT}\n")
    # coba cari di semua modul
    for root, dirs, files in os.walk(r"c:\ai-engineer"):
        if "venv_bnsp" in root: continue
        for fn in files:
            if fn.lower() == "01_numpy_fundamental.py":
                fp.write(f"FOUND_AT: {os.path.join(root, fn)}\n")
    fp.close()
    sys.exit(2)

fp.write(f"SCRIPT_EXISTS_OK = {SCRIPT}\n")
fp.flush()

rc = 0
from contextlib import redirect_stdout, redirect_stderr
with redirect_stdout(fp), redirect_stderr(fp):
    try:
        with open(SCRIPT, "r", encoding="utf-8") as f:
            code = f.read()
        exec(compile(code, SCRIPT, "exec"), {"__name__": "__main__", "__file__": SCRIPT})
    except SystemExit as e:
        rc = e.code if isinstance(e.code, int) else 1
    except Exception:
        rc = 3
        fp.write("\n\n=== EXCEPTION ===\n")
        fp.write(traceback.format_exc())
        fp.write("=================\n")

fp.write(f"\n\nWRAPPER_END RC={rc} {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
fp.close()
sys.exit(rc)
