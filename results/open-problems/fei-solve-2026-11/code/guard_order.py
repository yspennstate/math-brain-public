"""Guarded orders for the root of the two-level tree DNF (FLOW 12(r)).

Order (first revealed ... last revealed; the witness label is the LAST revealed element of U - i):
    [root] [unguarded leaves] [mates] [guard leaves]
where the guards are the first `gam` leaves of every clause of every mate. gam = 0 is "leaves first",
gam = L is "mates first". Uses the arbitrary-order resampling moments of Codex worker FEIB20 (nested.py).

Usage: python guard_order.py W D [W D ...]
"""
import sys
import os
import json
import math

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "codex", "workers", "FEIB20"))
import nested as N


def guarded(T, gam):
    lo, hi = [], []
    for m in range(T.M):
        for c in range(T.D - 1):
            for l in range(T.L):
                (hi if l < gam else lo).append(T.leaf(m, c, l))
    return [0] + lo + list(range(1, 1 + T.M)) + hi


def main():
    a = [int(t) for t in sys.argv[1:]]
    for w, D in zip(a[0::2], a[1::2]):
        T = N.Model(w, D)
        lg = math.log2(D)
        gams = sorted(set([0, 1, 2] + [int(round(lg)) + k for k in (-2, -1, 0, 1, 2, 3, 4)] + [T.L]))
        for gam in gams:
            if gam < 0 or gam > T.L:
                continue
            r = N.witness(T, 0, guarded(T, gam))
            print(json.dumps({"w": w, "D": D, "n": T.n, "gam": gam, "inf": r["inf"], "ratio": round(r["ratio"], 6),
                              "min_step": r["min_step"], "mass_error": r["mass_error"]}), flush=True)


if __name__ == "__main__":
    main()
