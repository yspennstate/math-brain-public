from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; OUT.mkdir(exist_ok=True)
AGENT=RUN.parent.parent; ROOT=AGENT.parent.parent
PREV=AGENT/'runs/20261013T213917Z-account05-A100-release-and-continuation-ledger'
CAN=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def save(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def read(p): return p.read_text(encoding='utf-8-sig')
receipts=[]
for p,name in [(ROOT/'BOARD.md','BOARD_SNAPSHOT.md'),(ROOT/'claude/B20/STREAM_NOTES.md','B20_NOTES_SNAPSHOT.md'),(AGENT/'STATUS.md','PRE_STAGE_STATUS.md'),(CAN/'EXECUTION_PROTOCOL.json','EXECUTION_PROTOCOL_SNAPSHOT.json')]:
    b=p.read_bytes(); receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    (OUT/name).write_bytes(b)
previous=json.loads(read(PREV/'out/CLAIM_CENSUS.json'))
old={x['source']:x for x in previous}; census=[]; changes=[]; errors=[]
roots=list((ROOT/'agents').glob('A*/runs/*/CLAIMS.json'))+list((ROOT/'claude').glob('B*/runs/*/CLAIMS.json'))+[CAN/'CLAIM_REGISTRY.json']
for p in sorted(roots):
    if p.parent==RUN: continue
    b=p.read_bytes()
    try:
        obj=json.loads(b.decode('utf-8-sig'))
        records=obj if isinstance(obj,list) else obj.get('claims',[])
        if not isinstance(records,list): raise ValueError('claims not a list')
        for c in records:
            if not isinstance(c,dict) or 'claim_id' not in c: continue
            census.append({'source':str(p),'record':c,'statement_only_sha256':hashlib.sha256(c.get('exact_statement','').encode()).hexdigest()})
        # Compare bytes with the previous source receipt, avoiding claims-list overwrites.
        receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    except Exception as e: errors.append({'source':str(p),'error':str(e)})
old_hash={x['path']:x['sha256'] for x in json.loads(read(PREV/'out/SOURCE_RECEIPTS.json'))['files']}
for row in receipts:
    if row['path'].endswith('CLAIMS.json') and old_hash.get(row['path'])!=row['sha256']:
        changes.append({'source':row['path'],'change':'NEW' if row['path'] not in old_hash else 'CHANGED','sha256':row['sha256']})
save(OUT/'CLAIM_CENSUS.json',census); save(OUT/'NEW_OR_CHANGED_CLAIM_SOURCES.json',changes); save(OUT/'PARSE_FAILURES.json',errors)
save(OUT/'SOURCE_RECEIPTS.json',{'snapshot_utc':datetime.now(timezone.utc).isoformat(),'files':receipts})
save(RUN/'FROZEN_SPEC.json',{'helper':'A100-stage3-source-intake-v1','family':'no Boolean search; source-version census','domain':'existing root CLAIMS.json under A*/runs and B*/runs, excludes current run','case_count':'one finite snapshot; discovered count reported','symmetry':'none','arithmetic':'byte hashes and JSON exact text','memory_estimate_MB':40,'max_runtime_seconds':60,'automatic_dimension_escalation':False})
print(json.dumps({'claim_records':len(census),'new_or_changed_sources':len(changes),'parse_failures':len(errors)},indent=2),flush=True)
for a in ['A066','A073','A081','A090','A094','A096','A097','A098','A099']:
    print(a,[p.parent.name for p in roots if p.parent.parent.parent.name==a][-3:],flush=True)
