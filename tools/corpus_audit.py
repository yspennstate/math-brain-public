"""Full-corpus integrity audit, end to end. Read-only on the store.

Checks every CURRENT node (superseded excluded):
  A. statement health via the activation gate's own rules (stub detection);
  B. theorem/lemma kinds carry a nonempty proof_text;
  C. graph: non-SUPERSEDES edges touching retired nodes; depends_on cycles;
  D. per-shelf retrieval probes with expected-hit assertions;
  E. injection latency at current size.
Writes an audit report and a flagged-node worklist that becomes QA round 3.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

BUILD = Path(r"~\math-brain-build")
sys.path.insert(0, str(BUILD / "src"))
sys.path.insert(0, str(BUILD / "tools"))

import re  # noqa: E402

from math_brain.models import EdgeKind  # noqa: E402
from math_brain.retrieval import retrieve  # noqa: E402
from math_brain.store import ResearchStore  # noqa: E402


def store_body_health(body: str) -> str | None:
    """Hole detection for STORE bodies (statement + assumptions concatenated,
    so end-anchored sentence rules do not apply). Flags only real damage."""
    s = (body or "").strip()
    if len(s) < 60:
        return "too-short"
    if "." not in s:
        return "no-sentence-at-all"
    if re.search(r"[a-z]\s+,(?!\.\.)|[a-z]\s+;|[a-z]\s+\.(?!\.)(?!\s+[a-z0-9(])", s):
        # "x ... x" / "x_1 ,..., x_n" ellipses and infix dot products
        # ("omega . k") are legitimate; a stranded dot before a capital or
        # sentence end is stripping damage.
        return "hole-space-before-punctuation"
    if re.search(r"\b(one has|reads|denoted by|given by|defined as|defined by|equal to)\s*(where|[,.])", s, re.I):
        return "hole-missing-formula"
    # "to be" / "to have" are grammatical infinitives, not stripping damage;
    # "to" only flags when paired with a verb form ungrammatical after it.
    if re.search(r"\b(in|of|from|over|by|with)\s+(has|is|are|was|be|can|converges|holds|satisfies)\b", s) \
            or re.search(r"\bto\s+(has|is|are|was|can|converges|holds|satisfies)\b", s):
        return "hole-preposition-verb-gap"
    return None

STORE = BUILD / "local" / "population" / "brain.sqlite3"
OUT_DIR = Path(r"~\math-brain-inbox\qa")
REPORT = BUILD / "local" / "population" / f"corpus_audit_{time.strftime('%Y%m%dT%H%M%S')}.json"

# Referee-cleared false positives (QA round 3 judged these correct as written);
# the mechanical flag patterns over-match their phrasing. Skip in future audits.
CLEARED_LOGICALS = {
    "math:harvest.wikipedia:wiki-nakayama-s-lemma",
    "math:harvest.wikipedia:wiki-riemann-hypothesis",
    "math:harvest.wikipedia:wiki-four-color-theorem",
    "math:harvest.wikipedia:wiki-well-ordering-theorem",
    "math:number-theory.elementary:bezout-identity",
    "math:number-theory.elementary:infinitude-of-primes",
    "math:harvest.wikipedia:wiki-brouwer-degree",
    "math:harvest.wikipedia:wiki-invariance-of-domain",
    # QA-4: "not known to be NP-complete" trips the preposition-verb pattern;
    # the statement is correct as written.
    "math:logic.computability:complexity-class-np",
}

# QA-4 defect class: harvest ledes that only point at a named result (history,
# attribution, "describes the connection between...") without asserting any
# mathematics. Grammatical, so the hole patterns pass them; a theorem-ish
# title with no assertion marker in the body is the discriminator.
TITLE_ASSERTIVE_RE = re.compile(
    r"\b(theorem|lemma|inequality|formula|law|principle|identity|rule|paradox|"
    r"conjecture|hypothesis)\b",
    re.I,
)
CONTENT_MARKER_RE = re.compile(
    r"[=<>]|\bif\b|\bthen\b|\bfor (?:all|every|each)\b|\bthere (?:is|are|exists?)\b|"
    r"\bevery\b|\ball\b|\bany\b|\bno\b|\bcannot\b|\bunique\b|\bexactly\b|\bat most\b|"
    r"\bat least\b|\bdivides\b|\bconverges\b|\bcontains\b|\bequals\b|\bequal to\b|"
    r"\bsatisfies\b|\bimplies\b|\bbounded\b|\bclosed under\b|\bproportional\b",
    re.I,
)

PROBES = [
    ("algebra", "quotient of a group by a normal subgroup and the first isomorphism theorem", "First Isomorphism"),
    ("analysis", "does a bounded entire function have to be constant by cauchy estimates", "Liouville"),
    ("probability", "tail bound for a martingale with bounded increments azuma", "Azuma"),
    ("rmt", "smallest singular value of a square random matrix and invertibility", "Least Singular"),
    ("logic", "no consistent effectively axiomatized theory interpreting arithmetic proves its own consistency", "Incompleteness"),
    ("optimization", "kkt conditions and strong duality under slater for convex problems", "Slater"),
    ("category", "yoneda embedding is fully faithful and natural transformations from hom", "Yoneda"),
    ("stochastic", "chain rule correction term for a function of an ito process", "Ito"),
]


def main() -> int:
    with ResearchStore(STORE) as store:
        all_nodes = list(store.iter_nodes())
        edges = list(store.iter_edges())
    superseded = {e.target_id for e in edges if e.kind is EdgeKind.SUPERSEDES}
    current = [n for n in all_nodes if n.id not in superseded]

    # A + B: statement health and proof presence
    flagged = []
    for n in current:
        meta = n.metadata if isinstance(n.metadata, dict) else {}
        if str(meta.get("logical_id") or "") in CLEARED_LOGICALS:
            continue
        kind = str(meta.get("claim_kind") or "")
        why = store_body_health(n.body or "")
        if not why and TITLE_ASSERTIVE_RE.search(n.title or "") and not CONTENT_MARKER_RE.search(n.body or ""):
            why = "pointer-only-no-assertion"
        if why:
            flagged.append({"node_id": n.id, "logical_id": meta.get("logical_id"),
                            "kind": kind, "title": n.title, "reason": f"stmt:{why}"})
            continue
        if kind in ("theorem", "lemma") and not str(meta.get("proof_text") or "").strip():
            flagged.append({"node_id": n.id, "logical_id": meta.get("logical_id"),
                            "kind": kind, "title": n.title, "reason": "missing-proof-text"})

    # C: graph integrity
    current_ids = {n.id for n in current}
    legacy_retired_edges = sum(
        1 for e in edges
        if e.kind is not EdgeKind.SUPERSEDES
        and (e.source_id in superseded or e.target_id in superseded)
    )
    dep_adj: dict[str, list[str]] = {}
    for e in edges:
        if e.kind is EdgeKind.DEPENDS_ON and e.source_id in current_ids and e.target_id in current_ids:
            dep_adj.setdefault(e.source_id, []).append(e.target_id)
    state: dict[str, int] = {}
    cycles = 0

    def visit(u: str) -> bool:
        state[u] = 1
        for v in dep_adj.get(u, ()):  # noqa: B023
            s = state.get(v, 0)
            if s == 1:
                return False
            if s == 0 and not visit(v):
                return False
        state[u] = 2
        return True

    for u in list(dep_adj):
        if state.get(u, 0) == 0 and not visit(u):
            cycles += 1

    # D: shelf probes
    probe_results = []
    for shelf, query, expect in PROBES:
        r = retrieve(query, nodes=current, edges=edges, limit=3,
                     min_support_score=0.5, min_margin=0.1)
        top = r.hits[0].node.title if (not r.abstained and r.hits) else None
        ok = bool(top and expect.lower() in top.lower())
        probe_results.append({"shelf": shelf, "expect": expect, "top": top, "ok": ok})

    # E: latency (retrieval only; process startup excluded)
    t0 = time.time()
    retrieve("does the order of a subgroup divide the order of the group",
             nodes=current, edges=edges, limit=3)
    latency_s = round(time.time() - t0, 3)

    report = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "nodes_total": len(all_nodes),
        "nodes_current": len(current),
        "superseded": len(superseded),
        "edges_total": len(edges),
        "flagged_count": len(flagged),
        "flagged": flagged,
        "legacy_edges_touching_retired": legacy_retired_edges,
        "depends_on_cycles": cycles,
        "probes": probe_results,
        "probe_pass": sum(1 for p in probe_results if p["ok"]),
        "retrieval_latency_s": latency_s,
    }
    REPORT.write_text(json.dumps(report, indent=1), encoding="utf-8")
    print(f"nodes current {len(current)} (superseded {len(superseded)}) | "
          f"flagged {len(flagged)} | legacy retired-edges {legacy_retired_edges} | "
          f"dep cycles {cycles} | probes {report['probe_pass']}/{len(PROBES)} | "
          f"retrieval {latency_s}s")
    for p in probe_results:
        print(("PASS " if p["ok"] else "MISS ") + p["shelf"] + " -> " + str(p["top"]))
    for f in flagged[:15]:
        print("FLAG", f["reason"], "|", f["kind"], "|", str(f["logical_id"])[:60])
    print("report:", REPORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
