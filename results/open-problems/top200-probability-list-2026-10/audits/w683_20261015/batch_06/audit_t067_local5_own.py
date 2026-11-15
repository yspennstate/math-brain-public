from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
import json
from audit_t067_uniform_own import run,memcheck
memcheck()
L=F(559017,1250000)
assert 5*L*L>1 and L<F(2887,5000)
assert F(217,500)/9==F(217,4500)
result=run('local_radius5',F(217,500),L,F(1,1000),8640000)
proof=Path('~/brain_workers/w682/proofs/T067-LOCAL-RADIUS5-001_v1.md')
result.update(at=datetime.now().astimezone().isoformat(),complete=True,proof_sha256=sha256(proof.read_bytes()).hexdigest(),critical_degree5_margin=str(5*L*L-1),method='Own prefix polynomial numerator and complete rational tensor Bernstein conversion; no source certificate imports')
Path('checks/t067_local5_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result))
