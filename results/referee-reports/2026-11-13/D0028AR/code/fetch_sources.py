"""Fetch scholarly PDFs in memory and persist only their extracted plain text.

No claim_files code is imported or executed. Run from the audit root.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
                  VECLIB_MAXIMUM_THREADS="1", NUMEXPR_NUM_THREADS="1")

def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Independent mathematical referee source retrieval"})
    with urllib.request.urlopen(req, timeout=60) as response:
        content = response.read(25_000_001)
        final_url = response.url
    if len(content) > 25_000_000:
        raise ValueError("source exceeds 25 MB cap")
    if content.startswith(b"%PDF"):
        proc = subprocess.run(["pdftotext", "-layout", "-", "-"], input=content,
                              capture_output=True, check=True, timeout=45)
        plain = proc.stdout
        kind = "PDF bytes held in memory; pdftotext -layout - -"
    else:
        raise ValueError("Expected a PDF; no HTML saved as a source text")
    target = ROOT / "sources" / (name + ".txt")
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(plain)
    return {"name": name, "url": url, "final_url": final_url,
            "source_sha256": hashlib.sha256(content).hexdigest(),
            "text_sha256": hashlib.sha256(plain).hexdigest(),
            "bytes_text": len(plain), "method": kind}

if __name__ == "__main__":
    name, url = sys.argv[1:]
    try:
        result = fetch(name, url)
    except Exception as exc:
        result = {"name": name, "url": url, "error": str(exc)}
    (ROOT / "data").mkdir(exist_ok=True)
    with (ROOT / "data" / "source_manifest.jsonl").open("a") as out:
        out.write(json.dumps(result) + "\n")
    print(json.dumps(result))
    sys.exit(1 if "error" in result else 0)
