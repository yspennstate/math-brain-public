#!/usr/bin/env python3
"""Read-only recheck of the preceding session's full twelve-corner result."""
import json
import os
from pathlib import Path
import resource
import runpy
import signal
import time

resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
signal.alarm(600)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
start = time.monotonic()
prior = Path('~/codex_op_1114r5/briefs/T101')
a = runpy.run_path(str(prior / 'audit_twelve.py'))
data = json.loads((prior / 'twelve_data.json').read_text())
found, stats = a['cells'](12)
expected = {a['segment_key'](tuple(map(tuple, s['corners']))):
            (tuple(s['horizontal']), tuple(s['vertical'])) for s in data['shapes']}
assert {s: v[:2] for s, v in found.items()} == expected
assert len(found) == 9901
a['audit_polynomial_identity'](found)
checks, leading, leading_F = a['audit_probabilities'](found)
counts, nodes = a['walks'](20)
for m in range(41):
    assert a['coefficient'](m) == data['root_counts'][str(2*m)]
for length in range(4, 21, 2):
    assert counts[length, 12] == data['root_counts'][str(length)]
out = dict(stats=stats, checks=checks, linear_coefficient=str(leading),
           leading_F=str(leading_F), walk_nodes=nodes,
           root_counts={str(l): counts[l, 12] for l in range(12, 21, 2)},
           elapsed_seconds=time.monotonic()-start,
           priority=os.getpriority(os.PRIO_PROCESS, 0))
Path('recheck.json').write_text(json.dumps(out, indent=2)+'\n')
out['full_peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert out['full_peak_rss_bytes'] < 1_000_000_000
Path('recheck.json').write_text(json.dumps(out, indent=2)+'\n')
print('PASS preceding result: every boundary and strip, polynomial identities,')
print('unit walks through 20, coefficients through 80, probabilities and tails.')
print({k: v for k, v in out.items() if k != 'checks'})
print('p=1/2:', checks[2]['R12'], checks[2]['B12'])
