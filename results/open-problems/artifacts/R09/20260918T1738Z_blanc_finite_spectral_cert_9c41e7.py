#!/usr/bin/env python3
from fractions import Fraction

def units(d):
    out = []
    for i in range(d):
        for s in (-1, 1):
            v = [0] * d
            v[i] = s
            out.append(tuple(v))
    return out

def add(x, y):
    return tuple(a + b for a, b in zip(x, y))

def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))

def off0(B, S, d):
    B = set(B)
    S = set(S)
    V = B - S
    z = (0,) * d
    if z not in V:
        return set()
    U = units(d)
    seen = {z}
    todo = [z]
    while todo:
        x = todo.pop()
        for u in U:
            y = add(x, u)
            if y in V and y not in seen:
                seen.add(y)
                todo.append(y)
    return seen

def live_states_size_le_2(d):
    U = units(d)
    z = (0,) * d
    clusters = [frozenset([z])] + [frozenset([z, e]) for e in U]
    states = []
    for A in clusters:
        typ = len(A)
        for tail in A:
            for u in U:
                head = add(tail, u)
                if head in A:  # terminal pointed state: omit
                    continue
                states.append((A, tail, head, typ))
    return states

def is_cut(Astate, Bstate, d):
    A, atail, ahead, _ = Astate
    B, btail, bhead, _ = Bstate
    deleted = {sub(x, ahead) for x in A}
    return btail not in off0(B, deleted, d)

def verify_counts(d):
    Om = 2 * d
    states = live_states_size_le_2(d)
    n1 = sum(1 for s in states if s[3] == 1)
    n2 = sum(1 for s in states if s[3] == 2)
    assert n1 == Om
    assert n2 == 2 * Om * (Om - 1)
    target1 = Om
    target2 = (Om - 1) * (2 * Om - 1)
    for A in states:
        c1 = c2 = 0
        for B in states:
            if not is_cut(A, B, d):
                if B[3] == 1:
                    c1 += 1
                else:
                    c2 += 1
        assert c1 == target1, (d, A, c1, target1)
        assert c2 == target2, (d, A, c2, target2)
    return len(states), target1, target2

def small_cluster_row_mass(d, p):
    Om = 2 * d
    mu1 = (1 - p) ** Om
    mu2 = p * (1 - p) ** (2 * Om - 2)
    return Om * mu1 + (Om - 1) * (2 * Om - 1) * mu2

def m0_lambda_bound(d, p):
    Om = 2 * d
    a = Om * p
    assert a < 1
    # For Lambda_0, chi_Lambda0=1 and phi_p(Lambda_0)=Omega p.
    return (1 - a) * small_cluster_row_mass(d, p) / Om

def main():
    print("R09 exact finite-state spectral certificate check")
    for d in (7, 8, 9, 10):
        Om = 2 * d
        n, t1, t2 = verify_counts(d)
        p = Fraction(1, 4 * d)  # Omega p = 1/2
        lb = m0_lambda_bound(d, p)
        single = (1 - Om * p) * (1 - p) ** Om
        gain = lb / single
        print(
            "d", d,
            "states", n,
            "noncut_targets=(%d,%d)" % (t1, t2),
            "p", p,
            "lambda_lb", lb,
            "lambda_lb_decimal", float(lb),
            "gain_over_singleton", float(gain),
        )
        assert lb > single > 0
    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
