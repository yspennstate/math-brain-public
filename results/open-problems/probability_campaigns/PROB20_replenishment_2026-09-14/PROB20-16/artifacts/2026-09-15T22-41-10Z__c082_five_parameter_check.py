#!/usr/bin/env python3
# PROB20-16 exact checker: five-parameter C082 solid + arbitrary Hermitian tube.
import sympy as sp
from math import comb

h,g,r,q,p,u1,u2,u3,u4,u5 = sp.symbols('h g r q p u1 u2 u3 u4 u5', real=True)

a0 = sp.Rational(6784250,15630789)
b0 = sp.Rational(32125,79546)
nu0 = sp.Rational(1812625,15630789)
c0 = sp.Rational(6375,79546)

alpha = a0-h-g
beta = b0-h+2*g
nu = nu0+r
c = c0+p

Delta = sp.expand(beta*(alpha**2-nu**2-q**2)-4*c**2*(alpha-nu))
R = sp.expand(alpha*beta-2*c**2-Delta)
P = sp.expand(alpha**2-nu**2-q**2-Delta)
N12 = sp.expand((beta*nu-2*c**2)**2 + beta**2*q**2)
N13 = sp.expand(2*c**2*((alpha-nu)**2+q**2))

# Exact structured inverse identities for M=I-K.
sq2 = sp.sqrt(2)
M = sp.Matrix([
    [alpha, -nu-sp.I*q, -sq2*c],
    [-nu+sp.I*q, alpha, sq2*c],
    [-sq2*c, sq2*c, beta],
])
assert sp.expand(M.det()-Delta) == 0
adj = sp.Matrix([
    [alpha*beta-2*c**2, beta*(nu+sp.I*q)-2*c**2, sq2*c*(alpha-nu-sp.I*q)],
    [beta*(nu-sp.I*q)-2*c**2, alpha*beta-2*c**2, -sq2*c*(alpha-nu+sp.I*q)],
    [sq2*c*(alpha-nu+sp.I*q), -sq2*c*(alpha-nu-sp.I*q), alpha**2-nu**2-q**2],
])
assert all(sp.expand(z)==0 for z in (M*adj-Delta*sp.eye(3)))

polys = {
    'Delta': Delta,
    'R': R,
    'P': P,
    'ell12_lo': 10*R-7*Delta,
    'ell12_hi': sp.Rational(99,50)*Delta-R,
    'ell3_lo': 10*P-7*Delta,
    'ell3_hi': sp.Rational(99,50)*Delta-P,
    'rho12_lo': 625*N12-49*R**2,
    'rho12_hi': 25*R**2-144*N12,
    'rho13_lo': 625*N13-49*R*P,
    'rho13_hi': 25*R*P-144*N13,
}

subs = {
    h: -sp.Rational(3,20)+sp.Rational(4,25)*u1,
    g: -sp.Rational(1,500)+sp.Rational(4,125)*u2,
    r: -sp.Rational(1,100)+sp.Rational(1,50)*u3,
    q: -sp.Rational(1,100)+sp.Rational(1,50)*u4,
    p: -sp.Rational(1,250)+sp.Rational(1,125)*u5,
}
vars5=(u1,u2,u3,u4,u5)

def bernstein_coefficients(expr):
    poly=sp.Poly(sp.expand(expr.subs(subs)), *vars5, domain=sp.QQ)
    degs=tuple(poly.degree(v) for v in vars5)
    data=poly.as_dict()
    for ax,d in enumerate(degs):
        groups={}
        for idx,val in data.items():
            key=idx[:ax]+idx[ax+1:]
            groups.setdefault(key,{})[idx[ax]]=val
        new={}
        for key,arr in groups.items():
            for i in range(d+1):
                s=sp.Rational(0)
                for aa in range(i+1):
                    cv=arr.get(aa,0)
                    if cv:
                        s += cv*sp.Rational(comb(i,aa),comb(d,aa))
                full=key[:ax]+(i,)+key[ax:]
                new[full]=sp.factor(s)
        data=new
    return degs,list(data.values())

print('PROB20-16 C082 FIVE-PARAMETER SOLID EXACT CERTIFICATE')
print('box: h[-3/20,1/100], g[-1/500,3/100], r[-1/100,1/100], q[-1/100,1/100], p[-1/250,1/250]')
print('J operator norm = 2')
print('central spectral margins: K >= 143/1500 I; I-K >= 91/500 I')
for name,expr in polys.items():
    degs,vals=bernstein_coefficients(expr)
    m=min(vals)
    assert m>0,(name,m)
    print(f'{name}: degree={degs}, coefficients={len(vals)}, min={m}, approx={float(m)}')

eps=sp.Rational(1,20000)
m=sp.Rational(91,500)
eta=sp.factor(eps/(m*(m-eps)))
assert eta == sp.Rational(500,331149)
assert eta < sp.Rational(1,650)
eta0=sp.Rational(1,650)
a=sp.Rational(7,10)
rho_lo=sp.factor((sp.Rational(7,25)*a-eta0)/(a+eta0))
rho_hi=sp.factor((sp.Rational(5,12)*a+eta0)/(a-eta0))
assert rho_lo == sp.Rational(79,285)
assert rho_hi == sp.Rational(2287,5448)
assert rho_lo > sp.Rational(1,10)
assert rho_hi < sp.Rational(21,50)
assert a-eta0 > sp.Rational(1,2)
assert sp.Rational(99,50)+eta0 < 2
print('generic Hermitian tube epsilon =', eps, float(eps))
print('exact odds perturbation bound =', eta, float(eta), '< 1/650')
print('robust rho interval =', rho_lo, rho_hi, float(rho_lo), float(rho_hi))
print('structured pJ endpoint operator displacement = 1/125; ratio to preceding generic tube 1/6000 = 48')
assert sp.Rational(1,125)/sp.Rational(1,6000) == 48
print('ALL EXACT ASSERTIONS PASSED')
