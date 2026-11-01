"""Tiny foreground checks: fresh existing admission, <=2 CPU seconds, no workers."""
import json
import math
import time
from datetime import datetime
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE = Path('~/.claude/compute/compute_state.json')
started = time.process_time()
out = {'scope': 'Finite exact enumeration and finite-depth recurrences, not a proof of P0043',
       'command': 'python -X utf8 -B verify_small.py', 'checks': [], 'status': 'HELD'}


def budget():
    if time.process_time() - started > 2:
        raise RuntimeError('Tiny-run CPU budget reached; no larger run admitted')


def admission():
    state = json.loads(STATE.read_text(encoding='utf-8-sig'))
    fields = ('status', 'mode', 'cpu_pct', 'mem_load_pct', 'mem_avail_mb', 'commit_used_pct',
              'code_stale', 'governor_suspended', 'ts')
    gate = {key: state.get(key) for key in fields}
    gate['file_age_seconds'] = time.time() - STATE.stat().st_mtime
    gate['checked_epoch'] = time.time()
    gate['state_timestamp_age_seconds'] = (datetime.now() - datetime.strptime(state['ts'], '%Y-%m-%d %H:%M:%S')).total_seconds()
    gate['max_cpu_seconds'] = 2
    gate['worker_threads'] = 1
    gate['child_processes'] = 0
    gate['gpu_use'] = False
    gate['policy'] = 'Existing ok/warn admission only, plus stricter local tiny-run caps; no override'
    out['gate'] = gate
    allowed = (state.get('status') in {'ok', 'warn'}
               and 0 <= gate['file_age_seconds'] <= 60
               and 0 <= gate['state_timestamp_age_seconds'] <= 60
               and not state.get('code_stale') and not state.get('governor_suspended')
               and isinstance(state.get('cpu_pct'), (int, float)) and state['cpu_pct'] < 80
               and isinstance(state.get('mem_load_pct'), (int, float)) and state['mem_load_pct'] < 90
               and isinstance(state.get('mem_avail_mb'), (int, float)) and state['mem_avail_mb'] > 1024
               and isinstance(state.get('commit_used_pct'), (int, float)) and state['commit_used_pct'] < 95)
    if not allowed:
        raise RuntimeError('Fresh existing gate or stricter tiny-run caps do not admit this check')


def recurse(branches, p):
    s, deriv = Fraction(1), Fraction(0)
    for b in reversed(branches):
        z = 1 - p * s
        s, deriv = 1 - z ** b, b * z ** (b - 1) * (s + p * deriv)
    return s, deriv


def tree(branches):
    edges, level, next_id = [], [0], 1
    for b in branches:
        following = []
        for parent in level:
            for _ in range(b):
                edges.append((parent, next_id))
                following.append(next_id)
                next_id += 1
        level = following
    return edges, set(level)


def event(mask, edges, targets):
    reached = {0}
    for i, (parent, child) in enumerate(edges):
        if mask & (1 << i) and parent in reached:
            reached.add(child)
    return bool(reached & targets)


def enumerate_case(branches, p):
    edges, targets = tree(branches)
    edge_count = len(edges)
    assert edge_count <= 9
    f, deriv, open_piv = Fraction(0), Fraction(0), Fraction(0)
    for mask in range(1 << edge_count):
        budget()
        if not event(mask, edges, targets):
            continue
        opened = mask.bit_count()
        weight = p ** opened * (1 - p) ** (edge_count - opened)
        pivotals = sum(bool(mask & (1 << i)) and not event(mask ^ (1 << i), edges, targets)
                       for i in range(edge_count))
        assert pivotals <= len(branches)
        f += weight
        deriv += weight * (opened / p - (edge_count - opened) / (1 - p))
        open_piv += weight * pivotals
    expected_f, expected_deriv = recurse(branches, p)
    assert f == expected_f and deriv == expected_deriv and p * deriv == open_piv
    assert p * deriv <= len(branches) * f
    return {'branches': list(branches), 'p': str(p), 'configurations': 1 << edge_count,
            'probability': str(f), 'russo_derivative': str(deriv), 'exact_match': True}


def float_recurse(branches, p):
    s, deriv = 1.0, 0.0
    for b in reversed(branches):
        z = 1 - p * s
        s, deriv = -math.expm1(b * math.log1p(-p * s)), b * z ** (b - 1) * (s + p * deriv)
    return s, deriv


try:
    admission()
    for branches in ((2,), (2, 2), (3, 2)):
        for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
            out['checks'].append(enumerate_case(branches, p))
    out['exact_cases'] = len(out['checks'])
    out['configurations_enumerated'] = sum(item['configurations'] for item in out['checks'])

    k = [((n + 1) ** 2).bit_length() - 1 for n in range(4097)]
    branches = [1 << (1 + k[n] - k[n - 1]) for n in range(1, 4097)]
    assert branches[0] == 8 and set(branches[1:]) <= {2, 4}
    for n in range(1, 4097):
        assert (n + 1) ** 2 <= 2 * (1 << k[n]) <= 2 * (n + 1) ** 2
    out['level_inequalities_checked'] = 4096
    out['analytic_critical_survival_lower_bound'] = 6 / math.pi ** 2
    out['countertree_depths'] = []
    for n in (64, 256, 1024, 4096):
        budget()
        pairs = {str(p): float_recurse(branches[:n], p) for p in (0.48, 0.49, 0.495, 0.5)}
        assert pairs['0.5'][0] >= 6 / math.pi ** 2
        out['countertree_depths'].append({'depth': n, 'probability_and_derivative': pairs,
                                         'critical_window_mass_delta_001': pairs['0.5'][0] - pairs['0.49'][0]})
    out['regular_tree_checks'] = []
    for n in (1, 16, 256, 4096):
        for p in (0.25, 0.35, 0.45, 0.49, 0.5):
            budget()
            s, deriv = float_recurse([3] + [2] * (n - 1), p)
            assert 0 <= deriv <= 27 + 1e-10
            out['regular_tree_checks'].append({'depth': n, 'p': p, 'probability': s, 'derivative': deriv})
    out['maximum_sampled_regular_tree_derivative'] = max(item['derivative'] for item in out['regular_tree_checks'])
    out['uniform_regular_tree_derivative_bound_proved_in_packet'] = 27
    out['status'] = 'PASS'
except (OSError, ValueError, RuntimeError, AssertionError) as exc:
    out['reason'] = str(exc) or type(exc).__name__
    out['status'] = 'FAIL' if isinstance(exc, AssertionError) else 'HELD'
finally:
    out['cpu_seconds'] = time.process_time() - started
    (ROOT / 'MEASUREMENTS.json').write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in out.items() if key not in {'checks', 'countertree_depths', 'regular_tree_checks'}}))
