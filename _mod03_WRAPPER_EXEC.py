import os, sys, io, time
os.environ.setdefault("PYTHONUTF8", "1")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True)

LOG = r"c:\ai-engineer\_mod03_output_FINAL.txt"
log_f = open(LOG, "w", encoding="utf-8")

class Both:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def write(self, d):
        self.a.write(d)
        self.b.write(d)
        self.a.flush()
        self.b.flush()
    def flush(self):
        self.a.flush()
        self.b.flush()

sys.stdout = Both(sys.stdout, log_f)
sys.stderr = Both(sys.stderr, log_f)

SCRIPT = r"c:\ai-engineer\modul_03_data_prep\01_data_understanding_cleaning.py"
print("="*70, flush=True)
print(f"WRAPPER START {time.strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
print(f"EXEC PY: {sys.executable}", flush=True)
print(f"EXEC SCRIPT: {SCRIPT}", flush=True)
print("="*70, flush=True)

sys.path.insert(0, os.path.dirname(SCRIPT))

import traceback
try:
    with open(SCRIPT, "r", encoding="utf-8") as f:
        code = f.read()
    exec(compile(code, SCRIPT, "exec"), {"__name__": "__main__", "__file__": SCRIPT})
    print("\nWRAPPER: EXEC SUCCESS")
except SystemExit as e:
    print(f"\nWRAPPER: SystemExit code={e.code}")
except Exception:
    print("\nWRAPPER: EXCEPTION DURING EXEC:")
    print(traceback.format_exc())
finally:
    print(f"\nWRAPPER END {time.strftime('%Y-%m-%d %H:%M:%S')}")
    log_f.close()
