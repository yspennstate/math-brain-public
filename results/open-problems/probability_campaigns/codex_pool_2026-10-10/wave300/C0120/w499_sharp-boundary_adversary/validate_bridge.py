import itertools
import json
import math
from pathlib import Path
import random
from statistics import NormalDist
import time

base = Path(__file__).resolve().parent
gate = json.loads((base / 'COMPUTE_GATE_BRIDGE.json').read_text(encoding='utf-8'))
started = time.perf_counter()
rng = random.Random(4990120)
normal = NormalDist()
max_errors = []
enumerated_paths = 0
for n in range(1, 5):
    assert n <= gate['max_enumerated_layers']
    origin = rng.gauss(0, 1)
    width = min(n, 3)
    layers = [[rng.gauss(0, 1) for _ in range(width)] for _ in range(n)]
    count = width ** n
    assert enumerated_paths + count <= gate['max_enumerated_paths']
    direct = max(origin + math.fsum(layers[k][p[k]] for k in range(n)) for p in itertools.product(range(width), repeat=n))
    factored = origin + math.fsum(max(row) for row in layers)
    max_errors.append(abs(direct - factored))
    enumerated_paths += count
    assert max_errors[-1] < 1e-12

rows = []
for m in [16, 64, 256, 1024, 65536, 1000000]:
    assert m <= gate['max_scalar_m']
    a = normal.inv_cdf(1 - 1 / m)
    s = m ** (-0.5)
    delta = math.sqrt(s)
    rho = math.exp(-s)
    tau = math.sqrt(-math.expm1(-2 * s))
    p_interval = 0.5 * (math.erfc(a / math.sqrt(2)) - math.erfc((a + delta) / math.sqrt(2)))
    top_two_event = (m * (m - 1) / 2) * p_interval ** 2 * math.exp((m - 2) * math.log1p(-1 / m))
    conditional_flip_floor = normal.cdf(-rho * delta / (math.sqrt(2) * tau))
    mismatch_floor = top_two_event * conditional_flip_floor
    assert a * delta <= 1
    assert 0 < mismatch_floor < 1
    rows.append({'m': m, 'a_m': a, 'OU_time': s, 'a_sqrt_s': a * delta, 'top_two_event_probability': top_two_event, 'per_layer_mismatch_lower_bound': mismatch_floor, 'N_times_mismatch_lower_bound': m * mismatch_floor, 'whole_path_change_lower_bound': -math.expm1(m * math.log1p(-mismatch_floor))})
    assert time.perf_counter() - started < gate['max_runtime_seconds']

result = {'command': 'python -X utf8 ~/brain_workers/w499/validate_bridge.py', 'finite_identity_cases': len(max_errors), 'paths_enumerated': enumerated_paths, 'max_identity_error': max(max_errors), 'scalar_event_cases': len(rows), 'elapsed_seconds': time.perf_counter() - started, 'status': 'PASS', 'interpretation': 'Arithmetic and indexing checks only. The Theta variance and limits are proved analytically in ATTEMPT.md and await independent referee.', 'rows': rows}
(base / 'BRIDGE_MEASUREMENTS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
