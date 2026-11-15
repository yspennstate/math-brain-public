"""Check exact main-theorem quotations and compare the earlier snapshots."""

from pathlib import Path
import hashlib
import os
import re
import resource


ROOT = Path(__file__).resolve().parent
EARLIER = Path('~/codex_op_1114/briefs/AV_T054')
CASES = {
    'goe': 'GOE-introduction.tex',
    'anderson': 'Anderson-introduction.tex',
    'ising': 'Ising-model.tex',
}
verify = (ROOT / 'VERIFY.md').read_text()
quoted = re.findall(r'```tex\n(.*?)\n```', verify, re.S)
assert len(quoted) == 3
for (key, previous), quote in zip(CASES.items(), quoted):
    current = (ROOT / f'{key}-theorem-source.tex').read_text()
    old = (EARLIER / previous).read_text()
    pattern = r'\\begin\{theorem\}.*?\\end\{theorem\}'
    now_theorem = re.search(pattern, current, re.S).group()
    old_theorem = re.search(pattern, old, re.S).group()
    assert quote == now_theorem == old_theorem
    print(f'{key}: exact quote and unchanged theorem, chars={len(quote)}')
names = (ROOT / 'lean-docs-files.txt').read_text().splitlines()
assert len(names) == 245 and '218.md' in names and '219.md' not in names
print('Lean scope-note inventory: 245; 218 present; 219 absent')
report = (ROOT / 'REPORT.md').read_text()
assert report.startswith('VERDICT: PROVED ')
for file in ('REPORT.md', 'VERIFY.md', 'PROOF.md', 'LOG.md'):
    data = (ROOT / file).read_bytes()
    assert not any(byte < 32 and byte not in (9, 10, 13) for byte in data)
    print(f'{file}: bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()}')
print('nice', os.getpriority(os.PRIO_PROCESS, 0))
print('OMP_NUM_THREADS', os.environ.get('OMP_NUM_THREADS'))
print('peak_rss_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
