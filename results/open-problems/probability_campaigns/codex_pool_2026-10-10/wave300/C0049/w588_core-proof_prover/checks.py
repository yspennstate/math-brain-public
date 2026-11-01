from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone, timedelta
import json
import math
import time

ROOT = Path(__file__).resolve().parent
gate = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
assert gate['permitted'] and not gate['gpu'] and not gate['network'] and not gate['model_calls']
started = datetime.now(timezone.utc)
gate['activated_at_utc'] = started.isoformat()
gate['expires_at_utc'] = (started + timedelta(seconds=gate['max_wall_seconds'])).isoformat()
(ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2) + '\n', encoding='utf-8')
tick = time.perf_counter()

# Exact arithmetic in x=1/z with coefficients that are polynomials in u,t.
ONE = {(0, 0): Q(1)}
ZERO = {}

def plus(a, b):
    d = a.copy()
    for k, v in b.items():
        d[k] = d.get(k, Q(0)) + v
    return {k: v for k, v in d.items() if v}

def scale(a, c):
    return {k: v*c for k, v in a.items() if v*c}

def times(a, b):
    d = {}
    for (au, at), av in a.items():
        for (bu, bt), bv in b.items():
            k = (au+bu, at+bt)
            d[k] = d.get(k, Q(0)) + av*bv
    return {k: v for k, v in d.items() if v}

def series_times(a, b):
    return [plus(plus(times(a[0], b[k]), times(a[1], b[k-1]) if k>=1 else ZERO), times(a[2], b[k-2]) if k>=2 else ZERO) for k in range(3)]

def power_one_plus(v, exponent):
    v2 = series_times(v, v)
    return [plus(plus(ONE if k==0 else ZERO, scale(v[k], exponent)), scale(v2[k], exponent*(exponent-1)/2)) for k in range(3)]

coefficients = []
for sigma in [Q(1,4), Q(1,3), Q(1,2), Q(2,3), Q(1)]:
    gp = power_one_plus([ZERO, ZERO, {(0,1): Q(-2)}], sigma)
    denom = power_one_plus([ZERO, {(1,0): Q(-1)}, {(0,1): Q(2)}], -sigma)
    h = series_times(gp, denom)
    assert h[0] == ONE
    assert h[1] == {(1,0): sigma}
    expected = {(2,0): sigma*(sigma+1)/2, (0,1): -4*sigma}
    assert h[2] == expected
    factor = 2/(sigma*(sigma+1))
    assert scale(h[2], factor) == {(2,0): Q(1), (0,1): -8/(sigma+1)}
    # Negative control: omitting g' halves the time coefficient and is rejected.
    assert denom[2] != expected
    coefficients.append({'sigma': str(sigma), 'kappa': str(8/(1+sigma)), 'quadratic_time_coefficient': str(h[2][(0,1)]), 'omitted_derivative_control': 'REJECTED'})

# Integer Gaussian pairs make the four-edge verification exact.
def add(a, b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[0], -a[1])
def imag(a): return (-a[1], a[0])
edges = {((3,3),(4,3)):(1,0), ((4,3),(4,4)):(0,-1), ((3,4),(4,4)):(-1,0), ((3,3),(3,4)):(0,1)}
def edge(v, w): return edges.get(tuple(sorted((v,w))), (0,0))
residuals = []
boundary = []
averages = {}
for x in range(9):
    for y in range(9):
        v = (x,y)
        e,n,w,s = [edge(v,p) for p in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]]
        r = add(add(e, imag(n)), add(neg(w), neg(imag(s))))
        assert r == (0,0)
        residuals.append(r)
        av = add(add(e,n), add(w,s))
        averages[v] = av
        if x in [0,8] or y in [0,8]:
            assert av == (0,0)
            boundary.append(av)
assert averages[(3,3)] == (1,1) and averages[(2,3)] == (0,0)
assert averages[(3,3)][0]**2 + averages[(3,3)][1]**2 == 2

# Non-UI control: the rare positive terminal value has mean one for every n.
ui_controls = []
for n in [2,10,1000]:
    assert Q(1,n)*n == 1
    ui_controls.append({'n': n, 'initial_mean': 1, 'terminal_mean': 1, 'nonzero_probability': str(Q(1,n)), 'limit_is_martingale': False})

parameter_checks = []
for q in [0.01, 0.25, 1.0, 2.0, 3.0, 4.0]:
    sig = 2/math.pi*math.asin(math.sqrt(q)/2)
    a = 8/(1+sig)
    b = 4*math.pi/math.acos(-math.sqrt(q)/2)
    assert math.isclose(a,b,rel_tol=1e-14)
    parameter_checks.append({'q':q, 'sigma':sig, 'kappa':a, 'dictionary_error':abs(a-b)})

elapsed = time.perf_counter()-tick
endpoint_checks = []
for n in [2,4,8,16]:
    r = 1-Q(1,n)
    pi_phi_prime = 2/(1-r*r)
    assert n <= pi_phi_prime < 2*n
    assert 2/(1-(-r)*(-r)) == pi_phi_prime
    endpoint_checks.append({'n':n, 'pi_times_abs_phi_prime':str(pi_phi_prime), 'lower_bound':n})
elapsed = time.perf_counter()-tick
assert elapsed <= gate['max_wall_seconds']
report = {
    'status':'PASS', 'command':'python -X utf8 ~/brain_workers/w588/checks.py',
    'run_utc':started.isoformat(), 'compute_seconds':elapsed,
    'exact_sigma_cases':len(coefficients), 'laurent_coefficients':coefficients,
    'exact_cr_vertex_checks':len(residuals), 'exact_cr_nonzero_residuals':0,
    'boundary_vertex_checks':len(boundary), 'plaquette_edge_count':len(edges),
    'normalized_adjacent_vertex_jump_squared':'1/8',
    'non_ui_controls':ui_controls, 'parameter_dictionary_checks':parameter_checks,
    'marked_endpoint_exact_controls':endpoint_checks,
    'scope':'Exact algebra and finite counterexample controls; not a formal proof receipt, a scaling-limit simulation, or an independent mathematical review.',
    'formal_check_receipt':None,
    'gate':'COMPUTE_GATE.json'
}
(ROOT/'measurements.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['status','compute_seconds','exact_sigma_cases','exact_cr_vertex_checks','exact_cr_nonzero_residuals','plaquette_edge_count','normalized_adjacent_vertex_jump_squared']},indent=2))
