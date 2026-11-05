"""Controls for the bm25 lever of recall_levers.py against this tree's bm25.score_postings.

 B1 on random postings sidecars the numpy form returns the same slugs and the same float scores, in the same
    order, as score_postings with its fast loop, on every query
 B2 the same against the plain loop (BRAIN_BM25_FASTLOOP=0)
 B3 a torn blob (length not a multiple of 12) gives None from both
 B4 a control: a perturbed K1 is caught (the comparison can fail)
 B5 this tree's score_postings is a proven version, so the lever installs

    python test_bm25_lever.py      (a few seconds; ALL PASS at the end; needs numpy)
"""
import os
import random
import sqlite3
import struct
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
results = []


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


WORDS = ["alpha", "beta", "gamma", "delta", "kernel", "matrix", "spectral", "graph", "walk", "bound", "random",
         "tree", "limit", "measure", "proof", "lemma", "flow", "norm", "entropy", "ring"]


def sidecar(rng, n_docs):
    con = sqlite3.connect(":memory:")
    con.execute("create table p(term text primary key, df int, blob blob)")
    con.execute("create table d(pos int primary key, slug text)")
    lens = [rng.randint(5, 400) for _ in range(n_docs)]
    for pos in range(n_docs):
        con.execute("insert into d values(?,?)", (pos, "m%04d" % pos))
    for w in WORDS:
        docs = sorted(rng.sample(range(n_docs), rng.randint(0, n_docs)))
        b = b"".join(struct.pack("<IiI", p, rng.randint(1, 9), lens[p]) for p in docs)
        con.execute("insert into p values(?,?,?)", (w, len(docs), zlib.compress(b)))
    avgdl = sum(lens) / float(n_docs)
    return con, float(n_docs), avgdl


def query(rng):
    return " ".join(rng.choice(WORDS + ["unseen", "nothing"]) for _ in range(rng.randint(1, 8)))


def main():
    import numpy as np
    import bm25
    import recall_levers as rl
    real = bm25.score_postings
    rng = random.Random(20261105)
    same_fast = same_plain = total = 0
    try:
        for _ in range(40):
            conn = sidecar(rng, rng.randint(3, 300))
            for _ in range(8):
                q = query(rng)
                k = rng.choice([1, 5, 20, 50])
                total += 1
                bm25._FASTLOOP = True
                a = real(q, k, conn=conn)
                bm25._FASTLOOP = False
                b = real(q, k, conn=conn)
                c = rl._bm25_np(bm25, np, q, k, conn)
                same_fast += a == c
                same_plain += b == c
        check(same_fast == total, "B1 numpy form equals the fast loop on %d of %d queries" % (same_fast, total))
        check(same_plain == total, "B2 numpy form equals the plain loop on %d of %d queries" % (same_plain, total))
        con = sqlite3.connect(":memory:")
        con.execute("create table p(term text primary key, df int, blob blob)")
        con.execute("create table d(pos int primary key, slug text)")
        con.execute("insert into p values(?,?,?)", ("alpha", 1, zlib.compress(b"\x00" * 13)))
        torn = (con, 1.0, 10.0)
        bm25._FASTLOOP = True
        check(real("alpha", 5, conn=torn) is None and rl._bm25_np(bm25, np, "alpha", 5, torn) is None,
              "B3 a torn blob gives None from both")
        conn = sidecar(rng, 200)
        q = "alpha kernel spectral walk"
        want = real(q, 20, conn=conn)
        k1 = bm25.K1
        try:
            bm25.K1 = k1 * 1.01
            got = rl._bm25_np(bm25, np, q, 20, conn)
        finally:
            bm25.K1 = k1
        check(want and got != want, "B4 control: a perturbed K1 is caught")
        check(rl._proven("bm25", real), "B5 this tree's score_postings is a proven version")
    finally:
        bm25._FASTLOOP = os.environ.get("BRAIN_BM25_FASTLOOP", "1") == "1"
    print("ALL PASS" if all(results) else "SOME FAILED")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
