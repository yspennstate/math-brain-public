"""Check source quotations, saved catalogue scope and report consistency."""

from pathlib import Path
import hashlib
import os
import re
import resource
import signal


signal.alarm(30)
root=Path(__file__).resolve().parent
verify=(root/'VERIFY.md').read_text()
quotes=re.findall(r'```tex\n(.*?)\n```',verify,re.S)
assert len(quotes)==3
pattern=r'\\begin\{theorem\}.*?\\end\{theorem\}'
first=Path('~/codex_op_1114/briefs/AV_T054')
round3=Path('~/codex_op_1114r3/briefs/AV_T054')
round4=Path('~/codex_op_1114r4/briefs/AV_T054')
for key,name,quote in zip(['goe','anderson','ising'],
                          ['GOE-introduction.tex','Anderson-introduction.tex','Ising-model.tex'],quotes):
    source_name=key+'-theorem-source.tex'
    versions=[(root/source_name).read_text(),
              (round3/source_name).read_text(),
              (round4/source_name).read_text(),
              (first/name).read_text()]
    for s in versions:
        assert re.search(pattern,s,re.S).group()==quote
    print('PASS exact_theorem_quote',key,'characters',len(quote),'snapshots',len(versions))
docs=(root/'lean-docs-files.txt').read_text().splitlines()
assert len(docs)==245 and '218.md' in docs and '219.md' not in docs
cat=(root/'lean-catalogue.yaml').read_text().lower()
assert not any(x in cat for x in [
    'goe-bulk-universality-for-fixed-degree',
    'fixed-energy-universality-for-weak-anderson',
    'conformal-universality-of-bulk-ising-correlations'])
print('PASS no_matching_selected_Lean_main_theorem')
report=(root/'REPORT.md').read_text()
assert report.splitlines()[0].startswith('VERDICT: PROVED ')
assert 'PARTIAL-CLAIMED' in report and 'PARTIAL-CLAIMED' in verify
row=verify.split('## Recommended replacement for “where it stands” (three sentences)\n\n')[1].split('\n\n')[0]
assert len(re.split(r'(?<=\.)\s+',row))==3
assert all(x in row for x in ['GOE bulk universality for fixed-degree random regular graphs','23 September 2026'])
for name in ['PROOF.md','VERIFY.md','REPORT.md','LOG.md','audit_bernstein.py']:
    data=(root/name).read_bytes()
    assert not any(b<32 and b not in (9,10,13) for b in data)
    print('FILE',name,'bytes',len(data),'sha256',hashlib.sha256(data).hexdigest())
assert os.getpriority(os.PRIO_PROCESS,0)>=15
assert os.environ.get('OMP_NUM_THREADS')=='1'
print('PASS report_format_three_sentence_row_and_no_control_characters')
print('peak_rss_bytes',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
