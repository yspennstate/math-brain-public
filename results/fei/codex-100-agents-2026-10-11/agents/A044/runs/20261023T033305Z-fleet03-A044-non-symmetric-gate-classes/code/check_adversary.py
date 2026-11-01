from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parents[1]
# Independent direct Walsh representation: two disjoint fair quadratic signs.
f=[(-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16)]
a=[F(sum(f[x]*(-1)**((x&s).bit_count()) for x in range(16)),16) for s in range(16)]
assert all(abs(c)==F(1,4) for c in a)
rr=sum((F(s.bit_count()-2)*a[s]*a[s] for s in range(16) if s.bit_count()>=3),F(0))
assert rr==F(3,8)
# Each two-input child and the binary outer parity gate have Fourier degree<=2,
# hence R=0 under ALL their induced laws. Their composed output has R=3/8.
assert rr>0
out={'status':'PASS','representation':'Independent direct16-point Walsh sum','R_output':'3/8','weighted_gate_R_total':'0','conclusion':'R and B=(11Delta-7R)/2 are not composition additive; telescope Delta only.','exact_assertions':3}
(R/'out/ADVERSARY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
