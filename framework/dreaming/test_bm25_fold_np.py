"""test_bm25_fold_np.py - the numpy path of bm25_fold.score() gives the loop's list, and hands back to the loop when a unit's
positions repeat (13 Nov 2026, an agent; the repeated-position branch had never been run on purpose - an agent's
audit of the numpy path, AGENT_AUDIT entry 33).

    python test_bm25_fold_np.py      prints one line per case and PASS / FAIL; exit 0 on PASS

A fake posting source stands in for the overlay, so the cases do not depend on the live index.
"""
import os
import sys

DR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DR)
import numpy as np  # noqa: E402
import bm25_fold as bf  # noqa: E402


class Src:
    def __init__(self, post, n=50, avgdl=37.5):
        self.post_, self.n, self.avgdl = post, n, avgdl

    def arrays(self, t):
        ps, fs, ds = zip(*self.post_[t]) if self.post_.get(t) else ((), (), ())
        return list(ps), list(fs), list(ds)

    def np_arrays(self, t):
        ps, fs, ds = self.arrays(t)
        return (np.array(ps, dtype="<u4"), np.array(fs, dtype="<i4"), np.array(ds, dtype="<u4"))

    def slug(self, k):
        return "doc%03d" % k


class BM:
    df = {}


def run(post, us, numpy_on):
    bf._source, bf.units = (lambda bm: Src(post)), (lambda toks, dfget, cut=None: us)
    os.environ["BRAIN_FOLD_NUMPY"] = "1" if numpy_on else "0"
    return bf.score(BM(), "unused words", topk=20)


def main():
    orig = (bf._source, bf.units)
    good = {"a": [(1, 2, 30), (4, 1, 50), (9, 3, 20)], "b": [(4, 2, 50), (7, 1, 44)],
            "c": [(1, 1, 30), (7, 2, 44), (12, 1, 61)]}
    rep_single = {"a": [(1, 2, 30), (4, 1, 50), (4, 2, 50), (9, 3, 20)], "b": [(7, 1, 44)]}
    rep_member = {"a": [(1, 2, 30)], "b": [(4, 2, 50), (4, 1, 50), (7, 1, 44)]}
    cases = [("sorted postings, a two-term unit", good, [("a",), ("b", "c")], False),
             ("repeated position in a one-term unit", rep_single, [("a",), ("b",)], True),
             ("repeated position in a member of a two-term unit", rep_member, [("a", "b")], True)]
    ok = True
    try:
        for name, post, us, repeats in cases:
            src = Src(post)
            got_np = bf._score_np(src, us, 20, src.n, src.avgdl, 1.2, 0.75)
            handed_back = got_np is None
            a, b = run(post, us, True), run(post, us, False)
            same = a == b and bool(a)
            good_case = same and handed_back == repeats
            ok &= good_case
            print("%-4s %s: numpy %s, lists identical %s (%d rows)" % ("ok" if good_case else "FAIL", name,
                  "handed back to the loop" if handed_back else "ran", same, len(a or [])))
    finally:
        bf._source, bf.units = orig
        os.environ.pop("BRAIN_FOLD_NUMPY", None)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
