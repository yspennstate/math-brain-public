from fractions import Fraction
from math import comb
import sympy as sp

l,p,x,y = sp.symbols('l p x y')
L0 = sp.Rational(19,10)
L1 = sp.Rational(54,25)
P0 = sp.Rational(41,50)
P1 = sp.Rational(1)

u = (3-l)/3
d = 1 - l*(3-p)/6
r = sp.factor(d/u)

def binexp(n, f):
    return sp.factor(sum(sp.binomial(n,j)*r**j*(1-r)**(n-j)*f(j) for j in range(n+1)))

K1 = binexp(1, lambda j: l/(l+j*u)**2)
K2 = binexp(2, lambda j: l/(l+j*u)**2)
rho = sp.factor((1-p)*2*K1 + p*3*K2)

A2 = 2*u/(l+2*u)**2
A3 = 3*u/(l+3*u)**2
A = sp.factor((1-p)*A2+p*A3)
eta = sp.factor(A/(1-rho))

a = l-1
Kc = binexp(2, lambda j: a/(a+j*u)**2)
D = sp.factor(1/a + 2*eta*Kc/d - 3/(9-l))

theta0 = sp.factor(3*p/(4-p))
g0 = sp.factor(theta0*(1-theta0)/(2+theta0))
Prod = sp.factor(l*g0*D)

def bernstein_coeffs_2d(poly_expr):
    poly = sp.Poly(sp.expand(poly_expr), x, y, domain=sp.QQ)
    nx,ny = poly.degree(x),poly.degree(y)
    coeff = {(i,j):sp.Rational(0) for i in range(nx+1) for j in range(ny+1)}
    for (i,j),c in poly.terms():
        coeff[(i,j)] = c
    B = {}
    for I in range(nx+1):
        for J in range(ny+1):
            s = sp.Rational(0)
            for i in range(I+1):
                for j in range(J+1):
                    c = coeff.get((i,j),0)
                    if c:
                        s += c*sp.Rational(comb(I,i),comb(nx,i))*sp.Rational(comb(J,j),comb(ny,j))
            B[(I,J)] = sp.factor(s)
    return nx,ny,B

def bern_cert(poly_lp, name):
    sub = sp.expand(poly_lp.subs({
        l: L0+(L1-L0)*x,
        p: P0+(P1-P0)*y
    }))
    nx,ny,B = bernstein_coeffs_2d(sub)
    vals = list(B.values())
    mn = min(vals, key=lambda z: float(z))
    assert all(bool(v>=0) for v in vals), (name, 'negative Bernstein coefficient', mn)
    print(f'{name}: PASS degree=({nx},{ny}) coeffs={len(vals)} min_coeff={mn}')

# Basic rectangle / inverse-moment constants.
dmin = sp.factor(d.subs({l:L1,p:P0}))
umin = sp.factor(u.subs(l,L1))
rmin = sp.factor(r.subs({l:L1,p:P0}))
assert dmin == sp.Rational(269,1250)
assert umin == sp.Rational(7,25)
assert rmin == sp.Rational(269,350)
assert sp.factor(r.subs(p,1)-1) == 0
print('d_min =', dmin, 'u_min =', umin, 'r_min =', rmin, 'r(p=1)=', sp.factor(r.subs(p,1)))

# Exact contraction certificate rho <= 19/20.
R = sp.together(sp.Rational(19,20)-rho)
Rn,Rd = R.as_numer_denom()
bern_cert(Rn, 'rho_gap_numerator')
bern_cert(Rd, 'rho_gap_denominator')
rho_corner = sp.factor(rho.subs({l:L1,p:P0}))
assert rho_corner < sp.Rational(19,20)
print('rho_corner =', rho_corner, '=', float(rho_corner))

# g is decreasing on the admissible theta interval.
theta_corner = sp.factor(theta0.subs(p,P0))
gprime_num_corner = sp.factor(2-4*theta_corner-theta_corner**2)
assert gprime_num_corner < 0
print('theta_min =', theta_corner, 'gprime_numerator(theta_min) =', gprime_num_corner)

# Main product certificate Prod <= 999/1000. SymPy's canonical denominator
# carries a negative factor (rho-1), so certify -numerator and -denominator.
Q = sp.together(sp.Rational(999,1000)-Prod)
Qn,Qd = Q.as_numer_denom()
bern_cert(-Qn, 'product_gap_neg_numerator')
bern_cert(-Qd, 'product_gap_neg_denominator')
prod_corner = sp.factor(Prod.subs({l:L1,p:P0}))
assert prod_corner < sp.Rational(999,1000)
print('product_corner =', prod_corner, '=', float(prod_corner))
print('product_gap_corner =', sp.factor(sp.Rational(999,1000)-prod_corner))

# Uniform derivative margin from exact speed identity.
margin = sp.factor(sp.Rational(4,1000)/(3+L1)**2)
assert margin == sp.Rational(5,33282)
print('certified_speed_derivative_margin =', margin, '=', float(margin))

# Quantify the weaker direct q-contraction route at the hard corner.
lv,pv = L1,P0
uv = sp.factor(u.subs(l,lv))
rv = sp.factor(r.subs({l:lv,p:pv}))
def qK_u(k):
    return sp.factor(sum(
        sp.binomial(k-1,j)*rv**j*(1-rv)**(k-1-j)
        * lv/((j+1)*(lv+(j+1)*uv))
        for j in range(k)
    ))
qK2 = qK_u(2)
qK3 = qK_u(3)
rho_q = sp.factor((1-pv)*2*qK2 + pv*3*qK3)
Mq = sp.factor((1/lv)/(1-rho_q))
eta_q = sp.factor(uv*Mq)
Kcv = sp.factor(Kc.subs({l:lv,p:pv}))
dv = sp.factor(d.subs({l:lv,p:pv}))
Dq = sp.factor(1/(lv-1) + 2*eta_q*Kcv/dv - 3/(9-lv))
Pq = sp.factor(lv*g0.subs(p,pv)*Dq)
assert rho_q < 1
assert Pq > 1
print('direct_q_corner_rho =', rho_q, '=', float(rho_q))
print('direct_q_corner_Mq_bound =', Mq, '=', float(Mq))
print('direct_q_corner_speed_product_bound =', Pq, '=', float(Pq), '> 1 (insufficient)')

print('ALL_EXACT_CHECKS_PASS')
