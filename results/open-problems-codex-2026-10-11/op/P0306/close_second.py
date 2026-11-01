from pathlib import Path
import json

root=Path(__file__).resolve().parent
report=json.loads((root/'second_validation.json').read_text(encoding='utf-8'))
assert report['claim_rows']==15
assert report['numerical_checks']=='passed'
path=root/'STATUS.md'
text=path.read_text(encoding='utf-8')
lines=text.splitlines()
assert lines[0]=='STATE: WORKING'
lines[0]='STATE: DONE'
for i,line in enumerate(lines):
    if line.startswith('NEXT:'):
        lines[i]='NEXT: A future attempt must prove an all-boundary-two-stars record/tree cover or the precise Gaussian-tilted mixed arm/diameter estimate; neither is established here.'
    if line.startswith('VERDICT:'):
        lines[i]='VERDICT: PARTIAL'
lines += ['', '2026-10-11 continuation: Serious second attempt completed. Two new approaches recorded and pursued: tree/full-contour records with exact deterministic countermodels, and quantitative tilted annular barriers. Exact source pages checked, all numerical diagnostics passed, and 15 claim records validated. No positive-gamma all-boundary-two-stars upper bound or target counterexample proved. Formal-check provenance is recorded separately in LEAN_CHECK.md. Remaining gaps are explicit in RECORD_REDUCTION.md, BARRIER_REDUCTION.md, and ATTEMPT.md.']
path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines[:3]))
