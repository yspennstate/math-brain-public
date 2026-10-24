"""Targeted later-intake lookup; no store exports, tests, or bank material."""
import json
from pathlib import Path
import re

root=Path('~/<private-repo>/06_math_research')
patterns={
 'P0289':r'Ross.s second|modulation.*workload',
 'C0035':r'trigonometric.polynomial.*block|block.factor.*determinantal',
 'P0001':r'negative.correlation.*uniform.forest|uniform.forest.*negative',
 'P0133':r'torus.*homotopy|homotopy.*torus',
 'C0002':r'fluctuations.*intermediate.level|intermediate.level.*deviation',
 'C0059':r'dual.*Boltzmann.*transien|transien.*dual.*Boltzmann',
 'C0083':r'critical.value.*Hamming|Hamming.*expansion',
 'C0128':r'zero.one.*excited|excited.*zero.one',
 'P0015':r'phase.retrieval.*4M|4M.*5.*measurement',
 'P0044':r'invariant.*coupling.*(?:wired|spanning.forest)',
}
found=[]
files=0
for folder in sorted(root.glob('probability_1000_intake_*')):
    if folder.name=='probability_1000_intake_claude_20260907':
        continue
    for name in ['problems.jsonl','attempts.jsonl']:
        path=folder/name
        if not path.exists():
            continue
        files+=1
        with path.open(encoding='utf-8-sig') as handle:
            for number,line in enumerate(handle,1):
                row=json.loads(line)
                text=' '.join(str(row.get(k,'')) for k in ['title','statement','result','key_identity'])
                hits=[p for p,pattern in patterns.items() if re.search(pattern,text,re.I)]
                if hits:
                    record={'matches':hits,'path':str(path),'line':number,'row':row}
                    found.append(record)
                    print(json.dumps({'matches':hits,'problem_id':row.get('problem_id'),'status':row.get('current_status',row.get('verification')),'title':row.get('title'),'source_id':row.get('source_id')},ensure_ascii=False))
receipt={'command':'python -X utf8 status_scan.py','ledger_files_scanned':files,'matched_rows':len(found),'matches':found,'limit':'A negative local lookup is not a current global literature-status certificate.'}
target=Path(__file__).resolve().parent/'later_status_scan.json'
target.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'ledger_files_scanned':files,'matched_rows':len(found)}))
