import sys
import os
import traceback
import time

LOG_PATH = r"c:\ai-engineer\_mod03_output.txt"
SCRIPT_PATH = r"c:\ai-engineer\modul_03_data_prep\01_data_understanding_cleaning.py"

with open(LOG_PATH, "w", encoding="utf-8") as log:
    log.write("="*70 + "\n")
    log.write(f"RUNNER OUTPUT CAPTURE - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log.write(f"PYTHON: {sys.executable}\n")
    log.write(f"VERIFY numpy/pandas:\n")

    try:
        import numpy as np
        log.write(f"  numpy  OK  version={np.__version__}\n")
    except Exception as e:
        log.write(f"  numpy FAIL {type(e).__name__}: {e}\n")

    try:
        import pandas as pd
        log.write(f"  pandas OK  version={pd.__version__}\n")
    except Exception as e:
        log.write(f"  pandas FAIL {type(e).__name__}: {e}\n")

    log.write("="*70 + "\n\n")
    log.write("--- STDOUT/STDERR MODUL 03 BAGIAN 1 ---\n")
    log.flush()

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    class Tee:
        def __init__(self, log, orig):
            self.log = log
            self.orig = orig
        def write(self, data):
            self.log.write(data)
            self.log.flush()
            try:
                self.orig.write(data)
            except Exception:
                pass
        def flush(self):
            self.log.flush()
            try:
                self.orig.flush()
            except Exception:
                pass

    sys.stdout = Tee(log, old_stdout)
    sys.stderr = Tee(log, old_stderr)

    try:
        with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
            code = f.read()
        exec(compile(code, SCRIPT_PATH, "exec"), {"__name__": "__main__", "__file__": SCRIPT_PATH})
    except SystemExit as e:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        log.write(f"\nSYSTEM EXIT code={e.code}\n")
    except Exception:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        log.write("\n\nEXCEPTION TRACEBACK:\n")
        log.write(traceback.format_exc())
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        log.write(f"\nRUNNER FINISH at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log.flush()

print("LOG WRITTEN TO:", LOG_PATH)
