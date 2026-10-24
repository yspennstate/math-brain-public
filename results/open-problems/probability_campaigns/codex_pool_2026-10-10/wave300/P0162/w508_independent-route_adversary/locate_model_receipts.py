"""Read target identities only; no credential/profile reads or model self-attestation."""
import json
import os
import sqlite3
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
con = sqlite3.connect("file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro", uri=True, timeout=2)
columns = [r[1] for r in con.execute("PRAGMA table_info(agents)")]
fields = [x for x in ("agent_id", "runtime", "session", "session_id", "native_session_id") if x in columns]
rows = [dict(zip(fields, row)) for row in con.execute(
    "SELECT " + ",".join(fields) + " FROM agents WHERE agent_id IN (?,?)", ("w508", "w509"))]
con.close()
thread = os.environ.get("CODEX_THREAD_ID", "")
codex_root = Path("~/.codex-img-acc2")
date_root = codex_root / "sessions/2026/10/10"
transcripts = []
if thread and date_root.is_dir():
    found = subprocess.run(["rg", "--files", str(date_root), "-g", "*" + thread + "*.jsonl"],
                           capture_output=True, text=True, timeout=20)
    transcripts = found.stdout.splitlines()
receipt = {"author_thread_id":thread, "mesh_identity_rows":rows,
           "author_transcript_candidates":transcripts,
           "requested_or_registration_model_is_served_evidence":False}
(root / "MODEL_RECEIPT_LOCATOR.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt))
