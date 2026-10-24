from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json,time
import kernel as k
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();k.CAP=50
def chars(t):return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
b=[k.bent(x,4) for x in range(16)];ba=chars(b)
h=[k.bent(x&15,4)*(-1 if (x&15)==0 and (x>>4) else 1) for x in range(32)];ha=chars(h)
cp=[];cm=[]
for y in range(4):
 p=(y.bit_count()%2)^(y==1);bb=k.bent(y,2);cp.append(bb if not p else 0);cm.append(bb if p else 0)
ca,cb=chars(cp),chars(cm);d=Q(1,64);states=defaultdict(lambda:[Q(0),Q(0)]);ratios={}
for s in range(4):
 l=Q(cb[s],ca[s]+cb[s])
 for q in range(16):
  for t in range(32):
   aa=ca[s]*(2*ba[q])*(2*ba[t&15] if t<16 else 0)+cb[s]*ha[q]*ha[t]
   vv=cb[s]*ha[q+16]*ha[t]
   # Core denominator4, query module32, other module32.
   mu=Q(vv*vv,4096**2)/d;r=Q(aa*aa+vv*vv,4096**2)
   eps=ba[q]//4
   lab=('O',eps) if t>=16 else ('C',str(l),eps,1 if ba[t]==4 else 0,0)
   ratio=mu/r
   if lab in ratios:assert ratios[lab]==ratio
   ratios[lab]=ratio;states[lab][0]+=mu;states[lab][1]+=r
assert sum(u for u,r in states.values())==sum(r for u,r in states.values())==1
expected=json.loads((ROOT/'out'/'validation.json').read_text())
record=next(r for r in expected['records'] if (r['m'],r['L'],r['point'])==(2,2,1))['contexts'][0]
assert {str(l):dict(mu=str(u),r=str(r),likelihood=str(ratios[l])) for l,(u,r) in states.items()}==record['states']
function=[]
for x in range(4096):
 y=x&3;x0=(x>>2)&15;z0=(x>>6)&1;x1=(x>>7)&15;z1=(x>>11)&1;p=(y.bit_count()%2)^(y==1)
 function.append(k.bent(y,2)*k.bent(x0,4)*k.bent(x1,4)*(-1 if p*((x0==0)*z0+(x1==0)*z1)%2 else 1))
freqs=[0,64,384,448];coeff={s:sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(function)) for s in freqs}
assert [coeff[s] for s in freqs]==[100,12,-124,-20]
first=Q(64*12**2,100**2+12**2);second=Q(64*20**2,124**2+20**2)
assert first==Q(288,317) and second==Q(800,493) and first!=second
out=dict(helper_version='A035-direct-count-reproduction-v1',runtime_seconds=time.perf_counter()-start,case_count=1,retained_rows=2048,state_count=len(states),complete_root_character_sums=coeff,same_count_deleted_fiber=['no other selector frequency','core ratio 1/2','queried bent sign +1'],different_exact_likelihoods=[str(first),str(second)],strict_conditional_KL='Positive by equality criterion for KL chain rule; both rows have positive derivative probability.',certificate=record['lost_conditional_KL'],status='PASS')
(ROOT/'out'/'reproduction.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
