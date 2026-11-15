from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
import contextlib,json
from audit_t067_uniform_own import run,memcheck
root=Path(__file__).resolve().parent
proof=Path('~/brain_workers/w682/proofs/T067-LOCAL-RADIUS80-001_v1.md')
initial=sha256(proof.read_bytes()).hexdigest()
L=F(559017,5000000);M=F(537,500)
assert 80*L*L>1 and L<F(2887,5000) and M/9==F(179,1500)
with (root/'checks/t067_local80_own.log').open('w',encoding='utf-8') as log,contextlib.redirect_stdout(log):
    memcheck();result=run('local_radius80',M,L,F(1,1000),2880000)
assert sha256(proof.read_bytes()).hexdigest()==initial
result.update(at=datetime.now().astimezone().isoformat(),complete=True,proof_sha256=initial,critical_degree80_margin=str(80*L*L-1),method='Own complete rational prefix-polynomial/Bernstein reconstruction, no author code imported')
(root/'checks/t067_local80_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['complete','proof_sha256','critical_degree80_margin','bernstein_signs']}))
