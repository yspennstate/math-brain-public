from fractions import Fraction as R
from math import factorial
from itertools import permutations
from collections import Counter
from bisect import bisect_left
from pathlib import Path
import json, random, time

N=7
zero=lambda:[R(0)]*(N+1)
def const(x):
 a=zero();a[0]=R(x);return a
def sub(a,b):return [x-y for x,y in zip(a,b)]
def mul(a,b):
 c=zero()
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:N+1-i]):
    if y:c[i+j]+=x*y
 return c
def inv(a):
 assert a[0]
 b=zero();b[0]=1/a[0]
 for n in range(1,N+1):b[n]=-sum(a[j]*b[n-j] for j in range(1,n+1))/a[0]
 return b
def det(M):
 M=[[a[:] for a in row] for row in M];ans=const(1)
 for i in range(len(M)):
  pivot=next(j for j in range(i,len(M)) if M[j][i][0])
  if pivot!=i:M[i],M[pivot]=M[pivot],M[i];ans=[-x for x in ans]
  ans=mul(ans,M[i][i]);pinv=inv(M[i][i])
  for j in range(i+1,len(M)):
   fac=mul(M[j][i],pinv)
   for k in range(i+1,len(M)):M[j][k]=sub(M[j][k],mul(fac,M[i][k]))
 return ans
def p(u,y,x):
 c=zero()
 if 0<=y-x<=N:c[y-x]=u**(y-x)/factorial(y-x)
 return c
def E(u,a,b):
 return [u**n/R(factorial(n)*factorial(a+n-b)) if a+n>=b else R(0) for n in range(N+1)]
def formula(obs):
 merged={}
 for t,k in obs:
  if t:merged[t]=min(k,merged.get(t,k))
 ts=sorted(merged)
 if not ts:return const(1),0
 ks=[min(merged[s] for s in ts[i:]) for i in range(len(ts))]
 T=ts[-1];d=ks[-1]-1
 if not d:return const(1),0
 markers=[(t,x) for t,k in zip(ts[:-1],ks[:-1]) for x in range(d-k+1)]
 A=[[E(T,i,j) for j in range(d)] for i in range(d)]
 F=[[p(t,x,i) for t,x in markers] for i in range(d)]
 G=[[E(T-t,x,j) for j in range(d)] for t,x in markers]
 Q=[[p(s-t,y,x) if t<s else zero() for s,y in markers] for t,x in markers]
 M=[A[i]+F[i] for i in range(d)]+[ [[-v for v in a] for a in G[i]+Q[i]] for i in range(len(markers))]
 return det(M),len(M)

def profiles(n):
 ans=[];ph=Counter();qh=Counter();qcounts=Counter()
 for perm in permutations(range(1,n+1)):
  tops=[];lens=[0];birth=[]
  for j,x in enumerate(perm,1):
   i=bisect_left(tops,x)
   if i==len(tops):tops.append(x);birth.append(j)
   else:tops[i]=x
   lens.append(len(tops))
  ans.append(tuple(lens));ph[tuple(tops)]+=1;qh[tuple(birth)]+=1
  if len(tops)>=3:qcounts[tuple(tops[:3])]+=1
 assert ph==qh,('P/Q joint mismatch',n)
 return Counter(ans),qcounts
def compositions(n,r):
 if r==1:yield(n,);return
 for h in range(n+1):
  for tail in compositions(n-h,r-1):yield(h,)+tail
def enumeration(obs,profs):
 positive=[(t,k) for t,k in obs if t]
 if not positive:return const(1)
 ts=sorted(set(t for t,k in positive));T=ts[-1]
 # Original constraints retained; no suffix-min preprocessing on this branch.
 ks=[min(k for s,k in positive if s==t) for t in ts]
 ds=[t-s for s,t in zip([R(0)]+ts,ts)]
 result=zero()
 for n in range(N+1):
  for hs in compositions(n,len(ts)):
   cuts=[];c=0
   for h in hs:c+=h;cuts.append(c)
   count=sum(m for lengths,m in profs[n].items() if all(lengths[c]<k for c,k in zip(cuts,ks)))
   weight=R(count,factorial(n))
   for dt,h in zip(ds,hs):weight*=dt**h/factorial(h)
   result[n]+=weight
 return result

start=time.time();profs=[];atoms={}
for n in range(N+1):
 profiles_n,q=profiles(n);profs.append(profiles_n)
 if n:atoms[n]=q
print('Exact P/Q first-row joint distributions agree for n=0,...,7',flush=True)
cases=[[],[(0,8)],[(R(2),1)],[(R(3,2),2)],[(R(4,3),4)],
 [(R(1,3),1),(R(2,3),2),(R(5,3),3)],
 [(R(1,2),3),(R(1,2),2),(R(1),4)],
 [(R(1,4),5),(R(1,2),2),(R(3,4),4),(R(1),3)],
 [(R(1,5),2),(R(2,5),3),(R(3,5),4),(R(4,5),5),(R(1),6)],
 [(R(1,4),1),(R(1,2),1),(R(1),5)],
 [(R(1,3),4),(R(2,3),4),(R(1),4)]]
rng=random.Random(22008)
for _ in range(10):
 cases.append([(R(i,4),rng.randrange(1,7)) for i in rng.sample(range(1,7),rng.randrange(2,5))])
checks=[]
for i,case in enumerate(cases):
 got,size=formula(case);expected=enumeration(case,profs)
 assert got==expected,(case,got,expected)
 checks.append({'observations':[(str(t),k) for t,k in case],'matrix_size':size,'coefficients':[str(x) for x in got]})
 print(f'Case {i+1}/{len(cases)}: exact coefficients 0..7 agree; size {size}',flush=True)

# Independently verify all triple-density Taylor coefficients through total degree 4.
import sympy as sp
g,h=sp.symbols('g h')
L=lambda j,v:sum(v**n/sp.Integer(factorial(n)*factorial(n+j)) for n in range(5))
C=sp.Poly(sp.expand(L(1,g+h)*(L(1,h)-L(2,h))+(L(3,g+h)-L(2,g+h))*L(0,h)),g,h)
density=[]
for r in range(5):
 for s in range(5-r):
  n=r+s+3;q=R(atoms[n][(1,r+2,n)],factorial(n))
  expected=q/(factorial(r)*factorial(s));got=C.coeff_monomial(g**r*h**s)
  assert got==sp.Rational(expected.numerator,expected.denominator)
  density.append({'r':r,'s':s,'coefficient':str(expected)})
mixed=R(1,6)*R(11,120)-R(1,8)**2
logmixed=mixed/R(1,6)**2
conditional=(R(1,8)*R(1,2)-R(1,6)*R(1,3))/R(1,2)**2
assert (mixed,logmixed,conditional)==(R(-1,2880),R(-1,80),R(1,36))
result={'degree':N,'P_Q_joint_checks':'all permutations n<=7','cases':checks,'density':density,'non_markov_constants':[str(x) for x in (mixed,logmixed,conditional)],'elapsed_seconds':time.time()-start}
Path(__file__).with_name('independent_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('All checks passed, elapsed',result['elapsed_seconds'],flush=True)
