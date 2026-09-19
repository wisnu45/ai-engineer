# TINY LAUNCHER - Open output FIRST, then exec the Modul 03 script.
import os
import sys
import time

OUT_PATH = r"c:\ai-engineer\_mod03_tiny_result.txt"
fp = open(OUT_PATH, "w", encoding="utf-8", buffering=1)
fp.write("LAUNCHER_START " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
fp.write("PY=" + sys.executable + "\n")
fp.flush()

os.environ["PYTHONUTF8"] = "1"
os.environ["PYTHONIOENCODING"] = "utf-8"

try:
    import io
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception as e:
    fp.write(f"RECONF_FAIL: {e}\n")
    try:
        import io as _io
        sys.stdout = _io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True)
        sys.stderr = _io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True)
    except Exception as e2:
        fp.write(f"ALT_RECONF_FAIL: {e2}\n")
fp.flush()

import traceback
try:
    import numpy as np
    import pandas as pd
    fp.write(f"IMPORT_OK numpy={np.__version__} pandas={pd.__version__}\n")
    fp.flush()
except Exception as e:
    fp.write(f"IMPORT_FAIL: {type(e).__name__}: {e}\n")
    fp.write(traceback.format_exc())
    fp.close()
    sys.exit(1)

# Redirect stdout/stderr to BOTH (fp + original)
orig_out, orig_err = sys.stdout, sys.stderr
class TEE:
    def __init__(self, a, b): self.a = a; self.b = b
    def write(self, d):
        try: self.a.write(d); self.a.flush()
        except Exception: pass
        try: self.b.write(d); self.b.flush()
        except Exception: pass
    def flush(self):
        try: self.a.flush()
        except Exception: pass
        try: self.b.flush()
        except Exception: pass

sys.stdout = TEE(fp, orig_out)
sys.stderr = TEE(fp, orig_err)

SCRIPT = r"c:\ai-engineer\modul_03_data_prep\01_data_understanding_cleaning.py"
rc = 0
try:
    with open(SCRIPT, "r", encoding="utf-8") as f:
        code = f.read()
    exec(compile(code, SCRIPT, "exec"), {"__name__": "__main__", "__file__": SCRIPT})
except SystemExit as e:
    rc = e.code if isinstance(e.code, int) else 1
except Exception:
    rc = 3
    orig_out.write("\n")
    orig_err.write("\nEXCEPTION IN SCRIPT:\n")
    traceback.print_exc(file=orig_err)
finally:
    sys.stdout = orig_out
    sys.stderr = orig_err
    fp.write("\nLAUNCHER_END RC=" + str(rc) + " " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    fp.close()

sys.exit(rc)
