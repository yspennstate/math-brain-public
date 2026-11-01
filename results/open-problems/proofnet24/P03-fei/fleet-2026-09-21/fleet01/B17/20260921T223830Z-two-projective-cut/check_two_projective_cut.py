#!/usr/bin/env python3
import itertools, math, random

def vals_from_mask(mask, n):
    return [(mask >> x) & 1 for x in range(1 << n)]

def influence(vals, n):
    N = 1 << n
    return sum(
        sum(vals[x] != vals[x ^ (1 << i)] for x in range(N)) / N
        for i in range(n)
    )

def build(c, h0, h1, a, b):
    nx, ny = 1 << a, 1 << b
    return [[h1[y] if c[x] else h0[y] for y in range(ny)] for x in range(nx)]

def delta_rank_one(E):
    nx, ny = len(E), len(E[0])
    best = 1.0
    for mask in range(1 << (ny - 1)):
        v = [0] + [((mask >> (y - 1)) & 1) for y in range(1, ny)]
        err = 0
        for x in range(nx):
            r = sum(E[x][y] ^ v[y] for y in range(ny))
            err += min(r, ny - r)
        best = min(best, err / (nx * ny))
    return best

def cut_W(E, a, b):
    nx, ny = 1 << a, 1 << b
    W = 0.0
    for i in range(a):
        for j in range(b):
            bad = 0
            for x in range(nx):
                xx = x ^ (1 << i)
                for y in range(ny):
                    yy = y ^ (1 << j)
                    bad += E[x][y] ^ E[xx][y] ^ E[x][yy] ^ E[xx][yy]
            W += bad / (nx * ny)
    return W

def one_case(c, h0, h1, a, b):
    alpha = min(sum(c) / len(c), 1 - sum(c) / len(c))
    s = [u ^ v for u, v in zip(h0, h1)]
    d = min(sum(s) / len(s), 1 - sum(s) / len(s))
    Ic, Is = influence(c, a), influence(s, b)
    E = build(c, h0, h1, a, b)
    delta = delta_rank_one(E)
    W = cut_W(E, a, b)
    formula_err = max(abs(delta - alpha * d), abs(W - Ic * Is))
    rhs = 0.0 if delta == 0 else 2 * delta * math.log2(1 / delta)
    strong = 0.0 if alpha == 0 or d == 0 else 4 * alpha * d * math.log2(1 / alpha) * math.log2(1 / d)
    return formula_err, W - rhs, W - strong, (alpha, d, Ic, Is, delta, W, rhs, strong)

def exhaustive_2_2():
    max_formula_err = 0.0
    min_log_slack = float("inf")
    min_strong_slack = float("inf")
    equality = None
    count = 0
    for cm in range(1 << 4):
        c = vals_from_mask(cm, 2)
        for m0 in range(1 << 4):
            h0 = vals_from_mask(m0, 2)
            for m1 in range(1 << 4):
                h1 = vals_from_mask(m1, 2)
                fe, ls, ss, stats = one_case(c, h0, h1, 2, 2)
                max_formula_err = max(max_formula_err, fe)
                if stats[4] > 0:
                    if ls < min_log_slack:
                        min_log_slack, equality = ls, (cm, m0, m1, stats)
                    min_strong_slack = min(min_strong_slack, ss)
                count += 1
    return count, max_formula_err, min_log_slack, min_strong_slack, equality

def seeded_3_3(samples=512, seed=1701):
    rng = random.Random(seed)
    max_formula_err = 0.0
    min_log_slack = float("inf")
    min_strong_slack = float("inf")
    for _ in range(samples):
        c = [rng.randrange(2) for _ in range(8)]
        h0 = [rng.randrange(2) for _ in range(8)]
        h1 = [rng.randrange(2) for _ in range(8)]
        fe, ls, ss, stats = one_case(c, h0, h1, 3, 3)
        max_formula_err = max(max_formula_err, fe)
        if stats[4] > 0:
            min_log_slack = min(min_log_slack, ls)
            min_strong_slack = min(min_strong_slack, ss)
    return samples, max_formula_err, min_log_slack, min_strong_slack

if __name__ == "__main__":
    a = exhaustive_2_2()
    b = seeded_3_3()
    print("B17 two-projective-row cut checker")
    print("full_FEI=OPEN_NOT_PROVED")
    print("exhaustive_2x2_cases", a[0])
    print("max_formula_error", format(a[1], ".17g"))
    print("min_open_cut_slack", format(a[2], ".17g"))
    print("min_strong_product_slack", format(a[3], ".17g"))
    print("equality_witness", a[4])
    print("seeded_3x3_cases", b[0])
    print("seeded_max_formula_error", format(b[1], ".17g"))
    print("seeded_min_open_cut_slack", format(b[2], ".17g"))
    print("seeded_min_strong_product_slack", format(b[3], ".17g"))
    assert a[1] == 0.0 and a[2] >= -1e-12 and a[3] >= -1e-12
    assert b[1] == 0.0 and b[2] >= -1e-12 and b[3] >= -1e-12
    print("PASS")
