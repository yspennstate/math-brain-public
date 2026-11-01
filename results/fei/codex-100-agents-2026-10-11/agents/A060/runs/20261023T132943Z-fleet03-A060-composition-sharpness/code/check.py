from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json,time,sys,hashlib
import exact as e

ROOT=Path(__file__).resolve().parents[1]
CHECKS=0
def ck(x):
 global CHECKS
 assert x
 CHECKS+=1
def overlap(a,b):return not(a[1]<b[0] or b[1]<a[0])
def rational(x):return e.times(e.ln(Q(2)),Q(x))
def I(g):return sum((inf(g,i) for i in range(len(g).bit_length()-1)),Q(0))
def inf(g,i):return Q(sum(g[x]!=g[x^(1<<i)] for x in range(len(g))),len(g))
def cut(g,i,a):return tuple(v for x,v in enumerate(g) if (x>>i)&1==a)
@lru_cache(None)
def H(g):return e.H(g)
def D(g,i):return e.add(H(g),e.neg(e.times(e.add(H(cut(g,i,0)),H(cut(g,i,1))),Q(1,2))))
def mean(g):return Q(sum(g),len(g))
def kap():
 l,h=e.bits(e.ln(Q(3)))
 return 3-Q(2)/(1+l),3-Q(2)/(1+h)
def prof(K,C,mu,tf=e.fwht):
 k,c=tf(K),tf(C); t=Q(sum(C),len(C))
 return e.add(e.add(*(e.eta((x+mu*y)**2) for x,y in zip(k,c))),e.neg(e.times(e.eta(mu*mu),t)),e.times(e.add(*(e.eta(y*y) for y in c)),1-mu*mu))
def wrap(K,C,g):return tuple(K[x]+C[x]*v for v in g for x in range(len(K)))
def restrict(g,states):
 n=len(states)
 return tuple(g[x] for x in range(1<<n) if all(a==2 or (x>>j)&1==a for j,a in enumerate(states)))
def source(m=4):
 b=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2)) for x in range(1<<m))
 C=tuple(int(x==(1<<m)-1) for x in range(1<<m))
 return tuple(b[x]-C[x] for x in range(len(b))),C,b
def coretest(n):
 k=kap()[0]; counts=0
 for mask in range(1<<(1<<n)):
  g=tuple(1-2*((mask>>x)&1) for x in range(1<<n)); total=I(g)
  for i in range(n):
   d=inf(g,i);delta=min(d,1-d)
   iso=e.add(rational(total-d),e.times(e.ln(delta),delta)) if delta else rational(total-d)
   ck(iso[1]>=0)
   dec=D(g,i)
   ck(dec[1]<=e.times(rational(k),total)[0] or total==0 and dec[0]<=0<=dec[1])
   ck(total==d+(I(cut(g,i,0))+I(cut(g,i,1)))/2)
   counts+=1
 return {'n':n,'coordinate_cases':counts}
def wrappers():
 counts=0; C=(0,0,0,1)
 for bm in range(16):
  K=tuple((1-2*((bm>>x)&1)) if not C[x] else 0 for x in range(4))
  for gm in range(256):
   g=tuple(1-2*((gm>>x)&1) for x in range(8));t=Q(1,4);F=wrap(K,C,g);ep=prof(K,C,mean(g))
   ck(overlap(ep,e.add(H(F),e.neg(e.times(H(g),t)))))
   ck(ep[1]>=0 and ep[0]<=rational(Q(3))[1])
   for i in range(3):
    children=[cut(g,i,a) for a in (0,1)]
    ec=e.times(e.add(*(prof(K,C,mean(h)) for h in children)),Q(1,2))
    physical=D(F,i+2); gi=D(g,i)
    predicted=e.add(e.times(gi,t),ep,e.neg(ec))
    ck(overlap(physical,predicted))
    ck(gi[1]<=e.times(rational(kap()[0]),I(g))[0] or I(g)==0)
    counts+=1
 return {'wrapper_core_edges':counts,'wrapper_roots':4096}
def histories():
 K,C,b=source();c=Q(1,16);B0=Q(7);G=tuple(-1 if x==0 else 1 for x in range(8))
 old=e.times(D(G,0),c);ck(old[0]>0)
 start=prof(K,C,Q(0)); L=e.add(rational(B0),e.neg(old),e.neg(start));ck(L[0]>rational(Q(1))[1])
 rows=[];nodes=edges=0
 k=kap()[0]
 for states in product(range(3),repeat=4):
  Kr,Cr=restrict(K,states),restrict(C,states);t=Q(sum(Cr),len(Cr))
  for olda in (0,1):
   ga=cut(G,0,olda)
   for tag in (0,1,-1):
    h=tuple(ga)+tuple(-v for v in ga) if tag==0 else tuple(tag*v for v in ga)
    F=wrap(Kr,Cr,h); ep=prof(Kr,Cr,0 if tag==0 else mean(h))
    ck(overlap(ep,e.add(H(F),e.neg(e.times(H(ga),t)))))
    ck(ep[1]>=0)
    for i in range(2):
     children=[cut(h,i,a) for a in (0,1)]
     actual=D(F,i+len(states)-states.count(0)-states.count(1))
     dg=D(ga,i)
     childprof=e.times(e.add(*(prof(Kr,Cr,mean(hc)) for hc in children)),Q(1,2))
     expect=e.add(e.times(dg,t),ep,e.neg(childprof))
     ck(overlap(actual,expect))
     cash=e.add(e.times(rational(k),t*I(ga)),e.neg(e.times(dg,t)))
     ck(cash[1]>=0)
     # SAME source plus original core owner, retaining BOTH complete children.
     owner_before=e.add(L,ep,e.times(rational(k),t*I(ga)))
     owner_after=e.add(L,childprof,cash)
     ck(overlap(e.add(owner_before,e.neg(owner_after)),actual))
     for hc in children:ck(prof(Kr,Cr,mean(hc))[1]>=0)
     edges+=1
    nodes+=1
 # Physical full policy: old y0; query exterior x0; collapse tag; query y1;
 # then exhaust remaining exterior. Every old sibling and both tag outcomes kept.
 def tree(F, labels, extra=False):
  if not labels:return H(F),(0,0),1
  i=labels[0]; cs=[cut(F,i,a) for a in (0,1)]
  rest=[j-1 if j>i else j for j in labels[1:]]
  sub=[tree(h,rest) for h in cs]
  terminal=e.times(e.add(*(z[0] for z in sub)),Q(1,2))
  debit=e.add(D(F,i),e.times(e.add(*(z[1] for z in sub)),Q(1,2)))
  ck(overlap(H(F),e.add(terminal,debit)))
  return terminal,debit,sum(z[2] for z in sub)
 tagged=tuple(G)+tuple(-v for v in G);root=wrap(K,C,tagged)
 terminal,debit,leaves=tree(root,[4,0,7,5,1,2,3])
 ck(leaves==128)
 rows.append({'old_debit':e.serial(old),'L':e.serial(L),'full_terminal_mean':e.serial(terminal),'actual_total_debit':e.serial(debit),'full_leaves':leaves})
 return {'reached_profiles':nodes,'extra_core_edges':edges,'fixture':rows}
def resets():
 rows=[]
 for m in (4,8,12):
  K,C,b=source(m);c=Q(1,1<<m)
  # Two disjoint actual tag sectors: no giant tagged table needed.
  plus=tuple(x+y for x,y in zip(K,C));minus=tuple(x-y for x,y in zip(K,C))
  rootH=e.add(e.add(*(e.eta(x*x) for x in e.fwht(K))),e.add(*(e.eta(x*x) for x in e.fwht(C))))
  dec=e.add(rootH,e.neg(e.times(e.add(H(plus),H(minus)),Q(1,2))))
  ck(dec[0]>rational(c*(m-1))[1]);ck(dec[0]>rational(c*kap()[1])[1])
  rows.append({'m':m,'influence':str(c),'D_over_Inf':e.serial(e.times(dec,1/c)),'both_terminal_entropies':[e.serial(H(plus)),e.serial(H(minus))]})
 return {'reset_obstructions':rows}
def repro():
 cases=0
 for gm in range(16):
  g=tuple(1-2*((gm>>x)&1) for x in range(4))
  for bm in range(4):
   K=(1-2*(bm&1),0);C=(0,1);F=wrap(K,C,g)
   ck(e.direct(F)==e.fwht(F))
   ep=prof(K,C,mean(g),e.direct)
   ck(overlap(ep,e.add(e.H(F,e.direct),e.neg(e.times(e.H(g,e.direct),Q(1,2))))))
   for i in range(2):
    ds=e.add(e.H(F,e.direct),e.neg(e.times(e.add(*(e.H(cut(F,i+1,a),e.direct) for a in (0,1))),Q(1,2))))
    ck(overlap(ds,D(F,i+1)))
   cases+=1
 h=(1,1,1,-1);ck(I(h)==1);ck(overlap(D(h,0),rational(2)))
 return {'independent_direct_character_roots':cases,'AND2_lower_rate':2}
def main(mode):
 global CHECKS
 start=time.perf_counter();CHECKS=0
 if mode=='pilot':result=coretest(2)
 elif mode=='core':result=coretest(3)
 elif mode=='wrapper':result=wrappers()
 elif mode=='histories':result=histories()
 elif mode=='reset':result=resets()
 elif mode=='reproduce':result=repro()
 else:raise ValueError(mode)
 ck(3**3<2**5);ck(e.ln(Q(2))[0]>2*e.SCALE//3)
 result.update(mode=mode,status='PASS',checks=CHECKS,elapsed_s=time.perf_counter()-start,kappa_interval=[str(x) for x in kap()],kappa_display=[float(x) for x in kap()],helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 ck(result['elapsed_s']<55)
 result['checks']=CHECKS
 (ROOT/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8',newline='')
 print(json.dumps({k:result[k] for k in ('mode','status','checks','elapsed_s','kappa_display')}),flush=True)
 H.cache_clear()
if __name__=='__main__':main(sys.argv[1])
