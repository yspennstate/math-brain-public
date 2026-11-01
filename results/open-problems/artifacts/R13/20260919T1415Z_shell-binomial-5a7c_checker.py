from fractions import Fraction as F
from math import factorial, comb

# R13 exact checker: shellwise recovery of omitted positive binomial mass
# in the p=33/20, D=139 cosine-power / inverse-gamma DTV certificate.
# Every acceptance test is an exact rational inequality.

D = 139
q = 40
beta = F(13,40)
a_num = 53
cold = F(78472,100000)
cnew = F(78476,100000)
dc = cnew-cold
dm = F(8839437,10**7)  # D^(-1/40) > dm
sqrtpi_inv2 = F(500000,1772454) # 1/(2sqrt(pi)) > this
Uold = F(43,40)
U1 = F(41,40)
U2 = F(537,500)  # 1.074
Told = Uold**q
Smax = Told/D

# Imported certified predecessor floor: the first six positive binomial
# layers based on Z_old, integrated with W_61 on [0,Uold^40].
delta0 = F(53745767,10**9)
base_up = F(7694998,10**6)
old_h = F(728141,100000)
new_h = F(728139,100000)

# Prove c_* > cnew exactly by the predecessor Gautschi product at N=10000.
N = 10000
P = F(1)
for k in range(N):
    P *= F(40*k+13,40*k+27)
c40_lower = beta**(-27) * P**40 * (F(N)-beta)**14 / (1+beta)**40
assert c40_lower > cnew**40
assert dm**40 * D < 1

# Sparse polynomial helpers in u, t=u^40.
def padd(a,b):
    out = dict(a)
    for k,v in b.items():
        out[k] = out.get(k,F(0))+v
        if out[k] == 0:
            out.pop(k,None)
    return out

def pmul(a,b):
    out = {}
    for i,x in a.items():
        if not x: continue
        for j,y in b.items():
            if y:
                out[i+j] = out.get(i+j,F(0))+x*y
    return {k:v for k,v in out.items() if v}

# Reconstruct the predecessor lower polynomial Z_old for
# G(s)=e^s L(s) >= 1+Z_old(u) on 0<=u<=Uold.
A = {0:F(1)}
term = F(1)
for k in range(1,6):
    term *= beta / ((F(k-1)-beta)*k)
    assert term < 0
    A[q*k] = term / D**k
term6 = term * beta / ((F(5)-beta)*6)
r = beta*Smax / ((F(6)-beta)*7)
assert 0 < r < 1
A[q*6] = -abs(term6)/(1-r)/D**6

NB = {}
nb = F(1)
for k in range(5):
    if k>0:
        nb *= beta / ((F(a_num,q)+k)*k)
    deg = a_num + q*k
    NB[deg] = cold*nb*dm**deg
Llo = padd(A,NB)

E8 = {}
fac=1
for j in range(9):
    if j>1:
        fac *= j
    E8[q*j] = F(1,D**j*fac)
Z = pmul(E8,Llo)
Z[0] = Z.get(0,F(0))-1
if Z.get(0)==0:
    Z.pop(0,None)
assert min(Z) == a_num

# Global positivity check retained from predecessor.
z_global = Z[a_num]
for deg,c in Z.items():
    if deg>a_num and c<0:
        z_global += c*Uold**(deg-a_num)
assert z_global > 0

# W_61(t) is the odd Taylor polynomial for exp(-t), hence W_61<=exp(-t)
# globally. W_60 is the even Taylor upper bound and is >0, so W_61 is
# decreasing. Exact endpoint positivity therefore makes W_61 nonnegative
# throughout [0,U2^40].
def W_at(t,N=61):
    return sum(F((-1)**j, factorial(j))*t**j for j in range(N+1))
assert W_at(U2**q,61) > 0

# Exact integral of W_N(u^40) * u^power over a rational shell.
def intW(power, lo, hi, N=61):
    s=F(0)
    for j in range(N+1):
        den = power + 40*j + 1
        s += F((-1)**j, factorial(j)) * (hi**den-lo**den) / den
    return s

# Reconstruct the exact localized linear increment already certified in the
# predecessor report: D*w >= dc*dm^13*u^53 on [0,U1].
J1 = 40*intW(32,F(0),U1,9)
assert J1 > 0
inc_prev = dc*dm**13*J1*sqrtpi_inv2
assert inc_prev > 0

delta_prev = delta0 + inc_prev

# New route: extend the linear term to U2, and recover positive binomial mass
# that all earlier certificates deliberately discarded.
lin_tail = dc*dm**13 * 40*intW(32,U1,U2,61)*sqrtpi_inv2
assert lin_tail > 0

# Shells. On [l,r], Q(u)=Z(u)/u^53 has the exact lower bound obtained by
# evaluating positive powers at l and negative powers at r.
bounds = [F(0),F(1)] + [F(k,100) for k in range(101,108)] + [U2]
shells = list(zip(bounds[:-1],bounds[1:]))
assert shells[0] == (F(0),F(1)) and shells[-1][1] == U2

def shell_margin(lo,hi):
    m=F(0)
    for deg,c in Z.items():
        p=deg-a_num
        if p==0:
            m += c
        elif c>0:
            m += c*lo**p
        else:
            m += c*hi**p
    return m

margins=[shell_margin(lo,hi) for lo,hi in shells]
assert all(m>0 for m in margins)

# Old base (1+Z)^D: predecessor counted k=1,...,6. Recover k=7,...,12
# on [0,U2] shellwise.
old_extra=F(0)
for k in range(7,13):
    for (lo,hi),m in zip(shells,margins):
        J = intW(53*k-21,lo,hi,61)
        assert J > 0
        old_extra += 40*F(comb(D,k))*m**k*J*sqrtpi_inv2
assert old_extra > 0

# Coefficient improvement: write G >= 1+Z+w. The predecessor added only
# the r=0 part of D*w on [0,U1]. We already extended r=0 to [U1,U2].
# Now recover r=1,...,7 from D*w*(1+Z)^(D-1) on [0,U2].
# Since D*w >= dc*dm^13*u^53, these are exact lower terms.
cross_extra=F(0)
for rpow in range(1,8):
    for (lo,hi),m in zip(shells,margins):
        J = intW(53*(rpow+1)-21,lo,hi,61)
        assert J > 0
        cross_extra += (
            40*F(comb(D-1,rpow))*dc*dm**13*m**rpow*J*sqrtpi_inv2
        )
assert cross_extra > 0

extra = lin_tail + old_extra + cross_extra
delta_new = delta_prev + extra
C_upper = base_up*(1-delta_new)

# Existing exact prefactor majorant remains valid via pi<355/113.
assert base_up**2 > F(9801,520)*F(355,113)
assert C_upper < new_h
assert old_h-new_h == F(2,100000)

# Active-row pruning at n=86: at most 139 active rows.
row_ratio = F(86**2,1)/(new_h*new_h)
assert F(139) < row_ratio < F(140)

print('R13_SHELL_BINOMIAL_RECOVERY_EXACT_PASS')
print('gautschi_relative_margin =', float(c40_lower/cnew**40-1))
print('W61_endpoint =', float(W_at(U2**q,61)))
print('global_Z_factor_margin =', float(z_global))
print('shell_count =', len(shells))
print('shell_margins =', [float(m) for m in margins])
print('delta0 =', float(delta0))
print('inc_prev =', float(inc_prev))
print('delta_prev =', float(delta_prev))
print('lin_tail =', float(lin_tail))
print('old_extra_k7_k12 =', float(old_extra))
print('cross_extra_r1_r7 =', float(cross_extra))
print('new_extra_total =', float(extra))
print('delta_new =', float(delta_new))
print('C_upper =', float(C_upper))
print('old_h =', float(old_h))
print('new_h =', float(new_h))
print('improvement =', float(old_h-new_h))
print('row_ratio =', float(row_ratio))