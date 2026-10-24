#!/usr/bin/env python3
"""Self-check for B16 translation-averaged XOR-fiber uncertainty ledger.

Scientific scope:
- exact rational verification of the mixture and influence identities;
- floating Shannon-entropy verification of the entropy ledger and J <= M;
- exact endpoint checks for quadratic bent phases in n=4.

This is a self-check of the derived identities, not an end-to-end FEI proof.
"""
from fractions import Fraction
from itertools import product
from math import log2
import json
import random

SEED = 20260921

def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def spec_prob(vals):
    N = len(vals)
    return [Fraction(w*w, N*N) for w in fwht_int(vals)]

def entropy(p):
    return sum(-float(x)*log2(float(x)) for x in p if x)

def influence_frac(p):
    return sum(prob * s.bit_count() for s, prob in enumerate(p))

def shift(vals, z):
    return [vals[x ^ z] for x in range(len(vals))]

def pointwise_product(arrs):
    out = []
    for x in range(len(arrs[0])):
        v = 1
        for a in arrs:
            v *= a[x]
        out.append(v)
    return out

def xor_convolution(ps):
    q = list(ps[0])
    N = len(q)
    for p in ps[1:]:
        nxt = [Fraction(0) for _ in range(N)]
        for a, pa in enumerate(q):
            if not pa:
                continue
            for b, pb in enumerate(p):
                if pb:
                    nxt[a ^ b] += pa * pb
        q = nxt
    return q

def xor_influence_from_marginals(ps, n):
    ans = Fraction(0)
    for i in range(n):
        prodcorr = Fraction(1)
        for p in ps:
            ji = sum((prob for s, prob in enumerate(p) if (s >> i) & 1), Fraction(0))
            prodcorr *= 1 - 2*ji
        ans += (1 - prodcorr) / 2
    return ans

def translated_family(vals_list):
    m = len(vals_list)
    N = len(vals_list[0])
    for zs in product(range(N), repeat=m-1):
        arrs = [vals_list[0]]
        arrs.extend(shift(vals_list[j+1], zs[j]) for j in range(m-1))
        yield zs, spec_prob(pointwise_product(arrs))

def ledger(vals_list):
    N = len(vals_list[0])
    n = N.bit_length() - 1
    ps = [spec_prob(v) for v in vals_list]
    q = xor_convolution(ps)
    Hs = [entropy(p) for p in ps]
    translated = list(translated_family(vals_list))
    K = len(translated)
    mixture = [
        sum((pz[s] for _, pz in translated), Fraction(0)) / K
        for s in range(N)
    ]
    avgH = sum(entropy(pz) for _, pz in translated) / K
    M = sum(Hs) - entropy(q)
    J = entropy(q) - avgH
    avgI = sum((influence_frac(pz) for _, pz in translated), Fraction(0)) / K
    Iq = xor_influence_from_marginals(ps, n)
    return {
        "n": n,
        "m": len(vals_list),
        "mix_exact": mixture == q,
        "influence_exact": avgI == Iq,
        "entropy_error": abs(avgH - (sum(Hs) - M - J)),
        "uncertainty_margin": M - J,
        "M": M,
        "J": J,
        "avgH": avgH,
        "sumH": sum(Hs),
        "avgI": float(avgI),
        "Iq": float(Iq),
    }

def all_bool(n):
    N = 1 << n
    for mask in range(1 << N):
        yield [1 if (mask >> x) & 1 else -1 for x in range(N)]

def quad_phase(n, edges):
    out = []
    for x in range(1 << n):
        q = 0
        for i, j in edges:
            q ^= ((x >> i) & 1) & ((x >> j) & 1)
        out.append(-1 if q else 1)
    return out

def spectrum_shape(p):
    nz = [x for x in p if x]
    return {
        "support": len(nz),
        "distinct_nonzero": sorted({str(x) for x in nz}),
    }

def main():
    tol = 2e-12
    exact_triplets = 0
    max_entropy_error = 0.0
    min_uncertainty_margin = float("inf")
    funcs = list(all_bool(2))
    for fs in product(funcs, repeat=3):
        out = ledger(fs)
        assert out["mix_exact"]
        assert out["influence_exact"]
        assert out["entropy_error"] <= tol
        assert out["uncertainty_margin"] >= -tol
        exact_triplets += 1
        max_entropy_error = max(max_entropy_error, out["entropy_error"])
        min_uncertainty_margin = min(min_uncertainty_margin, out["uncertainty_margin"])

    rng = random.Random(SEED)
    random_cases = 0
    random_max_entropy_error = 0.0
    random_min_margin = float("inf")
    random_max_ratio = 0.0
    for m in (2, 3, 4):
        for _ in range(64):
            fs = [[rng.choice((-1, 1)) for _ in range(8)] for _ in range(m)]
            out = ledger(fs)
            assert out["mix_exact"]
            assert out["influence_exact"]
            assert out["entropy_error"] <= tol
            assert out["uncertainty_margin"] >= -tol
            random_cases += 1
            random_max_entropy_error = max(random_max_entropy_error, out["entropy_error"])
            random_min_margin = min(random_min_margin, out["uncertainty_margin"])
            if out["M"] > tol:
                random_max_ratio = max(random_max_ratio, out["J"] / out["M"])

    q0 = quad_phase(4, [(0,1), (2,3)])
    q1 = quad_phase(4, [(0,1), (0,3), (1,2)])
    same = ledger([q0, q0])
    mismatch = ledger([q0, q1])

    # All q0 translated self-products must be characters: one spectral atom.
    same_supports = []
    for _, pz in translated_family([q0, q0]):
        same_supports.append(spectrum_shape(pz)["support"])
    assert set(same_supports) == {1}

    # q0 * shifted(q1) has the nondegenerate quadratic part q0+q1:
    # every translated product is bent, hence uniform spectrum.
    mismatch_shapes = []
    for _, pz in translated_family([q0, q1]):
        mismatch_shapes.append(spectrum_shape(pz))
    assert all(sh["support"] == 16 and sh["distinct_nonzero"] == ["1/16"]
               for sh in mismatch_shapes)

    assert abs(same["M"] - 4.0) <= tol and abs(same["J"] - 4.0) <= tol
    assert abs(mismatch["M"] - 4.0) <= tol and abs(mismatch["J"]) <= tol

    result = {
        "status": "PASS_SELF_CHECK",
        "scope": "translation_averaged_xor_fiber_uncertainty_ledger_only",
        "full_FEI_proved": False,
        "exhaustive_n2_ordered_triples": exact_triplets,
        "exhaustive_max_entropy_identity_error": max_entropy_error,
        "exhaustive_min_M_minus_J": min_uncertainty_margin,
        "random_n3_cases": random_cases,
        "random_max_entropy_identity_error": random_max_entropy_error,
        "random_min_M_minus_J": random_min_margin,
        "random_max_J_over_M": random_max_ratio,
        "bent_endpoints": {
            "same_quadratic": {
                "M": same["M"], "J": same["J"], "avg_output_entropy": same["avgH"],
                "translated_output_supports": sorted(set(same_supports)),
            },
            "nondegenerate_quadratic_difference": {
                "M": mismatch["M"], "J": mismatch["J"],
                "avg_output_entropy": mismatch["avgH"],
                "translated_output_support": 16,
                "translated_output_mass": "1/16",
            },
        },
        "interpretation": (
            "For identical quadratic bent phases the coherent information refund J saturates M; "
            "for a pair whose quadratic difference is also bent, J=0 although M is unchanged. "
            "Thus unsigned factor spectral laws and multiplicity do not lower-bound J."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
