from fractions import Fraction as R
from math import factorial
from itertools import permutations
from bisect import bisect_left
from pathlib import Path
import json,time

N=7
zero=lambda:[R(0)]*(N+1)
def const(x):
 p=zero();p[0]=R(x);return p
def add(a,b):return [x+y for x,y in zip(a,b)]
def neg(a):return [-x for x in a]
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
 for n in range(1,N+1):b[n]=-sum(a[i]*b[n-i] for i in range(1,n+1))/a[0]
 return b
def det(M):
 n=len(M)
 if n==0:return const(1)
 M=[[v[:] for v in row] for row in M];ans=const(1)
 for i in range(n):
  j=next(j for j in range(i,n) if M[j][i][0])
  if j!=i:M[i],M[j]=M[j],M[i];ans=neg(ans)
  pivot=M[i][i];ans=mul(ans,pivot);inverse=inv(pivot)
  for j in range(i+1,n):
   w=mul(M[j][i],inverse)
   for k in range(i+1,n):M[j][k]=add(M[j][k],neg(mul(w,M[i][k])))
   M[j][i]=zero()
 return ans

def normalize(obs):
 at={}
 for t,k in obs:
  t=R(t)
  if t>0:at[t]=min(k,at.get(t,k))
 obs=sorted(at.items())
 ks=[k for t,k in obs]
 for i in range(len(ks)-2,-1,-1):ks[i]=min(ks[i],ks[i+1])
 return [(obs[i][0],ks[i]) for i in range(len(obs))]
def p(t,y,x):
 a=zero()
 if 0<=y-x<=N:a[y-x]=R(t)**(y-x)/factorial(y-x)
 return a
def pair(t,x,b):
 a=zero()
 for n in range(N+1):
  y=x+n
  if y>=b:a[n]=R(t)**n/(factorial(n)*factorial(y-b))
 return a
def block_coeff(obs):
 obs=normalize(obs)
 if not obs:return const(1),0
 T=obs[-1][0];d=obs[-1][1]-1
 markers=[(t,x) for t,k in obs[:-1] for x in range(d-(k-1))]
 q=len(markers)
 if d==0:return const(1),0
 A=[[pair(T,i,j) for j in range(d)] for i in range(d)]
 F=[[p(t,x,i) for t,x in markers] for i in range(d)]
 G=[[pair(T-t,x,j) for j in range(d)] for t,x in markers]
 Q=[[p(s-t,y,x) if t<s else zero() for s,y in markers] for t,x in markers]
 M=[A[i]+F[i] for i in range(d)]+[[neg(v) for v in G[a]]+[neg(v) for v in Q[a]] for a in range(q)]
 return det(M),d+q

def compositions(n,r):
 if r==1:yield (n,);return
 for i in range(n+1):
  for tail in compositions(n-i,r-1):yield(i,)+tail

def lis_prefixes(word):
 tops=[];lengths=[0]
 for x in word:
  i=bisect_left(tops,x)
  if i==len(tops):tops.append(x)
  else:tops[i]=x
  lengths.append(len(tops))
 return lengths
prefixes={n:[lis_prefixes(p) for p in permutations(range(1,n+1))] for n in range(N+1)}

def permutation_coeff(obs):
 # Independent preparation: do NOT apply the suffix-minimum reduction.
 at={}
 for t,k in obs:
  t=R(t)
  if t>0:at[t]=min(k,at.get(t,k))
 obs=sorted(at.items())
 if not obs:return const(1)
 r=len(obs);dt=[obs[0][0]]+[obs[i][0]-obs[i-1][0] for i in range(1,r)]
 result=zero()
 for n in range(N+1):
  for comp in compositions(n,r):
   counts=[];total=0
   for c in comp:total+=c;counts.append(total)
   accepted=sum(all(L[c]<k for c,(t,k) in zip(counts,obs)) for L in prefixes[n])
   w=R(accepted,factorial(n))
   for a,c in zip(dt,comp):w*=a**c/factorial(c)
   result[n]+=w
 return result
cases=[[(2,1)],[(2,2)],[(2,3)],[(2,4)],[(1,1),(2,2)],[(1,2),(2,3)],[(1,1),(2,2),(3,3)],[(1,2),(2,3),(3,4)],[(1,4),(2,2),(3,4)],[(1,2),(2,2),(3,4)],[(1,3),(1,2),(2,4)],[(R(1,2),2),(R(3,2),3),(R(5,2),4)],[(1,1),(2,2),(3,3),(4,4),(5,5)],[(1,3),(2,1)],[(0,1),(1,2)]]
start=time.monotonic();results=[]
for obs in cases:
 block,size=block_coeff(obs);direct=permutation_coeff(obs)
 assert block==direct,(obs,block,direct)
 row={'observations':[(str(t),k) for t,k in obs],'dimension':size,'coefficients':[str(x) for x in block],'result':'PASS'};results.append(row)
 print('PASS',row['observations'],'dimension',size,flush=True)
Path('finite_block_checks.json').write_text(json.dumps({'cutoff_degree':N,'cases':results,'seconds':time.monotonic()-start},indent=2),encoding='utf8')
print('ALL EXACT PERMUTATION / BLOCK CHECKS PASS',time.monotonic()-start)
