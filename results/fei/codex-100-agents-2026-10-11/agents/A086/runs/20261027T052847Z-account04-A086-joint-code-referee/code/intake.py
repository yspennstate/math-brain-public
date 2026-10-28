from pathlib import Path
import hashlib,json,os
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'out'; OUT.mkdir(exist_ok=True)
root=Path('~')
campaign=root/'mop_fei100/reports/fei-2026-10-11'
supp=root/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
context=root/'brain_workers/FEI100_20261011/context'
paths=[campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
paths+=list(campaign.glob('*.tex'))+[supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list((supp/'sources').glob('*.txt'))+list(context.glob('*.txt'))
paths+=[root/'.claude/compute/interventions.tsv',root/'<private-repo>/12_cognitive_architecture/scheduled_tasks/README.md']
records=[]
for p in paths:
    if not p.exists():
        records.append({'path':str(p),'missing':True});continue
    raw=p.read_bytes()
    try: s=raw.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=raw.decode('cp1252');enc='cp1252'
    records.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc,'lines':len(s.splitlines()),'intake':'whole decoded; targeted locators only; not independent full proof audit'})
    if p.suffix=='.json':json.loads(s)
(OUT/'INTAKE.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
state=json.loads((root/'.claude/brain_health/state.json').read_text(encoding='utf-8-sig'))
health={k:v for k,v in state.items() if k!='issues'}
(OUT/'WAKE_HEALTH.json').write_text(json.dumps(health,indent=2),encoding='utf-8')
print(json.dumps({'intake_files':len(records),'missing':[r['path'] for r in records if r.get('missing')],'health_keys':list(state),'thread':os.environ.get('CODEX_THREAD_ID'),'health_receipt':str(OUT/'WAKE_HEALTH.json')}))
