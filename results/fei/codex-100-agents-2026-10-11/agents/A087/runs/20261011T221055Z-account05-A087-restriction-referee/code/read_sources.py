from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
REPORTS=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
paths=[REPORTS/p for p in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += sorted((REPORTS/'runs').rglob('*.md'))+sorted((REPORTS/'runs').rglob('CLAIMS.json'))
paths += [SUP/p for p in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+sorted((SUP/'sources').glob('*.md'))
paths += sorted((BASE/'context').glob('*.txt'))+[BASE/'BOARD.md',BASE/'claude/B18/STREAM_NOTES.md']
for a in list(range(21,31))+list(range(61,66)):
    d=BASE/'agents'/f'A{a:03}'
    paths += sorted(d.glob('STATUS.md'))+sorted(d.glob('LEARNED.md'))
    for name in ['REPORT.md','CLAIMS.json','*.tex','*SCOPE.md','SPEC_CORRECTIONS.md']:
        paths += sorted((d/'runs').rglob(name))
receipts=[]
ROOT.joinpath('out').mkdir(parents=True,exist_ok=True)
for p in dict.fromkeys(paths):
    if not p.exists():
        receipts.append({'path':str(p),'missing':True}); continue
    b=p.read_bytes(); s=b.decode('utf-8-sig',errors='replace')
    receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(s.splitlines()),'read_kind':'byte inventory; excerpts inspected separately'})
    if p.name in ['CAMPAIGN.md','NATIVE_MAPPING.md','SEED_LEMMAS.md','ERASURE_REDUCTION.md','ERASURE_RIGIDITY.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ONE_BIT_ENDPOINT.md']:
        print('\nSOURCE',p,'\n',s)
    elif p.name=='CLAIMS.json' and 'agents' in str(p):
        print('\nCLAIMS',p,'\n',s)
    elif p.name=='STATUS.md': print(p,s)
ROOT.joinpath('out/source_inventory.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print('INVENTORY',len(receipts))
