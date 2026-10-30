from pathlib import Path
from fractions import Fraction as F
import json, hashlib, time

ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261014T054454Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py'
# Frozen source helper; the prefix defines exact arithmetic, without its graph loop.
source=OLD.read_text(encoding='utf-8').split('rows=[];candidates=0;sets=0;wins=')[0]
exec(compile(source,str(OLD),'exec'),globals())
R=ROOT
budget=60 if args.pilot else 300
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,c):return a[0]*c,a[1]*c
def add(a,b):return a[0]+b[0],a[1]+b[1]
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def KL(a,b):return sub(CE(a,b),CE(a,a))
rows=[];candidates=0;graphs=0;sets=0
for n in ([3] if args.pilot else [3,4,5]):
 universe=list(itertools.combinations(range(n),2))
 for mask in range(1<<len(universe)):
  candidates+=1;edges=[e for j,e in enumerate(universe) if mask&(1<<j)]
  if len(components(n,edges))!=1 or any(len(components(n,edges,x))!=1 for x in range(n)):continue
  graphs+=1
  lam=F(1,max(sum(u in e for e in edges) for u in range(n)))
  D=(1+lam/4)**len(edges)-1
  em=[sum(1<<u for u in e) for e in edges]
  C=[int(not any(z&e==e for e in em)) for z in range(1<<n)]
  s=F(sum(C),1<<n);v=4*s*(1-s)
  ck(0<s<1)
  ch=[F(t,1<<n) for t in walsh(C)]
  p=[F(t*t,1<<(2*n)) for t in walsh([1-2*c for c in C])]
  I=sum((A.bit_count()*pA for A,pA in enumerate(p)),F(0));ck(I>=v)
  masses=[occupation(n,edges,A,lam,D) for A in range(1,1<<n)]
  Z=sum(masses);ck(0<Z<=1);ck(all(m>0 for m in masses))
  q=[m/Z for m in masses]
  P=[pA/v for pA in p[1:]];ck(sum(P)==sum(q)==1)
  excess=scale(KL(P,q),v)
  for x in range(n):
   private=[u for u in range(n) if u!=x];h=[]
   for b in (0,1):
    vals=[C[(b<<x)+sum(((z>>j)&1)<<u for j,u in enumerate(private))] for z in range(1<<(n-1))]
    h.append([F(t,len(vals)) for t in walsh(vals)])
   rc=[]
   for A in range(1<<n):
    T=sum(((A>>u)&1)<<j for j,u in enumerate(private));a,b=h[0][T],h[1][T]
    ck(ch[A]==((a-b)/2 if A&(1<<x) else (a+b)/2))
    rc.append((a*a+b*b)/(4*s))
   ck(sum(rc)==1);re=rc[0];ck(s/2<=re<=F(1,2))
   row=[a/(1-re) for a in rc[1:]];L=2*(1-re)/(1-s)
   ck(L>1);ck(sum(row)==1);ck(all(a<=L*b for a,b in zip(P,row)))
   S=[(L*b-a)/(L-1) for a,b in zip(P,row)];ck(min(S)>=0 and sum(S)==1)
   debt=KL(row,q);other=KL(S,q)
   # Exact finite-mixture KL identity, interval-checked with outward rational logarithms.
   js=sub(CE(row,row),add(scale(CE(P,P),1/L),scale(CE(S,S),1-1/L)))
   rhs=add(sub(scale(debt,L),scale(other,L-1)),scale(js,L))
   ck(overlap(KL(P,q),rhs))
   hmix=CE([1/L,1-1/L],[1/L,1-1/L])
   ck(js[1]<=hmix[0] or overlap(js,hmix))
   coarse=add(scale(debt,v*L),scale(hmix,v*L))
   ck(excess[1]<=coarse[0])
   ck(v*L==8*s*(1-re))
   ck(v*L*hmix[1]<F(9,2)*I)
   ck(excess[1]<v*L*debt[0]+F(9,2)*I)
   rows.append({'n':n,'edge_mask':mask,'query':x,'s':str(s),'I':str(I),'row_empty':str(re),'L':str(L),'Z':str(Z),'occupation_excess_over_I':outward(scale(excess,1/I)),'inherited_row_KL_over_I':outward(scale(debt,v*L/I))})
  sets+=(1<<n)-1
  (R/'out/checkpoint.json').write_text(json.dumps({'graphs':graphs,'queries':len(rows),'assertions':assertions,'elapsed_seconds':time.monotonic()-start},indent=2),encoding='utf-8')
# Constant rows / a zero row, plus endpoint probabilities, using every indicator on two bits.
boundaries=0
for c0 in range(16):
 for c1 in range(16):
  vals0=[(c0>>z)&1 for z in range(4)];vals1=[(c1>>z)&1 for z in range(4)]
  s=F(sum(vals0)+sum(vals1),8)
  if s in (0,1):boundaries+=1;continue
  a=[F(t,4) for t in walsh(vals0)];b=[F(t,4) for t in walsh(vals1)]
  re=(a[0]**2+b[0]**2)/(4*s);L=2*(1-re)/(1-s)
  ck(s/2<=re<=F(1,2));ck(L>1)
  for j in range(4):
   for sign in (1,-1):ck((a[j]+sign*b[j])**2<=2*(a[j]**2+b[j]**2))
  boundaries+=1
out={'helper':'A014-nonseparating-inherited-KL-v1','mode':'pilot' if args.pilot else 'full','labelled_candidates':candidates,'graphs':graphs,'all_nonempty_sets':sets,'queries':len(rows),'boundary_pairs':boundaries,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'rows':rows}
(R/('out/pilot.json' if args.pilot else 'out/check.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
