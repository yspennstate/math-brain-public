"""PROVED: exact small-ratio controls for all three padding coefficients."""
import sympy as S
from fractions import Fraction as F
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from frame import A,B,C,d,e,f,h,a,r,formula
from padding import base_coefficients

def construct(rho,index):
    assert index in (0,1,2)
    rho=F(rho);rhoS=S.Rational(rho.numerator,rho.denominator)
    rr,*gen=ring('z0,z1,z2,z3,x0,x1,x2',QQ);z,x=gen[:4],gen[4:]
    U=[sum(((5-j)if i<j else -j)*z[j-1]for j in range(1,5))for i in range(5)]
    span=U[0]-U[4];W=[sum((U[4]-U[j+1])*x[j]for j in range(3))]+[span*x[j]for j in range(3)]+[sum((U[j+1]-U[0])*x[j]for j in range(3))]
    t=sum(v*v for v in U);n=sum(v*v for v in W)
    raw=[sum(v**4 for v in U),sum(v**4 for v in W),sum(v*v*w*w for v,w in zip(U,W)),sum(v**3 for v in U),sum(v*v*w for v,w in zip(U,W)),sum(v*w*w for v,w in zip(U,W)),sum(v**3 for v in W),-U[0]*U[4],(U[0]+U[4])**2]
    degrees=[(4,0),(0,4),(2,2),(3,0),(2,1),(1,2),(0,3),(2,0),(2,0)]
    pp,vv=S.symbols('p vv');sym=[A,B,C,d,e,f,h,pp,vv]
    R6=3*d*d+3*r*r*h*h+(1+4*r)*e*e+(r*r+4*r)*f*f+2*(1+r)*(d*f+r*h*e)
    radial=S.Poly(S.expand(base_coefficients((A,B,C),a,r)[index]/(16,8,1)[index]+a*a*R6),a)
    H=S.Poly(radial.nth(2),r)
    # Subtract exactly the nonnegative completion in the r^2 coefficient.
    Rstar=S.expand(H.nth(2)-3*(h+e/3)**2-f*f-(C-e*e)/3)
    assert not any(Rstar.has(q)for q in (d,e,f,h))
    D=20*pp-1-r*(7-5*vv)
    phi=S.expand(radial.nth(0)*D*D+2*D*radial.nth(1)+4*(H.nth(0)+r*H.nth(1)+r*r*Rstar))
    ctrls=[phi.subs(r,0),phi.subs(r,0)+rhoS*S.diff(phi,r).subs(r,0)/2,phi.subs(r,rhoS)]
    result=[]
    for control in ctrls:
        out=rr.zero
        for powers,c in S.Poly(control,*sym).terms():
            ud=sum(p*de[0]for p,de in zip(powers,degrees));wd=sum(p*de[1]for p,de in zip(powers,degrees))
            assert ud%2==wd%2==0 and ud<=6 and wd<=4
            term=QQ(int(c.p),int(c.q))*t**(3-ud//2)*n**(2-wd//2)
            for val,power in zip(raw,powers):term*=val**power
            out+=term
        result.append(out)
    return rr,tuple(result)
