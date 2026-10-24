from __future__ import annotations
import math
import numpy as np
import sympy as sp

h,g,u,v = sp.symbols("h g u v", real=True)
I3 = sp.eye(3)
D = sp.diag(1,1,-2)

Lstar = sp.Matrix([
    [sp.Rational(8,5), sp.Rational(68,125), sp.Rational(51,125)*sp.sqrt(2)],
    [sp.Rational(68,125), sp.Rational(8,5), -sp.Rational(51,125)*sp.sqrt(2)],
    [sp.Rational(51,125)*sp.sqrt(2), -sp.Rational(51,125)*sp.sqrt(2), sp.Rational(9,5)],
])
Kstar = sp.simplify(Lstar*(I3+Lstar).inv())
Kexpected = sp.Matrix([
    [sp.Rational(8846539,15630789), sp.Rational(1812625,15630789), sp.Rational(6375,79546)*sp.sqrt(2)],
    [sp.Rational(1812625,15630789), sp.Rational(8846539,15630789), -sp.Rational(6375,79546)*sp.sqrt(2)],
    [sp.Rational(6375,79546)*sp.sqrt(2), -sp.Rational(6375,79546)*sp.sqrt(2), sp.Rational(47421,79546)],
])
assert sp.simplify(Kstar-Kexpected)==sp.zeros(3)

lowL=Lstar-sp.Rational(1,2)*I3
highL=3*I3-Lstar
assert all(lowL[:k,:k].det()>0 for k in range(1,4))
assert all(highL[:k,:k].det()>0 for k in range(1,4))

Khg=Kstar+h*I3+g*D
Lhg=sp.simplify((I3-Khg).inv()-I3)

A = 125-393*(h+g)
Q = -159092*g**2-79546*g*h+55375*g+79546*h**2-75875*h+15625
R = (3125000-10568625*h-8500547*h**2+31261578*h**3
     +13730625*g-29374828*g*h-20874281*g**2
     -93784734*g**2*h-62523156*g**3)
P = 159092*g**2+79546*g*h-134921*g-79546*h**2-3671*h+28125
N = 4250*(1706*g-853*h+250)
C = 2*6375**2

expected = {
    (0,0):R/(A*Q),(1,1):R/(A*Q),(2,2):P/Q,
    (0,1):N/(A*Q),(1,0):N/(A*Q),
    (0,2):6375*sp.sqrt(2)/Q,(2,0):6375*sp.sqrt(2)/Q,
    (1,2):-6375*sp.sqrt(2)/Q,(2,1):-6375*sp.sqrt(2)/Q,
}
for ij,val in expected.items():
    assert sp.factor(Lhg[ij]-val)==0, ij

hl,hh=sp.Rational(-3,20),sp.Rational(1,100)
gl,gh=sp.Rational(-1,500),sp.Rational(3,100)

def bern2(poly):
    expr=sp.expand(poly.subs({h:hl+(hh-hl)*u,g:gl+(gh-gl)*v}))
    pp=sp.Poly(expr,u,v)
    du,dv=pp.degree(u),pp.degree(v)
    out=[]
    for i in range(du+1):
        for j in range(dv+1):
            bij=sp.Rational(0)
            for k in range(i+1):
                for ell in range(j+1):
                    q=pp.coeff_monomial(u**k*v**ell)
                    bij += q*sp.binomial(i,k)/sp.binomial(du,k)*sp.binomial(j,ell)/sp.binomial(dv,ell)
            out.append(sp.factor(bij))
    return du,dv,out

polys={
    "A":A,
    "Q":Q,
    "R":R,
    "P":P,
    "ell1_lo":10*R-7*A*Q,
    "ell1_hi":39*A*Q-20*R,
    "ell3_lo":10*P-7*Q,
    "ell3_hi":39*Q-20*P,
    "rho12_lo":625*N**2-64*R**2,
    "rho12_hi":9*R**2-64*N**2,
    "rho13_lo":625*C*A-64*R*P,
    "rho13_hi":9*R*P-64*C*A,
}
cert={}
for name,poly in polys.items():
    du,dv,bc=bern2(poly)
    assert all(x>0 for x in bc), (name,bc)
    cert[name]=(du,dv,len(bc),min(bc))

assert hl+gl == sp.Rational(-19,125)
assert hh+gh == sp.Rational(1,25)
assert hl-2*gh == sp.Rational(-21,100)
assert hh-2*gl == sp.Rational(7,500)
assert sp.Rational(1,3)-sp.Rational(21,100)==sp.Rational(37,300)
assert 1-sp.Rational(3,4)-sp.Rational(1,25)==sp.Rational(21,100)

delta=sp.Rational(1,2000)
mcomp=sp.Rational(21,100)
res=sp.factor(delta/(mcomp*(mcomp-delta)))
assert res==sp.Rational(100,8799)
assert res<sp.Rational(1,80)

eta=sp.Rational(1,80)
rho_hi=sp.Rational(3,8)*sp.Rational(56,55)+sp.Rational(1,55)
rho_lo=sp.Rational(8,25)*sp.Rational(56,57)-sp.Rational(1,57)
assert rho_hi==sp.Rational(2,5)
assert rho_lo==sp.Rational(141,475)
assert rho_hi<sp.Rational(21,50)
assert rho_lo>sp.Rational(1,10)
assert sp.Rational(7,10)-eta>sp.Rational(1,2)
assert sp.Rational(39,20)+eta<2

g0=sp.Rational(3,100)
distance=sp.Rational(3,2)*g0
assert distance==sp.Rational(9,200)
assert distance>sp.Rational(1,1000)

Knp=np.array(Kstar.evalf(30),dtype=np.complex128)
rng=np.random.default_rng(20260915)
mins={"kernel":float("inf"),"complement":float("inf"),"ell":float("inf"),"rho":float("inf")}
maxs={"ell":-float("inf"),"rho":-float("inf")}
for _ in range(1000):
    hv=rng.uniform(float(hl),float(hh))
    gv=rng.uniform(float(gl),float(gh))
    X=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    E=(X+X.conj().T)/2
    op=np.max(np.abs(np.linalg.eigvalsh(E)))
    if op:
        E*=rng.uniform(0,float(delta))/op
    K=Knp+hv*np.eye(3)+gv*np.diag([1,1,-2])+E
    ev=np.linalg.eigvalsh(K)
    L=np.linalg.inv(np.eye(3)-K)-np.eye(3)
    ell=np.real(np.diag(L))
    rhos=np.array([
        abs(L[1,2])/math.sqrt(ell[1]*ell[2]),
        abs(L[0,2])/math.sqrt(ell[0]*ell[2]),
        abs(L[0,1])/math.sqrt(ell[0]*ell[1]),
    ])
    assert ev.min()>0 and ev.max()<1
    assert ell.min()>0.5 and ell.max()<2
    assert rhos.min()>0.1 and rhos.max()<0.42
    mins["kernel"]=min(mins["kernel"],float(ev.min()))
    mins["complement"]=min(mins["complement"],float((1-ev).min()))
    mins["ell"]=min(mins["ell"],float(ell.min()))
    maxs["ell"]=max(maxs["ell"],float(ell.max()))
    mins["rho"]=min(mins["rho"],float(rhos.min()))
    maxs["rho"]=max(maxs["rho"],float(rhos.max()))

print("PROB20-16 C082 TWO-PARAMETER PLATE/PRISM CHECK PASSED")
print("rectangle h =",hl,hh,"g =",gl,gh)
print("exact central spectral margins =",sp.Rational(37,300),sp.Rational(21,100))
print("exact tube resolvent bound =",res,float(res))
print("robust rho interval =",rho_lo,rho_hi)
print("distance from g=3/100 point to scalar line =",distance,float(distance))
for name,(du,dv,n,mn) in cert.items():
    print(name,"bidegree =",du,dv,"count =",n,"minimum Bernstein coefficient =",mn,"~",float(sp.N(mn,18)))
print("sample minimum kernel eigenvalue =",mins["kernel"])
print("sample minimum complement eigenvalue =",mins["complement"])
print("sample odds diagonal range =",mins["ell"],maxs["ell"])
print("sample normalized-correlation range =",mins["rho"],maxs["rho"])
