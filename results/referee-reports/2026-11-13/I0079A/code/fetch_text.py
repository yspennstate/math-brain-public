"""Retrieve an arXiv PDF in memory and retain only pdftotext output."""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
(root / "sources").mkdir(exist_ok=True)
(root / "data").mkdir(exist_ok=True)
for ident in sys.argv[1:]:
    url = "https://arxiv.org/pdf/" + ident
    req = urllib.request.Request(url, headers={"User-Agent": "I0079 mathematical literature audit"})
    with urllib.request.urlopen(req, timeout=90) as response:
        raw = response.read(30_000_000)
    if not raw.startswith(b"%PDF"):
        raise ValueError(f"Not a PDF response for {ident}")
    converted = subprocess.run(["pdftotext", "-layout", "-", "-"], input=raw, capture_output=True, check=True).stdout
    name = ident.replace("/", "_")
    target = root / "sources" / (name + ".txt")
    target.write_bytes(converted)
    entry = {"id": ident, "url": url, "retrieved_utc": datetime.now(timezone.utc).isoformat(),
             "pdf_sha256_in_memory": hashlib.sha256(raw).hexdigest(),
             "text_sha256": hashlib.sha256(converted).hexdigest(), "text_bytes": len(converted),
             "pages": len(converted.decode().split("\f")) - 1}
    with (root / "data" / "sources.jsonl").open("a") as f:
        f.write(json.dumps(entry) + "\n")
    print(json.dumps(entry), flush=True)
