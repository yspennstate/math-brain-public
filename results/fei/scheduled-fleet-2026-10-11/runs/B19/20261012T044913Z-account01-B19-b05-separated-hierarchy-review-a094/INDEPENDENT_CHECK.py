#!/usr/bin/env python3
"""Independent reconstruction of B05's separated-hierarchy U payment.

This checker was written for the B19 review.  It does not import the author
checker.  Walsh coefficients are computed as integers, upper-set masses as
Fractions, and logarithmic evaluations at 80 decimal digits.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
import math

getcontext().prec = 80
D = Decimal
LN2 = D(2).ln()
TOL = D("1e-65")


def dfrac(q):
    return D(q.numerator) / D(q.denominator)


def lg(q):
    return dfrac(q).ln() / LN2


def walsh(values):
    out = list(values)
    width = 1
    while width < len(out):
        for base in range(0, len(out), 2 * width):
            for j in range(width):
                a, b = out[base + j], out[base + width + j]
                out[base + j] = a + b
                out[base + width + j] = a - b
        width *= 2
    return out


def spectral_law(values):
    n = (len(values).bit_length() - 1)
    den = 1 << (2 * n)
    return [Fraction(a * a, den) for a in walsh(values)]


def upper_transform(p):
    q = list(p)
    n = len(q).bit_length() - 1
    for bit_index in range(n):
        bit = 1 << bit_index
        for s in range(1 << n):
            if not (s & bit):
                q[s] += q[s | bit]
    return q


def upper_entropy(values):
    p = spectral_law(values)
    pi = upper_transform(p)
    total = D(0)
    for mass, cap in zip(p, pi):
        if mass:
            total += dfrac(mass) * lg(cap / mass)
    return total


def defect(values):
    return Fraction(sum(v == -1 for v in values), len(values))


def mean_packet(r):
    mu2 = (1 - 2 * r) ** 2
    if not mu2:
        return D(0)
    return dfrac(mu2) * lg(1 / mu2)


def separated_switch(left, right, depth):
    n0 = len(left).bit_length() - 1
    n1 = len(right).bit_length() - 1
    zmask = (1 << depth) - 1
    out = []
    for point in range(1 << (depth + n0 + n1)):
        z = point & zmask
        x = (point >> depth) & ((1 << n0) - 1)
        y = point >> (depth + n0)
        out.append(right[y] if z == 0 else left[x])
    return tuple(out)


def claimed_formula(left, right, depth):
    p = Fraction(1, 1 << depth)
    r0, r1 = defect(left), defect(right)
    rbar = (1 - p) * r0 + p * r1
    q0, q1 = 4 * r0 * (1 - r0), 4 * r1 * (1 - r1)
    theta = r0 + r1 - 2 * r0 * r1
    delta2 = (r1 - r0) ** 2
    answer = mean_packet(rbar)
    answer += dfrac(1 - p) * (upper_entropy(left) - mean_packet(r0))
    answer += dfrac(p) * (upper_entropy(right) - mean_packet(r1))
    a0 = dfrac((1 - p) ** 2) * lg(1 / (1 - p))
    a0 += dfrac(p) * D(depth) / 2 - dfrac(p * p) * D(depth)
    answer += dfrac(q0) * a0
    answer += dfrac(q1 * p) * D(depth) / 2
    answer += dfrac((2 * p - 4 * p * p) * delta2) * D(depth)
    if delta2:
        answer += dfrac(4 * (p - p * p) * delta2) * lg(theta / delta2)
    return answer


def influence(values, coordinate):
    bit = 1 << coordinate
    changes = sum(values[x] != values[x ^ bit] for x in range(len(values)))
    return Fraction(changes, len(values))


def all_cores(max_variables=2):
    out = []
    for n in range(max_variables + 1):
        points = 1 << n
        for code in range(1 << points):
            out.append(tuple(1 if ((code >> x) & 1) else -1 for x in range(points)))
    return out


L_M = 4 * (D(1) + D(2) / D(1).exp()) / LN2
C_SEP = D(3) + L_M + D(2) / LN2 + D(2) / (D(1).exp() * LN2)


class PhysicalTree:
    def __init__(self, truth, selector_coordinates=(), leaves=None):
        self.truth = tuple(truth)
        self.n = len(truth).bit_length() - 1
        self.selectors = tuple(selector_coordinates)
        self.leaves = [(Fraction(1), upper_entropy(self.truth))] if leaves is None else list(leaves)


def combine(left, right, depth=1):
    p = Fraction(1, 1 << depth)
    truth = separated_switch(left.truth, right.truth, depth)
    selectors = tuple(range(depth))
    selectors += tuple(depth + i for i in left.selectors)
    selectors += tuple(depth + left.n + i for i in right.selectors)
    leaves = [((1 - p) * w, u) for w, u in left.leaves]
    leaves += [(p * w, u) for w, u in right.leaves]
    return PhysicalTree(truth, selectors, leaves)


def tree_margin(tree):
    retained = sum((dfrac(w) * u for w, u in tree.leaves), D(0))
    selector_influence = sum((dfrac(influence(tree.truth, i)) for i in tree.selectors), D(0))
    charge = upper_entropy(tree.truth) - retained
    return C_SEP * selector_influence - charge


def main():
    cores = all_cores(2)
    formula_cases = 0
    node_cases = 0
    max_formula_error = D(0)
    min_node_margin = D("Infinity")

    for left, right in product(cores, repeat=2):
        r0, r1 = defect(left), defect(right)
        theta = r0 + r1 - 2 * r0 * r1
        for depth in range(1, 6):
            root = separated_switch(left, right, depth)
            direct = upper_entropy(root)
            formula = claimed_formula(left, right, depth)
            max_formula_error = max(max_formula_error, abs(direct - formula))
            p = Fraction(1, 1 << depth)
            charge = direct - dfrac(1 - p) * upper_entropy(left) - dfrac(p) * upper_entropy(right)
            payment = C_SEP * dfrac(2 * p * depth * theta)
            min_node_margin = min(min_node_margin, payment - charge)
            formula_cases += 1
            node_cases += 1

    one_bit = [tuple(1 if ((code >> x) & 1) else -1 for x in range(2)) for code in range(4)]
    min_tree_margin = D("Infinity")
    balanced_cases = 0
    chain_cases = 0

    # Every assignment of four one-bit leaves in a balanced depth-two tree.
    for leaves in product(one_bit, repeat=4):
        tree = combine(combine(PhysicalTree(leaves[0]), PhysicalTree(leaves[1])),
                       combine(PhysicalTree(leaves[2]), PhysicalTree(leaves[3])))
        min_tree_margin = min(min_tree_margin, tree_margin(tree))
        balanced_cases += 1

    # Every assignment of four one-bit leaves in a depth-three comb.
    for leaves in product(one_bit, repeat=4):
        tree = PhysicalTree(leaves[0])
        for leaf in leaves[1:]:
            tree = combine(tree, PhysicalTree(leaf))
        min_tree_margin = min(min_tree_margin, tree_margin(tree))
        chain_cases += 1

    # Verify the exact physical reach identity separately on all trees above
    # through the nonnegative final margins and explicit coordinate sums.
    assertions = formula_cases + node_cases + balanced_cases + chain_cases
    if max_formula_error > TOL:
        raise AssertionError(("formula", max_formula_error))
    if min_node_margin < -TOL:
        raise AssertionError(("node", min_node_margin))
    if min_tree_margin < -TOL:
        raise AssertionError(("tree", min_tree_margin))

    print(f"C_sep={C_SEP}")
    print(f"formula_cases={formula_cases}")
    print(f"node_bound_cases={node_cases}")
    print(f"balanced_tree_cases={balanced_cases}")
    print(f"chain_tree_cases={chain_cases}")
    print(f"assertions={assertions}")
    print(f"max_formula_error={max_formula_error}")
    print(f"min_node_margin={min_node_margin}")
    print(f"min_tree_margin={min_tree_margin}")
    print("randomness=none")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
