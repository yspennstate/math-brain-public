#!/usr/bin/env python3
"""Exact exhaustive check of the product-spectral classification for n <= 4.

For f:{0,1}^n -> {+1,-1}, use normalized Walsh coefficients
    fhat(S)=2^{-n} sum_x f(x)(-1)^{S.x}.
The spectral law is mu(S)=fhat(S)^2.
We test exactly whether mu is the product of its coordinate marginals.
All arithmetic is integer/Fraction; no floating point is used.
"""
from fractions import Fraction
import json


def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def product_profile(vals, n):
    N = 1 << n
    w = fwht_int(vals)              # fhat = w/N
    q = [z*z for z in w]            # mu numerator over N^2
    total = N*N
    rnum = [
        sum(q[s] for s in range(N) if (s >> i) & 1)
        for i in range(n)
    ]
    scale = total ** (n-1)
    for s in range(N):
        rhs = 1
        for i, r in enumerate(rnum):
            rhs *= r if ((s >> i) & 1) else total-r
        if q[s] * scale != rhs:
            return None
    return tuple(Fraction(r, total) for r in rnum)


def main():
    out = {"arithmetic": "exact_integer_and_Fraction", "dimensions": {}}
    for n in range(1, 5):
        N = 1 << n
        profile_counts = {}
        violations = 0
        # Fix f(0)=+1 and double for global sign.
        for mask in range(1 << (N-1)):
            vals = [1] + [
                -1 if ((mask >> (j-1)) & 1) else 1
                for j in range(1, N)
            ]
            r = product_profile(vals, n)
            if r is None:
                continue
            key = tuple(str(x) for x in r)
            profile_counts[key] = profile_counts.get(key, 0) + 2
            half_count = sum(x == Fraction(1, 2) for x in r)
            if any(x not in (0, Fraction(1, 2), 1) for x in r):
                violations += 2
            elif half_count % 2:
                violations += 2
        out["dimensions"][str(n)] = {
            "boolean_functions_total": 2**N,
            "product_spectral_functions": sum(profile_counts.values()),
            "distinct_product_profiles": len(profile_counts),
            "classification_violations": violations,
            "profiles": [
                {"marginals": list(k), "function_count": v}
                for k, v in sorted(profile_counts.items())
            ],
        }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
