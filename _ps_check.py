import sys
import os
outp = []
outp.append("OK")
outp.append("PY_VER=" + sys.version.split()[0])
outp.append("EXE=" + sys.executable)
for name in ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "scipy", "joblib"]:
    try:
        m = __import__(name)
        v = getattr(m, "__version__", "installed")
        outp.append(f"OK_{name.upper()}={v}")
    except Exception as e:
        outp.append(f"ERR_{name.upper()}={type(e).__name__}: {e}")

with open(r"c:\ai-engineer\_ps_check_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(outp) + "\n")

print("\n".join(outp))
