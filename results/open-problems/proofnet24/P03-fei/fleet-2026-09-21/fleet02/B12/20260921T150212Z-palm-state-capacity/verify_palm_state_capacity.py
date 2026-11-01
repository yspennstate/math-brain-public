#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from collections import defaultdict
from fractions import Fraction

TOL = 2e-12


def entropy(probs):
    return -sum(x * math.log2(x) for x in probs if x > 0.0)


def walsh_spectrum(values):
    N = len(values)
    n = N.bit_length() - 1
    assert 1 << n == N
    out = []
    for mask in range(N):
        s = 0
        for x, fx in enumerate(values):
            s += fx * (-1 if ((x & mask).bit_count() & 1) else 1)
        out.append(Fraction(s, N))
    return out


def exact_subset(mask, n):
    return frozenset(i for i in range(n) if (mask >> i) & 1)


def exact_shadows(p, n):
    v = {}
    for mask in range(1 << n):
        A = exact_subset(mask, n)
        a = len(A)
        v[A] = sum(
            prob / math.comb(len(B), a)
            for B, prob in p.items()
            if A <= B
        )
    return v


def exact_palm_checks(p, n):
    """All probability identities use Fraction; entropy identity is checked in float."""
    v = exact_shadows(p, n)
    I = sum(Fraction(len(B)) * prob for B, prob in p.items())
    assert I > 0

    mu = {}
    joint_ax = defaultdict(Fraction)
    for mask in range(1 << n):
        A = exact_subset(mask, n)
        w = v[A] - p.get(A, Fraction(0))
        if w == 0:
            continue
        mu[A] = w / I
        a = len(A)
        for i in range(n):
            if i not in A:
                C = frozenset(set(A) | {i})
                r = v[C] / (Fraction(a + 1) * w)
                joint_ax[(A, i)] += mu[A] * r

    assert sum(mu.values()) == 1
    assert sum(joint_ax.values()) == 1
    pi = []
    for i in range(n):
        target = sum(prob for B, prob in p.items() if i in B) / I
        got = sum(q for (A, j), q in joint_ax.items() if j == i)
        assert got == target
        pi.append(target)

    sel = 0.0
    for A, muA in mu.items():
        a = len(A)
        w = v[A] - p.get(A, Fraction(0))
        r = []
        for i in range(n):
            if i not in A:
                C = frozenset(set(A) | {i})
                ri = v[C] / (Fraction(a + 1) * w)
                r.append(float(ri))
        post_residual_log = 0.0
        for B, prob in p.items():
            if A < B:
                post = prob / (Fraction(math.comb(len(B), a)) * w)
                post_residual_log += float(post) * math.log2(len(B) - a)
        j = entropy(r) - post_residual_log
        sel += float(muA) * j

    Hpi = entropy([float(x) for x in pi])
    PA = defaultdict(float)
    PX = defaultdict(float)
    joint = {}
    for key, q in joint_ax.items():
        qf = float(q)
        joint[key] = qf
        PA[key[0]] += qf
        PX[key[1]] += qf
    IAX = sum(
        q * math.log2(q / (PA[A] * PX[i]))
        for (A, i), q in joint.items()
        if q > 0
    )
    refund = sum(
        float(prob) * math.lgamma(len(B) + 1) / math.log(2.0)
        for B, prob in p.items()
    ) / float(I)
    rhs = Hpi - IAX - refund
    assert abs(sel - rhs) < TOL, (sel, rhs)
    return {
        "influence": float(I),
        "selector_per_influence": sel,
        "profile_entropy": Hpi,
        "prefix_next_mutual_information": IAX,
        "factorial_refund": refund,
        "identity_error": abs(sel - rhs),
        "pi": [float(x) for x in pi],
    }


def majority3_spectral_law():
    vals = []
    for x in range(8):
        bits = [1 if ((x >> j) & 1) else -1 for j in range(3)]
        vals.append(1 if sum(bits) > 0 else -1)
    coeff = walsh_spectrum(vals)
    return {exact_subset(mask, 3): c * c for mask, c in enumerate(coeff)}


def tribes_values(w, m):
    n = w * m
    vals = []
    for x in range(1 << n):
        fired = False
        for b in range(m):
            if all((x >> (b * w + j)) & 1 for j in range(w)):
                fired = True
                break
        vals.append(-1 if fired else 1)
    return vals


def tribes_formula(w, m):
    d = 2.0 ** (-w)
    q0 = 1.0 - d
    q = q0 ** m
    V = 4.0 * q * (1.0 - q)
    I = m * w * (2.0 ** (1 - w)) * (q0 ** (m - 1))
    Hloc = (-(d * math.log2(d) + q0 * math.log2(q0))) + d * math.log2((1 << w) - 1)
    Hcond = (m * Hloc - (-(q * math.log2(q) + (1.0 - q) * math.log2(1.0 - q)))) / (1.0 - q)
    H = (
        -(V * math.log2(V) + (1.0 - V) * math.log2(1.0 - V))
        if 0.0 < V < 1.0
        else 0.0
    ) + V * Hcond
    mu = m * d
    refund_upper = math.log2(w) + (1.0 - d + mu)
    n = m * w
    Hpi = math.log2(n)
    state_capacity_lower = Hpi - refund_upper
    return {
        "w": w,
        "m": m,
        "n": n,
        "q": q,
        "variance": V,
        "influence": I,
        "fourier_entropy": H,
        "H_over_I": H / I,
        "profile_entropy": Hpi,
        "factorial_refund_upper": refund_upper,
        "profile_minus_refund_upper": state_capacity_lower,
    }


def exact_tiny_tribes_check():
    w, m = 2, 3
    vals = tribes_values(w, m)
    coeff = walsh_spectrum(vals)
    ps = [c * c for c in coeff]
    I_exact = sum(Fraction(mask.bit_count()) * ps[mask] for mask in range(len(ps)))
    H_direct = entropy([float(p) for p in ps])
    formula = tribes_formula(w, m)
    assert I_exact == Fraction(27, 16)
    assert abs(float(I_exact) - formula["influence"]) < TOL
    assert abs(H_direct - formula["fourier_entropy"]) < TOL
    return {
        "w": w,
        "m": m,
        "influence_exact": "27/16",
        "entropy_direct": H_direct,
    }


def main():
    maj = exact_palm_checks(majority3_spectral_law(), 3)
    tiny = exact_tiny_tribes_check()
    kappa = math.log(2.0)
    rows = []
    for w in [4, 6, 8, 10, 12, 16, 20]:
        m = max(1, round(kappa * (1 << w)))
        rows.append(tribes_formula(w, m))

    assert rows[-1]["H_over_I"] > 3.9999
    assert rows[-1]["profile_minus_refund_upper"] > 0.85 * rows[-1]["w"]
    for a, b in zip(rows, rows[1:]):
        assert b["profile_minus_refund_upper"] > a["profile_minus_refund_upper"]

    out = {
        "status": "PASS",
        "exact_probability_checks": {
            "mu_normalization": True,
            "Palm_X_marginal_equals_normalized_influence": True,
            "majority3_entropy_identity_error": maj["identity_error"],
        },
        "majority3": maj,
        "tiny_tribes_exact": tiny,
        "balanced_tribes_rows": rows,
        "claims_checked": [
            "Palm continuation law and X marginal identity",
            "selector = profile entropy - prefix-next MI - factorial refund",
            "exact tiny tribes influence/entropy formulas",
            "balanced tribes H/I approaches 4",
            "low-state capacity lower bound grows linearly with block width",
        ],
        "scope": "engineering/mathematical self-check; finite diagnostics do not prove FEI",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
