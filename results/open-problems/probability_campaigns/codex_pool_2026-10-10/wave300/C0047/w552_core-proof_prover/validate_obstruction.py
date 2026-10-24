import json
import time
from fractions import Fraction as Q
from pathlib import Path
import validate

start = time.monotonic()
gate = validate.gate('OBSTRUCTION_GATE.json')
p,z = Q(3,5),Q(5,3)
m = 2*p*(p+p*p-p*p*p)
assert m == Q(558,625) < 1
assert z*z > 2
assert z+2/z == Q(43,15)
assert 2 > Q(13,10)**2
assert p*z == 1
result = {'status':'PASS','exact_inequalities':5,'offspring_mean_at_three_fifths':str(m),
          'trial_beta':str(z),'trial_adjacency_radius':str(z+2/z),'gate':gate,
          'command':'python -X utf8 ~/brain_workers/w552/validate_obstruction.py',
          'scope':'Only constants in the analytic C3*C2 nonbacktracking-route obstruction; no duplicate finite enumeration or infinite bound certificate.',
          'formal_proof_receipt':False,'elapsed_seconds':time.monotonic()-start}
Path(__file__).with_name('OBSTRUCTION_VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','exact_inequalities','offspring_mean_at_three_fifths','elapsed_seconds']}))
