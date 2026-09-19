import os, sys
HOME = os.path.expanduser("~")
bashrc = os.path.join(HOME, ".bashrc")
bash_profile = os.path.join(HOME, ".bash_profile")

ALIAS = "alias ai-activate='cd /c/ai-engineer && source ./activate_venv_bnsp.sh'\n"
EXPORT_PYTHONUTF8 = "export PYTHONUTF8=1\n"

added = []

# Write to ~/.bashrc
with open(bashrc, "a+", encoding="utf-8", errors="replace") as f:
    f.seek(0)
    content = f.read()
    if "ai-activate" not in content:
        f.write("\n# ---- Alias AI Engineer BNSP venv ----\n")
        f.write(EXPORT_PYTHONUTF8)
        f.write(ALIAS)
        added.append(bashrc)

# Write to ~/.bash_profile jika ada (Git Bash kadang baca ini)
if os.path.isfile(bash_profile):
    with open(bash_profile, "a+", encoding="utf-8", errors="replace") as f:
        f.seek(0)
        content = f.read()
        if "ai-activate" not in content:
            f.write("\n# ---- Alias AI Engineer BNSP venv ----\n")
            f.write(EXPORT_PYTHONUTF8)
            f.write(ALIAS)
            added.append(bash_profile)
else:
    # Git Bash default kadang only baca /etc/profile + ~/.bash_profile, jadi buat .bash_profile
    with open(bash_profile, "w", encoding="utf-8", errors="replace") as f:
        # Sertakan sourcing .bashrc jika ada
        f.write("# ~/.bash_profile - auto created by BNSP AI setup\n")
        f.write("if [ -f ~/.bashrc ]; then . ~/.bashrc; fi\n")
        f.write("\n# ---- Alias AI Engineer BNSP venv ----\n")
        f.write(EXPORT_PYTHONUTF8)
        f.write(ALIAS)
        added.append(bash_profile)

LOG = r"c:\ai-engineer\_bashrc_setup_result.txt"
with open(LOG, "w", encoding="utf-8") as lg:
    lg.write("HOME = " + HOME + "\n")
    lg.write("Files updated:\n")
    for p in added:
        lg.write("  ✅ " + p + "\n")
    lg.write("\nCONTENT ~/.bashrc (LAST 20 lines):\n")
    try:
        with open(bashrc, "r", encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
            for line in lines[-20:]:
                lg.write("  | " + line + "\n")
    except Exception as e:
        lg.write("  READ_ERROR: " + repr(e) + "\n")
print("OK, log:", LOG)
