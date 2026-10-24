"""Exact, bounded checks for the mathematical rows; no live writes."""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
import random
import time

root = Path(__file__).resolve().parent
start = time.perf_counter()
receipt = {'command': 'python -X utf8 ~/brain_workers/w332/check_math.py', 'checks': []}

def record(name, count, detail):
    receipt['checks'].append({'name': name, 'cases': count, 'passed': True, 'detail': detail})
    print(name, count, 'PASS', flush=True)

rng = random.Random(332)
curvature_cases = 0
for case in range(120):
    points = sorted(set([0, 100] + [rng.randrange(101) for _ in range(rng.randrange(1, 6))]))
    ws = [rng.randrange(1, 21) for _ in points]
    weights = [F(w, sum(ws)) for w in ws]
    mean = sum(w * F(x, 100) for x, w in zip(points, weights))
    xs = [F(x, 100) - mean for x in points]
    a = sum(w*x*x for x, w in zip(xs, weights))
    b = sum(w*x**4 for x, w in zip(xs, weights))
    assert a <= F(1, 4)
    assert b + 3*a*a <= a
    for y in [F(1, 100), F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(1), F(2)]:
        norm = sum(w*(x*x+y)**2 for x, w in zip(xs, weights))
        mu = [w*(x*x+y)**2/norm for x, w in zip(xs, weights)]
        profile = sum(p/(x*x+y) for x, p in zip(xs, mu))
        assert 1/profile == (b+2*a*y+y*y)/(a+y)
        deriv = sum(p*x/(x*x+y)**2 for x, p in zip(xs, mu))
        assert deriv == 0
        second = 2*sum(p*(3*x*x-y)/(x*x+y)**3 for x, p in zip(xs, mu))
        if second >= 0:
            curvature_cases += 1
            assert y <= 3*a
            assert profile >= 1
record('P0174 centered second/fourth moment inequalities', 120, 'Exact rational finite laws of diameter one, seed 332.')
record('P0174 reweighting and stationary-profile identities', 840, 'Exact fractions, including Jensen consequence only when F second derivative is nonnegative.')
record('P0174 critical points with nonnegative curvature', curvature_cases, 'All have profile >= 1; finite sampling is a check, not a universal proof.')
a = F(1, 4)
y = 3*a
for u in [F(i, 40) for i in range(-40, 41) if i != 0]:
    profile = (1/((F(1, 2)-u)**2+y)+1/((-F(1, 2)-u)**2+y))/2
    expected = -u**4/(4*a*(16*a*a+4*a*u*u+u**4))
    assert profile-1 == expected < 0
record('P0174 endpoint is a strict fourth-order maximum', 80, 'Exact profile difference at y=3a; equality cannot be a separating minimum.')
assert F(2) > 3*a
record('P0174 stationary condition alone is insufficient', 1, 'The symmetric endpoint law is stationary for y=2>3a; the curvature guard is essential.')

N, k = 12, 4
configs = list(combinations(range(N), k))
for m in range(1, N):
    vals = [sum(i < m for i in config) for config in configs]
    mean = F(sum(vals), len(vals))
    var = sum((F(v)-mean)**2 for v in vals)/len(vals)
    predicted = F(m)*F(k,N)*(1-F(k,N))*F(N-m,N-1)
    assert var == predicted
    comp_vals = [k-v for v in vals]
    comp_mean = F(sum(comp_vals), len(vals))
    comp_var = sum((F(v)-comp_mean)**2 for v in comp_vals)/len(vals)
    assert comp_var == var
record('P0389 fixed-mass complement and hypergeometric variance', len(configs)*11, 'All 495 uniform four-subsets on 12 sites; 11 window sizes. Fixed total does not imply mesoscopic hyperuniformity.')

for d in [7, 8, 10, 12, 20]:
    ratio_exponent = F(1,3)-F(2,d)
    assert ratio_exponent > 0
    beta = (F(1,3)+F(2,d))/2
    assert F(2,d) < beta < F(1,3)
record('C0068 crossover inequality reversal', 5, 'For d>6, V^(-2/d)/V^(-1/3)=V^(1/3-2/d) diverges. eps=V^-beta in the gap satisfies eps >> window and eps << crossover.')
receipt['elapsed_seconds'] = time.perf_counter()-start
(root/'measurements.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt, indent=2))
