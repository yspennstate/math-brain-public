"""Exact first moment of the number of pairs at hopcount >= k in K_n with Exp(1) weights.

E N_{n,k} = (n/2) * sum_{d>=k} f_{n,d},  where  sum_d f_{n,d} z^d = prod_{j=1}^{n-1} (1 + z/j).

usage:  python first_moment.py [out.json]

Prints (i) exact values for small n, (ii) the ratio of E N_{n,k} at k = ceil(b_n) to its limit
C_* alpha^{-(k-b_n)} for n = 10^2,...,10^6, (iii) for the sizes used in the simulations, the levels k at which
E N_{n,k} crosses 1/2, and the values of E N_{n,k} near them.
"""
import json
import math
import sys
from fractions import Fraction


def alpha_star():
    a = 3.5
    for _ in range(60):
        a -= (a * math.log(a) - a - 1.0) / math.log(a)
    return a


ALPHA = alpha_star()
THETA = math.log(ALPHA)
C_STAR = 1.0 / (2.0 * math.gamma(1.0 + ALPHA) * (1.0 - 1.0 / ALPHA) * math.sqrt(2.0 * math.pi * ALPHA))


def b(n):
    return ALPHA * math.log(n) - math.log(math.log(n)) / (2.0 * THETA)


def profile_exact(n):
    """Coefficients f_{n,0..n-1} as fractions."""
    f = [Fraction(1)]
    for j in range(1, n):
        g = f + [Fraction(0)]
        for d in range(len(f), 0, -1):
            g[d] += f[d - 1] / j
        f = g
    return f


def profile_float(n, kmax):
    """Coefficients f_{n,0..kmax} in floating point (all terms are positive)."""
    f = [0.0] * (kmax + 1)
    f[0] = 1.0
    for j in range(1, n):
        inv = 1.0 / j
        top = min(j, kmax)
        for d in range(top, 0, -1):
            f[d] += f[d - 1] * inv
    return f


def tail_exact(n, kmax):
    """sum_{d>=k} f_{n,d} for k = 0..kmax, with the part above kmax bounded and added.

    The coefficients decay faster than geometrically above alpha*log n, so the truncation at kmax (taken well
    above that level) changes nothing at double precision; the function checks this.
    """
    f = profile_float(n, kmax)
    tails = [0.0] * (kmax + 2)
    for d in range(kmax, -1, -1):
        tails[d] = tails[d + 1] + f[d]
    assert f[kmax] < 1e-30 * max(tails[kmax // 2], 1e-300) or kmax >= n - 1
    return tails


def expected_pairs(n, kmax):
    t = tail_exact(n, kmax)
    return [0.5 * n * x for x in t]


def main():
    out = {"alpha": ALPHA, "theta": THETA, "C_star": C_STAR, "half_over_theta": 0.5 / THETA,
           "five_minus_alpha_log4": 5.0 - ALPHA * math.log(4.0)}
    print("alpha* = %.14f   1/(2 log alpha*) = %.9f   C_* = %.13f   5 - alpha* log 4 = %.7f"
          % (ALPHA, 0.5 / THETA, C_STAR, 5.0 - ALPHA * math.log(4.0)))

    print("\nexact values, small n:  P(M_n = n-1) = E N_{n,n-1} = n/(2 (n-1)!)")
    small = {}
    for n in range(2, 9):
        f = profile_exact(n)
        assert sum(f) == n
        en = [Fraction(n, 2) * sum(f[k:]) for k in range(1, n)]
        assert en[-1] == Fraction(n, 2 * math.factorial(n - 1))
        small[n] = [str(x) for x in en]
        print("  n=%d  E N_{n,k}, k=1..%d: %s" % (n, n - 1, ", ".join(str(x) for x in en)))
    out["small_n_expected_pairs"] = small

    print("\nE N_{n,k} at k = ceil(b_n) against C_* alpha^{-(k-b_n)}")
    rows = []
    for e in range(2, 7):
        n = 10 ** e
        kmax = int(ALPHA * math.log(n)) + 60
        en = expected_pairs(n, kmax)
        k = math.ceil(b(n))
        lim = C_STAR * ALPHA ** (-(k - b(n)))
        mu = sum(ALPHA / (j + ALPHA) for j in range(1, n))
        var = sum(ALPHA * j / (j + ALPHA) ** 2 for j in range(1, n))
        gauss = math.exp(-(k - mu) ** 2 / (2.0 * var))
        rows.append({"n": n, "b_n": b(n), "k": k, "EN": en[k], "limit_form": lim, "ratio": en[k] / lim,
                     "mean_S_minus_alpha_log_n": mu - ALPHA * math.log(n), "var_S": var, "gaussian_factor": gauss})
        print("  n=10^%d  b_n=%.4f  k=%d  E N=%.6e  limit form=%.6e  ratio=%.4f   mean S_n - alpha log n=%.4f  "
              "exp(-(k-mean)^2/(2 var))=%.4f" % (e, b(n), k, en[k], lim, en[k] / lim, mu - ALPHA * math.log(n), gauss))
    out["ratio_table"] = rows

    print("\nsimulation sizes: levels k with E N_{n,k} near 1/2")
    sims = []
    for n in (250, 500, 1000, 2000, 4000):
        kmax = int(ALPHA * math.log(n)) + 60
        en = expected_pairs(n, kmax)
        khalf = max(k for k in range(1, kmax) if en[k] >= 0.5)
        sims.append({"n": n, "alpha_log_n": ALPHA * math.log(n), "b_n": b(n), "largest_k_with_EN_ge_half": khalf,
                     "EN": {str(k): en[k] for k in range(max(1, khalf - 12), khalf + 8)}})
        print("  n=%d  alpha log n=%.3f  b_n=%.3f  largest k with E N >= 1/2: %d" % (n, ALPHA * math.log(n), b(n), khalf))
    out["simulation_sizes"] = sims

    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as fh:
            json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
