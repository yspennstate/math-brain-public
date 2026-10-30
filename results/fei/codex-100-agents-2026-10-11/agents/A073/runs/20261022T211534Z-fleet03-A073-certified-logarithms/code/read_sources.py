from pathlib import Path
import hashlib, json, sys
root=Path('~')
campaign=root/'mop_fei100/reports/fei-2026-10-11'
supp=root/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
worker=root/'brain_workers/FEI100_20261011'
run=Path(__file__).resolve().parents[1]
out=run/'out'; out.mkdir(exist_ok=True)
sys.stdout=(out/'READS.log').open('w',encoding='utf-8')
sources=[]
paths=[campaign/x for x in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md'))
paths += list((worker/'context').glob('*.txt'))
paths += list((worker/'agents/A073/runs').glob('*/REPORT.md'))
paths += list((campaign/'runs/B15').glob('*/REPORT.md'))
for path in paths:
    if not path.is_file():
        print('MISSING',path); continue
    data=path.read_bytes()
    try:
        body=data.decode('utf-8-sig'); encoding='utf-8-sig'
    except UnicodeDecodeError:
        body=data.decode('cp1252'); encoding='cp1252-explicit-legacy'
    sources.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'encoding':encoding})
    (out/'source_read_manifest.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
    print('\nSOURCE',path.name,'bytes',len(data))
    if path.suffix=='.json':
        obj=json.loads(body)
        def walk(obj):
            if isinstance(obj,dict):
                if any(x in json.dumps(obj,ensure_ascii=False) for x in ['A073','C018','C019','C024','G-R-MISMATCH']):
                    for k,v in obj.items():
                        if isinstance(v,(dict,list)): walk(v)
                        elif any(x in str(v) for x in ['A073','C018','C019','C024','G-R-MISMATCH']): print(k,str(v)[:1400])
            elif isinstance(obj,list):
                for v in obj: walk(v)
        walk(obj)
    else:
        hits=[line for line in body.splitlines() if any(s in line.lower() for s in ['conditional','relative entropy','reset','universal bridge','first unsupported','first unproved','full fei','theorem 8','thm:shared'])]
        print('\n'.join(hits[:14]))
(out/'source_read_manifest.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
sys.stdout.close()
print('Source reads saved:',len(sources),file=sys.__stdout__)
