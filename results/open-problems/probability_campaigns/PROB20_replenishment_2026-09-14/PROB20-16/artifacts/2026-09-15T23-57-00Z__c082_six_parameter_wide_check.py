#!/usr/bin/env python3
# PROB20-16 exact addendum checker: doubled sixth coordinate, direct C082 bounds.
import sympy as sp
from math import comb

h,g,r,q,p,s,u1,u2,u3,u4,u5,u6 = sp.symbols(
    'h g r q p s u1 u2 u3 u4 u5 u6', real=True
)
a0=sp.Rational(6784250,15630789)
b0=sp.Rational(32125,79546)
nu0=sp.Rational(1812625,15630789)
c0=sp.Rational(6375,79546)
alpha=a0-h-g
beta=b0-h+2*g
nu=nu0+r
c=c0+p
uabs=c**2+s**2
Delta=sp.expand(beta*(alpha**2-nu**2-q**2)-4*uabs*(alpha-nu))
R=sp.expand(alpha*beta-2*uabs-Delta)
P=sp.expand(alpha**2-nu**2-q**2-Delta)
N12=sp.expand((beta*nu-2*uabs)**2+beta**2*q**2)
N13=sp.expand(2*uabs*((alpha-nu)**2+q**2))

# Direct C082 chart inequalities: 1/2 <= ell <= 2; 1/10 <= rho <= 21/50.
polys={
 'Delta':Delta,'R':R,'P':P,
 'ell12_lo':2*R-Delta,
 'ell12_hi':2*Delta-R,
 'ell3_lo':2*P-Delta,
 'ell3_hi':2*Delta-P,
 'rho12_lo':100*N12-R**2,
 'rho12_hi':441*R**2-2500*N12,
 'rho13_lo':100*N13-R*P,
 'rho13_hi':441*R*P-2500*N13,
}
subs={
 h:-sp.Rational(3,20)+sp.Rational(4,25)*u1,
 g:-sp.Rational(1,500)+sp.Rational(4,125)*u2,
 r:-sp.Rational(1,100)+sp.Rational(1,50)*u3,
 q:-sp.Rational(1,100)+sp.Rational(1,50)*u4,
 p:-sp.Rational(1,250)+sp.Rational(1,125)*u5,
 s:-sp.Rational(1,50)+sp.Rational(1,25)*u6,
}
vars6=(u1,u2,u3,u4,u5,u6)

def bern(expr):
    poly=sp.Poly(sp.expand(expr.subs(subs)),*vars6,domain=sp.QQ)
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
                new[key[:ax]+(i,)+key[ax:]]=sp.factor(total)
        data=new
    vals=list(data.values())
    return degs,len(vals),min(vals)

print('PROB20-16 SIX-PARAMETER DOUBLED-S DIRECT C082 CERTIFICATE')
print('s interval = [-1/50,1/50]')
for name,e in polys.items():
    degs,n,m=bern(e)
    assert m>0,(name,m)
    print(f'{name}: degree={degs}, coefficients={n}, min={m}, approx={float(m)}')
print('All direct C082 inequalities hold on the doubled-s central box.')
print('No full-dimensional tube around this doubled-s box is claimed by this checker.')
print('ALL EXACT ASSERTIONS PASSED')
