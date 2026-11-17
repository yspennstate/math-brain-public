"""test_semtop_evidence.py - the math hook's semantic first claim needs a winner (29 Sep 2026).

    python test_semtop_evidence.py [MATH_SENSE.py] [--old OLD_MATH_SENSE.py]

A stand-in for math_brain.semantic serves fixed claim vectors and a fixed question vector.
 T1 every cosine equal: no first claim, and the vouch does not agree with the card at index 0
 T2 the top two tie exactly: no first claim
 T3 a clear winner: it is the first claim, the vouch agrees with it and with nothing else
 T4 a NaN cosine: no first claim
 T5 one claim in the store: it is the first claim
 T6 MATHBRAIN_SEMTOP_MARGIN below zero: the old rule (argmax) comes back
With --old, the hook before this change must agree with the card at index 0 on T1's flat vector (the check can fail).
"""
import importlib.machinery
import importlib.util
import os
import shutil
import sqlite3
import sys
import tempfile
import types

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
MS = os.path.abspath(ARGS[0]) if ARGS and not ARGS[0].startswith("--") else os.path.join(HERE, "math_sense.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
sys.path.insert(0, HERE)
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


class Hit:
    def __init__(self, nid):
        self.node = types.SimpleNamespace(id=nid)


def with_semantic(vecs, ids, question, fn):
    """Run fn() with `from math_brain import semantic` resolving to a stand-in holding these vectors."""
    fake = types.ModuleType("math_brain.semantic")
    fake.QUERY_PREFIX = ""
    fake._vecs = np.asarray(vecs, dtype=np.float32)
    fake._ids = np.asarray(ids)
    fake._digests = np.asarray([digest_of(i) for i in ids])     # bound to store_for's rows (test_claim_vectors_bound.py)
    fake._load_artifact = lambda: None
    fake._query_encoder = lambda: types.SimpleNamespace(embed=lambda text: np.asarray(question, dtype=np.float32))
    pkg = types.ModuleType("math_brain")
    pkg.semantic = fake
    saved = {k: sys.modules.get(k) for k in ("math_brain", "math_brain.semantic")}
    sys.modules["math_brain"], sys.modules["math_brain.semantic"] = pkg, fake
    try:
        return fn()
    finally:
        for k, v in saved.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v


IDS = ["claim_aaaaaaaaaaaaaaaaaaaa1", "claim_bbbbbbbbbbbbbbbbbbbb2", "claim_cccccccccccccccccccc3"]
FLAT = [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]            # every claim orthogonal to the question: cosines 0, 0, 0
TIE = [[1.0, 0.0], [1.0, 0.0], [0.0, 1.0]]             # the first two tie at the top
CLEAR = [[1.0, 0.0], [0.6, 0.8], [0.0, 1.0]]           # the first wins
Q = [1.0, 0.0]


FIXTURES = tempfile.mkdtemp(prefix="semtop_evidence_")


def digest_of(nid):
    return "digest-of-" + nid


def store_for(ids):
    """A store holding exactly these claims: since 29 Sep the hook names no first claim over vectors that do not cover
    the store it serves, or were made from other text (test_claim_vectors_bound.py), so each case needs a store that
    matches its vectors, digests included."""
    path = os.path.join(FIXTURES, "store_%d.sqlite3" % len(os.listdir(FIXTURES)))
    con = sqlite3.connect(path)
    con.executescript("create table nodes (id text primary key, kind text, title text, body text, digest text);"
                      "create table claims (id text primary key);"
                      "create table edges (kind text, source_id text, target_id text);")
    for i in ids:
        con.execute("insert into nodes values (?, 'claim', ?, ?, ?)", (i, i, i, digest_of(i)))
        con.execute("insert into claims values (?)", (i,))
    con.commit()
    con.close()
    return path


def top_and_vouch(m, vecs, ids, nid):
    m.STORE_PATH = store_for(ids)

    def run():
        m._SEMTOP.clear()
        return m._semantic_top("a prompt"), m._vouch_agrees("a prompt", [Hit(nid)])
    return with_semantic(vecs, ids, Q, run)


def main():
    m = load(MS, "ms_semtop")
    t, v = top_and_vouch(m, FLAT, IDS, IDS[0])
    check(t is None and v is False, "T1 flat cosines: first claim %r, vouch %r" % (t, v))
    t, v = top_and_vouch(m, TIE, IDS, IDS[0])
    check(t is None and v is False, "T2 tied top: first claim %r, vouch %r" % (t, v))
    t, v = top_and_vouch(m, CLEAR, IDS, IDS[0])
    _, v_other = top_and_vouch(m, CLEAR, IDS, IDS[1])
    check(t == IDS[0] and v is True and v_other is False,
          "T3 clear winner: first claim %r, vouch for it %r, for another %r" % (t, v, v_other))
    t, _ = top_and_vouch(m, [[float("nan"), 0.0], [1.0, 0.0], [0.0, 1.0]], IDS, IDS[1])
    check(t is None, "T4 a NaN cosine: first claim %r" % t)
    t, _ = top_and_vouch(m, [[1.0, 0.0]], IDS[:1], IDS[0])
    check(t == IDS[0], "T5 one claim: first claim %r" % t)
    saved = m.SEMTOP_MARGIN
    m.SEMTOP_MARGIN = -1.0
    try:
        t, v = top_and_vouch(m, FLAT, IDS, IDS[0])
    finally:
        m.SEMTOP_MARGIN = saved
    check(t == IDS[0] and v is True, "T6 margin off: the old argmax rule (%r, vouch %r)" % (t, v))
    if OLD:
        o = load(OLD, "ms_semtop_old")
        t, v = top_and_vouch(o, FLAT, IDS, IDS[0])
        check(t == IDS[0] and v is True,
              "N1 the hook before this change agrees on a flat vector (first claim %r, vouch %r; the check can fail)"
              % (t, v))
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    try:
        rc = main()
    finally:
        shutil.rmtree(FIXTURES, ignore_errors=True)
    sys.exit(rc)
