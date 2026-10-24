#!/usr/bin/env python3
"""Exact falsification check for the Boolean bipartition interaction lemma.

For every sign-normalized Boolean truth table through n=4 and every nontrivial
coordinate bipartition U | U^c (modulo swapping the two sides), compute

  A = sum_{empty != S subset U} fhat(S)^2,
  B = sum_{empty != S subset U^c} fhat(S)^2,
  Delta = sum_{S meets U and U^c} fhat(S)^2,

and verify A*B <= 4*Delta using integer Walsh numerators only.
The computation is diagnostic; the all-dimensional proof is analytic.
"""
from fractions import Fraction


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def main():
    total = 0
    zero_cross = 0
    best = Fraction(0, 1)
    best_data = None

    for n in range(2, 5):
        N = 1 << n
        # Fix coordinate 0 on the U side to quotient U <-> U^c.
        partitions = [u for u in range(1, N - 1) if u & 1]
        # Quotient f <-> -f by fixing f(0)=+1.
        for code in range(1 << (N - 1)):
            values = [1] + [1 if (code >> (x - 1)) & 1 else -1
                            for x in range(1, N)]
            walsh = fwht(values)
            squares = [z * z for z in walsh]

            for U in partitions:
                V = (N - 1) ^ U
                A = B = Delta = 0
                for S, w2 in enumerate(squares):
                    if S == 0 or w2 == 0:
                        continue
                    hit_u = bool(S & U)
                    hit_v = bool(S & V)
                    if hit_u and not hit_v:
                        A += w2
                    elif hit_v and not hit_u:
                        B += w2
                    elif hit_u and hit_v:
                        Delta += w2

                total += 1
                if Delta == 0:
                    assert A * B == 0
                    zero_cross += 1
                    continue

                # Since Fourier masses are w2/N^2, A_mass*B_mass<=4 Delta_mass
                # is exactly A*B <= 4*Delta*N^2.
                assert A * B <= 4 * Delta * N * N
                ratio = Fraction(A * B, Delta * N * N)
                if ratio > best:
                    best = ratio
                    best_data = (n, code, U, A, B, Delta, N)

    print(f"function_partition_checks={total}")
    print(f"zero_cross_checks={zero_cross}")
    print(f"max_A_times_B_over_Delta={best.numerator}/{best.denominator}")
    print(f"max_ratio_decimal={float(best):.12f}")
    print(f"argmax_n_code_U_A_B_Delta_N={best_data}")
    print("violations=0")


if __name__ == "__main__":
    main()
