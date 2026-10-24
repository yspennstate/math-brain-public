#!/usr/bin/env python3
"""Exact-algebra regression for B18 decomposable-gate margin telescope.

Uses a synthetic symmetric Gamma only to verify identities that are algebraic
and Gamma-independent. No certificate data or benchmark answers are used.
"""
import math
import random
from functools import lru_cache

TOL = 5e-10

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0-p) * math.log2(1.0-p)

def Gamma(p):
    # Smooth symmetric boundary-zero test potential.
    return p * (1.0-p) * (2.3 + 0.7 * (1.0-2.0*p)**2)

def gate_stats(tt, k, ps):
    n = 1 << k
    vals = [-1.0 if ((tt >> x) & 1) else 1.0 for x in range(n)]
    coeff = []
    for S in range(n):
        c = 0.0
        for x in range(n):
            fac = 1.0
            for i, p in enumerate(ps):
                bit = (x >> i) & 1
                if (S >> i) & 1:
                    fac *= math.sqrt(p * (1.0-p)) * (1.0 if bit == 0 else -1.0)
                else:
                    fac *= p if bit else (1.0-p)
            c += vals[x] * fac
        coeff.append(c)

    pS = [c*c for c in coeff]
    Ht = -sum(w * math.log2(w) for w in pS if w > 1e-300)
    pout = (1.0 - coeff[0]) / 2.0
    Its = [
        sum(pS[S] for S in range(n) if (S >> i) & 1)
        for i in range(k)
    ]
    base = []
    for p in ps:
        V = 4.0 * p * (1.0-p)
        base.append((Gamma(p) + h2(V)) / V)
    D = sum(a*b for a, b in zip(Its, base)) - Ht - Gamma(pout)
    I = sum(Its)
    W = I/4.0 - pout*(1.0-pout)
    return {"Ht": Ht, "pout": pout, "Its": Its, "I": I, "D": D, "W": W}

def eval_tt(tt, k, bits):
    x = sum((b & 1) << i for i, b in enumerate(bits))
    return (tt >> x) & 1

def composite_tt(outer_tt, children):
    ks = [k for _, k in children]
    K = sum(ks)
    out_tt = 0
    for x in range(1 << K):
        pos = 0
        ys = []
        for child_tt, ck in children:
            ys.append(eval_tt(
                child_tt, ck,
                [(x >> (pos+j)) & 1 for j in range(ck)]
            ))
            pos += ck
        if eval_tt(outer_tt, len(children), ys):
            out_tt |= 1 << x
    return out_tt, K

def random_composition_regression(seed=180022, tests=3000):
    rng = random.Random(seed)
    max_D = max_W = max_I = 0.0
    failures = 0
    used = 0

    for _ in range(tests):
        m = rng.randint(2, 3)
        ks = [rng.choice((1, 2)) for _ in range(m)]
        while sum(ks) > 5:
            ks[rng.randrange(m)] = 1

        children = []
        leaf_ps = []
        for k in ks:
            if k == 1:
                ctt = rng.choice((1, 2))
            else:
                ctt = rng.randrange(1, (1 << (1 << k)) - 1)
            children.append((ctt, k))
            leaf_ps.extend(rng.uniform(0.03, 0.97) for _ in range(k))
        outer_tt = rng.randrange(1 << (1 << m))
        full_tt, K = composite_tt(outer_tt, children)
        full = gate_stats(full_tt, K, leaf_ps)

        child_stats = []
        qs = []
        pos = 0
        for child_tt, k in children:
            ps = leaf_ps[pos:pos+k]
            pos += k
            st = gate_stats(child_tt, k, ps)
            child_stats.append(st)
            qs.append(st["pout"])

        # Constant children are boundary cases; the theorem treats them by
        # continuity, while this interior identity test keeps V(q_i)>0.
        if any(q < 1e-12 or q > 1.0-1e-12 for q in qs):
            continue

        outer = gate_stats(outer_tt, m, qs)
        alpha = [
            outer["Its"][i] / (4.0 * qs[i] * (1.0-qs[i]))
            for i in range(m)
        ]
        pred_D = outer["D"] + sum(
            a * st["D"] for a, st in zip(alpha, child_stats)
        )
        pred_W = outer["W"] + sum(
            a * st["W"] for a, st in zip(alpha, child_stats)
        )
        pred_I = sum(
            a * st["I"] for a, st in zip(alpha, child_stats)
        )

        eD = abs(full["D"] - pred_D)
        eW = abs(full["W"] - pred_W)
        eI = abs(full["I"] - pred_I)
        max_D = max(max_D, eD)
        max_W = max(max_W, eW)
        max_I = max(max_I, eI)
        failures += int(max(eD, eW, eI) > TOL)
        used += 1

    return used, failures, max_D, max_W, max_I

def truth_var(n, i):
    tt = 0
    for x in range(1 << n):
        if (x >> i) & 1:
            tt |= 1 << x
    return tt

def binary_formula_truth_tables(n):
    """All truth tables representable by a disjoint-variable binary tree
    with an arbitrary Boolean 2-input gate at every internal node.
    """
    full_tt = (1 << (1 << n)) - 1

    @lru_cache(None)
    def rec(mask):
        vs = [i for i in range(n) if (mask >> i) & 1]
        if len(vs) == 1:
            v = truth_var(n, vs[0])
            return frozenset((v, full_tt ^ v))

        out = set()
        low = vs[0]
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other and ((sub >> low) & 1):
                A, B = rec(sub), rec(other)
                for ta in A:
                    na = full_tt ^ ta
                    for tb in B:
                        nb = full_tt ^ tb
                        atoms = (na & nb, ta & nb, na & tb, ta & tb)
                        for op in range(16):
                            t = 0
                            for j, atom in enumerate(atoms):
                                if (op >> j) & 1:
                                    t |= atom
                            out.add(t)
            sub = (sub - 1) & mask
        return frozenset(out)

    return rec((1 << n) - 1)

def depends_all(tt, n):
    for i in range(n):
        if all(
            ((tt >> x) & 1) == ((tt >> (x ^ (1 << i))) & 1)
            for x in range(1 << n)
        ):
            return False
    return True

used, failures, maxD, maxW, maxI = random_composition_regression()
print("PASS" if failures == 0 else "FAIL")
print(f"composition_cases={used}")
print(f"composition_failures={failures}")
print(f"max_abs_D_identity_error={maxD:.3e}")
print(f"max_abs_W_identity_error={maxW:.3e}")
print(f"max_abs_I_identity_error={maxI:.3e}")

for n in range(2, 6):
    safe = binary_formula_truth_tables(n)
    full_dep = sum(depends_all(tt, n) for tt in safe)
    print(
        f"binary_decomposable_arity_{n}: "
        f"all={len(safe)} fully_dependent={full_dep}"
    )
