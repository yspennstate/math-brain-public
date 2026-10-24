"""Convert QA verdicts (with required fixes) into a corrections draft bundle.

For every verdict that is not "correct" and carries a fix: emit an entry with
the same logical identity and kind, statement = the referee's fix,
supersedes_existing = true. Theorem/lemma kinds keep the prior proof_text when
the problem was in the statement (the common case for extraction holes); if no
prior proof exists the kind is demoted to concept, honestly. The parent still
reads the generated draft before activation: output is .part.

A verdict for a node the review did not contain is refused, and no bundle is
written: a verdict file can only correct what its round sampled (scheduled audit
account01/B16, B16-R13-QA-SAMPLE-RERUN-ERASES-COVERAGE-011, 29 Sep 2026).

Each correction names the review that produced it: the round from the review's
file name, and the first 16 hex characters of the SHA-256 of the review and of
the verdict file, in its source revision. Until 29 Sep every correction said
"round 3" and "qa-corrected-2026-08-02-r3" whatever it came from, so none could
be traced to its review (scheduled audit account01/B18,
B18-R13-QA-CORRECTION-BUNDLE-UNBOUND-TO-REVIEW-GENERATION-20260929).

    python tools/apply_verdicts.py VERDICTS.json REVIEW.json OUT_NAME
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

BUILD = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BUILD / "src"))

from math_brain.store import ResearchStore  # noqa: E402

STORE = BUILD / "local" / "population" / "brain.sqlite3"
INBOX = Path(os.environ.get("MATH_BRAIN_DRAFT_INBOX")
             or BUILD.parent / "math-brain-inbox" / "claude-mathbrain-build-0802")


def review_provenance(review_path: str, review_bytes: bytes,
                      verdict_bytes: bytes) -> tuple[str, str]:
    """(domain, revision) for the corrections drawn from this review and these verdicts."""
    m = re.fullmatch(r"review_(\d+)\.json", Path(review_path).name)
    round_label = str(int(m.group(1))) if m else "unnumbered"
    review_sha = hashlib.sha256(review_bytes).hexdigest()[:16]
    verdict_sha = hashlib.sha256(verdict_bytes).hexdigest()[:16]
    day = time.strftime("%Y-%m-%d", time.gmtime())
    return (f"QA-corrected (round {round_label}, audit-driven)",
            f"qa-corrected-{day}-r{round_label}-review-{review_sha}-verdicts-{verdict_sha}")


def main(verdicts_path: str, review_path: str, out_name: str) -> int:
    verdict_bytes = Path(verdicts_path).read_bytes()
    review_bytes = Path(review_path).read_bytes()
    verdicts = json.loads(verdict_bytes.decode("utf-8"))
    review = json.loads(review_bytes.decode("utf-8"))
    domain, revision = review_provenance(review_path, review_bytes, verdict_bytes)
    by_id = {item["node_id"]: item for item in review["items"]}
    outside = sorted({str(v.get("node_id")) for v in verdicts} - set(by_id))
    if outside:
        print(f"refused: {len(outside)} verdict(s) name nodes the review did not contain, "
              f"e.g. {outside[:3]}; no bundle written", file=sys.stderr)
        return 2
    entries = []
    skipped = []
    with ResearchStore.open_read_only(STORE) as store:
        for v in verdicts:
            if v["verdict"] == "correct":
                continue
            fix = (v.get("fix") or "").strip()
            if len(fix) < 60:
                skipped.append((v["node_id"], "no-usable-fix"))
                continue
            node = store.get_node(v["node_id"])
            if node is None:
                skipped.append((v["node_id"], "node-missing"))
                continue
            meta = node.metadata
            logical = str(meta.get("logical_id") or "")
            if not logical.startswith("math:"):
                skipped.append((v["node_id"], "no-logical-id"))
                continue
            _, namespace, name = logical.split(":", 2)
            kind = str(meta.get("claim_kind") or "concept")
            proof = str(meta.get("proof_text") or "").strip()
            if kind in ("theorem", "lemma") and not proof:
                kind = "concept"
                proof = ""
            entries.append({
                "key": ("fx-" + name)[:60],
                "namespace": namespace,
                "logical_name": name,
                "kind": kind,
                "supersedes_existing": True,
                "title": node.title,
                "statement": fix,
                "proof_text": proof or None,
                "assumptions": [],
                "domain": domain,
                "source": {
                    "source_id": str(meta.get("source_id") or "qa-correction"),
                    "url": "https://en.wikipedia.org/wiki/" + name.replace("wiki-", "").replace("-", "_"),
                    "revision": revision,
                    "license": "CC-BY-SA-4.0",
                },
            })
    draft = {
        "spec": "mathbrain-draft-v1",
        "author_agent": "claude-mathbrain-build-0802",
        "bundle_slug": out_name,
        "entries": entries,
        "relations": [],
    }
    out = INBOX / f"bundle_{out_name}.part"
    out.write_text(json.dumps(draft, indent=1), encoding="utf-8")
    print(f"wrote {out}: {len(entries)} corrections, {len(skipped)} skipped")
    for nid, why in skipped:
        print("SKIP", nid[:30], why)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
