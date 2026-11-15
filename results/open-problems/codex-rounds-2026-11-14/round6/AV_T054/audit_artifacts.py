"""Verify exact source quotations and final artifact consistency, read-only."""

import ast
import hashlib
import os
from pathlib import Path
import re
import resource
import signal


signal.alarm(30)
root = Path(__file__).resolve().parent
verify = (root/'VERIFY.md').read_text()
quotes = re.findall(r'```tex\n(.*?)\n```',verify,re.S)
assert len(quotes) == 3
pattern = r'\\begin\{theorem\}.*?\\end\{theorem\}'
for key,quote in zip(['goe','anderson','ising'],quotes):
    filename = key+'-theorem-source.tex'
    sources = [root/filename]
    sources += [Path(f'~/codex_op_1114r{r}/briefs/AV_T054')/filename
                for r in [3,4,5]]
    for source in sources:
        assert re.search(pattern,source.read_text(),re.S).group() == quote
    print('PASS exact_theorem',key,'characters',len(quote),'source_versions',len(sources))

catalogue = (root/'lean-catalogue.yaml').read_text().lower()
for slug in ['goe-bulk-universality-for-fixed-degree',
             'fixed-energy-universality-for-weak-anderson',
             'conformal-universality-of-bulk-ising-correlations']:
    assert slug not in catalogue
names = (root/'lean-docs-files.txt').read_text().splitlines()
assert len(names) == len(set(names)) == 245
assert '218.md' in names and '219.md' not in names
assert (root/'LICENSE.openai-math').read_text().startswith('                                 Apache License') or 'Apache License' in (root/'LICENSE.openai-math').read_text()[:100]
print('PASS current_Lean_catalogue_and_scope_inventory; license_saved')

report = (root/'REPORT.md').read_text()
assert report.startswith('VERDICT: PROVED ')
assert 'PARTIAL-CLAIMED' in report and 'PARTIAL-CLAIMED' in verify
assert 'without simple spectrum' in report.splitlines()[0]
row = verify.split('## Recommended replacement for “where it stands” (three sentences)\n\n')[1].split('\n\n')[0]
assert len(re.split(r'(?<=\.)\s+',row)) == 3
assert 'GOE bulk universality for fixed-degree random regular graphs' in row
assert '23 September 2026' in row
print('PASS continuation_verdict_and_three_sentence_row')

for name in ['REPORT.md','PROOF.md','VERIFY.md','LOG.md','audit_matrix.py','audit_artifacts.py']:
    data = (root/name).read_bytes()
    assert not any(b<32 and b not in (9,10,13) for b in data)
    if name.endswith('.py'):
        ast.parse(data,filename=name)
    print('FILE',name,'bytes',len(data),'sha256',hashlib.sha256(data).hexdigest())
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS,0) >= 15
print('PASS syntax_and_control_characters')
print('peak_rss_bytes',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
