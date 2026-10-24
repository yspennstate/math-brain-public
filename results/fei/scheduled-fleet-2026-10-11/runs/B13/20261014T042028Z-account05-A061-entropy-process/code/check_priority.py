import arithmetic as h
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from collections import Counter
import json,time,itertools,sys

MODE=sys.argv[1];ROOT=Path(__file__).resolve().parents[1]
CORES=[(1,1,1,1),(-1,1,1,1),(1,-1,-1,1),(1,-1,1,-1)]
@lru_cache(None)
def stats(t):
 a=h.fwht(t);return a,h.entropy([x*x for x in a]),h.total(a),sum(t,F())/len(t)
def phi(q):return h.combine((-1,h.masslog(q)))
def Phi(x,y):return h.combine((1,phi(x)),(1,phi(y)),(-1,phi(x+y)))
def positive(e,label=''):
 if not e:h.check(True);return
 h.check(h.interval(e)[0]>=0,(label,h.interval(e)))
def sign(e):
 if not e:return 0
 lo,hi=h.interval(e);h.check(lo>0 or hi<0,('ambiguous sign',e,lo,hi));return 1 if lo>0 else -1
@lru_cache(None)
def query(t,i):return h.metrics(t,i,stats(t)[0])
def rarity(p,b,Vu,Vv):return h.combine((Vu,phi(p)),(Vv,phi((1-p)*b)))

localcases=treecases=nodes=growth=0
def local(pilot=False):
 global localcases
 widths=(1,) if pilot else (1,2)
 maps=list(itertools.product((0,1,2),repeat=4))[:9 if pilot else 81]
 for s in widths:
  p=F(1,1<<s)
  c=h.shifted(Phi((1-p)**2,p*p),p-2*p*p)
  k=h.combine((1,phi(1-p)),(-F(1,2),phi(1-2*p)))
  for mapping in maps:
   b=F(mapping.count(0),4)
   for u in CORES:
    y=stats(u)[3];Vu=1-y*y
    for v in CORES:
     mv=stats(v)[3];Vv=1-mv*mv
     gt=tuple(mv if z==0 else (1 if z==1 else -1) for z in mapping)
     x=sum(gt,F())/4;ga=h.fwht(gt);delta=[z-(y if i==0 else 0) for i,z in enumerate(ga)]
     W=b*Vv;h.equal(W+sum(z*z for z in ga[1:]),1-x*x,'law of variance')
     profile=h.shifted({},(p-2*p*p)*sum(z*z for z in delta))
     for g,z in zip(ga,delta):profile=h.combine((1,profile),(1,Phi((g-p*z)**2,p*p*z*z)))
     n=s+6
     def value(z):
      if z&((1<<s)-1)==0:return u[(z>>(s+2))&3]
      lab=mapping[(z>>s)&3]
      return v[(z>>(s+4))&3] if lab==0 else (1 if lab==1 else -1)
     t=tuple(value(z) for z in range(1<<n));m=query(t,0)
     kap=h.combine((1,rarity(p,b,Vu,Vv)),(-F(1,2),rarity(2*p,b,Vu,Vv)),(-F(1,2),rarity(F(0),b,Vu,Vv)))
     h.equal(m['d'],p*(1-x*y),'same physical fallback mismatch')
     h.equal(kap,h.combine((1,h.constant(p*Vu)),(W,k)),'owned release')
     h.equal(h.combine((1,m['B']),(-1,kap)),h.combine((1,profile),(W,c),(-W,k)),'profile decomposition')
     positive(h.shifted(h.combine((1,kap),(-1,m['B'])),8*m['d']),'B residual rate8')
     positive(h.shifted(h.combine((1,kap),(-1,m['D'])),11*m['d']),'D residual rate11')
     localcases+=1
  query.cache_clear();stats.cache_clear()

ORDER=(0,1,4,2,3,6,5,7)
def tree(u,v,orientation,C):
 global nodes,growth,treecases
 def label(z):
  X=z&1;A=(z>>1)&3;B=(z>>3)&1
  if X==0 and A==0:return 0
  if X==orientation and B==0:return 1
  return 2
 def value(z):
  lab=label(z)
  return u[(z>>4)&3] if lab==0 else v[(z>>6)&3] if lab==1 else 1
 def corestate(seed,offset,hist):
  rem=[i for i in (offset,offset+1) if hist[i]<0]
  out=[]
  for z in range(1<<len(rem)):
   a=[hist[offset],hist[offset+1]]
   for k,i in enumerate(rem):a[i-offset]=(z>>k)&1
   out.append(seed[a[0]+2*a[1]])
  return tuple(out)
 @lru_cache(None)
 def info(hist):
  rem=[i for i in range(8) if hist[i]<0];tt=[]
  for z in range(1<<len(rem)):
   bits=list(hist)
   for k,i in enumerate(rem):bits[i]=(z>>k)&1
   tt.append(value(sum(b<<i for i,b in enumerate(bits))))
  tt=tuple(tt);a,H,I,mu=stats(tt)
  controls=[i for i in range(4) if hist[i]<0];counts=Counter()
  for z in range(1<<len(controls)):
   bits=[max(0,x) for x in hist]
   for k,i in enumerate(controls):bits[i]=(z>>k)&1
   counts[label(sum(b<<i for i,b in enumerate(bits)))]+=1
  Q={};inherit={}
  for j,seed,offset in ((0,u,4),(1,v,6)):
   q=F(counts[j],1<<len(controls));ct=corestate(seed,offset,hist);_,hc,ic,mc=stats(ct)
   reserve=hc if C==0 else {}
   inherit=h.combine((1,inherit),(q,reserve))
   Q=h.combine((1,Q),(q,reserve),(1-mc*mc,phi(q)))
  return tt,H,I,Q,inherit
 stops={k:{'H':{},'Q':{},'data':F(),'ctrl':F()} for k in (3,5,8)}
 def recur(hist,level,spentD=F(),spentC=F()):
  global nodes,growth
  tt,H,I,Q,inherit=info(hist);nodes+=1;w=F(1,1<<level)
  if level in stops:
   out=stops[level];out['H']=h.combine((1,out['H']),(w,H));out['Q']=h.combine((1,out['Q']),(w,Q));out['data']+=w*spentD;out['ctrl']+=w*spentC
  if level==8:
   h.equal(H,{});h.equal(Q,{});return {},Q
  original=ORDER[level];remaining=[i for i in range(8) if hist[i]<0];m=query(tt,remaining.index(original));children=[]
  for b in (0,1):
   ch=list(hist);ch[original]=b;children.append(tuple(ch))
  childq=[info(ch)[3] for ch in children]
  rate=F(11) if original<4 else C+F(11,2)
  residual=h.shifted(h.combine((1,Q),(-F(1,2),childq[0]),(-F(1,2),childq[1]),(-1,m['D'])),rate*m['d'])
  positive(residual,'interleaved physical node price')
  if original<4:
   h.equal(inherit,h.combine((F(1,2),info(children[0])[4]),(F(1,2),info(children[1])[4])),'controller inherited reserve martingale')
  positive(h.shifted(h.combine((1,Q),(-F(1,2),childq[0]),(-F(1,2),childq[1])),C*m['d'] if original>=4 else 0),'expected reserve growth')
  for child in childq:
   diff=h.combine((1,child),(-1,Q))
   if sign(diff)>0:growth+=1
  rr=[]
  for ch in children:
   rv,_=recur(ch,level+1,spentD+(m['d'] if original>=4 else 0),spentC+(m['d'] if original<4 else 0));rr.append(rv)
  val=h.shifted(h.combine((1,m['D']),(F(1,2),rr[0]),(F(1,2),rr[1])),-11*m['d'])
  R=val if sign(val)>0 else {}
  positive(h.combine((1,Q),(-1,R)),'least reserve domination')
  return R,Q
 initial=(-1,)*8;tt,H,I,Q,inherit=info(initial)
 aa=stats(tt)[0];Ictrl=sum((aa[z]**2*(z&15).bit_count() for z in range(len(aa))),F())
 positive(h.shifted(h.combine((1,inherit),(-1,Q)),2*Ictrl),'original edge funding')
 reserve,_=recur(initial,0)
 for level,out in stops.items():
  rhs=h.shifted(h.combine((1,Q),(1,out['H']),(-1,out['Q']),(-1,H)),(C+F(11,2))*out['data']+11*out['ctrl'])
  positive(rhs,'actual stopped terminal ledger')
  positive(h.shifted(h.combine((1,Q),(-1,out['Q'])),C*out['data']),'stopped reserve expectation')
 h.equal(stops[8]['data']+stops[8]['ctrl'],I,'one physical influence account')
 treecases+=1
 return {'orientation':orientation,'C':str(C),'root_Q':[str(x) for x in h.interval(Q)],'complete_spent_data':str(stops[8]['data']),'complete_spent_control':str(stops[8]['ctrl']),'least_root_reserve':[str(x) for x in h.interval(reserve)],'stopped_nonzero_H':bool(stops[3]['H'] or stops[5]['H'])}

rows=[]
if MODE in ('pilot','local'):local(MODE=='pilot')
if MODE in ('pilot','trees'):
 cores=CORES[:2] if MODE=='pilot' else CORES
 for u in cores:
  for v in cores:
   for orientation in (0,1):
    for C in (F(0),F(4)):
     rows.append(tree(u,v,orientation,C));query.cache_clear();stats.cache_clear()
h.check(time.perf_counter()-h.START<h.CAP,'runtime cap')
out=ROOT/'out';out.mkdir(exist_ok=True)
result={'status':'PASS','mode':MODE,'local_cases':localcases,'complete_trees':treecases,'physical_tree_nodes':nodes,'positive_child_growth_occurrences':growth,'assertions':h.ASSERTS,'seconds':time.perf_counter()-h.START,'rows':rows}
(out/(MODE.upper()+'_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
