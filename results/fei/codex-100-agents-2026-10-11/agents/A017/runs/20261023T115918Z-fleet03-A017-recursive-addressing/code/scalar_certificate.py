"""Independent integer proof of the exact entropy-rate margin."""
import json,math,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec=json.loads((R/'out/scalar_spec.json').read_text(encoding='utf-8'))
assert spec['helper_version']=='A017-exponential-integer-margin-v1'
factorial=math.factorial(16)
numerator=sum(8**k*(factorial//math.factorial(k)) for k in range(17))
left=numerator*2**104;right=factorial*5**25*3**36
assert left>right
# e^8 > sum_(k=0)^16 8^k/k! > 5^25*3^36/2^104.
# Taking ln gives exactly32 times the natural margin K/8-Delta(b).
result=dict(status='PASS',helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 left_integer=str(left),right_integer=str(right),positive_difference=str(left-right),
 interpretation='Delta_i(b)<(4+2/ln(2))*Inf_i(b), although B_i(b)>4*Inf_i(b).',
 series_order=16,sign_uses_only_integer_comparison=True)
(R/'out/scalar_certificate.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
print('PASS: positive-integer exponential lower certificate for actual K-rate entropy payment')
