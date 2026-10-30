"""Export a random sample of ingested nodes for cross-agent adversarial QA.

Samples N current nodes from the population store (seeded, reproducible),
writes a review file with id, title, kind, statement, proof text, and source,
plus the exact verdict schema the QA worker must return. The parent ingests
verdicts and quarantines or supersedes bad nodes; the sampler never mutates.

A round's review file is written once. Running the same round again with the
same store and settings reproduces it byte for byte and changes nothing; any
other result is refused, so a rerun cannot erase what a round covered. Earlier
rounds' reviews are excluded from the sample, and a review file that cannot be
read is an error rather than a round that never happened (from an audit of the
QA sampler, 29 Sep 2026).

    python tools/qa_sample.py [N] [ROUND]
"""

from __future__ import annotations

import json
import os
import random
import sys
from pathlib import Path

BUILD_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BUILD_ROOT / "src"))

from math_brain.store import ResearchStore  # noqa: E402

STORE = BUILD_ROOT / "local" / "population" / "brain.sqlite3"
OUT = Path(os.environ.get("MATH_BRAIN_QA_DIR") or BUILD_ROOT.parent / "math-brain-inbox" / "qa")


def reviewed_elsewhere(round_no: int) -> set[str]:
    """Node ids in the reviews of every other round; a review that cannot be read raises."""
    already: set[str] = set()
    for prior in sorted(OUT.glob("review_*.json")):
        if prior.name == f"review_{round_no:03d}.json":
            continue
        try:
            data = json.loads(prior.read_text(encoding="utf-8"))
            already.update(item["node_id"] for item in data["items"])
        except (OSError, ValueError, KeyError, TypeError) as exc:
            raise ValueError(
                f"cannot read {prior.name}: {exc}; fix or move it before sampling"
            ) from exc
    return already


def main(n: int = 25, seed: int = 20260802, round_no: int = 1) -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    with ResearchStore.open_read_only(STORE) as store:
        from math_brain.models import EdgeKind

        superseded = {
            e.target_id for e in store.iter_edges() if e.kind is EdgeKind.SUPERSEDES
        }
        nodes = [x for x in store.iter_nodes() if x.id not in superseded]
    try:
        already = reviewed_elsewhere(round_no)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2
    nodes = [x for x in nodes if x.id not in already]
    rng = random.Random(seed + round_no)
    sample = rng.sample(nodes, min(n, len(nodes)))
    items = []
    for node in sample:
        meta = node.metadata if isinstance(node.metadata, dict) else {}
        items.append(
            {
                "node_id": node.id,
                "title": node.title,
                "kind": str(meta.get("claim_kind") or node.kind),
                "statement": node.body,
                "proof_text": meta.get("proof_text") or None,
                "source_hint": meta.get("source_id") or meta.get("draft") or "",
            }
        )
    review = {
        "instructions": (
            "Adversarial QA of mathematical knowledge nodes. For EACH item return a "
            "verdict object: {node_id, verdict: correct|wrong|imprecise|stub, "
            "problem: null or one sentence naming the exact defect (a missing "
            "hypothesis, a false claim, a truncated statement), fix: null or the "
            "corrected statement}. Judge the STATEMENT text on its own: is it a "
            "true, complete, self-contained mathematical statement as typed (kind "
            "definition/theorem/lemma/concept)? For theorems also judge the proof "
            "sketch: does it prove the right statement, no false steps? Be harsh; "
            "a wrong node poisons live reasoning. Write the verdict array as JSON "
            "to the path named in output_path."
        ),
        "output_path": str(OUT / f"verdicts_{round_no:03d}.json"),
        "items": items,
    }
    text = json.dumps(review, indent=1)
    out_file = OUT / f"review_{round_no:03d}.json"
    if out_file.exists():
        if out_file.read_text(encoding="utf-8") == text:
            print(f"{out_file} already holds this round; unchanged")
            return 0
        print(f"{out_file} already holds a different round {round_no}; choose a new round number",
              file=sys.stderr)
        return 2
    with open(out_file, "x", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {out_file}: {len(items)} items for review")
    return 0


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    rnd = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    raise SystemExit(main(n, round_no=rnd))
