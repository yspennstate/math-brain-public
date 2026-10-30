from fractions import Fraction as Q
from pathlib import Path
import json, time, subprocess, sys, os, hashlib
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def ck(p):
    global checks
    assert p; checks+=1
alpha=Q(1,8)
for t in [Q(1,8),Q(1,4),Q(1,2),Q(1),Q(2),Q(3)]:
    beta=alpha/t
    weights=[Q(1,k*k+1) for k in range(1,7)]
    S=sum((t**k*w for k,w in enumerate(weights,1)),Q(0))
    eta=[t**k*w/S for k,w in enumerate(weights,1)]
    ck(sum(eta)==1)
    for r in range(1,5):
        p=Q(1,2**r); ck(p*p*2**r==p)
        for u in range(2**r):
            H=[Q(1) if u==0 else Q(k+u,k+1) for k in range(1,7)]
            J=sum((q*beta**k*h for k,(q,h) in enumerate(zip(eta,H),1)),Q(0))
            N=sum((alpha**k*w*h for k,(w,h) in enumerate(zip(weights,H),1)),Q(0))
            ck(S*J==N)
        ck(time.monotonic()-start<55)
result={'status':'PASS','assertions':checks,'seconds':time.monotonic()-start,
        'scope':'algebra fixtures only; no Boolean or full-cost conclusion inferred'}
(ROOT/'out/scale_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
# Termwise homogeneity underlying equation (1), in a conservative semiring.
# This checks only the integer identity, not real logarithms, posterior sums or FEI.
stmt='theorem lifted_scaling (t b w k : Nat) : (t^k * w) * b^k = (t*b)^k * w := by\n  simp [Nat.mul_pow, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]'
source='import Lean\n'+stmt.strip()+'\n'
(ROOT/'out/scale_core_source.lean').write_bytes(source.encode('utf-8'))
previous=ROOT/'out/lean_attempt.json'
if previous.exists():
    (ROOT/'out/lean_initial_mismatch.json').write_bytes(previous.read_bytes())
env=os.environ.copy(); env['LEAN_CHECK_DIR']=str(ROOT/'out/lean_core')
cmd=[sys.executable,'-X','utf8',r'lean_check.py',
     '--core','--file',str(ROOT/'out/scale_core_source.lean'),'--target','lifted_scaling','--reviewed-sha256',
     hashlib.sha256(source.encode('utf-8')).hexdigest(),'--timeout','45','--json']
receipt={'command':cmd,'submitted_source_sha256':hashlib.sha256(source.encode('utf-8')).hexdigest(),
         'scope':'Nat termwise scale product law only; compare prose separately'}
try:
    done=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,timeout=58,
                        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    receipt.update(exit_code=done.returncode,stdout=done.stdout,stderr=done.stderr)
except subprocess.TimeoutExpired as exc:
    receipt.update(status='RUNTIME_UNVERIFIED',reason='58-second wrapper bound; no verified compiler outcome')
(ROOT/'out/lean_attempt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'lean_exit_code':receipt.get('exit_code'),'status':receipt.get('status','receipt saved')}))
