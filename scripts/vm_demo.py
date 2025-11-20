# vm_demo.py — Linear, step-by-step demo for self-managed MySQL on a VM
# Run this file top-to-bottom OR run it cell-by-cell in VS Code.
# Prereqs:
#   pip install sqlalchemy pymysql pandas python-dotenv
#
# Env vars (populate a local .env):
#   VM_DB_HOST, VM_DB_PORT, VM_DB_USER, VM_DB_PASS, VM_DB_NAME

import os, time
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# --- 0) Load environment ---
load_dotenv("assignment_4/.env")  # reads .env in current working directory

VM_DB_HOST = os.getenv("VM_DB_HOST")
VM_DB_PORT = os.getenv("VM_DB_PORT", "3306")
VM_DB_USER = os.getenv("VM_DB_USER")
VM_DB_PASS = os.getenv("VM_DB_PASS")
VM_DB_NAME = os.getenv("VM_DB_NAME")

print("[ENV] VM_DB_HOST:", VM_DB_HOST)
print("[ENV] VM_DB_PORT:", VM_DB_PORT)
print("[ENV] VM_DB_USER:", VM_DB_USER)
print("[ENV] VM_DB_NAME:", VM_DB_NAME)

# --- 1) Connect to server (no DB) and ensure database exists ---
server_url = f"mysql+pymysql://{VM_DB_USER}:{VM_DB_PASS}@{VM_DB_HOST}:{VM_DB_PORT}/?ssl_disabled=true"
print("[STEP 1] Connecting to MySQL server (no DB):", server_url.replace(VM_DB_PASS, "*****"))
t0 = time.time()

engine_server = create_engine(server_url, pool_pre_ping=True)
with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{VM_DB_NAME}`"))
    conn.commit()
print(f"[OK] Ensured database `{VM_DB_NAME}` exists.")

# --- 2) Connect to the target database ---
db_url = f"mysql+pymysql://{VM_DB_USER}:{VM_DB_PASS}@{VM_DB_HOST}:{VM_DB_PORT}/{VM_DB_NAME}?ssl_disabled=true"
engine = create_engine(db_url)

# ---- 3) Create a DataFrame and write to a table ----
table_name = "visits"
df = pd.DataFrame(
    [
        {"patient_id": 10, "visit_date": "2025-10-01", "bp_sys": 117, "bp_dia": 75},
        {"patient_id": 11, "visit_date": "2025-10-02", "bp_sys": 120, "bp_dia": 80},
        {"patient_id": 12, "visit_date": "2025-10-03", "bp_sys": 130, "bp_dia": 82},
        {"patient_id": 13, "visit_date": "2025-10-04", "bp_sys": 125, "bp_dia": 84},
        {"patient_id": 14, "visit_date": "2025-10-05", "bp_sys": 126, "bp_dia": 83},
    ]
)

print("[STEP 3] Writing DataFrame to table:", table_name)
with engine.begin() as conn:
    df.to_sql(table_name, con=conn, if_exists="replace", index=False)
print("[OK] Wrote DataFrame to table.")

# --- 4) Read back a quick check ---
print("[STEP 4] Reading back row count ...")
with engine.connect() as conn:
    count_df = pd.read_sql(f"SELECT COUNT(*) AS n_rows FROM `{table_name}`", con=conn)
print(count_df)

elapsed = time.time() - t0
print(f"[DONE] VM path completed in {elapsed:.1f}s at {datetime.utcnow().isoformat()}Z")
