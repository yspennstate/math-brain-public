from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time
RUN=Path(__file__).resolve().parents[1]
spec=json.loads((RUN/'out/FROZEN_TENSOR_SPEC.json').read_text())
checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
def mul(a,b,L):
 return [sum((a[j]*b[i-j] for j in range(i+1)),F(0)) for i in range(L+1)]
def power(a,k,L):
 r=[F(1)]+[F(0)]*L
 while k:
  if k&1:r=mul(r,a,L)
  k//=2
  if k:a=mul(a,a,L)
 return r
def row_low(n,m,L):
 e=F(1,1<<(n-1));a=(1-e)**2
 P=[a]+[e*e*comb(n,j) for j in range(1,L+1)]
 spectators=power(P,m-1,L)
 mu=[e*comb(n-1,j) if j<n else F(0) for j in range(L+1)]
 q=[a+e*e]+[2*e*e*comb(n-1,j) if j<n else F(0) for j in range(1,L+1)]
 return sum(mul(mu,spectators,L)),sum(mul(q,spectators,L))
def walsh(a):
 a=a[:];d=1
 while d<len(a):
  for b in range(0,len(a),2*d):
   for j in range(b,b+d):
    u,v=a[j],a[j+d];a[j],a[j+d]=u+v,u-v
  d*=2
 return a
t0=time.perf_counter();rows=[]
for n in (2,3):
 for m in (2,3):
  N=n*m;vals=[(-1)**sum(((x>>(b*n))&((1<<n)-1))==0 for b in range(m)) for x in range(1<<N)]
  w=walsh(vals);p=[F(c*c,1<<(2*N)) for c in w];e=F(1,1<<(n-1));ck(all(x>0 for x in p));ck(sum(p)==1)
  for L in (0,1,2):
   predicted_mu,predicted_q=row_low(n,m,L)
   for i in range(N):
    bit=1<<i;lower=[s for s in range(1<<N) if not s&bit]
    ck(sum(p[s|bit] for s in lower)==e)
    ck(F(sum(vals[x]!=vals[x^bit] for x in range(1<<N)),1<<N)==e)
    ck(sum(p[s|bit]/e for s in lower if s.bit_count()<=L)==predicted_mu)
    ck(sum(p[s]+p[s|bit] for s in lower if s.bit_count()<=L)==predicted_q)
    ck(sum(p[s]+p[s|bit] for s in lower)==1)
   rows.append(dict(kind='finite',n=n,m=m,L=L,N=N,status='PASS'))
for n in (6,8,12,20):
 m=1<<(n//2);e=F(1,1<<(n-1));a=(1-e)**2
 ck(m*e<=F(1,4));ck(m-1>=F(m,2));ck(2*(n-1)*e<=1)
 for L in (0,1,2):
  ck(n>=2*L+2)
  beta=e*sum(comb(n-1,j) for j in range(L+1))
  low_mu,low_q=row_low(n,m,L)
  z=e*e*sum(comb(n,j) for j in range(L+1,n+1));event=(m-1)*z*a**(m-2)
  ck(z>=e);ck(a**(m-2)>=F(1,2));ck(1-low_q>=event)
  ck(event>=m*e/4);ck(1-low_q>=F(1,1<<((n+1)//2+1)))
  ck(low_mu<=beta)
  lower=F(n//2-2)-beta*(n-1)
  rows.append(dict(kind='symbolic',n=n,m=m,L=L,N=n*m,I=str(n*m*e),coarse_M_over_I_at_least=str(lower),true_M_over_I_at_most='2',full_support=True,status='PASS'))
ck(len(rows)==24)
result=dict(status='PASS',cases=24,assertions=checks,failures=0,runtime_seconds=time.perf_counter()-t0,rows=rows,full_FEI='OPEN',arithmetic='Integer/Fraction exact low-degree generating polynomials and direct physical truth tables')
(RUN/'out/TENSOR.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
