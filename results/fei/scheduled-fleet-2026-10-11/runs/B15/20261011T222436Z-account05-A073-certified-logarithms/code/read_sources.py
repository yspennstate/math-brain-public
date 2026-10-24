from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
BASE=Path(r'~\mop_fei100')
REPORT=BASE/'reports/fei-2026-10-11'
SUP=BASE/'research_pushes/2026-10-11-full-fei-100-agents'
CTX=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[REPORT/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths+=list(REPORT.joinpath('runs').rglob('REPORT.md'))
paths+=[SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list(SUP.joinpath('sources').glob('*'))+list(CTX.glob('*.txt'))
receipts=[]
for p in paths:
    if not p.is_file():continue
    raw=p.read_bytes(); txt=raw.decode('utf-8-sig',errors='replace')
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'scope':'Full byte ingestion; selected context locators printed, no complete manuscript reconstruction claimed'})
    if p.suffix=='.json':
        data=json.loads(txt)
        if p.name=='PACKET_STATUS.json':
            print('PACKET_STATUS keys',list(data)); print('A073 occurrences',txt.count('A073'))
        elif p.name in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','STREAM_NEXT_ACTIONS.json']:
            print('\nINDEX',p.name);print(txt)
    elif p.parent==CTX:
        lines=txt.splitlines(); print('\nPAPER',p.name,'lines',len(lines));print('\n'.join(lines[:65]))
        hits=[i for i,l in enumerate(lines) if re.search(r'Proposition 7\.1|Proposition 8\.1|Theorem 1\.1|orthonormal|product bias|entropy in bits',l,re.I)]
        for i in hits[:5]:print('\n'.join(lines[max(0,i-2):i+10]))
    elif p.parent.name=='sources' and ('BLOCK_RESTRICTION' in p.name or 'LOG_ALLOCATION' in p.name): print('\nSOURCE',p.name,txt)
    elif p.parent.parent.parent.name=='runs':print('\nEARLIER',p,txt)
(ROOT/'out').mkdir(parents=True,exist_ok=True)
(ROOT/'out/source_receipts.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print('Saved source receipts',len(receipts))
