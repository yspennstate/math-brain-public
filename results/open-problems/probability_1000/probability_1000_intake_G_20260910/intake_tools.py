"""Intake tooling for the Claude continuation of the 1,000 open probability problems campaign.

Same record schemas as the Codex campaign tree (probability-source.v1, problems.jsonl rows,
probability-attempt.v1). Problem IDs carry the prefix G so the merge into the campaign ledger
can remap them without collision. Raw source bytes live under
Downloads/Probability_1000_intake_G_20260910/sources/<id>/.

    python intake_tools.py fetch --id <id> --url <https url> --kind pdf|html --title "..." --access "..."
    python intake_tools.py snapshot
"""
import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
OUTPUT = Path.home() / "Downloads" / "Probability_1000_intake_G_20260910"


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def append(path, row):
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def records(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def latest(path, key):
    return {row[key]: row for row in records(path)}


def fetch(args):
    import requests
    if not re.fullmatch(r"[a-z0-9_]+", args.id):
        raise ValueError("Source id must be lowercase ASCII letters, numbers, underscores")
    parsed = urlparse(args.url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Source URL must be HTTPS and contain no credentials")
    folder = OUTPUT / "sources" / args.id
    raw = folder / ("source.pdf" if args.kind == "pdf" else "source.html")
    extracted = folder / "text.txt"
    if raw.exists():
        raise FileExistsError("Acquired bytes already exist; use a new version id for changed source")
    row = {"schema": "probability-source.v1", "source_id": args.id, "title": args.title,
           "url": args.url, "kind": args.kind, "acquired_at": now(), "access_evidence": args.access,
           "reading_status": "unread", "statement_validation": "not_started",
           "intake": "G_20260910"}
    try:
        response = requests.get(args.url, timeout=(15, 60), headers={
            "User-Agent": "ProbabilityResearch/1.0 (single-reader academic source verification)"})
        response.raise_for_status()
        payload = response.content
        if len(payload) > 32 * 1024 * 1024:
            raise ValueError("Source exceeds bounded single-file acquisition limit")
        if args.kind == "pdf":
            import fitz
            if not payload.startswith(b"%PDF"):
                raise ValueError("Response is not a PDF")
            document = fitz.open(stream=payload, filetype="pdf")
            plain = "".join(f"\n===== PDF PAGE {i+1} =====\n" + page.get_text()
                            for i, page in enumerate(document))
            row["page_count"] = len(document)
            document.close()
        else:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(payload, "html.parser")
            for unwanted in soup(["script", "style", "nav"]):
                unwanted.decompose()
            plain = soup.get_text("\n", strip=True)
            row["page_count"] = None
        if len(plain.strip()) < 100:
            raise ValueError("Extracted source text is suspiciously short")
        row.update({"http_status": response.status_code, "final_url": response.url,
                    "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest(),
                    "extracted_characters": len(plain),
                    "extracted_sha256": hashlib.sha256(plain.encode()).hexdigest(),
                    "raw_relative_to_downloads": str(raw.relative_to(OUTPUT)).replace("\\", "/"),
                    "text_relative_to_downloads": str(extracted.relative_to(OUTPUT)).replace("\\", "/"),
                    "acquisition_status": "validated_and_extracted"})
        folder.mkdir(parents=True, exist_ok=True)
        raw.write_bytes(payload)
        extracted.write_text(plain, encoding="utf-8", newline="\n")
        append(HERE / "sources.jsonl", row)
        print(json.dumps({k: row[k] for k in ["source_id", "bytes", "page_count", "acquisition_status"]}))
    except Exception as exc:
        row.update({"acquisition_status": "failed", "error_type": type(exc).__name__, "error": str(exc)[:300]})
        append(HERE / "source_failures.jsonl", row)
        print(json.dumps({"source_id": args.id, "status": "failed", "error_type": type(exc).__name__, "error": str(exc)[:200]}))
        raise SystemExit(1)


def snapshot(_args):
    sources = latest(HERE / "sources.jsonl", "source_id")
    problems = latest(HERE / "problems.jsonl", "problem_id")
    attempts = records(HERE / "attempts.jsonl")
    attempted = {a["problem_id"] for a in attempts if a.get("substantive")}
    admitted = [p for p in problems.values() if p.get("admitted")]
    distinct = {p.get("dedup_key", p["problem_id"]) for p in admitted}
    status = {
        "schema": "probability-1000-intake-G.v1",
        "as_of_utc": now(),
        "validated_sources": sum(1 for s in sources.values() if s.get("acquisition_status") == "validated_and_extracted"),
        "admitted_rows": len(admitted),
        "admitted_distinct_problems": len(distinct),
        "attempted_problems": len([p for p in admitted if p["problem_id"] in attempted]),
        "literature_resolved_excluded": sum(1 for p in problems.values() if p.get("current_status") == "resolved_in_literature"),
        "candidate_full_results": sorted(p["problem_id"] for p in admitted if p.get("result_status") == "candidate_full_solution"),
        "candidate_partial_results": sorted(p["problem_id"] for p in admitted if p.get("result_status") in ("partial_result", "candidate_partial_counterexample")),
        "author_checked_original_solutions": 0,
        "independently_reviewed_original_solutions": 0,
    }
    (HERE / "STATUS.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(status, indent=2))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    f = sub.add_parser("fetch")
    f.add_argument("--id", required=True)
    f.add_argument("--url", required=True)
    f.add_argument("--kind", choices=["pdf", "html"], default="pdf")
    f.add_argument("--title", required=True)
    f.add_argument("--access", default="public web")
    f.set_defaults(func=fetch)
    s = sub.add_parser("snapshot")
    s.set_defaults(func=snapshot)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
