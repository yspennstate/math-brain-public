"""Bounded, read-only exact-ID fallback proposed after deliberate recall times out.

No writes, model loads, index rebuilds, tests, or automatic theorem promotion.
The caller decides the deadline and records the returned provenance.
"""
import argparse
import json
import re
import subprocess
import time
from pathlib import Path


def exact_id_fallback(problem_id, export_dir, limit=3, timeout=10):
    if not re.fullmatch(r"C[0-9]{4}", problem_id):
        raise ValueError("only an exact C-number is allowed")
    if not 1 <= limit <= 5 or not 0 < timeout <= 60:
        raise ValueError("bounded limit and timeout required")
    path = Path(export_dir) / "nodes.jsonl"
    started = time.perf_counter()
    try:
        result = subprocess.run(
            ["rg", "-n", "-m", str(limit), "-e", rf"\b{problem_id}\b", str(path)],
            capture_output=True,
            encoding="utf-8",
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {"status": "abstain_timeout", "seconds": time.perf_counter() - started, "rows": []}
    if result.returncode not in (0, 1):
        return {"status": "abstain_error", "seconds": time.perf_counter() - started, "rows": [], "error": result.stderr[:500]}
    rows = []
    for line in result.stdout.splitlines():
        number, raw = line.split(":", 1)
        node = json.loads(raw)
        rows.append({"source_path": str(path), "source_line": int(number), "node": node})
    return {
        "status": "retrieved_unreviewed" if rows else "abstain_no_exact_id",
        "seconds": time.perf_counter() - started,
        "problem_id": problem_id,
        "rows": rows,
        "proof_status": "unchanged; retrieval is not source verification or mathematical proof",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem_id")
    parser.add_argument("--export-dir", default="~/math-brain-build/export/population")
    parser.add_argument("--timeout", type=float, default=10)
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(exact_id_fallback(args.problem_id, args.export_dir, args.limit, args.timeout), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
