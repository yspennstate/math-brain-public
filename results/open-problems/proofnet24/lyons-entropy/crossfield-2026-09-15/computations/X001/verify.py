"""Exact verification for the arbitrary-guide fractional-background identity.

No numerical Hessian differentiation or finite sampling is used for claims.
The computations verify one rational six-site example and the determinant
combinatorics behind the dimension-independent bound. The report supplies
proofs for the universal assertions.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
checks=0

def eq(a,b):
    global checks
    assert a==b, (a,b)
    checks+=1

def frac(x):
    x=s.cancel(s.expand_complex(x))
    assert x.is_Rational, x
    return F(int(x.p),int(x.q))

def atoms(K):
    n=K.rows
    ans={}
    for mask in range(1<<n):
        Q=K-s.diag(*[0 if mask>>i&1 else 1 for i in range(n)])
        ans[mask]=(-1)**(n-mask.bit_count())*frac(Q.det(method='domain-ge'))
    eq(sum(ans.values()),F(1))
    return ans

def jets(K,A):
    p=atoms(K);plus=atoms(K+A);minus=atoms(K-A)
    return {x:(p[x],(plus[x]-minus[x])/2,plus[x]+minus[x]-2*p[x]) for x in p}

def addlog(table,p,coefficient):
    if not coefficient:return
    assert p>0
    for z,sgn in [(p.numerator,1),(p.denominator,-1)]:
        for prime,exp in s.factorint(z).items():
            prime=int(prime)
            table[prime]=table.get(prime,F(0))+sgn*int(exp)*coefficient
            if not table[prime]:del table[prime]

def addtable(target,source,scale=F(1)):
    for prime,c in source.items():
        target[prime]=target.get(prime,F(0))+scale*c
        if not target[prime]:del target[prime]

def entropy(ps):
    out={}
    for p in ps.values():
        if p:addlog(out,p,-p)
    return out

def curvature(js):
    fisher=F(0);logpart={}
    for p,q,r in js.values():
        if not p:
            eq(q,F(0));eq(r,F(0));continue
        assert p>0
        fisher+=q*q/p
        addlog(logpart,p,r)
    return fisher,logpart

def log_interval(x,terms=80):
    assert x>0
    scale=0
    while x>=2:x/=2;scale+=1
    while x<1:x*=2;scale-=1
    def base(z):
        y=(z-1)/(z+1);v=y;total=F(0)
        for k in range(terms):
            total+=2*v/F(2*k+1);v*=y*y
        tail=2*v/(F(2*terms+1)*(1-y*y))
        return total,total+tail
    lo,hi=base(x);l2,h2=base(F(2))
    return (lo+scale*l2,hi+scale*h2) if scale>=0 else (lo+scale*h2,hi+scale*l2)

def value_interval(r,logs):
    lo=hi=r
    for prime,c in logs.items():
        a,b=log_interval(F(prime))
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi

V=s.Matrix([[1,2],[2,1],[2,-2]])/3
eq(V.T*V,s.eye(2))
T=s.Matrix([[s.Rational(2,5),s.Rational(1,10)+s.I/20],[s.Rational(1,10)-s.I/20,s.Rational(3,5)]])
E=s.Matrix([[s.Rational(1,7),s.Rational(1,30)+s.I/42],[s.Rational(1,30)-s.I/42,s.Rational(1,5)]])
assert frac(T.det())>0 and frac((s.eye(2)-T).det())>0
assert T[0,0]>0 and 1-T[0,0]>0
assert E[0,0]>0 and frac(E.det())>0
assert T*E!=E*T
M=V*T*V.T;D=V*E*V.T
m=3;n=2*m
K=s.zeros(n);A=s.zeros(n)
for i in range(m):
    for j in range(m):
        for a in range(2):
            for b in range(2):
                K[2*i+a,2*j+b]=M[i,j]/2+(s.Rational(1,4)*(-1)**(a+b) if i==j else 0)
                A[2*i+a,2*j+b]=D[i,j]/2
jphysical=jets(K,A)
jlatent=jets(M,D)
C={0:{0:F(1,2),1:F(1,4),2:F(1,4),3:F(0)},
   1:{0:F(0),1:F(1,4),2:F(1,4),3:F(1,2)}}
for mask in range(1<<n):
    expected=[F(0)]*3
    for bits,j in jlatent.items():
        weight=F(1)
        for i in range(m):weight*=C[(bits>>i)&1][(mask>>(2*i))&3]
        for k in range(3):expected[k]+=weight*j[k]
    eq(jphysical[mask],tuple(expected))

hphysical=entropy({x:j[0] for x,j in jphysical.items()})
fphysical,lphysical=curvature(jphysical)
haverage={2:F(3*m,2)};faverage=F(0);laverage={}
minor_sum=F(0);weighted_gram=F(0)
for mask in range(1<<m):
    rows=[i for i in range(m) if mask>>i&1]
    MR=M.extract(rows,rows);DR=D.extract(rows,rows)
    js=jets(MR,DR)
    hs=entropy({x:j[0] for x,j in js.items()});f,ls=curvature(js)
    addtable(haverage,hs,F(1,1<<m));faverage+=f/F(1<<m);addtable(laverage,ls,F(1,1<<m))
    VR=V.extract(rows,[0,1]);gram=frac((VR.T*VR).det())
    weighted_gram+=gram/F(1<<m)
    if len(rows)==2:minor_sum+=gram
    rhs=sum(frac(V.extract(list(pair),[0,1]).det())**2 for pair in combinations(rows,2))
    eq(gram,rhs)
eq(hphysical,haverage);eq(fphysical,faverage);eq(lphysical,laverage)
eq(minor_sum,F(1));eq(weighted_gram,F(1,4))

# Verify the exact Hessian lower bound (2 - log(2)/4) det(E) for m=3.
delta=frac(E.det());boundlogs={2:-delta/F(4)};boundr=2*delta
reslogs=dict(lphysical);addtable(reslogs,boundlogs,-1)
reslo,reshi=value_interval(fphysical-boundr,reslogs)
assert reslo>0
checks+=1
cvlo,cvhi=value_interval(fphysical,lphysical)

# Local three-site realizations for unequal background eigenvalues.
local_erasure_checks=[]
for lam in [s.Rational(1,5),s.Rational(1,3),s.Rational(1,2),s.Rational(2,3),s.Rational(4,5)]:
    if lam<=s.Rational(1,2):
        v=s.Matrix([1/s.sqrt(2),1/s.sqrt(2),0])
        u=s.Matrix([s.sqrt(lam/(2*(1-lam))),-s.sqrt(lam/(2*(1-lam))),s.sqrt((1-2*lam)/(1-lam))])
    else:
        u=s.Matrix([1/s.sqrt(2),1/s.sqrt(2),0])
        v=s.Matrix([s.sqrt((1-lam)/(2*lam)),-s.sqrt((1-lam)/(2*lam)),s.sqrt((2*lam-1)/lam)])
    eq(s.simplify((u.T*u)[0]),s.Integer(1));eq(s.simplify((v.T*v)[0]),s.Integer(1));eq(s.simplify((u.T*v)[0]),s.Integer(0))
    c0=atoms(lam*v*v.T);c1=atoms(u*u.T+lam*v*v.T)
    erasure=min(frac(lam),1-frac(lam));common=F(0)
    for mask in c0:
        if c0[mask] and c1[mask]:eq(c0[mask],c1[mask]);common+=c0[mask]
    eq(common,erasure)
    eq(sum(p for mask,p in c0.items() if not c1[mask]),1-erasure)
    eq(sum(p for mask,p in c1.items() if not c0[mask]),1-erasure)
    local_erasure_checks.append({'lambda':str(lam),'erasure':str(erasure)})

# Arbitrary retention form of the exterior-moment identity.
ta=[F(4,5),F(2,3),F(1,2)]
weighted=F(0)
for mask in range(1<<m):
    rows=[i for i in range(m) if mask>>i&1]
    w=F(1)
    for i in range(m):w*=ta[i] if i in rows else 1-ta[i]
    VR=V.extract(rows,[0,1]);weighted+=w*frac((VR.T*VR).det())
eq(weighted,frac((V.T*s.diag(*[s.Rational(x.numerator,x.denominator) for x in ta])*V).det()))

result={
 'status':'PASS', 'exact_assertions':checks,
 'physical_dimension':n,'guide_count':m,
 'physical_rank':m+2,'latent_rank':2,
 'noncommuting_base_and_direction':True,
 'positive_atoms':sum(j[0]>0 for j in jphysical.values()),
 'fisher_exact':str(fphysical),
 'det_direction':str(delta),
 'hessian_negative_lower':str(cvlo),
 'hessian_negative_upper':str(cvhi),
 'hessian_negative_decimal':float((cvlo+cvhi)/2),
 'quantitative_surplus_lower':str(reslo),
 'quantitative_surplus_decimal':float((reslo+reshi)/2),
 'entropy_prime_coefficients':{str(p):str(c) for p,c in sorted(hphysical.items())},
 'curvature_prime_coefficients':{str(p):str(c) for p,c in sorted(lphysical.items())},
 'local_erasure_realizations':local_erasure_checks,
 'arbitrary_retention_exterior_moment':str(weighted),
 'scope':'One exact six-site example, five exact local erasure realizations, and exact exterior-moment identities; universal theorems are proved in agents/X001.md.'
}
(ROOT/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['hessian_negative_lower','hessian_negative_upper','quantitative_surplus_lower','entropy_prime_coefficients','curvature_prime_coefficients']},indent=2))
