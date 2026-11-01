#!/usr/bin/env python3
"""Independent A094 reconstruction of the aligned-width B05 theorem.

This intentionally does not import the author checker.  It uses direct Walsh
sums, edge-count influence, a separately written rational log enclosure, and
all small full-column-rank physical matrices (not only identity matrices).
"""

from collections import Counter
from fractions import Fraction


LOG_TERMS = 56


def rank2(rows, r):
    rows = list(rows)
    rank = 0
    for bit in range(r):
        pivot = next((j for j in range(rank, len(rows))
                      if (rows[j] >> bit) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for j in range(len(rows)):
            if j != rank and ((rows[j] >> bit) & 1):
                rows[j] ^= rows[rank]
        rank += 1
    return rank


def walsh_direct(values):
    N = len(values)
    return [sum(values[x] * (-1 if ((x & a).bit_count() & 1) else 1)
                for x in range(N)) for a in range(N)]


def influence_edges(values, n):
    N = 1 << n
    total = Fraction(0)
    for j in range(n):
        changed = sum(values[x] != values[x | (1 << j)]
                      for x in range(N) if not ((x >> j) & 1))
        total += Fraction(changed, 1 << (n - 1))
    return total


def ln_unit_bounds(x, terms=LOG_TERMS):
    """Bounds ln(x), 1 <= x <= 2, by an independently coded atanh tail."""
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    s = Fraction(0)
    for k in range(terms):
        s += z ** (2 * k + 1) / (2 * k + 1)
    low = 2 * s
    next_power = z ** (2 * terms + 1)
    tail = 2 * next_power / ((2 * terms + 1) * (1 - z * z))
    return low, low + tail


LN2 = ln_unit_bounds(Fraction(2))


def lg2_bounds(q):
    q = Fraction(q)
    assert q >= 1
    exponent = 0
    while q >= 2:
        q /= 2
        exponent += 1
    if q == 1:
        return Fraction(exponent), Fraction(exponent)
    nl, nu = ln_unit_bounds(q)
    dl, du = LN2
    return exponent + nl / du, exponent + nu / dl


def entropy_bounds_from_squares(squares, den):
    lo = hi = Fraction(0)
    for a in squares:
        if not a:
            continue
        p = Fraction(a, den)
        ll, uu = lg2_bounds(Fraction(den, a))
        lo += p * ll
        hi += p * uu
    return lo, hi


def finite_constants():
    rows = []
    for n in range(1, 5):
        N = 1 << n
        den = N * N
        signatures = Counter()
        for mask in range(1 << (N - 1)):
            values = [1] + [(-1 if ((mask >> (x - 1)) & 1) else 1)
                            for x in range(1, N)]
            w = walsh_direct(values)
            squares = tuple(sorted(a * a for a in w if a))
            influence = influence_edges(values, n)
            if influence:
                signatures[(squares, influence)] += 1

        point = [1] * N
        point[-1] = -1
        pw = walsh_direct(point)
        target = (tuple(sorted(a * a for a in pw if a)),
                  influence_edges(point, n))
        tlo, thi = entropy_bounds_from_squares(target[0], den)
        tlo /= target[1]
        thi /= target[1]

        runner_hi = Fraction(-1)
        maximizer_count = 0
        for sig, count in signatures.items():
            hlo, hhi = entropy_bounds_from_squares(sig[0], den)
            rlo, rhi = hlo / sig[1], hhi / sig[1]
            if sig == target:
                maximizer_count += count
            else:
                assert rhi < tlo, (n, float(rhi), float(tlo))
                runner_hi = max(runner_hi, rhi)
        rows.append((n, len(signatures), maximizer_count, tlo, thi, runner_hi))
    return rows


def full_rank_matrices(s, r):
    for code in range(1 << (s * r)):
        rows = [(code >> (i * r)) & ((1 << r) - 1) for i in range(s)]
        if rank2(rows, r) == r:
            yield rows


def phase_choices(s, r, t, serial):
    # Two deterministic, distinct affine choices per structural instance.
    masks = ((0, 0, 0),
             (serial & ((1 << s) - 1),
              (serial * 3 + 1) & ((1 << r) - 1),
              (serial * 5 + 1) & ((1 << t) - 1)))
    return masks


def shield_reconstruction():
    cases = 0
    atoms = 0
    for r in (1, 2):
        for s in range(r, 4):
            for Mrows in full_rank_matrices(s, r):
                for t in range(0, 4 - r):
                    yz = r + t
                    # Exhaust every core through yz=3.
                    for dmask in range(1 << ((1 << yz) - 1)):
                        D = [1] + [(-1 if ((dmask >> (v - 1)) & 1) else 1)
                                   for v in range(1, 1 << yz)]
                        serial = dmask + sum(row << (3 * i)
                                             for i, row in enumerate(Mrows))
                        for a, b, c in phase_choices(s, r, t, serial):
                            n = s + r + t
                            values = []
                            for state in range(1 << n):
                                z = state & ((1 << t) - 1)
                                u = (state >> t) & ((1 << r) - 1)
                                x = state >> (t + r)
                                bilinear = sum(((x >> i) & 1) *
                                               ((Mrows[i] & u).bit_count() & 1)
                                               for i in range(s)) & 1
                                affine = ((a & x).bit_count() +
                                          (b & u).bit_count() +
                                          (c & z).bit_count()) & 1
                                values.append((-1 if bilinear ^ affine else 1) *
                                              D[(u << t) | z])

                            actual = sorted(v * v for v in walsh_direct(values) if v)
                            predicted = []
                            fiber_influence = Fraction(0)
                            for u in range(1 << r):
                                fiber = []
                                for z in range(1 << t):
                                    fiber.append(D[(u << t) | z] *
                                                 (-1 if ((c & z).bit_count() & 1)
                                                  else 1))
                                fw = walsh_direct(fiber)
                                for q in fw:
                                    if q:
                                        predicted.extend([q * q * (1 << (2 * s))]
                                                         * (1 << r))
                                fiber_influence += influence_edges(fiber, t) / (1 << r)
                            assert actual == sorted(predicted)
                            assert influence_edges(values, n) >= r + fiber_influence
                            atoms += len(actual)
                            cases += 1
    return cases, atoms


def hardness_identity():
    # Independently reconstruct q(x,u)=(-1)^(xu).
    q = [1, 1, 1, -1]
    w = walsh_direct(q)
    assert [a * a for a in w] == [4, 4, 4, 4]
    assert influence_edges(q, 2) == 1
    hlo, hhi = entropy_bounds_from_squares([4, 4, 4, 4], 16)
    assert hlo == hhi == 2


def main():
    hardness_identity()
    constants = finite_constants()
    cases, atoms = shield_reconstruction()
    print("B19 independent aligned-width review")
    print(f"log enclosure terms: {LOG_TERMS}")
    for n, profiles, count, lo, hi, runner in constants:
        print(f"n={n}: profiles={profiles}, maximizer_reps={count}, "
              f"C=[{float(lo):.18f},{float(hi):.18f}], "
              f"width={float(hi-lo):.3e}, runner_upper={float(runner):.18f}")
    print(f"nonidentity/full-rank shield reconstructions: {cases}")
    print(f"reconstructed nonzero spectral atoms: {atoms}")
    print("all independent direct-Walsh, edge-influence, interval, and embedding checks passed")


if __name__ == "__main__":
    main()
