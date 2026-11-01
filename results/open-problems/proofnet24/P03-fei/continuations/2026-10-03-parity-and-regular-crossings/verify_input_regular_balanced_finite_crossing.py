#!/usr/bin/env python3
"""Fresh finite checks for balanced regular finite-crossing FEI candidate.

Exact rational checks cover the new local signed-translation lemma and
endpoint conventions.  Small truth tables check Walsh energy/influence for
balanced regular score functions.  These checks supplement, not replace,
the analytic proof and Berry--Esseen argument.
"""

from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
import json
import math
from pathlib import Path


def interval_label(x, cuts, left=1):
    """Open-interval label; tests avoid x at a cut."""
    k = sum(c < x for c in cuts)
    return left * (-1 if k % 2 else 1)


def pivotal_measure(a, b, u, v, cuts, left=1):
    lo, hi = sorted((a, b))
    pts = {lo, hi}
    for c in cuts:
        for z in (c - u, c - v):
            if lo < z < hi:
                pts.add(z)
    pts = sorted(pts)
    total = Fraction(0)
    signed = Fraction(0)
    for x, y in zip(pts, pts[1:]):
        mid = (x + y) / 2
        fu = interval_label(mid + u, cuts, left)
        fv = interval_label(mid + v, cuts, left)
        signed += (y - x) * (fv - fu)
        if fu != fv:
            total += y - x
    return total, signed


def translation_checks():
    count = 0
    exact_boundary = 0
    even_m = 0
    odd_m = 0
    families = [
        tuple(map(Fraction, xs))
        for xs in [(-7,), (-5, 2), (-8, -2, 5),
                   (-9, -4, 1, 7), (-10, -6, -1, 3, 9)]
    ]
    for cuts in families:
        m = len(cuts)
        # Protected points in every complementary interval, including tails.
        points = [cuts[0] - 4]
        points += [(x + y) / 2 for x, y in zip(cuts, cuts[1:])]
        points += [cuts[-1] + 4]
        for left in (-1, 1):
            for a, b in combinations(points, 2):
                if interval_label(a, cuts, left) == interval_label(b, cuts, left):
                    continue
                clearance = min(min(abs(a - c) for c in cuts),
                                min(abs(b - c) for c in cuts))
                h = clearance / 3
                shifts = (-h, -h/2, Fraction(0), h/3, h)
                for u, v in combinations(shifts, 2):
                    pm, signed = pivotal_measure(a, b, u, v, cuts, left)
                    assert pm >= abs(u - v)
                    expected = abs(Fraction(2) * (v-u))
                    assert abs(signed) == expected
                    count += 1
                    exact_boundary += 1
                    if m % 2:
                        odd_m += 1
                    else:
                        even_m += 1
    return dict(exact_local_translation=count,
                exact_boundary_integrals=exact_boundary,
                even_crossing_cases=even_m, odd_crossing_cases=odd_m)


def walsh(values):
    a = [Fraction(v) for v in values]
    n = (len(a)).bit_length() - 1
    for j in range(n):
        step = 1 << j
        for base in range(0, len(a), 2 * step):
            for k in range(step):
                x, y = a[base+k], a[base+k+step]
                a[base+k], a[base+k+step] = x+y, x-y
    den = len(a)
    return [x / den for x in a]


def truth_checks():
    checked = balanced = regular = 0
    max_ratio = 0.0
    max_case = None
    for n in range(2, 8):
        for weights in combinations_with_replacement(range(0, 4), n):
            if not any(weights):
                continue
            sigma2 = sum(w*w for w in weights)
            b_actual = max(weights) * math.sqrt(n / sigma2)
            if b_actual > 2 + 1e-12:
                continue
            regular += 1
            scores = []
            signs = list(product((-1, 1), repeat=n))
            for x in signs:
                scores.append(sum(w*z for w, z in zip(weights, x)))
            levels = sorted(set(scores))
            mids = [Fraction(x+y, 2) for x, y in zip(levels, levels[1:])]
            # One through three genuine crossings selected between score levels.
            for m in range(1, min(3, len(mids)) + 1):
                for cut_idx in combinations(range(len(mids)), m):
                    cuts = tuple(mids[i] for i in cut_idx)
                    vals = [interval_label(Fraction(s), cuts) for s in scores]
                    checked += 1
                    minority = min(vals.count(1), vals.count(-1))
                    if minority * 8 < len(vals):
                        continue
                    balanced += 1
                    coeff = walsh(vals)
                    energy = Fraction(0)
                    entropy = 0.0
                    for mask, c in enumerate(coeff):
                        p = c*c
                        energy += p * mask.bit_count()
                        if p:
                            pf = float(p)
                            entropy -= pf * math.log2(pf)
                    influence = Fraction(0)
                    for j in range(n):
                        changes = sum(vals[k] != vals[k ^ (1 << j)]
                                      for k in range(len(vals)))
                        influence += Fraction(changes, len(vals))
                    assert energy == influence
                    if influence:
                        ratio = entropy / float(influence)
                        if ratio > max_ratio:
                            max_ratio = ratio
                            max_case = dict(n=n, weights=list(weights),
                                            cuts=[str(x) for x in cuts],
                                            minority_count=minority,
                                            entropy_over_influence=ratio)
    return dict(weight_families=regular, score_functions=checked,
                balanced_score_functions=balanced,
                maximum_entropy_over_influence=max_ratio,
                maximizer=max_case)


def main():
    report = {
        "status": "PASS exact local-translation and finite truth checks; analytic proof separate",
        "translation": translation_checks(),
        "truth_tables": truth_checks(),
        "exact": [
            "local signed-translation boundary identity for opposite protected labels",
            "pivotal Lebesgue measure at least selected-score displacement",
            "even and odd crossing counts",
            "Walsh Parseval physical energy equals total influence",
        ],
        "scope": "No large-N0 enumeration, Berry-Esseen proof, novelty certificate, or unrestricted FEI claim",
    }
    out = Path(__file__).with_name("input_regular_balanced_finite_crossing_checks.json")
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
