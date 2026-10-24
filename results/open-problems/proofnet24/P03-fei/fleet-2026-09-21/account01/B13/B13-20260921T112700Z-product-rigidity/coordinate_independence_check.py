#!/usr/bin/env python3
"""Exact finite check of B13 coordinate spectral-independence rigidity.

Enumerates Boolean functions up to global negation for n<=4. For each
coordinate i it tests exactly, with integer squared Walsh coefficients,
whether the spectral membership bit X_i is independent of X_{-i}. It
then checks that q_i=P(i in X)=Inf_i(f) is in {0,1/2,1}.

This is only a finite sanity check; PRODUCT_SPECTRAL_RIGIDITY.md contains
the dimension-free proof.
"""
from collections import Counter
import json


def fwht_int(values):
    a = list(values)
    h = 1
    while h < len(a):
        for k in range(0, len(a), 2*h):
            for j in range(k, k+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def coord_independent_exact(walsh, n, i):
    N = 1 << n
    total = N*N
    sq = [z*z for z in walsh]
    qnum = sum(sq[s] for s in range(N) if (s >> i) & 1)
    for s in range(N):
        if (s >> i) & 1:
            continue
        s1 = s | (1 << i)
        # p(s1)/(q) = p(s)/(1-q), cross-multiplied exactly.
        if sq[s1] * (total-qnum) != sq[s] * qnum:
            return False, qnum, total
    return True, qnum, total


def run():
    out = {}
    for n in range(1, 5):
        N = 1 << n
        canonical = 1 << (N-1)  # fix f(0)=+1
        independent_coordinate_cases = 0
        bad_cases = 0
        q_hist = Counter()
        for bits in range(canonical):
            f = [1] + [1 if (bits >> (x-1)) & 1 else -1 for x in range(1, N)]
            walsh = fwht_int(f)
            for i in range(n):
                ok, qnum, total = coord_independent_exact(walsh, n, i)
                if not ok:
                    continue
                independent_coordinate_cases += 1
                if qnum == 0:
                    key = "0"
                elif qnum == total:
                    key = "1"
                elif 2*qnum == total:
                    key = "1/2"
                else:
                    key = f"{qnum}/{total}"
                    bad_cases += 1
                q_hist[key] += 1
        out[str(n)] = {
            "canonical_boolean_functions": canonical,
            "independent_coordinate_cases": independent_coordinate_cases,
            "bad_marginal_cases": bad_cases,
            "q_histogram": dict(sorted(q_hist.items())),
        }
    return out


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
