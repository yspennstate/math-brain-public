from math import sqrt, pi, exp
import sympy as sp
import mpmath as mp

mp.mp.dps = 80

# Exact constants from the proof.
d0 = sqrt(2.0) - 1.0
c_pair = 2.0 * (sqrt(2.0) - 1.0)
kappa0 = 9.0/8.0 * d0*d0
C_dec = c_pair * (pi*pi/6.0) / kappa0
C_dec_closed = 8.0*pi*pi*(sqrt(2.0)+1.0)/27.0

print(f"d0={d0:.15f}")
print(f"c_pair={c_pair:.15f}")
print(f"kappa0={kappa0:.15f}")
print(f"C_dec={C_dec:.15f}")
print(f"C_dec_closed={C_dec_closed:.15f}")
assert abs(C_dec-C_dec_closed) < 1e-13

# Symbolic Hellinger/cubic-tilt identity:
# E[D_a^theta D_b^(1-theta)]
# = exp(-(9/2) theta(1-theta)(a-b)^2 t).
a,b,th = sp.symbols('a b th', positive=True)
exponent = sp.Rational(1,2)*(3*(th*a+(1-th)*b))**2 \
           - sp.Rational(9,2)*(th*a*a+(1-th)*b*b)
target = -sp.Rational(9,2)*th*(1-th)*(a-b)**2
print("hellinger_symbolic_residual=", sp.simplify(exponent-target))
assert sp.simplify(exponent-target) == 0

# Pair inequality constant.
# With u=s+s^{-1} >=2, the normalized excess is
# h(u)=u^(3/2)-(u-1)*sqrt(u+2), whose derivative is negative.
u = sp.symbols('u', positive=True)
h = u**sp.Rational(3,2) - (u-1)*sp.sqrt(u+2)
dh = sp.simplify(sp.diff(h,u))
print("pair_h_at_2=", sp.simplify(h.subs(u,2)))
print("pair_h_derivative=", dh)
assert sp.simplify(h.subs(u,2) - (2*sp.sqrt(2)-2)) == 0

# High-precision numerical check of h(u)<=h(2) on a broad range.
h2 = 2*mp.sqrt(2)-2
max_ratio = mp.mpf('-inf')
argmax = None
for k in range(20001):
    log10s = -10 + 20*mp.mpf(k)/20000
    s = mp.power(10, log10s)
    ratio = ((s*s+1)**mp.mpf('1.5') - s**3 - 1) / (s**mp.mpf('1.5'))
    if ratio > max_ratio:
        max_ratio = ratio
        argmax = s
assert max_ratio <= h2 + mp.mpf('1e-20')
print("pair_ratio_grid_max=", mp.nstr(max_ratio, 25))
print("pair_ratio_grid_argmax=", mp.nstr(argmax, 20))

# Spectral gap check for a_n=sqrt(1+n^2): convexity implies adjacent
# gaps are increasing, hence minimum gap is a_1-a_0=sqrt(2)-1.
g_prev = None
for n in range(0,501):
    an = mp.sqrt(1+n*n)
    an1 = mp.sqrt(1+(n+1)*(n+1))
    g = an1-an
    assert g >= mp.sqrt(2)-1
    if g_prev is not None:
        assert g >= g_prev
    g_prev = g
print("spectral_gap_first_501=PASS")

# Finite Schur/Hilbert-kernel check:
# sum_{n<m} x_n x_m/(m-n)^2 <= (pi^2/6) sum_n x_n^2.
for N in (8, 32, 128):
    xs = [mp.mpf(1)/(n+1) for n in range(N)]
    lhs = mp.mpf('0')
    for n in range(N):
        for m in range(n+1,N):
            lhs += xs[n]*xs[m]/((m-n)**2)
    rhs = (mp.pi**2/6)*sum(x*x for x in xs)
    assert lhs <= rhs
    print(f"schur_ratio_N{N}=", mp.nstr(lhs/rhs, 20))

# Sample exact overlap decay on torus shells n=0,1.
a0 = 1.0
a1 = sqrt(2.0)
kap01 = 9.0/8.0*(a1-a0)**2
for tt in (0.25, 1.0, 4.0):
    overlap = exp(-kap01*tt)
    assert 0.0 < overlap <= 1.0
    print(f"overlap_01_t{tt:g}={overlap:.15f}")

print("CHECK_PASS")
