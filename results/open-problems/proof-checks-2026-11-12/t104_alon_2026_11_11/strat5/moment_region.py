"""PROVED: exact rational moment polytope and its scale threshold.

No linear-programming tolerances enter this script: all vertices are
enumerated by exact 3-by-3 solves and checked against every inequality.
"""
import itertools,json
import sympy as s
AA,BB,CC=s.symbols('A B C')
r=s.symbols('r')
ineq=[([-1,0,0],-s.Rational(7,30)),([0,-1,0],-s.Rational(7,30)),
      ([1,0,0],s.Rational(13,20)),([0,1,0],s.Rational(13,20)),
      ([0,0,-1],0),([0,0,1],s.Rational(3,10)),
      ([1,0,1],s.Rational(4,5)),([0,1,1],s.Rational(4,5)),
      ([1,1,2],s.Rational(7,5)),([-1,-1,2],0),
      ([-1,0,-1],-s.Rational(1,4)),([0,-1,-1],-s.Rational(1,4))]
vertices=set()
for inds in itertools.combinations(range(len(ineq)),3):
    mat=s.Matrix([ineq[i][0] for i in inds])
    if not mat.det(): continue
    v=mat.inv()*s.Matrix([ineq[i][1] for i in inds])
    if all((s.Matrix([row])*v)[0]<=rhs for row,rhs in ineq): vertices.add(tuple(v))
vertices=sorted(vertices)
assert vertices
print('PROVED: exact moment-polytope vertices',len(vertices),flush=True)
with open('moment_vertices.json','w') as out:json.dump([[str(x) for x in v] for v in vertices],out,indent=2)
def lh(v,low):
    A,B,C=v
    f=A+r*B+(1+r)*C-(1+r)/5
    L=s.Rational(14,9)*f
    cr=(1-7*r)*(9+r)/24 if low else 0
    h=2*(1+r)*f/9+s.Rational(4,3)*(1+r*r)-s.Rational(14,3)*(A+r*r*B)-4*(1+r*r+r/3)*C-cr*C
    return s.factor(L),s.factor(h)
for rr in [0,s.Rational(1,20),s.Rational(1,10),s.Rational(1,7),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),1]:
    candidates=[]
    for v in vertices:
        L,h=lh(v,rr<s.Rational(1,7))
        ll=L.subs(r,rr)
        hh=h.subs(r,rr) if hasattr(h,'subs') else h
        if hh<0: candidates.append((-ll/hh,v))
    threshold,v=min(candidates)
    print('PROVED: r =',rr,'scale threshold =',threshold,'vertex =',v,flush=True)
# Exact proof of a uniform region: every endpoint polynomial is nonnegative.
def nonnegative_quadratic(expr,lo,hi):
    poly=s.Poly(s.expand(expr),r)
    assert poly.degree()<=2
    vals=[poly.eval(lo),poly.eval(hi)]
    if poly.degree()==2 and poly.nth(2)>0:
        crit=-poly.nth(1)/(2*poly.nth(2))
        if lo<=crit<=hi:vals.append(poly.eval(crit))
    return min(vals)>=0
for scale in [s.Rational(4,11),s.Rational(9,20),s.Rational(5,11)]:
    ok=True
    for low,lo,hi in [(True,0,s.Rational(1,7)),(False,s.Rational(1,7),1)]:
        for v in vertices:
            L,h=lh(v,low)
            if not nonnegative_quadratic(L+scale*h,lo,hi):ok=False
    print('PROVED: uniform a<= '+str(scale) if ok else 'NUMERICAL: this relaxation does not prove uniform a<= '+str(scale),flush=True)
