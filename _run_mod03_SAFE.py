import os, sys, time, traceback
os.environ.setdefault("PYTHONUTF8", "1")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_mod03_result.txt")

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(f"START {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"PY={sys.executable}\n")
    try:
        import numpy, pandas
        f.write(f"NUMPY_OK={numpy.__version__}  PANDAS_OK={pandas.__version__}\n")
    except Exception as e:
        f.write(f"IMPORT_FAIL: {e}\n")

    SCRIPT = os.path.join(os.path.dirname(OUT), "modul_03_data_prep", "01_data_understanding_cleaning.py")
    f.write(f"ABOUT TO EXEC SCRIPT: {SCRIPT}\n")
    f.flush()

    buf = []
    import io as _io
    cap = _io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    class Dup:
        def __init__(self, orig, cap): self.orig = orig; self.cap = cap
        def write(self, d):
            try: self.cap.write(d)
            except Exception: pass
            try: self.orig.write(d)
            except Exception: pass
        def flush(self):
            try: self.cap.flush()
            except Exception: pass
            try: self.orig.flush()
            except Exception: pass
    sys.stdout = Dup(old_out, cap)
    sys.stderr = Dup(old_err, cap)

    rc = 0
    try:
        with open(SCRIPT, "r", encoding="utf-8") as sf:
            code = sf.read()
        exec(compile(code, SCRIPT, "exec"), {"__name__": "__main__", "__file__": SCRIPT})
    except SystemExit as e:
        rc = e.code if isinstance(e.code, int) else 1
    except Exception:
        rc = 2
        cap.write("\n==== EXCEPTION ====\n")
        cap.write(traceback.format_exc())
    finally:
        sys.stdout = old_out
        sys.stderr = old_err

    f.write(f"EXEC_FINISHED RC={rc}\n")
    f.write("==== STDOUT/STDERR CAPTURED BELOW ====\n")
    f.write(cap.getvalue())
    f.write("\n==== END CAPTURE ====\n")
    f.write(f"FINISH {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

with open(OUT, "a", encoding="utf-8") as f:
    f.write(f"APPEND_VERIFY_OK\n")

print(f"RESULT_FILE={OUT}")
