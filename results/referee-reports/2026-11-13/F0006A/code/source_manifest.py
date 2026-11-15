#!/usr/bin/env python3
"""Extract local PDFs and record their hashes; no network or external writes."""
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))

urls = {
    "vu_2005.02797.pdf": "https://arxiv.org/pdf/2005.02797",
    "shah_2006.04701.pdf": "https://arxiv.org/pdf/2006.04701",
    "alon_vu_anti_hadamard.pdf": "https://web.math.princeton.edu/~nalon/PDFS/av1.pdf",
}
manifest = []
for name, url in urls.items():
    p = ROOT / "sources" / name
    reader = PdfReader(p)
    extracted = "\n\n".join(f"PAGE {i+1}\n{page.extract_text()}"
                              for i, page in enumerate(reader.pages))
    p.with_suffix(".txt").write_text(extracted)
    manifest.append({"filename": name, "url": url, "pages": len(reader.pages),
                     "bytes": p.stat().st_size,
                     "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})

(ROOT / "data" / "source_manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
lines = ["# Sources", "", "Accessed 13 November 2026. All URLs below are primary author, publisher, arXiv, or OEIS sources.", "",
         "| Local PDF | Source | Pages | SHA-256 |", "|---|---|---:|---|"]
for entry in manifest:
    lines.append(f'| [{entry["filename"]}]({entry["filename"]}) | [{entry["url"]}]({entry["url"]}) | '
                 f'{entry["pages"]} | {entry["sha256"]} |')
lines += ["", "The .txt files contain pypdf extractions of the corresponding PDFs.", "",
          "Shitov's *The range of 0-1 determinants is large* (2025), Theorem 1, was read in the web PDF reader:", "",
          "- Author record: https://www.researchgate.net/publication/397595060_The_range_of_0-1_determinants_is_large",
          "- Primary PDF: https://www.researchgate.net/profile/Yaroslav-Shitov/publication/397595060_The_range_of_0-1_determinants_is_large/links/691689a59d514a24b4323683/The-range-of-0-1-determinants-is-large.pdf",
          "- DOI: https://doi.org/10.13140/RG.2.2.32216.35842",
          "- Upload date recorded by the author page: 14 November 2025.",
          "- Status recorded by the page: Preprint. No refereed publication was verified.",
          "- Shell PDF/download requests, including a browser User-Agent request, returned HTTP 403. No local PDF is represented as downloaded.",
          "- `shitov_primary_web_extract.txt` retains proof passages from the primary PDF reader.",
          "- `spectrum_and_theorem_web_extract.txt` retains Theorem 1, proof passages, references, and OEIS A089472/A013588 entries.",
          "- `random_determinant_literature_web_extract.txt` retains the arXiv records used to distinguish limiting laws, singularity, cokernels, and anticoncentration.",
          "", "The web extracts are reader output, not clean transcriptions; flattened exponents and floor/ceiling symbols must be interpreted with the formulas in REPORT.md.",
          "", "Additional primary references are linked directly in REPORT.md. The search scope and stopping decision are in LOG.md."]
(ROOT / "sources" / "MANIFEST.md").write_text("\n".join(lines)+"\n")
print(json.dumps(manifest, indent=2))
