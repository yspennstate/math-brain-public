"""Exact finite-tree meeting checks and log-domain comparison controls."""
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path
import time
from verify_obstruction import gate

root = Path(__file__).resolve().parent
# Preserve the previous fresh compute receipt before opening this tiny new gate.
(root/'COMPUTE_GATE_initial.json').write_bytes((root/'COMPUTE_GATE.json').read_bytes())
gate(work='exact nonuniform finite-tree meeting enumeration and logarithmic comparison controls')
start = time.perf_counter()
exact = []
for m in range(1,7):
    probabilities = [Fraction(16,25) if i%2 == 0 else Fraction(9,25) for i in range(m)]
    weights = []
    for bits in product([False,True],repeat=m):
        w = math.prod(p if bit else 1-p for bit,p in zip(bits,probabilities))
        left = 0
        for bit in bits:
            if not bit:
                break
            left += 1
        right = 0
        for bit in reversed(bits):
            if not bit:
                break
            right += 1
        weights.append((w,left,right))
    enumerated = sum((wa*wb for wa,la,_ in weights for wb,_,rb in weights if la+rb>=m),Fraction())
    q = math.prod(probabilities)
    formula = q*(1+sum(1-p for p in probabilities))
    assert enumerated == formula
    exact.append({'bridge_edges':m,'pairs':4**m,'q':str(q),'r_enumerated':str(enumerated),'r_formula':str(formula)})
numeric = []
for m in [1,2,5,10,100,1000]:
    for p in [0.01,0.2,0.64,0.9,0.999999]:
        log_q = m*math.log(p)
        log_q_over_r_squared = -log_q - 2*math.log1p(m*(1-p))
        margin = log_q_over_r_squared - (1-math.log(4))
        assert margin >= -1e-12
        numeric.append({'m':m,'p':p,'log_bound_margin':margin})
result = {'command':'python -X utf8 verify_tree_bound.py','exact_nonuniform_tree_controls':exact,
          'comparison_controls':numeric,'exact_pair_total':sum(row['pairs'] for row in exact),
          'active_seconds':time.perf_counter()-start,'passed':True,
          'limitation':'Finite controls only; the analytic tree proof is in TREE_NONLINEAR.md; no cyclic or 3D claim.'}
assert result['active_seconds'] < 5
(root/'TREE_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'exact_pairs':result['exact_pair_total'],'comparison_cases':len(numeric),'active_seconds':result['active_seconds']}))
