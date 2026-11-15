#!/usr/bin/env python3
"""A separate exact audit of the four-user remainder and certificate."""
import os
import resource
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

os.environ['OMP_NUM_THREADS'] = '1'
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def mul(a, b):
    out = [Q(0)] * (len(a)+len(b)-1)
    for i in range(len(a)):
        for j in range(len(b)):
            out[i+j] += a[i]*b[j]
    return out


def transition(source, target):
    # Independently enumerate all 16 attempt masks, each with probability 1/16.
    coeff = [Q(0)]*4
    for light0, light1, light2, tag in product((0, 1), repeat=4):
        active = [i for i, b in enumerate((light0, light1, light2)) if b and source[i]]
        post = list(source)
        if tag == 0 and len(active) == 1:
            post[active[0]] -= 1
        for arrivals in product((0, 1), repeat=3):
            if tuple(x+y for x, y in zip(post, arrivals)) != target:
                continue
            term = [Q(1,16)]
            for a in arrivals:
                term = mul(term, [Q(0), Q(1)] if a else [Q(1), Q(-1)])
            coeff = [a+b for a, b in zip(coeff, term)]
    return coeff


departure = {}
for mask in product((0, 1), repeat=3):
    if not any(mask):
        continue
    count = 0
    for coins in product((0, 1), repeat=4):
        count += (not coins[-1]) and sum(a*b for a, b in zip(mask, coins)) == 1
    departure[mask] = Q(count,16)
assert min(departure.values()) == Q(3,16)
print('enumerated light departure probabilities:', sorted(set(departure.values())))

target = (1, 1, 0)
polys = {str(q): transition(q, target) for q in ((0,0,0),(1,0,0),(0,1,0),(0,0,1),target)}
assert polys[str((0,0,0))] == [0,0,1,-1]
assert polys[str((1,0,0))] == [0,Q(3,4),Q(-5,4),Q(1,2)]
assert polys[str((0,1,0))] == polys[str((1,0,0))]
assert polys[str((0,0,1))] == [0,0,Q(1,4),Q(-1,4)]
assert polys[str(target)][0] == Q(3,4)
print('pair-transition polynomials:', {k: list(map(str,v)) for k,v in polys.items()})

# Verify the claimed uniform Lyapunov bound by direct positive drift slack.
g = Q(33,32)**3
beta = Q(55,64)*g
slack = 4*(1-beta)-Q(3,16)*g
assert slack > 0
print('Lyapunov invariant-moment slack:', slack)

# Independently collect the proof's error contributions without importing verify.py.
tail2, tail3 = 4096, 131072
empty_error = 16+1
single_error = 2*(Q(3,4)*(2*tail2)+16*2)
rest_error = 4 + 3*tail2 + tail3 + 3*tail2
busy_error = 4*(empty_error+single_error+rest_error)+tail3
mu_error = Q(3,8)*busy_error+Q(tail3,8)
assert busy_error == 803156 and mu_error < 400000

# Read serialized exact certificate, recompute every value, compare decimal endpoints.
record = json.loads(Path('verification.json').read_text())['certificate']
e = Q(record['epsilon'])
lam = Q(record['tagged_arrival'])
lo, hi = Q(record['service_lower']), Q(record['service_upper'])
assert lam == Q('0.499996999992')
assert lo == Q('0.4999969999891') and hi == Q('0.4999969999899')
assert lam-hi == Q(21,10**13)
assert hi == Q(1,2)-3*e-Q(21,2)*e**2+400000*e**3
rho = Q(record['rho_light'])
assert 0 < rho < 1
light_capacity = rho*Q(1,2)*(1-rho/2)**2*Q(1,2)
tag_capacity = Q(1,2)*(1-rho/2)**3
assert light_capacity-e == Q(record['light_slack']) > 0
assert tag_capacity-lam == Q(record['tag_slack']) > 0
assert str(Q(record['light_slack']).numerator) in Path('PROOF.md').read_text()
assert str(Q(record['tag_slack']).numerator) in Path('PROOF.md').read_text()
print('independent certificate recomputation: passed')
print('ALL AUDIT CHECKS PASSED')
print('peak RSS bytes (macOS):', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
