from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import runpy,json,time,sys
ROOT=Path(__file__).resolve().parents[1]
U=runpy.run_path(str(ROOT.parent/'20261011T221822Z-fleet05-A048-tensor-stress/code/check.py'))
add,scale,entropy,hb,walsh,influence,entatom,interval=[U[k] for k in ('add','scale','entropy','hb','walsh','influence','entatom','interval')]
checks=0
def eq(a,b):
 global checks
 assert a==b,(a,b);checks+=1
def nonneg(v):
 global checks
 if v: assert interval(v)[0]>=0,v
 checks+=1
def ser(v):return {str(k):str(x) for k,x in sorted(v.items())}
def spectral(tab):return [x*x for x in walsh(tab)]
def family(s,n,pad):
 return [(1-2*int((z&((1<<s)-1))!=((1<<s)-1) and ((z>>s)&((1<<n)-1))==((1<<n)-1)))*(-1 if pad and z>>(s+n)&1 else 1) for z in range(1<<(s+n+pad))]
def reserve(s,n,pad):
 if not s:return {}
 q=F(1,1<<s);delta=F(1,1<<n)
 return hb(q) if pad else scale(entatom(1-q),4*delta*(1-delta))
def family_case(m,n,pad):
 root=family(m,n,pad);p=spectral(root);h=entropy(p);t=F(1,1<<m);delta=F(1,1<<n)
 ic=F(sum(sum(root[z]!=root[z^(1<<i)] for z in range(len(root))) for i in range(m)),len(root))
 eq(ic,2*m*t*delta)
 M=J=D=K=res={};leafH={};leafI=F(0)
 for s in range(m,0,-1):
  tab=family(s,n,pad);w=F(1,1<<(m-s));p=spectral(tab);children=[tab[b::2] for b in (0,1)]
  hchildren=scale(add(*(entropy(spectral(ch)) for ch in children)),F(1,2))
  retained=[p[2*z]+p[2*z+1] for z in range(len(p)//2)]
  mm=add(entropy(p),scale(entropy(retained),-1));jj=add(entropy(retained),scale(hchildren,-1));dd=add(mm,jj)
  kap=add(reserve(s,n,pad),scale(reserve(s-1,n,pad),F(-1,2)))
  nonneg(kap)
  M=add(M,scale(mm,w));J=add(J,scale(jj,w));D=add(D,scale(dd,w));K=add(K,scale(kap,w));res=add(res,scale(add(dd,scale(kap,-1)),w))
  # b=0 terminates in the negative point defect; the final b=1 selects +1.
  leafH=add(leafH,scale(entropy(spectral(children[0])),w/2));leafI+=w/2*influence(children[0])
  if s==1:
   leafH=add(leafH,scale(entropy(spectral(children[1])),w/2));leafI+=w/2*influence(children[1])
 eq(K,reserve(m,n,pad));eq(add(K,res),D);eq(add(leafH,D),h)
 eq(influence(root)-leafI,ic)
 hn=[1-2*int(z==(1<<n)-1) for z in range(1<<n)]
 eq(leafH,scale(entropy(spectral(hn)),1-t));eq(leafI,pad+(1-t)*2*n*delta)
 result={'m':m,'n':n,'common_parity':bool(pad),'control_influence':str(ic),'root_entropy':ser(h),'terminal_entropy':ser(leafH),'terminal_influence':str(leafI),'label_reserve':ser(K),'M':ser(M),'J':ser(J),'controller_decrement':ser(D),'signed_residual_sum':ser(res)}
 (ROOT/'out'/f'family_m{m}_n{n}_p{pad}.json').write_text(json.dumps(result,indent=2)+'\n')
 return result,p
def H(j,inds):
 d=defaultdict(F)
 for key,p in j.items():d[tuple(key[i] for i in inds)]+=p
 return entropy(d.values())
def MI(j,a,b):return add(H(j,a),H(j,b),scale(H(j,a+b),-1))
def schedule_case(tab,policy):
 n=(len(tab)-1).bit_length()
 @lru_cache(None)
 def node(hist):
  used=sum(1<<i for i,b in hist);inds=[i for i in range(n) if not (used>>i&1)];base=sum(b<<i for i,b in hist)
  arr=[tab[base+sum(((z>>a)&1)<<i for a,i in enumerate(inds))] for z in range(1<<len(inds))]
  law={sum(((s>>a)&1)<<i for a,i in enumerate(inds)):x*x for s,x in enumerate(walsh(arr)) if x}
  return law,influence(arr)
 def query(hist):
  if policy=='first' and hist:return None
  if policy=='adaptive' and (len(hist)==2 or len(hist)==1 and hist[0][1]==0):return None
  if policy=='parity' and len(hist)==2:return None
  remaining=[i for i in range(n) if i not in [a for a,b in hist]]
  if not remaining:return None
  if policy=='parity' and hist:return 1 if hist[0][1]==0 else 2
  return remaining[0]
 rootlaw,rootI=node(());todo={(s,s,()):p for s,p in rootlaw.items()};leaves=defaultdict(F)
 while todo:
  nxt=defaultdict(F)
  for (s0,s,hist),mass in todo.items():
   i=query(hist)
   if i is None:leaves[(s0,s,hist)]+=mass;continue
   plaw=node(hist)[0];T=s&~(1<<i);q=plaw.get(T,F(0))+plaw.get(T|(1<<i),F(0));eq(q>0,True)
   for b in (0,1):
    child=hist+((i,b),);cl=node(child)[0];prob=cl.get(T,F(0))/(2*q)
    if prob:nxt[(s0,T,child)]+=mass*prob
  todo=dict(nxt)
 eq(sum(leaves.values()),1)
 hmass=defaultdict(F);slaw=defaultdict(lambda:defaultdict(F));A=0
 for (s,w,hist),p in leaves.items():
  hmass[hist]+=p;slaw[hist][w]+=p
  for i,b in hist:A|=1<<i
 for hist,prob in hmass.items():
  eq(prob,F(1,1<<len(hist)));eq({s:p/prob for s,p in slaw[hist].items()},node(hist)[0])
 removed=rootI-sum((prob*node(hist)[1] for hist,prob in hmass.items()),F(0))
 a=sum((p*(s&A).bit_count() for s,p in rootlaw.items()),F(0))
 dj=defaultdict(F)
 for (s,w,hist),p in leaves.items():dj[(s,s&~w)]+=p
 eq(sum((p*d.bit_count() for (s,d),p in dj.items()),F(0)),removed)
 e=add(H(dj,(0,1)),scale(H(dj,(0,)),-1))
 theta=removed/a if a else F(0);ce={};KL={}
 for s,sp in rootlaw.items():
  labels=[i for i in range(n) if (s&A)>>i&1];norm=F(0)
  for z in range(1<<len(labels)):
   d=sum(((z>>j)&1)<<i for j,i in enumerate(labels));rho=theta**d.bit_count()*(1-theta)**(len(labels)-d.bit_count());norm+=rho
   p=dj.get((s,d),F(0))
   if p:
    eq(rho>0,True);ce=add(ce,scale(U['logvec'](rho),-p));KL=add(KL,scale(U['logvec'](p/sp/rho),p))
  eq(norm,1)
 capacity=scale(hb(theta),a)
 eq(ce,capacity);eq(add(e,KL),capacity);nonneg(KL)
 # Actual conditional injection equals deletion conditional entropy.
 inj=add(H(leaves,(0,1)),scale(H(leaves,(0,)),-1));eq(inj,e)
 rootj=MI(leaves,(0,),(2,));wj=MI(leaves,(1,),(2,));nonneg(add(rootj,e,scale(wj,-1)))
 if policy=='parity':eq(e,{2:F(1)})
 return {'n':n,'policy':policy,'R':str(removed),'a':str(a),'injection':ser(e),'capacity':ser(capacity),'KL':ser(KL)}
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;results=[];base=None
 for m in ([1] if pilot else range(1,5)):
  for n in ([3] if pilot else range(1,7)):
   pair=[]
   for pad in (0,1):
    rec,p=family_case(m,n,pad);pair.append(rec);results.append(rec)
    if (m,n,pad)==(1,3,1):base={s:p for s,p in enumerate(p) if p}
   for k in ('root_entropy','terminal_entropy','M','J','controller_decrement','control_influence'):eq(pair[0][k],pair[1][k])
   eq(F(pair[1]['terminal_influence'])-F(pair[0]['terminal_influence']),1)
   # Exact signed compensation for the entire reserve boost.
   forkey=lambda rec,k:{int(a):F(b) for a,b in rec[k].items()}
   eq(add(forkey(pair[1],'signed_residual_sum'),scale(forkey(pair[0],'signed_residual_sum'),-1)),scale(add(forkey(pair[1],'label_reserve'),scale(forkey(pair[0],'label_reserve'),-1)),-1))
   if (m,n)==(1,6):
    dd=forkey(pair[1],'controller_decrement');lo,hi=interval(dd);eq(hi<F(1,4),True)
    cert={'m':m,'n':n,'reserve':'1','controller_influence':'1/64','reserve_over_controller_influence':'64','decrement_interval':[str(lo),str(hi)],'signed_residual_strict_upper':'-3/4','proof':'signed residual=D-1 and certified D<1/4'}
    (ROOT/'out'/'SIGNED_CANCELLATION_CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n')
 review=[]
 for mask in (range(2) if pilot else range(16)):
  tab=[1-2*((mask>>z)&1) for z in range(4)]
  for policy in ('complete','first','adaptive'):review.append(schedule_case(tab,policy))
 review.append(schedule_case([(-1)**z.bit_count() for z in range(8)],'parity'))
 formulas=[]
 if not pilot:
  for m in range(1,5):
   for n in range(1,9):
    t=F(1,1<<m);delta=F(1,1<<n);ic=2*m*t*delta
    eq(m*t/ic,F(1<<(n-1)))
    formulas.append({'m':m,'n':n,'control_influence':str(ic),'reserve_to_control_influence_lower_bound':str(F(1<<(n-1)))})
  for copies in (1,2,3):
   joint={():F(1)}
   for _ in range(copies):joint={key+(s,):p*q for key,p in joint.items() for s,q in base.items()}
   eq(entropy(joint.values()),scale(entropy(base.values()),copies))
   eq(sum((p*sum(s.bit_count() for s in key) for key,p in joint.items()),F(0)),copies*sum((p*s.bit_count() for s,p in base.items()),F(0)))
 summary={'status':'PASS','case_count':9 if pilot else 132,'assertions':checks,'seconds':time.perf_counter()-start,'families':results,'schedule_review':review,'formula_certificates':formulas}
 (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps({k:v for k,v in summary.items() if k not in ('families','schedule_review','formula_certificates')}))
if __name__=='__main__':main()
