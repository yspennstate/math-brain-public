"""Download mathematical sources and retain extracted text only.

Run with: python3 code/fetch_sources.py
PDF bytes exist only in memory and are passed to pdftotext on stdin.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request

os.environ.update({k: "1" for k in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")})
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("chatterjee_0810.4221v2.txt", "https://arxiv.org/pdf/0810.4221v2"),
    ("ding_eldan_zhai_1311.5592v2.txt", "https://arxiv.org/pdf/1311.5592v2"),
]

def main():
    target = ROOT / "sources"
    target.mkdir(exist_ok=True)
    manifest = []
    for filename, url in SOURCES:
        request = urllib.request.Request(url, headers={"User-Agent": "C0122 literature audit"})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = response.read(20_000_001)
                final_url = response.url
            if len(payload) > 20_000_000:
                raise ValueError("Source exceeds 20 MB limit")
            if not payload.startswith(b"%PDF"):
                raise ValueError("Expected a PDF response")
            result = subprocess.run(["pdftotext", "-layout", "-", "-"],
                                    input=payload, capture_output=True, check=True)
            (target / filename).write_bytes(result.stdout)
            manifest.append({"file": filename, "requested_url": url,
                             "final_url": final_url,
                             "pdf_bytes": len(payload),
                             "text_sha256": hashlib.sha256(result.stdout).hexdigest()})
            print(filename, len(result.stdout), "text bytes", flush=True)
        except Exception as error:
            manifest.append({"file": filename, "requested_url": url, "error": str(error)})
            print(filename, type(error).__name__, str(error), flush=True)
        (target / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

if __name__ == "__main__":
    main()
