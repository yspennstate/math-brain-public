from fractions import Fraction as F
from pathlib import Path
from math import lcm
import json,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out'
d=json.loads((O/'ACTIVATION_FIXTURE.json').read_text(encoding='utf-8'))
p={s:F(v) for s,v in d['source_spectrum'].items()};old={s:F(v) for s,v in d['inherited_reference'].items()};new={s:F(v) for s,v in d['fresh_reference'].items()}
denom=lcm(*(v.denominator for v in p.values()));ratio=F(1)
for s,v in p.items():ratio*=(old[s]/new[s])**int(v*denom)
assert ratio<1
margin=(1-ratio)/denom
# ln(ratio)<=ratio-1 and ln2<1 prove reset< -margin bits.
assert margin>0
simple=F(1,4096);has_simple=2*ratio.numerator**(4096//denom)<ratio.denominator**(4096//denom) if 4096%denom==0 else False
result={'status':'PASS','source_denominator':denom,'integer_numerator':ratio.numerator,'integer_denominator':ratio.denominator,'positive_integer_difference':ratio.denominator-ratio.numerator,'exact_reset_bits':'log2(integer_numerator/integer_denominator)/source_denominator','certified_margin_bits':str(margin),'bound':'reset < -certified_margin_bits','additional_dyadic_margin':'reset < -1/4096 bits' if has_simple else 'not asserted','proof':'integer ratio<1; ln(ratio)<=ratio-1; ln2<1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'precision_refinement':'none; sign obtained by exact integer comparison'}
(O/'ACTIVATION_INTEGER_SIGN.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','source_denominator':denom,'integer_digits':[len(str(ratio.numerator)),len(str(ratio.denominator))],'margin_bits':str(margin),'dyadic_margin':result['additional_dyadic_margin']}))
