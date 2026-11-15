from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
import contextlib,json
from audit_t067_uniform_own import run,memcheck
memcheck()
L=F(559017,2500000)
assert 20*L*L>1 and L<F(2887,5000)
assert F(771,1000)/9==F(257,3000)
with Path('checks/t067_local20_own.log').open('w',encoding='utf8') as log,contextlib.redirect_stdout(log):
    result=run('local_radius20',F(771,1000),L,F(1,1000),11520000)
proof=Path('~/brain_workers/w682/proofs/T067-LOCAL-RADIUS20-001_v1.md')
result.update(at=datetime.now().astimezone().isoformat(),complete=True,proof_sha256=sha256(proof.read_bytes()).hexdigest(),critical_degree20_margin=str(20*L*L-1),method='Own rational prefix polynomial and complete tensor Bernstein conversion, no source certificate imports')
Path('checks/t067_local20_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['complete','proof_sha256','critical_degree20_margin']}))
