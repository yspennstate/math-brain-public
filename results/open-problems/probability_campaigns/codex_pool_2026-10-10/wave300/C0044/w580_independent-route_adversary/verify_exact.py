"""Tiny serial rational check of the explicit iid uniformly elliptic example."""
from datetime import datetime
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math
import time

root = Path(__file__).resolve().parent
state_path = Path('~/.claude/compute/compute_state.json')
state = json.loads(state_path.read_text(encoding='utf-8-sig'))
sample_time = datetime.strptime(state['ts'], '%Y-%m-%d %H:%M:%S')
age = (datetime.now() - sample_time).total_seconds()
fields = ('ts','status','mode','reasons','cpu_pct','mem_avail_mb','commit_eff_used_pct','commit_eff_avail_mb','hung_windows')
gate = {k: state.get(k) for k in fields}
gate['age_seconds'] = age
gate['scope'] = 'one serial finite-stencil rational check, at most 128 states; no models, GPU, parallelism or sweep'
gate['allowed'] = (0 <= age <= 90 and state.get('status') not in ('distress','critical')
                   and state.get('mode') in ('owner_present_polite','owner_away_open','open')
                   and isinstance(state.get('cpu_pct'), (int,float)) and math.isfinite(state['cpu_pct']) and state['cpu_pct'] < 95
                   and isinstance(state.get('mem_avail_mb'), (int,float)) and state['mem_avail_mb'] > 4096
                   and isinstance(state.get('commit_eff_used_pct'), (int,float)) and state['commit_eff_used_pct'] < 85
                   and isinstance(state.get('commit_eff_avail_mb'), (int,float)) and state['commit_eff_avail_mb'] > 16384
                   and state.get('hung_windows') == 0)
(root / 'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2), encoding='utf-8')
if not gate['allowed']:
    result = {'status':'GATE_CLOSED','gate':gate,'experiments_run':0}
    (root/'EXACT_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
    raise SystemExit(3)

t0 = time.perf_counter()
d = 3
origin = (0,)*d
steps = [tuple(sign if j==i else 0 for j in range(d)) for i in range(d) for sign in (1,-1)]
e = steps[0]
neg = lambda v: tuple(-x for x in v)
sub = lambda a,b: tuple(x-y for x,y in zip(a,b))
sites = sorted({origin, neg(e), *(sub(v,e) for v in steps)})
b,delta = F(1,6),F(1,12)
def row(sign):
    return (b+delta*sign, b-delta*sign, b,b,b,b)

mean_f = mean_kf = mean_current = mean_kcurrent = F(0)
count = 0
for signs in product((-1,1),repeat=len(sites)):
    omega = dict(zip(sites, signs))
    for sign in signs:
        assert sum(row(sign)) == 1
        assert min(row(sign)) >= F(1,12)
    weights = row(omega[origin])
    f = row(omega[neg(e)])[0]
    kf = sum((weights[i]*row(omega[sub(v,e)])[0] for i,v in enumerate(steps)),F(0))
    mean_f += f
    mean_kf += kf
    count += 1
mean_f /= count
mean_kf /= count
assert count == 128
assert mean_f == F(1,6)
assert mean_kf == F(25,144)
assert mean_kf-mean_f == delta**2 == F(1,144)

incoming_sites = [neg(v) for v in steps]
density_mean = density_square = density_abs = F(0)
histogram = {}
for signs in product((-1,1), repeat=len(incoming_sites)):
    S = sum((row(signs[i])[i] for i in range(len(steps))),F(0))
    histogram[str(S)] = histogram.get(str(S),0)+1
    density_mean += S
    density_square += (S-1)**2
    density_abs += abs(S-1)
density_count = 2**len(incoming_sites)
density_mean /= density_count
density_square /= density_count
tv = density_abs/(2*density_count)
assert density_mean == 1
assert density_square == 2*delta**2 == F(1,72)
assert tv == F(1,24)
assert histogram == {'1':32,'5/6':16,'7/6':16}

# Controls: a fresh-site marginal misses the bias; deterministic rows have none.
current_expectation = sum((b*b for _ in steps),F(0))
assert current_expectation == b
deterministic_incoming = sum((b for _ in steps),F(0))
assert deterministic_incoming == 1

result = {'status':'PASS','command':'python -X utf8 ~/brain_workers/w580/verify_exact.py',
          'observable_stencil_states':count,'density_stencil_states':density_count,
          'uniform_ellipticity_lower_bound':'1/12','before_expectation':str(mean_f),
          'after_one_step_expectation':str(mean_kf),'stationarity_residual':str(mean_kf-mean_f),
          'chi_square':str(density_square),'total_variation':str(tv),'density_histogram':histogram,
          'fresh_site_expectation_before_and_after':str(current_expectation),
          'deterministic_density_control':str(deterministic_incoming),
          'wall_seconds':time.perf_counter()-t0,'gate':gate,'proof_receipt':False,
          'meaning':'Exact finite example check; does not prove the general lemma or resolve C0044.'}
(root/'EXACT_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
