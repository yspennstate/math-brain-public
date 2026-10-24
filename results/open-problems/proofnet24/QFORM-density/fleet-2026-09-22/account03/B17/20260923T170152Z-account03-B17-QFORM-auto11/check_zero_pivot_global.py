from fractions import Fraction as F

# Exact-rational certificate for the analytic comparison in REPORT.md.
# No floating-point value is used in any assertion.

def atan_interval_unit_fraction(q: int, n_even: int):
    """Alternating-series interval for atan(1/q).

    n_even must be even. The partial sum through n_even ends positive and is
    an upper bound; appending the next (negative) term is a lower bound.
    """
    assert n_even % 2 == 0 and q > 1
    x = F(1, q)
    s = F(0)
    for n in range(n_even + 1):
        s += ((-1) ** n) * x ** (2*n + 1) / F(2*n + 1)
    upper = s
    n = n_even + 1
    lower = s - x ** (2*n + 1) / F(2*n + 1)
    return lower, upper

# Self-contained Machin interval:
# pi = 16 atan(1/5) - 4 atan(1/239).
a5_lo, a5_hi = atan_interval_unit_fraction(5, 10)
a239_lo, a239_hi = atan_interval_unit_fraction(239, 2)
pi_lo = 16*a5_lo - 4*a239_hi
pi_hi = 16*a5_hi - 4*a239_lo
assert pi_lo < pi_hi

# w=2^(-1/4) < 0.840897 because (0.840897)^4 > 1/2.
w_hi = F(840897, 10**6)
assert w_hi**4 > F(1, 2)

# sqrt(3/(2*pi)) < 0.690989.  It suffices to use pi>=pi_lo.
sf_hi = F(690989, 10**6)
assert sf_hi**2 > F(3, 1)/(2*pi_lo)

# Exact coefficients obtained after integrating the n=0,...,4 alternating
# erf majorant against the convex-chord majorant for (1+u^2)^(-1/4).
A = F(1580209, 2587200)
B = F(38243, 147840)
H_hi = 2*sf_hi*(A + B*w_hi)

# Tail J(1)=atanh(w)+atan(w).
# atan(w)=pi/4-atan((1-w)/(1+w)).  Since w<=w_hi, the transformed
# argument is >= r_lo.  The alternating partial sum ending negative is a
# lower bound for atan(r_lo), hence gives an upper bound for atan(w).
r_lo = (1-w_hi)/(1+w_hi)
atan_r_lo = r_lo - r_lo**3/F(3) + r_lo**5/F(5) - r_lo**7/F(7)
atan_w_hi = pi_hi/F(4) - atan_r_lo

# Positive atanh series at w_hi plus a geometric remainder.
N = 70
atanh_hi = F(0)
for n in range(N + 1):
    atanh_hi += w_hi**(2*n + 1)/F(2*n + 1)
atanh_hi += w_hi**(2*N + 3)/(F(2*N + 3)*(1-w_hi**2))

I_hi = H_hi + atan_w_hi + atanh_hi
assert I_hi < F(306811, 100000)  # I < 3.06811

# sqrt(6/pi)=2 sqrt(3/(2*pi)) < 2*sf_hi.
C_hi = (2*sf_hi)*F(306811, 100000)
assert C_hi < F(4240061, 1000000)  # < 4.240061
assert F(4240061, 1000000)**2 < F(18, 1)  # 4.240061 < 3 sqrt(2)

# Aggregate-basis matrix of the exact finite physical family.
M = ((0,1,0),(1,0,0),(0,0,1))
M2 = tuple(tuple(sum(M[i][k]*M[k][j] for k in range(3)) for j in range(3)) for i in range(3))
assert M2 == ((1,0,0),(0,1,0),(0,0,1))
assert sum(M[i][i] for i in range(3)) == 1
# determinant by direct 3x3 expansion
D = (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
     - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
     + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
assert D == -1

print("pi interval width:", float(pi_hi-pi_lo))
print("head upper:", float(H_hi))
print("atan(w) upper:", float(atan_w_hi))
print("atanh(w) upper:", float(atanh_hi))
print("I upper:", float(I_hi))
print("density upper certificate:", float(C_hi))
print("PASS QFORM_ZERO_PIVOT_GLOBAL_FOURIER_CERT")
