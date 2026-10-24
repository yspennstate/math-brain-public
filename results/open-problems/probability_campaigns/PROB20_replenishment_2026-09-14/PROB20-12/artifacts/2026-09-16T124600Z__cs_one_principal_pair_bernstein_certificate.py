import sympy as sp
from itertools import product
from math import comb
from collections import Counter

# Exact checker for PROB20-12, 2026-09-16T124600Z.
# One-common-principal-pair slice p2=q2=0 of the strong 540-facet operator gap.

c1,c2,s1,s2,p0,p1,q0,q1=sp.symbols('c1 c2 s1 s2 p0 p1 q0 q1', real=True)
z0,z1,z2,z3,z4,z5=sp.symbols('z0 z1 z2 z3 z4 z5', real=True)
z=(z0,z1,z2,z3,z4,z5)

# Cross A∧B component of a bivector beta in the CS basis.
M=sp.Matrix([
    [z0,       s1*z1,        s2*z2],
    [-c1*z3,  0,             c1*s2*z5],
    [-c2*z4, -c2*s1*z5,      0]
])
p=sp.Matrix([p0,p1,0])
q=sp.Matrix([q0,q1,0])
P=sp.eye(3)-p*p.T
Q=sp.eye(3)-q*q.T
N=P*M*Q

# Base 3+3 gap D = diag(0,r,r,d,d,r+d).
r=c1**2*c2**2
d=s1**2*s2**2
Dq=r*(z1**2+z2**2)+d*(z3**2+z4**2)+(r+d)*z5**2

# Correct real-gauge target amplitude <a∧b, J beta>.
# On this slice p2=q2=0.
f=(-p1*c1*q0)*z2 + (-p0*q1*s1)*z4 + (p0*q0)*z5

cross=sp.expand(sum(N[i,j]**2 for i in range(3) for j in range(3)))
qgap=sp.expand(Dq+cross-f**2)
G=sp.hessian(qgap,z)/2

# Reduce by exact sphere/CS relations.
rels=[
    c1**2+s1**2-1,
    c2**2+s2**2-1,
    p0**2+p1**2-1,
    q0**2+q1**2-1,
]
gb=sp.groebner(rels,s1,s2,c1,c2,p0,p1,q0,q1,order='grevlex')
def red(e):
    return sp.factor(gb.reduce(sp.expand(e))[1])

# Block split.
Aidx=[0,1,3]
Bidx=[2,4,5]
off=[red(G[i,j]) for i in Aidx for j in Bidx]
assert all(v==0 for v in off)
GA=G.extract(Aidx,Aidx)
GB=G.extract(Bidx,Bidx)

# Introduce squared variables X,Y,U,V.
X,Y,U,V=sp.symbols('X Y U V', real=True)
def evenmap(e):
    e=red(e)
    poly=sp.Poly(sp.expand(e),c1,c2,p1,q1)
    out=0
    for mon,coef in poly.terms():
        assert all(k%2==0 for k in mon), (mon,e)
        out += coef*X**(mon[0]//2)*Y**(mon[1]//2)*U**(mon[2]//2)*V**(mon[3]//2)
    return sp.factor(out)

# GA certificates.
A00=evenmap(GA[0,0])
A01=evenmap(GA.extract([0,1],[0,1]).det())
A02=evenmap(GA.extract([0,2],[0,2]).det())
Adet=evenmap(GA.det())
assert sp.expand(A00-U*V)==0
assert sp.expand(A01-U*V*X*Y)==0
assert sp.expand(A02-U*V*(1-X)*(1-Y))==0
assert sp.expand(Adet-U*V*X*Y*(1-X)*(1-Y))==0

# GB pivot and determinant certificates.
B00=evenmap(GB[0,0])
M01=evenmap(GB.extract([0,1],[0,1]).det())
M02=evenmap(GB.extract([0,2],[0,2]).det())
Bdet=evenmap(GB.det())
B00_expected=(1-U)*X*Y+U*((1-X)*(1-Y)+X*V)
Bdet_expected=(X*Y+U*(1-X))*((1-X)*(1-Y)+X*V)*(U*(1-X)*(1-Y)+V*X*Y)
assert sp.expand(B00-B00_expected)==0
assert sp.expand(Bdet-Bdet_expected)==0

# Tensor-product Bernstein conversion on [0,1]^4.
vars4=(X,Y,U,V)
def bernstein_coeffs(poly,degs):
    P=sp.Poly(sp.expand(poly),*vars4)
    mon=P.as_dict()
    out={}
    for k in product(*[range(d+1) for d in degs]):
        val=sp.Rational(0)
        for j,a in mon.items():
            if all(jj<=kk for jj,kk in zip(j,k)):
                w=sp.Rational(1)
                for jj,kk,dd in zip(j,k,degs):
                    w *= sp.Rational(comb(kk,jj),comb(dd,jj))
                val += a*w
        out[k]=sp.factor(val)
    return out

bc01=bernstein_coeffs(M01,(2,2,2,2))
bc02=bernstein_coeffs(M02,(2,2,2,2))
assert all(v>=0 for v in bc01.values())
assert all(v>=0 for v in bc02.values())

cnt01=Counter(bc01.values())
cnt02=Counter(bc02.values())
expected01={sp.Rational(0):56,sp.Rational(1,8):3,sp.Rational(1,4):9,
            sp.Rational(1,2):6,sp.Rational(3,4):1,sp.Rational(1):6}
expected02={sp.Rational(0):48,sp.Rational(1,8):4,sp.Rational(1,4):10,
            sp.Rational(5,16):1,sp.Rational(3,8):1,sp.Rational(1,2):11,
            sp.Rational(1):6}
assert dict(cnt01)==expected01
assert dict(cnt02)==expected02

print('block_split', True)
print('GA_A00', A00)
print('GA_minor01', A01)
print('GA_minor02', A02)
print('GA_det', Adet)
print('GB_B00', sp.factor(B00))
print('GB_det', sp.factor(Bdet))
print('M01_Bernstein_counts', sorted((str(k),v) for k,v in cnt01.items()))
print('M02_Bernstein_counts', sorted((str(k),v) for k,v in cnt02.items()))
print('ALL EXACT CHECKS PASSED')
