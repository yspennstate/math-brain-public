from pathlib import Path
import json, hashlib, re
root=Path(r'math-open-problems/reports\fei-2026-10-11')
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
paths=list(root.glob('*.md'))+list(root.glob('*.json'))+[root/'FEI_100_agent_research_plan.tex']+list((root/'runs').rglob('REPORT.md'))+list(supp.glob('*.md'))+list((supp/'sources').rglob('*.md'))+list((supp/'sources').rglob('*.txt'))+list(Path(r'context').glob('*.txt'))
receipt=[]
for p in paths:
    raw=p.read_bytes(); s=raw.decode('utf-8-sig',errors='replace'); lines=s.splitlines()
    receipt.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'lines':len(lines)})
    if p.name=='AGENT_ASSIGNMENTS.json':
        d=json.loads(s)
        def walk(x):
            if isinstance(x,dict):
                if x.get('packet_id')=='A058' or x.get('agent_id')=='A058': print('A058 CONTRACT',json.dumps(x))
                else:
                    for v in x.values():walk(v)
            elif isinstance(x,list):
                for v in x:walk(v)
        walk(d)
    if p.suffix in ['.tex','.txt'] or p.name=='REPORT.md':
        hits=[i for i,l in enumerate(lines) if re.search(r'composition|collision|shared.data|overlap|C024|C018|A058|B12',l,re.I)]
        print('\nSOURCE',p,'LINES',len(lines),'MATCHES',len(hits))
        for i in hits[:18]: print(str(i+1)+': '+' '.join(lines[max(0,i-1):i+4]))
Path('source_receipts.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('RECEIPTS',len(receipt))
