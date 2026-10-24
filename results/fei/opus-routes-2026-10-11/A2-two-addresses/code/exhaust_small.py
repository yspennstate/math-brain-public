"""Exhaustive scan of K2 for n <= 4: every Boolean function, every address set |A| <= 2.
Records max H/I among functions in K2 that need exactly two addresses (no 0/1-address witness),
and overall.  Float logs (evidence only); exact rational influence."""
import sys, json, math, itertools
sys.path.insert(0, __file__.rsplit("\\", 1)[0] if "\\" in __file__ else __file__.rsplit("/", 1)[0])
from fei2 import *

def scan(n):
    N = 1 << n
    best = (0, None, None)
    best2 = (0, None, None)
    count_K2 = 0
    count_exact2 = 0
    for code in range(1 << N):
        f = [1 - 2 * ((code >> x) & 1) for x in range(N)]
        W = wht_int(f)
        Hf, If = H_I_float(W, n)
        if If == 0:
            continue
        # witness search
        wit = None
        min_k = None
        for A in address_sets(n, 2):
            if conditionally_product(W, n, A):
                wit = A
                min_k = len(A)
                break
        if wit is None:
            continue
        count_K2 += 1
        r = Hf / If
        if r > best[0] + 1e-12:
            best = (r, code, wit)
        if min_k == 2:
            count_exact2 += 1
            if r > best2[0] + 1e-12:
                best2 = (r, code, wit)
    return dict(n=n, count_K2=count_K2, count_exactly_two=count_exact2,
                best_overall=dict(ratio=best[0], code=best[1], A=best[2]),
                best_two_needed=dict(ratio=best2[0], code=best2[1], A=best2[2]))

if __name__ == "__main__":
    res = []
    for n in range(1, 5):
        r = scan(n)
        print(r, flush=True)
        res.append(r)
    with open(sys.argv[1] if len(sys.argv) > 1 else "exhaust_small.json", "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)
