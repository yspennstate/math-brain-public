"""A017-critical-integer-v1: independent direct Walsh sums, integer signs only."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0;classes=Counter();examples={};maximum=F(0);winner=None
def req(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
for code in range(128):
 a=[1]+[1-2*((code>>(x-1))&1) for x in range(1,8)]
 # Direct character sums; no FFT or prior spectral implementation.
 W=[sum(a[x]*(-1)**((x&s).bit_count()&1) for x in range(8)) for s in range(8)]
 req(sum(W)==8 and sum(w*w for w in W)==64)
 hist=Counter((w-1)**2 for w in W);num=den=1
 for t,c in hist.items():num*=pow(t+1,(t+1)*c);den*=pow(t,t*c)
 req(num<2**32*den)  # B=log2(num/den)/64 < 1/2 = 4 Inf.
 ratio=F(num,den)
 if ratio>maximum:maximum=ratio;winner=code
 key=tuple(sorted(hist.items()));classes[key]+=1;examples.setdefault(key,code)
 # Independent edge-isoperimetric ingredient for the reviewed sparse leaf proof.
 E=[x for x in range(8) if a[x]<0];s=len(E);internal=sum(x^(1<<i) in E for x in E for i in range(3))//2
 if s: req(2**(2*internal)<=s**s)
 req(sum(sum(a[x]!=a[x^(1<<i)] for x in range(8)) for i in range(3))>=6 if s else True)
certificate=[]
for hist,count in sorted(classes.items()):
 num=den=1
 for t,c in hist:num*=pow(t+1,(t+1)*c);den*=pow(t,t*c)
 certificate.append(dict(squared_amplitude_histogram=dict(hist),multiplicity=count,example_seed=examples[hist],positive_integer_slack=str(2**32*den-num)))
req(sum(x['multiplicity'] for x in certificate)==128)
req(3**3*13**13>2**52) # h2(3/16)<3/4.
out=dict(status='PASS',helper='A017-critical-integer-v1',Boolean_three_bit_seeds=128,histogram_classes=len(classes),assertions=checks,elapsed_seconds=time.perf_counter()-start,max_B_exact=dict(seed=winner,formula='log2(numerator/denominator)/64',numerator=str(maximum.numerator),denominator=str(maximum.denominator)),certificate=certificate,three_sixteenths_binary_entropy_integer_slack=str(3**3*13**13-2**52))
(R/'out/CRITICAL_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ['certificate','max_B_exact']}))
