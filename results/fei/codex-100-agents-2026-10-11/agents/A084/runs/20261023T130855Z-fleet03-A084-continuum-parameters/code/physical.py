"""Literal whole-function Walsh and physical-query audit; no outer approximation."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
import seed_engine as e
import critical as c
R=Path(__file__).resolve().parents[1];CHECKS=0
def ck(v):
 global CHECKS
 assert v
 CHECKS+=1
def eta_profile(q):return e.mul(e.lp(q),-q) if q else {}
def correction(p):return e.add(eta_profile((1-p)**2),eta_profile(p*p),e.mul(eta_profile((1-2*p)**2),F(-1,2)),{2:4*p*(1-p)})
def fresh(t):return (1,)*len(t)+t
def run(pilot):
 start=time.perf_counter();d=2 if pilot else 3;N=1<<d
 root=json.loads((R/'out'/('PILOT_ROOT.json' if pilot else 'CRITICAL_POINT.json')).read_text(encoding='utf-8'))
 K=F(49,10) if pilot else F(root['certified_rational_upper'])
 rows=[];seen=set()
 @lru_cache(None)
 def stats(t):return e.core(t)
 @lru_cache(None)
 def hull(t,k):
  z=stats(t);best=e.pos(e.add(z['H'],{2:-k*z['I']}))
  for i in range((len(t)-1).bit_length()):
   v=e.mean([hull(e.child(t,i,b),k) for b in range(2)])
   if e.cmp(v,best)>0:best=v
  return best
 def check(t,label):
  if t in seen:return
  seen.add(t);g=stats(t);ft=fresh(t);f=stats(ft);p=F(sum(v==-1 for v in t),len(t))
  C=e.add(f['H'],e.neg(e.mul(g['H'],F(1,2))))
  ck(C==correction(p));ck(f['I']==g['I']/2+p)
  ck(e.cmp(C,{2:K*p})<=0)
  live=e.child(ft,(len(t)-1).bit_length(),1);dead=e.child(ft,(len(t)-1).bit_length(),0)
  ck(live==t and dead==(1,)*len(t))
  rg=hull(t,K);rf=hull(ft,K);ck(rf==e.mul(rg,F(1,2)))
  # Entropy itself is a supplied coherent inner envelope, giving nonzero tests.
  W=e.mul(g['H'],F(1,2));slack=e.add({2:K*f['I']},e.neg(f['H']),W)
  ck(e.cmp(slack,{})>=0)
  for i in range((len(t)-1).bit_length()):
   kids=[e.child(t,i,b) for b in range(2)];ck(all(e.child(ft,i,b)==fresh(kids[b]) for b in range(2)))
   hs=e.mean([e.mul(stats(x)['H'],F(1,2)) for x in kids]);ck(e.cmp(W,hs)>=0)
   # Full spectrum and influence price on BOTH children, no terminal erased.
   for x in kids:
    y=stats(fresh(x));s=stats(x);px=F(sum(v==-1 for v in x),len(x))
    ck(e.add(y['H'],e.neg(e.mul(s['H'],F(1,2))))==correction(px))
    ck(y['I']==s['I']/2+px)
  rows.append({'label':label,'core_bits':(len(t)-1).bit_length(),'p':str(p),'complete_correction':e.pack(C),'fresh_physical_influence':str(p),'K':str(K),'hull_equality':'EXACT','supplied_entropy_envelope':'PASS'})
 for mask in range(1<<N):
  check(tuple(-1 if mask>>x&1 else 1 for x in range(N)),f'table{mask}')
 if not pilot:
  special=tuple(-1 if x<7 else 1 for x in range(32));check(special,'fixed5bit_7negative')
  pp=F(7,32);under=e.add(correction(pp),{2:-F(487,100)*pp});ck(e.cmp(under,{})>0)
  # A below-hypothesis example must REJECT unconditional hull contraction.
  g=(-1,1,1,1);small=hull(g,F(1));large=hull(fresh(g),F(1))
  ck(e.cmp(large,e.mul(small,F(1,2)))>0)
  counter={'K':'1','core':list(g),'core_hull':e.pack(small),'full_hull':e.pack(large),'contracted_inner':e.pack(e.mul(small,F(1,2))),'verdict':'REJECT_CONTRACTION_BELOW_HYPOTHESIS','scalar_underprice_control':{'p':'7/32','lambda':'487/100','excess':e.pack(under),'scope':'Scalar payment failure, NOT a hull/FEI counterexample'}}
  (R/'out/COUNTERCONTROLS.json').write_text(json.dumps(counter,indent=2)+'\n',encoding='utf-8')
 result={'status':'PASS','core_tables':len(seen),'all_three_bit_tables':not pilot,'complete_fourier_core_and_full_functions_checked':stats.cache_info().currsize,'own_assertions':CHECKS,'engine_assertions':e.CHECKS,'recorded_assertions':CHECKS+e.CHECKS,'K':str(K),'runtime_seconds':time.perf_counter()-start,'all_real_coverage':'PROOF.md unique critical point plus root certificate, not these finite tests','full_fei':'OPEN'}
 ck(time.perf_counter()-start<55)
 prefix='PILOT_PHYSICAL' if pilot else 'PHYSICAL'
 (R/'out'/(prefix+'_CASES.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
 (R/'out'/(prefix+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
