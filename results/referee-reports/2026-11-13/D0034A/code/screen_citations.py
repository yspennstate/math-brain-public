"""Download and screen OpenAlex-indexed citations; this is not a full-text audit.

Run from the workspace: python3 code/screen_citations.py
Only standard-library modules are used. Output stays in data/.
"""
import json
import os
import resource
from pathlib import Path
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://api.openalex.org/works"
TARGET = "W2100967164"


def abstract_text(index):
    if not index:
        return ""
    pairs = [(position, word) for word, positions in index.items() for position in positions]
    return " ".join(word for _, word in sorted(pairs))


def main():
    data = ROOT / "data"
    works = []
    meta = None
    for page in range(1, 21):
        params = {
            "filter": f"cites:{TARGET},from_publication_date:2005-01-01,to_publication_date:2026-11-13",
            "per-page": 200,
            "page": page,
            "select": "id,doi,title,publication_year,abstract_inverted_index,primary_location",
        }
        url = BASE + "?" + urllib.parse.urlencode(params)
        try:
            saved = data / f"citations_page_{page:02}.json"
            if saved.exists():
                batch = json.loads(saved.read_text())
            else:
                with urllib.request.urlopen(url, timeout=25) as response:
                    batch = json.load(response)
        except Exception as exc:
            (data / "citation_screen_error.txt").write_text(str(exc) + "\n")
            break
        (data / f"citations_page_{page:02}.json").write_text(json.dumps(batch, ensure_ascii=False))
        meta = batch.get("meta", {})
        works.extend(batch.get("results", []))
        print(f"Page {page}: total indexed={meta.get('count')}, fetched={len(works)}", flush=True)
        if not batch.get("results") or len(works) >= meta.get("count", float("inf")):
            break
    ranked = []
    for work in works:
        abstract = abstract_text(work.get("abstract_inverted_index"))
        text = (work.get("title", "") + " " + abstract).lower()
        score = sum(weight * (phrase in text) for phrase, weight in [
            ("harris", 3), ("representation", 2), ("representability", 4),
            ("instantaneous function", 8), ("one-dependent", 3), ("1-dependent", 3),
            ("finitely dependent", 3), ("hidden markov", 2), ("question 6", 8),
        ])
        if score:
            ranked.append({"score": score, "title": work["title"], "year": work["publication_year"],
                           "id": work["id"], "doi": work["doi"], "abstract": abstract,
                           "location": work.get("primary_location")})
    result = {"target": TARGET, "scope": "2005-01-01 through 2026-11-13", "fetched": len(works),
              "indexed_total": (meta or {}).get("count"),
              "with_abstract": sum(bool(w.get("abstract_inverted_index")) for w in works),
              "nice": os.getpriority(os.PRIO_PROCESS, 0),
              "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "warning": "Keyword screening of indexed titles/abstracts only; not exhaustive full text or all literature.",
              "candidates": sorted(ranked, key=lambda item: (-item["score"], -item["year"]))}
    (data / "citation_screen.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "candidates"}))
    for item in result["candidates"][:25]:
        print(item["score"], item["year"], item["title"], item["doi"])


if __name__ == "__main__":
    main()
