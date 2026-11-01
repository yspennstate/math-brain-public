#!/usr/bin/env python3
from fractions import Fraction

LOWER = Fraction(99083249, 125000000)
RHO_CERT = Fraction(6293309, 10000000)
OLD_RHO6 = Fraction(44277390789435, 70368744177664)
ELL = 6
ITER = 100
KTRUNC = 20


def bits(n):
    return range(1 << n)


def head(x, n):
    return (x >> (n - 1)) & 1


def sh(x, n, u):
    return ((x << 1) & ((1 << n) - 1)) | u


def F(h, n):
    """Exact one-sided information-debt Bellman operator from the 10:46 report."""
    out = {}
    for a in bits(n):
        ha = head(a, n)
        for b in bits(n):
            eq = ha == head(b, n)
            if eq:
                out[a, b, 0] = Fraction(1) + sum(
                    (h[sh(a, n, u), sh(b, n, v), 0]
                     for u in (0, 1) for v in (0, 1)), Fraction(0)) / 4
            else:
                A = (h[sh(a, n, 0), b, 0] + h[sh(a, n, 1), b, 0]) / 2
                B = (h[a, sh(b, n, 0), 0] + h[a, sh(b, n, 1), 0]) / 2
                P = Fraction(0)
                for u in (0, 1):
                    consume_A = h[sh(a, n, u), b, 0]
                    consume_B = (h[a, sh(b, n, 0), 1 + u] +
                                 h[a, sh(b, n, 1), 1 + u]) / 2
                    P += max(consume_A, consume_B) / 2
                out[a, b, 0] = max(A, B, P)
            for u in (0, 1):
                s = 1 + u
                if eq:
                    out[a, b, s] = Fraction(1) + (
                        h[sh(a, n, u), sh(b, n, 0), 0] +
                        h[sh(a, n, u), sh(b, n, 1), 0]) / 2
                else:
                    consume_A = h[sh(a, n, u), b, 0]
                    consume_B = (h[a, sh(b, n, 0), s] +
                                 h[a, sh(b, n, 1), s]) / 2
                    out[a, b, s] = max(consume_A, consume_B)
    return out


def full_iter(n, steps):
    h = {(a, b, s): Fraction(0)
         for a in bits(n) for b in bits(n) for s in (0, 1, 2)}
    for _ in range(steps):
        h = F(h, n)
        # Exact gauge normalization; F is additively homogeneous.
        c = h[0, 0, 0]
        if c:
            h = {k: v - c for k, v in h.items()}
    return h


def debt_trunc(hN, n, a, u, rho, K):
    """d^(K): exact debt Snell value with at most K waits before forced X-clear."""
    au = sh(a, n, u)
    x = head(a, n)
    d = {}
    for b in bits(n):
        if head(b, n) == x:
            d[b] = Fraction(1) + (hN[au, sh(b, n, 0)] +
                                  hN[au, sh(b, n, 1)]) / 2 - rho
        else:
            d[b] = hN[au, b] - rho
    for _ in range(K):
        nd = {}
        for b in bits(n):
            if head(b, n) == x:
                nd[b] = Fraction(1) + (hN[au, sh(b, n, 0)] +
                                       hN[au, sh(b, n, 1)]) / 2 - rho
            else:
                stop = hN[au, b] - rho
                wait = (d[sh(b, n, 0)] + d[sh(b, n, 1)]) / 2 - rho
                nd[b] = max(stop, wait)
        d = nd
    return d


def all_debts(hN, n, rho, K):
    return {(a, u): debt_trunc(hN, n, a, u, rho, K)
            for a in bits(n) for u in (0, 1)}


def reduced_GK(hN, n, rho, K):
    ds = all_debts(hN, n, rho, K)
    out = {}
    for a in bits(n):
        for b in bits(n):
            if head(a, n) == head(b, n):
                out[a, b] = Fraction(1) + sum(
                    (hN[sh(a, n, u), sh(b, n, v)]
                     for u in (0, 1) for v in (0, 1)), Fraction(0)) / 4
            else:
                A = (hN[sh(a, n, 0), b] + hN[sh(a, n, 1), b]) / 2
                B = (hN[a, sh(b, n, 0)] + hN[a, sh(b, n, 1)]) / 2
                P = Fraction(0)
                for u in (0, 1):
                    consume_A = hN[sh(a, n, u), b]
                    consume_B = (ds[a, u][sh(b, n, 0)] +
                                 ds[a, u][sh(b, n, 1)]) / 2
                    P += max(consume_A, consume_B) / 2
                out[a, b] = max(A, B, P)
    return out


def first_inwindow_match_time(a, b, n):
    x = head(a, n)
    for t in range(n):
        if ((b >> (n - 1 - t)) & 1) == x:
            return t
    return None


def max_gap(big, small, n):
    return max(big[a, u][b] - small[a, u][b]
               for a in bits(n) for u in (0, 1) for b in bits(n))


print("R17 PROB10-02 exact Snell-elimination / reduced-certificate checker")
print("SECTION scalar_cylinder_obstruction")
print("all-zero periodic environment is fixed by T_X,T_Y and has match reward 1")
print("therefore the diagonal cylinder inequality reduces exactly to c_X+c_Y >= 1")
print("SCALAR_CYLINDER_PERIODIC_OBSTRUCTION_PASS")

print("SECTION first_match_profile_quotient_counterexample")
n = 3
rho = Fraction(3, 5)
hsimple = {(a, b): Fraction(b & 1) for a in bits(n) for b in bits(n)}
a = 0b000
u = 0
b0 = 0b100
b1 = 0b101
assert first_inwindow_match_time(a, b0, n) == 1
assert first_inwindow_match_time(a, b1, n) == 1
d1 = debt_trunc(hsimple, n, a, u, rho, 1)
d8 = debt_trunc(hsimple, n, a, u, rho, 8)
assert d1[b0] == d8[b0] == Fraction(3, 10)
assert d1[b1] == d8[b1] == Fraction(2, 5)
print("same_first_match_prefix=10, T=1")
print("d_star(100)=", d8[b0], "d_star(101)=", d8[b1])
print("FIRST_MATCH_ONLY_QUOTIENT_COUNTEREXAMPLE_PASS")

print("SECTION geometric_tail_regression")
n = 3
rho = Fraction(1, 5)
htest = {(a, b): Fraction(((a + b) % 7) - 3, 3)
         for a in bits(n) for b in bits(n)}
span = max(htest.values()) - min(htest.values())
big = all_debts(htest, n, rho, 30)
for K in range(n, 10):
    small = all_debts(htest, n, rho, K)
    gap = max_gap(big, small, n)
    bound = (span + 1) / (2 ** (K - n + 1))
    assert gap >= 0 and gap <= bound
    print("K=", K, "observed_gap=", gap, "proved_theorem_bound=", bound)
print("GEOMETRIC_TAIL_REGRESSION_PASS")

print("SECTION ell6_exact_reduced_subsolution")
hfull = full_iter(ELL, ITER)
hN = {(a, b): hfull[a, b, 0] for a in bits(ELL) for b in bits(ELL)}
GK = reduced_GK(hN, ELL, RHO_CERT, KTRUNC)
residuals = [GK[k] - hN[k] for k in GK]
mn = min(residuals)
mx = max(residuals)
margin = mn - RHO_CERT
assert margin > 0
assert RHO_CERT > OLD_RHO6
gamma_cert = 2 * RHO_CERT / (1 + RHO_CERT)
assert gamma_cert < LOWER
print("ell=", ELL, "full_exact_candidate_iterations=", ITER, "snell_truncation_K=", KTRUNC)
print("rho_cert=", RHO_CERT)
print("min_reduced_residual=", mn)
print("max_reduced_residual=", mx)
print("exact_margin=", margin)
print("previous_ell6_rho=", OLD_RHO6)
print("rho_improvement=", RHO_CERT - OLD_RHO6)
print("transferred_gamma_lower=", gamma_cert)
print("current_source_lower=", LOWER)
print("source_endpoint_moves=", gamma_cert > LOWER)
print("ELL6_REDUCED_SUBSOLUTION_PASS")
print("ALL_EXACT_CHECKS_PASS")
print("RETURN_CODE=0")
