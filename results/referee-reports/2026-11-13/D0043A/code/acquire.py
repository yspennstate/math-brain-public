"""Download scholarly sources as text, never writing PDF bytes to disk."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def acquire(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "D0043 private mathematical research"})
    with urllib.request.urlopen(req, timeout=90) as response:
        content = response.read()
    if not content.startswith(b"%PDF"):
        raise ValueError(f"Not PDF content: {url}")
    converted = subprocess.run(["pdftotext", "-layout", "-", "-"], input=content,
                               capture_output=True, check=True).stdout.decode("utf-8")
    path = ROOT / "sources" / f"{name}.txt"
    path.parent.mkdir(exist_ok=True)
    path.write_text(converted)
    metadata = {"url": url, "pdf_sha256_not_retained": hashlib.sha256(content).hexdigest(),
                "text_sha256": hashlib.sha256(converted.encode()).hexdigest(),
                "pages": converted.count("\f")}
    manifest = ROOT / "sources" / "manifest.json"
    entries = json.loads(manifest.read_text()) if manifest.exists() else {}
    entries[name] = metadata
    manifest.write_text(json.dumps(entries, indent=2) + "\n")
    print(name, metadata["pages"], "pages", len(converted), "characters", flush=True)

if __name__ == "__main__":
    import sys
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
    for item in sys.argv[1:]:
        name, url = item.split("=", 1)
        try:
            acquire(name, url)
        except Exception as exc:
            print(name, type(exc).__name__, str(exc), flush=True)
