#!/usr/bin/env python3
"""
NM13-12 / T03 signed low-rank contraction witness certificate.

This is a sanity-check artifact for analytic theorems proved in the companion report.
It evaluates the exact finite-N probability that one of r orthogonal contracted
covariance eigenvectors is a feasible witness for the negative spherical perceptron.

For equal contracted eigenvalue lambda, with M constraints and t=1/sqrt(lambda),
a given contracted eigenvector is feasible with probability Phi(t)^M.
Because Gaussian coordinates along orthogonal eigenvectors are independent,
the r axis-witness events are independent, hence

    P(any contracted eigenvector is feasible)
      = 1 - (1 - Phi(t)^M)^r.

No simulation is used.
"""
import math

ALPHA_ISO_U = 12.78437096216
ALPHA_ISO_L = 6.30297437506

def normal_tail(t):
    return 0.5 * math.erfc(t / math.sqrt(2.0))

def axis_witness_probability(N, alpha, r, lam):
    M = int(math.floor(alpha * N))
    t = 1.0 / math.sqrt(lam)
    q = normal_tail(t)                 # q = P(Z < -t)
    log_p_one = M * math.log1p(-q)     # log Phi(t)^M
    p_one = 0.0 if log_p_one < -745.0 else math.exp(log_p_one)
    if p_one <= 0.0:
        p_any = 0.0
    elif p_one >= 1.0:
        p_any = 1.0
    else:
        log_none = r * math.log1p(-p_one)
        p_any = 1.0 if log_none < -745.0 else -math.expm1(log_none)
    return q, p_one, p_any, log_p_one

def poly_rank_scale(N, beta, c):
    L = math.log(N)
    t2 = 2.0 * L - 3.0 * math.log(L) + c
    assert t2 > 0
    return 1.0 / t2

def fixed_rank_scale(N, c):
    L = math.log(N)
    t2 = 2.0 * L - math.log(L) + c
    assert t2 > 0
    return 1.0 / t2

def axis_load_threshold(beta, c):
    # alpha for which alpha e^{-c/2}/sqrt(4pi) = beta
    return beta * math.sqrt(4.0 * math.pi) * math.exp(c / 2.0)

print("SIGNED_CONTRACTION_AXIS_CERTIFICATE")
print("isotropic_bracket", ALPHA_ISO_L, ALPHA_ISO_U)

# Main concrete separation used in the report.
beta = 0.25
c = 6.0
alpha_axis = axis_load_threshold(beta, c)
gap = alpha_axis - ALPHA_ISO_U
print("poly_rank_example beta c alpha_axis gap_over_iso_upper",
      beta, c, repr(alpha_axis), repr(gap))
assert alpha_axis > ALPHA_ISO_U + 5.0

# Same-alpha separation: isotropic is already rigorously UNSAT for alpha=12.9,
# while the contracted model is asymptotically SAT by an axis witness.
alpha_test = 12.9
a = alpha_test * math.exp(-c/2.0) / math.sqrt(4.0 * math.pi)
print("same_alpha_test", alpha_test, "axis_exponent", repr(a), "beta", beta)
assert ALPHA_ISO_U < alpha_test < alpha_axis
assert a < beta

for N in (10**6, 10**8, 10**10, 10**12, 10**14):
    r = max(1, int(N ** beta))
    lam = poly_rank_scale(N, beta, c)
    q, p_one, p_any, log_p_one = axis_witness_probability(N, alpha_test, r, lam)
    L = math.log(N)
    asym_tail_const = math.exp(-c/2.0) / math.sqrt(4.0 * math.pi)
    tail_ratio = (N * q / L) / asym_tail_const
    log_rp = math.log(r) + log_p_one
    print("poly_N", N,
          "r", r,
          "lambda", repr(lam),
          "p_one", repr(p_one),
          "p_any", repr(p_any),
          "tail_ratio", repr(tail_ratio),
          "log_rp", repr(log_rp))

# Rank-one extreme contraction: lambda=1/(3 log N) makes a fixed eigenvector
# feasible whp for every fixed alpha.  Numerical values show the exact formula.
for N in (10**4, 10**6, 10**8, 10**10):
    lam = 1.0 / (3.0 * math.log(N))
    q, p_one, p_any, _ = axis_witness_probability(N, ALPHA_ISO_U + 0.5, 1, lam)
    print("rank1_strong_contraction_N", N,
          "lambda", repr(lam),
          "tail", repr(q),
          "p_axis", repr(p_one))
assert axis_witness_probability(10**10, ALPHA_ISO_U + 0.5, 1,
                                1.0/(3.0*math.log(10**10)))[1] > 0.9999

# Fixed-r critical window check:
# if t_N^2=2 log N - log log N + c, then
# N \bar Phi(t_N) -> e^{-c/2}/sqrt(4pi),
# and a single-axis feasibility probability tends exp(-alpha * that constant).
c0 = 0.0
limit_tail = math.exp(-c0/2.0) / math.sqrt(4.0 * math.pi)
limit_p = math.exp(-alpha_test * limit_tail)
print("fixed_rank_limit tail_const p_one_limit", repr(limit_tail), repr(limit_p))
for N in (10**6, 10**10, 10**14):
    lam = fixed_rank_scale(N, c0)
    q, p_one, _, _ = axis_witness_probability(N, alpha_test, 1, lam)
    print("fixed_rank_N", N,
          "Ntail", repr(N*q),
          "p_one", repr(p_one))
# loose sanity: large-N values must be near the asymptotic constants.
q14, p14, _, _ = axis_witness_probability(10**14, alpha_test, 1,
                                          fixed_rank_scale(10**14, c0))
assert abs(10**14*q14 - limit_tail) < 0.01
assert abs(p14 - limit_p) < 0.005

print("ALL_CHECKS_PASS")
