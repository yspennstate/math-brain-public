"""Exact rational certificate for a 16-state MMPP survival-order violation.

No floating-point operation is used in the mathematical certificate.
The printed decimal strings are only displays of exact rational quantities.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import factorial
import json

N = 80
T = F(12)
V = [1000, 924, 707, 383, 0, -383, -707, -924,
     -1000, -924, -707, -383, 0, 383, 707, 924]
assert len(V) == 16 and sum(V) == 0
D = [F(10000 + v, 1000000) for v in V]
LAM = sum(D, F(0)) / 16
assert LAM == F(1, 100)
assert min(D) == F(9, 1000) and max(D) == F(11, 1000)
PI = [F(1, 16)] * 16
ALPHA = [p * d / LAM for p, d in zip(PI, D)]
W = [p - a for p, a in zip(PI, ALPHA)]
assert sum(ALPHA, F(0)) == 1 and all(a > 0 for a in ALPHA)

# C = Q-D, r=1+max(D), B=T(C+rI).  B has diagonal
# T(max(D)-D_i), forward-cycle entries T, and all other entries zero.
R = 1 + max(D)
BDIAG = [T * (max(D) - d) for d in D]
L = max(T + x for x in BDIAG)
assert R == F(1011, 1000) and L == F(1503, 125)
WNORM = sum(map(abs, W), F(0))

# term is W B^k / k!, updated without storing a dense matrix.
term = W.copy()
S = sum(term, F(0))
for k in range(1, N + 1):
    term = [(term[j] * BDIAG[j] + T * term[(j - 1) % 16]) / k
            for j in range(16)]
    S += sum(term, F(0))

# ||B||_infty=L.  The scalar series tail is bounded geometrically,
# since successive ratios after k=N+1 do not exceed L/(N+2)<1.
TAIL = WNORM * L ** (N + 1) / factorial(N + 1) / (1 - L / (N + 2))
assert L / (N + 2) < 1
assert TAIL < F(1, 10**31)
assert S + TAIL < -F(39, 10)
assert -F(4) < S - TAIL

# Therefore -4 < W exp(B) 1 < -3.9 exactly.  Since
# W exp(TC)1 = exp(-rT) W exp(B)1, the desired difference is negative.
# exp(-rT) > 3^-13, using rT=12.132<13 and e<3.
CERTIFIED_NEGATIVE_BOUND = -F(39, 10 * 3**13)

def resolvent_apply(rhs):
    """Solve (D-Q)x=rhs exactly using the directed-cycle recurrence."""
    multiplier, offset = F(1), F(0)
    for d, b in zip(D, rhs):
        multiplier *= 1 + d
        offset = (1 + d) * offset + b
    x0 = offset / (multiplier - 1)
    x = [x0]
    for i in range(15):
        x.append((1 + D[i]) * x[i] - rhs[i])
    assert (1 + D[15]) * x[15] - x0 == rhs[15]
    assert all((1 + D[i]) * x[i] - x[(i + 1) % 16] == rhs[i]
               for i in range(16))
    return x

RONE = resolvent_apply([F(1)] * 16)
RRONE = resolvent_apply(RONE)
MU_PI = sum(RONE, F(0)) / 16
M2_PI = 2 * sum(RRONE, F(0)) / 16
SCV_PI = M2_PI / MU_PI ** 2 - 1
assert F(0) < SCV_PI < F(199999, 200000) < 1
MEAN_ALPHA = sum(a * x for a, x in zip(ALPHA, RONE))
M2_ALPHA = 2 * sum(a * x for a, x in zip(ALPHA, RRONE))
SCV_ALPHA = M2_ALPHA / MEAN_ALPHA ** 2 - 1
assert MEAN_ALPHA == F(100)
assert SCV_ALPHA > 1

def dec(x):
    with localcontext() as ctx:
        ctx.prec = 60
        return str(Decimal(x.numerator) / Decimal(x.denominator))

report = {
    "arithmetic": "fractions.Fraction, exact rational; decimals are display only",
    "states": 16,
    "cycle_transition_rate": "1",
    "arrival_rates": [str(d) for d in D],
    "mean_arrival_rate": str(LAM),
    "t": str(T),
    "r": str(R),
    "B_infinity_norm": str(L),
    "signed_initial_row_l1": str(WNORM),
    "series_degree": N,
    "partial_sum_display": dec(S),
    "absolute_tail_bound_display": dec(TAIL),
    "exact_assertions": ["tail < 10^-31", "-4 < S-tail", "S+tail < -39/10"],
    "certified_difference_upper_bound": str(CERTIFIED_NEGATIVE_BOUND),
    "certified_difference_upper_bound_display": dec(CERTIFIED_NEGATIVE_BOUND),
    "time_stationary_mean_display": dec(MU_PI),
    "time_stationary_second_moment_display": dec(M2_PI),
    "time_stationary_SCV_display": dec(SCV_PI),
    "time_stationary_SCV_exact_assertion": "0 < SCV_pi < 199999/200000 < 1",
    "event_stationary_SCV_display": dec(SCV_ALPHA),
    "event_stationary_SCV_exact_assertion": "SCV_alpha > 1 (the separate established theorem is respected)",
    "conclusion": "Conjecture 3.9 fails; also the time-stationary SCV>=1 question in He2021 Section4.3 fails"
}
print(json.dumps(report, indent=2))
