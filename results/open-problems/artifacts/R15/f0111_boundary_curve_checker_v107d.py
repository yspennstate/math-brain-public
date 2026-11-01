"""R15 exact self-check for the U_K=N boundary theorem.

All interval endpoints and all log enclosures are rational Fractions.  The checker
covers only the retained F0111 screen; it says nothing about native I0076.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from functools import lru_cache
from math import factorial

# ---------- exact small-s arithmetic ----------
def exp_lower(q, n):
    q = F(q)
    return sum(q**j / F(factorial(j)) for j in range(n + 1))

def exp_upper(q, n):
    q = F(q)
    partial = exp_lower(q, n)
    first = q**(n + 1) / F(factorial(n + 1))
    ratio = q / F(n + 2)
    assert ratio < 1
    return partial + first / (1 - ratio)

assert exp_upper(F(3), 10) < F(201, 10)
assert F(201, 10)**4 < F(2320000, 13)
# Therefore exp(12)<2320000/13, so log S>12 when S>232/(13s), s<=1e-4.
assert exp_lower(F(6), 8) == F(1709, 5) > 341
# Therefore log(1+20 C)<6 for C=15,17.

for C in (15, 17):
    beta = F(C) + F(13, 232)  # B/s < C+13/232
    # t<401/400, q2<6, Umax<(9/8)s, c=3/100.
    alpha = F(C) - F(401, 400) * F(27, 4) - F(3, 200) * beta
    # A log^2 A <= p^2/A and L>12 on 0<s<=1e-4.
    rho = F(3, 100) * C*C / (F(24) * 10000 * (1 - F(C, 10000)))
    margin = 12 * alpha - 6 * beta - rho
    assert margin > 0
    print(f"SMALL_S_PASS N={12 if C==15 else 13} C={C} rational_margin={margin}")

# ---------- exact rational interval arithmetic ----------
@dataclass(frozen=True)
class IV:
    lo: F
    hi: F
    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError((self.lo, self.hi))
    @staticmethod
    def c(x):
        x = F(x)
        return IV(x, x)
    def __add__(self, other):
        other = other if isinstance(other, IV) else IV.c(other)
        return IV(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self):
        return IV(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + -(other if isinstance(other, IV) else IV.c(other))
    def __rsub__(self, other):
        return IV.c(other) - self
    def __mul__(self, other):
        other = other if isinstance(other, IV) else IV.c(other)
        vals = (self.lo*other.lo, self.lo*other.hi,
                self.hi*other.lo, self.hi*other.hi)
        return IV(min(vals), max(vals))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = other if isinstance(other, IV) else IV.c(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError((other.lo, other.hi))
        return self * IV(1 / other.hi, 1 / other.lo)
    def __rtruediv__(self, other):
        return IV.c(other) / self
    def sq(self):
        if self.lo <= 0 <= self.hi:
            return IV(F(0), max(self.lo*self.lo, self.hi*self.hi))
        vals = (self.lo*self.lo, self.hi*self.hi)
        return IV(min(vals), max(vals))
    def __pow__(self, n):
        if n == 0:
            return IV.c(1)
        if n == 2:
            return self.sq()
        if n < 0:
            return IV.c(1) / (self ** (-n))
        result, base = IV.c(1), self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result

# For 1<=y<2, log y=2 sum_{j>=0} w^(2j+1)/(2j+1), w=(y-1)/(y+1).
# The omitted positive tail is bounded by a geometric series, so these are
# exact rational lower/upper enclosures.
NTERMS = 12

def log_unit_bounds(y):
    w = (y - 1) / (y + 1)
    w2 = w*w
    term, partial = w, F(0)
    for j in range(NTERMS):
        partial += term / F(2*j + 1)
        term *= w2
    lo = 2 * partial
    rem = 2 * term / F(2*NTERMS + 1) / (1 - w2)
    return lo, lo + rem

LOG2 = log_unit_bounds(F(2))

@lru_cache(maxsize=200000)
def log_point_bounds(x):
    x = F(x)
    assert x > 0
    y, m = x, 0
    while y >= 2:
        y /= 2
        m += 1
    while y < 1:
        y *= 2
        m -= 1
    ly, uy = log_unit_bounds(y)
    l2, u2 = LOG2
    if m >= 0:
        return F(m)*l2 + ly, F(m)*u2 + uy
    return F(m)*u2 + ly, F(m)*l2 + uy

def log_iv(a):
    assert a.lo > 0
    lo, _ = log_point_bounds(a.lo)
    _, hi = log_point_bounds(a.hi)
    return IV(lo, hi)

# Exact U_K formula from the carried scalar reduction.
def UK(d, s):
    d, s = F(d), F(s)
    return F(29)*(d+1)*(d+s+1)*(d+2*s+1) / (4*(s+1)*(s+2))

# UK is strictly increasing in d.  Return an exact dyadic bracket of UK(d,s)=N.
def droot_bracket(N, s, iters=42):
    lo, hi = F(2, 5), F(3, 5)
    assert UK(lo, s) < N < UK(hi, s)
    for _ in range(iters):
        mid = (lo + hi) / 2
        if UK(mid, s) < N:
            lo = mid
        else:
            hi = mid
    assert UK(lo, s) < N < UK(hi, s)
    return lo, hi

# J = E - t Umax q1 q2 - (eps/2)V.  J>0 implies the exact boundary gate
# \widehat Gamma_N^partial >0 by the analytic inequality written in the report.
def J_box(N, C, slo, shi, c=F(3, 100)):
    # UK also increases in s, hence the root d_N(s) decreases in s.
    dlo, _ = droot_bracket(N, shi)
    _, dhi = droot_bracket(N, slo)
    d, s = IV(dlo, dhi), IV(slo, shi)
    z = 1 + s
    k = 2*z*(1-z*z) / ((1-d*d)*(d+3*z))
    y = (d+z)*(1-z)*(1-d-2*z) / (2*(1-d)*(d+3*z))
    x = 1-k-y
    K2 = (d+z)*(1-z*z) / (d+3*z)
    tJ, tK = (1-z)**2-K2, (1+z)**2-K2
    R = -2*(d+z)*(1-z*z)*(d*d*z+3*d*z*z+d+3*z**3) / (d+3*z)**2
    AJ, AK = 1+3*tJ*tJ/R, 1+3*tK*tK/R
    LK = y*AK
    Sval = -29/k
    Tcap = y*(N-LK)
    a, b = 1+d, 1-d
    Umax = F(1, 2)*((b/a)**2*Tcap - x + AJ*x*x)

    p = C*s
    A = 1-p
    D = 1/Sval
    B = p+D
    L = log_iv(Sval)
    logA = log_iv(A)
    q1 = log_iv(Sval*A)
    q2 = log_iv(1+p*Sval)
    logB = log_iv(B)
    entropy = -A*logA + p*L - B*q2
    variance = A*(logA**2) + B*(logB**2)
    eps = c/L
    t = 1+eps
    return entropy - t*Umax*q1*q2 - F(1, 2)*eps*variance

def certify_curve(N, C, smax):
    smin = F(1, 10000)
    stack = []
    # Start with 16 rational slabs and recursively refine only failures.
    for i in range(16):
        lo = smin + (smax-smin)*i/16
        hi = smin + (smax-smin)*(i+1)/16
        stack.append((lo, hi, 0))
    leaves = 0
    maxdepth = 0
    worst = None
    while stack:
        lo, hi, depth = stack.pop()
        J = J_box(N, C, lo, hi)
        if J.lo > 0:
            leaves += 1
            maxdepth = max(maxdepth, depth)
            worst = J.lo if worst is None or J.lo < worst else worst
            continue
        if depth >= 18:
            raise AssertionError(("uncertified slab", N, lo, hi, J.lo, J.hi))
        mid = (lo+hi)/2
        stack.append((mid, hi, depth+1))
        stack.append((lo, mid, depth+1))
    print("CURVE_PASS", "N=", N, "leaves=", leaves,
          "maxdepth=", maxdepth,
          "worst_lower_float=", float(worst),
          "worst_num_bits=", worst.numerator.bit_length(),
          "worst_den_bits=", worst.denominator.bit_length())

certify_curve(12, F(15), F(3601, 250000))
certify_curve(13, F(17), F(12637, 1000000))
print("BOUNDARY_UK_EQ_N_N12_N13_EXCLUDED")
print("ALL_EXACT_CHECKS_PASS")
