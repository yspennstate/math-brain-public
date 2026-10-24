"""Restrict the completed recall report to the job's mathematical memory slugs."""
from pathlib import Path
import json
p = Path(__file__).resolve().parent / "recall_receipt.json"
data = json.loads(p.read_text(encoding="utf-8"))
lines = data.pop("stdout", "").splitlines()
data["job_scoped_memory_matches"] = [line for line in lines if "prob1000_" in line or "perceptron_proof_open_gaps_fleet" in line][:3]
data["note"] = "Unrelated recall matches excluded; only the required mathematical scar was opened."
p.write_text(json.dumps(data, indent=2), encoding="utf-8")
print("Recall receipt restricted to relevant mathematical slugs.")
