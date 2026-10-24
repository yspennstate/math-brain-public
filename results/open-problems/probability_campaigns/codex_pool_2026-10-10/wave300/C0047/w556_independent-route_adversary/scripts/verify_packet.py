"""Bounded arithmetic witnesses and source-level checks; not a Lean receipt."""
import ctypes
import datetime
import json
import math
import os
from pathlib import Path
import re
import shutil
import time

HERE = Path(__file__).resolve().parents[1]
sizes = (64, 256, 1024, 2048)
gate = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'kind': 'deterministic arithmetic/source check; no simulation, GPU or training',
        'max_arithmetic_terms': 8192, 'planned_arithmetic_terms': 2 * sum(sizes),
        'max_process_seconds': 2.0, 'disk_free_bytes': shutil.disk_usage(HERE).free}
if os.name == 'nt':
    class MemoryStatus(ctypes.Structure):
        _fields_ = [('length', ctypes.c_uint32), ('load', ctypes.c_uint32)] + [
            (name, ctypes.c_uint64) for name in
            ('total_physical', 'available_physical', 'total_page', 'available_page',
             'total_virtual', 'available_virtual', 'available_extended')]
    status = MemoryStatus()
    status.length = ctypes.sizeof(status)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
        raise RuntimeError('fresh memory gate unavailable')
    gate['available_physical_bytes'] = status.available_physical
    assert status.available_physical >= 64 * 1024 * 1024, 'fresh memory gate refused'
assert gate['disk_free_bytes'] >= 64 * 1024 * 1024, 'fresh disk gate refused'
assert 2 * sum(sizes) <= gate['max_arithmetic_terms']
gate['approved'] = True
(HERE / 'FRESH_COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
start = time.process_time()

witnesses = []
for n in sizes:
    rayleigh = 1 + 2 * math.fsum((1 - m / n) * (1 + m) ** (-0.75) for m in range(1, n))
    lower = n * (1 + n) ** (-0.75)
    partial_row_square = 1 + 2 * math.fsum((1 + m) ** (-1.5) for m in range(1, n))
    assert partial_row_square < 5
    assert rayleigh >= lower
    assert lower > math.sqrt(5)
    witnesses.append({'n': n, 'rayleigh_quotient': rayleigh,
                      'analytic_lower_bound': lower,
                      'uniform_row_square_upper_bound': 5,
                      'finite_row_square_partial_sum': partial_row_square,
                      'invalid_row_only_bound_rejected': True})
assert all(a['rayleigh_quotient'] < b['rayleigh_quotient'] for a, b in zip(witnesses, witnesses[1:]))

admitted = []
for name in ('BenjaminiSchramm.lean', 'CayleyPercolation.lean'):
    text = (HERE / 'sources' / name).read_text(encoding='utf-8')
    matches = list(re.finditer(r'(?m)^theorem\s+([A-Za-z_][A-Za-z_0-9]*)', text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end]
        tokens = list(re.finditer(r'(?m)^\s*sorry\s*$', block))
        assert tokens, 'expected source-level admission missing; inspect changed source'
        admitted.append({'file': name, 'theorem': match.group(1),
                         'declaration_line': text[:match.start()].count('\n') + 1,
                         'admission_count': len(tokens),
                         'verdict': 'NOT_A_FORMAL_PROOF_RECEIPT'})
assert {r['theorem'] for r in admitted} == {'full_main', 'critical_laws', 'cayley_main', 'arbitrary_cayley'}

claims = [json.loads(line) for line in (HERE / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert len({r['id'] for r in claims}) == len(claims)
required = ('statement', 'assumptions', 'source', 'proof_or_counterexample',
            'independent_reviewer', 'remaining_gap', 'status')
for claim in claims:
    assert all(field in claim for field in required)
    assert claim['parent_problem_solved'] is False
elapsed = time.process_time() - start
assert elapsed < gate['max_process_seconds'], 'bounded CPU check exceeded budget'
receipt = {'command': 'python -X utf8 ~/brain_workers/w556/scripts/verify_packet.py',
           'gate': gate, 'process_seconds': elapsed, 'witnesses': witnesses,
           'source_level_admitted_theorems': admitted, 'claim_rows_checked': len(claims),
           'formal_compilation_run': False, 'trusted_axioms_obtained': False,
           'before': {'row_only_inference': 'would accept a bounded operator from finite row-square sums'},
           'after': {'counterexample': 'unbounded by the analytic interval lower bound',
                     'finite_witnesses_exceeding_sqrt5': len(witnesses),
                     'admitted_comparator_declarations_rejected_as_receipts': len(admitted)},
           'meaning': 'Finite arithmetic supports the analytic counterexample; it does not prove the parent conjecture or a deployed recall gain.'}
(HERE / 'VERIFICATION.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt, indent=2))
