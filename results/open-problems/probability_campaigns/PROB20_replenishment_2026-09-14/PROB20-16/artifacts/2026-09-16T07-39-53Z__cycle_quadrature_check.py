import itertools
import math
import numpy as np
import sympy as sp

# Exact symbolic determinant and atom-coefficient checks.
d1,d2,d3,r,s,u,y,z=sp.symbols('d1 d2 d3 r s u y z', real=True)
M=sp.Matrix([[d1,r,u+sp.I*y],[r,d2,s],[u-sp.I*y,s,d3]])
det=sp.expand(M.det())
target=sp.expand(d1*d2*d3-d1*s**2-d2*(u**2+y**2)-d3*r**2+2*r*s*u)
assert sp.simplify(det-target)==0

a,b,c=sp.symbols('a b c', real=True)
K=sp.Matrix([[a,r,u+sp.I*y],[r,b,s],[u-sp.I*y,s,c]])
for bits in itertools.product([0,1], repeat=3):
    Mm=K.copy(); zeros=0
    for i,bit in enumerate(bits):
        if bit==0:
            Mm[i,i]-=1; zeros+=1
    p=sp.expand(((-1)**zeros)*Mm.det())
    coeff=sp.Poly(p,y).coeff_monomial(y**2)
    pi=b if bits[1]==1 else (1-b)
    expected=-pi*((-1)**(bits[0]+bits[2]))
    assert sp.simplify(coeff-expected)==0
    assert sp.Poly(p,y).coeff_monomial(y)==0

# Exact two-site DPP interaction identity.
A,D,X2=sp.symbols('A D X2', real=True)
p11=A*D-X2
p10=A-p11
p01=D-p11
p00=1-A-D+p11
assert sp.expand(p10*p01-p00*p11-X2)==0

# Exact rational strict example on |y|<=2/25.
aa=sp.Rational(21,50); bb=sp.Rational(53,100); cc=sp.Rational(57,100)
rr=sp.Rational(9,100); ss=sp.Rational(2,25); uu=sp.Rational(1,25)
zmax=sp.Rational(4,625)
detKz=aa*bb*cc-aa*ss**2-bb*(uu**2+z)-cc*rr**2+2*rr*ss*uu
detIz=(1-aa)*(1-bb)*(1-cc)-(1-aa)*ss**2-(1-bb)*(uu**2+z)-(1-cc)*rr**2-2*rr*ss*uu
assert aa>0 and aa*bb-rr**2>0 and detKz.subs(z,zmax)>0
assert (1-aa)>0 and (1-aa)*(1-bb)-rr**2>0 and detIz.subs(z,zmax)>0

example_atoms=[]
for bits in itertools.product([0,1], repeat=3):
    Mm=K.subs({a:aa,b:bb,c:cc,r:rr,s:ss,u:uu})
    M2=Mm.copy(); zeros=0
    for i,bit in enumerate(bits):
        if bit==0:
            M2[i,i]-=1; zeros+=1
    p=sp.expand(((-1)**zeros)*M2.det())
    poly=sp.Poly(p,y)
    pz=poly.coeff_monomial(1)+poly.coeff_monomial(y**2)*z
    vals=[sp.simplify(pz.subs(z,0)),sp.simplify(pz.subs(z,zmax))]
    assert min(vals)>0
    example_atoms.extend(vals)

# Numerical diagnostic: compare direct atom Hessian with the exact conditional formula.
def probs(params, yy):
    aa0,bb0,cc0,rr0,ss0,uu0=params
    KK=np.array([[aa0,rr0,uu0+1j*yy],[rr0,bb0,ss0],[uu0-1j*yy,ss0,cc0]],complex)
    out={}
    for bits in itertools.product([0,1], repeat=3):
        MM=KK.copy(); zeros=0
        for i,bit in enumerate(bits):
            if bit==0:
                MM[i,i]-=1; zeros+=1
        out[bits]=float((((-1)**zeros)*np.linalg.det(MM)).real)
    return KK,out

def curvature_atom(params, yy):
    KK,p=probs(params,yy)
    bb0=params[1]
    H2=0.0
    for bits,pp in p.items():
        pi=bb0 if bits[1] else 1-bb0
        ci=-pi*((-1)**(bits[0]+bits[2]))
        py=2*yy*ci
        pyy=2*ci
        H2 += -(py*py/pp + pyy*math.log(pp))
    return H2

def curvature_cond(params, yy):
    KK,p=probs(params,yy)
    bb0=params[1]
    lamavg=0.0; invsum=0.0
    for mid,pi in [(0,1-bb0),(1,bb0)]:
        q=[p[(x1,mid,x3)]/pi for x1,x3 in [(0,0),(1,0),(0,1),(1,1)]]
        q00,q10,q01,q11=q
        lam=math.log(q10*q01/(q00*q11))
        assert lam>=-1e-11
        lamavg += pi*lam
        invsum += pi*sum(1/qx for qx in q)
    return -2*lamavg-4*yy*yy*invsum

rng=np.random.default_rng(20260916)
count=0; attempts=0
max_disc=0.0
max_curv=-1e300
while count<1000 and attempts<100000:
    attempts+=1
    aa0,bb0,cc0=rng.uniform(.28,.72,3)
    rr0,ss0,uu0=rng.uniform(-.09,.09,3)
    yy=float(rng.uniform(-.09,.09))
    params=(aa0,bb0,cc0,rr0,ss0,uu0)
    KK,p=probs(params,yy)
    ev=np.linalg.eigvalsh(KK)
    if ev[0]<=.03 or ev[-1]>=.97 or min(p.values())<=1e-8:
        continue
    h2a=curvature_atom(params,yy)
    h2c=curvature_cond(params,yy)
    max_disc=max(max_disc,abs(h2a-h2c))
    max_curv=max(max_curv,h2c)
    assert h2c<=1e-10
    count+=1
assert count==1000

print('PASS symbolic determinant identity')
print('PASS 8 exact atom y^2 coefficients')
print('PASS two-site interaction identity')
print('exact rational example zmax =', zmax)
print('exact rational example det K endpoint =', sp.factor(detKz.subs(z,zmax)))
print('exact rational example det(I-K) endpoint =', sp.factor(detIz.subs(z,zmax)))
print('exact rational example minimum atom endpoint =', min(example_atoms))
print('diagnostic samples =', count)
print('diagnostic max direct-vs-conditional curvature discrepancy =', repr(max_disc))
print('diagnostic largest analytic H second derivative =', repr(max_curv))
