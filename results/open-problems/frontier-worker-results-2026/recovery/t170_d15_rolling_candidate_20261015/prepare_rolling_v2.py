from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent
src=(H/'pilot_t170_rolling.py').read_bytes()
old=src.replace(b'1<=cap<=128',b'2<=cap<=128',1)
r=json.loads((H/'T170_ROLLING_d15_C32_RECEIPT.json').read_bytes())
assert hashlib.sha256(old).hexdigest()==r['checker_sha256']
def frozen(name,payload):
 p=H/name
 if p.exists():assert p.read_bytes()==payload
 else:p.write_bytes(payload)
frozen('pilot_t170_rolling_C32_source.py',old)
frozen('pilot_t170_rolling_cap1_source.py',src)
newer=src.replace(b'print(json.dumps(out))',b'print(json.dumps({k:v for k,v in out.items() if k!="diagonal_floor"}))')
assert newer!=src
frozen('pilot_t170_rolling_v2.py',newer)
print('Preserved exact original source hashes; v2 only shortens printed metadata')
