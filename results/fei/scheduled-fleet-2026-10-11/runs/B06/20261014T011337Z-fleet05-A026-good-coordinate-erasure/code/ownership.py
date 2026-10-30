import json,time
from fractions import Fraction as F
from pathlib import Path
import check as c
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();trees=[];checks=0
def split(h,i,bit):
 return [h[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(len(h)//2)]
def stat(h,policy,partial):
 mu=F(sum(h),len(h));V=1-mu*mu
 n=len(h).bit_length()-1
 I=sum(F(sum(h[x]!=h[x^(1<<i)] for x in range(len(h))),len(h)) for i in range(n))
 if not V or not n or (partial and n<=1):return F(0),V,F(0),I
 ds=[F(sum(h[x]!=h[x^(1<<i)] for x in range(len(h))),len(h)) for i in range(n)]
 i=0 if policy=='forward' else n-1 if policy=='reverse' else max(range(n),key=lambda j:(ds[j],-j))
 plus,minus=split(h,i,1),split(h,i,0)
 mup,mum=F(sum(plus),len(plus)),F(sum(minus),len(minus))
 gamma=(mup-mum)/2
 assert V-((1-mup*mup)+(1-mum*mum))/2==gamma*gamma
 q1,v1,s1,l1=stat(plus,policy,partial);q2,v2,s2,l2=stat(minus,policy,partial)
 Q=gamma*gamma+(q1+q2)/2;VL=(v1+v2)/2
 S=ds[i]+(s1+s2)/2;IL=(l1+l2)/2
 assert Q==V-VL and S==I-IL
 return Q,VL,S,IL
outer=[]
for mask,f in c.truths(2):
 D=[F(f[2*r+1]-f[2*r],2) for r in range(2)]
 outer.append((mask,F(sum(d*d for d in D),2),c.B(c.b.walsh(f),0)))
for n in range(4):
 for mask,h in c.truths(n):
  V=1-F(sum(h),len(h))**2
  for policy in ['forward','reverse','largest']:
   for partial in [False,True]:
    Q,VL,S,IL=stat(h,policy,partial)
    if not partial:assert VL==0 and Q==V
    for om,delta,Bz in outer:
     charged=c.b.mul(Bz,Q);expected=c.b.mul(Bz,V-VL)
     assert charged==expected
     assert delta*S>=0;checks+=1
    trees.append({'n':n,'mask':mask,'policy':policy,'partial':partial,'variance_drop':str(Q),'leaf_variance':str(VL),'spent_encoder_influence':str(S),'leaf_encoder_influence':str(IL)})
assert len(trees)==1668 and checks==26688
(ROOT/'out/variance_ownership.json').write_text(json.dumps({'status':'PASS','encoder_trees':len(trees),'shadow_cases':checks,'records':trees},indent=2)+'\n',encoding='utf-8')
bent=[]
for k in [4,6,8,10,12]:
 delta=F(1,1<<k);s=F(1,1<<(k//2))
 plus=((1<<k)+(1<<(k//2)))//2;minus=(1<<k)-plus
 Bz={};c.add(Bz,c.phi((s-delta)**2,delta**2),plus);c.add(Bz,c.phi((s+delta)**2,delta**2),minus)
 lower=dict(Bz);c.b.addlog(lower,2,-delta*(k-1));c.positive(lower)
 # Independently reconstruct actual k-bit quadratic bent and flipped slices.
 g=[-1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2 else 1 for x in range(1<<k)]
 W=c.b.walsh(g);assert set(abs(w) for w in W)=={1<<(k//2)}
 gp=g[:];gp[0]=-gp[0]
 assert F(sum(u!=v for u,v in zip(g,gp)),len(g))==delta
 actual_outer=[v for u,w in zip(g,gp) for v in [u,w]]
 assert c.B(c.b.walsh(actual_outer),0)==Bz
 Pi=F(3,2)*delta
 bent.append({'k':k,'selector_influence':str(delta),'shadow_charge_prime_log':c.b.serial(Bz),'shadow_charge_over_encoder_spend':c.b.iv((c.b.interval(Bz)[0]/Pi,c.b.interval(Bz)[1]/Pi)),'analytic_ratio_lower':str(F(2*(k-1),3))})
 assert time.perf_counter()-start<60
result={'status':'PASS','encoder_trees':len(trees),'shadow_ownership_checks':checks,'bent_cases':len(bent),'elapsed_seconds':time.perf_counter()-start,'all_k_bridge':'PROOF.md section 5; five finite instances only corroborate','records':bent}
(ROOT/'out/bent_bank_obstruction.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
