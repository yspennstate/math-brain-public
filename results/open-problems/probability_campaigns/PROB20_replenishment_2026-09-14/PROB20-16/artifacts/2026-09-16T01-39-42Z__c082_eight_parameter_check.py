#!/usr/bin/env python3
"""Exact PROB20-16 eight-parameter C082 certificate.

Run memory-bounded parts separately, e.g.
  python ...py low
  python ...py rho12_lo
  python ...py rho12_hi
  python ...py rho13_lo
  python ...py rho13_hi
  python ...py rho23_lo
  python ...py rho23_hi

All arithmetic in the proof-critical certificate is exact sympy.QQ arithmetic.
"""
import sys
from math import comb
import sympy as sp

h,g,r,q,p,s,t,w = sp.symbols('h g r q p s t w', real=True)
v = sp.symbols('u1:9', real=True)

a0=sp.Rational(6784250,15630789)
b0=sp.Rational(32125,79546)
nu0=sp.Rational(1812625,15630789)
c0=sp.Rational(6375,79546)
alpha=a0-h-g
beta=b0-h+2*g
nu=nu0+r
c=c0+p
rt2=sp.sqrt(2)

M=sp.Matrix([
 [alpha-t, -nu-sp.I*q, -rt2*(c+w+sp.I*s)],
 [-nu+sp.I*q, alpha+t, rt2*(c-w+sp.I*s)],
 [-rt2*(c+w-sp.I*s), rt2*(c-w-sp.I*s), beta],
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
W=sp.Rational(1,2000)
subs={
 h:-sp.Rational(3,20)+sp.Rational(4,25)*v[0],
 g:-sp.Rational(1,500)+sp.Rational(4,125)*v[1],
 r:-sp.Rational(1,100)+sp.Rational(1,50)*v[2],
 q:-sp.Rational(1,100)+sp.Rational(1,50)*v[3],
 p:-sp.Rational(1,250)+sp.Rational(1,125)*v[4],
 s:-sp.Rational(1,50)+sp.Rational(1,25)*v[5],
 t:-sp.Rational(1,300)+sp.Rational(1,150)*v[6],
 w:-W+2*W*v[7],
}

def bern_bounds(expr):
    poly=sp.Poly(sp.expand(expr.subs(subs)),*v,domain=sp.QQ)
    degs=tuple(poly.degree(x) for x in v)
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

def check(name,expr):
    degs,n,mn,mx=bern_bounds(expr)
    assert mn>0,(name,mn)
    print(f'{name}: degree={degs}, coefficients={n}, min={mn}, approx={float(mn)}, max={mx}')

if len(sys.argv)!=2:
    raise SystemExit('usage: checker.py low|rho12_lo|rho12_hi|rho13_lo|rho13_hi|rho23_lo|rho23_hi')
part=sys.argv[1]
print('PROB20-16 EIGHT-PARAMETER S_RE DIRECT C082 CERTIFICATE W=1/2000')
if part=='low':
    for name,expr in low_polys.items():
        check(name,expr)
    mK=sp.Rational(13,250)-2*W
    mI=sp.Rational(52,375)-2*W
    assert mK==sp.Rational(51,1000)
    assert mI==sp.Rational(413,3000)
    print('kernel spectral lower margin =',mK)
    print('complement spectral lower margin =',mI)
elif part in high_polys:
    check(part,high_polys[part])
else:
    raise SystemExit('unknown part')
print('EXACT ASSERTIONS PASSED FOR PART',part)
