from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def ck(v):
 global checks
 checks+=1; assert v,checks
 assert time.perf_counter()-start<55
def fwht(a):
 a=a[:]; k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(i,i+k): a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return a
saved=json.loads((ROOT/'out/validation.json').read_text(encoding='utf-8'))
for row in saved['family']:
 m=row['m']; t=row['parent_truth_table']; w=fwht(t)
 ck(all(abs(a)==2**m for a in w)); ck(fwht(w)==[len(t)*a for a in t])
 for leaf in row['leaves']:
  t=leaf['truth_table']; w=fwht(t); ck(w==leaf['walsh_integers'])
  ck([s for s,a in enumerate(w) if a]==leaf['support'])
  for z,val in enumerate(t):
   x1=z&1; y=z>>1; fixed=leaf['fixed']
   ck(val==(-1)**((y&1)*(x1+(y>>1).bit_count())+(fixed&(y>>1)).bit_count()))
  edges=sum(t[z]!=t[z^(1<<i)] for i in range(m+1) for z in range(len(t)))
  ck(Q(edges,len(t))==Q(m+1,2))

def logadd(d,q,weight):
 for n,sign in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=n:
   while n%p==0: d[p]+=sign*weight; n//=p
   p+=1
  if n>1:d[n]+=sign*weight
def kl(p,q):
 out=defaultdict(Q)
 for a,b in zip(p,q):
  if a: ck(b>0); logadd(out,a/b,a)
 return dict((p,a) for p,a in out.items() if a)
def add(*terms):
 out=defaultdict(Q)
 for factor,v in terms:
  for p,a in v.items():out[p]+=factor*a
 return {p:a for p,a in out.items() if a}
def entropy(p):
 d=defaultdict(Q)
 for a in p:
  if a:logadd(d,a,-a)
 return {p:a for p,a in d.items() if a}
def marginal(p,i):return [sum(a for s,a in enumerate(p) if (s>>i)&1==b) for b in (0,1)]
fixtures=[]
for r in (1,2):
 n=3*r; p=[Q(9**sum(((s>>(3*j))&7)==0 for j in range(r)),16**r) for s in range(1<<n)]
 for M in (1,2):
  weights=[Q(1)] if M==1 else [Q(1,3),Q(2,3)]
  params=[[Q((i+j)%2+1,3) for i in range(n)] for j in range(M)]
  comp=[]
  for par in params:
   law=[]
   for s in range(1<<n):
    a=Q(1)
    for i,q in enumerate(par):a*=q if (s>>i)&1 else 1-q
    law.append(a)
   comp.append(law)
  q=[sum(weights[j]*comp[j][s] for j in range(M)) for s in range(1<<n)]
  joint=[[p[s]*weights[j]*comp[j][s]/q[s] for s in range(1<<n)] for j in range(M)]
  v=[sum(a) for a in joint]; ck(sum(v)==1)
  rhs=kl(v,weights); ctc={}; mi={}; smi={}
  for j in range(M):
   R=[a/v[j] for a in joint[j]]; marg=[marginal(R,i) for i in range(n)]
   productlaw=[]
   for s in range(1<<n):
    a=Q(1)
    for i in range(n):a*=marg[i][(s>>i)&1]
    productlaw.append(a)
   tc=kl(R,productlaw); ctc=add((1,ctc),(v[j],tc)); rhs=add((1,rhs),(v[j],tc))
   mi=add((1,mi),(v[j],kl(R,p)))
   for i in range(n):
    rhs=add((1,rhs),(v[j],kl(marg[i],[1-params[j][i],params[j][i]])))
    smi=add((1,smi),(v[j],kl(marg[i],marginal(p,i))))
  ck(kl(p,q)==rhs)
  tc=add(*[(1,entropy(marginal(p,i))) for i in range(n)],(-1,entropy(p)))
  ck(ctc==add((1,tc),(-1,smi),(1,mi)))
  fixtures.append({'r':r,'M':M,'posterior_identity':'PASS','conditional_TC_identity':'PASS'})
out={'checks':checks,'seconds':time.perf_counter()-start,'fixtures':fixtures,'status':'PASS'}
(ROOT/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
