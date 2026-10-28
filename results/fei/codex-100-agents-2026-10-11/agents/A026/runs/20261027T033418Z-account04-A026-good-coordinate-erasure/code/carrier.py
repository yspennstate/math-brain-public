"""Independent direct-character certificate: no imports from check.py."""
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import json,time
R=Path(__file__).resolve().parents[1]; start=time.monotonic();count=0
def ck(x):
 global count
 count+=1
 assert x,count
 if time.monotonic()-start>55:raise TimeoutError('frozen cap')
def P(f):
 n=len(f);return [F(sum(v*(-1)**((x&s).bit_count()%2) for x,v in enumerate(f)),n)**2 for s in range(n)]
def fac(n):
 d=2
 while d*d<=n:
  while n%d==0:yield d;n//=d
  d+=1
 if n>1:yield n
def H(p):
 out=defaultdict(F)
 for v in p:
  if v:
   for k in fac(v.numerator):out[k]-=v
   for k in fac(v.denominator):out[k]+=v
 return {k:v for k,v in out.items() if v}
def plus(a,b):
 d=defaultdict(F,a)
 for k,v in b.items():d[k]+=v
 return {k:v for k,v in d.items() if v}
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def influence(f,j):return F(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f))
def itotal(f):return sum((influence(f,j) for j in range(len(f).bit_length()-1)),F(0))
def insert(x,i,b):return (x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)
def kid(f,i,b):return [f[insert(x,i,b)] for x in range(len(f)//2)]
def bi(f,i):
 p=P(f);q=[p[insert(t,i,0)]+p[insert(t,i,1)] for t in range(len(f)//2)]
 return plus(H(p),scale(H(q),-1))
def carrier(h,m):
 n=len(h).bit_length()-1;N=1<<(n*m)
 core=[]
 for x in range(N):
  v=1
  for j in range(m):v*=h[(x>>(j*n))&((1<<n)-1)]
  core.append(v)
 return [(-1 if gate==0 else 1)*v for gate in range(4) for v in core],core
rows=nodes=0
def tree(f,gate,cores,labels,depth,policy):
 """Adaptive restrictions of a fixed disjoint product, checked nodewise."""
 global nodes
 nodes+=1;n=len(f).bit_length()-1
 prodH=H(P(gate));prodI=itotal(gate)
 for c in cores:prodH=plus(prodH,H(P(c)));prodI+=itotal(c)
 ck(H(P(f))==prodH);ck(itotal(f)==prodI)
 if not n or (policy==2 and depth>=2):return
 j=(sum(v for _,v in labels)+depth+policy)%n
 # labels lists which component owns each current physical coordinate.
 comp,local=labels[j];newlabels=[]
 for k,(c,l) in enumerate(labels):
  if k!=j:newlabels.append((c,l-1 if c==comp and l>local else l))
 for b in range(2):
  gg=list(gate);cc=[list(c) for c in cores]
  if comp==0:gg=kid(gg,local,b)
  else:cc[comp-1]=kid(cc[comp-1],local,b)
  tree(kid(f,j,b),gg,cc,newlabels,depth+1,policy)
for n in range(3):
 for lab in range(1<<(1<<n)):
  h=[1-2*((lab>>x)&1) for x in range(1<<n)]
  for m in (1,2):
   f,c=carrier(h,m);pn=P(h);pf=P(f);N=len(c);rows+=1
   expected=H(P(c));ck(H(pf)==plus(expected,{2:F(2)}));ck(itotal(f)==m*itotal(h)+1)
   for gbit in (n*m,n*m+1):
    ck(bi(f,gbit)=={2:F(1)});ck(influence(f,gbit)==F(1,2))
    for b in range(2):ck(H(P(kid(f,gbit,b)))==expected)
   for j in range(n*m):ck(bi(f,j)==bi(h,j%n));ck(influence(f,j)==influence(h,j%n))
   # y is the highest gate bit: one first child is core, the other z*core.
   ck(kid(f,n*m+1,1)==c+c)
   if m==1:
    labels=[(1,j) for j in range(n)]+[(0,0),(0,1)]
    for policy in range(3):tree(f,[-1,1,1,1],[h],labels,0,policy)
result={'status':'PASS','carriers':rows,'adaptive_nodes':nodes,'assertions':count,'seconds':time.monotonic()-start,'implementation':'direct characters, physical edges, independent prime-log entropy; no main imports'}
(R/'out/CARRIER.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
