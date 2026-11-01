# -*- coding: utf-8 -*-
# Copied from the probability campaign's build_corpus_store.py (2026-09-06) and re-pointed at the multi-domain bank; that lane's file is never edited from here.

"""build_corpus_store.py - a statements-only store of the harvested literature, for the brain_v2 arm.

Every theorem/lemma/proposition/corollary STATEMENT extracted from the arXiv math.PR sources (accepted or not:
the statement is useful even when its proof was too long or too short for the bank) becomes one node in a sqlite
file with the production store's `nodes` columns (id, kind, title, body, metadata_json, digest, created_at), so the
notes builder can rank over it with --store. PROOF TEXT IS NEVER STORED: the arm measures what a brain that had
read the literature's results (with their hypotheses) can add, not one that memorised the proofs the bank mutates.

    python build_corpus_store.py --proofs proofs.jsonl --out corpus_statements.sqlite [--union <production store>]

With --union the production store's nodes are copied in first (read-only source), so the file is the production
brain plus the literature: the brain_v2 store. The production file is never written.
"""
import argparse
import hashlib
import io
import json
import os
import sqlite3
import time

HERE = os.path.dirname(os.path.abspath(__file__))
HYP_RE = __import__("re").compile(r"^(?:Let|Suppose|Assume|Fix|Consider|Given|If|For|Under|Whenever|Take|Set|Put|Define)\b")


def split_hypotheses(statement):
    """A statement's sentences that open with Let/Suppose/Assume/... are its hypotheses; the rest is the conclusion.
    Crude, sentence-level, and recorded as metadata only, so a served note can show the hypothesis list."""
    import re
    s = statement.replace("\n", " ")
    # protect math so sentence splitting does not break inside $...$
    parts = re.split(r"(?<=[.;])\s+(?=[A-Z\\])", s)
    hyps, concl = [], []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        (hyps if HYP_RE.match(p) else concl).append(p)
    return hyps, concl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proofs", default=os.path.join(HERE, "proofs.jsonl"))
    ap.add_argument("--out", default=os.path.join(HERE, "corpus_statements.sqlite"))
    ap.add_argument("--union", default="")
    a = ap.parse_args()
    if os.path.exists(a.out):
        os.remove(a.out)
    con = sqlite3.connect(a.out)
    con.execute("create table nodes (id text primary key, kind text, title text, body text, metadata_json text, digest text, created_at text)")
    n_prod = 0
    if a.union:
        src = sqlite3.connect("file:" + a.union.replace("\\", "/") + "?mode=ro", uri=True)
        rows = src.execute("select id, kind, title, body, metadata_json, digest, created_at from nodes").fetchall()
        src.close()
        con.executemany("insert or ignore into nodes values (?,?,?,?,?,?,?)", rows)
        n_prod = len(rows)
    seen = set()
    n_lit = 0
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for ln in io.open(a.proofs, encoding="utf-8"):
        if not ln.strip():
            continue
        r = json.loads(ln)
        st = (r.get("statement") or "").strip()
        if len(st) < 40 or len(st) > 2500:
            continue
        dg = hashlib.sha256(st.encode("utf-8")).hexdigest()[:20]
        if dg in seen:
            continue
        seen.add(dg)
        title = "%s (%s, arXiv %s): %s" % (r.get("kind", "result").capitalize(), r.get("published", "")[:4], r.get("paper", ""),
                                            (r.get("title") or "")[:90])
        hyps, concl = split_hypotheses(st)
        meta = {"source": "arxiv", "paper": r.get("paper"), "kind": r.get("kind"), "labels": r.get("labels"),
                "published": r.get("published"), "campaign": "campaign_2026-09-06_prob_lit_bank", "statement_only": True,
                "hypotheses": hyps, "conclusion": " ".join(concl)}
        con.execute("insert or ignore into nodes values (?,?,?,?,?,?,?)",
                    ("lit_" + dg, "literature_statement", title, st, json.dumps(meta, ensure_ascii=False), dg, now))
        n_lit += 1
    con.commit()
    total = con.execute("select count(*) from nodes").fetchone()[0]
    con.close()
    print(json.dumps({"out": a.out, "production_nodes": n_prod, "literature_statements": n_lit, "total_nodes": total,
                      "sha256": hashlib.sha256(open(a.out, "rb").read()).hexdigest()[:16]}, indent=1))


if __name__ == "__main__":
    main()
