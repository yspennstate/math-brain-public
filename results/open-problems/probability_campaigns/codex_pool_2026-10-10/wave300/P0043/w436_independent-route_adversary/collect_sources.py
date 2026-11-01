"""Fetch only the public primary references named in this packet; no live writes."""
from pathlib import Path
from urllib.request import Request, urlopen
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
SOURCES = {
    "book": ("https://rdlyons.pages.iu.edu/prbtree/book_pb.pdf", "lyons_peres_pb_2026.pdf", 24_000_000),
    "paper2026": ("https://raw.githubusercontent.com/openai/math/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf", "critical_quasitransitive_20260924.pdf", 8_000_000),
    "comparator": ("https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalPercolation.lean", "CriticalPercolation.lean", 300_000),
    "doc213": ("https://raw.githubusercontent.com/openai/math/main/lean/docs/213.md", "doc213.md", 100_000),
    "hutchcroft2016": ("https://arxiv.org/pdf/1605.05301", "hutchcroft2016.pdf", 2_000_000),
}

def main():
    folder = ROOT / "sources"
    folder.mkdir(exist_ok=True)
    for key in sys.argv[1:]:
        url, name, limit = SOURCES[key]
        target = folder / name
        row = {"key": key, "url": url, "file": str(target.relative_to(ROOT)), "checked_at_utc": datetime.now(timezone.utc).isoformat()}
        try:
            with urlopen(Request(url, headers={"User-Agent": "ProbabilitySourceAudit/1.0"}), timeout=35) as response:
                data = response.read(limit + 1)
            if len(data) > limit:
                raise ValueError("source exceeds the explicit byte cap")
            if name.endswith(".pdf") and not data.startswith(b"%PDF"):
                raise ValueError("expected PDF header")
            target.write_bytes(data)
            row.update(status="fetched", bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        except Exception as exc:
            row.update(status="fetch_failed", error=f"{type(exc).__name__}: {exc}")
        with (ROOT / "SOURCE_FETCHES.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(json.dumps(row, ensure_ascii=False), flush=True)

if __name__ == "__main__":
    main()
