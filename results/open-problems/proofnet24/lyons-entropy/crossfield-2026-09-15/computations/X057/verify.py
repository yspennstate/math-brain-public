#!/usr/bin/env python3
"""Exact determinant/Fisher verification of X057's analytic theorem."""
from fractions import Fraction as F
import itertools, json, math
from pathlib import Path
import sympy as s
out=Path(__file__).resolve().parent
checks=0
def ck(v):
 global checks
 assert v
 checks+=1
n=6
v=s.Matrix([1,2,3]); U=s.eye(3)-2*v*v.T/(v.dot(v))
H=s.zeros(n)
H[:3,3:]=U; H[3:,:3]=U.T
K=s.eye(n)/2+s.Rational(5,16)*H
ck(U*U.T==s.eye(3)); ck(H*H==s.eye(n))
L=K*(s.eye(n)-K).inv(); diag=L[0,0]
ck(all(L[i,i]==diag for i in range(n)))
ck(set(L.eigenvals())=={s.Rational(3,13),s.Rational(13,3)})
D=s.diag(*[s.Rational(a,120) for a in [1,-2,3,-4,5,-6]])
xs=list(itertools.product([0,1],repeat=n)); ps={}; rs={}; jets={}
J=s.zeros(n); W=s.zeros(n)
for x in xs:
 B=K-s.diag(*[1-a for a in x]); R=B.inv()
 p=(-1)**(n-sum(x))*B.det(); ck(p>0)
 z=(R*D).trace(); acc=z*z-(R*D*R*D).trace()
 ps[x]=p; rs[x]=R; jets[x]=(p*z,p*acc)
 J+=p*s.Matrix([R[i,i] for i in range(n)])*s.Matrix([R[i,i] for i in range(n)]).T
 W+=p*R.applyfunc(lambda a:a*a)
 for i in range(n):
  ck(sum(R[i,j]**2 for j in range(n) if j!=i)<=s.Rational(4,5)*R[i,i]**2)
ck(sum(ps.values())==1)
ck(sum(p1 for p1,p2 in jets.values())==0)
ck(sum(p2 for p1,p2 in jets.values())==0)
ck(J==W)
pairlog={}; pairfi=s.zeros(n); minR=s.Integer(1)
for i,j in itertools.combinations(range(n),2):
 outside=[h for h in range(n) if h not in [i,j]]
 accfi=0; logs=[]
 for y in itertools.product([0,1],repeat=n-2):
  un=[]
  for xi,xj in itertools.product([0,1],repeat=2):
   x=[0]*n; x[i]=xi; x[j]=xj
   for h,a in zip(outside,y):x[h]=a
   un.append(ps[tuple(x)])
  m=sum(un); a,b,c,d=[z/m for z in un]
  r=a*d/(b*c); t=b*c-a*d
  ff=t*(1/a+1/b+1/c+1/d)
  ck(t>=0); ck(r>=s.Rational(25,169)); ck(ff>=1-r)
  u=a+d; z=t/(a*d)
  ck(ff==z*(1+u*z)/(1+z))
  accfi+=m*ff; logs.append((m,r))
  minR=min(minR,r)
 ck(accfi==J[i,j]); pairfi[i,j]=pairfi[j,i]=accfi
 pairlog[i,j]=logs
for i in range(n):
 ck(J[i,i]>=4)
 ck(sum(J[i,j] for j in range(n) if i!=j)<=s.Rational(4,5)*J[i,i])
# Independent exact determinant polynomial coefficients through t^2.
z=s.Symbol('z')
for x in xs:
 # Multiaffinity evaluates each derivative via the appropriate minor.
 B=K-s.diag(*[1-a for a in x]);sgn=(-1)**(n-sum(x))
 p1=sgn*sum(D[i,i]*B.minor_submatrix(i,i).det() for i in range(n))
 p2=0
 for i,j in itertools.combinations(range(n),2):
  ids=[h for h in range(n) if h not in [i,j]]
  p2+=2*sgn*D[i,i]*D[j,j]*B.extract(ids,ids).det()
 ck((p1,p2)==jets[x])
# Rational enclosure log(169/25)=4 atanh(4/9), with a geometric tail.
a=F(4,9); terms=3
lo=4*sum((a**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
hi=lo+4*a**(2*terms+1)/(F(2*terms+1)*(1-a*a))
beta_lo=F(9,5)-F(169,180)*hi
eta_lo=F(169,144)*lo-1
ck(beta_lo>F(1,200)); ck(eta_lo>1)
# Numerical identity check only; not a sign proof.
fi=sum(float(p1*p1/ps[x]) for x,(p1,p2) in jets.items())
logacc=sum(float(p2)*math.log(float(ps[x])) for x,(p1,p2) in jets.items())
chi=sum(float(D[i,i]**2*J[i,i]) for i in range(n))
qsum=chi
for (i,j),logs in pairlog.items():
 c=sum(float(m)*(-math.log(float(r))) for m,r in logs)
 qsum+=2*float(D[i,i]*D[j,j])*(float(J[i,j])-c)
ck(abs((fi+logacc)-qsum)<1e-12)
res={'status':'PASS','exact_assertions':checks-1,'numerical_identity_assertions':1,
 'beta_lower_rational':str(beta_lo),'beta_rounded':(324-169*math.log(169/25))/180,
 'center_odds_condition_number':str(s.Rational(169,9)),
 'min_conditional_odds_ratio':str(minR),'negative_entropy_curvature':fi+logacc,
 'chi_energy':chi,'determinant_vs_pair_error':abs(fi+logacc-qsum),
 'kernel':[[str(K[i,j]) for j in range(n)] for i in range(n)]}
(out/'results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='kernel'},indent=2))
