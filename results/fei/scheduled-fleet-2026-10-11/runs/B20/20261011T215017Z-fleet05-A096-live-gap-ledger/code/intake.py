from pathlib import Path
import json, hashlib, datetime
ROOT=Path(r'~\brain_workers\FEI100_20261011')
OWN=ROOT/'agents/A096'
RUN=OWN/'runs/20261011T215017Z-fleet05-A096-live-gap-ledger'
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
def read(p):
    raw=p.read_bytes()
    return raw.decode('utf-8-sig',errors='replace'), hashlib.sha256(raw).hexdigest()
sources=[]
for p in sorted(set(list(BASE.glob('*.json'))+list(BASE.glob('*.md'))+list(BASE.glob('*.tex'))+list(SUP.glob('*.md'))+list((SUP/'sources').glob('*.md'))+list((ROOT/'context').glob('*.txt')))):
    txt,sha=read(p)
    sources.append({'path':str(p),'sha256':sha,'bytes':p.stat().st_size,'headings':[x for x in txt.splitlines() if x.startswith('#')][:30]})
rows=[]
reports=list((BASE/'runs').rglob('REPORT.md'))+list((ROOT/'agents').glob('A*/runs/*/REPORT.md'))
for p in sorted(reports):
    if OWN in p.parents: continue
    txt,sha=read(p)
    files={}
    for name in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']:
        q=p.parent/name
        if q.exists():
            qt,qs=read(q); files[name]={'sha256':qs,'bytes':q.stat().st_size}
    claims=[]
    q=p.parent/'CLAIMS.json'
    if q.exists():
        obj=json.loads(read(q)[0]); cs=obj if isinstance(obj,list) else obj.get('claims',[])
        if not cs and isinstance(obj,dict) and 'claim_id' in obj: cs=[obj]
        claims=[{k:c.get(k) for k in ['claim_id','version','exact_statement','status','proof_dependencies','first_unproved_line','next_consumers']} for c in cs]
    row={'report':str(p),'report_sha256':sha,'report_bytes':len(txt.encode()),'files':files,'four_files_present':len(files)==4,'claims':claims,'headings':[x for x in txt.splitlines() if x.startswith('#')]}
    rows.append(row)
    print('\nSOURCE',str(p), '\n'+txt)
    print('CLAIMS',json.dumps(claims,ensure_ascii=False))
packets=json.loads((BASE/'PACKET_STATUS.json').read_text(encoding='utf-8-sig'))
registry=json.loads((BASE/'CLAIM_REGISTRY.json').read_text(encoding='utf-8-sig'))
obstructions=json.loads((BASE/'OBSTRUCTION_REGISTRY.json').read_text(encoding='utf-8-sig'))
ledger={'schema':'a096-source-bound-intake/1','snapshot_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'authority':'Local proposed adoption delta only; shared indices untouched.','sources':sources,'reports':rows,'canonical_claim_registry':registry,'canonical_obstruction_registry':obstructions,'canonical_packet_snapshot':packets,'missing_lead_notes':str(ROOT/'claude/B20/STREAM_NOTES.md'),'full_fei_status':'OPEN'}
(RUN/'out').mkdir(parents=True,exist_ok=True)
(RUN/'out/SOURCE_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False),encoding='utf-8')
print('TOTAL_REPORTS',len(rows))
