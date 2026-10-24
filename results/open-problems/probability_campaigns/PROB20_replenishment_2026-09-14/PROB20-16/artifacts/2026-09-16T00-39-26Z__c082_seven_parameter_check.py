#!/usr/bin/env python3
# PROB20-16 exact seven-parameter C082 certificate + wide-core tube.
import sympy as sp
from math import comb

h,g,r,q,p,s,t = sp.symbols('h g r q p s t', real=True)
v = sp.symbols('u1:8', real=True)

a0=sp.Rational(6784250,15630789)
b0=sp.Rational(32125,79546)
nu0=sp.Rational(1812625,15630789)
c0=sp.Rational(6375,79546)
alpha=a0-h-g
beta=b0-h+2*g
nu=nu0+r
c=c0+p
uabs=c**2+s**2

Delta=sp.expand(alpha**2*beta-4*alpha*uabs-beta*(nu**2+q**2+t**2)+4*nu*uabs)
R1=sp.expand(-alpha**2*beta+alpha*beta+4*alpha*uabs
             +beta*(nu**2+q**2+t**2+t)-4*nu*uabs-2*uabs)
R2=sp.expand(-alpha**2*beta+alpha*beta+4*alpha*uabs
             +beta*(nu**2+q**2+t**2-t)-4*nu*uabs-2*uabs)
P=sp.expand(-alpha**2*beta+alpha**2+4*alpha*uabs
            +beta*(nu**2+q**2+t**2)-4*nu*uabs-nu**2-q**2-t**2)
N12=sp.expand((beta*nu-2*uabs)**2+beta**2*q**2)
N13=sp.expand(2*uabs*((alpha-nu+t)**2+q**2))
N23=sp.expand(2*uabs*((alpha-nu-t)**2+q**2))

polys={
 'Delta':Delta,'R1':R1,'R2':R2,'P':P,
 'ell1_lo':2*R1-Delta,'ell1_hi':2*Delta-R1,
 'ell2_lo':2*R2-Delta,'ell2_hi':2*Delta-R2,
 'ell3_lo':2*P-Delta,'ell3_hi':2*Delta-P,
 'rho12_lo':100*N12-R1*R2,'rho12_hi':441*R1*R2-2500*N12,
 'rho13_lo':100*N13-R1*P,'rho13_hi':441*R1*P-2500*N13,
 'rho23_lo':100*N23-R2*P,'rho23_hi':441*R2*P-2500*N23,
}
subs={
 h:-sp.Rational(3,20)+sp.Rational(4,25)*v[0],
 g:-sp.Rational(1,500)+sp.Rational(4,125)*v[1],
 r:-sp.Rational(1,100)+sp.Rational(1,50)*v[2],
 q:-sp.Rational(1,100)+sp.Rational(1,50)*v[3],
 p:-sp.Rational(1,250)+sp.Rational(1,125)*v[4],
 s:-sp.Rational(1,50)+sp.Rational(1,25)*v[5],
 t:-sp.Rational(1,300)+sp.Rational(1,150)*v[6],
}

def bern_bounds(expr):
    poly=sp.Poly(sp.expand(expr.subs(subs)),*v,domain=sp.QQ)
    degs=tuple(poly.degree(x) for x in v)
    data=poly.as_dict()
    for ax,d in enumerate(degs):
        groups={}
        for idx,val in data.items():
            key=idx[:ax]+idx[ax+1:]
            groups.setdefault(key,{})[idx[ax]]=val
        new={}
        for key,arr in groups.items():
            for i in range(d+1):
                z=sp.Rational(0)
                for a in range(i+1):
                    cv=arr.get(a,0)
                    if cv:
                        z += cv*sp.Rational(comb(i,a),comb(d,a))
                new[key[:ax]+(i,)+key[ax:]]=z
        data=new
    vals=list(data.values())
    return degs,len(vals),min(vals),max(vals)

print('PROB20-16 SEVEN-PARAMETER DIRECT C082 CERTIFICATE')
bounds={}
for name,e in polys.items():
    degs,n,mn,mx=bern_bounds(e)
    assert mn>0,(name,mn)
    bounds[name]=(mn,mx)
    print(f'{name}: degree={degs}, coefficients={n}, min={mn}, approx={float(mn)}')

mK=sp.Rational(13,250)
mI=sp.Rational(52,375)
assert mK>0 and mI>0
print('kernel spectral lower margin =',mK)
print('complement spectral lower margin =',mI)

MD=bounds['Delta'][1]
MR1=bounds['R1'][1]; MR2=bounds['R2'][1]; MP=bounds['P'][1]
field_gaps=[
 bounds['ell1_lo'][0]/(2*MD), bounds['ell1_hi'][0]/MD,
 bounds['ell2_lo'][0]/(2*MD), bounds['ell2_hi'][0]/MD,
 bounds['ell3_lo'][0]/(2*MD), bounds['ell3_hi'][0]/MD,
]
delta_ell=min(field_gaps)
rho_lo_gaps=[
 bounds['rho12_lo'][0]/(100*MR1*MR2)*sp.Rational(25,13),
 bounds['rho13_lo'][0]/(100*MR1*MP)*sp.Rational(25,13),
 bounds['rho23_lo'][0]/(100*MR2*MP)*sp.Rational(25,13),
]
rho_hi_gaps=[
 bounds['rho12_hi'][0]/(2500*MR1*MR2)*sp.Rational(25,21),
 bounds['rho13_hi'][0]/(2500*MR1*MP)*sp.Rational(25,21),
 bounds['rho23_hi'][0]/(2500*MR2*MP)*sp.Rational(25,21),
]
delta_rho_lo=min(rho_lo_gaps)
delta_rho_hi=min(rho_hi_gaps)
eps_star=min(delta_ell/2, sp.Rational(5,11)*delta_rho_lo,
             sp.Rational(25,71)*delta_rho_hi)

print('delta_ell >=',delta_ell,float(delta_ell))
print('delta_rho_lo >=',delta_rho_lo,float(delta_rho_lo))
print('delta_rho_hi >=',delta_rho_hi,float(delta_rho_hi))
print('epsilon_star =',eps_star,float(eps_star))

theta=sp.Rational(1,150000)
odds_move=sp.factor(theta/(mI*(mI-theta)))
assert odds_move < eps_star
print('tube radius =',theta)
print('odds resolvent move =',odds_move,float(odds_move))
print('odds resolvent move < epsilon_star: PASSED')
print('ALL EXACT ASSERTIONS PASSED')
