"""Check exact source identity and constant certificates; not a formal proof audit."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, re
ROOT = Path(__file__).resolve().parent
p = ROOT / 'paper.tex'
b = p.read_bytes()
expected = '90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb'
assert hashlib.sha256(b).hexdigest() == expected, 'Source differs from the audited repair target'
text = b.decode('utf-8')
checks = {
    'source_sha256_matches': True,
    'source_git_blob': hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),
    'physical_lines': len(text.splitlines()),
    'proof_environments': len(re.findall(r'\\begin\{proof\}',text)),
    'C3_sixth_power_margin': F(15)**6-F(26244)*F(11,4)**6,
    'C2_eighth_power_margin': F(61,5)**8-F(8388608)*F(11,4)**4,
    'concentration_fourth_power_margin': F(19)**4-F(2048)*F(68,25)**3*F(63,20),
    'sqrt2_upper_squared_margin': F(14143,10000)**2-2,
    'sqrt12_upper_squared_margin': F(693,200)**2-12,
    'half_kernel_2192_margin': F(548,25)-(F(3927,1250)+4+4*F(1733,2500)+12),
    'halfpotential_76_margin': 76-F(693,200)*F(548,25),
    'main_scalar_267_margin': 267-F(693,200)*77,
    'main_indefinite_269_margin': 269-(16*(8+4*F(1733,2500)+6)+F(10,27)),
}
for name,val in checks.items():
    if name.endswith('margin'): assert val>0, (name,val)
# Elementary e bounds from its series: tail after N is bounded by its first term / (1-1/(N+2)).
from math import factorial
N=8
partial=sum((F(1,factorial(j)) for j in range(N+1)),F(0))
tail=F(1,factorial(N+1))/(1-F(1,N+2))
assert partial>F(27,10) and partial+tail<F(68,25)<F(11,4)
checks['e_series_interval']=[str(partial),str(partial+tail)]
checks['unsafe_control_bytes']=[x for x in b if x<32 and x not in (9,10,13)]
assert not checks['unsafe_control_bytes']
checks['status']='PASS; finite source/constant checks only, not a Lean build or universal proof certificate'
(ROOT/'repair_checks.json').write_text(json.dumps(checks,indent=2,default=str)+'\n')
print(json.dumps(checks,indent=2,default=str))
