from pathlib import Path
import hashlib,json
base=Path(r'~\mop_fei100')
report=base/'reports/fei-2026-10-11'
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
ctx=Path(r'~\brain_workers\FEI100_20261011\context')
run=Path(__file__).resolve().parents[1]
paths=[report/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md')) + list(ctx.glob('*.txt'))
paths += list((report/'runs').rglob('REPORT.md'))
receipts=[]
for p in paths:
    data=p.read_bytes()
    try:txt=data.decode('utf-8-sig')
    except UnicodeDecodeError:txt=data.decode('cp1252')
    receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'scope':'read by source loader; only targeted excerpts inspected in assistant context'})
    if p.parent==ctx:
        lines=txt.splitlines()
        selected=[]
        for i,l in enumerate(lines):
            if any(w in l.lower() for w in ['proposition 7.1','proposition 8.', 'rare activation','two-coordinate identity','lemma 6.1','exact composition','point-defect','point flip']):
                selected.append((i+1,'\n'.join(lines[max(0,i-2):i+16])))
        print(p.name, json.dumps(selected[:10],ensure_ascii=False))
    if p.name=='PACKET_STATUS.json':
        obj=json.loads(txt)
        print('PACKET A022',json.dumps([x for x in obj['packets'] if x['packet_id']=='A022']))
(run/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print('sources loaded',len(receipts))
