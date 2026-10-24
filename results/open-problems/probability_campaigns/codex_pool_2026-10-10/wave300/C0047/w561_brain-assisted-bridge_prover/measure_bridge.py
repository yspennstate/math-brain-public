"""Tiny exact checks for this packet; no test-bank material or large compute."""
import json
from pathlib import Path
from fractions import Fraction as F
import shutil
import time
import psutil
from spectral_bridge_guard import assess

ROOT = Path(__file__).resolve().parent
gate = {
    'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'cpu_percent': psutil.cpu_percent(interval=0.2),
    'available_ram_bytes': psutil.virtual_memory().available,
    'free_disk_bytes': shutil.disk_usage(ROOT).free,
    'scope': 'serial exact enumeration; <=64 configurations per graph; no GPU',
}
gate['allow'] = (gate['cpu_percent'] <= 85 and
                 gate['available_ram_bytes'] >= 536870912 and
                 gate['free_disk_bytes'] >= 10485760)
(ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
if not gate['allow']:
    (ROOT / 'MEASUREMENTS.json').write_text(json.dumps({'state': 'gate_refused', 'gate': gate}, indent=2), encoding='utf-8')
    print(json.dumps({'state': 'gate_refused', 'gate': gate}))
    raise SystemExit(0)

start = time.perf_counter()
fixtures = [
    {'name': 'T4-normalized-counterexample', 'pc_upper': '1/3', 'spectral_upper': '7/8', 'degree': 4, 'spectral_definition': 'normalized_random_walk', 'expected': 'NOT_CERTIFIED'},
    {'name': 'T6-conservative-valid-bound', 'pc_upper': '1/5', 'spectral_upper': '3/4', 'degree': 6, 'spectral_definition': 'normalized_random_walk', 'expected': 'SUFFICIENT_CRITERION_MET'},
    {'name': 'degree-not-established', 'pc_upper': '1/3', 'spectral_upper': '7/8', 'degree': None, 'spectral_definition': 'normalized_random_walk', 'expected': 'MISSING_DEGREE'},
    {'name': 'normalization-not-established', 'pc_upper': '1/3', 'spectral_upper': '7/8', 'degree': 4, 'spectral_definition': None, 'expected': 'MISSING_NORMALIZATION'},
]
fixture_rows = []
for fixture in fixtures:
    args = {key: value for key, value in fixture.items() if key not in ('name', 'expected')}
    result = assess(**args, hypotheses_confirmed=True)
    assert result['status'] == fixture['expected'], (fixture, result)
    baseline_accepts = F(fixture['pc_upper']) < 1 / F(fixture['spectral_upper'])
    fixture_rows.append({'case': fixture['name'], 'baseline_accepts': baseline_accepts, 'after': result})
# Boundary equality must not certify a strict gap; missing mathematical evidence must fail closed.
assert assess(pc_upper='1/3', spectral_upper='1/3', degree=9,
              spectral_definition='normalized_random_walk', hypotheses_confirmed=True)['status'] == 'NOT_CERTIFIED'
assert assess(pc_upper='1/5', spectral_upper='3/4', degree=6,
              spectral_definition='normalized_random_walk')['status'] == 'MISSING_HYPOTHESES'


def matrices(n, edges, p):
    m = len(edges)
    assert m <= 6
    T = [[F(0) for _ in range(n)] for _ in range(n)]
    D = [[F(0) for _ in range(n)] for _ in range(n)]
    for mask in range(1 << m):
        parent = list(range(n))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for bit, (u, v) in enumerate(edges):
            if mask & (1 << bit):
                parent[root(u)] = root(v)
        k = mask.bit_count()
        w = p ** k * (1-p) ** (m-k)
        dw = (k * p ** (k-1) * (1-p) ** (m-k) if k else F(0))
        dw -= ((m-k) * p ** k * (1-p) ** (m-k-1) if m-k else F(0))
        for x in range(n):
            for y in range(n):
                if root(x) == root(y):
                    T[x][y] += w
                    D[x][y] += dw
    return T, D


graphs = [
    ('path3', 3, [(0,1),(1,2)]),
    ('triangle', 3, [(0,1),(1,2),(2,0)]),
    ('square', 4, [(0,1),(1,2),(2,3),(3,0)]),
    ('K4', 4, [(x,y) for x in range(4) for y in range(x+1,4)]),
]
checks = 0
for name, n, edges in graphs:
    for p in (F(1,4), F(1,2), F(3,4)):
        T, D = matrices(n, edges, p)
        for x in range(n):
            for y in range(n):
                rhs = sum((T[x][u]*T[v][y]+T[x][v]*T[u][y] for u,v in edges), F(0))
                assert 0 <= D[x][y] <= rhs, (name, str(p), x, y, D[x][y], rhs)
                checks += 1

p = F(3,4)
factor = 3*p*p
tree_columns = {str(n): str(1+4*p*p*sum((factor**k for k in range(n)),F(0))) for n in (1,10,20)}
# The conservative spectral upper bounds used in fixtures are proved by squaring.
assert F(7,8)**2 > F(3,4)  # sqrt(3)/2 < 7/8
assert F(3,4)**2 > F(5,9)  # sqrt(5)/3 < 3/4
out = {
    'state': 'passed', 'gate': gate,
    'seconds_cpu_work_wall': time.perf_counter()-start,
    'fixture_scope': 'four self-authored regression cases; not a blind benchmark',
    'baseline_unsupported_acceptances': 3,
    'after_unsupported_acceptances': 0,
    'valid_sufficient_case_preserved': 1,
    'fixtures': fixture_rows,
    'exact_Russo_BK_entry_checks': checks,
    'graphs': [name for name,_,_ in graphs],
    'total_Bernoulli_configurations': 3*sum(2**len(edges) for _,_,edges in graphs),
    'tree_exponential_decay_counterexample': {
        'degree': 4, 'p': '3/4', 'squared_column_shell_growth_factor': str(factor),
        'partial_squared_column_norms': tree_columns,
        'conclusion': 'Exact geometric growth proves divergence; the finite sums alone are only illustrations.'},
    'proof_status': 'These checks corroborate L02 and L04; they do not prove the infinite graph theorem or the parent conjecture.',
}
(ROOT / 'MEASUREMENTS.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
