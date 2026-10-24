"""Small bounded arithmetic checks; the written proofs carry the mathematics."""
from datetime import datetime, timezone
from fractions import Fraction as R
import argparse
import json
import math
from pathlib import Path
import time

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--gate', default='COMPUTE_GATE.json')
parser.add_argument('--out', default='measurements.json')
args = parser.parse_args()
gate_path = root / args.gate
out_path = root / args.out
if gate_path.parent.resolve() != root or out_path.parent.resolve() != root:
    raise SystemExit('Outputs must stay in the worker folder')
gate = json.loads(gate_path.read_text(encoding='utf-8'))
if gate['state'] != 'fresh' or gate['gpu'] or gate['training'] or gate['network']:
    raise SystemExit('A fresh CPU-only gate is required')
gate.update(state='consumed', started_utc=datetime.now(timezone.utc).isoformat())
gate_path.write_text(json.dumps(gate, indent=2), encoding='utf-8')
start = time.monotonic()
cases = 0

def charge():
    global cases
    cases += 1
    if cases > gate['max_cases'] or time.monotonic()-start > gate['max_runtime_seconds']:
        raise RuntimeError('Compute gate exceeded')

def spectrum(g, xi, a):
    return (2-a*a/2)/(xi*(2/g+g/2-a))

# Independently evaluate the original rational expression and its square deficit.
identity_cases = 0
for gi in range(1, 16):
    g = R(gi, 8)
    Q = 2/g+g/2
    for xi in (R(1, 4), R(1, 2), R(1)):
        for a in [R(ai, 4) for ai in range(-8, 9)]+[g]:
            charge()
            value = spectrum(g, xi, a)
            assert g/xi-value == (a-g)**2/(2*xi*(Q-a))
            assert 0 <= value <= g/xi
            assert (value == g/xi) == (a == g)
            identity_cases += 1

# Same Euclidean spectrum, two incompatible absolute D values, zero KPZ residual.
kpz_cases = 0
countermodels = []
for g in (R(1, 2), R(1), R(3, 2), R(7, 4)):
    Q = 2/g+g/2
    for j in range(9):
        z = g*R(j, 8)
        x = Q*z-z*z/2
        profiles = []
        for D in (R(3), R(4)):
            charge()
            xi = g/D
            t = z/xi
            residual = x-(xi*Q*t-xi*xi*t*t/2)
            assert residual == 0
            assert 0 <= t <= D
            profiles.append({'D': str(D), 'x': str(x), 't': str(t),
                             'normalized_t': str(t/D), 'residual': str(residual)})
            kpz_cases += 1
        assert profiles[0]['normalized_t'] == profiles[1]['normalized_t']
        if g == 1 and j == 8:
            countermodels = profiles

# General-x optimizer: parameterize x by its exact optimizing alpha=z.
general_x_cases = 0
for g in (R(1, 2), R(1), R(3, 2), R(7, 4)):
    Q = 2/g+g/2
    xi = R(1, 2)
    for j in (0, 2, 4, 6, 8):
        z = g*R(j, 8)
        x = Q*z-z*z/2
        for a in (R(-2), R(-1), R(0), R(1), R(2), z):
            charge()
            raw = x-a*a/2
            t = z/xi
            clipped = max(raw, R(0))/(xi*(Q-a))
            assert clipped <= t
            if raw >= 0:
                assert t-raw/(xi*(Q-a)) == (a-z)**2/(2*xi*(Q-a))
            if x > 0:
                assert (clipped == t) == (a == z)
            else:
                assert clipped == 0
            general_x_cases += 1

# Endpoint paths have sharply different limiting constants despite the same corner.
boundary = []
for label, k in (('beta=delta^3', None), ('k=1/16', R(1,16)),
                 ('k=1/4', R(1,4)), ('k=1', R(1)), ('beta=delta', 'infinity')):
    rows=[]
    predicted = R(0) if k is None else (R(2) if k == 'infinity' else 8*k/(4*k+1))
    for power in (4, 8, 12, 16):
        charge()
        delta = R(1, 2**power)
        g = 2-delta
        beta = delta**3 if k is None else (delta if k == 'infinity' else k*delta**2)
        a = 2-beta
        value = spectrum(g, R(1), a)
        alternate = (2*beta-beta*beta/2)/(beta+delta*delta/(2*g))
        assert value == alternate
        rows.append({'power': power, 'value': float(value),
                     'absolute_error_from_limit': float(abs(value-predicted))})
    boundary.append({'path': label,'predicted_limit':float(predicted),'measurements':rows})

conditioning=[]
for power in (4, 8, 12, 16):
    charge()
    delta=R(1, 2**power)
    g=2-delta
    q=(4-g*g)/(2*g)
    conditioning.append({'power':power, 'gamma':float(g),
                         'optimal_lipschitz_constant':float(1/q)})

# Floating checks supplement the exact endpoint formula; they are not certificates.
holder_cases=0
max_ratio=0.0
for g in (0.5,1.0,1.5,1.99,1.9999):
    Q=2/g+g/2
    for x in (0.0,0.5,1.0,1.9,2.0):
        for y in (0.0,0.5,1.0,1.9,2.0):
            if x == y:
                continue
            charge()
            gap=abs(math.sqrt(Q*Q-2*x)-math.sqrt(Q*Q-2*y))
            bound=math.sqrt(2*abs(x-y))
            assert gap <= bound+1e-12
            max_ratio=max(max_ratio, gap/bound)
            holder_cases+=1

result={'gate_id':gate['gate_id'],'command':'python -X utf8 .\\measure_boundary.py --gate COMPUTE_GATE.json --out measurements.json',
        'cases':cases,'elapsed_seconds':time.monotonic()-start,
        'exact_deficit_cases':identity_cases,'exact_general_x_cases':general_x_cases,
        'exact_kpz_cases':kpz_cases,'exact_residual_failures':0,
        'absolute_dimension_countermodels':countermodels,
        'boundary_paths':boundary,'conditioning':conditioning,
        'floating_holder_cases':holder_cases,'max_observed_holder_ratio':max_ratio,
        'interpretation':'Arithmetic checks and numerical illustrations only; no original-target solution, independent audit, or formal proof receipt.'}
out_path.write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({key:result[key] for key in ('cases','elapsed_seconds','exact_deficit_cases','exact_general_x_cases','exact_kpz_cases','exact_residual_failures','absolute_dimension_countermodels','conditioning','interpretation')},indent=2))
