#!/usr/bin/env python3
"""Direct Walsh checks for the separated-core rare-switch hierarchy theorem.

Command:
  python verify_separated_hierarchy.py
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import itertools
import math
import random

getcontext().prec = 70
D = Decimal
LN2 = D(2).ln()
E = D(1).exp()
SEED = 2026101205
TOL = D("1e-55")


def log2(x):
    return x.ln() / LN2


def mpq(q):
    return D(q.numerator) / q.denominator


def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def upper_masses(prob):
    pi = list(prob)
    n = int(math.log2(len(pi)))
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                pi[s] += pi[s | bit]
    return pi


def U(truth):
    n = int(math.log2(len(truth)))
    den = 1 << (2 * n)
    prob = [Fraction(w * w, den) for w in fwht(truth)]
    pi = upper_masses(prob)
    return sum((mpq(q) * log2(mpq(t / q)) for q, t in zip(prob, pi) if q), D(0))


def defect_rate(truth):
    return D(sum(x == -1 for x in truth)) / len(truth)


def M(r):
    y = (1 - 2 * r) ** 2
    return D(0) if y == 0 else y * log2(1 / y)


def switch(g0, g1, d):
    """Fresh d-bit rare switch; child variable blocks are physically disjoint."""
    n0 = int(math.log2(len(g0)))
    n1 = int(math.log2(len(g1)))
    mask = (1 << d) - 1
    ans = []
    for index in range(1 << (d + n0 + n1)):
        z = index & mask
        x = (index >> d) & ((1 << n0) - 1)
        y = index >> (d + n0)
        ans.append(g1[y] if z == 0 else g0[x])
    return tuple(ans)


def switch_formula(g0, g1, d):
    p = D(2) ** (-d)
    r0, r1 = defect_rate(g0), defect_rate(g1)
    rbar = (1 - p) * r0 + p * r1
    q0, q1 = 4 * r0 * (1 - r0), 4 * r1 * (1 - r1)
    delta2 = (r1 - r0) ** 2
    theta = r0 + r1 - 2 * r0 * r1
    overlap_log = D(0) if delta2 == 0 else delta2 * log2(theta / delta2)
    return (M(rbar) + (1 - p) * (U(g0) - M(r0)) + p * (U(g1) - M(r1))
            + q0 * ((1 - p) ** 2 * log2(1 / (1 - p)) + p * d / 2 - p * p * d)
            + q1 * p * d / 2
            + (2 * p * d - 4 * p * p * d) * delta2
            + 4 * (p - p * p) * overlap_log)


def coordinate_influence(truth, i):
    bit = 1 << i
    return D(sum(truth[x] != truth[x ^ bit] for x in range(len(truth)))) / len(truth)


L_M = 4 * (1 + 2 / E) / LN2
C_SEP = 3 + L_M + 2 / LN2 + 2 / (E * LN2)


class Tree:
    def __init__(self, truth, selectors=(), leaves=None):
        self.truth = tuple(truth)
        self.n = int(math.log2(len(truth)))
        self.selectors = tuple(selectors)
        self.leaves = [(D(1), U(self.truth))] if leaves is None else list(leaves)


def join(left, right, d):
    p = D(2) ** (-d)
    truth = switch(left.truth, right.truth, d)
    selectors = (tuple(range(d))
                 + tuple(d + i for i in left.selectors)
                 + tuple(d + left.n + i for i in right.selectors))
    leaves = [((1 - p) * w, u) for w, u in left.leaves]
    leaves += [(p * w, u) for w, u in right.leaves]
    return Tree(truth, selectors, leaves)


def all_small_cores():
    ans = []
    for n in range(3):
        N = 1 << n
        for code in range(1 << N):
            ans.append(tuple(1 if code >> x & 1 else -1 for x in range(N)))
    return ans


def structured_cores():
    out = []
    out.append(tuple(-1 if x == 15 else 1 for x in range(16)))
    out.append(tuple(-1 if x.bit_count() % 2 else 1 for x in range(32)))
    # Quadratic bent function on four bits.
    out.append(tuple(-1 if (((x & 1) * ((x >> 1) & 1) +
                              ((x >> 2) & 1) * ((x >> 3) & 1)) % 2) else 1
                     for x in range(16)))
    # Two address bits select one of four data bits.
    out.append(tuple(1 if (x >> (2 + (x & 3))) & 1 else -1 for x in range(64)))
    # Disjoint tensor and an overlap-product leaf are allowed as terminal cores.
    out.append(tuple((1 if (x & 3) == 3 else -1) *
                     (1 if ((x >> 2) & 3) == 3 else -1) for x in range(16)))
    out.append(tuple((1 if (x & 3) == 3 else -1) *
                     (1 if ((x >> 1) & 3) == 3 else -1) for x in range(8)))
    return out


def main():
    max_formula_error = D(0)
    min_node_margin = D("Infinity")
    node_cases = 0
    cores = all_small_cores()
    for g0, g1 in itertools.product(cores, repeat=2):
        for d in range(1, 5):
            f = switch(g0, g1, d)
            exact = U(f)
            formula = switch_formula(g0, g1, d)
            max_formula_error = max(max_formula_error, abs(exact - formula))
            p = D(2) ** (-d)
            theta = defect_rate(g0) + defect_rate(g1) - 2 * defect_rate(g0) * defect_rate(g1)
            charge = exact - (1 - p) * U(g0) - p * U(g1)
            margin = C_SEP * (2 * p * d * theta) - charge
            min_node_margin = min(min_node_margin, margin)
            node_cases += 1

    rng = random.Random(SEED)
    big = structured_cores()
    for _ in range(40):
        big.append(tuple(rng.choice((-1, 1)) for _ in range(16)))
    structured_cases = 0
    for k in range(60):
        g0, g1 = rng.choice(big), rng.choice(big)
        # Keep direct Walsh tables within a bounded pilot.
        if int(math.log2(len(g0))) + int(math.log2(len(g1))) > 9:
            continue
        for d in (1, 2):
            f = switch(g0, g1, d)
            max_formula_error = max(max_formula_error, abs(U(f) - switch_formula(g0, g1, d)))
            structured_cases += 1

    # Direct arbitrary-depth chain and balanced-tree telescopes.
    one_bit = [tuple(1 if code >> x & 1 else -1 for x in range(2)) for code in range(4)]
    tree_cases = 0
    min_tree_margin = D("Infinity")
    for _ in range(120):
        t = Tree(rng.choice(one_bit))
        for _depth in range(rng.randint(1, 5)):
            t = join(Tree(rng.choice(one_bit)), t, 1)
        leaf_packet = sum((w * u for w, u in t.leaves), D(0))
        charge = U(t.truth) - leaf_packet
        isel = sum((coordinate_influence(t.truth, i) for i in t.selectors), D(0))
        min_tree_margin = min(min_tree_margin, C_SEP * isel - charge)
        tree_cases += 1
    for _ in range(80):
        a, b, c, d0 = [Tree(rng.choice(one_bit)) for _ in range(4)]
        t = join(join(a, b, 1), join(c, d0, 1), 1)
        leaf_packet = sum((w * u for w, u in t.leaves), D(0))
        charge = U(t.truth) - leaf_packet
        isel = sum((coordinate_influence(t.truth, i) for i in t.selectors), D(0))
        min_tree_margin = min(min_tree_margin, C_SEP * isel - charge)
        tree_cases += 1

    if max_formula_error > TOL or min_node_margin < -TOL or min_tree_margin < -TOL:
        raise AssertionError((max_formula_error, min_node_margin, min_tree_margin))
    print(f"seed={SEED}")
    print(f"exhaustive_node_cases={node_cases}")
    print(f"structured_node_cases={structured_cases}")
    print(f"direct_tree_cases={tree_cases}")
    print(f"L_M={L_M:.20g}")
    print(f"C_sep={C_SEP:.20g}")
    print(f"max_formula_error={max_formula_error:.8g}")
    print(f"min_node_margin={min_node_margin:.12g}")
    print(f"min_tree_margin={min_tree_margin:.12g}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
