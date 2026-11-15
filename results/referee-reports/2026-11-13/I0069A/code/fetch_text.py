"""Fetch a paper as plain text; PDF bytes never touch the filesystem."""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import argparse
import hashlib
import json
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("url")
parser.add_argument("output")
args = parser.parse_args()
request = urllib.request.Request(args.url, headers={"User-Agent": "I0069-research/1.0"})
with urllib.request.urlopen(request, timeout=90) as response:
    blob = response.read()
    final_url = response.url
if blob.startswith(b"%PDF"):
    text = subprocess.run(["pdftotext", "-layout", "-", "-"], input=blob,
                          stdout=subprocess.PIPE, check=True).stdout.decode("utf-8")
    kind = "PDF converted in memory; form feeds preserve page boundaries"
else:
    text = blob.decode("utf-8")
    kind = "text/HTML response"
    if "<html" in text[:4000].lower() or "<!doctype html" in text[:4000].lower():
        raise RuntimeError("Received HTML instead of paper text; no source file saved")
path = Path(args.output)
path.write_text(text)
metadata = {"url": args.url, "final_url": final_url, "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            "source_sha256": hashlib.sha256(blob).hexdigest(), "text_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "bytes_downloaded": len(blob), "characters_saved": len(text), "conversion": kind,
            "pages": len([p for p in text.split("\f") if p.strip()])}
with Path("data/source_manifest.jsonl").open("a") as output:
    output.write(json.dumps({"file": str(path), **metadata}) + "\n")
print(json.dumps({"file": str(path), **metadata}))
