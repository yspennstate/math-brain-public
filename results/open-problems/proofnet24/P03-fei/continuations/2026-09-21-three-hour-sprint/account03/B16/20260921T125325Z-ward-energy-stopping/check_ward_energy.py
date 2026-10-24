#!/usr/bin/env python3
"""Exact finite checks for B16 binary odd-block Ward-energy identities.

Standard library only.  This is a falsification/sanity checker for algebraic
identities proved in REPORT.md; it is not a proof of FEI.
"""
from fractions import Fraction
import json
import random


def odd_counts(mask: int, h: int):
    """q_l = number of dyadic blocks at depth l with odd R-occupancy."""
    nleaves = 1 << h
    out = []
    for level in range(h + 1):
        block = 1 << (h - level)
        q = 0
        for start in range(0, nleaves, block):
            cnt = 0
            for x in range(start, start + block):
                cnt += (mask >> x) & 1
            q += cnt & 1
        out.append(q)
    return out


def parity_descendant(mask: int, lo: int, size: int):
    """Unique singleton reached by repeatedly following the odd child."""
    assert sum((mask >> x) & 1 for x in range(lo, lo + size)) % 2 == 1
    while size > 1:
        half = size // 2
        left = sum((mask >> x) & 1 for x in range(lo, lo + half))
        if left % 2 == 1:
            size = half
        else:
            lo += half
            size = half
    assert (mask >> lo) & 1
    return lo


def representative_sets(mask: int, h: int):
    """S_l: one parity-descendant leaf for each odd block at depth l."""
    nleaves = 1 << h
    levels = []
    for level in range(h + 1):
        block = 1 << (h - level)
        reps = set()
        for start in range(0, nleaves, block):
            cnt = sum((mask >> x) & 1 for x in range(start, start + block))
            if cnt % 2 == 1:
                reps.add(parity_descendant(mask, start, block))
        levels.append(reps)
    return levels


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def verify(mask: int, h: int):
    R = [x for x in range(1 << h) if (mask >> x) & 1]
    assert len(R) % 2 == 1
    qs = odd_counts(mask, h)
    sets = representative_sets(mask, h)
    assert qs[0] == 1 and qs[-1] == len(R)
    assert all(q % 2 == 1 for q in qs)
    assert all(sets[j] <= sets[j + 1] for j in range(h))
    assert sets[-1] == set(R)
    assert [len(s) for s in sets] == qs

    # c=1 suffices by homogeneity.
    vecs = []
    for S, q in zip(sets, qs):
        vecs.append([Fraction(1, q) if x in S else Fraction(0) for x in R])
    inc = [[a - b for a, b in zip(vecs[j + 1], vecs[j])] for j in range(h)]

    for j in range(h):
        q, qp = qs[j], qs[j + 1]
        assert qp >= q and (qp - q) % 2 == 0
        births = (qp - q) // 2
        exact_drop = Fraction(1, q) - Fraction(1, qp)
        assert exact_drop == Fraction(2 * births, q * qp)
        assert dot(inc[j], inc[j]) == exact_drop
        assert sum(inc[j], Fraction(0)) == 0

    for i in range(h):
        for j in range(i + 1, h):
            assert dot(inc[i], inc[j]) == 0
        assert dot(inc[i], vecs[-1]) == 0

    total = sum((dot(d, d) for d in inc), Fraction(0)) + dot(vecs[-1], vecs[-1])
    assert total == 1
    return tuple(qs)


def slow_l1_turnover(m: int):
    assert m >= 1 and m % 2 == 1
    s = Fraction(0)
    q = 1
    while q < m:
        qp = q + 2
        s += Fraction(2, qp)
        q = qp
    return s


def main():
    exhaustive = {}
    for h in range(1, 5):
        nleaves = 1 << h
        checked = 0
        sequences = set()
        for mask in range(1, 1 << nleaves):
            if mask.bit_count() % 2 == 0:
                continue
            sequences.add(verify(mask, h))
            checked += 1
        exhaustive[str(h)] = {
            "odd_subsets_checked": checked,
            "distinct_q_sequences": len(sequences),
        }

    rng = random.Random(20260921)
    sampled = {}
    for h in (5, 6, 8):
        nleaves = 1 << h
        count = 2000
        max_final_q = 0
        max_jump = 0
        for _ in range(count):
            mask = 0
            for x in range(nleaves):
                if rng.getrandbits(1):
                    mask |= 1 << x
            if mask.bit_count() % 2 == 0:
                mask ^= 1
            qs = verify(mask, h)
            max_final_q = max(max_final_q, qs[-1])
            max_jump = max(max_jump, max(qs[j + 1] - qs[j] for j in range(h)))
        sampled[str(h)] = {
            "samples": count,
            "max_final_q": max_final_q,
            "max_single_level_q_jump": max_jump,
        }

    turnover = {}
    for m in (3, 5, 17, 65, 257, 1025):
        s = slow_l1_turnover(m)
        turnover[str(m)] = {
            "exact": f"{s.numerator}/{s.denominator}",
            "float": float(s),
            "quadratic_variation": float(Fraction(m - 1, m)),
        }

    print(json.dumps({
        "status": "PASS",
        "exhaustive": exhaustive,
        "sampled": sampled,
        "slow_refinement_l1_turnover": turnover,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
