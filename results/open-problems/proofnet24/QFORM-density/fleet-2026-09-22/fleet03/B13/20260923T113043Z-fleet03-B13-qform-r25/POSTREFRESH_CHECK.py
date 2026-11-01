import math
import random

# Exact constant from fleet01/B13 Nystrom rigidity.
C_N = math.sqrt(128**8 + 32**8)
assert abs(C_N - 268437503.99218756) < 1e-6

# Deterministic pseudo-random sanity checks of the two support-box inequalities.
# These are checks only; the report contains the proofs.
random.seed(13025)
max_frob_ratio = 0.0
max_maxnorm_ratio = 0.0
for m in (2, 3, 5, 10):
    for _ in range(500):
        A = [[random.gauss(0.0, 1.0) for _ in range(m)] for _ in range(m)]
        E = [[0.5*(A[i][j] + A[j][i]) for j in range(m)] for i in range(m)]
        r = [math.exp(random.gauss(0.0, 1.0)) for _ in range(m)]
        y = [(2.0*random.random()-1.0)*r[i] for i in range(m)]
        lhs = abs(sum(y[i]*E[i][j]*y[j] for i in range(m) for j in range(m)))
        frob = math.sqrt(sum(E[i][j]**2 for i in range(m) for j in range(m)))
        b_frob = frob*sum(x*x for x in r)
        maxnorm = max(abs(E[i][j]) for i in range(m) for j in range(m))
        b_max = maxnorm*(sum(r)**2)
        assert lhs <= b_frob*(1+1e-12)
        assert lhs <= b_max*(1+1e-12)
        if b_frob:
            max_frob_ratio = max(max_frob_ratio, lhs/b_frob)
        if b_max:
            max_maxnorm_ratio = max(max_maxnorm_ratio, lhs/b_max)

# Algebra behind the half-ratio threshold and fifth-power support-spread corollary.
# If 2*C_N*R1sq/(L*rho^4*d) <= 1, denominator in (5.3) is <=2.
for rho in (2.0, 5.0, 20.0):
    L, d = 0.7, 0.4
    R1sq = L*rho**4*d/(2*C_N)
    denominator = 1 + 2*C_N*R1sq/(L*rho**4*d)
    assert abs(denominator-2.0) < 1e-12

print('QFORM_B13_R25_POSTREFRESH_CHECK_PASS')
print('C_N=', format(C_N, '.12f'))
print('max_frob_sample_ratio=', format(max_frob_ratio, '.12f'))
print('max_maxnorm_sample_ratio=', format(max_maxnorm_ratio, '.12f'))
