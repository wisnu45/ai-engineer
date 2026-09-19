# V2 TINY LAUNCHER - Use contextlib.redirect_stdout + redirect_stderr for 100% capture.
import os
import sys
import time
import traceback
from contextlib import redirect_stdout, redirect_stderr, ExitStack

OUT_PATH = r"c:\ai-engineer\_mod03_tiny_result.txt"
fp = open(OUT_PATH, "w", encoding="utf-8", buffering=1)
fp.write("LAUNCHER_START_V2 " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
fp.write("PY=" + sys.executable + "\n")
fp.flush()

os.environ["PYTHONUTF8"] = "1"
os.environ["PYTHONIOENCODING"] = "utf-8"

# FIRST: patch numpy/pandas stdout/stderr to use utf-8 BEFORE importing anything
# We do the sys.stdout/stderr reconf early so any print in package init works.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True)

try:
    import numpy as np
    import pandas as pd
    fp.write(f"IMPORT_OK numpy={np.__version__} pandas={pd.__version__}\n")
except Exception as e:
    fp.write(f"IMPORT_FAIL: {type(e).__name__}: {e}\n")
    fp.write(traceback.format_exc())
    fp.close()
    sys.exit(1)
fp.flush()

SCRIPT = r"c:\ai-engineer\modul_03_data_prep\01_data_understanding_cleaning.py"
rc = 0

# Use ExitStack to capture ALL stdout/stderr (including from pandas)
with ExitStack() as stack:
    stack.enter_context(redirect_stdout(fp))
    stack.enter_context(redirect_stderr(fp))
    try:
        with open(SCRIPT, "r", encoding="utf-8") as f:
            code = f.read()
        exec(compile(code, SCRIPT, "exec"), {"__name__": "__main__", "__file__": SCRIPT})
    except SystemExit as e:
        rc = e.code if isinstance(e.code, int) else 1
    except Exception:
        rc = 3
        # Cannot print to fp via print because it's redirected; write directly.
        fp.write("\n\n====== EXCEPTION DURING SCRIPT EXEC ======\n")
        fp.write(traceback.format_exc())
        fp.write("==========================================\n")

fp.write(f"\n\nLAUNCHER_END_V2 RC={rc} " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
fp.close()
sys.exit(rc)
