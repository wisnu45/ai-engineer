import os
folder = r"c:\ai-engineer\venv_bnsp\Scripts"
out = r"c:\ai-engineer\_venv_files.txt"
with open(out, "w", encoding="utf-8") as f:
    if os.path.isdir(folder):
        files = sorted(os.listdir(folder))
        f.write(f"Total {len(files)} files in {folder}\n")
        f.write("="*80 + "\n")
        for name in files:
            full = os.path.join(folder, name)
            if os.path.isfile(full):
                sz = os.path.getsize(full)
                f.write(f"FILE | {name:40s} | {sz:>10,} bytes\n")
            elif os.path.isdir(full):
                f.write(f"DIR  | {name:40s} |\n")
    else:
        f.write(f"FOLDER NOT FOUND: {folder}\n")
print("OK, written to", out)
