"""Check exact source quotations and the final report's basic requirements."""

from pathlib import Path
import hashlib
import os
import re
import resource
import signal


signal.alarm(30)
root = Path(__file__).resolve().parent
previous = Path('~/codex_op_1114r3/briefs/AV_T054')
original = Path('~/codex_op_1114/briefs/AV_T054')
verify = (root / 'VERIFY.md').read_text()
quotes = re.findall(r'```tex\n(.*?)\n```', verify, re.S)
assert len(quotes) == 3
pattern = r'\\begin\{theorem\}.*?\\end\{theorem\}'
for (key, old_name), quote in zip((('goe', 'GOE-introduction.tex'),
                                 ('anderson', 'Anderson-introduction.tex'),
                                 ('ising', 'Ising-model.tex')), quotes):
    source_name = key + '-theorem-source.tex'
    fresh = re.search(pattern, (root / source_name).read_text(), re.S).group()
    round3 = re.search(pattern, (previous / source_name).read_text(), re.S).group()
    first = re.search(pattern, (original / old_name).read_text(), re.S).group()
    assert quote == fresh == round3 == first
    print(f'PASS {key}: exact theorem, unchanged from both earlier snapshots, chars={len(quote)}')

names = (root / 'lean-docs-files.txt').read_text().splitlines()
assert len(names) == 245 and '218.md' in names and '219.md' not in names
catalogue = (root / 'lean-catalogue.yaml').read_text().lower()
for title in ('GOE bulk universality for fixed-degree random regular graphs',
              'Fixed-energy universality for weak Anderson disorder on random regular graphs',
              'Conformal universality of bulk Ising correlations under weak interactions'):
    assert title.lower() not in catalogue
print('PASS Lean catalogue: no exact main-theorem titles; scope notes 245, 218 present, 219 absent')

report = (root / 'REPORT.md').read_text()
assert report.startswith('VERDICT: PROVED ')
assert len(report.splitlines()[1:4]) == 3
assert 'being completed' not in report
paragraph = verify.split('## Recommended replacement for “where it stands” (three sentences)\n\n')[1].split('\n\n')[0]
assert len(re.findall(r'\.(?:\s|$)', paragraph)) == 3
assert 'GOE bulk universality for fixed-degree random regular graphs' in paragraph
assert '23 September 2026' in paragraph
print('PASS continuation verdict; three-sentence recommended status')

for name in ('VERIFY.md', 'PROOF.md', 'REPORT.md', 'LOG.md',
             'audit_subsets.py', 'audit_artifacts.py'):
    data = (root / name).read_bytes()
    assert not any(b < 32 and b not in (9, 10, 13) for b in data)
    print(f'{name}: bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()}')
print('nice', os.getpriority(os.PRIO_PROCESS, 0))
print('OMP_NUM_THREADS', os.environ.get('OMP_NUM_THREADS'))
print('peak_rss_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
