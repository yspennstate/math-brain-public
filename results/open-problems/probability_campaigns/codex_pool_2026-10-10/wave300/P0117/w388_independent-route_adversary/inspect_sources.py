"""Targeted read-only source inspection; all output is inside w388."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sqlite3
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["store", "download"])
args = parser.parse_args()

if args.mode == "store":
    path = "~/math-brain-build/local/population/brain.sqlite3"
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=5)
    con.execute("PRAGMA query_only=ON")
    tables = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    schemas = {name: con.execute(f'PRAGMA table_info("{name}")').fetchall()
               for (name,) in tables if name in {"cards", "nodes", "sources", "entries", "relations", "edges"}}
    rows = con.execute("SELECT id,title,body,metadata_json FROM nodes WHERE title IN (?,?) OR title LIKE ? LIMIT 8", (
        "Open problem: Absence of bi-infinite geodesics in planar iid FPP",
        "Attempt on Absence of bi-infinite geodesics in planar iid FPP",
        "%No bigeodesics in planar first-passage%",
    )).fetchall()
    result = {"tables": tables, "schemas": schemas}
    target = [{"id": i, "title": t, "body": b, "metadata_json": m} for i, t, b, m in rows]
    (ROOT / "store_target_rows.json").write_text(json.dumps(target, indent=2), encoding="utf-8")
    (ROOT / "store_schema.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"nodes_schema": schemas.get("nodes"), "target_rows": target}, indent=2))
else:
    dest = ROOT / "sources"
    dest.mkdir(exist_ok=True)
    sources = [
        ("no_bigeodesics_20260924.pdf", "https://raw.githubusercontent.com/openai/math/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf"),
        ("ahlberg_hanson_hoffman_2208.11576.pdf", "https://arxiv.org/pdf/2208.11576"),
    ]
    receipts = []
    for name, url in sources:
        receipt = {"filename": name, "url": url}
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Probability-source-check/1.0"})
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read(2_000_001)
            if len(data) > 2_000_000 or not data.startswith(b"%PDF"):
                raise ValueError("not a PDF within the two-megabyte source gate")
            pdf = dest / name
            pdf.write_bytes(data)
            receipt.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), downloaded=True)
            extractor = None
            if importlib.util.find_spec("pypdf"):
                from pypdf import PdfReader
                content = "\n".join(f"PAGE {i+1}\n{page.extract_text()}" for i, page in enumerate(PdfReader(pdf).pages))
                extractor = "pypdf"
            elif importlib.util.find_spec("fitz"):
                import fitz
                with fitz.open(pdf) as doc:
                    content = "\n".join(f"PAGE {i+1}\n{page.get_text()}" for i, page in enumerate(doc))
                extractor = "fitz"
            elif shutil.which("pdftotext"):
                txt = pdf.with_suffix(".txt")
                subprocess.run([shutil.which("pdftotext"), "-layout", str(pdf), str(txt)], timeout=30, check=True)
                content = txt.read_text(encoding="utf-8")
                extractor = "pdftotext"
            if extractor:
                pdf.with_suffix(".txt").write_text(content, encoding="utf-8")
            receipt["extractor"] = extractor
        except Exception as exc:
            receipt.update(downloaded=False, error=f"{type(exc).__name__}: {str(exc)[:300]}")
        receipts.append(receipt)
        (ROOT / "source_download_receipts.json").write_text(json.dumps(receipts, indent=2), encoding="utf-8")
        print(json.dumps(receipt))
