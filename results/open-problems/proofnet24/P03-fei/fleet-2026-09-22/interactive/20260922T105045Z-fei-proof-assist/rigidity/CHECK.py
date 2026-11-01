#!/usr/bin/env python3
"""Finite diagnostics for the amplitude-bin KL theorem, not its proof."""
import itertools
import json
import math
import random
from collections import defaultdict


def walsh(values):
    data = list(values)
    span = 1
    while span < len(data):
        for base in range(0, len(data), 2 * span):
            for offset in range(span):
                left, right = data[base + offset], data[base + offset + span]
                data[base + offset] = left + right
                data[base + offset + span] = left - right
        span *= 2
    return data


def kappa(q):
    ratio = 2 ** (2 / q)
    a = ratio * math.log(ratio) / (ratio - 1)
    return (a - 1 - math.log(a)) / math.log(2)


def influence_classes(amplitudes):
    n = len(amplitudes).bit_length() - 1
    numerators = [sum(a*a for s, a in enumerate(amplitudes) if s >> i & 1) for i in range(n)]
    classes = defaultdict(list)
    for i, influence in enumerate(numerators):
        classes[influence].append(i)
    return list(classes.values()), numerators


def conditional_loss(amplitudes, q=None, svic=False, adaptive=False):
    n = len(amplitudes).bit_length() - 1
    classes, numerators = influence_classes(amplitudes)
    cells = defaultdict(list)
    for s, a in enumerate(amplitudes):
        if not s or not a:
            continue
        counts = tuple(sum(s >> i & 1 for i in group) for group in classes)
        if svic:
            positive = abs(a)
            v2 = (positive & -positive).bit_length()-1
            key = (counts, 1 if a > 0 else -1, v2)
        elif s.bit_count() == 1:
            key = ("singleton", s)
        elif adaptive:
            key = ("higher_linear", counts,
                   ((abs(a)**(2*q)).bit_length()-1) // (s.bit_count()-1))
        else:
            # Exact integer binning: floor(q log_2 |A|).
            key = ("higher", counts, (abs(a)**q).bit_length()-1)
        cells[key].append(a*a)
    denominator = len(amplitudes)**2
    total = 0.0
    for weights in cells.values():
        mass = sum(weights)
        total += sum(w * math.log2(len(weights)*w/mass) for w in weights) / denominator
    tail = sum(a*a for s, a in enumerate(amplitudes) if s.bit_count() >= 2) / denominator
    influence = sum(numerators) / denominator
    return total, tail, influence, len(cells), len(classes)


def cyclic_odd(n, rng):
    """A genuine balanced Boolean table, invariant under cyclic rotations."""
    mask = (1 << n)-1

    def orbit(x):
        points = []
        for _ in range(n):
            points.append(x)
            x = ((x << 1) & mask) | (x >> (n-1))
        return set(points)

    table = [0] * (1 << n)
    for x in range(1 << n):
        if table[x]:
            continue
        positive, negative = orbit(x), orbit(x ^ mask)
        assert not positive & negative  # n is odd, so weights differ.
        sign = rng.choice((-1, 1))
        for y in positive:
            table[y] = sign
        for y in negative:
            table[y] = -sign
    assert sum(table) == 0
    return table


def sparse_suspension(m):
    values = []
    for s in range(1 << (m+1)):
        old = s >> 1
        values.append((-1 if s & 1 else 1) * (-1 if old == 0 else 1))
    return values


def majority_depth_two():
    values = []
    for s in range(1 << 9):
        children = [sum(1 if (s >> (3*j+i)) & 1 else -1 for i in range(3)) for j in range(3)]
        values.append(1 if sum(1 if x > 0 else -1 for x in children) > 0 else -1)
    return values


def biased_squared_weights(table, numerator, denominator):
    """Exact integer weights for common rational input bias numerator/denominator."""
    data = list(table)
    span = 1
    while span < len(data):
        for base in range(0, len(data), 2*span):
            for j in range(span):
                left, right = data[base+j], data[base+j+span]
                data[base+j] = (denominator-numerator)*left + numerator*right
                data[base+j+span] = right-left
        span *= 2
    n = len(table).bit_length()-1
    weights = [a*a*(numerator*(denominator-numerator))**s.bit_count()
               for s,a in enumerate(data)]
    scale = denominator**(2*n)
    assert sum(weights) == scale
    return weights, scale


def check_biased(table, numerator, denominator):
    weights, scale = biased_squared_weights(table, numerator, denominator)
    n = len(table).bit_length()-1
    nonempty_mass = sum(weights[1:])
    if not nonempty_mass:
        return
    occurrence = [sum(w for s,w in enumerate(weights) if s >> i & 1) for i in range(n)]
    grouped = defaultdict(list)
    for i, r in enumerate(occurrence):
        grouped[r].append(i)
    classes = list(grouped.values())
    excess = (sum(occurrence)-nonempty_mass)/scale
    for q in (1,2,4):
        for adaptive in (False,True):
            cells = defaultdict(list)
            for s,w in enumerate(weights):
                if not s or not w:
                    continue
                if s.bit_count()==1:
                    key=('singleton',s)
                else:
                    counts=tuple(sum(s>>i&1 for i in c) for c in classes)
                    log_integer=(w**q).bit_length()-1
                    b=log_integer//(s.bit_count()-1 if adaptive else 2)
                    key=('higher',counts,b)
                cells[key].append(w)
            weighted_loss=sum(sum(w*math.log2(len(values)*w/sum(values)) for w in values)
                              for values in cells.values())/scale
            coefficient=1/q if adaptive else kappa(q)
            assert weighted_loss <= coefficient*excess + 1e-12


def main():
    checked = 0
    max_loss = {q: 0.0 for q in (1, 2, 4)}
    max_linear_loss = {q: 0.0 for q in (1, 2, 4)}
    max_original = 0.0
    positive_example = None

    def check(table, label):
        nonlocal checked, max_original, positive_example
        amplitudes = walsh(table)
        assert amplitudes[0] == 0
        assert sum(a*a for a in amplitudes) == len(table)**2
        original = conditional_loss(amplitudes, svic=True)[0]
        max_original = max(max_original, original)
        for q in (1, 2, 4):
            loss, tail, influence, cells, classes = conditional_loss(amplitudes, q)
            assert loss >= -2e-13
            assert tail <= influence - 1 + 1e-13
            assert loss <= kappa(q)*tail + 2e-12, (label, q, loss, tail)
            assert loss <= math.log(2)/(2*q*q)*(influence-1) + 2e-12
            max_loss[q] = max(max_loss[q], loss)
            linear_loss, _, _, linear_cells, _ = conditional_loss(amplitudes, q, adaptive=True)
            assert linear_loss <= (influence-1)/q + 2e-12
            max_linear_loss[q] = max(max_linear_loss[q], linear_loss)
            if classes == 1:
                n = len(table).bit_length()-1
                count_bound = 2*q*n*sum(1/j for j in range(1,n))+2*n
                assert linear_cells <= count_bound+1e-10
            if q == 1 and loss > 1e-4 and positive_example is None:
                positive_example = {"label": label, "loss": loss, "tail": tail,
                    "influence": influence, "cells": cells, "influence_classes": classes,
                    "original_svic_loss": original, "truth_table": table}
        checked += 1

    # Exhaust all 12,870 balanced four-input Boolean functions.
    for positions in itertools.combinations(range(16), 8):
        table = [-1]*16
        for index in positions:
            table[index] = 1
        check(table, "balanced_n4")

    # Equal-influence, genuinely multilevel examples with nonzero binning loss.
    rng = random.Random(20260922)
    for n in (5, 7, 9, 11):
        for index in range(32):
            check(cyclic_odd(n, rng), f"cyclic_odd_n{n}_sample{index}")

    zero_loss_families = []
    for m in range(2, 11):
        amplitudes = walsh(sparse_suspension(m))
        for q in (1, 2, 4):
            assert abs(conditional_loss(amplitudes, q)[0]) < 1e-12
        zero_loss_families.append(f"one_point_suspension_m{m}")
    amplitudes = walsh(majority_depth_two())
    for q in (1, 2, 4):
        assert abs(conditional_loss(amplitudes, q)[0]) < 1e-12
    zero_loss_families.append("recursive_ternary_majority_depth2")

    biased_checked=0
    for n in (5,7,9):
        for numerator,denominator in ((1,3),(1,5),(2,5)):
            for _ in range(4):
                check_biased(cyclic_odd(n,rng),numerator,denominator)
                biased_checked+=1

    assert positive_example is not None
    print(json.dumps({"status": "PASS", "checked_boolean_tables": checked,
        "exhaustive_domain": "all balanced functions on four inputs",
        "random_domain": "32 deterministic-seeded cyclic odd functions at each n=5,7,9,11",
        "kappa": {q:kappa(q) for q in (1,2,4)}, "max_observed_loss": max_loss,
        "max_linear_adaptive_loss": max_linear_loss,
        "max_original_svic_loss": max_original,
        "biased_exact_weight_checks":biased_checked,
        "biased_domain":"cyclic odd sources n5,7,9 at common rational biases1/3,1/5,2/5; fixed and adaptive bins after one common amplitude rescaling",
        "zero_loss_families": zero_loss_families,
        "nonzero_loss_example": positive_example,
        "limitation": "Numerical diagnostics of exact integer spectra; analytic theorem is proved in REPORT.md."}, indent=2))


if __name__ == "__main__":
    main()
