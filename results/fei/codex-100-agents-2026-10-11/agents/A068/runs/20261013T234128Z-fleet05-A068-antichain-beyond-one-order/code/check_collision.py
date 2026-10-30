import json
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter

start = perf_counter()
checks = 0
def check(condition):
    global checks
    assert condition
    checks += 1

def spectrum(values):
    return [sum(F(v * (-1 if (s & u).bit_count() % 2 else 1), len(values))
                for u, v in enumerate(values)) for s in range(len(values))]

for table in range(16):
    f = [1 if table >> u & 1 else -1 for u in range(4)]
    a = spectrum(f)
    for orientation in (1, -1):
        g = [f[u | ((u ^ (orientation == -1)) << 1)] for u in range(2)]
        b = spectrum(g)
        for s in range(2):
            paired = s ^ 3
            check(b[s] == a[s] + orientation * a[paired])
            check(b[s] ** 2 <= 2 * (a[s] ** 2 + a[paired] ** 2))
        check(sum(v*v for v in b) == 1)
        check(b[1] ** 2 == F(g[0] != g[1]))

# Regular AND2 core, with constant orientations (+1,-1), then identify data.
h = [1, -1, -1, -1]
f = [h[u ^ 2] for u in range(4)]
a = spectrum(f)
check(a == [F(-1,2), F(1,2), F(-1,2), F(-1,2)])
g = [f[u | (u << 1)] for u in range(2)]
check(g == [-1,-1])
# Accepted rank reference: w=(1/4,1/2,1/4), rank weights (1,1/4).
reference = [F(1,4), F(2,5), F(1,10), F(1,4)]
check(sum(reference) == 1)
push = [reference[s] + reference[s ^ 3] for s in range(2)]
check(push == [F(1,2),F(1,2)])
result = {
    'status': 'PASS', 'cases': 32, 'exact_assertions': checks,
    'runtime_seconds': perf_counter()-start,
    'witness': {'core': 'AND2', 'constant_control_orientations': [1,-1],
                'identification': 'x2=x1', 'output': 'constant -1',
                'parent_reference': list(map(str,reference)),
                'pushforward_reference': list(map(str,push)),
                'output_entropy_bits': 0, 'output_influence': 0,
                'complete_pushforward_reference_cost_bits': 1},
    'scope': 'Projection coefficient identity and naive inherited-reference obstruction; not a counterexample to FEI'
}
path = Path(__file__).resolve().parents[1] / 'out' / 'collision.json'
path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result))
