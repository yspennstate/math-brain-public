"""Independent bit-mask counts and final saved-artifact audit."""
import ast
import itertools
import json
import os
import resource
import signal
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(30)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

# A second implementation of small-support connectivity, using integer masks
# and an adjacency matrix instead of the tuple-set flood fills in the checker.
points = list(itertools.product(range(3), repeat=2))
neighbors = []
for p in points:
    mask = 0
    for j, q in enumerate(points):
        if p != q and max(abs(p[k]-q[k]) for k in range(2)) == 1:
            mask |= 1 << j
    neighbors.append(mask)


def expand(mask):
    ans = mask
    for j in range(9):
        if mask & (1 << j):
            ans |= neighbors[j]
    return ans


def connected(mask):
    visited = mask & -mask
    while True:
        new = expand(visited) & mask
        if new == visited:
            return visited == mask
        visited = new


connected_sets = [mask for mask in range(1, 512) if connected(mask)]
pair_count = sum(not (expand(a) & b) for a in connected_sets for b in connected_sets)
geometry = json.loads(Path('geometry_checks.json').read_text())
assert len(connected_sets) == geometry['connected_supports_3x3'] == 388
assert pair_count == geometry['counts']['support_pairs'] == 204
assert geometry['counts']['ternary_2d'] == 3**9
assert geometry['counts']['binary_3d'] == 2**8
assert geometry['counts']['sparse_ternary_3d'] == 3**6
for record in geometry['examples']:
    d = record['dimension']
    assert (record['support'], record['neighborhood'], record['filled']) == (
        7**d-3**d, 9**d-1, 7**d)
    assert record['shared_exterior_neighborhood_sites'] == 5**(d-1)
    assert record['omitted_filled_sites'] == 1
    assert record['realized_nested_supports'] == 3
assert geometry['peak_rss_bytes'] < 1024**3 and geometry['elapsed_seconds'] < 20*60

recheck = json.loads(Path('independent_recheck.json').read_text())
assert len(recheck['comparisons']) == 3*2*3*3 == 54
assert [r['physical'] for r in recheck['examples']] == [2*(4*4+8*8), 2*(4*8+8*4)]
assert all(r['independent_average'] == 8*2*3*3 for r in recheck['examples'])
assert recheck['peak_rss_bytes'] < 1024**3 and recheck['elapsed_seconds'] < 20*60

for filename in ('recheck_replacement.py', 'check_geometry.py', 'audit_artifacts.py'):
    ast.parse(Path(filename).read_text())
for filename in ('LOG.md', 'PROOF.md', 'REPORT.md', 'recheck_output.txt',
                 'geometry_output.txt', 'independent_recheck.json', 'geometry_checks.json'):
    assert Path(filename).stat().st_size > 0
assert Path('REPORT.md').read_text().startswith('VERDICT: PARTIAL ')
assert not Path('SOLVED_ELSEWHERE.md').exists()
proof = Path('PROOF.md').read_text()
assert proof.count(r'\[') == proof.count(r'\]')
assert proof.count(r'\(') == proof.count(r'\)')
assert 'No surface-pressure estimate' in proof
print('Independent bit-mask counts:', len(connected_sets), 'connected supports;', pair_count,
      'ordered separated pairs.')
print('Volume counts, overlap counts, all 54 rechecks, syntax and saved artifacts verified.')
print('Effective nice:', os.getpriority(os.PRIO_PROCESS, 0))
print('Audit peak RSS bytes:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('Artifact audit passed.')
