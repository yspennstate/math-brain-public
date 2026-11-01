#!/usr/bin/env python3
"""Exact seven-orbit certificate for weights (pr,p,p; qr,q,q) on K_{2,3}."""

import json
from pathlib import Path
import sympy as sp


def is_forest(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def enumerate_polynomial(p, q, r, z):
    edges = [(0,j) for j in (2,3,4)] + [(1,j) for j in (2,3,4)]
    weights = [p*r,p,p,q*r,q,q]
    spokes = [(5,i) for i in range(5)]
    polynomial = 0
    count = 0
    for bm in range(64):
        be = [edges[k] for k in range(6) if bm >> k & 1]
        weight = sp.prod(weights[k] for k in range(6) if bm >> k & 1)
        for sm in range(32):
            se = [spokes[k] for k in range(5) if sm >> k & 1]
            if is_forest(6, be + se):
                count += 1
                polynomial += weight * sp.prod(z[k] for k in range(5) if sm >> k & 1)
    return sp.expand(polynomial), count


def rayleigh(P, z, i, j):
    return sp.expand(sp.diff(P,z[i])*sp.diff(P,z[j])-P*sp.diff(P,z[i],z[j]))


def qdata(P, variable):
    a,b,c = sp.Poly(P, variable).all_coeffs()
    return tuple(map(sp.expand,(a,b,c,b*b-4*a*c)))


def main():
    p,q,r = sp.symbols("p q r", positive=True)
    z = sp.symbols("z0:5", real=True)
    x,y = sp.symbols("x y", real=True)
    P, count = enumerate_polynomial(p,q,r,z)

    h = p+q+1
    hs = r*(p+q)+1
    h0,h1 = p*(r+2)+1, q*(r+2)+1
    T = (p+q)*(r+1)+2
    N = 2*p*q+p+q+1
    L = (p**2*q*r**2+p**2*q*r+p**2*r+p*q**2*r**2+p*q**2*r
         +p*q*r**2+2*p*q*r+p*q+p*r+p+q**2*r+q*r+q+1)
    M = (p**2*q*r**2+2*p**2*q*r+p**2*r+p*q**2*r**2+2*p*q**2*r
         +p*q*r**2+2*p*q*r+2*p*q+p*r+p+q**2*r+q*r+q+1)

    phi_a = (p+1)*(q+1)*(x*x+y*y)+2*p*q*x*y
    phi_01 = L*(x*x+y*y)+2*p*q*hs*x*y
    phi_03 = h*N*x*x+2*p*q*r**2*h*x*y+r**2*L*y*y
    phi_23 = (q**2*r*(q+1)*(q*r+1)*x*x + 2*p**2*q**2*r**2*x*y
              +p**2*r*(p+1)*(p*r+1)*y*y)
    phi_34 = q**2*(q+1)**2*x*x+2*p**2*q**2*x*y+p**2*(p+1)**2*y*y
    Eq = p*q*r+2*p*q+2*p*r+p+q**2*r+2*q**2+q*r+5*q+3
    Ep = p**2*r+2*p**2+p*q*r+2*p*q+p*r+5*p+2*q*r+q+3
    K = (p**2*q*r**2+2*p**2*q*r-p**2*r+p*q**2*r**2+2*p*q**2*r
         -p*q*r**2+2*p*q*r-p*r-p-q**2*r-q*r-q-1)
    phi_e = q**2*(q*r+1)*Eq*x*x+2*p*q*K*x*y+p**2*(p*r+1)*Ep*y*y

    checks=[]
    d01=rayleigh(P,z,0,1);a01,_,_,D01=qdata(d01,z[2])
    checks += [sp.expand(a01-p*q*phi_a.subs({x:z[3]+h,y:z[4]+h}))==0,
      sp.expand(D01+4*p**2*q**2*r**2*(z[3]+h)**2*(z[4]+h)**2*phi_01.subs({x:z[3]+h,y:z[4]+h}))==0,
      sp.expand(d01.subs({z[3]:-h,z[4]:-h}))==0]

    for i,name,lead,bound in [
        (0,"02",p*r*(p*r+1),p*q**2*r*(q+1)*T),
        (1,"12",q*r*(q*r+1),p**2*q*r*(p+1)*T)]:
        d=rayleigh(P,z,i,2); other=1-i; a,_,_,D=qdata(d,z[other])
        checks += [sp.expand(a-lead*(z[3]+h)**2*(z[4]+h)**2)==0,
          sp.expand(D-D01)==0,
          sp.expand(d.subs(z[3],-h)-bound*(z[4]+h)**2)==0,
          sp.expand(d.subs(z[4],-h)-bound*(z[3]+h)**2)==0]

    for i,other,lead,bound_s,bound_o in [
        (0,1,p*(p+1),p*q**2*r**2*(q*r+1)*T,2*p*q**2*(q+1)*h),
        (1,0,q*(q+1),p**2*q*r**2*(p*r+1)*T,2*p**2*q*(p+1)*h)]:
        d=rayleigh(P,z,i,3);a,_,_,D=qdata(d,z[other])
        checks += [sp.expand(a-lead*(z[2]+hs)**2*(z[4]+h)**2)==0,
          sp.expand(D+4*p**2*q**2*(z[2]+hs)**2*(z[4]+h)**2*phi_03.subs({x:z[2]+hs,y:z[4]+h}))==0,
          sp.expand(d.subs(z[2],-hs)-bound_s*(z[4]+h)**2)==0,
          sp.expand(d.subs(z[4],-h)-bound_o*(z[2]+hs)**2)==0]

    d23=rayleigh(P,z,2,3);a23,_,_,D23=qdata(d23,z[4])
    checks += [sp.expand(a23-phi_23.subs({x:z[0]+h0,y:z[1]+h1}))==0,
      sp.expand(D23+4*p**2*q**2*r**2*h*phi_e.subs({x:z[0]+h0,y:z[1]+h1}))==0,
      sp.expand(d23.subs({z[0]:-h0,z[1]:-h1})-2*p**2*q**2*r*h*T)==0]

    d34=rayleigh(P,z,3,4);a34,_,_,D34=qdata(d34,z[2])
    checks += [sp.expand(a34-phi_34.subs({x:z[0]+h0,y:z[1]+h1}))==0,
      sp.expand(D34-D23)==0,
      sp.expand(d34.subs({z[0]:-h0,z[1]:-h1})-p**2*q**2*r**2*T**2)==0]

    positivity={
      "phi_a":[(p+1)*(q+1),h*N],
      "phi_01":[L,(p*r+1)*(q*r+1)*h*M],
      "phi_03":[h*N,r**2*(p+1)*(q+1)*h*M],
      "phi_23":[q**2*r*(q+1)*(q*r+1),p**2*q**2*r**2*L],
      "phi_34":[q**2*(q+1)**2,p**2*q**2*h*N],
      "phi_e":[q**2*(q*r+1)*Eq,2*p**2*q**2*T**2*M],
    }
    checks += [all(v.is_positive for v in vals) for vals in positivity.values()]
    assert all(checks),checks
    report={
      "status":"PASS","sympy_version":sp.__version__,
      "enumerated_augmented_forests_at_unit_weights":count,
      "polynomial_terms":len(sp.Poly(P,*z).terms()),
      "rayleigh_pair_orbits_checked":[[0,1],[0,2],[1,2],[0,3],[1,3],[2,3],[3,4]],
      "exact_identity_checks":len(checks),
      "positive_form_certificates":{k:[str(sp.factor(v)) for v in vals] for k,vals in positivity.items()},
      "scope":"K_{2,3} weights (pr,p,p; qr,q,q), with p,q,r>0",
    }
    out=Path(__file__).with_name("theta_three_parameter_apex_stability_exact_results.json")
    out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
