"""Small independent checks supporting PROOF.md; standard library only.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 audit_geometry.py
This checks constants and constructions, not the diffusion conjecture.
"""
import math
import os
import resource
import time
from fractions import Fraction

# Bounded standard-library loops; report and check peak resident memory below.
started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
print("priority", os.getpriority(os.PRIO_PROCESS, 0))


def ball_gamma(j):
    return math.pi ** (j / 2) / math.gamma(1 + j / 2)


def ball_recurrence(j):
    # Integrate a two-coordinate disk to obtain kappa_j=2*pi*kappa_(j-2)/j.
    if j == 0:
        return 1.0
    if j == 1:
        return 2.0
    return (2 * math.pi / j) * ball_recurrence(j - 2)


def simpson(f, end, n=2048):
    h = end / n
    return h / 3 * (f(0) + f(end) + sum(
        (4 if k % 2 else 2) * f(k * h) for k in range(1, n)))


max_volume_error = 0.0
for d in range(2, 9):
    for r in (0.1, 0.7, 2.0):
        L = 3.4
        # Independently integrate the two caps by axial cross-sections.
        caps = 2 * ball_recurrence(d - 1) * r**d * simpson(
            lambda theta: math.cos(theta)**d, math.pi / 2)
        fubini = ball_recurrence(d - 1) * r**(d - 1) * L + caps
        cylinder_ball = ball_gamma(d - 1) * r**(d - 1) * L + ball_gamma(d) * r**d
        error = abs(fubini - cylinder_ball) / cylinder_ball
        max_volume_error = max(max_volume_error, error)
        assert error < 2e-11, (d, r, error)
        assert math.isclose(ball_gamma(d), ball_recurrence(d), rel_tol=2e-14)
print("sausage volumes d=2..8, three radii: max relative discrepancy %.3g" % max_volume_error)

# Check every geometric face margin exactly; no floating point here.
r = Fraction(7, 10)
L = Fraction(17, 5)
cell = L + 3*r
initial, final = 3*r/2, 3*r/2 + L
assert initial-r == r/2
assert cell-(final+r) == r/2
assert 3*r/2-r == r/2
assert 3*r-(3*r/2+r) == r/2
print("independent sausage cells: all face margins exactly r/2; adjacent supports gap r")

# Check the shell-volume bound used for the direction-net cardinality.
# The shell difference is computed from its odd binomial terms, avoiding cancellation.
worst_ratio = 0.0
for d in range(2, 9):
    for alpha in (0.5, 0.1, 0.01, 0.001):
        shell = sum(2 * math.comb(d, k) * (alpha/2)**k
                    for k in range(1, d+1, 2))
        upper = d * alpha * (5/4)**(d-1)
        assert shell <= upper
        worst_ratio = max(worst_ratio, shell/upper)
print("sphere-shell bound d=2..8: largest shell / bound %.6f" % worst_ratio)

# The leading constants by transverse shadow and by rescaling to radius one.
lam, r = 0.23, 0.7
for d in (2, 3, 5):
    a = lam * ball_gamma(d-1) * r**(d-1)
    coefficient = d/a
    scaled = r * d / (lam * r**d * ball_recurrence(d-1))
    assert math.isclose(coefficient, scaled, rel_tol=2e-14)
    if d == 2:
        assert math.isclose(coefficient, 1/(lam*r), rel_tol=2e-14)
    if d == 3:
        assert math.isclose(coefficient, 3/(lam*math.pi*r*r), rel_tol=2e-14)
    print("d=%d a=%.10f d/a=%.10f (shadow and radius-one scaling agree)" % (d,a,coefficient))

# Independently check logarithmic rates of the actual finite-scale formulas.
d = 3
a = lam * ball_gamma(d-1) * r**(d-1)
epsilon = 0.25
c_upper = (1+epsilon)*d/a
eta = r * (1 - (1+epsilon)**(-1/(2*(d-1))))
b = lam * ball_gamma(d-1) * (r-eta)**(d-1)
K = d * 2**d * (5/4)**(d-1)
c_lower = (1-epsilon)*d/a
print("logR, log(U)/logR, log(N*p)/logR")
last_upper, last_lower = None, None
for s in (20., 40., 80., 160.):
    R = math.exp(s)
    L = c_upper*s
    log_upper = (d*math.log(2*R*math.sqrt(d)/eta+3) + math.log(K)
                 + (d-1)*math.log(2*L/eta) - lam*ball_gamma(d)*(r-eta)**d - b*L)
    L = c_lower*s
    A = 2*R/math.sqrt(d)
    n1, n2 = math.floor(A/(L+3*r)), math.floor(A/(3*r))
    assert n1 > 0 and n2 > 0
    log_np = (math.log(n1) + (d-1)*math.log(n2)
              - lam*ball_gamma(d)*r**d - a*L)
    print("%5.0f % .8f % .8f" % (s, log_upper/s, log_np/s))
    last_upper, last_lower = log_upper, log_np
assert last_upper < 0 and last_lower > 0
assert math.isclose(d-b*c_upper, d*(1-math.sqrt(1+epsilon)), rel_tol=2e-14)
print("limiting rates %.8f %.8f" % (d-b*c_upper, d-a*c_lower))

# Recheck the earlier scale witness without huge exponentials.
for s in (4., 16., 64.):
    log_r, log_T = -s, 2*s-1.5*math.log(s)
    old = math.exp(log_T + 2*log_r + 2*math.log(s))
    new = math.exp(log_T + 2*log_r + math.log(s))
    assert math.isclose(old, math.sqrt(s), rel_tol=2e-13)
    assert math.isclose(new, 1/math.sqrt(s), rel_tol=2e-13)
    print("earlier witness s=%g old=%.8g new=%.8g" % (s, old, new))

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# ru_maxrss is bytes on macOS (this host).
assert rss < 1024**3
print("peak resident bytes", rss)
print("PASS; elapsed %.3f seconds" % (time.monotonic()-started))
