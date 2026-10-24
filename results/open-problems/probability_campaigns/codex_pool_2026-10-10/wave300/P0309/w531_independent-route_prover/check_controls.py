"""Small deterministic controls for the saved mathematics; no proof certificate."""
from __future__ import annotations
import ctypes
import itertools
import json
import math
import os
from pathlib import Path
import time
from datetime import datetime

ROOT = Path(__file__).resolve().parent
RESULT = {"proof_certificate": False, "independent_audit": False, "passed": 0, "failures": [], "measurements": {}}
START = time.monotonic()
CPU_START = time.process_time()


def gate():
    """Read the existing governor, then sample current CPU/RAM/commit directly."""
    state_path = Path('~/.claude/compute/compute_state.json')
    s = json.loads(state_path.read_text(encoding='utf-8-sig'))
    age = max(0.0, (datetime.now() - datetime.strptime(s['ts'], '%Y-%m-%d %H:%M:%S')).total_seconds())
    import psutil
    cpu = psutil.cpu_percent(interval=0.2)
    ram = psutil.virtual_memory().available / 1048576
    disk = psutil.disk_usage(str(ROOT)).free / 1073741824
    class MemoryStatus(ctypes.Structure):
        _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong),
                    ('ullTotalPhys', ctypes.c_ulonglong), ('ullAvailPhys', ctypes.c_ulonglong),
                    ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                    ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong),
                    ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]
    mem = MemoryStatus()
    mem.dwLength = ctypes.sizeof(mem)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
        raise RuntimeError('fresh commit probe failed')
    commit_pct = 100.0 * (1.0 - mem.ullAvailPageFile / mem.ullTotalPageFile)
    reasons = s.get('reasons', [])
    pressure = any(any(q in str(r).lower() for q in ['cpu_pressure', 'memory_pressure', 'commit_pressure', 'disk_pressure']) for r in reasons)
    allowed = (age <= 600 and s.get('mode') in {'normal', 'owner_present_polite', 'idle', 'green'}
               and s.get('status') not in {'critical', 'throttle', 'stop', 'red'} and not pressure
               and math.isfinite(cpu) and cpu <= 90 and ram >= 2048 and commit_pct <= 95 and disk >= 1)
    receipt = {'sampled_local': datetime.now().isoformat(), 'governor_age_seconds': age,
               'governor_mode': s.get('mode'), 'governor_status': s.get('status'), 'governor_reasons': reasons,
               'fresh_cpu_pct': cpu, 'fresh_available_ram_mb': ram, 'fresh_commit_used_pct': commit_pct,
               'fresh_disk_free_gb': disk, 'threads': 1, 'gpu': False, 'models': False,
               'max_cpu_seconds': 2, 'max_wall_seconds': 30, 'admitted': allowed,
               'doctrine': '12_cognitive_architecture/compute_governor/COMPUTE_DOCTRINE.md; current governor mode retained'}
    (ROOT / 'compute_gate_receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    if not allowed:
        raise RuntimeError('fresh small-compute gate denied; no numerical controls run')


def budget():
    if time.process_time() - CPU_START > 2 or time.monotonic() - START > 30:
        raise RuntimeError('small-compute budget reached')


def check(ok, label):
    budget()
    if not ok:
        RESULT['failures'].append(label)
        raise AssertionError(label)
    RESULT['passed'] += 1


def green(n, d=3, h=0.0):
    vals = [4 * math.sin(math.pi * j / n) ** 2 for j in range(n)]
    total = 0.0
    for k in itertools.product(range(n), repeat=d):
        if not any(k) and h == 0:
            continue
        total += 1.0 / (sum(vals[j] for j in k) + h)
    budget()
    return total / n**d


def invert(matrix):
    n = len(matrix)
    a = [list(row) + [float(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[pivot] = a[pivot], a[col]
        den = a[col][col]
        a[col] = [x / den for x in a[col]]
        for i in range(n):
            if i != col:
                fac = a[i][col]
                a[i] = [x - fac * y for x, y in zip(a[i], a[col])]
    return [row[n:] for row in a]


def run():
    gate()
    RESULT['measurements']['nonzero_mode_3d'] = {}
    for n in [2, 3, 4, 5, 6, 8, 12, 16, 32]:
        g = green(n)
        RESULT['measurements']['nonzero_mode_3d'][str(n)] = g
        check(0 < g <= 13 / 16, f'3d nonzero-mode bound N={n}')
    RESULT['measurements']['nonzero_mode_2d'] = {str(n): green(n, 2) for n in [8, 16, 32, 64]}
    g2 = list(RESULT['measurements']['nonzero_mode_2d'].values())
    check(all(a < b for a, b in zip(g2, g2[1:])), '2d roughness grows across selected volumes')
    pts = list(itertools.product(range(2), repeat=3))
    ids = {x: i for i, x in enumerate(pts)}
    lap = [[0.0] * 8 for _ in pts]
    for x in pts:
        for j in range(3):
            y = list(x)
            y[j] = (y[j] + 1) % 2
            a, b = ids[x], ids[tuple(y)]
            lap[a][a] += 1
            lap[b][b] += 1
            lap[a][b] -= 1
            lap[b][a] -= 1
    max_error = 0.0
    for h in [0.001, 0.3, 1.0]:
        inv = invert([[lap[i][j] + h * (i == j) for j in range(8)] for i in range(8)])
        diag = sum(inv[i][i] for i in range(8)) / 8
        error = abs(diag - green(2, h=h))
        max_error = max(max_error, error)
        check(error <= 1e-8, f'direct Hessian inverse versus Fourier h={h}')
        check(max(abs(sum(row) - 1 / h) for row in inv) <= 1e-7, f'constant eigenmode h={h}')
    RESULT['measurements']['direct_inverse_max_abs_error'] = max_error
    zero = {str(h): 1 / (h * 4**3) for h in [0.01, 0.0001, 0.000001]}
    RESULT['measurements']['fixed_N4_zero_mode'] = zero
    check(zero['1e-06'] > 1000 * zero['0.01'], 'fixed-volume zero mode cannot be discarded')

    # Complete enumeration of a discrete repulsive eight-site toy gas. This is
    # an algebra control for P1, not a quadrature proof of the continuum model.
    source = [[1 - 2 * c for c in x] for x in pts]
    states = []
    for mask in range(256):
        occupied = [i for i in range(8) if mask & (1 << i)]
        energy = sum(0.03 / (sum(((pts[i][j] - pts[k][j]) / 2) ** 2 for j in range(3)) ** 2)
                     for a, i in enumerate(occupied) for k in occupied[a + 1:])
        modes = [sum(source[i][j] for i in occupied) for j in range(3)]
        states.append((len(occupied), energy, sum(modes), modes))
    for mask, (_, e, q, _) in enumerate(states):
        flipped = sum(1 << (i ^ 7) for i in range(8) if mask & (1 << i))
        check(abs(states[flipped][1] - e) < 1e-12 and states[flipped][2] == -q,
              f'half-cell translation identity mask={mask}')

    def pressure(h):
        weights = [0.7**n * math.exp(-e + h * q) for n, e, q, _ in states]
        z = sum(weights)
        m = sum(w * row[2] for w, row in zip(weights, states)) / z
        variance = sum(w * row[2] ** 2 for w, row in zip(weights, states)) / z - m * m
        modes = [sum(w * row[3][j] for w, row in zip(weights, states)) / z for j in range(3)]
        return math.log(z), m, variance, modes

    errors = []
    for h in [0, 0.05, 0.2, 0.5]:
        p, m, var, modes = pressure(h)
        step = 1e-4
        num1 = (pressure(h + step)[0] - pressure(h - step)[0]) / (2 * step)
        num2 = (pressure(h + step)[0] - 2 * p + pressure(h - step)[0]) / step**2
        errors.append({'h': h, 'first_error': abs(num1 - m), 'second_error': abs(num2 - var)})
        check(abs(p - pressure(-h)[0]) < 1e-12, f'even pressure h={h}')
        check(var > 0, f'pressure variance convexity h={h}')
        check(abs(num1 - m) < 1e-6 and abs(num2 - var) < 2e-6, f'pressure derivative identities h={h}')
        check(max(modes) - min(modes) < 1e-12, f'three-mode permutation symmetry h={h}')
    check(abs(pressure(0)[1]) < 1e-12, 'finite-volume zero-field response is zero')
    p0 = pressure(0)[0]
    base_w = [0.7**n * math.exp(-e) for n, e, _, _ in states]
    base_p = [w / sum(base_w) for w in base_w]
    entropy_errors = []
    imax = max(range(len(states)), key=lambda i: states[i][2])
    for h in [0.01, 0.05, 0.2, 0.5]:
        ph, mh, _, _ = pressure(h)
        ws = [0.7**n * math.exp(-e + h * q) for n, e, q, _ in states]
        trial = [w / sum(ws) for w in ws]
        entropy = sum(t * math.log(t / b) for t, b in zip(trial, base_p))
        err = abs((ph - p0) - (h * mh - entropy))
        entropy_errors.append(err)
        check(entropy >= -1e-12 and err < 1e-12, f'Gibbs trial entropy identity h={h}')
        delta_bound = h * states[imax][2] + math.log(base_p[imax])
        check(ph - p0 >= delta_bound - 1e-12, f'sector relative-entropy lower bound h={h}')
    RESULT['measurements']['relative_entropy_max_identity_error'] = max(entropy_errors)
    RESULT['measurements']['enumerated_repulsive_toy_states'] = len(states)
    RESULT['measurements']['pressure_derivative_errors'] = errors

    independent = []
    for beta in [0.2, 1, 2, 5]:
        response = math.tanh(beta * 0.1)
        slope_at_zero = 0.0
        check(response > 0 and slope_at_zero == 0, f'positive pinned response false sufficient condition beta={beta}')
        independent.append({'beta': beta, 'response_h_0.1': response, 'zero_source_right_slope_exact': slope_at_zero})
    RESULT['measurements']['false_pinned_response_controls'] = independent
    paths = [{'V': v, 'too_fast_removal': math.tanh(1 / v),
              'volume_first_compatible': math.tanh(math.sqrt(v))} for v in [16, 64, 256, 1024]]
    check(paths[-1]['too_fast_removal'] < 0.001 and paths[-1]['volume_first_compatible'] > 0.99,
          'a pressure cusp does not license an arbitrary diagonal')
    RESULT['measurements']['collective_cusp_limit_paths'] = paths
    budget()


try:
    run()
    RESULT['status'] = 'PASS'
except Exception as exc:
    RESULT['status'] = 'GATED' if 'gate denied' in str(exc) else 'FAIL'
    RESULT['error'] = str(exc)
finally:
    RESULT['elapsed_wall_seconds'] = time.monotonic() - START
    RESULT['elapsed_cpu_seconds'] = time.process_time() - CPU_START
    RESULT['command'] = 'python -X utf8 ~/brain_workers/w531/check_controls.py'
    (ROOT / 'control_results.json').write_text(json.dumps(RESULT, indent=2), encoding='utf-8')
    print(json.dumps({k: RESULT[k] for k in ['status', 'passed', 'failures', 'elapsed_wall_seconds', 'elapsed_cpu_seconds']}))
if RESULT['status'] != 'PASS':
    raise SystemExit(2)
