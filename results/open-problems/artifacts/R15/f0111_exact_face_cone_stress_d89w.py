from fractions import Fraction as F


def pt(x):
    return (F(x), F(x))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[1], -a[0])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    v = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return (min(v), max(v))


def smul(c, a):
    return mul((F(c), F(c)), a)


def div(a, b):
    assert b[0] > 0
    return mul(a, (1/b[1], 1/b[0]))


def sq(a):
    if a[0] >= 0:
        return (a[0]**2, a[1]**2)
    if a[1] <= 0:
        return (a[1]**2, a[0]**2)
    return (F(0), max(a[0]**2, a[1]**2))


def log_interval_ratio(num, den, N=24):
    """Exact rational enclosure using log q = 2 atanh((q-1)/(q+1))."""
    q = F(num, den)
    assert q > 0
    if q < 1:
        lo, hi = log_interval_ratio(den, num, N)
        return (-hi, -lo)
    y = (q - 1)/(q + 1)
    s = F(0)
    for m in range(N):
        s += y**(2*m+1)/F(2*m+1)
    lo = 2*s
    tail = 2*y**(2*N+1)/(F(2*N+1)*(1-y*y))
    return (lo, lo + tail)


# A rational point on the z<-1 cubic-null branch, with active block sizes 2 and 9.
delta = F(1, 50)
z = F(-25, 9)
a = 1 + delta
b = 1 - delta
p = delta + z

x = (delta+z)*(1+z)*(1+delta+2*z)/(2*(1+delta)*(delta+3*z))
y = (delta+z)*(1-z)*(1-delta-2*z)/(2*(1-delta)*(delta+3*z))
k = 2*z*(1-z*z)/((1-delta*delta)*(delta+3*z))
assert x == F(1191944, 909063)
assert y == F(62046277, 14848029)
assert k == F(-200000000, 44544087)
assert x + y + k == 1

# No rest coordinates: C=-(n-1)=-10, so S=-10/k.
S = -F(10)/k
assert S == F(44544087, 20000000)
eu = x*S/F(2)
ev = y*S/F(9)
assert eu == F(7300657, 5000000)
assert ev == F(62046277, 60000000)
assert eu > 1 and ev > 1

# Exact cubic-null construction and strict quartic sign.
Q = (delta+z)*(1-z*z)/(delta+3*z)
N4 = delta*delta*z + 3*delta*z*z + delta + 3*z**3
R4 = -2*(delta+z)*(1-z*z)*N4/(delta+3*z)**2
assert R4 > 0

# Exact logarithm intervals for u, v, log S.
u = log_interval_ratio(eu.numerator, eu.denominator)
v = log_interval_ratio(ev.numerator, ev.denominator)
logS = log_interval_ratio(S.numerator, S.denominator)

# Value contact plus Hessian-null aggregate equations uniquely determine U,V,W.
# Omega = sum_{edges} B_ij q_i q_j = log S - u*x - v*y.
Omega = sub(sub(logS, smul(x, u)), smul(y, v))
termJ = div(smul(x*(p-a), sq(u)), pt(2*a))
termK = div(smul(y*(p+b), sq(v)), pt(2*b))
const = sub(termJ, termK)
Luv = add(smul(b, u), smul(a, v))
W = div(smul(2*a*b, sub(Omega, const)), sq(Luv))
U = div(add(smul(b, W), pt(x*(p-a))), pt(2*a))
V = div(sub(smul(a, W), pt(y*(p+b))), pt(2*b))

# Aggregate singleton sums from exact gradient contact.
AJ = sub(sub(pt(2-x), smul(2, mul(u, U))), mul(v, W))
AK = sub(sub(pt(9-y), smul(2, mul(v, V))), mul(u, W))

assert U[0] > 0 and V[0] > 0 and W[0] > 0
assert AJ[0] > 0 and AK[0] > 0
assert F(543,1000) < U[0] < U[1] < F(545,1000)
assert F(7009,1000) < V[0] < V[1] < F(7010,1000)
assert F(6185,1000) < W[0] < W[1] < F(6187,1000)
assert F(69,1000) < AJ[0] < AJ[1] < F(71,1000)
assert F(2009,1000) < AK[0] < AK[1] < F(2011,1000)

# Block-symmetric coefficients.
alphaJ = smul(F(1,2), AJ)
alphaK = smul(F(1,9), AK)
betaJJ = U
betaKK = smul(F(1,36), V)
betaJK = smul(F(1,18), W)
rJ = x/F(2)
rK = y/F(9)

# Full contact Hessian PSD: two transverse eigenvalues and the nonzero quotient eigenvalue.
lambdaJ = sub(pt(rJ), betaJJ)
lambdaK = sub(pt(rK), betaKK)
traceQ = add(
    sub(add(pt(rJ), betaJJ), pt(2*rJ*rJ)),
    sub(add(pt(rK), smul(8, betaKK)), pt(9*rK*rK)),
)
assert lambdaJ[0] > F(111,1000)
assert lambdaK[0] > F(269,1000)
assert traceQ[0] > F(420,1000)
# The other quotient eigenvalue is exactly zero because U,V were defined by
# 2aU-bW=x(p-a), aW-2bV=y(p+b), i.e. H_gap h=0.

# The previous rational all-subset face hierarchy is satisfied strictly for EVERY
# subset type s from the J block and t from the K block.
# Barrier: A >= d (sqrt(N)-sqrt(B))_+^2, d=3/(2m-1).
# For B<N and R=N+B-A/d>0, this is certified without square roots by
# 4*N*B >= R^2.  We use lower B / upper R, so every comparison is rigorous.
min_sq_metric = None
min_type = None
for sj in range(3):
    for tk in range(10):
        m = sj + tk
        if m < 2:
            continue
        Nedge = F(m*(m-1), 2)
        d = F(3, 2*m-1)
        Asub = add(smul(sj, alphaJ), smul(tk, alphaK))
        Bsub = add(
            add(smul(F(sj*(sj-1),2), betaJJ), smul(F(tk*(tk-1),2), betaKK)),
            smul(sj*tk, betaJK),
        )
        assert Bsub[0] >= 0
        if Bsub[0] >= Nedge:
            metric = F(1)
        else:
            Rhi = Nedge + Bsub[1] - Asub[0]/d
            if Rhi <= 0:
                metric = F(1)
            else:
                metric = 4*Nedge*Bsub[0] - Rhi*Rhi
                assert metric > 0
        if min_sq_metric is None or metric < min_sq_metric:
            min_sq_metric = metric
            min_type = (sj, tk)
assert min_sq_metric > F(1,500)
assert min_type == (2,0)

# The exact face cone is stronger.  On the K-only 9-face take s=log(4/3).
# Then 9*exp(s)-8=4 exactly, so f_9(s)=9s-log 4.
s = log_interval_ratio(4, 3)
log4 = smul(2, log_interval_ratio(2, 1))
f9 = sub(smul(9, s), log4)
PK = add(mul(AK, s), mul(V, sq(s)))
gap = sub(PK, f9)
assert gap[0] > F(-9,200)      # > -0.045
assert gap[1] < F(-11,250)     # < -0.044

print("ALL_EXACT_CHECKS_PASS")
print("branch: delta=1/50, z=-25/9, blocks=(2,9), no rest")
print("x=1191944/909063; y=62046277/14848029; k=-200000000/44544087")
print("S=44544087/20000000; exp(u)=7300657/5000000; exp(v)=62046277/60000000")
print("strict quartic factor R4>0")
print("positive exact-contact coefficients and full local Hessian PSD certified")
print("all previous rational subset-face barriers pass; minimum squared certificate > 1/500 at subset type (2,0)")
print("exact K-only 9-face fails at s=log(4/3): -0.045 < P_K(s)-f_9(s) < -0.044")
