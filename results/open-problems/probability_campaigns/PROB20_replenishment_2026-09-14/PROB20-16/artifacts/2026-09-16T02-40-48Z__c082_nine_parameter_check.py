#!/usr/bin/env python3
"""Exact PROB20-16 ninth-coordinate C082 certificate.

Modes:
  python checker.py low
  python checker.py high

`low` performs the complete nine-variable Bernstein certificate for the ten
field/positivity signs at |y|<=1/4500.

`high` uses the already SHA-verified eight-coordinate y=0 correlation minima
from artifact blob f1236527bd1ed41a52b587b33d589839751748f9 and computes exact
eight-variable Bernstein min/max bounds for the coefficients a_1,...,a_4 in
F(y)=F(0)+sum a_k y^k. It then proves a positive lower bound by the triangle
inequality for |y|<=1/4500.

All proof-critical arithmetic is exact sympy.QQ arithmetic.
"""
import sys
from math import comb
import sympy as sp

h,g,r,q,p,s,t,w,y = sp.symbols('h g r q p s t w y', real=True)
rt2=sp.sqrt(2)
a0=sp.Rational(6784250,15630789)
b0=sp.Rational(32125,79546)
nu0=sp.Rational(1812625,15630789)
c0=sp.Rational(6375,79546)
alpha=a0-h-g
beta=b0-h+2*g
nu=nu0+r
c=c0+p

M=sp.Matrix([
 [alpha-t, -nu-sp.I*q, -rt2*(c+w+sp.I*(s+y))],
 [-nu+sp.I*q, alpha+t, rt2*(c-w+sp.I*(s-y))],
 [-rt2*(c+w-sp.I*(s+y)), rt2*(c-w-sp.I*(s-y)), beta],
])
Delta=sp.expand(M.det())
adj=M.adjugate()
R1=sp.expand(adj[0,0]-Delta)
R2=sp.expand(adj[1,1]-Delta)
P=sp.expand(adj[2,2]-Delta)
N12=sp.expand(sp.re(adj[0,1]*sp.conjugate(adj[0,1])))
N13=sp.expand(sp.re(adj[0,2]*sp.conjugate(adj[0,2])))
N23=sp.expand(sp.re(adj[1,2]*sp.conjugate(adj[1,2])))

low_polys={
 'Delta':Delta,'R1':R1,'R2':R2,'P':P,
 'ell1_lo':2*R1-Delta,'ell1_hi':2*Delta-R1,
 'ell2_lo':2*R2-Delta,'ell2_hi':2*Delta-R2,
 'ell3_lo':2*P-Delta,'ell3_hi':2*Delta-P,
}
high_polys={
 'rho12_lo':100*N12-R1*R2,
 'rho12_hi':441*R1*R2-2500*N12,
 'rho13_lo':100*N13-R1*P,
 'rho13_hi':441*R1*P-2500*N13,
 'rho23_lo':100*N23-R2*P,
 'rho23_hi':441*R2*P-2500*N23,
}

# Exact archived minima from the SHA-verified eight-coordinate y=0 output.
base_mins={
 'rho12_lo':sp.Rational(33002878262321194765114412585767,549723520715672250000000000000000),
 'rho12_hi':sp.Rational(67085632121965674574992373,1050845439838800000000000000),
 'rho13_lo':sp.Rational(12024498914188881968275192309,175911526629015120000000000000),
 'rho13_hi':sp.Rational(49085743948036410813870935037259,61080391190630250000000000000000),
 'rho23_lo':sp.Rational(12024498914188881968275192309,175911526629015120000000000000),
 'rho23_hi':sp.Rational(49085743948036410813870935037259,61080391190630250000000000000000),
}

v8=sp.symbols('u1:9', real=True)
v9=sp.symbols('v1:10', real=True)
Y=sp.Rational(1,4500)
base_sub8={
 h:-sp.Rational(3,20)+sp.Rational(4,25)*v8[0],
 g:-sp.Rational(1,500)+sp.Rational(4,125)*v8[1],
 r:-sp.Rational(1,100)+sp.Rational(1,50)*v8[2],
 q:-sp.Rational(1,100)+sp.Rational(1,50)*v8[3],
 p:-sp.Rational(1,250)+sp.Rational(1,125)*v8[4],
 s:-sp.Rational(1,50)+sp.Rational(1,25)*v8[5],
 t:-sp.Rational(1,300)+sp.Rational(1,150)*v8[6],
 w:-sp.Rational(1,2000)+sp.Rational(1,1000)*v8[7],
}
sub9={
 h:-sp.Rational(3,20)+sp.Rational(4,25)*v9[0],
 g:-sp.Rational(1,500)+sp.Rational(4,125)*v9[1],
 r:-sp.Rational(1,100)+sp.Rational(1,50)*v9[2],
 q:-sp.Rational(1,100)+sp.Rational(1,50)*v9[3],
 p:-sp.Rational(1,250)+sp.Rational(1,125)*v9[4],
 s:-sp.Rational(1,50)+sp.Rational(1,25)*v9[5],
 t:-sp.Rational(1,300)+sp.Rational(1,150)*v9[6],
 w:-sp.Rational(1,2000)+sp.Rational(1,1000)*v9[7],
 y:-Y+2*Y*v9[8],
}

def bern_bounds(expr, variables, subs):
    poly=sp.Poly(sp.expand(expr.subs(subs)),*variables,domain=sp.QQ)
    degs=tuple(poly.degree(x) for x in variables)
    data=poly.as_dict()
    for ax,d in enumerate(degs):
        groups={}
        for idx,val in data.items():
            groups.setdefault(idx[:ax]+idx[ax+1:],{})[idx[ax]]=val
        ratios=[[sp.Rational(comb(i,a),comb(d,a)) for a in range(i+1)]
                for i in range(d+1)]
        new={}
        for key,arr in groups.items():
            for i in range(d+1):
                z=sp.Rational(0)
                for a in range(i+1):
                    cv=arr.get(a,0)
                    if cv:
                        z += cv*ratios[i][a]
                new[key[:ax]+(i,)+key[ax:]]=z
        data=new
    vals=list(data.values())
    return degs,len(vals),min(vals),max(vals)

if len(sys.argv)!=2 or sys.argv[1] not in {'low','high'}:
    raise SystemExit('usage: checker.py low|high')

print('PROB20-16 NINE-PARAMETER DIRECT C082 CERTIFICATE')
print('certified ninth width |y| <=',Y)

if sys.argv[1]=='low':
    for name,expr in low_polys.items():
        deg,n,mn,mx=bern_bounds(expr,v9,sub9)
        assert mn>0,(name,mn)
        print(f'{name}: degree={deg}, coefficients={n}, min={mn}, approx={float(mn)}, max={mx}')
    mK=sp.Rational(51,1000)-2*Y
    mI=sp.Rational(413,3000)-2*Y
    assert mK==sp.Rational(91,1800)
    assert mI==sp.Rational(2471,18000)
    print('kernel spectral lower margin =',mK)
    print('complement spectral lower margin =',mI)
    print('LOW EXACT ASSERTIONS PASSED')
else:
    for name,expr in high_polys.items():
        py=sp.Poly(expr,y)
        assert py.degree()<=4
        loss=sp.Rational(0)
        print(name,'base_min=',base_mins[name])
        for k in range(1,5):
            coeff=sp.expand(py.coeff_monomial(y**k))
            if coeff==0:
                mn=mx=sp.Rational(0); deg=(); n=1
            else:
                deg,n,mn,mx=bern_bounds(coeff,v8,base_sub8)
            Mabs=max(abs(mn),abs(mx))
            loss += Mabs*Y**k
            print(f'  k={k}: degree={deg}, coefficients={n}, min={mn}, max={mx}, M={Mabs}')
        residual=sp.factor(base_mins[name]-loss)
        assert residual>0,(name,residual)
        print('  certified residual=',residual,'approx=',float(residual))
    print('HIGH EXACT COEFFICIENT-BOUND ASSERTIONS PASSED')

print('STATUS: EXACT CERTIFICATE PASSED')
