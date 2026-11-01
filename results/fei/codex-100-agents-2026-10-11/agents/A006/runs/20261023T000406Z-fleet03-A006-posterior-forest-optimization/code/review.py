"""Independent direct-character matching review and actual queue trace certificates."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,prod
import json,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0;traces=0;label_choices=0
def ck(p):
 global checks
 checks+=1;assert p,checks
def event(vertices,edges,lam):
 global traces
 # A canonical assignment is chosen, never optimized separately into new weights.
 own={}
 for v in vertices:
  i=next(j for j,e in enumerate(edges) if v in e);own.setdefault(i,set()).add(v)
 gates=sorted(own);arcs={i:{j for j in gates if j!=i and own[i]&set(edges[j])} for i in gates}
 reach={i:set(arcs[i])|{i} for i in gates}
 for k in gates:
  for i in gates:
   if k in reach[i]:reach[i]|=reach[k]
 scc={frozenset(j for j in gates if j in reach[i] and i in reach[j]) for i in gates}
 roots=sorted(min(C) for C in scc if not any(arcs[i]&C for i in gates if i not in C))
 found=set(roots);queue=roots[:];parent={};children={i:[] for i in gates}
 for i in queue:
  for j in sorted(arcs[i]):
   if j in found:continue
   found.add(j);v=min(own[i]&set(edges[j]));parent[j]=(i,v);children[i].append((v,j));queue.append(j)
 ck(found==set(gates));ck(len(parent)==len(gates)-len(roots))
 # Execute the actual deterministic occurrence order, including repeated slots.
 actual=[];pending=roots[:]
 for i in pending:
  ck(i not in actual);actual.append(i)
  for v,j in sorted(children[i]):
   ck(v in own[i] and v in edges[j]);pending.append(j)
 ck(set(actual)==set(gates) and set.union(*own.values())==set(vertices))
 D=(1+lam/4)**len(edges)-1
 # Direct independent Bernoulli root/exclusion probability, then condition nonempty.
 rprob=prod(lam/(4+lam) if i in roots else 4/(4+lam) for i in range(len(edges)))
 nonempty=1-(4/(4+lam))**len(edges);q=rprob/nonempty
 ck(q==(lam/4)**len(roots)/D)
 for i in actual:
  s=len(own[i]);c=len(children[i]);q*=F(1,s*(s+1))*F(1,comb(2,s))*F(1,(c+1)*(c+2))*F(1,comb(s+c-1,c))*lam**c
 ck(q>=((lam/72)**len(vertices))/D)
 traces+=1
 return q
def spectrum(a,b,edges):
 n=a+b;N=1<<n
 f=[1 if any((x>>i&1) and (x>>j&1) for i,j in edges) else -1 for x in range(N)]
 # Direct character sums are independent of the main checker's butterfly transform.
 w=[sum(z*(-1 if (x&S).bit_count()%2 else 1) for x,z in enumerate(f)) for S in range(N)]
 inf=[F(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N) for i in range(n)]
 ck(sum(z*z for z in w)==N*N);ck(sum(inf)==sum(F(S.bit_count()*z*z,N*N) for S,z in enumerate(w)))
 q=F(sum(z==-1 for z in f),N)
 for i,j in edges:ck(inf[i]+inf[j]>=F(4,3)*q)
 return f,w,sum(inf)
reviewrows=[]
for b in range(2,6):
 for a in range(2,b+1):
  for k in range(a+1):
   edges=[(i,a+j) for i in range(a) for j in range(b) if not (i==j and i<k)]
   f,w,I=spectrum(a,b,edges);n=a+b;N=1<<n;u,v=F(1,1<<a),F(1,1<<b)
   ck(F(sum(z==-1 for z in f),N)==u+v+(k-1)*u*v)
   I0=2*a*u*(1-v)+2*b*v*(1-u);ck(I==I0+2*k*(n-4)*u*v>=I0)
   R=M=F(0)
   for S in range(1,N):
    U=S&((1<<a)-1);V=S>>a;r=sum(bool(U>>i&1)!=bool(V>>i&1) for i in range(k))
    formula=-2*(u*(not V)+v*(not U)+u*v*(k-1-2*r))
    ck(F(w[S],N)==formula)
    if not U:R+=F(S.bit_count()*w[S]**2,N*N)
    elif V:M+=F(S.bit_count()*w[S]**2,N*N)
   ck(R==2*v*(b-2*u*(b+k)+u*u*(b*(k+1)+2*k)))
   ck(M==2*u*v*((k+1)*(a*(1-v)+b*(1-u))-2*k*(u+v)))
   reviewrows.append({'a':a,'b':b,'k':k,'I':str(I),'R':str(R),'M':str(M)})
   ck(time.monotonic()-start<52)
# Every nonempty labelled 2x2 graph, then five larger overlapping fixtures.
jobs=[];complete=[(i,2+j) for i in range(2) for j in range(2)]
for mask in range(1,16):jobs.append((2,2,[e for j,e in enumerate(complete) if mask>>j&1]))
for a,b,H in [(3,3,[3,6,4]),(3,3,[3,6,5]),(4,4,[3,6,12,9]),(4,4,[3,3,12,12]),(6,6,[3,3,12,12,48,48])]:
 jobs.append((a,b,[(i,a+j) for i in range(a) for j in range(b) if not H[i]>>j&1]))
for a,b,edges in jobs:
 n=a+b;lam=F(1,b);total=F(0)
 incident=set(v for e in edges for v in e)
 for mask in range(1,1<<n):
  vertices={i for i in range(n) if mask>>i&1}
  if not vertices<=incident:continue
  total+=event(vertices,edges,lam)
 ck(total<=1)
 # Full-side singleton-root sums; fixed root order, deduplicated actual root sets.
 for side in [range(a),range(a,a+b)]:
  V=[v for v in side if v in incident];options=[[j for j,e in enumerate(edges) if v in e] for v in V]
  seen=set();count=0
  for assignment in product(*options):
   rootset=tuple(sorted(assignment));ck(len(rootset)==len(set(rootset)) and rootset not in seen);seen.add(rootset);count+=1
  label_choices+=count
  D=(1+lam/4)**len(edges)-1
  qsum=F(count)*(lam/32)**len(V)/D
  formula=prod(F(len(o),32*b) for o in options)/D
  ck(qsum==formula)
 ck(time.monotonic()-start<54)
for c in range(129):
 ck((c+1)**2*(c+2)<=2*6**c)
 for s in [1,2]:ck((c+1)*(c+2)*comb(s+c-1,c)<=2*6**c)
ck(72**4<2**25)
for b in range(4,513):ck(b*b<=2**b and (b+1)**2*32<=50*b*b)
for d in range(513):ck((d+4)**2<=16*2**d and (d+5)**2*32<=50*(d+4)**2)
ck(F(25,4)+F(9,8)+28==F(283,8)<36)
ck(F(25,4)+F(9,8)+F(304,9)==F(2963,72)<42)
out={'status':'PASS','helper_version':'A006-independent-queue-and-matching-review-v1','matching_functions':len(reviewrows),'queue_graphs':len(jobs),'distinct_canonical_histories':traces,'singleton_root_choices':label_choices,'assertions':checks,'seconds':time.monotonic()-start,'matching_rows':reviewrows}
(B/'out/REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='matching_rows'}))
