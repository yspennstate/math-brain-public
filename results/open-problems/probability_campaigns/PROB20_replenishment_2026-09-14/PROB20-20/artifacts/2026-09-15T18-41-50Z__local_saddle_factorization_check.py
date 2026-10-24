#!/usr/bin/env python3
"""PROB20-20 diagnostic for the moving truncated-saddle checkpoint.

This is a numerical bookkeeping check, NOT a proof of the universal theorem.
It verifies on several finite toy laws the exact identity

  P_pi(S_n=m, max<=U) = exp(-n I_U(lambda)) P_t(S_n=m),

and reports the central tilted local cost against the scale Var_t(X)+log n.

Only the Python standard library is used.
"""

import math
from typing import Dict, List, Tuple


def normalize(weights: Dict[int, float]) -> Dict[int, float]:
    z = sum(weights.values())
    return {k: v / z for k, v in weights.items()}


def tilted(pi: Dict[int, float], U: int, t: float) -> Tuple[Dict[int, float], float, float, float]:
    vals = {k: p * math.exp(t * k) for k, p in pi.items() if k <= U}
    z = sum(vals.values())
    pt = {k: v / z for k, v in vals.items()}
    mean = sum(k * p for k, p in pt.items())
    second = sum(k * k * p for k, p in pt.items())
    var = second - mean * mean
    return pt, z, mean, var


def solve_t(pi: Dict[int, float], U: int, target: float) -> float:
    _, _, mean0, _ = tilted(pi, U, 0.0)
    if target < mean0 - 1e-13:
        lo, hi = -1.0, 0.0
        while tilted(pi, U, lo)[2] > target:
            lo *= 2.0
    else:
        lo, hi = 0.0, 1.0
        while tilted(pi, U, hi)[2] < target:
            hi *= 2.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if tilted(pi, U, mid)[2] < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def sum_atom(dist: Dict[int, float], n: int, m: int) -> float:
    dp = [0.0] * (m + 1)
    dp[0] = 1.0
    for _ in range(n):
        ndp = [0.0] * (m + 1)
        for s, a in enumerate(dp):
            if a == 0.0:
                continue
            for k, p in dist.items():
                if s + k <= m:
                    ndp[s + k] += a * p
        dp = ndp
    return dp[m]


def run_case(name: str, weights: Dict[int, float], U: int, n: int, m: int) -> None:
    pi = normalize(weights)
    lam = m / n
    t = solve_t(pi, U, lam)
    pt, phi, mean, var = tilted(pi, U, t)
    assert abs(mean - lam) < 1e-10

    trunc_pi = {k: p for k, p in pi.items() if k <= U}
    direct = sum_atom(trunc_pi, n, m)
    central = sum_atom(pt, n, m)
    I = lam * t - math.log(phi)
    via_tilt = math.exp(-n * I) * central

    rel = abs(direct - via_tilt) / max(direct, via_tilt, 1e-300)
    assert rel < 2e-10, (name, direct, via_tilt, rel)
    assert central > 0.0

    local_cost = -math.log(central)
    scale = var + math.log(n) + 1.0
    print(f"[{name}]")
    print(f"  U={U} n={n} m={m} lambda={lam:.8f} t={t:.8g}")
    print(f"  Phi_U(t)={phi:.12g} variance={var:.12g}")
    print(f"  direct truncated atom={direct:.12e}")
    print(f"  tilted central atom={central:.12e}")
    print(f"  exact factorization relerr={rel:.3e}")
    print(f"  -log central={local_cost:.8f}")
    print(f"  (-log central)/(var+log n+1)={local_cost/scale:.8f}")


def main() -> None:
    cases: List[Tuple[str, Dict[int, float], int, int, int]] = []

    w1 = {k: 1.0 / ((k + 1) ** 3) for k in range(0, 26)}
    cases.append(("smooth_proxy", w1, 20, 45, 90))

    w2 = {0: 1.0, 1: 0.7, 2: 0.45, 5: 0.18, 11: 0.06, 19: 0.018, 31: 0.0045}
    cases.append(("lacunary", w2, 19, 36, 108))

    w3 = {0: 1.0, 1: 0.55, 2: 0.08, 3: 0.31, 7: 0.025, 8: 0.07, 15: 0.008, 24: 0.002}
    cases.append(("jagged", w3, 15, 40, 100))

    for case in cases:
        run_case(*case)

    print("ALL EXACT TILT FACTORIZATION CHECKS PASSED")
    print("The variance-scale ratios above are diagnostics only, not a proof constant.")


if __name__ == "__main__":
    main()
