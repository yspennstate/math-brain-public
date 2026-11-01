#!/usr/bin/env python3
"""Reproduce B13 block-spectral-channel finite checks and sharp bent family.

Standard library only. This is supporting computation, not a proof of full FEI.
"""
import itertools
import json
import math


def fwht(values):
    a = [float(v) for v in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]


def entropy(p):
    return -sum(x*math.log2(x) for x in p if x > 0.0)


def influences(values, n):
    N = 1 << n
    return [
        sum(values[x] != values[x ^ (1 << j)] for x in range(N)) / N
        for j in range(n)
    ]


def local_spectrum(values, n, X, Y, y):
    base = 0
    for t, j in enumerate(Y):
        if (y >> t) & 1:
            base |= 1 << j
    restricted = []
    for xx in range(1 << len(X)):
        z = base
        for t, j in enumerate(X):
            if (xx >> t) & 1:
                z |= 1 << j
        restricted.append(values[z])
    coeff = fwht(restricted)
    return [c*c for c in coeff]


def block_channel(values, n, X):
    X = tuple(X)
    Y = tuple(j for j in range(n) if j not in X)
    spectra = [local_spectrum(values, n, X, Y, y)
               for y in range(1 << len(Y))]
    marginal = [sum(p[i] for p in spectra)/len(spectra)
                for i in range(len(spectra[0]))]
    mutual_info = entropy(marginal) - sum(entropy(p) for p in spectra)/len(spectra)
    inf = influences(values, n)
    outside_influence = sum(inf[j] for j in Y)
    return mutual_info, outside_influence, inf


def exhaustive(n):
    N = 1 << n
    best = (-1.0, None)
    # Fix the first truth-table value to +1, quotienting global negation.
    for mask in range(1 << (N-1)):
        values = [1] + [1 if (mask >> (i-1)) & 1 else -1 for i in range(1, N)]
        for r in range(1, n):
            for X in itertools.combinations(range(n), r):
                mi, iout, inf = block_channel(values, n, X)
                if iout > 0.0:
                    ratio = mi/iout
                    if ratio > best[0] + 1e-12:
                        best = (ratio, {
                            "truth_mask_after_fixed_first_value": mask,
                            "block_X": list(X),
                            "mutual_information_bits": mi,
                            "outside_influence": iout,
                            "influences": inf,
                        })
    return {"n": n, "max_ratio": best[0], "witness": best[1]}


def bent_truth(k):
    assert k % 2 == 0
    out = []
    for x in range(1 << k):
        bit = 0
        for r in range(0, k, 2):
            bit ^= ((x >> r) & 1) & ((x >> (r+1)) & 1)
        out.append(-1 if bit else 1)
    return out


def js(p, q):
    m = [(x+y)/2.0 for x, y in zip(p, q)]
    return entropy(m) - 0.5*entropy(p) - 0.5*entropy(q)


def bent_flip_ratio(k):
    h = bent_truth(k)
    hp = list(h)
    hp[0] *= -1
    p = [c*c for c in fwht(h)]
    q = [c*c for c in fwht(hp)]
    delta = 1.0/len(h)
    return js(p, q)/delta


result = {
    "universal_constant_2_over_ln2": 2.0/math.log(2.0),
    "exhaustive_global_sign_quotiented": [exhaustive(n) for n in (2, 3, 4)],
    "bent_one_point_flip": [
        {"k": k, "ratio_JS_over_outside_influence": bent_flip_ratio(k)}
        for k in (2, 4, 6, 8, 10, 12)
    ],
    "classification": {
        "finite_exhaustion": "computational evidence only",
        "bent_family_limit": "analytic sharpness target; numerics are a reproducer",
        "full_FEI": "OPEN"
    }
}
print(json.dumps(result, indent=2, sort_keys=True))
