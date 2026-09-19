# ============================================================================
# activate_venv_bnsp.sh — ACTIVATION SCRIPT KHUSUS GIT BASH (MINGW64) WINDOWS
# VERSI 2 — Bash Strict Safe, double activation guard, tput color PS1 escape
# ============================================================================
# CARA PAKAI (di Git Bash):
#   cd /c/ai-engineer
#   source ./activate_venv_bnsp.sh
#
# Setelah sukses, prompt Anda BERUBAH menjadi:  (venv_bnsp) user@machine MINGW64 /c/ai-engineer
# Untuk keluar dari venv, ketik: deactivate
# ============================================================================

# --- DOUBLE ACTIVATION GUARD: Jika sudah aktif, cetak info dan return ---
if [ -n "${VIRTUAL_ENV_BNSP_ACTIVE:-}" ]; then
    echo ""
    echo "ℹ️  venv_bnsp SUDAH AKTIF (VIRTUAL_ENV=$VIRTUAL_ENV)"
    echo "   PYTHON_EXE = $(which python)"
    echo "   Gunakan 'deactivate' terlebih dahulu jika ingin refresh."
    return 0 2>/dev/null || exit 0
fi

VENV_DIR="/c/ai-engineer/venv_bnsp"
VENV_SCRIPTS="$VENV_DIR/Scripts"

if [ ! -d "$VENV_DIR" ]; then
    echo "❌ ERROR: Folder venv TIDAK DITEMUKAN di $VENV_DIR"
    echo "   Pastikan Anda sudah membuat virtual env venv_bnsp di c:\\ai-engineer\\"
    return 1 2>/dev/null || exit 1
fi

if [ ! -f "$VENV_SCRIPTS/python.exe" ]; then
    echo "❌ ERROR: python.exe TIDAK ADA di $VENV_SCRIPTS/python.exe"
    return 1 2>/dev/null || exit 1
fi

# --- Deactivate function (declare ONCE, guard agar tidak redeclare error) ---
if ! declare -f deactivate_venvbnsp_cleanup >/dev/null 2>&1; then
deactivate_venvbnsp_cleanup () {
    if [ -n "${_OLD_BNSP_PATH:-}" ]; then
        PATH="$_OLD_BNSP_PATH"
        export PATH
        unset _OLD_BNSP_PATH
    fi
    if [ -n "${_OLD_BNSP_PS1:-}" ]; then
        PS1="$_OLD_BNSP_PS1"
        export PS1
        unset _OLD_BNSP_PS1
    fi
    if [ -n "${_OLD_BNSP_PYTHONHOME:-}" ]; then
        PYTHONHOME="$_OLD_BNSP_PYTHONHOME"
        export PYTHONHOME
        unset _OLD_BNSP_PYTHONHOME
    else
        unset PYTHONHOME 2>/dev/null
    fi
    unset VIRTUAL_ENV 2>/dev/null
    unset VIRTUAL_ENV_BNSP_ACTIVE 2>/dev/null
    # Unset our functions (jika dideklarasikan):
    unset -f deactivate_venvbnsp_cleanup 2>/dev/null
    unset -f deactivate 2>/dev/null
    return 0
}
fi

# Override global deactivate() HANYA JIKA BELUM ADA / bukan punya kita:
if ! declare -f deactivate >/dev/null 2>&1; then
    deactivate () { deactivate_venvbnsp_cleanup; }
fi

# --- Set variables ---
export VIRTUAL_ENV="$VENV_DIR"
export VIRTUAL_ENV_BNSP_ACTIVE=1
_OLD_BNSP_PATH="$PATH"
PATH="$VENV_SCRIPTS:$PATH"
export PATH

# --- Simpan PS1 lama & Apply prefix (WARNA HIJAU jika tput support) ---
_OLD_BNSP_PS1="${PS1:-}"
_PREFIX=""
if command -v tput >/dev/null 2>&1; then
    _GREEN="$(tput setaf 2 2>/dev/null || true)"
    _RESET="$(tput sgr0 2>/dev/null || true)"
    _PREFIX="\[${_GREEN}\](venv_bnsp)\[${_RESET}\] "
else
    _PREFIX="(venv_bnsp) "
fi
PS1="${_PREFIX}${PS1:-}"
unset _PREFIX _GREEN _RESET
export PS1

# --- Unset PYTHONHOME jika set (simpan untuk restore) ---
if [ -n "${PYTHONHOME:-}" ]; then
    _OLD_BNSP_PYTHONHOME="${PYTHONHOME}"
    unset PYTHONHOME
fi

# ============================================================================
# PRINT OUTPUT SUKSES + VERIFIKASI PAKET
# ============================================================================
echo ""
echo "✅ Virtual env (venv_bnsp) AKTIF!"
echo "   VENV_DIR    = $VIRTUAL_ENV"
echo "   PYTHON_EXE  = $(which python 2>/dev/null || echo 'python-not-in-PATH')"
echo ""
echo "🔍 Verifikasi cepat (numpy, pandas, scikit-learn):"
python -c "
import sys
try:
    import numpy
    print('   numpy  OK =', numpy.__version__)
except Exception as e:
    print('   numpy  FAIL:', type(e).__name__, e)
try:
    import pandas
    print('   pandas OK =', pandas.__version__)
except Exception as e:
    print('   pandas FAIL:', type(e).__name__, e)
try:
    import sklearn
    print('   sklearn OK =', sklearn.__version__)
except Exception as e:
    print('   sklearn FAIL:', type(e).__name__, e)
"
echo ""
echo "💡 Tips:"
echo "   • Ketik 'deactivate' untuk keluar dari virtual environment."
echo "   • Jalankan Modul:  python modul_02_python_ai/01_numpy_fundamental.py"
echo "   • Atau Modul 03:  python modul_03_data_prep/01_data_understanding_cleaning.py"
echo ""
