# -*- coding: utf-8 -*-
# Copied from the probability campaign's plit_notes_bm25.py (2026-09-06) and re-pointed at the multi-domain bank; that lane's file is never edited from here.

"""md_notes_bm25.py - brain notes for the plit bank, BM25 over the math store (the B12 builder's rule, unchanged),
in the runner's notes schema; placebo notes by the same shifted-donor rule (kind and bulk matched, relevance broken).

    python md_notes_bm25.py --run run_md [--k 3] [--steps 3] [--store <sqlite path>] [--label brain]

--label writes <label>_notes.json (default brain) so a second store generation can be served as its own arm
(brain_v2) against the same frozen sample. The placebo file is written only for the default label.
"""
import argparse
import collections
import io
import json
import math
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK10K = os.path.join(os.path.expanduser("~"), "ai-memories-and-functionality", "06_math_research",
                       "probability_open_problem_campaign_2026_08_09", "eval", "bank10k")
sys.path.insert(0, BANK10K)
import run_bank10k as rb  # noqa: E402

rb.ITEMS = os.path.join(HERE, "items", "mdlit.jsonl")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="run_md")
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--steps", type=int, default=3)
    ap.add_argument("--store", default=rb.STORE)
    ap.add_argument("--label", default="brain")
    ap.add_argument("--exclude-kind-prefix", default="", help="skip store nodes whose kind starts with this")
    ap.add_argument("--exclude-own-statement", action="store_true",
                    help="never serve the literature node that IS the item's claim (found by the statement digest, no keys read)")
    ap.add_argument("--exclude-own-paper", action="store_true",
                    help="never serve a literature node from the item's own paper (the paper is read off the own-statement node)")
    a = ap.parse_args()
    run = a.run if os.path.isabs(a.run) else os.path.join(HERE, a.run)
    ids = json.load(io.open(os.path.join(run, "SAMPLE.json"), encoding="utf-8"))["item_ids"]
    idset = set(ids)
    items = {}
    for ln in io.open(rb.ITEMS, encoding="utf-8"):
        it = json.loads(ln)
        if it["item_id"] in idset:
            items[it["item_id"]] = it
    conn = sqlite3.connect(a.store)
    nodes = [(nid, ki, ti, bo) for nid, ki, ti, bo in conn.execute("select id, kind, title, body from nodes")]
    paper_of = {}
    if a.exclude_own_paper:
        for nid, meta in conn.execute("select id, metadata_json from nodes where id like 'lit_%'"):
            try:
                paper_of[nid] = json.loads(meta or "{}").get("paper")
            except Exception:
                pass
    conn.close()
    if a.exclude_kind_prefix:
        nodes = [n for n in nodes if not str(n[1] or "").startswith(a.exclude_kind_prefix)]
    import hashlib
    own_stats = {"own_statement_in_store": 0, "own_paper_known": 0}
    docs = []
    df = collections.Counter()
    for nid, ki, ti, bo in nodes:
        toks = list(rb._tok(ti or "")) * 2 + list(rb._tok(bo or ""))
        tf = collections.Counter(toks)
        docs.append((nid, ti, bo, tf, len(toks)))
        for t in tf:
            df[t] += 1
    n = len(docs)
    avgdl = sum(d[4] for d in docs) / max(1, n)
    k1, b = 1.2, 0.75
    idf = {t: math.log(1.0 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}
    brain = {}
    for m, iid in enumerate(ids):
        it = items[iid]
        steps = it.get("argument_steps") or []
        qtext = it["claim"] + " " + " ".join(s.get("text", "") for s in steps[: a.steps])
        q = rb._tok(qtext)
        own_id = "lit_" + hashlib.sha256(it["claim"].strip().encode("utf-8")).hexdigest()[:20]
        own_paper = paper_of.get(own_id)
        if a.exclude_own_statement or a.exclude_own_paper:
            if any(d[0] == own_id for d in docs):
                own_stats["own_statement_in_store"] += 1
            if own_paper:
                own_stats["own_paper_known"] += 1
        scored = []
        for nid, ti, bo, tf, dl in docs:
            if (a.exclude_own_statement or a.exclude_own_paper) and nid == own_id:
                continue
            if a.exclude_own_paper and own_paper and paper_of.get(nid) == own_paper:
                continue
            s = 0.0
            for t in q:
                f = tf.get(t)
                if f:
                    s += idf[t] * f * (k1 + 1) / (f + k1 * (1 - b + b * dl / avgdl))
            if s > 0:
                scored.append((s, nid, ti, bo))
        scored.sort(reverse=True)
        brain[iid] = [{"node_id": x[1], "title": x[2], "body": (x[3] or "")[:1200], "score": round(x[0], 3)} for x in scored[: a.k]]
        if (m + 1) % 50 == 0:
            print("  %d/%d" % (m + 1, len(ids)), flush=True)
    fp = rb.sample_fingerprint(ids)
    meta = {"store": a.store, "n_nodes": n, "k": a.k, "ranking": "bm25 title x2 + body, query claim + %d steps" % a.steps,
            "sample_fingerprint": fp, "label": a.label, "exclude_own_statement": a.exclude_own_statement,
            "exclude_own_paper": a.exclude_own_paper, "own_stats": own_stats}
    rb.dump_atomic(os.path.join(run, a.label + "_notes.json"), dict(meta, notes=brain))
    if a.label == "brain":
        shift = 37 % len(ids) or 1
        placebo = {iid: brain[ids[(k + shift) % len(ids)]] for k, iid in enumerate(ids)}
        for k, iid in enumerate(ids):
            if [r["node_id"] for r in placebo[iid]] == [r["node_id"] for r in brain[iid]]:
                for extra in range(1, len(ids)):
                    cand = brain[ids[(k + shift + extra) % len(ids)]]
                    if [r["node_id"] for r in cand] != [r["node_id"] for r in brain[iid]]:
                        placebo[iid] = cand
                        break
        rb.dump_atomic(os.path.join(run, "placebo_notes.json"), dict(meta, label="placebo", notes=placebo))
    empty = sum(1 for v in brain.values() if not v)
    print("notes for %d items (%d empty); store %d nodes; label %s -> %s" % (len(ids), empty, n, a.label, run))
    return 0


if __name__ == "__main__":
    sys.exit(main())
