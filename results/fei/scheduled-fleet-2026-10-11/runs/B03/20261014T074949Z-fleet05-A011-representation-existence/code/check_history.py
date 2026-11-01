import shared as s
from fractions import Fraction as F
from pathlib import Path
import time,json
R=Path(__file__).resolve().parents[1];start=time.monotonic();cases=[]
def add(a,b,weight=F(1)):return a[0]+weight*b[0],a[1]+weight*b[1]
def inherited(v,Q,j):
 a=s.fw(v);P=[x*x for x in a];N=len(v)//2
 vals=[[v[s.insert(W,j,b)] for W in range(N)] for b in range(2)]
 Pc=[[x*x for x in s.fw(w)] for w in vals]
 m=[(Pc[0][W]+Pc[1][W])/2 for W in range(N)]
 rr=[Q[s.insert(W,j,0)]+Q[s.insert(W,j,1)] for W in range(N)]
 Rt=[]
 for b in range(2):
  # A source-only node has zero true/reference fibers; retain any positive reference mass explicitly.
  Rt.append([rr[W]*Pc[b][W]/m[W] if m[W] else rr[W] for W in range(N)])
 Z=[sum(w) for w in Rt];Rb=[[w/Z[b] for w in Rt[b]] for b in range(2)]
 s.ck(Z[0]+Z[1]==2);s.ck(Z[0]>0 and Z[1]>0)
 for W in range(N):
  s.ck(P[s.insert(W,j,0)]+P[s.insert(W,j,1)]==m[W])
  if m[W]:
   for b in range(2):s.ck(Rb[b][W]*m[W]*Z[b]==rr[W]*Pc[b][W])
 cp=s.ce(P,Q);cc=[s.ce(Pc[b],Rb[b]) for b in range(2)]
 T=s.sub(cp,s.avg(*cc));D=s.sub(s.entropy(P),s.avg(s.entropy(Pc[0]),s.entropy(Pc[1])))
 # Rounding intervals surround the exact atom-likelihood disintegration.
 s.ck(T[1]>=D[0])
 return vals,Rb,T,D,cp,cc,Z
for k in [2,4,6]:
 n=k+4;N=2**n;t=F(1,N);point=(1<<(k//2))-1
 def core(W):
  z=W&((1<<k)-1);y=(W>>k)&7
  return (-1)**sum(((z>>(2*i))&1)*((z>>(2*i+1))&1) for i in range(k//2))*(-1 if y==0 else 1)
 v=[core(W)*(-1 if W==point else 1) for W in range(2*N)]
 a=s.fw(v);P=[x*x for x in a];q=[P[T]+P[N+T] for T in range(N)]
 Q=[t*P[U*N+T]/q[T] for U in range(2) for T in range(N)]
 If=sum(s.inf(v));Hp=s.entropy(P)
 for order in [(n-1,n),(n,n-1)]:
  first,second=order;j2=second-1 if second>first else second
  vals,Rb,T1,D1,cp,cc,Z1=inherited(v,Q,first)
  queryT=T1;queryD=D1;leafcost=(F(0),F(0));leafH=(F(0),F(0));leafI=F(0);pivot=s.inf(v)[first];zs=[]
  for b in range(2):
   leaves,refs,T2,D2,cp2,lc,Z2=inherited(vals[b],Rb[b],j2)
   queryT=add(queryT,T2,F(1,2));queryD=add(queryD,D2,F(1,2));zs.append([str(z) for z in Z2])
   pivot+=s.inf(vals[b])[j2]/2
   for c in range(2):
    leafcost=add(leafcost,lc[c],F(1,4));lp=[x*x for x in s.fw(leaves[c])]
    leafH=add(leafH,s.entropy(lp),F(1,4));leafI+=sum(s.inf(leaves[c]))/4
    s.ck(len(set(leaves[c]))==2)
  s.ck(pivot==2*t);s.ck(If-leafI==2*t)
  exactD=s.sub(Hp,leafH);diff=s.sub(queryD,exactD);s.ck(diff[0]<=0<=diff[1])
  s.ck(exactD[0]>(F(3*k,4)+F(9,2))*pivot)
  s.ck(queryT[0]>(F(3*k,4)+F(9,2))*pivot)
  full=add(leafcost,queryT);diff=s.sub(full,cp);s.ck(diff[0]<=0<=diff[1])
  # Positive margin certifies the whole retained-terminal ledger, rather than assuming descendants are paid.
  s.ck(full[1]<4*If)
  margin=s.sub((4*If,4*If),full);s.ck(margin[0]>=F(k-1)-(k+12)*t)
  cases.append({'k':k,'order':'dummy,control' if first==n-1 else 'control,dummy','actual_total_pivotal_mass':str(pivot),'first_normalizers':[str(z) for z in Z1],'second_normalizers':zs,'complete_terminal_cost':s.display(leafcost),'full_query_cost':s.display(queryT),'complete_retained_ledger':s.display(full),'entropy_price_per_total_pivotal':s.display((exactD[0]/pivot,exactD[1]/pivot)),'owned_root_margin':s.display(margin)})
  (R/'out/HISTORY_CHECKPOINT.json').write_text(json.dumps({'status':'PARTIAL','cases':cases,'assertions':s.checks},indent=2),encoding='utf-8')
  if time.monotonic()-start>55:raise RuntimeError('cutoff')
out={'status':'PASS','assertions':s.checks,'history_cases':len(cases),'physical_leaves':24,'seconds':time.monotonic()-start,'cases':cases,'fresh_floor_resets':0,'arithmetic':'Fraction, actual Walsh and edges, exact atom likelihood factors, outward rational log enclosures'}
(R/'out/HISTORY_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
