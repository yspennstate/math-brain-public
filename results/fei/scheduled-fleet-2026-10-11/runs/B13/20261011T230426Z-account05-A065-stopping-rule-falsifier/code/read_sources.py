from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
paths=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths+=[supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list((supp/'sources').glob('*.md'))+list((base/'runs').rglob('REPORT.md'))
paths += list(Path(r'~\brain_workers\FEI100_20261011\context').glob('*.txt'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B13\STREAM_NOTES.md')]
paths+=list(Path(r'~\brain_workers\FEI100_20261011\agents\A064').rglob('REPORT.md'))
rows=[]
for p in paths:
    raw=p.read_bytes()
    try:s=raw.decode('utf-8'); enc='utf-8'
    except UnicodeDecodeError:s=raw.decode('cp1252');enc='cp1252'
    rows.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc,'scope':'whole-file loaded; selected relevant mathematical passages inspected, not an audit of every theorem'})
    if p.name=='PACKET_STATUS.json':
        d=json.loads(s); print('A065 contract',json.dumps([q for q in d['packets'] if q['packet_id']=='A065'],indent=2))
    if p.name=='FEI_100_agent_research_plan.tex':
        a=s.find('A065'); print('PLAN A065',s[max(0,a-700):a+1700])
    if p.parent.name=='sources' and p.name in ['BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ERASURE_REDUCTION.md','LOG_ALLOCATION_CURATED.md']:
        print('SOURCE',p.name,s[:10500])
(ROOT/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print('SOURCE RECEIPTS',len(rows))
