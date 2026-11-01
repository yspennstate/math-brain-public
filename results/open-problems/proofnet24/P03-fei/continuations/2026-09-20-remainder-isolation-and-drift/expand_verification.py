#!/usr/bin/env python3
"""Expand the exact factored rationals in the archived execution output.
No evaluation of untrusted code is used. Output bytes are SHA-256 checked.
"""
from fractions import Fraction
from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parent
archive = json.loads((root / "verification.compact.json").read_text())
if archive["encoding"] != "lossless-tribes-rational-formula-v1":
    raise ValueError("Unsupported encoding")
data = archive["data"]
for row in data["transitive_drift"]["rows"]:
    formula = row["ratio_lower"]
    if formula["exact_formula"] != "(N-2)*((N-1)/N)^(N-3)" or formula["N"] != row["N"]:
        raise ValueError("Unexpected formula")
    N = row["N"]
    if not isinstance(N, int) or not 4 <= N <= 1024:
        raise ValueError("Out-of-range parameter")
    row["ratio_lower"] = str((N-2) * Fraction(N-1, N)**(N-3))
text = (json.dumps(data, indent=2) + "\n").encode()
if hashlib.sha256(text).hexdigest() != archive["decoded_sha256"]:
    raise ValueError("Decoded output does not match the executed source")
(root / "verification.json").write_bytes(text)
print("Restored verified execution output:", archive["decoded_sha256"])
