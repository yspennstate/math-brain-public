#!/usr/bin/env python3
"""Exact certificate: arbitrary positive weights on K2,3."""
import json
from pathlib import Path
import sympy as sp


def is_forest(n,E):
    p=list(range(n))
    def f(x):
        while p[x]!=x:p[x]=p[p[x]];x=p[x]
        return x
    for u,v in E:
        u,v=f(u),f(v)
        if u==v:return False
        p[u]=v
    return True


def polynomial(w,z):
    edges=[(0,j) for j in (2,3,4)]+[(1,j) for j in (2,3,4)]
    out=0;count=0
    for m in range(64):
        E=[edges[k] for k in range(6) if m>>k&1]
        if not is_forest(5,E):continue
        count+=1;p=list(range(5))
        def f(x):
            while p[x]!=x:p[x]=p[p[x]];x=p[x]
            return x
        for u,v in E:u,v=f(u),f(v);p[u]=v
        cs={}
        for i in range(5):cs.setdefault(f(i),[]).append(i)
        out+=sp.prod(w[k] for k in range(6) if m>>k&1)*sp.prod(1+sum(z[i] for i in C) for C in cs.values())
    return sp.expand(out),count


def rayleigh(P,z,i,j):return sp.expand(sp.diff(P,z[i])*sp.diff(P,z[j])-P*sp.diff(P,z[i],z[j]))
def qdata(F,t):
    v=sp.Poly(F,t).all_coeffs();v=[0]*(3-len(v))+v;A,B,C=map(sp.expand,v)
    return A,B,C,sp.expand(B*B-4*A*C)
def bdet(H,x,y):
    p=sp.Poly(sp.expand(H),x,y);U=p.coeff_monomial(x*x);V=p.coeff_monomial(x*y)/2;W=p.coeff_monomial(y*y)
    return sp.expand(U*W-V*V),U,W


def main():
    a,b,c,d,e,f=sp.symbols('a b c d e f',positive=True);pars=(a,b,c,d,e,f)
    z=sp.symbols('z0:5',real=True);x,y=sp.symbols('x y',real=True)
    P,n=polynomial(pars,z);checks=[]
    R=lambda u,v,r,s:(1+u+v)*(1+r)*(1+s)+u*v*(1+r+s)
    # Cross determinant for columns (u,r) and (v,s).
    T=lambda u,v,r,s:u*s*(u+1)*(s+1)+v*r*(v+1)*(r+1)-2*u*v*r*s
    Q=((1+a+b+c)*(1+d)*(1+e)*(1+f)
       +a*b*(1+f)*(1+d+e)+a*c*(1+e)*(1+d+f)
       +b*c*(1+d)*(1+e+f)+a*b*c*(1+d+e+f))

    F01=sp.expand(rayleigh(P,z,0,1).subs({z[3]:x-1-b-e,z[4]:y-1-c-f}))
    A01,_,_,D01=qdata(F01,z[2])
    E01=c*f*(c+1)*(f+1)*x*x+2*b*c*e*f*x*y+b*e*(b+1)*(e+1)*y*y
    checks += [sp.expand(A01-E01)==0,bdet(A01,x,y)[0]==sp.expand(b*c*e*f*R(b,c,e,f))]
    phi=sp.cancel(-D01/(4*a*d*x*x*y*y));detphi,Uphi,Wphi=bdet(phi,x,y)
    checks += [sp.Poly(phi,x,y).total_degree()==2,
      sp.expand(detphi-b*c*e*f*(a+1)*(d+1)*Q)==0,
      all(k>0 for k in sp.Poly(Uphi,*pars).coeffs()),all(k>0 for k in sp.Poly(Wphi,*pars).coeffs()),
      sp.expand(F01.subs(x,0)-b*e*(b+1)*(e+1)*y*y*(z[2]+a+d+1)**2)==0,
      sp.expand(F01.subs(y,0)-c*f*(c+1)*(f+1)*x*x*(z[2]+a+d+1)**2)==0]

    F02=sp.expand(rayleigh(P,z,0,2).subs({z[3]:x-1-b-e,z[4]:y-1-c-f}))
    A02,_,_,D02=qdata(F02,z[1])
    checks += [sp.expand(A02-a*(a+1)*x*x*y*y)==0,sp.expand(D02-D01)==0,
      sp.expand(F02.subs(x,0)-e*(e+1)*T(a,b,d,e)*y*y)==0,
      sp.expand(F02.subs(y,0)-f*(f+1)*T(a,c,d,f)*x*x)==0]

    F23=sp.expand(rayleigh(P,z,2,3).subs({z[0]:x-1-a-b-c,z[1]:y-1-d-e-f}))
    A23,_,_,D23=qdata(F23,z[4]);detA23,_,_=bdet(A23,x,y)
    E23=d*e*(d+1)*(e+1)*x*x+2*a*b*d*e*x*y+a*b*(a+1)*(b+1)*y*y
    checks += [sp.expand(A23-E23)==0,sp.expand(detA23-a*b*d*e*R(a,b,d,e))==0,
      sp.expand(F23.subs({x:0,y:0})-T(a,c,d,f)*T(b,c,e,f))==0]
    detD23,UD23,WD23=bdet(-D23,x,y)
    target=16*a*b*c*d*e*f*T(a,b,d,e)*T(a,c,d,f)*T(b,c,e,f)*Q
    checks += [sp.Poly(-D23,x,y).total_degree()==2,sp.expand(detD23-target)==0,
      sp.expand(UD23.subs(dict(zip(pars,[1]*6))))>0,
      sp.expand(WD23.subs(dict(zip(pars,[1]*6))))>0]
    assert all(checks),checks
    report={"status":"PASS","sympy_version":sp.__version__,"scope":"arbitrary positive (a,b,c;d,e,f) on K2,3",
      "backbone_forests":n,"spoke_terms":len(sp.Poly(P,*z).terms()),"exact_identity_checks":len(checks),
      "Q_term_count":len(sp.Poly(sp.expand(Q),*pars).terms()),
      "internal_discriminant_determinant_terms":len(sp.Poly(sp.expand(detD23),*pars).terms()),
      "logic":"T>0 by strict AM-GM; internal diagonal sign is constant because determinant>0 on connected positive orthant and is positive at (1,...,1)",
      "pair_templates":{"endpoint_endpoint":1,"endpoint_internal":6,"internal_internal":3},
      "conclusion":"all ten Rayleigh differences nonnegative; polynomial real stable"}
    Path(__file__).with_name('theta_six_weight_apex_stability_exact_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
