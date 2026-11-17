"""test_math_review_reads.py - the math hook reads a card's recorded review after the selection, for the shown cards only,
and judges each review row on its own (29 Sep 2026).

    python test_math_review_reads.py [MATH_SENSE.py] [--old OLD_MATH_SENSE.py]

Builds throwaway evidence tables (the store's own evidence schema and claim index, read from the live store read-only)
in a temporary folder and reads them through _review_reads, and _trust_tag renders what it returns.
 V1  a sound human review that passed reads 'human read ...: no gap; provisional'; a sound agent read that failed reads
     'agent read ...: GAP FOUND; unverified'
 V2  a human review edited to pass without its digest (E1): no read shown, the card reads unverified
 V3  passed given as the string "false", digest consistent (E2): no read shown
 V4  payloads that are a JSON list, null, a string, a number or true (E5, E6): skipped, nothing raised
 V5  a payload that is not JSON (E7): skipped
 V6  two dated reads of one claim: the later one is shown
 V7  a row whose payload names another claim than its column: skipped
 V8  only the three values the tag uses are kept
 V9  5,000 review rows of other claims: reading three claims decodes only their rows
With --old, the reader before this change shows the edited review as a human's pass (V2), reads "false" as a pass (V3),
raises on a JSON list (V4) and decodes every row (V9): the checks can fail.
"""
import dataclasses
import importlib.machinery
import importlib.util
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import types

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD_SRC = r"~\math-brain-build\src"
LIVE = r"~\math-brain-build\local\population\brain.sqlite3"
ARGS = sys.argv[1:]
MS = os.path.abspath(ARGS[0]) if ARGS and not ARGS[0].startswith("--") else os.path.join(HERE, "math_sense.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
DREAMING = os.path.join(os.path.expanduser("~"), ".claude", "dreaming")   # the hook's sibling modules
sys.path.insert(0, DREAMING)
sys.path.insert(0, BUILD_SRC)
sys.path.insert(0, HERE)

from math_brain.models import Evidence, EvidenceKind, canonical_json, content_hash  # noqa: E402

fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


def schema():
    live = sqlite3.connect("file:%s?mode=ro" % LIVE.replace("\\", "/"), uri=True)
    sql = [r[0] for r in live.execute("SELECT sql FROM sqlite_master WHERE tbl_name = 'evidence' AND sql IS NOT NULL "
                                      "ORDER BY CASE type WHEN 'table' THEN 0 ELSE 1 END, name")]
    live.close()
    return sql


def sound(claim, kind, passed, when, **extra):
    """A review row written the way the store writes one: the payload and the digest of the same Evidence."""
    e = Evidence(claim_id=claim, kind=EvidenceKind(kind), summary="summary of the read", scope="the whole statement",
                 verifier="a reviewer", passed=passed, created_at=when, **extra)
    return e, dataclasses.asdict(e)


def insert(db, e, payload_text, digest=None, claim=None):
    db.execute("INSERT INTO evidence(id, claim_id, payload_json, digest, created_at) VALUES (?, ?, ?, ?, ?)",
               (e.id, claim or e.claim_id, payload_text, digest or e.digest(), e.created_at))


def build(path, filler=0, non_objects=True):
    db = sqlite3.connect(path)
    for q in schema():
        db.execute(q)
    e, p = sound("claim_human_pass", "human_proof_review", True, "2026-09-01T10:00:00+00:00")
    insert(db, e, canonical_json(p))
    e, p = sound("claim_agent_gap", "discovery_report", False, "2026-09-02T10:00:00+00:00")
    insert(db, e, canonical_json(p))
    e, p = sound("claim_edited", "human_proof_review", False, "2026-09-03T10:00:00+00:00")
    p["passed"] = True                                   # edited after the write; the digest is the original one
    insert(db, e, canonical_json(p))
    e, p = sound("claim_string_false", "human_proof_review", True, "2026-09-04T10:00:00+00:00")
    p["passed"] = "false"               # written around the model (which refuses it since 29 Sep); digest recomputed
    insert(db, e, canonical_json(p), digest=content_hash(p))
    for n, text in enumerate(("[]", "null", '"a string"', "3", "true") if non_objects else ()):
        e, _p = sound("claim_not_object", "discovery_report", True, "2026-09-05T10:0%d:00+00:00" % n)
        insert(db, e, text, digest="sha256:not-object-%d" % n)
    e, _p = sound("claim_not_json", "discovery_report", True, "2026-09-06T10:00:00+00:00")
    insert(db, e, "{not json", digest="sha256:not-json")
    e, p = sound("claim_two_reads", "discovery_report", False, "2026-09-07T10:00:00+00:00")
    insert(db, e, canonical_json(p))
    e, p = sound("claim_two_reads", "human_proof_review", True, "2026-09-08T10:00:00+00:00")
    insert(db, e, canonical_json(p))
    e, p = sound("claim_other", "human_proof_review", True, "2026-09-09T10:00:00+00:00")
    insert(db, e, canonical_json(p), claim="claim_named_wrong")     # the column names another claim than the payload
    for n in range(filler):
        e, p = sound("claim_filler_%05d" % n, "discovery_report", n % 2 == 0, "2026-08-01T00:00:00+00:00")
        insert(db, e, canonical_json(p))
    db.commit()
    db.close()


class Counting:
    """json.loads, counted while the reader runs (the hook calls it through the json module)."""

    def __init__(self):
        self.n, self.real = 0, json.loads

    def __enter__(self):
        def loads(*a, **k):
            self.n += 1
            return self.real(*a, **k)
        json.loads = loads
        return self

    def __exit__(self, *exc):
        json.loads = self.real


def old_reads(m, path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        return m._read_records(types.SimpleNamespace(connection=conn))
    finally:
        conn.close()


def main():
    m = load(MS, "ms_reviews_new")
    o = load(OLD, "ms_reviews_old") if OLD else None
    tmp = tempfile.mkdtemp(prefix="review_reads_")
    try:
        small, big = os.path.join(tmp, "small.sqlite3"), os.path.join(tmp, "big.sqlite3")
        build(small)
        build(big, filler=5000)
        every = ["claim_human_pass", "claim_agent_gap", "claim_edited", "claim_string_false", "claim_not_object",
                 "claim_not_json", "claim_two_reads", "claim_other", "claim_named_wrong"]
        try:
            reads, raised = m._review_reads(every, store_path=small), None
        except Exception as exc:
            reads, raised = {}, exc
        meta = {"claim_kind": "theorem", "proof_text": "", "statement_fidelity_reviewed": 1}
        tag = {c: m._trust_tag(meta, reads.get(c)) for c in every}
        check(raised is None and "human read 2026-09-01: no gap; provisional" in tag["claim_human_pass"]
              and "agent read 2026-09-02: GAP FOUND; unverified" in tag["claim_agent_gap"],
              "V1 sound reads shown: %r / %r" % (tag["claim_human_pass"], tag["claim_agent_gap"]))
        check("claim_edited" not in reads and " read " not in tag["claim_edited"]
              and tag["claim_edited"].endswith("unverified"),
              "V2 a review edited to pass without its digest is not shown: %r" % tag["claim_edited"])
        check("claim_string_false" not in reads, "V3 passed given as the string 'false' is not shown: %r"
              % tag["claim_string_false"])
        check(raised is None and "claim_not_object" not in reads,
              "V4 payloads that are a list, null, a string, a number or true: skipped, nothing raised (%r)" % raised)
        check("claim_not_json" not in reads, "V5 a payload that is not JSON: skipped")
        check((reads.get("claim_two_reads") or {}).get("passed") is True
              and (reads.get("claim_two_reads") or {}).get("when") == "2026-09-08",
              "V6 two dated reads: the later one is shown (%r)" % reads.get("claim_two_reads"))
        check("claim_named_wrong" not in reads and "claim_other" not in reads,
              "V7 a row whose payload names another claim than its column: skipped")
        check(bool(reads) and all(set(v) == {"when", "passed", "human"} for v in reads.values()),
              "V8 only when, passed and human are kept: %s" % sorted({k for v in reads.values() for k in v}))
        three = ["claim_human_pass", "claim_agent_gap", "claim_two_reads"]
        with Counting() as c:
            got = m._review_reads(three, store_path=big)
        rows_of_three = 4
        check(c.n == rows_of_three and set(got) == set(three),
              "V9 5,000 unrelated review rows: reading three claims decoded %d payloads (their %d rows)"
              % (c.n, rows_of_three))
        if o:
            objects = os.path.join(tmp, "objects.sqlite3")   # the old reader raises on the others (N3)
            build(objects, non_objects=False)
            ro_reads = old_reads(o, objects)
            old_tag = o._trust_tag(meta, ro_reads.get("claim_edited"))
            check("no gap; provisional" in old_tag,
                  "N1 the reader before this change shows the edited review as a human's pass: %r" % old_tag)
            check((ro_reads.get("claim_string_false") or {}).get("passed") is True,
                  "N2 the reader before this change reads the string 'false' as a pass: %r"
                  % ro_reads.get("claim_string_false"))
            only_list = os.path.join(tmp, "list.sqlite3")
            db = sqlite3.connect(only_list)
            for q in schema():
                db.execute(q)
            e, _p = sound("claim_list", "discovery_report", True, "2026-09-10T10:00:00+00:00")
            insert(db, e, "[]", digest="sha256:list")
            db.commit()
            db.close()
            try:
                old_reads(o, only_list)
                old_raised = None
            except Exception as exc:
                old_raised = type(exc).__name__
            check(old_raised == "AttributeError",
                  "N3 the reader before this change raises on a payload that is a JSON list (%s): the hook's outer "
                  "handler then silences the whole block" % old_raised)
            big_objects = os.path.join(tmp, "big_objects.sqlite3")
            build(big_objects, filler=5000, non_objects=False)
            with Counting() as c:
                old_reads(o, big_objects)
            check(c.n > 5000, "N4 the reader before this change decodes every row: %d payloads" % c.n)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
