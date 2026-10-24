from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100')
camp=base/'reports/fei-2026-10-11'
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
paths=[camp/name for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/name for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*'))
paths += list((camp/'runs').glob('**/REPORT.md'))
paths += list(Path('~/brain_workers/FEI100_20261011/context').glob('*.txt'))
paths += [Path('~/brain_workers/FEI100_20261011/BOARD.md')]
records=[]
for p in paths:
    if not p.is_file(): continue
    b=p.read_bytes(); s=b.decode('utf-8-sig',errors='replace')
    records.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'scope':'loaded completely; relevant passage inspection separately recorded'})
    if p.name=='PACKET_STATUS.json':
        print(json.dumps([x for x in json.loads(s)['packets'] if x['packet_id']=='A033'],indent=2))
    if p.name=='STREAM_NEXT_ACTIONS.json':
        print(json.dumps([x for x in json.loads(s)['streams'] if x['native_stream']=='B07'],indent=2))
(R/'out').mkdir(exist_ok=True)
(R/'out/SOURCE_MANIFEST.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print('Loaded',len(records),'sources; manifest saved.')
