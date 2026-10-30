import json,time,math,hashlib
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'A019-star-tree-v1','family':'majority cores n=1,3,5 and point-translation stars with 2 or3 modules; full selector-first trees','domain':'(n,ks,orientations)=(1,[2,2],[0,0]),(3,[2,2],[0,1]),(3,[2,2,2],[0,1,0]),(5,[1,2],[0,1]); vectors alternate first and last core coordinate; also dictator repeated-vector case','case_count':4,'selector_internal_node_count':204,'symmetry':'none','arithmetic':'integer Walsh, Fraction physical edge weights and prime-log interval erasure certificates','memory_estimate_MB':40,'maximum_runtime_seconds':60}
(R/'out/TREE_SPEC.json').write_text(json.dumps(spec,indent=2))
started=time.monotonic();checks=0;nodes=0
def ck(x):
 global checks
 checks+=1
 assert x
def fw(t):
 a=t[:];step=1
 while step<len(a):
  for start in range(0,len(a),2*step):
   for j in range(start,start+step):a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
  step*=2
 return tuple(Q(x,len(t)) for x in a)
@lru_cache(None)
def factor(n):
 p=2;d={}
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def H(ps):
 out=defaultdict(Q)
 for x in ps:
  if not x:continue
  for p,e in factor(x.denominator).items():out[p]+=x*e
  for p,e in factor(x.numerator).items():out[p]-=x*e
 return {p:w for p,w in out.items() if w}
def lin(terms):
 out=defaultdict(Q)
 for q,d in terms:
  for p,w in d.items():out[p]+=q*w
 return {p:w for p,w in out.items() if w}
def log1(x):
 z=(x-1)/(x+1);s=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(48)),Q(0));err=2*z**97/(97*(1-z*z));return s,s+err
l2,u2=log1(Q(2))
@lru_cache(None)
def logp(p):
 k=p.bit_length()-1;l,u=log1(Q(p,2**k));return k+l/u2,k+u/l2
def sign(d):
 lower=Q(0)
 for p,w in d.items():
  lo,hi=logp(p);lower+=w*(lo if w>=0 else hi)
 return lower>=0
records=[]
for n,ks,orientations in ((1,[2,2],[0,0]),(3,[2,2],[0,1]),(3,[2,2,2],[0,1,0]),(5,[1,2],[0,1])):
 a=1+sum(ks);g=[1 if 2*y.bit_count()<n else -1 for y in range(2**n)];vs=[1 if j%2==0 else 2**(n-1) for j in range(len(ks))]
 table=[]
 for y in range(2**n):
  for w in range(2**a):
   x=w&1;shift=0;off=1
   for k,s,v in zip(ks,orientations,vs):
    if x==s and ((w>>off)&(2**k-1))==0:shift^=v
    off+=k
   table.append(g[y^shift])
 gp=tuple(x*x for x in fw(g));root=tuple(x*x for x in fw(table))
 Icore=sum(Q(s.bit_count())*p for s,p in enumerate(gp));Iroot=sum(Q(s.bit_count())*p for s,p in enumerate(root))
 influence=Q(0);erasure=[];decrement=[];frontier=[(Q(1),table)]
 for depth in range(a):
  nextlevel=[]
  for weight,t in frontier:
   if time.monotonic()-started>60:raise TimeoutError('tree frozen deadline')
   nodes+=1;ff=fw(t);ps=tuple(x*x for x in ff)
   d=sum(ps[s] for s in range(len(ps)) if s&1)
   ck(d==Q(sum(t[s]!=t[s^1] for s in range(len(t))),len(t)))
   q=tuple(ps[2*j]+ps[2*j+1] for j in range(len(ps)//2))
   B=lin([(Q(1),H(ps)),(-Q(1),H(q))])
   ck(sign(lin([(3*d,{2:Q(1)}),(-Q(1),B)])))
   c0=t[0::2];c1=t[1::2];p0=tuple(x*x for x in fw(c0));p1=tuple(x*x for x in fw(c1))
   mix=tuple((p0[j]+p1[j])/2 for j in range(len(p0)));ck(mix==q)
   Delta=lin([(Q(1),H(ps)),(-Q(1,2),H(p0)),(-Q(1,2),H(p1))])
   JS=lin([(Q(1),H(mix)),(-Q(1,2),H(p0)),(-Q(1,2),H(p1))])
   ck(Delta==lin([(Q(1),B),(Q(1),JS)]))
   influence+=weight*d;erasure.append((weight,B));decrement.append((weight,Delta))
   nextlevel.extend([(weight/2,c0),(weight/2,c1)])
  frontier=nextlevel
 for weight,t in frontier:
  ck(any(t==[g[y^v] for y in range(2**n)] for v in range(2**n)))
  ck(H(tuple(x*x for x in fw(t)))==H(gp))
 ck(influence==Iroot-Icore)
 ck(lin(decrement)==lin([(Q(1),H(root)),(-Q(1),H(gp))]))
 ck(sign(lin([(3*influence,{2:Q(1)}),(-Q(1),lin(erasure))])))
 ck(sign(lin([(5*influence,{2:Q(1)}),(-Q(1),lin(decrement))])))
 raw=sum(Q(s.bit_count()-1)*root[s] for s in range(len(root)) if s&1)*2
 Ix=sum(root[s] for s in range(len(root)) if s&1);Ipriv=influence-Ix
 surplus=Q(0)
 for T,p in enumerate(gp):
  m=Q(1)
  for k,v in zip(ks,vs):
   if (T&v).bit_count()%2:m*=1-Q(2,2**k)
  surplus+=p*T.bit_count()*(1-m)
 ck(raw-Ipriv==surplus)
 records.append({'n':n,'ks':ks,'orientations':orientations,'queried_influence':str(influence),'terminal_influence':str(Icore),'localized_boundary_bill_at_K3':0,'raw_boundary_data_core_surplus':str(surplus)})
ck(nodes==spec['selector_internal_node_count'])
out={'status':'PASS','assertions':checks,'internal_nodes':nodes,'cases':len(records),'runtime_seconds':time.monotonic()-started,'records':records,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/TREE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('status','assertions','internal_nodes','cases','runtime_seconds')}))
