from pathlib import Path
import hashlib,json,re
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
TEAM=Path(r'~\brain_workers\FEI100_20261011')
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
files=[BASE/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += list((BASE/'runs').rglob('REPORT.md'))
files += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((SUP/'sources').glob('*.md'))+list((TEAM/'context').glob('*.txt'))+[TEAM/'BOARD.md']
files += [BASE/'source_material/reductions/paper/forests.tex',SUP/'baseline/current-threshold-paper.tex']
inventory=[]
for i in range(1,16):
    reports=list((TEAM/'agents'/f'A{i:03}').rglob('REPORT.md'))
    inventory.append({'packet_id':f'A{i:03}','reports':[str(p) for p in reports], 'availability':'PRESENT' if reports else 'NO_REPORT_AT_INTAKE'})
    for p in reports:
        files += [p]+list(p.parent.glob('*.tex'))+list(p.parent.glob('CLAIMS.json'))
manifest=[]; chunks=[]
for p in files:
    raw=p.read_bytes()
    try: t=raw.decode('utf-8-sig'); encoding='utf-8-sig'
    except UnicodeDecodeError: t=raw.decode('cp1252'); encoding='cp1252'
    manifest.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding})
    if p.parent==TEAM/'context':
        pats=['5.6.', 'A bound retaining', '2. Abstract', '2. Spatial', '2. A spatial', 'Theorem 1.1', 'Theorem 1.2']
        for pat in pats:
            k=t.find(pat)
            if k>=0: chunks.append('\nSOURCE '+str(p)+' LOCATOR '+pat+'\n'+t[max(0,k-150):k+6000])
    elif p.suffix=='.json' and p.name in ['PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']:
        obj=json.loads(t)
        def walk(x):
            if isinstance(x,dict):
                if x.get('packet_id') in [f'A{i:03}' for i in range(1,16)]+['A086'] or x.get('native_stream')=='B18': chunks.append(json.dumps(x,indent=2))
                else:
                    for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(obj)
(OUT/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(OUT/'CHAIN_INVENTORY.json').write_text(json.dumps(inventory,indent=2),encoding='utf-8')
(OUT/'INTAKE_EXCERPTS.txt').write_text('\n'.join(chunks),encoding='utf-8')
print('Source manifest:',len(manifest),'files. Chain:',[(x['packet_id'],x['availability']) for x in inventory])
print('\n'.join(chunks)[:40000])
