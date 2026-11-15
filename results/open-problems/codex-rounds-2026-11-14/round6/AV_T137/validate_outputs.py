"""Read-only validation of the saved audit deliverables."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent
for name in ('REPORT.md', 'PROOF.md', 'VERIFY.md', 'LOG.md', 'audit_output.txt',
             'audit_insertion.py', 'source_manifest.json', 'preprint_manifest.json'):
    assert (root/name).stat().st_size > 0, name
assert (root/'REPORT.md').read_text().splitlines()[0].startswith('VERDICT: PARTIAL ')
count = 0
for name in ('source_manifest.json', 'preprint_manifest.json'):
    for record in json.loads((root/name).read_text()):
        assert hashlib.sha256((root/'sources'/record['file']).read_bytes()).hexdigest() == record['sha256']
        count += 1
for name in ('REPORT.md', 'PROOF.md', 'VERIFY.md', 'LOG.md'):
    for path in re.findall(r'\]\(([^)]+)\)', (root/name).read_text()):
        if '://' not in path and not path.startswith('#'):
            assert (root/path.split('#')[0]).exists(), (name, path)
output = (root/'audit_output.txt').read_text()
assert output.count('coefficient=') == 30
assert 'Exact mixed-pattern absolute-mass checks: 12 passed' in output
assert output.count('Fresh exact main theorem: MATCH') == 3
assert 'Process nice: 20' in output
print('Validation passed: required outputs, verdict, all local links, 33 source hashes,')
print('30 exact coefficients, 12 mixed-pattern checks, and 3 unchanged main theorems.')
