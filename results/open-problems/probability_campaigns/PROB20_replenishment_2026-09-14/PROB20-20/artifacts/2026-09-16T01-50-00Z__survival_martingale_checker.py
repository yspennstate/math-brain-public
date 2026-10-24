#!/usr/bin/env python3
"""
PROB20-20 finite diagnostics for the 2026-09-16 near-full Palm/martingale checkpoint.

These are finite bookkeeping checks only. They do NOT verify Janson Problem 18.39.

Checks:
1. Exact enumeration of weighted size-biased permutations verifies
   E[remaining cloud mass after r peels] <= T*(1-L/M)^r <= T*exp(-rL/M).
2. Exact enumeration of iid paths verifies the stopped defective-mgf maximal
   Chernoff inequality
       P(exists s<=r: S_s>=x and max_{i<=s} X_i<=U)
       <= exp(-t*x + r*[log M_U(t)]_+).
3. Verifies the exact binary-entropy algebra used to optimize the universal
   rate-envelope correction.
"""
from __future__ import annotations
import itertools
import math
from typing import Dict, Sequence, Set, Tuple


def enumerate_size_biased_prefixes(masses: Sequence[int], r: int):
    """Yield (prefix, exact_probability) for r size-biased removals."""
    out = []

    def rec(remaining: Tuple[int, ...], prefix: Tuple[int, ...], prob: float):
        if len(prefix) == r or not remaining:
            out.append((prefix, prob))
            return
        total = sum(masses[i] for i in remaining)
        if total <= 0:
            out.append((prefix, prob))
            return
        for i in remaining:
            if masses[i] <= 0:
                continue
            nxt = tuple(j for j in remaining if j != i)
            rec(nxt, prefix + (i,), prob * masses[i] / total)

    rec(tuple(range(len(masses))), tuple(), 1.0)
    return out


def exact_remaining_cloud_expectation(
    masses: Sequence[int], cloud: Set[int], r: int
) -> float:
    ans = 0.0
    for prefix, prob in enumerate_size_biased_prefixes(masses, r):
        survivors = cloud.difference(prefix)
        ans += prob * sum(masses[i] for i in survivors)
    return ans


def check_survival_case(
    masses: Sequence[int], cloud: Set[int], L: int, r: int
) -> Tuple[float, float, float]:
    M = sum(masses)
    T = sum(masses[i] for i in cloud)
    exact = exact_remaining_cloud_expectation(masses, cloud, r)
    product_bound = T * (1.0 - L / M) ** r
    exponential_bound = T * math.exp(-r * L / M)
    if exact > product_bound + 1e-12:
        raise AssertionError((masses, cloud, L, r, exact, product_bound))
    if product_bound > exponential_bound + 1e-12:
        raise AssertionError((masses, cloud, L, r, product_bound, exponential_bound))
    return exact, product_bound, exponential_bound


def stopped_hit_probability(
    q: Dict[int, float], U: int, r: int, x: int
) -> float:
    """Exact finite probability of hitting x by time r before an increment > U."""
    supp = sorted(q)
    total = 0.0
    for seq in itertools.product(supp, repeat=r):
        path_prob = 1.0
        for k in seq:
            path_prob *= q[k]
        s = 0
        event = False
        for k in seq:
            if k > U:
                break
            s += k
            if s >= x:
                event = True
                break
        if event:
            total += path_prob
    return total


def defective_mgf(q: Dict[int, float], U: int, t: float) -> float:
    return sum(p * math.exp(t * k) for k, p in q.items() if k <= U)


def check_maximal_chernoff_case(
    q: Dict[int, float], U: int, r: int, x: int, t: float
) -> Tuple[float, float, float]:
    exact = stopped_hit_probability(q, U, r, x)
    M = defective_mgf(q, U, t)
    logM_plus = max(math.log(M), 0.0) if M > 0 else 0.0
    bound = math.exp(-t * x + r * logM_plus)
    if exact > bound + 2e-12:
        raise AssertionError((q, U, r, x, t, exact, M, bound))
    return exact, M, bound


def binary_entropy(p: float) -> float:
    return -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)


def check_entropy_identity(x: int, r: int) -> float:
    p = r / x
    if not (0 < p < 0.5):
        raise ValueError((x, r))
    d = -math.log(1.0 - p)
    lhs = x * d + r * math.log((1.0 - p) / p)
    rhs = x * binary_entropy(p)
    err = abs(lhs - rhs)
    if err > 1e-11:
        raise AssertionError((x, r, lhs, rhs, err))
    return err


def main() -> None:
    survival_cases = [
        ([8, 7, 2, 1, 1], {0, 1}, 7, 2),
        ([10, 9, 8, 1, 1, 1], {0, 1, 2}, 8, 3),
        ([5, 5, 5, 5, 1, 1, 1], {0, 1, 2, 3}, 5, 4),
        ([13, 11, 9, 4, 3, 2, 1], {0, 1, 2}, 9, 3),
    ]
    print("SURVIVAL CHECKS")
    for case in survival_cases:
        exact, product, expo = check_survival_case(*case)
        print(
            f"  masses={case[0]} r={case[3]}: "
            f"exact={exact:.15g}, product_bound={product:.15g}, "
            f"exp_bound={expo:.15g}"
        )

    q_cases = [
        {1: 0.35, 2: 0.25, 3: 0.15, 4: 0.10, 5: 0.08, 6: 0.07},
        {1: 0.50, 2: 0.18, 4: 0.12, 7: 0.10, 9: 0.06, 12: 0.04},
    ]
    print("\nMAXIMAL CHERNOFF CHECKS")
    nchecks = 0
    min_margin = float("inf")
    for q in q_cases:
        assert abs(sum(q.values()) - 1.0) < 1e-12
        for U in (3, 4, 5, 7, 9):
            if not any(k <= U for k in q):
                continue
            for r in (2, 3, 4):
                for x in (4, 6, 8, 10):
                    for t in (0.0, 0.05, 0.1, 0.25, 0.5):
                        exact, M, bound = check_maximal_chernoff_case(q, U, r, x, t)
                        min_margin = min(min_margin, bound - exact)
                        nchecks += 1
    print(f"  exact enumerated inequalities checked: {nchecks}")
    print(f"  smallest bound-minus-exact margin: {min_margin:.15g}")

    print("\nBINARY ENTROPY IDENTITY CHECKS")
    max_err = 0.0
    for x, r in ((100, 5), (100, 10), (30, 4), (250, 17), (1000, 23)):
        err = check_entropy_identity(x, r)
        max_err = max(max_err, err)
        print(f"  x={x}, r={r}, absolute algebra error={err:.3e}")
    print(f"  maximum algebra error: {max_err:.3e}")

    print("\nALL FINITE DIAGNOSTICS PASSED")
    print("Status: bookkeeping diagnostics only; not a proof of the universal conjecture.")


if __name__ == "__main__":
    main()
