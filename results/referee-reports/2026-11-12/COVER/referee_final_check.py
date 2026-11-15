"""Check report completion against the saved computational evidence."""
import json
from pathlib import Path

report=Path('REPORT.md').read_text()
assert report.splitlines()[0]=='Overall verdict: SOUND'
for k in range(1,7):
    assert f'## {k}.' in report
for name in ['referee_cones','referee_exact','referee_numeric']:
    result=json.loads(Path(name+'_results.json').read_text())
    assert result['passed'] is True
    assert result['seconds']<280
    assert result['max_rss_bytes']<10**9
    assert name+'.py' in report
cones=json.loads(Path('referee_cones_results.json').read_text())
assert [r['file'] for r in cones['cones']]==[f'cone_{i:02d}.json.gz' for i in range(30)]
assert cones['coefficient_count']==577620 and cones['boundary_tests']==84
assert 'GAP' not in report.splitlines()[0]
assert 'Corrections and scope clarifications' in report
print('PASS: report present; all 30 cones and all saved computational checks passed within resource limits.')
print('Report words:',len(report.split()))
