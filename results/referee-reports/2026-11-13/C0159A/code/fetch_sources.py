"""Fetch primary sources and retain plain text only; PDF bytes stay in memory."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import urllib.request

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
ROOT = Path(__file__).resolve().parents[1]

def fetch(url, name):
    request = urllib.request.Request(url, headers={"User-Agent": "C0159-literature-audit/1.0"})
    with urllib.request.urlopen(request, timeout=75) as response:
        blob = response.read(30_000_000)
        actual_url = response.url
    # Both input and output use pipes. No temporary PDF or images are created.
    result = subprocess.run(["pdftotext", "-layout", "-", "-"], input=blob,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    pages = result.stdout.decode("utf-8").split("\f")
    if not pages[-1].strip():
        pages.pop()
    out = [f"SOURCE: {url}\nRETRIEVED: {actual_url}\nPDF_SHA256: {hashlib.sha256(blob).hexdigest()}\n"]
    for page, content in enumerate(pages, 1):
        out.append(f"\n\n===== PDF PAGE {page} =====\n\n{content}")
    target = ROOT / "sources" / (name + ".txt")
    target.parent.mkdir(exist_ok=True)
    target.write_text("".join(out).replace("\x00", ""))
    print(json.dumps({"file": str(target.relative_to(ROOT)), "pages": len(pages), "url": actual_url}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("name")
    args = parser.parse_args()
    fetch(args.url, args.name)
