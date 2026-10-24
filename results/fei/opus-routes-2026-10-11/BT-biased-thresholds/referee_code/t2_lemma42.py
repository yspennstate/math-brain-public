"""Lemma 4.2 (DTC identity) for increasing T under arbitrary product laws.

Claim: alpha = mu(T=1) > 0, Y ~ mu_A, c_i = q_i rho_i / alpha (= mu_A(Y_i=1, i pivotal)),
    ln(1/alpha) = sum_i c_i ln(1/q_i) - DTC(mu_A),  DTC = H(Y) - sum_i H(Y_i | Y_-i) >= 0,
hence alpha ln(1/alpha) <= sum_i q_i ln(1/q_i) rho_i.
Everything is computed from the joint law mu_A directly (no use of the route's formulas).
"""
import random
import time
from fractions import Fraction as Fr
import mpmath
from bfcore import *

mpmath.mp.dps = 70


def H_of(ps):
    s = mpmath.mpf(0)
    for p in ps:
        if p > 0:
            s += mpq(p) * mpmath.log(mpq(1 / p))
    return s


def dtc_check(T, qs):
    n = len(qs)
    w = mu_weights(qs)
    alpha = sum(w[y] for y in range(1 << n) if T[y] == 1)
    if alpha == 0:
        return None
    muA = [w[y] / alpha if T[y] == 1 else Fr(0) for y in range(1 << n)]
    HY = H_of(muA)
    condsum = mpmath.mpf(0)
    rhos, cs, cdirect = [], [], []
    for i in range(n):
        bit = 1 << i
        # H(Y_i | Y_-i) under mu_A, from the joint law
        for y in range(1 << n):
            if y & bit:
                continue
            p0, p1 = muA[y], muA[y | bit]
            tot = p0 + p1
            if tot > 0:
                condsum += mpq(tot) * H_of([p0 / tot, p1 / tot])
        d = pivotal(T, n, i)
        rho = sum(w[y] for y in range(1 << n) if not (y & bit) and d[y] == 1) / (1 - qs[i])
        # rho = mu(d_i = 1): d_i independent of y_i; summing over y_i=0 rows gives (1-q_i) rho
        rhos.append(rho)
        cs.append(qs[i] * rho / alpha)
        cdirect.append(sum(muA[y] for y in range(1 << n) if (y & bit) and d[y] == 1))
    DTC = HY - condsum
    lhs = mpmath.log(mpq(1 / alpha))
    rhs = sum(mpq(cs[i]) * mpmath.log(mpq(1 / qs[i])) for i in range(n)) - DTC
    ineq_l = mpq(alpha) * lhs
    ineq_r = sum(mpq(qs[i]) * mpmath.log(mpq(1 / qs[i])) * mpq(rhos[i]) for i in range(n))
    return {
        "id_err": abs(lhs - rhs),
        "DTC": DTC,
        "c_match": cs == cdirect,
        "ineq_slack": ineq_r - ineq_l,
    }


def rq(extreme=True):
    if extreme and random.random() < 0.35:
        return random.choice([Fr(1, 10 ** 8), Fr(10 ** 8 - 1, 10 ** 8), Fr(1, 3), Fr(1, 1000), Fr(999, 1000)])
    return Fr(random.randint(1, 999), 1000)


if __name__ == "__main__":
    random.seed(42)
    t0 = time.time()
    worst_id = mpmath.mpf(0)
    min_dtc = mpmath.mpf(1)
    min_slack = mpmath.mpf(10)
    cbad = 0
    cases = 0
    mono = {}
    for n in range(1, 5):
        mono[n] = []
        for code in range(1 << (1 << n)):
            T = [(code >> y) & 1 for y in range(1 << n)]
            if is_monotone(T, n):
                mono[n].append(T)
        for T in mono[n]:
            for rep in range(25 if n < 4 else 12):
                qs = [rq() for _ in range(n)]
                r = dtc_check(T, qs)
                if r is None:
                    continue
                cases += 1
                worst_id = max(worst_id, r["id_err"])
                min_dtc = min(min_dtc, r["DTC"])
                min_slack = min(min_slack, r["ineq_slack"])
                cbad += 0 if r["c_match"] else 1
    print("monotone counts", {n: len(mono[n]) for n in mono})
    print("all increasing T, n<=4:", cases, "cases; max |identity error|", mpmath.nstr(worst_id, 5),
          "; min DTC", mpmath.nstr(min_dtc, 5), "; min inequality slack", mpmath.nstr(min_slack, 5),
          "; c_i definition mismatches", cbad, "; time", round(time.time() - t0, 1))
    # weighted thresholds n = 6..10, random weights and extreme biases
    worst_id2 = mpmath.mpf(0)
    min_slack2 = mpmath.mpf(10)
    min_dtc2 = mpmath.mpf(1)
    c2 = 0
    for trial in range(120):
        n = random.randint(6, 10)
        w = [random.choice([1, 1, 2, 3, 5, 8, 13, 50]) for _ in range(n)]
        theta = random.randint(1, sum(w))
        T = threshold_table(w, theta)
        qs = [rq() for _ in range(n)]
        r = dtc_check(T, qs)
        if r is None:
            continue
        c2 += 1
        worst_id2 = max(worst_id2, r["id_err"])
        min_slack2 = min(min_slack2, r["ineq_slack"])
        min_dtc2 = min(min_dtc2, r["DTC"])
        if not r["c_match"]:
            cbad += 1
    print("weighted thresholds n=6..10:", c2, "cases; max |identity error|", mpmath.nstr(worst_id2, 5),
          "; min DTC", mpmath.nstr(min_dtc2, 5), "; min slack", mpmath.nstr(min_slack2, 5), "; c mismatches", cbad,
          "; time", round(time.time() - t0, 1))
    # Kahn-Kalai equality case: subcubes (AND of a subset) under common p
    for k in [1, 3, 6]:
        n = 6
        T = [1 if all((y >> j) & 1 for j in range(k)) else 0 for y in range(1 << n)]
        qs = [Fr(1, 7)] * n
        r = dtc_check(T, qs)
        print("subcube k=%d: inequality slack %s, DTC %s" % (k, mpmath.nstr(r["ineq_slack"], 5), mpmath.nstr(r["DTC"], 5)))
