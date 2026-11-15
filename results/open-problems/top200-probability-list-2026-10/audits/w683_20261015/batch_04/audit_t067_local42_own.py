"""Reuse our audited prefix algebra, with the new reference rectangle."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
import json
from audit_t067_uniform_own import run,memcheck

memcheck()
assert 42*F(39,250)**2==F(63882,62500)>1
assert F(39,250)<F(2887,5000)
result=run('local42',F(9,10),F(39,250),F(1,20),1920)
assert result['bernstein_signs']=={'negative':0,'zero':6,'positive':120}
proof=Path('~/brain_workers/w682/proofs/T067-UNIFORM-LOCAL-EXT-001_v1.md')
result.update(at=datetime.now().astimezone().isoformat(),complete=True,proof_sha256=sha256(proof.read_bytes()).hexdigest(),method='Own prior exact prefix polynomial and independent Fraction two-axis Bernstein rebuild at new L')
Path('checks/t067_local42_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result))
