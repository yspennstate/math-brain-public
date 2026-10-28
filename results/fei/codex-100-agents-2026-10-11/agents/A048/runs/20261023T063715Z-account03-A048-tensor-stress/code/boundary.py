from fractions import Fraction as F
from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
v=[1]*15+[-1]
p=[F(sum(value*(-1)**((x&s).bit_count()) for x,value in enumerate(v)),16)**2 for s in range(16)]
assert p==[F(49,64)]+[F(1,64)]*15
I=F(sum(v[x]!=v[x|(1<<i)] for i in range(4) for x in range(16) if not x&(1<<i)),8)
assert I==F(1,2)
assert 7**6<2**17
H_lower=6-F(49,32)*F(17,6)
target=4*I-F(7,4)*(1-p[0])
assert H_lower==F(319,192)>target==F(407,256)
result={'status':'EXACT_REFUTATION_OF_VARIANCE_SLACK_EXTENSION','actual_family':'one4bit point defect','entropy_identity':'H=6-(49/32)log2(7)','H_strict_lower':str(H_lower),'claimed_upper':str(target),'rational_gap_lower':str(H_lower-target),'integer_log_sign':'7^6<2^17','scope':'Only H<=4I-(7/4)Var is refuted beyond3bit factors; no FEI counterexample'}
(B/'out/BOUNDARY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result))
