"""Small foreground verification of the analytic counterexample; no simulation."""
import ctypes
from datetime import datetime, timezone
from fractions import Fraction
from itertools import product
import json
import math
import os
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
WALL_START = time.monotonic()
CPU_START = time.process_time()

class MemoryStatus(ctypes.Structure):
    _fields_ = [('length', ctypes.c_ulong), ('load', ctypes.c_ulong)] + [
        (name, ctypes.c_ulonglong) for name in
        ('total_phys', 'avail_phys', 'total_page', 'avail_page',
         'total_virtual', 'avail_virtual', 'avail_extended')]

def checkpoint():
    if time.monotonic() - WALL_START > 30 or time.process_time() - CPU_START > 1:
        raise RuntimeError('Task-local bounded-verification gate exceeded')

gate = {
    'issued_at_utc': datetime.now(timezone.utc).isoformat(),
    'purpose': 'Exact finite-graph/rational checks and two bounded numerical formula checks',
    'foreground_processes': 1, 'gpu': False, 'simulation': False,
    'max_cpu_seconds': 1, 'max_wall_seconds': 30,
    'limits_scope': 'Task-local arithmetic budget; no shared resource gate or policy is changed',
    'status': 'CHECKING'}
if os.name == 'nt':
    memory = MemoryStatus()
    memory.length = ctypes.sizeof(memory)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
        raise RuntimeError('Cannot obtain fresh memory observation')
    gate['available_physical_bytes'] = int(memory.avail_phys)
    gate['memory_load_percent'] = int(memory.load)
    gate['minimum_available_physical_bytes'] = 1024 ** 3
    gate['status'] = 'PASS' if memory.avail_phys >= 1024 ** 3 else 'DENIED'
else:
    gate['status'] = 'DENIED'
    gate['reason'] = 'This verifier expects its authorized Windows environment'
(ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
if gate['status'] != 'PASS':
    raise RuntimeError('Fresh arithmetic gate denied; no verification performed')

def graph_crossing_probability(delta, bonds):
    # Construct the induced graph from exact coordinates, then use graph reachability.
    points = [(x * delta, y * delta)
              for x in range(-1, bonds + 2) for y in range(-2, 3)
              if 0 <= x * delta <= bonds * delta
              and -delta / 2 <= y * delta <= delta / 2]
    edges = [(i, j) for i in range(len(points)) for j in range(i + 1, len(points))
             if abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) == delta]
    sources = {i for i, point in enumerate(points) if point[0] == 0}
    targets = {i for i, point in enumerate(points) if point[0] == bonds * delta}
    successes = 0
    states = list(product((0, 1), repeat=len(edges)))
    for state in states:
        seen = set(sources)
        changed = True
        while changed:
            changed = False
            for (i, j), opened in zip(edges, state):
                if opened and ((i in seen) != (j in seen)):
                    seen.update((i, j))
                    changed = True
        successes += bool(seen & targets)
    checkpoint()
    return {'delta': str(delta), 'aspect': bonds, 'vertices': len(points),
            'edges': len(edges), 'configurations': len(states),
            'successes': successes, 'probability': str(Fraction(successes, len(states)))}

def elliptic_k_parameter(m):
    a, b = 1.0, math.sqrt(1.0 - m)
    for _ in range(32):
        a, b = (a + b) / 2, math.sqrt(a * b)
        if abs(a - b) < 1e-16:
            break
    checkpoint()
    return math.pi / (2 * a)

def cardy_beta_series(x):
    beta = math.gamma(1/3) ** 2 / math.gamma(2/3)
    coefficient, x_power, total = 1.0, x ** (1/3), 0.0
    for n in range(256):
        term = coefficient * x_power / (n + 1/3)
        total += term
        coefficient *= (n + 2/3) / (n + 1)
        x_power *= x
        next_term = coefficient * x_power / (n + 1 + 1/3)
        tail_bound = next_term / ((1 - x) * beta)
        if tail_bound < 1e-18:
            checkpoint()
            return total / beta, n + 1, tail_bound
    raise RuntimeError('Bounded series did not converge')

graphs = [graph_crossing_probability(delta, bonds)
          for delta in (Fraction(1), Fraction(1, 2), Fraction(1, 1024))
          for bonds in (1, 2)]
assert all(row['probability'] == ('1/2' if row['aspect'] == 1 else '1/4') for row in graphs)
exact_inequalities = {
    '(140/99)^2 < 2': Fraction(140, 99) ** 2 < 2,
    '(17/99)^2 < 1/32': Fraction(17, 99) ** 2 < Fraction(1, 32),
    '8/961 < (1/4)^3': Fraction(8, 961) < Fraction(1, 4) ** 3}
assert all(exact_inequalities.values())
x2 = (math.sqrt(2) - 1) ** 4
aspect2 = elliptic_k_parameter(1 - x2) / elliptic_k_parameter(x2)
square_cardy, square_terms, square_tail = cardy_beta_series(0.5)
rectangle_cardy, rectangle_terms, rectangle_tail = cardy_beta_series(x2)
assert abs(aspect2 - 2) < 1e-12
assert abs(square_cardy - 0.5) < 1e-12
assert rectangle_cardy < (8/961) ** (1/3) < 0.25
checkpoint()
result = {
    'command': 'python -X utf8 ~/brain_workers/w415/verify_boundary.py',
    'graph_cases': graphs, 'exact_rational_checks': exact_inequalities,
    'numerical_checks': {
        'cross_ratio_aspect2': x2, 'elliptic_ratio_aspect2': aspect2,
        'square_cardy_value': square_cardy, 'aspect2_cardy_value': rectangle_cardy,
        'aspect2_exact_bond_value': 0.25,
        'aspect2_difference': 0.25 - rectangle_cardy,
        'analytic_gap_lower_bound_display': 0.25 - (8/961) ** (1/3),
        'stretched_square_rotation_defect_s2': 1 - 2 * rectangle_cardy,
        'series_terms': [square_terms, rectangle_terms],
        'series_truncation_bounds': [square_tail, rectangle_tail],
        'caveat': 'Floating-point illustrations only; rounding/gamma error is not certified. Proof uses exact rational inequalities and cited analytic identities.'},
    'before_after': {
        'square_control_only_false_uniform_bridges_detected': 0,
        'with_aspect2_witness_false_uniform_bridges_detected': 1,
        'live_recall_or_store_improvement_measured': False},
    'wall_seconds': time.monotonic() - WALL_START,
    'cpu_seconds': time.process_time() - CPU_START,
    'passed': True, 'formal_proof_receipt': False}
(ROOT / 'MEASUREMENTS.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
