#!/usr/bin/env python3
"""Independent exact audit of arbitrary-positive-weight K_{2,3} apex stability."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from random import Random
import json
import sympy as sp

OUT = Path(__file__).with_name("theta_six_weight_apex_stability_k_independent.json")
SEED = 1003202606


def component_polynomial(weights, z):
    a,b,c,d,e,f = weights
    edges=[(0,2,a),(0,3,b),(0,4,c),(1,2,d),(1,3,e),(1,4,f)]
    answer=0; accepted=0
    for mask in range(64):
        parent=list(range(5))
        def root(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        weight=1; bad=False
        for index,(u,v,w) in enumerate(edges):
            if mask>>index&1:
                u,v=root(u),root(v)
                if u==v: bad=True; break
                parent[u]=v; weight*=w
        if bad: continue
        accepted+=1; components=defaultdict(list)
        for vertex in range(5): components[root(vertex)].append(vertex)
        for component in components.values():
            weight*=1+sum(z[vertex] for vertex in component)
        answer+=weight
    return sp.expand(answer),accepted


def rayleigh(P,z,i,j):
    return sp.expand(sp.diff(P,z[i])*sp.diff(P,z[j])-P*sp.diff(P,z[i],z[j]))


def quadratic_data(P,var):
    a,b,c=sp.Poly(P,var).all_coeffs()
    return tuple(map(sp.expand,(a,b,c,b*b-4*a*c)))


def coeff_positive(P,variables):
    return all(value>0 for value in sp.Poly(P,*variables).coeffs())


def H(u,v,r,s):
    return (u*v*r+u*v*s+u*v+u*r*s+u*r+u*s+u
            +v*r*s+v*r+v*s+v+r*s+r+s+1)


def T(u,v,r,s):
    # Columns (u,r),(v,s): the diagonal pairing is crossed.
    return u*s*(u+1)*(s+1)+v*r*(v+1)*(r+1)-2*u*v*r*s


def canonical(labels):
    names={}; return tuple(names.setdefault(x,len(names)) for x in labels)


def join(partition,u,v):
    if partition[u]==partition[v]: return None
    left,right=partition[u],partition[v]
    return canonical(left if x==right else x for x in partition)


def direct_marked(weights,beta,rows):
    a,b,c,d,e,f=map(Fraction,weights); n=5
    edges=[(0,2,a),(0,3,b),(0,4,c),(1,2,d),(1,3,e),(1,4,f)]
    edges += [(n+r,x,Fraction(rows[r])*Fraction(beta[x]))
              for r in range(4) for x in range(5) if rows[r]*beta[x]]
    states={tuple(range(9)):Fraction(1)}
    for u,v,w in edges:
        following=defaultdict(Fraction)
        for partition,mass in states.items():
            following[partition]+=mass
            target=join(partition,u,v)
            if target is not None: following[target]+=w*mass
        states=dict(following)
    out=[Fraction(0)]*4
    for partition,mass in states.items():
        for mask in range(4):
            target=partition
            if mask&1: target=join(target,5,6)
            if target is not None and mask&2: target=join(target,7,8)
            if target is not None: out[mask]+=mass
    return out


def root_cases(P,weights,z,count=24):
    rng=Random(SEED); s=sp.symbols('s',real=True); records=[]
    for trial in range(count):
        values=[sp.Rational(rng.randrange(1,9),rng.randrange(1,7)) for _ in range(6)]
        beta=[sp.Rational(rng.randrange(0,7),rng.randrange(1,6)) for _ in range(5)]
        if not any(beta): beta[trial%5]=1
        substitutions=dict(zip(weights,values)); substitutions.update({z[i]:s*beta[i] for i in range(5)})
        poly=sp.Poly(P.subs(substitutions),s,domain=sp.QQ)
        degree=sum(1 for x in beta if x>0); negative=0
        _,factors=sp.sqf_list(poly)
        for factor,multiplicity in factors:
            negative+=multiplicity*factor.count_roots(-sp.oo,0)
        assert poly.degree()==degree==negative
        records.append({'trial':trial,'weights':list(map(str,values)),
                        'profile':list(map(str,beta)),'degree':degree,
                        'negative_roots_counting_multiplicity':int(negative)})
    return records


def rational_stress(P,weights,z,trials=100):
    rng=Random(SEED+1); rows=[]
    for exponents,coefficient in sp.Poly(P,*z).terms():
        mask=sum(1<<i for i,e in enumerate(exponents) if e); rows.append((mask,coefficient))
    def value(numeric,point,i,j):
        total=di=dj=dij=sp.Rational(0)
        for mask,coefficient in numeric:
            term=coefficient
            for k in range(5):
                if mask>>k&1: term*=point[k]
            total+=term
            if mask>>i&1:
                term=coefficient
                for k in range(5):
                    if k!=i and mask>>k&1: term*=point[k]
                di+=term
            if mask>>j&1:
                term=coefficient
                for k in range(5):
                    if k!=j and mask>>k&1: term*=point[k]
                dj+=term
            if mask>>i&1 and mask>>j&1:
                term=coefficient
                for k in range(5):
                    if k not in (i,j) and mask>>k&1: term*=point[k]
                dij+=term
        return sp.factor(di*dj-total*dij)
    minimum=None
    for _ in range(trials):
        parameters=[sp.Rational(rng.randrange(1,10),rng.randrange(1,7)) for _ in range(6)]
        numeric=[(mask,sp.Rational(coefficient.subs(dict(zip(weights,parameters))))) for mask,coefficient in rows]
        point=[sp.Rational(rng.randrange(-12,13),rng.randrange(1,7)) for _ in range(5)]
        for i,j in combinations(range(5),2):
            current=value(numeric,point,i,j); assert current>=0
            minimum=current if minimum is None or current<minimum else minimum
    return {'specializations':trials,'pair_evaluations':10*trials,'minimum':str(minimum)}


def main():
    a,b,c,d,e,f=sp.symbols('a b c d e f',positive=True); weights=(a,b,c,d,e,f)
    z=sp.symbols('z0:5',real=True); x,y=sp.symbols('x y',real=True)
    P,backbone_forests=component_polynomial(weights,z)
    assert backbone_forests==54 and len(sp.Poly(P,*z).terms())==32
    assert P.subs({**{w:1 for w in weights},**{v:1 for v in z}})==712
    for coefficient in sp.Poly(P,*z).coeffs(): assert coeff_positive(coefficient,weights)

    xb,xc=z[3]+1+b+e,z[4]+1+c+f
    # Endpoint--endpoint template.
    d01=rayleigh(P,z,0,1); lead01,_,_,disc01=quadratic_data(d01,z[2])
    phi=c*f*(c+1)*(f+1)*x*x+2*b*c*e*f*x*y+b*e*(b+1)*(e+1)*y*y
    psi=(c*f*H(a,c,d,f)*x*x+2*b*c*e*f*(a+d+1)*x*y
         +b*e*H(a,b,d,e)*y*y)
    psi_poly=sp.Poly(psi,x,y); psix=psi_poly.coeff_monomial(x*x)
    psixy=psi_poly.coeff_monomial(x*y); psiy=psi_poly.coeff_monomial(y*y)
    qpoly=sp.cancel((psix*psiy-(psixy/2)**2)/(b*c*e*f*(a+1)*(d+1)))
    assert coeff_positive(qpoly,weights)
    checks=[
      sp.expand(lead01-phi.subs({x:xb,y:xc}))==0,
      sp.expand(disc01+4*a*d*xb*xb*xc*xc*psi.subs({x:xb,y:xc}))==0,
      sp.expand(d01.subs({z[3]:-1-b-e,z[4]:-1-c-f}))==0,
      sp.expand(c*f*(c+1)*(f+1)*b*e*(b+1)*(e+1)-(b*c*e*f)**2-b*c*e*f*H(b,c,e,f))==0,
    ]

    # Endpoint--internal; explicitly check both axes for both rows.
    d02=rayleigh(P,z,0,2); lead02,_,_,disc02=quadratic_data(d02,z[1])
    checks += [sp.expand(lead02-a*(a+1)*xb*xb*xc*xc)==0,
      sp.expand(disc02-disc01)==0,
      sp.expand(d02.subs(z[3],-1-b-e)-e*(e+1)*T(a,b,d,e)*xc*xc)==0,
      sp.expand(d02.subs(z[4],-1-c-f)-f*(f+1)*T(a,c,d,f)*xb*xb)==0]
    d12=rayleigh(P,z,1,2); lead12,_,_,disc12=quadratic_data(d12,z[0])
    checks += [sp.expand(lead12-d*(d+1)*xb*xb*xc*xc)==0,
      sp.expand(disc12-disc01)==0,
      sp.expand(d12.subs(z[3],-1-b-e)-b*(b+1)*T(a,b,d,e)*xc*xc)==0,
      sp.expand(d12.subs(z[4],-1-c-f)-c*(c+1)*T(a,c,d,f)*xb*xb)==0]

    # Internal--internal; collect in the unused arm.
    u0,u1=z[0]+1+a+b+c,z[1]+1+d+e+f
    d23=rayleigh(P,z,2,3); lead23,_,_,disc23=quadratic_data(d23,z[4])
    theta=d*e*(d+1)*(e+1)*x*x+2*a*b*d*e*x*y+a*b*(a+1)*(b+1)*y*y
    omega=sp.expand((-disc23/4).subs({z[0]:x-1-a-b-c,z[1]:y-1-d-e-f}))
    op=sp.Poly(omega,x,y); ox=op.coeff_monomial(x*x); oxy=op.coeff_monomial(x*y); oy=op.coeff_monomial(y*y)
    assert len(op.terms())==3
    detomega=sp.expand(ox*oy-(oxy/2)**2)
    checks += [sp.expand(lead23-theta.subs({x:u0,y:u1}))==0,
      sp.expand(disc23+4*omega.subs({x:u0,y:u1}))==0,
      sp.expand(detomega-a*b*c*d*e*f*T(a,b,d,e)*T(a,c,d,f)*T(b,c,e,f)*qpoly)==0,
      sp.expand(d23.subs({z[0]:-1-a-b-c,z[1]:-1-d-e-f})-T(a,c,d,f)*T(b,c,e,f))==0,
      sp.expand(d*e*(d+1)*(e+1)*a*b*(a+1)*(b+1)-(a*b*d*e)**2-a*b*d*e*H(a,b,d,e))==0]
    base={w:1 for w in weights}
    assert ox.subs(base)>0 and oy.subs(base)>0 and detomega.subs(base)>0
    assert all(checks),checks

    stress=rational_stress(P,weights,z); roots=root_cases(P,weights,z)
    rows=[Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(4,5)]
    marked_inputs=[
      ((1,2,3,4,5,6),[1,2,0,0,0]),((Fraction(2,3),Fraction(5,2),1,3,2,4),[0,1,3,0,0]),
      ((Fraction(7,4),Fraction(1,5),2,Fraction(5,3),Fraction(1,4),3),[0,0,1,2,0]),
      ((3,4,Fraction(5,3),Fraction(2,5),Fraction(7,2),1),[1,0,0,0,5]),
      ((1,3,Fraction(7,2),2,Fraction(4,5),5),[2,0,0,0,0]),
      ((Fraction(5,4),2,Fraction(1,7),3,Fraction(5,2),4),[0,0,0,0,0])]
    marked=[]
    for ws,beta in marked_inputs:
        coeff=direct_marked(ws,beta,rows); diff=coeff[1]*coeff[2]-coeff[0]*coeff[3]
        strict=sum(v>0 for v in beta)>=2; assert diff>=0 and (diff>0)==strict
        marked.append({'weights':list(map(str,ws)),'profile':list(map(str,beta)),
                       'EF_minus_AC':str(diff),'strict':strict})
    report={'status':'PASS; independent six-weight exact audit','backbone_forests':54,
      'polynomial_terms':32,'generic_symbolic_checks':len(checks),
      'Q_positive_terms':len(sp.Poly(qpoly,*weights).terms()),
      'internal_form_basepoint':{'A':str(ox.subs(base)),'B':str((oxy/2).subs(base)),
                                 'C':str(oy.subs(base)),'det':str(detomega.subs(base))},
      'endpoint_internal_boundaries':{
        'Delta02_Xb0':str(sp.factor(e*(e+1)*T(a,b,d,e))),
        'Delta02_Xc0':str(sp.factor(f*(f+1)*T(a,c,d,f))),
        'Delta12_Xb0':str(sp.factor(b*(b+1)*T(a,b,d,e))),
        'Delta12_Xc0':str(sp.factor(c*(c+1)*T(a,c,d,f)))},
      'rational_stress':stress,'root_cases':roots,'direct_marked_cases':marked,
      'summary':{'symbolic_checks':len(checks),'exact_pair_evaluations':stress['pair_evaluations'],
                 'root_cases':len(roots),'marked_cases':len(marked),
                 'strict_marked':sum(x['strict'] for x in marked),
                 'equality_marked':sum(not x['strict'] for x in marked),'counterexamples':0}}
    OUT.write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report['summary'],indent=2))

if __name__=='__main__': main()
