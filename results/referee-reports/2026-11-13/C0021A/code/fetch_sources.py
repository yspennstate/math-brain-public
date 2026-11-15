#!/usr/bin/env python3
"""Fetch papers into memory and save text extracts only (no PDF/page images)."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("garban_steif_book", "https://math.univ-lyon1.fr/~garban/Fichiers/book.pdf"),
    ("magniez_et_al_2016", "https://www.irif.fr/~magniez/PAPIERS/mnsstx-rsa16.pdf"),
    ("leonardos_2012_corrected", "https://eccc.weizmann.ac.il/report/2012/099/revision/1/download"),
    ("goos_jayram_2016", "https://drops.dagstuhl.de/storage/00lipics/lipics-vol050-ccc2016/LIPIcs.CCC.2016.5/LIPIcs.CCC.2016.5.pdf"),
    ("osss_2005", "https://www.cs.columbia.edu/~rocco/Public/focs05osss.pdf"),
    ("odonnell_servedio_2007", "https://www.cs.columbia.edu/~rocco/Public/15-os.pdf"),
    ("peres_schramm_sheffield_wilson", "https://arxiv.org/pdf/math/0508580"),
    ("leonardos_2023", "https://arxiv.org/pdf/2203.17168"),
    ("al_dhalaan_ben_david_2026", "https://arxiv.org/pdf/2601.08073"),
    ("peres_lecture_2009", "https://sites.math.washington.edu/~eyal/523A/lec/lec-6.pdf"),
]


def main():
    manifest = ROOT / "sources/manifest.json"
    records = json.loads(manifest.read_text()) if manifest.exists() else []
    for name, url in SOURCES:
        path = ROOT / "sources" / (name + ".txt")
        if path.exists():
            continue
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "C0021 source audit"})
            raw = urllib.request.urlopen(request, timeout=30).read()
            result = subprocess.run(["pdftotext", "-layout", "-", "-"], input=raw,
                                    capture_output=True, check=True)
            path.write_bytes(result.stdout)
            records.append(dict(name=name, url=url,
                pdf_sha256=hashlib.sha256(raw).hexdigest(),
                text_sha256=hashlib.sha256(result.stdout).hexdigest(),
                text_bytes=len(result.stdout),
                retrieved=datetime.datetime.now().astimezone().isoformat()))
            manifest.write_text(json.dumps(records, indent=2) + "\n")
            print(name, len(result.stdout), flush=True)
        except Exception as error:
            print(name, type(error).__name__, str(error), flush=True)


if __name__ == "__main__":
    main()
