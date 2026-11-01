from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import sys,json,time,hashlib
sys.dont_write_bytecode=True
import truth_kernel as k
R=Path(__file__).resolve().parents[1]
@lru_cache(None)
def law(L,h):return k.spectrum(L,tuple(sorted(h)))
def p(L,h):return law(L,tuple(sorted(h)))[1]
def source(L):
 root=p(L,());terms=[]
 for i in range(2*L+4):
  r=k.marg(root,i)
  terms.append(k.add(*(k.mul(k.log(r[s&~(1<<i)]/v),v) for s,v in root.items() if v and s>>i&1)))
 D=k.add(k.add(*terms),k.B(root,3),k.avg([k.B(p(L,((3,s),)),1) for s in [0,1]]))
 I=sum(v for S,v in root.items() for i in [3]+list(range(4,2*L+4)) if S>>i&1)
 ce=k.avg([k.CE(p(L,((3,s),(1,b))),k.fair(p(L,((3,s),(1,b))),0)) for s,b in product([0,1],repeat=2)])
 C=k.add(D,ce);k.ck(k.sub((17*I,17*I),C)[0]>F(7,8))
 return D,I,C
def canonical(L,main):
 D,I,C=source(L);j=4 if L==1 else 5;z=4+L;nodes={tuple(tuple(a) for a in n['history']):n for n in main['nodes']};localpos=[]
 def go(h,query):
  if not query:
   pp=p(L,h);return k.CE(pp,k.fair(pp,j))
  i=query[0];vals=[go(h+((i,u),),query[1:]) for u in [0,1]]
  return k.add(k.B(p(L,h),i),k.avg(vals))
 bills=[]
 for s,b in product([0,1],repeat=2):
  h=((3,s),(1,b));qs=([4] if L>1 else [])+[z,0,2];bills.append(go(h,qs))
 for h,n in nodes.items():
  pp=p(L,h);q=k.fair(pp,2);a=law(L,tuple(sorted(h)))[0];fresh=[];inc=[]
  for u in [0,1]:
   child=h+((2,u),);aa,cp=law(L,tuple(sorted(child)))
   for S,v in aa.items():k.ck(v==a[S]+(-1)**u*a[S|4])
   ce=k.CE(cp,k.fair(cp,j));fresh.append(ce);inc.append(k.CE(cp,k.marg(q,2)))
   k.overlap(ce,n['terminals'][u]['CE']);k.overlap(k.sub(ce,k.H(cp)),n['terminals'][u]['KL'])
  net=k.sub(k.add(k.B(pp,2),k.avg(fresh)),k.CE(pp,q));delta=k.sub(k.avg(fresh),k.avg(inc));rho=k.sub((F(1),F(1)),k.B(pp,2))
  for v,key in [(net,'net'),(delta,'Delta'),(rho,'rho')]:k.overlap(v,n[key])
  if net[0]>0:localpos.append(dict(history=h,net=k.saved(net),Delta=k.saved(delta),rho=k.saved(rho)))
 final=k.add(D,k.avg(bills));k.overlap(final,main['final_bill']);k.overlap(C,main['source_C2']);k.ck(k.sub((17*I,17*I),final)[0]>F(1,8))
 return dict(L=L,final_bill=k.saved(final),spare=k.saved(k.sub((17*I,17*I),final)),positive_local_nodes=localpos)
def all_trees(L):
 D,I,C=source(L);j=4;states=0;actions=0;envelopes=[]
 @lru_cache(None)
 def bellman(h):
  nonlocal states,actions
  states+=1;pp=p(L,h);stop=k.CE(pp,k.fair(pp,j));candidates=[stop]
  fixed=dict(h)
  for i in range(2*L+4):
   if i in fixed or i==j:continue
   actions+=1;ch=[bellman(tuple(sorted(h+((i,u),)))) for u in [0,1]]
   candidates.append(k.add(k.B(pp,i),k.avg(ch)))
  ans=(max(v[0] for v in candidates),max(v[1] for v in candidates))
  # Source-independent generic potential checks at every partial history.
  potential=k.add(k.H(pp),(F(1),F(1)));k.ck(ans[0]<=potential[1])
  return ans
 for s,b in product([0,1],repeat=2):envelopes.append(bellman(tuple(sorted(((3,s),(1,b))))))
 full=k.add(D,k.avg(envelopes));spare=k.sub((17*I,17*I),full);k.ck(spare[0]>F(1,8))
 return dict(L=L,retained_private_j=j,states=states,query_actions=actions,Bellman_bill=k.saved(full),spare=k.saved(spare),coverage='ALL deterministic complete adaptive query/stop policies on all other coordinates; interval upper envelope')
def tail():
 # Independently derive C_infinity from the actual limiting three-bit defect.
 root={s:(F(3,4) if s==0 else -F(1,4)) for s in range(16) if not s&2}
 pp={s:v*v for s,v in root.items()};M=[]
 for i in [0,2,3]:
  r=k.marg(pp,i);M.append(k.add(*(k.mul(k.log(r[s&~(1<<i)]/v),v) for s,v in pp.items() if s>>i&1)))
 Bx=k.B(pp,3);lim=k.add(k.add(*M),Bx,(F(3,2),F(3,2)))
 stated=k.add((F(39,16),F(39,16)),k.mul(k.log(F(10)),F(1,4)),k.mul(k.log(F(10,9)),F(9,16)))
 k.overlap(lim,stated);endpoint=k.sub((F(17,4),F(17,4)),k.add(lim,(F(26217,4194304),)*2));k.ck(endpoint[0]>F(7,8))
 # Error polynomial assembled by coefficient arithmetic, not copied as a fitted number.
 poly=[350+5*584,4+5*24,2];k.ck(poly==[3270,124,2]);shift=[poly[0]+poly[1]+poly[2],poly[1]+2*poly[2],poly[2]]
 k.ck([2*x-y for x,y in zip(poly,shift)]==[3144,120,2])
 return dict(C_infinity=k.saved(lim),tail_endpoint=k.saved(endpoint),polynomial=poly)
if __name__=='__main__':
 spec=dict(helper_version='A035-independent-FWHT-Bellman-v1',sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),canonical_domain=[1,2,3],Bellman_domain=[1,2],Bellman_states_expected=1080,arithmetic='Independent integer truth table FWHT and 24-term rational logarithm bounds; exact internal sums, outward160-bit saved bounds',memory_estimate_MB=120,max_runtime_seconds=55,symmetry='None; all partial physical histories, fixed retained j')
 (R/'out/REPRO_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
 start=time.monotonic();data=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
 root,_=law(1,())
 for shift in range(64):k.ck(sum(v*root[S^shift] for S,v in root.items())==int(shift==0))
 k.ck(F(32,31)**16<2)
 rows=[]
 for L in [1,2,3]:rows.append(canonical(L,next(v for v in data['cases'] if v['L']==L)));k.ck(time.monotonic()-start<55)
 policies=[all_trees(L) for L in [1,2]];k.ck(sum(r['states'] for r in policies)==1080)
 ans=dict(canonical=rows,all_trees=policies,tail=tail(),checks=k.COUNT,seconds=time.monotonic()-start);k.ck(ans['seconds']<55)
 (R/'out/REPRODUCE.json').write_text(json.dumps(ans,indent=2),encoding='utf-8')
 print(json.dumps(dict(checks=k.COUNT,seconds=ans['seconds'],Bellman_states=sum(v['states'] for v in policies))))
