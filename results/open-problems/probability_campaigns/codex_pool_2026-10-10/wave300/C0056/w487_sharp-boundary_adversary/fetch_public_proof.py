"""Fetch the exact public preprint named by the peer's source row."""
import hashlib
import json
import urllib.request
from pathlib import Path

folder = Path(__file__).resolve().parent
url = "https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/paper.tex"
with urllib.request.urlopen(url, timeout=35) as response:
    body = response.read(2_000_001)
if len(body)>2_000_000:
    raise RuntimeError("Public source exceeds the scoped two-megabyte cap")
(folder / "PUBLIC_PREPRINT.tex").write_bytes(body)
receipt = {"url":url, "bytes":len(body), "sha256":hashlib.sha256(body).hexdigest(),
           "mathematical_verdict":"not established by this receipt"}
(folder / "PUBLIC_PREPRINT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt))
