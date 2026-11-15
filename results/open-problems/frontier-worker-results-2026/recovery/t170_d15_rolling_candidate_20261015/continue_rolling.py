from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent
r=json.loads((H/'T170_ROLLING_d15_C128_RECEIPT.json').read_bytes())
assert r['cap0_mass']>.2 and r['conditional_margin']<0
s=(H/'pilot_t170_rolling_v2.py').read_bytes()
assert hashlib.sha256(s).hexdigest()==r['checker_sha256']
t=s.replace(b'1<=cap<=128',b'1<=cap<=256').replace(b'range(20000)',b'range(100000)').replace(b'range(30000)',b'range(100000)')
p=H/'pilot_t170_rolling_v3.py'
if p.exists():assert p.read_bytes()==t
else:p.write_bytes(t)
print('v3 preserves model/checker, extends justified cap to256 and iteration ceilings; time guards remain20/55 seconds')
