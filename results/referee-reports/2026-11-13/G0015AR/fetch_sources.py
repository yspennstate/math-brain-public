"""Independent source retrieval. PDFs exist only as bytes in memory."""
import concurrent.futures
import ctypes
import datetime
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "sources"
JOBS = {
    "kumar_duddala_2608.21125v1": "https://arxiv.org/pdf/2608.21125v1",
    "companion_2608.15987v1": "https://arxiv.org/pdf/2608.15987v1",
    "miermont_2008": "https://www.numdam.org/article/AIHPB_2008__44_6_1128_0.pdf",
    "deraphelis_1405.3916v3": "https://arxiv.org/pdf/1405.3916v3",
    "addario_berry_et_al_2507.23241v2": "https://arxiv.org/pdf/2507.23241v2",
    "foutel_rodier_2412.16035v1": "https://arxiv.org/pdf/2412.16035v1",
    "horton_powell_2601.05906v2": "https://arxiv.org/pdf/2601.05906v2",
    "stephenson_1412.6911": "https://arxiv.org/pdf/1412.6911",
    "haas_miermont_1003.3632": "https://arxiv.org/pdf/1003.3632",
}


def fetch(item):
    name, url = item
    raw = urllib.request.urlopen(url, timeout=55).read()
    if not raw.startswith(b"%PDF"):
        raise ValueError(f"Not a PDF: {url}")
    converted = subprocess.run(
        ["pdftotext", "-layout", "-", "-"], input=raw, capture_output=True, check=True
    ).stdout
    (SOURCES / (name + ".txt")).write_bytes(converted)
    return {"name": name, "url": url, "retrieved_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "binary_sha256": hashlib.sha256(raw).hexdigest(),
            "text_sha256": hashlib.sha256(converted).hexdigest(),
            "pages": converted.count(b"\f"), "pdf_saved": False}


if __name__ == "__main__":
    # One I/O worker and at most one conversion child, within the resource cap.
    libc = ctypes.CDLL(None, use_errno=True)
    ctypes.set_errno(0)
    priority = libc.getpriority(0, 0)
    if ctypes.get_errno():
        raise OSError(ctypes.get_errno(), "getpriority")
    if priority < 10 and libc.setpriority(0, 0, 10):
        raise OSError(ctypes.get_errno(), "setpriority")
    assert libc.getpriority(0, 0) >= 10
    SOURCES.mkdir(exist_ok=True)
    records = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        futures = {pool.submit(fetch, item): item for item in JOBS.items()}
        for future in concurrent.futures.as_completed(futures):
            name, url = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {"name": name, "url": url, "error": str(exc)}
            records.append(result)
            print(json.dumps(result), flush=True)
    (ROOT / "source_manifest.json").write_text(json.dumps(records, indent=2) + "\n")
    try:
        raw = urllib.request.urlopen("https://arxiv.org/src/2608.21125v1", timeout=55).read()
        pieces = []
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as archive:
            for member in archive.getmembers():
                if member.isfile() and member.name.endswith((".tex", ".bbl")):
                    pieces.append("% FILE: " + member.name + "\n" + archive.extractfile(member).read().decode())
        (SOURCES / "kumar_duddala_original_tex.txt").write_text("\n".join(pieces))
        print("Original TeX retrieved as plain text", flush=True)
    except Exception as exc:
        print("TeX unavailable:", exc, flush=True)
