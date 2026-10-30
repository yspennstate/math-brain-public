from pathlib import Path
from fractions import Fraction as F
import json,time
from arithmetic import Q
r=Path(__file__).resolve().parents[1];start=time.perf_counter()
s=json.loads((r/'out/SEED_CERTIFICATE.json').read_text(encoding='utf-8'))
I=F(s['I']);lo,hi=s['A4_interval']
assert I==F(98637,524288)
threshold=I/8+F(1,256)
assert lo*threshold.denominator>Q*threshold.numerator
deficit_lo=F(lo,Q)-I/8
# Fixed rational51-bit witness and uniform affine-rate bound.
upper=F(4*(24+2*20+2),2**20)
assert upper<F(1,256)<deficit_lo
z={'status':'PASS','old_rate_interval':['4','4097/1024'],'extended_closed_real_rate_interval':['4','33/8'],'reason':'exact I replaces I<=24 for the unchanged Boolean seed','I':str(I),'strict_deficit_floor':'1/256','endpoint_threshold':str(threshold),'endpoint_deficit_lower':str(deficit_lo),'cross_multiplication_positive_integer':lo*threshold.denominator-Q*threshold.numerator,'root_hull_upper_d20':str(upper),'positive_reach_d20':'1/1048576','exact_assertions':3,'runtime_seconds':time.perf_counter()-start}
(r/'out/RATE_EXTENSION.json').write_text(json.dumps(z,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:z[k] for k in ['status','extended_closed_real_rate_interval','exact_assertions','runtime_seconds']}))
