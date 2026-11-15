"""Print exact search summaries without losing rational values."""
import json
from fractions import Fraction as Q
with open('q2_best.json') as f:b=json.load(f)
for k,v in sorted(b.items()):print(k,float(Q(v['ratio'])),v['ratio'],v['source'],v['partition'])
try:
    with open('q2_shape_results.json') as f:z=json.load(f)
    print('SHAPES')
    for k,v in z['best'].items():print(k,float(Q(v['ratio'])),v['source'])
    print('FAILURES',z['failures'])
except FileNotFoundError:pass
