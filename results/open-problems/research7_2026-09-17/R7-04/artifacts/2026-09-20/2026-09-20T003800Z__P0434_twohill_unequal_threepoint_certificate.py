from sympy import symbols, Rational, factor, expand, simplify, diff, Poly
from math import comb

# Exact symbolic certificate for P0434 neighboring unequal-mass
# three-point TWO-GITTINS-HILL / TWO-M-SERPT-DEMOTION cell.

p, r, d, lam = symbols('p r d lam', positive=True)
q = 1-p-r
t = 1-p
mu = 2-p
m = mu + r*d
h0 = 1/p
h1 = t/q
ell = q/(p*t)
V = 4-3*p
M2 = p + 4*q + r*(2+d)**2
alpha = 1-lam
beta = 1-lam*mu
rho = lam*m
W_inf = lam*M2/(2*(1-rho)*beta)

# M-SERPT in r>t^2, d>t/q: m<S1<d, hence two demotions.
TM1 = 1 + lam/(2*alpha)
TM2 = 2/alpha + lam*V/(2*alpha*beta)
TMc = W_inf + (2+d)/beta

# Gittins exact branches in this cell:
# [0,1): (1-a)/p, [1,2): t(2-a)/q, [2,2+d): 2+d-a.
# h0=1/p < h1=t/q < d.
# For rank h0, the first recycled stage-1 interval has length ell=q/(pt).
C0 = 1 + t*ell**2 + r*h0**2
WG0 = lam*C0/(2*alpha)
TG1 = 1 + WG0

WG1 = lam*(V + r*h1**2)/(2*beta*alpha)
TG2 = WG1 + (2-ell)/alpha + ell

TGc = W_inf + (2+d-h1)/beta + (h1-h0)/alpha + h0

EM = simplify(p*TM1 + q*TM2 + r*TMc)
EG = simplify(p*TG1 + q*TG2 + r*TGc)
D = factor(EM-EG)
F = factor(2*EG-EM)

# Structural cancellation and compact policy-gap formula.
D_simple = lam/(2*alpha)*((q**2+r*t)/(p*t) + r*t**2/(q*beta))
assert simplify(D-D_simple) == 0
assert simplify(diff(D,d)) == 0
print('TWO_HILL_TAIL_LOCATION_CANCELLATION: PASS')
print('D_COMPACT_IDENTITY: PASS')

# F'=EG' is manifestly positive for stable systems.
Fp_manifest = r*(lam/(2*beta)*(2*r*(2+d)/(1-rho)
                 + lam*r*M2/(1-rho)**2) + 1/beta)
assert simplify(diff(F,d)-Fp_manifest) == 0
print('TAIL_DISPLACEMENT_MONOTONICITY: PASS')

# Reduce d>t/q to one-sided contact d=t/q.
# Rectangularize r>t^2 by r=t^2+u*t*(1-t), so q=t(1-t)(1-u).
# At d=t/q put x=rho in (0,1).
T,U,X = symbols('T U X', positive=True)
ps = 1-T
rs = T**2 + U*T*(1-T)
qs = simplify(1-ps-rs)
h1s = simplify((1-ps)/qs)
m0s = simplify((2-ps)+rs*h1s)
lams = simplify(X/m0s)

F0 = factor(F.subs({p:ps, r:rs, d:h1s, lam:lams}))
num0, den0 = F0.as_numer_denom()
Q = Poly(expand(-num0), T,U,X)

K = 1-U*(1-T)
Apos = expand(K-X*(1-T)*(1-U))
Bpos = expand(K-X*(1-T)*(1-U)*(1+T))
expected_den_pos = 2*(1-T)*(1-U)*(1-X)*Apos*Bpos
assert simplify(F0 - Q.as_expr()/expected_den_pos) == 0
print('BOUNDARY_REDUCTION_IDENTITY: PASS')
print('Q_DEGREES =', Q.degree_list())
print('Q_POWER_TERMS =', len(Q.terms()))

# Exact tensor Bernstein certificate Q>=0 on [0,1]^3.
degrees = Q.degree_list()
power = {mon:Rational(coef) for mon,coef in Q.terms()}

def bernstein_coeff(k):
    total = Rational(0)
    for mon,a in power.items():
        if all(mon[j] <= k[j] for j in range(3)):
            fac = Rational(1)
            for i,kk,n in zip(mon,k,degrees):
                fac *= Rational(comb(kk,i), comb(n,i))
            total += a*fac
    return factor(total)

coeffs = []
for kt in range(degrees[0]+1):
    for ku in range(degrees[1]+1):
        for kx in range(degrees[2]+1):
            k=(kt,ku,kx)
            coeffs.append((k,bernstein_coeff(k)))

neg=[z for z in coeffs if z[1] < 0]
zero=[z for z in coeffs if z[1] == 0]
pos=[z for z in coeffs if z[1] > 0]
assert not neg
assert len(coeffs)==168
assert len(pos)==132
assert len(zero)==36
print('BERNSTEIN_CERTIFICATE: PASS')
print('BERNSTEIN_TOTAL =',len(coeffs))
print('BERNSTEIN_POSITIVE =',len(pos))
print('BERNSTEIN_ZERO =',len(zero))
print('BERNSTEIN_NEGATIVE =',len(neg))
print('MIN_POSITIVE =',min(b for _,b in pos))
print('ALL_EXACT_CHECKS_PASS')
