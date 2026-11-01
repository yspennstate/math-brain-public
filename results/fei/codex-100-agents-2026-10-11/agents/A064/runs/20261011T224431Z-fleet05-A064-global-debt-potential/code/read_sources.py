from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
P=Path(r'~\mop_fei100\reports\fei-2026-10-11')
S=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
C=Path(r'~\brain_workers\FEI100_20261011\context')
files=[P/x for x in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
files += [S/x for x in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
files += list((S/'sources').glob('*.md'))+list(C.glob('*.txt'))+list((P/'runs').rglob('REPORT.md'))
receipts=[]
for p in files:
    raw=p.read_bytes(); t=raw.decode('utf-8-sig',errors='replace')
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'scope':'Loaded whole text for navigation; only selected mathematical passages reconstructed'})
    if p.parent==C:
        lines=t.splitlines(); print('\nPAPER',p.name)
        print('\n'.join(lines[:32]))
        indexes=[i for i,l in enumerate(lines) if re.search(r'(Proposition 8\.9|Corollary 8\.10|Proposition 7\.1|Theorem 3\.1|Theorem 3\.2)',l)]
        if not indexes: indexes=[i for i,l in enumerate(lines) if 'activation' in l.lower()][:2]
        for i in indexes[:4]:
            print('LOCATOR',i+1); print('\n'.join(lines[max(0,i-3):i+35]))
    if p.name=='FEI_100_agent_research_plan.tex':
        lines=t.splitlines()
        for i,l in enumerate(lines):
            if 'A064' in l: print('PLAN',i+1,'\n'.join(lines[max(0,i-2):i+5]))
j=json.loads((P/'PACKET_STATUS.json').read_text(encoding='utf-8-sig'))
def walk(x):
    if isinstance(x,dict):
        if x.get('packet_id')=='A064': print('PACKET',json.dumps(x))
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(j)
(R/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
