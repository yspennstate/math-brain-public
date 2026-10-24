#!/usr/bin/env python3
"""
Exact checker for P16 Cerny 3/4-letter symmetry reduction.

All arithmetic is integer/rational.  No randomness, floating point, timeout,
SAT/SMT, or heuristic acceptance is used.

Claims checked:
1. Burnside formula for q-letter ordered DFAs modulo simultaneous state
   relabeling and alphabet-letter permutation.
2. Burnside formula for k-element transition supports modulo state relabeling.
3. Brute-force agreement for n=2,3 where direct canonicalization is cheap.
4. Exact n=8 q=3,4 orbit counts, including the behavior-support quotient.
5. Exact n=8 candidate support count after deleting constant maps and identity.
6. Shitov's displayed cubic coefficient simplifies exactly to 8257/49923.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product, combinations
from math import factorial, gcd

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for p in range(max_part, 0, -1):
        for rest in partitions(n-p, p):
            yield (p,) + rest

def class_size(part):
    m = Counter(part)
    z = 1
    for d, c in m.items():
        z *= (d ** c) * factorial(c)
    return factorial(sum(part)) // z

def power_cycle_type(part, r):
    out = []
    for d in part:
        g = gcd(d, r)
        out.extend([d // g] * g)
    return tuple(sorted(out, reverse=True))

def commuting_transformations(part):
    m = Counter(part)
    ans = 1
    for d, md in m.items():
        choices = sum(e * me for e, me in m.items() if d % e == 0)
        ans *= choices ** md
    return ans

def ordered_letter_orbits(n, q):
    total = 0
    for pn in partitions(n):
        cn = class_size(pn)
        c = {ell: commuting_transformations(power_cycle_type(pn, ell))
             for ell in range(1, q + 1)}
        for pq in partitions(q):
            cq = class_size(pq)
            fixed = 1
            for ell in pq:
                fixed *= c[ell]
            total += cn * cq * fixed
    den = factorial(n) * factorial(q)
    assert total % den == 0
    return total // den

def fixed_allowed(part, exclude_rank1=False, exclude_identity=False):
    ans = commuting_transformations(part)
    if exclude_rank1:
        ans -= Counter(part).get(1, 0)
    if exclude_identity:
        ans -= 1
    return ans

def support_orbits(n, kmax=4, exclude_rank1=False, exclude_identity=False):
    sums = [0] * (kmax + 1)
    for part in partitions(n):
        cs = class_size(part)
        F = {r: fixed_allowed(power_cycle_type(part, r), exclude_rank1,
                              exclude_identity)
             for r in range(1, kmax + 1)}
        a = {1: F[1],
             2: (F[2] - F[1]) // 2,
             3: (F[3] - F[1]) // 3,
             4: (F[4] - F[2]) // 4}
        assert F[2] >= F[1] and F[3] >= F[1] and F[4] >= F[2]
        assert (F[2] - F[1]) % 2 == 0
        assert (F[3] - F[1]) % 3 == 0
        assert (F[4] - F[2]) % 4 == 0
        coeff = [1] + [0] * kmax
        for d in range(1, kmax + 1):
            A = a[d]
            nxt = [0] * (kmax + 1)
            for deg, base in enumerate(coeff):
                if not base:
                    continue
                choose = 1
                for j in range((kmax - deg) // d + 1):
                    if j:
                        choose = choose * (A - j + 1) // j
                    nxt[deg + d*j] += base * choose
            coeff = nxt
        for k in range(kmax + 1):
            sums[k] += cs * coeff[k]
    den = factorial(n)
    assert all(s % den == 0 for s in sums)
    return [s // den for s in sums]

def conjugate(f, pi):
    n = len(f)
    inv = [0] * n
    for i, j in enumerate(pi):
        inv[j] = i
    return tuple(pi[f[inv[j]]] for j in range(n))

def canonical_support(fs, n):
    return min(tuple(sorted(conjugate(f, pi) for f in fs))
               for pi in permutations(range(n)))

def brute_support_orbits(n, k):
    transformations = list(product(range(n), repeat=n))
    return len({canonical_support(comb, n)
                for comb in combinations(transformations, k)})

def main():
    print("P16_CERNY_SYMMETRY_EXACT_CHECK")
    print("ARITHMETIC integer_only_except_displayed_Fraction")
    print()
    expected_small = {2: [3, 4, 3, 1], 3: [7, 67, 509, 2984]}
    for n, exp in expected_small.items():
        burn = support_orbits(n, 4)[1:5]
        print(f"N{n}_SUPPORT_ORBITS_K1_TO_K4", burn)
        assert burn == exp
        brute = [brute_support_orbits(n, k) for k in range(1, 5)]
        print(f"N{n}_BRUTE_SUPPORT_ORBITS_K1_TO_K4", brute)
        assert brute == burn
    s8 = support_orbits(8, 4)
    print("N8_SUPPORT_ORBITS_K1_TO_K4", s8[1:5])
    assert s8[1:5] == [951, 3540690574, 19526393150503160,
                       81874873983464642056149]
    print("N8_BEHAVIOR_SUPPORT_ORBITS_UP_TO4", sum(s8[1:5]))
    assert sum(s8[1:5]) == 81874893509861333250834
    for q, expected in [(3, 19526400231564564),
                        (4, 81874932562648494674439)]:
        got = ordered_letter_orbits(8, q)
        print(f"N8_Q{q}_ISOMORPHISM_ORBITS_WITH_DUPLICATES", got)
        assert got == expected
    restricted = support_orbits(8, 4, exclude_rank1=True,
                                exclude_identity=True)
    print("N8_SUPPORT_ORBITS_K4_NO_CONSTANT_NO_IDENTITY", restricted[4])
    assert restricted[4] == 81874698258167607454204
    shitov = Fraction(7, 48) + 2 * Fraction(15625, 1597536)
    print("SHITOV_COEFFICIENT_EXACT", f"{shitov.numerator}/{shitov.denominator}")
    assert shitov == Fraction(8257, 49923)
    print()
    print("ALL_CHECKS_PASSED")

if __name__ == "__main__":
    main()
