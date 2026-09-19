import os, json, sys

VSC_DIR = r"c:\ai-engineer\.vscode"
os.makedirs(VSC_DIR, exist_ok=True)

# ============================================================
# 1. SETTINGS.JSON — Konfigurasi default TRAE/VS Code untuk project
# ============================================================
settings = {
    "python.defaultInterpreterPath": "c:\\ai-engineer\\venv_bnsp\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": True,
    "python.terminal.activateEnvInCurrentTerminal": True,
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.autoImportCompletions": True,
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none",
        "reportShadowedImports": "none"
    },
    "terminal.integrated.defaultProfile.windows": "Command Prompt",
    "terminal.integrated.profiles.windows": {
        "Command Prompt": {
            "path": "C:\\WINDOWS\\System32\\cmd.exe",
            "args": ["/K", "cd /d c:\\ai-engineer && venv_bnsp\\Scripts\\activate.bat"]
        },
        "PowerShell": {
            "path": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
            "args": ["-NoExit", "-Command", "Set-Location c:\\ai-engineer; .\\venv_bnsp\\Scripts\\Activate.ps1"]
        },
        "Git Bash": {
            "path": "C:\\Program Files\\Git\\bin\\bash.exe",
            "args": ["--cd=c:/ai-engineer", "-c", "source ./activate_venv_bnsp.sh; exec bash"]
        }
    },
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "files.encoding": "utf8",
    "editor.formatOnSave": True,
    "jupyter.sendSelectionToInteractiveWindow": False,
    "jupyter.alwaysTrustNotebooks": True,
    "terminal.integrated.env.windows": {
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8"
    },
    "explorer.fileNesting.enabled": True,
    "security.workspace.trust.untrustedFiles": "open",
    "window.zoomLevel": 0,
    "workbench.editorAssociations": {
        "*.md": "vscode.markdown.preview.editor",
        "*.json": "default"
    }
}

with open(os.path.join(VSC_DIR, "settings.json"), "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=2, ensure_ascii=False)

print("✅ .vscode/settings.json OK")

# ============================================================
# 2. LAUNCH.JSON — 17 konfigurasi Run & Debug, tinggal pilih dropdown
# ============================================================
all_mod_configs = []

def add_config(name, cwd, program):
    return {
        "name": name,
        "type": "debugpy",
        "request": "launch",
        "program": program,
        "console": "integratedTerminal",
        "cwd": cwd,
        "justMyCode": True,
        "env": {
            "PYTHONUTF8": "1",
            "PYTHONIOENCODING": "utf-8",
            "PYDEVD_WARN_EVALUATION_TIMEOUT": "5000"
        },
        "python": "c:\\ai-engineer\\venv_bnsp\\Scripts\\python.exe"
    }

ROOT = r"c:\ai-engineer"

MODUL = [
    ("M01 Fundamental AI", "modul_01_fundamental_ai", [
        "01_konsep_dasar_ai.py",
        "02_ai_lifecycle_etika.py",
        "03_responsible_ai_bias_fairness.py"
    ]),
    ("M02 Python AI", "modul_02_python_ai", [
        "01_numpy_fundamental.py",
        "02_pandas_dataframe.py",
        "03_visualisasi_matplotlib_seaborn.py",
        "04_function_oop_exception.py"
    ]),
    ("M03 Data Prep", "modul_03_data_prep", [
        "01_data_understanding_cleaning.py",
        "02_transformation_encoding_scaling.py",
        "03_eda_splitting.py"
    ]),
    ("M04 Machine Learning", "modul_04_machine_learning", [
        "01_klasifikasi_logreg_svm_dt_rf.py",
        "02_regresi_linreg_ridge_lasso_gbm.py",
        "03_clustering_kmeans_dbscan_hierarchical.py"
    ]),
    ("M05 Evaluasi & Tuning", "modul_05_ml_evaluation_tuning", [
        "01_metrics_evaluation_class_imbalance.py",
        "02_cross_validation_tuning_grid_random_search.py"
    ]),
    ("M06 Deep Learning", "modul_06_deep_learning", [
        "01_ann_mlp_perceptron_backprop.py",
        "02_cnn_classification_mnist.py"
    ]),
    ("M07 Computer Vision", "modul_07_computer_vision", [
        "01_image_processing_classification.py"
    ]),
    ("M08 NLP", "modul_08_nlp", [
        "01_text_preprocessing_tfidf_sentiment.py"
    ]),
    ("M09 Generative AI", "modul_09_generative_ai", [
        "01_generative_ai_llm_prompt_engineering_rag.py"
    ]),
    ("M10 Deployment", "modul_10_deployment", [
        "01_model_serialization_fastapi_docker_mlops.py"
    ]),
    ("M11 Proyek E2E", "modul_11_proyek_end_to_end", [
        "01_proyek_e2e_harga_rumah_portfolio.py"
    ]),
    ("M12 Persiapan BNSP", "modul_12_persiapan_bnsp", [
        "01_simulasi_asesmen_checklist_soal_bnsp.py"
    ])
]

for label, folder, files in MODUL:
    for fname in files:
        full_folder = os.path.join(ROOT, folder)
        full_program = os.path.join(full_folder, fname)
        nm = f"{label} | {fname}"
        all_mod_configs.append(add_config(nm, ROOT, full_program))

# Konfigurasi FASTAPI (Modul 10)
all_mod_configs.append({
    "name": "M10 FastAPI | uvicorn run server (port 8000)",
    "type": "debugpy",
    "request": "launch",
    "module": "uvicorn",
    "args": [
        "fastapi_churn_app_TEMPLATE:app",
        "--host", "0.0.0.0",
        "--port", "8000",
        "--reload"
    ],
    "console": "integratedTerminal",
    "cwd": r"c:\ai-engineer\modul_10_deployment",
    "env": {
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8"
    },
    "justMyCode": True,
    "python": "c:\\ai-engineer\\venv_bnsp\\Scripts\\python.exe"
})

# Konfigurasi FASTAPI Modul 11 House Prediction
all_mod_configs.append({
    "name": "M11 FastAPI | House Price server (port 8100)",
    "type": "debugpy",
    "request": "launch",
    "module": "uvicorn",
    "args": [
        "app_house_prediction_TEMPLATE:app",
        "--host", "0.0.0.0",
        "--port", "8100",
        "--reload"
    ],
    "console": "integratedTerminal",
    "cwd": r"c:\ai-engineer\modul_11_proyek_end_to_end",
    "env": {
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8"
    },
    "justMyCode": True,
    "python": "c:\\ai-engineer\\venv_bnsp\\Scripts\\python.exe"
})

launch = {
    "version": "0.2.0",
    "configurations": all_mod_configs,
    "compounds": [
        {
            "name": "▶️ Run ALL Modul 1-3 (Berurutan)",
            "configurations": [
                "M01 Fundamental AI | 01_konsep_dasar_ai.py",
                "M01 Fundamental AI | 02_ai_lifecycle_etika.py",
                "M01 Fundamental AI | 03_responsible_ai_bias_fairness.py",
                "M02 Python AI | 01_numpy_fundamental.py",
                "M02 Python AI | 02_pandas_dataframe.py",
                "M02 Python AI | 03_visualisasi_matplotlib_seaborn.py",
                "M02 Python AI | 04_function_oop_exception.py",
                "M03 Data Prep | 01_data_understanding_cleaning.py",
                "M03 Data Prep | 02_transformation_encoding_scaling.py",
                "M03 Data Prep | 03_eda_splitting.py"
            ],
            "stopAll": False
        }
    ]
}

with open(os.path.join(VSC_DIR, "launch.json"), "w", encoding="utf-8") as f:
    json.dump(launch, f, indent=2, ensure_ascii=False)

print(f"✅ .vscode/launch.json OK — Total {len(all_mod_configs)} konfigurasi Run & Debug")
for c in all_mod_configs[:10]:
    print("  -", c["name"])
print("  ... dan", len(all_mod_configs)-10, "konfigurasi lainnya.")

# ============================================================
# 3. EXTENSIONS.JSON — Rekomendasi ekstensi
# ============================================================
extensions = {
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.debugpy",
        "ms-python.isort",
        "ms-toolsai.jupyter-renderers",
        "mechatroner.rainbow-csv",
        "tamasfe.even-better-toml",
        "foxundermoon.shell-format",
        "exiasr.hadolint",
        "ms-azuretools.vscode-docker"
    ]
}

with open(os.path.join(VSC_DIR, "extensions.json"), "w", encoding="utf-8") as f:
    json.dump(extensions, f, indent=2, ensure_ascii=False)

print("✅ .vscode/extensions.json OK — 10 rekomendasi ekstensi")
print("\n" + "="*60)
print("🎉 SEMUA KONFIGURASI IDE TRAE SELESAI!")
print("="*60)
print("""
CARA MENGGUNAKAN TOMBOL RUN (3 PILIHAN):

1️⃣  TOMBOL RUN ▶️ (paling simpel)
   • BUKA file .py misal: modul_02_python_ai/03_visualisasi_matplotlib_seaborn.py
   • KLIK PANAH KECIL ▼ di samping tombol Run (segitiga hijau)
   • PILIH: 👉 'Run Python File'   👈 JANGAN pilih Run Interactive / Run Cell
   • ✅ SELESAI — terminal otomatis aktifkan venv_bnsp & eksekusi file!

2️⃣  F5 DEBUG MODE (jika mau step-by-step / breakpoint)
   • BUKA tab Run and Debug (CTRL+SHIFT+D) — serangga 🐞 di sidebar kiri
   • KLIK DROPDOWN "Run and Debug" di atas
   • PILIH konfigurasi misal:  'M02 Python AI | 03_visualisasi_matplotlib_seaborn.py'
   • TEKAN F5 — debug mode! Bisa pasang breakpoint (titik merah di line).

3️⃣  DOUBLE-CLICK SHORTCUT .BAT di File Explorer
   • Lihat folder 'shortcuts_klik_otomatis/' — file .bat untuk setiap modul.
   • Double-click file → terminal terbuka, venv aktif, script jalan AUTO.
""")
