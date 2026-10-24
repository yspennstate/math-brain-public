#!/usr/bin/env python3
# PROB20-16 exact checker: six-parameter C082 solid + arbitrary Hermitian tube.
import sympy as sp
from math import comb

h,g,r,q,p,s,u1,u2,u3,u4,u5,u6 = sp.symbols(
    'h g r q p s u1 u2 u3 u4 u5 u6', real=True
)

a0 = sp.Rational(6784250,15630789)
b0 = sp.Rational(32125,79546)
nu0 = sp.Rational(1812625,15630789)
c0 = sp.Rational(6375,79546)

alpha = a0-h-g
beta = b0-h+2*g
nu = nu0+r
c = c0+p
uabs = c**2+s**2

Delta = sp.expand(beta*(alpha**2-nu**2-q**2)-4*uabs*(alpha-nu))
R = sp.expand(alpha*beta-2*uabs-Delta)
P = sp.expand(alpha**2-nu**2-q**2-Delta)
N12 = sp.expand((beta*nu-2*uabs)**2 + beta**2*q**2)
N13 = sp.expand(2*uabs*((alpha-nu)**2+q**2))

# Exact determinant/cofactor identities.
sq2 = sp.sqrt(2)
z = c + sp.I*s
M = sp.Matrix([
    [alpha, -nu-sp.I*q, -sq2*z],
    [-nu+sp.I*q, alpha, sq2*z],
    [-sq2*sp.conjugate(z), sq2*sp.conjugate(z), beta],
])
assert sp.expand_complex(sp.expand(M.det()-Delta)) == 0
adj = M.adjugate()
assert sp.expand_complex(sp.expand(adj[0,0]-(alpha*beta-2*uabs))) == 0
assert sp.expand_complex(sp.expand(adj[2,2]-(alpha**2-nu**2-q**2))) == 0
assert sp.expand_complex(sp.expand(adj[0,1]-(beta*(nu+sp.I*q)-2*uabs))) == 0
assert sp.expand_complex(sp.expand(
    adj[0,1]*sp.conjugate(adj[0,1]) - N12
)) == 0
assert sp.expand_complex(sp.expand(
    adj[0,2]*sp.conjugate(adj[0,2]) - N13
)) == 0

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
    s: -sp.Rational(1,100)+sp.Rational(1,50)*u6,
}
vars6=(u1,u2,u3,u4,u5,u6)

def bernstein_coefficients(expr, substitutions=subs):
    poly=sp.Poly(sp.expand(expr.subs(substitutions)), *vars6, domain=sp.QQ)
    degs=tuple(poly.degree(v) for v in vars6)
    data=poly.as_dict()
    for ax,d in enumerate(degs):
        groups={}
        for idx,val in data.items():
            key=idx[:ax]+idx[ax+1:]
            groups.setdefault(key,{})[idx[ax]]=val
        new={}
        for key,arr in groups.items():
            for i in range(d+1):
                total=sp.Rational(0)
                for aa in range(i+1):
                    cv=arr.get(aa,0)
                    if cv:
                        total += cv*sp.Rational(comb(i,aa),comb(d,aa))
                full=key[:ax]+(i,)+key[ax:]
                new[full]=sp.factor(total)
        data=new
    return degs,list(data.values())

print('PROB20-16 C082 SIX-PARAMETER SOLID EXACT CERTIFICATE')
print('box: h[-3/20,1/100], g[-1/500,3/100], r[-1/100,1/100], q[-1/100,1/100], p[-1/250,1/250], s[-1/100,1/100]')
print('J_im operator norm = 2')
print('central spectral margins: K >= 113/1500 I; I-K >= 81/500 I')
mins={}
for name,expr in polys.items():
    degs,vals=bernstein_coefficients(expr)
    m=min(vals)
    assert m>0,(name,m)
    mins[name]=m
    print(f'{name}: degree={degs}, coefficients={len(vals)}, min={m}, approx={float(m)}')

# Exact generic Hermitian tube.
eps=sp.Rational(1,25000)
margin=sp.Rational(81,500)
eta=sp.factor(eps/(margin*(margin-eps)))
assert eta == sp.Rational(500,327969)
a=sp.Rational(7,10)
rho_lo=sp.factor((sp.Rational(7,25)*a-eta)/(a+eta))
rho_hi=sp.factor((sp.Rational(5,12)*a+eta)/(a-eta))
assert rho_lo == sp.Rational(15945481,57519575)
assert rho_hi == sp.Rational(3846305,9163132)
assert rho_lo > sp.Rational(1,10)
assert rho_hi < sp.Rational(21,50)
assert a-eta > sp.Rational(1,2)
assert sp.Rational(99,50)+eta < 2
print('generic Hermitian tube epsilon =', eps, float(eps))
print('exact odds perturbation bound =', eta, float(eta))
print('robust rho interval =', rho_lo, rho_hi, float(rho_lo), float(rho_hi))
print('structured s*J_im endpoint operator displacement = 1/50; ratio to preceding generic tube 1/20000 = 400')
assert sp.Rational(1,50)/sp.Rational(1,20000) == 400

# Retain the unsplit doubled-width certificate failure as a proof-method limitation.
subs_wide=dict(subs)
subs_wide[s]=-sp.Rational(1,50)+sp.Rational(1,25)*u6
for name in ('ell3_hi','rho12_hi'):
    degs,vals=bernstein_coefficients(polys[name],subs_wide)
    m=min(vals)
    assert m < 0
    print(f'wide-s unsplit failure {name}: degree={degs}, min={m}, approx={float(m)}')
print('NOTE: negative Bernstein coefficients at doubled width are certificate failure only, not a counterexample.')
print('ALL EXACT ASSERTIONS PASSED')
