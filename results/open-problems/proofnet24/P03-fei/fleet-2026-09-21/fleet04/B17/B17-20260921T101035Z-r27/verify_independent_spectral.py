#!/usr/bin/env python3
"""Exact small-n check for the independent-spectral-sample FEI lemma.

Enumerates Boolean functions f:{0,1}^n->{-1,+1} for n<=4 up to global negation.
The Walsh transform is integer-exact.  It tests whether the squared normalized
Fourier coefficients factor as a product Bernoulli law, and if so records the
coordinate marginals exactly.
"""
from fractions import Fraction
import json

def fwht(vals):
    a = list(vals)
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def independent_params(vals, n):
    W = fwht(vals)
    N = 1 << n
    den = N*N
    weights = [w*w for w in W]
    p = []
    for i in range(n):
        num = sum(weights[s] for s in range(N) if (s >> i) & 1)
        p.append(Fraction(num, den))
    for s, w2 in enumerate(weights):
        q = Fraction(1, 1)
        for i, pi in enumerate(p):
            q *= pi if ((s >> i) & 1) else (1-pi)
        if Fraction(w2, den) != q:
            return None
    return tuple(p)

def h2_fraction(p):
    # Only called on 0,1/2,1 after the theorem check.
    if p in (Fraction(0), Fraction(1)):
        return Fraction(0)
    if p == Fraction(1, 2):
        return Fraction(1)
    raise ValueError("unexpected marginal")

def main():
    out = {"dimensions": []}
    allowed = {Fraction(0), Fraction(1,2), Fraction(1)}
    for n in range(1, 5):
        N = 1 << n
        found = []
        # Fix f(0)=+1; global negation leaves squared spectrum unchanged.
        for bits in range(1 << (N-1)):
            vals = [1] + [1 if (bits >> (k-1)) & 1 else -1 for k in range(1, N)]
            p = independent_params(vals, n)
            if p is None:
                continue
            assert all(pi in allowed for pi in p), (n, p)
            H = sum(h2_fraction(pi) for pi in p)
            I = sum(p)
            if I:
                assert H <= 2*I
            found.append(p)
        uniq = sorted(set(found))
        out["dimensions"].append({
            "n": n,
            "boolean_functions_up_to_global_negation": 1 << (N-1),
            "independent_spectral_count": len(found),
            "unique_parameter_vectors": [
                [f"{x.numerator}/{x.denominator}" for x in p] for p in uniq
            ],
            "unique_parameter_vector_count": len(uniq),
        })
    out["status"] = "PASS"
    out["claim_checked"] = "For n<=4, every independent spectral sample has p_i in {0,1/2,1}, hence H<=2I."
    print(json.dumps(out, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
