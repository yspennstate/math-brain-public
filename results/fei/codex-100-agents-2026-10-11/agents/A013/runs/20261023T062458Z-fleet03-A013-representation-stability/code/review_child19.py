from pathlib import Path
import json,time
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v,checks
 checks+=1
 assert time.perf_counter()-start<50
# Complement representatives have truth sign +1 at vertex15.
# Direct character bitmasks, no FWHT and no Gray-code update.
pos=[sum(1<<x for x in range(16) if (x&t).bit_count()%2==0) for t in range(16)]
allmask=(1<<16)-1
lower={k:(k**128).bit_length()-1 for k in range(1,17)}
for k,l in lower.items():ck((1<<l)<=k**128<(1<<(l+1)))
best=None;witness=None;hist={}
for phase in range(32768):
 w=[(16 if t==0 else 0)-2*((phase&pos[t]).bit_count()-(phase&(allmask^pos[t])).bit_count()) for t in range(16)]
 sq=[x*x for x in w];energy=sum(t.bit_count()*x for t,x in enumerate(sq))
 # Four direct physical edge counts; each undirected edge once.
 edges=sum(((phase>>x)^(phase>>(x^(1<<j))))&1 for j in range(4) for x in range(16) if not(x>>j&1))
 ck(sum(sq)==256);ck(energy==32*edges)
 numerator=4*energy*128-8*256*128+2*sum(x*x*lower[abs(x)] for x in w if x)
 if energy:
  ck(numerator>=256*128//4)
  if best is None or numerator<best:best=numerator;witness=phase
 else:ck(phase==0 and numerator==0)
 key=str((sum(x!=0 for x in w),energy));hist[key]=hist.get(key,0)+2
src=Path('agents/A012/runs/20261023T053904Z-fleet03-A012-sparse-activation-accounting/out')
for mode in ('author','replay'):
 d=json.loads((src/f'CHILD_{mode}.json').read_text(encoding='utf-8'));ck(hist==d['histogram'])
out={'status':'PASS','assertions':checks,'complement_classes':32768,'actual_boolean_functions':65536,'minimum_certified_gap':str(F(best,256*128)),'witness':witness,'matched_source_histograms':['author','replay'],'seconds':time.perf_counter()-start,'histogram':hist}
(R/'out/CHILD_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='histogram'}))
