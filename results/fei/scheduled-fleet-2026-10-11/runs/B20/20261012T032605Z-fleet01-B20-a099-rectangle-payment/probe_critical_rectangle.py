#!/usr/bin/env python3
"""High-precision diagnostic for the remaining critical rectangle inequality.

This is explicitly NUMERICAL, not acceptance evidence.  It exhausts dimensions
through four and reports the largest observed value of
    min_i Delta_i H / rho_i
among descendant-critical tensor-prime Boolean functions.
"""

from functools import lru_cache
from itertools import combinations
from math import log2


def signs(table: int, n: int) -> list[int]:
    return [1 if ((table >> x) & 1) == 0 else -1 for x in range(1 << n)]


def fwht(a: list[int]) -> list[int]:
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def restrict_table(table: int, n: int, i: int, value: int) -> int:
    out = 0
    for z in range(1 << (n - 1)):
        lo = z & ((1 << i) - 1)
        hi = z >> i
        x = lo | (value << i) | (hi << (i + 1))
        out |= ((table >> x) & 1) << z
    return out


@lru_cache(None)
def stats(n: int, table: int) -> tuple[float, float, float]:
    den = 1 << n
    W = fwht(signs(table, n))
    H = 0.0
    I = 0.0
    for s, w in enumerate(W):
        if w:
            p = (w * w) / (den * den)
            H -= p * log2(p)
            I += s.bit_count() * p
    R = H / I if I else 0.0
    return H, I, R


@lru_cache(None)
def descendant_max_ratio(n: int, table: int) -> float:
    if n == 0:
        return 0.0
    ans = 0.0
    for i in range(n):
        for b in (0, 1):
            child = restrict_table(table, n, i, b)
            ans = max(ans, stats(n - 1, child)[2],
                      descendant_max_ratio(n - 1, child))
    return ans


def pivotal_probability(n: int, table: int, i: int) -> float:
    return sum(((table >> x) & 1) != ((table >> (x ^ (1 << i))) & 1)
               for x in range(1 << n)) / (1 << n)


def is_tensor_prime(n: int, table: int) -> bool:
    # rho_A=0 iff the sign matrix across A|B has multiplicative rank one.
    f = signs(table, n)
    for a in range(1, n):
        for A in combinations(range(n), a):
            if 0 not in A:  # complement duplicate
                continue
            B = tuple(i for i in range(n) if i not in A)
            def idx(xa: int, yb: int) -> int:
                z = 0
                for k, i in enumerate(A):
                    z |= ((xa >> k) & 1) << i
                for k, i in enumerate(B):
                    z |= ((yb >> k) & 1) << i
                return z
            ok = True
            for x in range(1 << len(A)):
                for y in range(1 << len(B)):
                    if f[idx(x, y)] * f[idx(0, 0)] != f[idx(x, 0)] * f[idx(0, y)]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return False
    return True


def main() -> None:
    critical_count = 0
    prime_count = 0
    worst = (-1.0, None)
    zero_cases = 0
    for n in range(1, 5):
        for table in range(1 << (1 << n)):
            H, I, R = stats(n, table)
            if I == 0 or R + 1e-12 < descendant_max_ratio(n, table):
                continue
            critical_count += 1
            if n > 1 and not is_tensor_prime(n, table):
                continue
            prime_count += 1
            ratios = []
            for i in range(n):
                p = pivotal_probability(n, table, i)
                if p == 0:
                    continue
                H0 = stats(n - 1, restrict_table(table, n, i, 0))[0]
                H1 = stats(n - 1, restrict_table(table, n, i, 1))[0]
                delta = H - (H0 + H1) / 2
                rho = p * (1 - p)
                if rho == 0:
                    if abs(delta) < 1e-11:
                        zero_cases += 1
                        ratios.append(0.0)
                    else:
                        ratios.append(float("inf"))
                else:
                    ratios.append(delta / rho)
            if ratios:
                value = min(ratios)
                if value > worst[0]:
                    worst = (value, (n, table, R, ratios))

    print("NUMERICAL CRITICAL-RECTANGLE PROBE COMPLETED")
    print(f"descendant_critical_functions={critical_count}")
    print(f"tensor_prime_critical_functions={prime_count}")
    print(f"zero_rho_zero_delta_coordinate_cases={zero_cases}")
    print(f"largest_min_delta_over_rho={worst[0]:.15g}")
    print(f"witness={worst[1]}")
    print("scope=all Boolean sign tables for 1<=n<=4")
    print("status=NUMERICAL; floating classification is not a certificate")


if __name__ == "__main__":
    main()
