import itertools
import json
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parent
checks = {}
local = []
for p in map(Q, ['0', '1/4', '49/100', '1/2', '51/100', '3/4', '1']):
    total = Q(0)
    singleton = Q(0)
    for bits in itertools.product([0, 1], repeat=7):
        weight = p**sum(bits) * (1-p)**(7-sum(bits))
        total += weight
        if bits == (1, 0, 0, 0, 0, 0, 0):
            singleton += weight
    assert total == 1 and singleton == p*(1-p)**6
    local.append({'p': str(p), 'total': str(total), 'singleton': str(singleton)})
checks['local_states'] = local
steps = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1)]
def boundary(s):
    return {(x+dx,y+dy) for x,y in s for dx,dy in steps} - set(s)
level = {frozenset({(0,0)})}
animals = []
for n in range(1,6):
    value = sum((Q(1, n*2**(n+len(boundary(s)))) for s in level), Q(0))
    animals.append({'size':n, 'count':len(level), 'contribution':str(value)})
    if n < 5:
        level = {s | {v} for s in level for v in boundary(s)}
assert [a['count'] for a in animals] == [1,6,33,176,930]
assert [a['contribution'] for a in animals] == ['1/128','3/1024','13/8192','65/65536','357/524288']
checks['rooted_animals'] = animals
checks['sum'] = str(sum((Q(a['contribution']) for a in animals), Q(0)))
assert checks['sum'] == '7341/524288'
b = sp.symbols('b')
identity = sp.factor((1/(b+1)-2/(b+2)+1/(b+3))/2 - 1/((b+1)*(b+2)*(b+3)))
assert identity == 0
checks['integral_coefficient_difference'] = str(identity)
assert Q(2) - Q(2,3) == Q(4,3)
assert Q(1,2)*(1-Q(1,2))**6 == Q(1,128)
checks['critical_singleton'] = '1/128'
checks['printed_exponent'] = '4/3'
(root/'independent_checks.json').write_text(json.dumps(checks, indent=2), encoding='utf-8')
print(json.dumps(checks, indent=2))
