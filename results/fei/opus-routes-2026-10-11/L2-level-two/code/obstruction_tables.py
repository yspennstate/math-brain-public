"""Exact tables for the obstructions O1 (x0 * bent_m) and O2 (Hamming ball), route L2.

O1: f = x0 * bent_m on n = m + 1 variables, m even.  p(T) = 2^-m for every T containing 0.
    B_k = C(m, k-1) (m - k + 1) 2^(1-m),  I = 1 + m/2,  B = m.
    At m = 2k: B_k / I = (2k/(k+1)) C(2k,k) 4^-k  ~  2/sqrt(pi k).
O2: A = {x : #(-1 coordinates) <= t},  f = 1 - 2 1_A on n variables.
    delta = P[Bin(n,1/2) <= t],  p0 = (1 - 2 delta)^2,  fhat({i}) = -pmf(t; n-1, 1/2),  p1 = pmf^2,
    Inf_i = pmf(t; n-1, 1/2),  I = n pmf,  B_0 = n phi(p0, p1),  Var = 4 delta (1 - delta).
Usage: python obstruction_tables.py OUTJSON
"""
import sys, json, math
from math import comb, log2, lgamma, log, exp


def phi(a, b):
    def eta(x):
        return 0.0 if x <= 0 else -x * log2(x)
    return eta(a) + eta(b) - eta(a + b)


def log_pmf(t, n):
    return lgamma(n + 1) - lgamma(t + 1) - lgamma(n - t + 1) - n * log(2)


def cdf(t, n):
    # exact for moderate n via log-sum-exp of pmfs
    if t < 0:
        return 0.0
    m = max(log_pmf(j, n) for j in range(0, t + 1))
    return exp(m) * sum(exp(log_pmf(j, n) - m) for j in range(0, t + 1))


def main():
    out = {"O1_bent": [], "O2_ball": []}
    for k in (1, 2, 3, 5, 10, 20, 50, 100, 200, 500):
        m = 2 * k
        Bk = comb(m, k - 1) * (m - k + 1) * 2.0 ** (1 - m) if m < 1000 else None
        I = 1 + m / 2
        exact = (2 * k / (k + 1)) * math.exp(lgamma(2 * k + 1) - 2 * lgamma(k + 1) - 2 * k * log(2))
        out["O1_bent"].append(dict(k=k, m=m, Bk_over_I=exact, Bk_direct=(Bk / I if Bk is not None else None),
                                   asymptotic=2 / math.sqrt(math.pi * k), sqrtk_times_ratio=exact * math.sqrt(k)))
    # check B = sum_k B_k = m for a few m
    out["O1_total_check"] = {str(m): sum(comb(m, k - 1) * (m - k + 1) * 2.0 ** (1 - m) for k in range(1, m + 1)) for m in (4, 10, 30)}
    for n in (101, 1001, 10001, 100001, 1000001):
        for beta in (0.5, 1.0, 2.0):  # t = n/2 - beta sqrt(n)/2  -> constant bias
            t = int(round(n / 2 - beta * math.sqrt(n) / 2))
            pm = exp(log_pmf(t, n - 1))
            delta = cdf(t, n) if n <= 100001 else None
            if delta is None:
                # normal approximation with continuity correction, flagged
                z = (t + 0.5 - n / 2) / (math.sqrt(n) / 2)
                delta = 0.5 * math.erfc(-z / math.sqrt(2))
                approx = True
            else:
                approx = False
            p0 = (1 - 2 * delta) ** 2
            p1 = pm * pm
            B0 = n * phi(p0, p1)
            var = 4 * delta * (1 - delta)
            I = n * pm
            out["O2_ball"].append(dict(n=n, t=t, beta=beta, delta=delta, delta_normal_approx=approx, Var=var, I=I,
                                       B0=B0, B0_over_Var=B0 / var, B0_over_I=B0 / I, W1=n * p1, B0_over_W1=B0 / (n * p1),
                                       log2n=log2(n)))
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)
    for r in out["O1_bent"]:
        print(f"O1 k={r['k']:4d}  B_k/I={r['Bk_over_I']:.5f}  sqrt(k)*ratio={r['sqrtk_times_ratio']:.5f}  (2/sqrt(pi)={2/math.sqrt(math.pi):.5f})")
    print("O1 totals B (should equal m):", out["O1_total_check"])
    for r in out["O2_ball"]:
        print(f"O2 n={r['n']:8d} beta={r['beta']}  delta={r['delta']:.4f}  B0/Var={r['B0_over_Var']:.3f}  B0/W1={r['B0_over_W1']:.3f}  B0/I={r['B0_over_I']:.5f}  log2n={r['log2n']:.2f}{'  (normal approx)' if r['delta_normal_approx'] else ''}")


if __name__ == "__main__":
    main()
