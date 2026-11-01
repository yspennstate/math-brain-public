from fractions import Fraction as F


def log_interval_ratio(num, den, N=24):
    q = F(num, den)
    assert q > 1
    y = (q - 1) / (q + 1)
    s = F(0)
    for m in range(N):
        s += y**(2*m+1) / F(2*m+1)
    lo = 2*s
    tail = 2*y**(2*N+1) / (F(2*N+1) * (1-y*y))
    return lo, lo + tail


def sq_pos(I):
    assert I[0] >= 0
    return I[0]*I[0], I[1]*I[1]


def add(I, J):
    return I[0] + J[0], I[1] + J[1]


def smul(c, I):
    if c >= 0:
        return c*I[0], c*I[1]
    return c*I[1], c*I[0]


def within(I, lo, hi):
    assert I[0] > F(lo[0], lo[1])
    assert I[1] < F(hi[0], hi[1])


# Rational scalar point on the surviving unequal-amplitude z>1 cubic-null branch.
delta = F(4, 5)
z = F(31, 20)
a = 1 + delta
b = 1 - delta
p = delta + z

x = (delta+z)*(1+z)*(1+delta+2*z) / (2*(1+delta)*(delta+3*z))
y = (delta+z)*(1-z)*(1-delta-2*z) / (2*(1-delta)*(delta+3*z))
k = 2*z*(1-z*z) / ((1-delta*delta)*(delta+3*z))
assert x == F(39151, 26160)
assert y == F(14993, 8720)
assert k == F(-5797, 2616)
assert x+y+k == 1
S = -F(3) / k
assert S == F(7848, 5797)
eu = x*S/2
ev = y*S/2
assert eu == F(6909, 6820)
assert ev == F(12267, 10540)
assert eu > 1 and ev > 1

rj = x/2
rk = y/2
assert rj == F(39151, 52320)
assert rk == F(14993, 17440)

# Carried exact cubic-null and quartic factors.
Q = (delta+z)*(1-z*z)/(delta+3*z)
N = delta*delta*z + 3*delta*z*z + delta + 3*z**3
R = -2*(delta+z)*(1-z*z)*N/(delta+3*z)**2
assert Q == F(-26367, 43600)
assert R == F(3950752179, 950480000)
assert R > 0

# Exact log intervals by the positive atanh series.
U = log_interval_ratio(6909, 6820)
V = log_interval_ratio(12267, 10540)
L = log_interval_ratio(7848, 5797)
within(U, (12965, 10**6), (12966, 10**6))
within(V, (151735, 10**6), (151736, 10**6))
within(L, (302918, 10**6), (302919, 10**6))

# Block-symmetric exact-contact/null family.
cjj = F(430661, 1883520)
sjj = F(2, 9)
ckk = F(-764643, 69760)
skk = F(18)

# T is defined by exact value contact.
U2 = sq_pos(U)
V2 = sq_pos(V)
Nlo = F(1883520)*L[0] - F(430661)*U2[1] - F(2818872)*U[1] + F(20645361)*V2[0] - F(3238488)*V[1]
Nhi = F(1883520)*L[1] - F(430661)*U2[0] - F(2818872)*U[0] + F(20645361)*V2[1] - F(3238488)*V[0]
UV9 = add(U, smul(F(9), V))
Den = smul(F(418560), sq_pos(UV9))
assert Nlo > 0 and Den[0] > 0
T = (Nlo/Den[1], Nhi/Den[0])
within(T, (651, 1000), (652, 1000))

bjj = (cjj+sjj*T[0], cjj+sjj*T[1])
bkk = (ckk+skk*T[0], ckk+skk*T[1])
within(bjj, (373, 1000), (374, 1000))
within(bkk, (757, 1000), (758, 1000))

aj = (F(1)-rj-bjj[1]*U[1]-2*T[1]*V[1],
      F(1)-rj-bjj[0]*U[0]-2*T[0]*V[0])
ak = (F(1)-rk-bkk[1]*V[1]-2*T[1]*U[1],
      F(1)-rk-bkk[0]*V[0]-2*T[0]*U[0])
within(aj, (49, 1000), (50, 1000))
within(ak, (8, 1000), (9, 1000))

# Null-row identities hold identically in T.
assert (rj+cjj-2*rj*rj)*a + 2*b*rj*rk == 0
assert sjj*a - 2*b == 0
assert -2*a*rj*rk - b*(rk+ckk-2*rk*rk) == 0
assert 2*a - b*skk == 0

# Full contact Hessian PSD. Antisymmetric eigenvalues are rj-bjj and rk-bkk.
# The block-constant 2x2 matrix has h as a nonzero null vector, so its other
# eigenvalue is its trace.
lamj = (rj-bjj[1], rj-bjj[0])
lamk = (rk-bkk[1], rk-bkk[0])
trace = (rj+bjj[0]-2*rj*rj + rk+bkk[0]-2*rk*rk,
         rj+bjj[1]-2*rj*rj + rk+bkk[1]-2*rk*rk)
within(lamj, (374, 1000), (376, 1000))
within(lamk, (102, 1000), (103, 1000))
within(trace, (140, 1000), (142, 1000))

# Global two-coordinate face obstruction on the J pair.
# A global majorant + PSD would require 2 alpha_J >= (1-sqrt(beta_JJ))^2.
# With w=1+beta-2alpha>0 this is equivalent to w^2-4 beta <= 0.
wJ = (F(1)+bjj[0]-2*aj[1], F(1)+bjj[1]-2*aj[0])
assert wJ[0] > 0 and bjj[0] > 0 and bjj[1] < 1
DJ = (wJ[0]*wJ[0]-4*bjj[1], wJ[1]*wJ[1]-4*bjj[0])
within(DJ, (131, 1000), (133, 1000))
assert DJ[0] > 0

print("ALL_EXACT_CHECKS_PASS")
print("delta=4/5; z=31/20; branch=z>1")
print("x=39151/26160; y=14993/8720; k=-5797/2616; S=7848/5797")
print("exp(u)=6909/6820; exp(v)=12267/10540")
print("cubic_null_Q=-26367/43600; quartic_R=3950752179/950480000>0")
print("certified coefficient intervals:")
print("  0.651<T<0.652; 0.373<beta_JJ<0.374; 0.757<beta_KK<0.758")
print("  0.049<alpha_J<0.050; 0.008<alpha_K<0.009")
print("certified Hessian PSD margins:")
print("  0.374<lambda_J<0.376; 0.102<lambda_K<0.103; 0.140<trace_block<0.142")
print("certified global-face contradiction:")
print("  D_J=(1+beta_JJ-2alpha_J)^2-4 beta_JJ satisfies 0.131<D_J<0.133")
