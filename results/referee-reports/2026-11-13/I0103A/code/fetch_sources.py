#!/usr/bin/env python3
"""Save arXiv metadata and PDF-to-text output; never write a PDF to disk."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
ROOT = Path(__file__).resolve().parents[1]
assert Path.cwd().resolve() == ROOT
SOURCES = ROOT / "sources"
SOURCES.mkdir(exist_ok=True)

def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "I0103 research source verification"})
    with urllib.request.urlopen(request, timeout=90) as response:
        return response.read(), response.geturl()

def fetch(identifier):
    record = {"id": identifier, "retrieved_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        body, url = get("https://arxiv.org/abs/" + identifier)
        # Retained as plain UTF-8 text (HTML markup included for metadata provenance).
        (SOURCES / (identifier + "_metadata.txt")).write_text(body.decode(), encoding="utf-8")
        record["metadata_url"] = url
        body, url = get("https://arxiv.org/pdf/" + identifier)
        if not body.startswith(b"%PDF"):
            raise ValueError("PDF endpoint did not return PDF bytes")
        record["pdf_url"] = url
        record["pdf_sha256"] = hashlib.sha256(body).hexdigest()
        result = subprocess.run(["pdftotext", "-layout", "-", "-"], input=body, capture_output=True, check=True)
        (SOURCES / (identifier + ".txt")).write_bytes(result.stdout)
        record["text_sha256"] = hashlib.sha256(result.stdout).hexdigest()
        record["pages"] = result.stdout.count(b"\x0c")
        print(json.dumps(record), flush=True)
    except Exception as error:
        record["error"] = str(error)
        print(json.dumps(record), flush=True)
    manifest = ROOT / "data" / "source_manifest.jsonl"
    manifest.parent.mkdir(exist_ok=True)
    with manifest.open("a") as output:
        output.write(json.dumps(record) + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="+")
    args = parser.parse_args()
    for identifier in args.ids:
        fetch(identifier)
