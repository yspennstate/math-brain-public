import arithmetic as h
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,itertools,time,sys

ROOT=Path(__file__).resolve().parents[1];MODE=sys.argv[1]
def iv(x):return F(x),F(x)
def add(*vs):return sum((x[0] for x in vs),F()),sum((x[1] for x in vs),F())
def scale(v,c):return (v[0]*c,v[1]*c) if c>=0 else (v[1]*c,v[0]*c)
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)
def pos(a):return max(F(),a[0]),max(F(),a[1])
def avg(vs):return scale(add(*vs),F(1,len(vs)))
def enc(a):return [str(x) for x in a]
GRID=1<<48;OUT=1<<160
@lru_cache(None)
def logq(q):
 assert q>0
 e=0
 while q<1:q*=2;e-=1
 while q>=2:q/=2;e+=1
 lo,hi=h.lnseries(q)
 lo=e+lo/h.LN2[1];hi=e+hi/h.LN2[0]
 return F((lo*OUT).__floor__(),OUT),F((hi*OUT).__ceil__(),OUT)
def logiv(a):
 assert a[0]>0
 lo=F((a[0]*GRID).__floor__(),GRID);hi=F((a[1]*GRID).__ceil__(),GRID)
 assert lo>0
 return logq(lo)[0],logq(hi)[1]
def product(ds):
 out=[]
 for s in range(1<<len(ds)):
  p=F(1)
  for i,d in enumerate(ds):p*=d if s&(1<<i) else 1-d
  out.append(p)
 return tuple(out)
@lru_cache(None)
def stats(t):
 a=h.fwht(t);p=tuple(x*x for x in a);n=len(t).bit_length()-1
 ds=tuple(sum((x for s,x in enumerate(p) if s&(1<<i)),F()) for i in range(n))
 for i,d in enumerate(ds):h.equal(d,h.vertex_influence(t,i),'physical versus spectral influence')
 H=h.entropy(p);TC=h.combine((1,h.entropy(product(ds))),(-1,H))
 return p,ds,H,TC
def compose(v):return tuple(-1 if z&1==0 and z&2 else v[z>>3] if z&1 and z&4 else 1 for z in range(8*len(v)))
def child(t,i,b):return tuple(t[h.insert(s,i,b)] for s in range(len(t)//2))
def entropyiv(t):return h.interval(stats(t)[2])
def tciv(t):return h.interval(stats(t)[3])
def slackiv(t):return sub(iv(4*sum(stats(t)[1],F())),entropyiv(t))
def rootref(t):
 p,ds,H,TC=stats(t);z=1-p[0];rr=[d/z for d in ds]
 def poly(c):
  q=F(1)
  for r in rr:q*=1-c*r
  return 1-c-q
 lo=F(1,2);hi=F(1)
 for k in range(16):
  if poly(lo)>0:break
  lo/=2
 else:raise AssertionError('frozen root bracket not found')
 h.check(poly(hi)<0,'interior positive root upper bracket')
 for k in range(36):
  mid=(lo+hi)/2;val=poly(mid)
  if not val:lo=hi=mid;break
  if val>0:lo=mid
  else:hi=mid
 h.check(lo==hi and poly(lo)==0 or poly(lo)>0 and poly(hi)<0)
 c=(lo,hi);theta=[scale(c,r) for r in rr]
 M=[]
 for s in range(len(p)):
  if not s:M.append(iv(p[0]));continue
  mass=iv(z)
  for i,th in enumerate(theta):mass=mul(mass,th if s&(1<<i) else sub(iv(1),th))
  M.append(mul(mass,(1/hi,1/lo)))
 total=add(*M);h.check(total[0]<=1<=total[1],'whole reference normalized')
 for i,d in enumerate(ds):
  mm=add(*[a for s,a in enumerate(M) if s&(1<<i)])
  h.check(mm[0]<=d<=mm[1],'matched original occupancy marginal')
 HM=add(h.interval(h.entropy([z,1-z])),scale(logiv(c),z))
 for d,th in zip(ds,theta):
  if d:HM=add(HM,scale(logiv(th),-d))
  if z-d:HM=add(HM,scale(logiv(sub(iv(1),th)),-(z-d)))
 A=sub(HM,h.interval(H));h.check(A[1]>=0,'canonical KL enclosure consistent with Gibbs nonnegativity')
 A=(max(F(),A[0]),A[1])
 return M,A,c
def trans(t,i,Q):
 p=stats(t)[0];cs=[child(t,i,b) for b in (0,1)];pc=[stats(c)[0] for c in cs]
 reach=[iv(0),iv(0)];refonly=iv(0)
 for s in range(len(p)//2):
  pe=p[h.insert(s,i,0)]+p[h.insert(s,i,1)]
  qe=add(Q[h.insert(s,i,0)],Q[h.insert(s,i,1)])
  if not pe:refonly=add(refonly,qe)
  k=[pc[b][s]/(2*pe) if pe else F(1,2) for b in (0,1)]
  h.equal(sum(k,F()),1,'full coherent kernel, including reference-only rows')
  for b in (0,1):reach[b]=add(reach[b],scale(qe,k[b]))
 for r in reach:h.check(r[0]>0,'supported physical outcome prediction')
 O=scale(logiv(scale(mul(reach[0],reach[1]),4)),-F(1,2))
 return cs,O,refonly,reach
def exactproductref(t):return [iv(q) for q in product(stats(t)[1])]

MASKS=(0,255) if MODE=='pilot' else range(256) if MODE=='exhaustive' else (0,255,1,254,7,248,15,240,235,91)
records=[];failures=[];primary=0;reference_only=0;nonzero_terminals=0
for mask in MASKS:
 v=tuple(1 if mask&(1<<s) else -1 for s in range(8));t=compose(v)
 M,A,c=rootref(t);ac,Oa,za,reach=trans(t,1,M)
 meanS=avg([slackiv(s) for s in ac]);h.check(meanS[0]>0,'original certified mean child owner')
 for s in ac:h.check(slackiv(s)[0]>=0,'individual original child certificate')
 Da=sub(add(Oa,avg([tciv(s) for s in ac])),A);first=pos(Da)
 for i in range(3):
  mids=[];Db=[];Ob=[];zb=[]
  for parent in ac:
   children,O,Z,_=trans(parent,i+2,exactproductref(parent))
   mids.append(children);Ob.append(O);zb.append(Z)
   Db.append(sub(add(O,avg([tciv(s) for s in children])),tciv(parent)))
  W2=add(first,avg([pos(d) for d in Db]));h.check(sub(scale(meanS,F(1,2)),W2)[0]>0,'source two-query half-budget at selected cases')
  for thirdidx in range(4):
   Dthird=[];Othird=[];leaves=[];refmass=[]
   for branch in mids:
    for parent in branch:
     cc,O,Z,_=trans(parent,thirdidx,exactproductref(parent))
     Dthird.append(sub(add(O,avg([tciv(s) for s in cc])),tciv(parent)))
     Othird.append(O);leaves.extend(cc);refmass.append(Z)
   W3=add(W2,avg([pos(d) for d in Dthird]));left=sub(meanS,W3)
   # Frozen target is whole original-owner eligibility; failures are saved, never silently repaired.
   passed=left[0]>0
   if not passed:failures.append({'mask':mask,'first_core_coordinate':i,'third_remaining_coordinate':thirdidx,'remaining':enc(left)})
   else:h.check(True,'third query paid by original remaining owner')
   ce=[add(entropyiv(s),tciv(s)) for s in leaves]
   terminalH=avg([entropyiv(s) for s in leaves]);terminalTC=avg([tciv(s) for s in leaves])
   totalO=add(Oa,avg(Ob),avg(Othird))
   rhs=add(A,W3,terminalH);lhs=add(totalO,avg(ce))
   h.check(sub(rhs,lhs)[1]>=0,'enclosure consistent with analytically proved retained-terminal bound')
   # Independent conservative-reference potential at each actual query.
   for b in (0,1):
    for j in (0,1):
     k=2*b+j;Pmid=add(tciv(mids[b][j]),pos(Dthird[k]));Pleaf=avg([tciv(s) for s in leaves[2*k:2*k+2]])
     h.check(sub(sub(Pmid,Pleaf),Othird[k])[1]>=0,'enclosure consistent with proved third physical reference potential')
   reference_only+=sum(z[1]>0 for z in zb+refmass)
   nonzero_terminals+=sum(bool(stats(s)[2]) for s in leaves)
   # Remaining original labels after deleting a and selected y_i.
   labels=['x','b']+[f'y{k}' for k in range(3) if k!=i]
   records.append({'mask':mask,'first_core_coordinate':i,'third_query':labels[thirdidx],'positive_two_query_bookings':enc(W2),'third_positive_debit':enc(avg([pos(d) for d in Dthird])),'total_positive_bookings':enc(W3),'original_mean_S4':enc(meanS),'remaining_same_owner':enc(left),'terminal_mean_H':enc(terminalH),'terminal_mean_TC':enc(terminalTC),'terminal_mean_CE':enc(avg(ce)),'first_conversion_signed':enc(Da),'third_signed_debits':[enc(d) for d in Dthird],'root_c':enc(c),'ref_only_mass_third':[enc(z) for z in refmass],'payment_pass':passed})
   primary+=1
 stats.cache_clear();logq.cache_clear()
 h.check(time.perf_counter()-h.START<h.CAP,'frozen time ceiling')
out=ROOT/'out';out.mkdir(exist_ok=True)
res={'status':'PASS' if not failures else 'OWNERSHIP_FAILURE_SAVED','mode':MODE,'labelled_cores':len(MASKS),'three_query_policies':primary,'terminal_visits':8*primary,'nonzero_terminal_entropy_visits':nonzero_terminals,'reference_only_node_visits':reference_only,'exact_assertions':h.ASSERTS,'seconds':time.perf_counter()-h.START,'failures':failures,'records':records}
(out/(MODE.upper()+'_CHECK.json')).write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in res.items() if k!='records'},indent=2))
