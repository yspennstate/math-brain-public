from pathlib import Path
from fractions import Fraction as R
import json,time
RUN=Path(__file__).resolve().parents[1];spec=json.loads((RUN/'TERMINAL_PROBE_SPEC.json').read_text());start=time.perf_counter();out=[]
assert 577**5*65**3<2**64
for k in spec['domain']:
 d=R(1,1<<k)
 # All v and q erased from SAME original core Q: u law ((1+d)/2,(1-d)/2).
 qu=[(1+d)/2,(1-d)/2]
 q=[qu[w&1]/16+(R(1,4) if (w&7)==0 else 0) for w in range(16)]
 t=[1 if not w&8 else (-1 if (w>>1)&3==0 else 1) for w in range(16)]
 a=list(t);step=1
 while step<16:
  for i in range(0,16,step*2):
   for j in range(i,i+step):a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
  step*=2
 p=[R(v*v,256) for v in a]
 assert sum(q)==sum(p)==1
 assert sum(w*s.bit_count() for s,w in enumerate(p))==R(3,4)
 assert p[0]+p[8]==R(5,8)
 assert all(q[s]==(9+d)/32 for s in [0,8])
 assert all(q[s]==(1+d)/32 for s,w in enumerate(p) if w and s not in [0,8])
 ratio=(9+d)**5*(1+d)**3/R(1<<16)
 assert (ratio<1)==(k>=6)
 out.append({'k':k,'delta':str(d),'I':'3/4','CE_exact':'5-[5 log2(9+delta)+3 log2(1+delta)]/8','CE_gt_4I':ratio<1,'exact_sign_ratio':str(ratio)})
result={'status':'PASS','cases':len(out),'assertions':1+6*len(out),'elapsed_seconds':time.perf_counter()-start,'all_k_ge_6_certificate':'577^5*65^3<2^64; polynomial monotone in delta','records':out}
(RUN/'out/TERMINAL_PROBE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'}))
