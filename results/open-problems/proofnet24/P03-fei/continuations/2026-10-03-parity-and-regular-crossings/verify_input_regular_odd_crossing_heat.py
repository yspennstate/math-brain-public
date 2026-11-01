"""Independent rational mask checks for input-regular odd crossings.

Tiny and zero rational weights are deliberate. No author helpers imported.
Only square roots and entropy constants are numerical supplements.
"""
from bisect import bisect_left
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path
import random

RNG = random.Random(2026100319)
C = dict(weight_vectors=0, masks=0, zero_energy_masks=0,
         exact_average_energy=0, numerical_average_square_root=0,
         displacement_moments=0, exact_resampling_masks=0)


def law(weights):
    out = Counter({Fraction(0): 1})
    for w in weights:
        new = Counter()
        for s, count in out.items():
            new[s - w] += count
            new[s + w] += count
        out = new
    return out


def fvalue(s, cuts, ties):
    j = bisect_left(cuts, s)
    if j < len(cuts) and s == cuts[j]:
        return ties[j]
    return -1 if j % 2 == 0 else 1


def inspect(weights):
    n = len(weights)
    variance = sum(w * w for w in weights)
    if variance == 0:
        return
    maximum = max(abs(w) for w in weights)
    b2 = Fraction(n) * maximum * maximum / variance
    assert b2 >= 1
    for k in sorted({1, min(2, n), min(3, n)}):
        masks = list(combinations(range(n), k))
        amax = Fraction(k) * b2 * variance / n
        assert amax == k * maximum * maximum
        mean_a = Fraction(0)
        mean_sqrt = 0.0
        for selected in masks:
            a = sum(weights[i] * weights[i] for i in selected)
            assert 0 <= a <= amax
            # Squared form of sqrt(a)>=a/sqrt(amax), exact even at zero.
            assert a * amax >= a * a
            mean_a += a / len(masks)
            mean_sqrt += math.sqrt(float(a)) / len(masks)
            sublaw = law([weights[i] for i in selected])
            denominator = 1 << (2 * k)
            m2 = Fraction(sum(cu * cv * (u - v) ** 2
                              for u, cu in sublaw.items() for v, cv in sublaw.items()), denominator)
            m4 = Fraction(sum(cu * cv * (u - v) ** 4
                              for u, cu in sublaw.items() for v, cv in sublaw.items()), denominator)
            l1 = Fraction(sum(cu * cv * abs(u - v)
                              for u, cu in sublaw.items() for v, cv in sublaw.items()), denominator)
            assert m2 == 2 * a
            assert m4 == 12 * a * a - 4 * sum(weights[i] ** 4 for i in selected)
            assert 3 * l1 * l1 >= 2 * a
            if not a:
                assert l1 == m2 == m4 == 0
                C['zero_energy_masks'] += 1
            C['masks'] += 1
            C['displacement_moments'] += 1
        assert mean_a == Fraction(k) * variance / n
        target = math.sqrt(k * float(variance) / (n * float(b2)))
        assert mean_sqrt + 2e-13 >= target
        C['exact_average_energy'] += 1
        C['numerical_average_square_root'] += 1
    # Several fixed masks are checked against the physical influence sum.
    # The following attained-score ties are arbitrary legal crossing labels.
    size = 1 << n
    scores = [sum(w * (1 if x & (1 << i) else -1)
                  for i, w in enumerate(weights)) for x in range(size)]
    cuts = sorted({Fraction(-1, 7), Fraction(0), Fraction(1, 7)})
    ties = [RNG.choice((-1, 1)) for _ in cuts]
    vals = [fvalue(s, cuts, ties) for s in scores]
    ii = [Fraction(sum(vals[x] != vals[x ^ (1 << i)] for x in range(size)), size)
          for i in range(n)]
    for selected in (tuple(range(min(3, n))), tuple(range(n - min(2, n), n))):
        k = len(selected)
        rest = [weights[i] for i in range(n) if i not in selected]
        rlaw, ulaw = law(rest), law([weights[i] for i in selected])
        pivotal = sum(cr * cu * cv * (fvalue(r + u, cuts, ties) != fvalue(r + v, cuts, ties))
                      for r, cr in rlaw.items() for u, cu in ulaw.items() for v, cv in ulaw.items())
        ns = Fraction(pivotal, 1 << (n + k))
        assert ns <= sum(ii[i] for i in selected) / 2
        C['exact_resampling_masks'] += 1
    C['weight_vectors'] += 1


def main():
    for n in range(3, 10):
        inspect([Fraction(1)] + [Fraction(0)] * (n - 1))
        inspect([Fraction(1), Fraction(1, 10 ** 6)] + [Fraction(0)] * (n - 2))
        inspect([Fraction(1)] * (n // 2) + [Fraction(1, 10 ** 5)] * (n - n // 2))
        for _ in range(6):
            inspect([RNG.choice([Fraction(0), Fraction(1, 10 ** 4),
                                 Fraction(1, 7), Fraction(1), Fraction(2)]) for i in range(n)])
    report = {'status': 'PASS independent finite checks; full analytic audit separate',
              'counts': C,
              'exact': ['mask energy mean K*sigma^2/n',
                        'regularity-implied uniform upper bound on mask energy',
                        'pointwise squared form of lower square-root inequality',
                        'zero-mask and rational second/fourth/L1 displacement moments',
                        'physical fixed-mask half-influence resampling bound'],
              'numerical': ['average square-root energy lower bound'],
              'scope': 'Tiny/zero weights covered; no large-n truth-table verification or full Boolean FEI claim'}
    Path(__file__).with_name('input_regular_odd_crossing_heat_checks.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
