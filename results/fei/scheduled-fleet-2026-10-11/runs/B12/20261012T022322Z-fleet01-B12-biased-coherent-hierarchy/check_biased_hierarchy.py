#!/usr/bin/env python3
"""Deterministic controls for A057 biased coherent identity and tree payment.

No randomness is used. Fourier coefficients of enumerated Boolean tables are
dyadic rationals represented exactly by Python Fraction; entropy logs are
evaluated in float64.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
import math


def fwht(values):
    a = list(values)
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for k in range(start, start + step):
                x, y = a[k], a[k + step]
                a[k], a[k + step] = x + y, x - y
        step *= 2
    return a


def hats(values):
    size = len(values)
    return [Fraction(x, size) for x in fwht(values)]


def psi(x):
    x = float(x)
    z = x * x
    return z * math.log(1.0 / z) if z else 0.0


def eraw(vector):
    return sum(psi(x) for x in vector)


def kernel(x, y):
    return psi(x) + psi(y) - 0.5 * (psi(x + y) + psi(x - y))


def audit_biased_identity():
    # Every ordered pair of Boolean branches on two variables.
    branch_functions = list(product((-1, 1), repeat=4))
    branch_pairs = []
    for plus in branch_functions:
        for minus in branch_functions:
            a_values = [Fraction(x + y, 2) for x, y in zip(plus, minus)]
            b_values = [Fraction(x - y, 2) for x, y in zip(plus, minus)]
            branch_pairs.append((a_values, b_values, hats(a_values), hats(b_values)))

    cases = 0
    max_split_error = 0.0
    max_kernel_error = 0.0
    for n in range(1, 4):
        size = 1 << n
        for child in product((-1, 1), repeat=size):
            child_hat = hats(child)
            mu = child_hat[0]
            for coordinate in range(n):
                r_values, s_values = [], []
                for t in range(1 << (n - 1)):
                    low = t & ((1 << coordinate) - 1)
                    high = t >> coordinate
                    base = low | (high << (coordinate + 1))
                    h_plus = child[base]
                    h_minus = child[base | (1 << coordinate)]
                    r_values.append(Fraction(h_plus + h_minus, 2))
                    s_values.append(Fraction(h_plus - h_minus, 2))
                r_hat, s_hat = hats(r_values), hats(s_values)
                alpha = s_hat[0]
                child_split = (
                    eraw(r_hat) + eraw(s_hat)
                    - 0.5 * eraw([x + y for x, y in zip(r_hat, s_hat)])
                    - 0.5 * eraw([x - y for x, y in zip(r_hat, s_hat)])
                )

                for a_values, b_values, a_hat, b_hat in branch_pairs:
                    q = sum(x * x for x in b_hat)
                    composed = [
                        a_values[w] + child[x] * b_values[w]
                        for x in range(size) for w in range(4)
                    ]
                    composed_hat = hats(composed)
                    physical_bit = 2 + coordinate
                    u_hat, v_hat = [], []
                    for t in range(1 << (n + 1)):
                        low = t & ((1 << physical_bit) - 1)
                        high = t >> physical_bit
                        mask = low | (high << (physical_bit + 1))
                        u_hat.append(composed_hat[mask])
                        v_hat.append(composed_hat[mask | (1 << physical_bit)])
                    composed_split = (
                        eraw(u_hat) + eraw(v_hat)
                        - 0.5 * eraw([x + y for x, y in zip(u_hat, v_hat)])
                        - 0.5 * eraw([x - y for x, y in zip(u_hat, v_hat)])
                    )

                    scalar_child = (
                        psi(mu) + psi(alpha)
                        - 0.5 * psi(mu + alpha) - 0.5 * psi(mu - alpha)
                    )
                    remainder = (
                        eraw([x + mu * y for x, y in zip(a_hat, b_hat)])
                        + eraw([alpha * y for y in b_hat])
                        - 0.5 * eraw([x + (mu + alpha) * y for x, y in zip(a_hat, b_hat)])
                        - 0.5 * eraw([x + (mu - alpha) * y for x, y in zip(a_hat, b_hat)])
                        - float(q) * scalar_child
                    )
                    max_split_error = max(
                        max_split_error,
                        abs(composed_split - float(q) * child_split - remainder),
                    )
                    kernel_form = sum(
                        float(b * b)
                        * (kernel(float(a / b + mu), float(alpha))
                           - kernel(float(mu), float(alpha)))
                        for a, b in zip(a_hat, b_hat) if b
                    )
                    max_kernel_error = max(max_kernel_error, abs(remainder - kernel_form))
                    cases += 1

    assert max_split_error < 4e-15
    assert max_kernel_error < 4e-15
    return cases, max_split_error, max_kernel_error


def max_adaptive_tree_cost(values, n):
    size = 1 << n

    @lru_cache(None)
    def dynamic(mask, assignment):
        if mask == size - 1:
            return 0.0
        compatible = [x for x in range(size) if (x & mask) == assignment]
        weight = Fraction(len(compatible), size)
        best = 0.0
        for i in range(n):
            if mask & (1 << i):
                continue
            alpha = Fraction(
                sum(values[x] * (1 if not (x & (1 << i)) else -1)
                    for x in compatible),
                len(compatible),
            )
            candidate = (
                float(weight) * psi(alpha)
                + dynamic(mask | (1 << i), assignment)
                + dynamic(mask | (1 << i), assignment | (1 << i))
            )
            best = max(best, candidate)
        return best

    return dynamic(0, 0)


def total_influence(values, n):
    size = 1 << n
    return sum(
        Fraction(sum(values[x] != values[x ^ (1 << i)] for x in range(size)), size)
        for i in range(n)
    )


def audit_adaptive_trees():
    rows = []
    for n in range(1, 5):
        size = 1 << n
        best_ratio = -1.0
        best = None
        for table_bits in range(1 << size):
            values = [1 if table_bits & (1 << x) else -1 for x in range(size)]
            influence = total_influence(values, n)
            cost = max_adaptive_tree_cost(values, n)
            ratio = cost / float(influence) if influence else 0.0
            assert ratio <= 2.0 / math.e + 1e-13
            if ratio > best_ratio:
                best_ratio = ratio
                best = (table_bits, influence, cost)
        rows.append((n, 1 << size, best_ratio, best))
    return rows


def collision_controls():
    # Actual four-input Boolean outer gate, recorded as its two three-bit branches.
    a_hat = [Fraction(-1, 2), Fraction(-1, 4), Fraction(-1, 4), 0,
             Fraction(-1, 4), 0, 0, Fraction(1, 4)]
    b_hat = [Fraction(-1, 4), 0, 0, Fraction(1, 4),
             0, Fraction(1, 4), Fraction(1, 4), Fraction(-1, 2)]
    mu = Fraction(1, 2)
    collision_energy = sum(
        b * b for a, b in zip(a_hat, b_hat) if b and a + mu * b == 0
    )
    rows = []
    for n in range(4, 15):
        size = 1 << n
        plus_count = size // 8 + 1
        minus_count = size // 8 - 1
        negative = set(list(range(0, size, 2))[:plus_count]
                       + list(range(1, size, 2))[:minus_count])
        child = [-1 if x in negative else 1 for x in range(size)]
        child_hat = hats(child)
        assert child_hat[0] == mu
        alpha = child_hat[1]
        assert alpha == Fraction(-4, size)
        remainder = sum(
            float(b * b)
            * (kernel(float(a / b + mu), float(alpha))
               - kernel(float(mu), float(alpha)))
            for a, b in zip(a_hat, b_hat) if b
        )
        rows.append((n, alpha, remainder, remainder / psi(alpha)))
    return collision_energy, rows


def main():
    print("seed=none; enumeration and controls are deterministic")
    cases, split_error, kernel_error = audit_biased_identity()
    print(f"biased_identity_cases={cases}")
    print(f"max_split_identity_abs_error={split_error:.17g}")
    print(f"max_kernel_rewrite_abs_error={kernel_error:.17g}")
    print("biased_identity_result=PASS")
    print("adaptive_tree_scope=all Boolean truth tables n<=4; maximum over all full nonreusing adaptive query trees")
    for n, count, ratio, best in audit_adaptive_trees():
        bits, influence, cost = best
        print(
            f"n={n} functions={count} max_tree_log_over_I={ratio:.16f} "
            f"table_bits={bits} I={influence} tree_log_nats={cost:.16f}"
        )
    print(f"analytic_bound_2_over_e={2.0 / math.e:.16f}")
    print("adaptive_tree_result=PASS")
    collision_energy, rows = collision_controls()
    print(f"biased_collision_energy={collision_energy}")
    for n, alpha, remainder, ratio in rows:
        print(
            f"collision_control_n={n} mu=1/2 alpha={alpha} "
            f"R={remainder:.17g} R_over_alpha_log={ratio:.16f}"
        )
    print("collision_control_predicted_limit=-1/4")
    print("collision_controls_result=PASS")


if __name__ == "__main__":
    main()
