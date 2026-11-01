#!/usr/bin/env python3
"""Exact Walsh reconstruction for the separated two-affine-coset theorem."""

from fractions import Fraction
import math


def fwht(values):
    out = list(map(Fraction, values))
    h = 1
    while h < len(out):
        for start in range(0, len(out), 2 * h):
            for j in range(start, start + h):
                x, y = out[j], out[j + h]
                out[j], out[j + h] = x + y, x - y
        h *= 2
    return tuple(x / len(out) for x in out)


def entropy_hat(hat):
    return sum(float(c * c) * math.log(1 / float(c * c)) for c in hat if c)


def influence_hat(hat):
    return sum(s.bit_count() * c * c for s, c in enumerate(hat))


def linear_subspaces(n):
    size = 1 << n
    for mask in range(1 << (size - 1)):
        space = {0} | {x for x in range(1, size) if mask >> (x - 1) & 1}
        if all((x ^ y) in space for x in space for y in space):
            yield frozenset(space)


def affine_cosets(n):
    answer = set()
    for space in linear_subspaces(n):
        unseen = set(range(1 << n))
        while unseen:
            x = min(unseen)
            coset = frozenset(x ^ v for v in space)
            unseen -= coset
            answer.add(coset)
    return sorted(answer, key=lambda d: (len(d), tuple(d)))


def distance(a, b):
    return min((x ^ y).bit_count() for x in a for y in b)


def full_composition(source_slice):
    # First slice has chi=+1 and d=0; second has chi=-1 and d=source_slice.
    a, d, composed = [], [], []
    for selector_bit in (0, 1):
        chi = 1 if selector_bit == 0 else -1
        for value in source_slice:
            defect = selector_bit * value
            d.append(defect)
            a.append(chi * (1 - defect))
            composed.append(a[-1] + defect)
    return tuple(a), tuple(d), tuple(composed)


total_pairs = 0
unique_unions = 0
positive_cases = 0
nonaffine_cases = 0
best_nonaffine = (-1.0, None)

for m in range(1, 5):
    cosets = affine_cosets(m)
    coset_set = set(cosets)
    unions = set()
    pairs_m = 0
    for i, first in enumerate(cosets):
        for second in cosets[i + 1:]:
            if not first.isdisjoint(second) or distance(first, second) < 2:
                continue
            pairs_m += 1
            total_pairs += 1
            union = first | second
            unions.add(union)

            s1 = tuple(int(x in first) for x in range(1 << m))
            s2 = tuple(int(x in second) for x in range(1 << m))
            s = tuple(x + y for x, y in zip(s1, s2))
            hs1, hs2, hs = fwht(s1), fwht(s2), fwht(s)
            p = Fraction(len(union), 1 << m)

            # Exact physical separation and source-influence identities.
            assert influence_hat(hs) == influence_hat(hs1) + influence_hat(hs2)
            a, d, composed = full_composition(s)
            hd = fwht(d)
            assert influence_hat(hd) == influence_hat(hs) / 2 + p / 4

            omega = (entropy_hat(fwht(composed)) - entropy_hat(fwht(a))
                     - entropy_hat(hd))
            assert omega <= 16 * math.log(2) * float(influence_hat(hd)) + 1e-11
            if omega > 1e-12:
                positive_cases += 1
            if union not in coset_set:
                nonaffine_cases += 1
                ratio = omega / float(influence_hat(hd))
                if ratio > best_nonaffine[0]:
                    best_nonaffine = (ratio, (m, tuple(sorted(first)),
                                              tuple(sorted(second)), omega,
                                              float(influence_hat(hd))))

            # Direct finite reconstruction of the entropy-superposition lemma.
            left = entropy_hat(hs)
            right = 2 * entropy_hat(hs1) + 2 * entropy_hat(hs2) + float(p) / math.e
            assert left <= right + 1e-11

    unique_unions += len(unions)
    print(f"slice_dimension={m} separated_pairs={pairs_m} unique_unions={len(unions)} PASS")

print(f"total_separated_pair_decompositions={total_pairs}")
print(f"total_unique_unions_by_dimension={unique_unions}")
print(f"positive_associator_cases={positive_cases}")
print(f"nonaffine_pair_cases={nonaffine_cases}")
print(f"best_nonaffine_ratio={best_nonaffine[0]:.15f}")
print(f"best_nonaffine_instance={best_nonaffine[1]}")
print(f"theorem_constant_16ln2={16 * math.log(2):.15f}")
print("RESULT=PASS")

