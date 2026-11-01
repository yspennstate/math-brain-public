"""Independently count the double-a-edge variant of the triangle block."""
from fractions import Fraction as F
from itertools import product
from math import comb
from decimal import Decimal, localcontext
from pathlib import Path
import json
import time

root = Path(__file__).resolve().parent
gate = json.loads((root/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
started = time.perf_counter()
configs = list(product((0, 1), repeat=7))
assert len(configs) <= gate['max_configurations']

def offspring(bits):
    connected = {0}
    edges = ((0,1), (0,2), (1,2))
    for _ in range(3):
        for edge_open, (u,v) in zip(bits[:3],edges):
            if edge_open and (u in connected or v in connected):
                connected.update((u,v))
    return int(1 in connected and (bits[3] or bits[4])) + int(2 in connected and (bits[5] or bits[6]))

coeffs = [0]*8
for bits in configs:
    k = sum(bits)
    for j in range(7-k+1):
        coeffs[k+j] += offspring(bits)*comb(7-k,j)*(-1)**j
assert coeffs == [0,0,4,2,-6,2,0,0], coeffs
samples = []
for p in (F(51,100), F(53,100), F(2,3)):
    mean = sum(F(offspring(bits))*p**sum(bits)*(1-p)**(7-sum(bits)) for bits in configs)
    assert mean == (2*p-p**2)*2*(p+p**2-p**3)
    samples.append({'p':str(p),'mean':str(mean),'supercritical':mean>1})
assert not samples[0]['supercritical'] and samples[1]['supercritical']
with localcontext() as ctx:
    ctx.prec = 60
    lo,hi = Decimal('0.51'),Decimal('0.53')
    for _ in range(gate['max_decimal_bisections']):
        p=(lo+hi)/2
        if 4*p**2+2*p**3-6*p**4+2*p**5 < 1:
            lo=p
        else:
            hi=p
    display=str((lo+hi)/2)
elapsed=time.perf_counter()-started
assert elapsed <= gate['max_runtime_seconds']
result={'status':'PASS','configurations':128,'mean_polynomial_coefficients':coeffs,
        'parallel_link_probability':'2p-p^2','critical_polynomial':'2p^5-6p^4+2p^3+4p^2-1',
        'pc_decimal_display_only':display,'rational_bracket':['51/100','53/100'],
        'samples':samples,'elapsed_seconds':round(elapsed,6),
        'command':'python -X utf8 ~/brain_workers/w559/verify_parallel_convention.py',
        'limits':'Exact local multiplicity check only; source-model interpretation is documented separately and does not alter the simple-graph proof.'}
encoded=json.dumps(result,indent=2)+'\n'
assert len(encoded.encode())<=gate['max_output_bytes']
(root/'MEASUREMENTS_PARALLEL.json').write_text(encoded,encoding='utf-8')
print(encoded)
