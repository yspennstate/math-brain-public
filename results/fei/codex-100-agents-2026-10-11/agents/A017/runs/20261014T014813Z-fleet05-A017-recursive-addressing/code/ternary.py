"""A017-two-edge-ternary-v1: exact local D5, Inf=1/8 certificate."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import itertools,json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();classes=Counter();checks=bad=0;maximum=F(0);witness=None
for tail in itertools.product([-1,0,1],repeat=7):
 h=(1,)+tail;W=[sum(h[x]*(-1)**((x&s).bit_count()&1) for x in range(8)) for s in range(8)]
 hist=Counter((w-1)**2 for w in W);num=den=1
 for t,c in hist.items():num*=pow(t+1,(t+1)*c);den*=pow(t,t*c)
 checks+=1
 if num>2**32*den:bad+=1
 ratio=F(num,den)
 if ratio>maximum:maximum=ratio;witness=list(h)
 classes[tuple(sorted(hist.items()))]+=1
out=dict(status='PASS' if not bad else 'EXACT_OBSTRUCTION',helper='A017-two-edge-ternary-v1',cases=2187,assertions=checks,K4_bad_cases=bad,histogram_classes=len(classes),max_B=dict(formula='log2(numerator/denominator)/64',numerator=str(maximum.numerator),denominator=str(maximum.denominator),ternary_core=witness),classes=[dict(hist=dict(k),multiplicity=v) for k,v in sorted(classes.items())],elapsed_seconds=time.perf_counter()-start)
(R/'out/TERNARY_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in out.items() if k not in ['classes','max_B']}))
