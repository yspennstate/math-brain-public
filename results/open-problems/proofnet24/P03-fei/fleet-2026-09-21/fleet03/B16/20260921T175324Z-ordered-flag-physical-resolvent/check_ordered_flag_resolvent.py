#!/usr/bin/env python3
"""Exact checks for B16 ordered-flag physical resolvent identities.

Standard library only. This does not audit the read-once FEI certificate.
"""

from fractions import Fraction
from itertools import permutations, combinations


def later_sets(n, perm):
    rank = {v: r for r, v in enumerate(perm)}
    return {
        i: tuple(j for j in range(n) if rank[j] > rank[i])
        for i in range(n)
    }


def normalized_flag_frame(n, perm):
    """lambda_pi(w)=(1/n) sum_i 2^{-|L_i|} 1_{w subset L_i}, including w=0."""
    later = later_sets(n, perm)
    lam = [Fraction(0) for _ in range(1 << n)]
    for i in range(n):
        L = later[i]
        wt = Fraction(1, n * (1 << len(L)))
        for bits in range(1 << len(L)):
            w = 0
            for a, j in enumerate(L):
                if (bits >> a) & 1:
                    w |= 1 << j
            lam[w] += wt
    return lam


def fixed_pivot_random_order_distribution(n, i=0):
    """Average of the fair-subset-of-later-set law over every coordinate order."""
    perms = list(permutations(range(n)))
    dist = [Fraction(0) for _ in range(1 << n)]
    for perm in perms:
        L = later_sets(n, perm)[i]
        wt = Fraction(1, len(perms) * (1 << len(L)))
        for bits in range(1 << len(L)):
            w = 0
            for a, j in enumerate(L):
                if (bits >> a) & 1:
                    w |= 1 << j
            dist[w] += wt
    return dist


def walsh_character(mask, x):
    return -1 if ((mask & x).bit_count() & 1) else 1


def main():
    frame_checks = 0
    incidence_checks = 0
    walsh_checks = 0
    moment_checks = 0

    # Exhaust every order through n=7.
    for n in range(2, 8):
        for perm in permutations(range(n)):
            lam = normalized_flag_frame(n, perm)
            assert sum(lam) == 1
            rank = {v: r for r, v in enumerate(perm)}
            for j in range(n):
                d_j = sum(
                    lam[w] for w in range(1 << n) if (w >> j) & 1
                )
                assert d_j == Fraction(rank[j], 2 * n)
                incidence_checks += 1
            assert max(
                sum(lam[w] for w in range(1 << n) if (w >> j) & 1)
                for j in range(n)
            ) == Fraction(n - 1, 2 * n)
            frame_checks += 1

    # Average over all orders with one fixed physical pivot.
    # This verifies the exact Hardy-resolvent multiplier 1/(|U|+1),
    # the single-coordinate marginal 1/4, and the pair marginal 1/12.
    for n in range(2, 8):
        i = 0
        dist = fixed_pivot_random_order_distribution(n, i)
        assert sum(dist) == 1
        others = [j for j in range(n) if j != i]

        for j in others:
            p1 = sum(dist[w] for w in range(1 << n) if (w >> j) & 1)
            assert p1 == Fraction(1, 4)
            moment_checks += 1

        for j, k in combinations(others, 2):
            p2 = sum(
                dist[w]
                for w in range(1 << n)
                if ((w >> j) & 1) and ((w >> k) & 1)
            )
            assert p2 == Fraction(1, 12)
            moment_checks += 1

        for U in range(1 << n):
            if (U >> i) & 1:
                continue
            degree = U.bit_count()
            multiplier = sum(
                dist[w] * walsh_character(U, w)
                for w in range(1 << n)
            )
            assert multiplier == Fraction(1, degree + 1)
            walsh_checks += 1

    print("status=PASS")
    print(f"all_coordinate_orders_checked={frame_checks}")
    print(f"coordinate_incidence_checks={incidence_checks}")
    print(f"walsh_resolvent_checks={walsh_checks}")
    print(f"one_and_two_coordinate_moment_checks={moment_checks}")
    print("deterministic_normalized_frame_D=(n-1)/(2n)<1/2")
    print("random_order_averaged_frame_D=(n-1)/(4n)<1/4")
    print("fixed_pivot_random_order_single_inclusion=1/4")
    print("fixed_pivot_random_order_pair_inclusion=1/12")
    print("fixed_pivot_flag_walsh_multiplier=1/(|U|+1)")
    print("fixed_Ber(1/4)_shortcut=REFUTED_BY_1/12_NE_1/16")


if __name__ == "__main__":
    main()
