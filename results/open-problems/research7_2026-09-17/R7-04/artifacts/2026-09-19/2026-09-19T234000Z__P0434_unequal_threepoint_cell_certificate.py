from sympy import symbols, Rational, factor, expand, simplify, diff, Poly
from math import comb

# Exact symbolic certificate for the P0434 three-point one-hill/two-demotion cell.
p, r, d, lam = symbols('p r d lam', positive=True)
q = 1-p-r
mu = 2-p
m = mu + r*d
h = mu/(1-r)
V = 4-3*p
EX2 = p + 4*q + r*(d+2)**2
alpha = 1-lam
beta = 1-lam*mu
rho = lam*m
W_inf = lam*EX2/(2*(1-rho)*beta)
W_h = lam*(V+r*h**2)/(2*beta)

# M-SERPT conditional means in the strict two-demotion cell.
TM1 = 1 + lam/(2*alpha)
TM2 = 2/alpha + lam*V/(2*alpha*beta)
TMc = W_inf + (d+2)/beta

# Gittins conditional means in the one-terminal-hill cell.
TG1 = 1 + W_h
TG2 = 2 + W_h
TGc = W_inf + (d+2-h)/beta + h

EM = simplify(p*TM1 + q*TM2 + r*TMc)
EG = simplify(p*TG1 + q*TG2 + r*TGc)
D = factor(EM-EG)
F = factor(2*EG-EM)

assert simplify(diff(D,d)) == 0
print('TAIL_LOCATION_CANCELLATION: PASS')
print('D =', D)

# Equal-probability specialization p=q=r=1/3 (equiv. d>4, c>6 in this cell).
Deq = factor(D.subs({p:Rational(1,3), r:Rational(1,3)}))
expected_Deq = lam*(37-39*lam)/(12*(1-lam)*(3-5*lam))
assert simplify(Deq-expected_Deq) == 0
print('EQUAL_PROBABILITY_GAP: PASS')
print('D_eq =', Deq)

# Boundary reduction for the full unequal-mass cell.
# Put t=1-p, r=u t^2, so 0<u<=1 is exactly r<=t^2.
# The topology threshold is d0=t^2/(pr)=1/(u p).
# For strict d>d0, m>1/p, hence stability gives lam<p. Set lam=x p, 0<x<1.
t,u,x = symbols('t u x', positive=True)
subs_boundary = {
    p: 1-t,
    r: u*t**2,
    d: 1/(u*(1-t)),
    lam: x*(1-t),
}
F0 = factor(F.subs(subs_boundary))
num0, den0 = F0.as_numer_denom()
Q = Poly(expand(-num0), t,u,x)

expected_den = 2*(1-t)*(1-x)*(1-u*t**2)*(1-x*(1-t))*(1-x*(1-t**2))
assert simplify(F0 - Q.as_expr()/expected_den) == 0
print('BOUNDARY_REDUCTION_IDENTITY: PASS')
print('Q_DEGREES =', Q.degree_list())
print('Q_POWER_TERMS =', len(Q.terms()))

# Tensor Bernstein coefficients on [0,1]^3 at the exact polynomial degrees.
degrees = Q.degree_list()
power = {mon: Rational(coef) for mon,coef in Q.terms()}

def bernstein_coeff(k):
    total = Rational(0)
    for mon,a in power.items():
        if all(mon[j] <= k[j] for j in range(3)):
            fac = Rational(1)
            for i,kk,n in zip(mon,k,degrees):
                fac *= Rational(comb(kk,i), comb(n,i))
            total += a*fac
    return factor(total)

coeffs=[]
for kt in range(degrees[0]+1):
    for ku in range(degrees[1]+1):
        for kx in range(degrees[2]+1):
            k=(kt,ku,kx)
            coeffs.append((k,bernstein_coeff(k)))

neg=[z for z in coeffs if z[1] < 0]
zero=[z for z in coeffs if z[1] == 0]
pos=[z for z in coeffs if z[1] > 0]
assert not neg
assert len(coeffs)==108
assert len(zero)==18
assert len(pos)==90
assert any(k[1]==2 and b>0 for k,b in pos)  # strict positivity also on u=1 face for interior t,x.
print('BERNSTEIN_CERTIFICATE: PASS')
print('BERNSTEIN_TOTAL =',len(coeffs))
print('BERNSTEIN_POSITIVE =',len(pos))
print('BERNSTEIN_ZERO =',len(zero))
print('BERNSTEIN_NEGATIVE =',len(neg))
print('MIN_POSITIVE =',min(b for _,b in pos))
print('FULL_BERNSTEIN_TABLE_BEGIN')
for k,b in coeffs:
    print(k, b)
print('FULL_BERNSTEIN_TABLE_END')
print('ALL_EXACT_CHECKS_PASS')
