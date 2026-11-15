"""Fetch a paper and retain plain text only; PDF bytes never enter a disk file."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("name")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = root / "sources" / args.name
    if output.suffix != ".txt" or output.parent != root / "sources":
        raise ValueError("Output must be a simple .txt filename")
    output.parent.mkdir(exist_ok=True)
    response = requests.get(args.url, timeout=90)
    response.raise_for_status()
    body = response.content
    if len(body) > 40_000_000:
        raise ValueError("Source exceeds size limit")
    if body.startswith(b"%PDF"):
        result = subprocess.run(["pdftotext", "-layout", "-", "-"],
                                input=body, capture_output=True, check=True)
        text = result.stdout.decode("utf-8")
    else:
        raise ValueError("Expected PDF response; nothing saved")
    output.write_text(text)
    metadata = dict(url=args.url, retrieved=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                    source_sha256=hashlib.sha256(body).hexdigest(),
                    text_sha256=hashlib.sha256(text.encode()).hexdigest(),
                    pages=len(text.split("\f")) - int(text.endswith("\f")))
    output.with_suffix(".metadata.txt").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(dict(file=str(output), **metadata)))


if __name__ == "__main__":
    main()
