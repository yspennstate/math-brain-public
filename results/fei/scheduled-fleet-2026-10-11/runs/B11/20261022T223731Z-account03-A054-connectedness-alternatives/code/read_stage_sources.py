from pathlib import Path
import json, hashlib, re
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(parents=True,exist_ok=True)
B=Path('~/mop_fei100/reports/fei-2026-10-11')
S=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
C=Path('~/brain_workers/FEI100_20261011/context')
paths=[B/x for x in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','EXECUTION_PROTOCOL.json','FEI_100_agent_research_plan.tex']]
paths += [S/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((S/'sources').glob('*.md'))+list(C.glob('*.txt'))
paths += [R.parents[1]/'runs/20261014T055856Z-account05-A054-connectedness-alternatives'/x for x in ['OVERLAP_PAYMENT.md','CLAIMS.json']]
records=[]; excerpts=[]
for p in paths:
    if not p.exists():
        records.append({'path':str(p),'missing':True});continue
    b=p.read_bytes()
    try:s=b.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:s=b.decode('cp1252');enc='cp1252 (source bytes are not valid UTF-8)'
    lines=s.splitlines()
    records.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(lines),'encoding':enc})
    keys=['A054','B11','component','critical','terminal','proper block','shared-data','shared data','physical restriction']
    hits=[(i+1,l[:350]) for i,l in enumerate(lines) if any(k.lower() in l.lower() for k in keys)]
    excerpts.append({'path':str(p),'hits':hits[:22]})
(R/'out/SOURCE_MANIFEST.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
(R/'out/SOURCE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2),encoding='utf-8')
print(json.dumps({'sources':len(records),'missing':[r['path'] for r in records if r.get('missing')],'relevant':excerpts[:13]},indent=2)[:18000])
