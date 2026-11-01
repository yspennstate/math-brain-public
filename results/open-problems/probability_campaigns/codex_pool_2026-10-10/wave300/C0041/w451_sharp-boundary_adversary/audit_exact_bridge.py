"""Independent exact two-site check of w450 L4; no Lean certificate."""
from fractions import Fraction as F
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import time

root = Path(__file__).resolve().parent
start = time.monotonic()
now = datetime.now(timezone.utc)
gate = {"purpose": "Independent exact audit of the signed finite-domain Green bridge", "created_at": now.isoformat(), "expires_at": (now + timedelta(minutes=10)).isoformat(), "max_wall_seconds": 10, "max_environments": 4, "matrix_dimension": 2, "gpu": False, "random_simulation": False}
(root / "AUDIT_COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")
theta = F(51, 100)
kernels = {"+": [F(9, 20), F(1, 20), F(1, 4), F(1, 4)], "-": [F(1, 20), F(9, 20), F(1, 4), F(1, 4)]}
weights = {"+": theta, "-": 1 - theta}
denominator = F(0)
numerator = F(0)
rows = []
for s, p in kernels.items():
    for t, q in kernels.items():
        # Independently invert I-Q for transient states 0,-e1.
        matrix = [[F(1), -p[1]], [-q[0], F(1)]]
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        green = matrix[1][1] / determinant
        probability = weights[s] * weights[t]
        drift = p[0] - p[1]
        denominator += probability * green
        numerator += probability * green * drift
        rows.append({"types": s + t, "Green00": str(green), "probability": str(probability), "directional_drift": str(drift)})
raw_drift = sum(weights[s] * (p[0] - p[1]) for s, p in kernels.items())
assert raw_drift == F(1, 125)
assert numerator < 0 and denominator > 0
assert [r["Green00"] for r in rows] == ["400/391", "400/399", "400/319", "400/391"]
receipt = {"command": "python -X utf8 ~/brain_workers/w451/audit_exact_bridge.py", "result": "PASS", "raw_mean_drift": str(raw_drift), "Green_weighted_numerator": str(numerator), "mean_Green": str(denominator), "Kalikow_drift": str(numerator / denominator), "Kalikow_drift_decimal": float(numerator / denominator), "environment_count": 4, "matrix_rows": rows, "elapsed_seconds": time.monotonic() - start, "verdict": "KEEP w450 L4 as a counterexample to positive-mean-drift => positive finite-domain Kalikow drift; no parent-target counterexample", "formal_check": False}
assert receipt["elapsed_seconds"] <= gate["max_wall_seconds"]
(root / "PEER_AUDIT_MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: receipt[k] for k in ["result", "raw_mean_drift", "Kalikow_drift", "Kalikow_drift_decimal"]}))
