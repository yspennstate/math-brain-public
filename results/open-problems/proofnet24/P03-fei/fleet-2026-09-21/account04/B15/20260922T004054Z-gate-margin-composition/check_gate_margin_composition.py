#!/usr/bin/env python3
"""Deterministic self-check for the FEI gate slack/margin composition identities.
Standard library only.  This is evidence for algebraic formulas proved in REPORT.md,
not a finite proof of FEI.
"""
import itertools
import math
import random


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def V(p):
    return 4.0 * p * (1.0 - p)


# Deliberately arbitrary symmetric endpoint-zero potential.
# The composition identities are claimed for every such Gamma, so a non-FEI
# potential is useful as an implementation cross-check.
def Gamma(p):
    v = V(p)
    return 0.73 * v + 0.19 * v * v + 0.07 * v * v * v


def gate_stats(vals, ps):
    k = len(ps)
    n = 1 << k
    assert len(vals) == n
    coeff = []
    for mask in range(n):
        total = 0.0
        for x in range(n):
            prob = 1.0
            basis = 1.0
            for i, p in enumerate(ps):
                bit = (x >> i) & 1
                y = 1.0 if bit else -1.0
                mu = 2.0 * p - 1.0
                prob *= p if bit else (1.0 - p)
                if (mask >> i) & 1:
                    basis *= (y - mu) / math.sqrt(V(p))
            total += prob * vals[x] * basis
        coeff.append(total)

    q = [a * a for a in coeff]
    s = sum(q)
    if abs(s - 1.0) > 2e-11:
        raise AssertionError(("parseval", s))
    H = -sum(z * math.log2(z) for z in q if z > 0.0)
    its = []
    for i in range(k):
        its.append(sum(q[mask] for mask in range(n) if (mask >> i) & 1))
    I = sum(its)
    mu_out = sum(
        (math.prod(ps[i] if (x >> i) & 1 else (1.0 - ps[i]) for i in range(k))) * vals[x]
        for x in range(n)
    )
    p_out = (1.0 + mu_out) / 2.0
    D = sum(its[i] * (Gamma(ps[i]) + h2(V(ps[i]))) / V(ps[i]) for i in range(k)) - Gamma(p_out) - H
    Q = I / 4.0 - p_out * (1.0 - p_out)
    return {
        "H": H,
        "its": its,
        "I": I,
        "pout": p_out,
        "D": D,
        "Q": Q,
        "coeff": coeff,
    }


def compose_vals(outer, inners):
    sizes = [int(round(math.log2(len(v)))) for v in inners]
    n = sum(sizes)
    offsets = []
    cur = 0
    for s in sizes:
        offsets.append(cur)
        cur += s
    vals = []
    for x in range(1 << n):
        macro = 0
        for i, inner in enumerate(inners):
            mask = (1 << sizes[i]) - 1
            z = (x >> offsets[i]) & mask
            if inner[z] > 0:
                macro |= 1 << i
        vals.append(outer[macro])
    return vals


def random_gate(k, rng):
    while True:
        v = [rng.choice((-1.0, 1.0)) for _ in range(1 << k)]
        if min(v) != max(v):
            return v


def output_bias(vals, ps):
    k = len(ps)
    mu = 0.0
    for x, y in enumerate(vals):
        prob = math.prod(ps[i] if (x >> i) & 1 else (1.0 - ps[i]) for i in range(k))
        mu += prob * y
    return (1.0 + mu) / 2.0


def main():
    rng = random.Random(20260922004054)
    max_D = 0.0
    max_Q = 0.0
    max_c = 0.0
    comps = 0
    cbars = 0

    for _ in range(800):
        m = rng.choice((2, 3))
        outer = random_gate(m, rng)
        inners = []
        inner_ps = []
        macro_ps = []
        ok = True
        for _i in range(m):
            k = rng.choice((1, 2, 3))
            g = random_gate(k, rng)
            ps = [rng.uniform(0.08, 0.92) for _ in range(k)]
            po = output_bias(g, ps)
            if not (1e-7 < po < 1.0 - 1e-7):
                ok = False
                break
            inners.append(g)
            inner_ps.append(ps)
            macro_ps.append(po)
        if not ok or sum(len(p) for p in inner_ps) > 8:
            continue

        flat_ps = list(itertools.chain.from_iterable(inner_ps))
        F = compose_vals(outer, inners)
        sf = gate_stats(F, flat_ps)
        sa = gate_stats(outer, macro_ps)
        sb = [gate_stats(inners[i], inner_ps[i]) for i in range(m)]

        lam = [sa["its"][i] / V(macro_ps[i]) for i in range(m)]
        D_rhs = sa["D"] + sum(lam[i] * sb[i]["D"] for i in range(m))
        Q_rhs = sa["Q"] + sum(lam[i] * sb[i]["Q"] for i in range(m))
        max_D = max(max_D, abs(sf["D"] - D_rhs))
        max_Q = max(max_Q, abs(sf["Q"] - Q_rhs))
        if abs(sf["D"] - D_rhs) > 5e-11:
            raise AssertionError(("D", sf["D"], D_rhs))
        if abs(sf["Q"] - Q_rhs) > 5e-11:
            raise AssertionError(("Q", sf["Q"], Q_rhs))

        comps += 1
        if sf["Q"] > 1e-8:
            weighted = 0.0
            weight = 0.0
            if sa["Q"] > 1e-10:
                weighted += sa["Q"] * (-sa["D"] / sa["Q"])
                weight += sa["Q"]
            for i in range(m):
                if sb[i]["Q"] > 1e-10 and lam[i] > 1e-12:
                    weighted += lam[i] * sb[i]["Q"] * (-sb[i]["D"] / sb[i]["Q"])
                    weight += lam[i] * sb[i]["Q"]
            if weight > 1e-9:
                cf = -sf["D"] / sf["Q"]
                cb = weighted / weight
                max_c = max(max_c, abs(cf - cb))
                if abs(cf - cb) > 2e-9:
                    raise AssertionError(("c", cf, cb))
                cbars += 1

    print("PASS")
    print("compositions_checked =", comps)
    print("margin_barycenters_checked =", cbars)
    print("max_abs_D_identity_error = %.3e" % max_D)
    print("max_abs_Q_identity_error = %.3e" % max_Q)
    print("max_abs_c_barycenter_error = %.3e" % max_c)


if __name__ == "__main__":
    main()
