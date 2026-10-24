# Evaluates the bound of Proposition 4 (two_sheet_side/REPORT.md) with the explicit constants of Proposition 3,
# at |lambda| = 1, the worst case allowed there.  a(c, R) is c times the Proposition 3 bound with lambda/c and
# cR, with log kappa added inside the logarithm; kappa is computed for the trapezoid cutoff (1 on [-1,1], 0 outside
# [-2,2]).  The recursion D(c) <= a(c, 5 K u^{1/2}) + 2 e^{-2u} D(2c) is unrolled J times with u_j = j + u_0, and
# D(2^J) is replaced by the crude bound a(2^J, K m^{1/2}/2); u_0 is taken as the best value on a grid.
import math
from scipy.integrate import quad

def phihat(e):
    if abs(e) < 1e-12:
        return 3.0
    return (2 * math.sin(1.5 * e) / e) * (2 * math.sin(0.5 * e) / e)

pieces = [quad(lambda e: abs(phihat(e)), k, k + 1, limit=200)[0] for k in range(400)]
kappa = 2 * (sum(pieces) + 4.0 / 400) / (2 * math.pi)     # tail |phihat| <= 4/e^2 beyond 400

def prop3(lam, logR, logk):
    inner = 2 * math.sqrt(2) * abs(lam) ** -0.5 * (1 + math.sqrt(2 * logR + 4 * math.pi))
    return (0.5 + (640 * math.sqrt(2) / math.pi) * abs(lam) ** -0.5
            + 2 * math.sqrt(2) * (1 + logk + max(0.0, math.log(inner))))

def a(c, logR, logk):
    return c * prop3(1.0 / c, math.log(c) + logR, logk)

def bound(logK, logm, u0, J=14):
    tot, coef = 0.0, 1.0
    for j in range(J):
        uj = j + u0
        tot += coef * a(2.0 ** j, math.log(5) + logK + 0.5 * math.log(uj), math.log(kappa))
        coef *= 2 * math.exp(-2 * uj)
    tail = coef * a(2.0 ** J, logK + 0.5 * logm - math.log(2), 0.0)
    return tot + tail, tail

print("kappa for the trapezoid cutoff: %.4f" % kappa)
print("%-10s %-8s %-40s %-10s %s" % ("K", "best u0", "bound for m = 10, 1e6, 1e100, 1e300", "tail", "sqrt2 loglogK"))
for logK in [math.log(3), 3 * math.log(10), 6 * math.log(10), 12 * math.log(10), 50 * math.log(10), 300 * math.log(10), 3000 * math.log(10)]:
    grid = [1 + 0.05 * i for i in range(400)]
    best = min(grid, key=lambda u0: bound(logK, 300 * math.log(10), u0)[0])
    vals = [bound(logK, lm * math.log(10), best)[0] for lm in (1, 6, 100, 300)]
    tail = bound(logK, 300 * math.log(10), best)[1]
    print("e^%-8.2f %-8.2f %-40s %-10.1e %.3f" % (logK, best, " ".join("%.3f" % v for v in vals), tail,
                                               math.sqrt(2) * math.log(logK)))
