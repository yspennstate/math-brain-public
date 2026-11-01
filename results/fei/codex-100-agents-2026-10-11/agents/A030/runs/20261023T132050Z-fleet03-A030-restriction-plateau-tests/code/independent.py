from fractions import Fraction as F
from pathlib import Path
import itertools,json,time,sys,hashlib
RUN=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv;start=time.perf_counter()
checks=nodes=zeros=off=0
def ck(b):
 global checks
 checks+=1;assert b,checks;assert time.perf_counter()-start<(55 if pilot else 180)
def walsh(tab):
 N=len(tab)
 return tuple(sum(((-1)**((k&t).bit_count()%2))*tab[k] for k in range(N))/F(N) for t in range(N))
def slice_tab(t,i,s):return tuple(v for k,v in enumerate(t) if ((k//(1<<i))%2)==s)
def push(tab,measure,i,s):
 a=walsh(tab);out=[]
 for low in range(len(tab)//2):
  k=(low% (1<<i)) + ((low//(1<<i))<<(i+1));l=k+(1<<i)
  den=a[k]**2+a[l]**2
  prob=(a[k]+(-1)**s*a[l])**2/(2*den) if den else F(1,2)
  out.append(2*(measure[k]+measure[l])*prob)
 return tuple(out)
def output(st):
 global zeros,off
 labels,cs,B,S,rem,nc=st;N=len(labels);D=len(cs[0]);ell=len(cs)
 truth=tuple(cs[labels[y]][x] for x in range(D) for y in range(N));amps=walsh(truth);p=tuple(a*a for a in amps)
 massesB=[sum(v) for v in B];massesS=[sum(v) for v in S]
 A=[];R=[]
 for j in range(ell):
  cj=walsh(tuple(int(v==j) for v in labels));bj=walsh(cs[j]);mb,ms=massesB[j],massesS[j]
  ck(all(v*v<=B[j][k] for k,v in enumerate(cj)));ck(all(v*v<=S[j][k] for k,v in enumerate(bj)))
  ck(mb>=F(labels.count(j),N));ck(ms>=1)
  if not mb:zeros+=1
  A.append(tuple(v/mb for v in B[j]) if mb else tuple(F(1,N) for _ in range(N)))
  R.append(tuple(v/ms for v in S[j]))
 q=tuple(sum(A[j][u]*R[j][t] for j in range(ell))/ell for t in range(D) for u in range(N))
 M=ell*sum(a*b for a,b in zip(massesB,massesS))
 ck(sum(q)==sum(p)==1);ck(M>=ell);ck(all(p[k]<=M*q[k] for k in range(len(p))))
 off+=sum(q[k]>0 and p[k]==0 for k in range(len(p)))
 return M,tuple(a*b for a,b in zip(massesB,massesS))
def children(st,i):
 global nodes
 nodes+=1;labels,cs,B,S,rem,nc=st;pos=rem.index(i);parentM,parenta=output(st);kids=[]
 for s in (0,1):
  if pos<nc:
   ll=slice_tab(labels,pos,s);cc=cs
   BB=tuple(push(tuple(int(v==j) for v in labels),B[j],pos,s) for j in range(len(cs)));SS=S;ncc=nc-1
  else:
   ll=labels;cc=tuple(slice_tab(c,pos-nc,s) for c in cs);BB=B
   SS=tuple(push(cs[j],S[j],pos-nc,s) for j in range(len(cs)));ncc=nc
  ns=(ll,cc,BB,SS,tuple(k for k in rem if k!=i),ncc);kids.append(ns)
 vals=[output(k) for k in kids]
 ck((vals[0][0]+vals[1][0])/2==parentM)
 ck(all((vals[0][1][j]+vals[1][1][j])/2==parenta[j] for j in range(len(cs))))
 return kids
tables=[tuple(1 if mask>>i&1 else -1 for i in range(4)) for mask in range(16)]
pairs=list(itertools.product(tables,tables))
if pilot:pairs=[pairs[k] for k in (0,15,46,239)]
for cs in pairs:
 labels=(0,1);B=tuple(tuple(v*v+F(1,252) for v in walsh(tuple(int(x==j) for x in labels))) for j in range(2))
 S=tuple(tuple(v*v+F(1,252) for v in walsh(c)) for c in cs)
 root=(labels,cs,B,S,(0,1,2),1)
 # B smoothing is pi/(63*2)=1/252; source smoothing is1/(63*4)=1/252.
 ck(output(root)[0]==2*F(64,63)**2)
 for order in itertools.permutations(range(3)):
  frontier=[root]
  for i in order:frontier=[c for st in frontier for c in children(st,i)]
ck(nodes==(168 if pilot else 10752));ck(zeros>0);ck(off>0)
ck(3**8<2**13);ck(64**32<2*63**32)
# Sharp witness: exact source and indicator references, no smoothing.
Z=(1,-1);NZ=(-1,1);exact=((0,1),(Z,NZ),((F(1,4),F(1,4)),)*2,((F(0),F(1)),)*2,(0,1),1)
M,_=output(exact);ck(M==2);ck(walsh((1,-1,-1,1))==(F(0),F(0),F(0),F(1)))
out={'status':'PASS','pilot':pilot,'actual_boolean_functions':len(pairs),'complete_query_orders_per_function':6,'query_nodes':nodes,'checks':checks,'zero_controller_envelopes':zeros,'off_true_reference_row_receipts':off,'helpers_imported':False,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'full_fei':'OPEN'}
(RUN/'out'/('INDEPENDENT_PILOT.json' if pilot else 'INDEPENDENT.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
