"""Incremental complete-report intake. Immutable prior receipts are inherited explicitly."""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[3];OUT=ROOT/'out'
OLD=ROOT.parents[1]/'runs/20261023T115236Z-fleet03-A096-live-gap-ledger/out'
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dump(n,x):(OUT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
start=time.perf_counter();reports=load(OLD/'COMPLETE_SAVED_REPORT_MAP.json');claims=load(OLD/'CLAIM_DEPENDENCY_COUNTEREXAMPLE_MAP.json');known={r['path'] for r in reports};new=0;newc=0;errors=[];receipts=[]
for i in range(1,101):
 home=BASE/'agents'/f'A{i:03d}'/'runs'
 if not home.is_dir():continue
 for folder in sorted(home.iterdir()):
  if folder==ROOT:continue
  p=folder/'REPORT.md'
  if str(p) in known:continue
  if not folder.is_dir() or not p.is_file():continue
  try:
   raw=p.read_bytes();text=raw.decode('utf-8-sig');complete=all((folder/n).is_file() for n in ('CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'))
   row={'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'full_report_read':True,'protocol_bundle':complete,'intake_run':ROOT.name};reports.append(row);new+=1
   cp=folder/'CLAIMS.json'
   if cp.is_file():
    rawc=cp.read_bytes();obj=json.loads(rawc.decode('utf-8-sig'));entries=obj if isinstance(obj,list) else obj.get('claims',[obj])
    for c in entries:
     if isinstance(c,dict):claims.append({'claim_source':str(cp),'claim_file_sha256':hashlib.sha256(rawc).hexdigest(),'report_sha256':row['sha256'],'full_report_read':True,'protocol_bundle':complete,**{k:c.get(k) for k in ('claim_id','version','statement_sha256','exact_statement','status','proof_dependencies','review_records','refutes','supersedes','first_unproved_line','next_consumers')}});newc+=1
  except Exception as e:errors.append({'path':str(p),'error':repr(e)})
required=[BASE/'BOARD.md',BASE/'claude/B20/STREAM_NOTES.md',ROOT.parents[1]/'STATUS.md',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
critical={'A050':'20261023T132645Z-fleet03-A050-repair-with-scope','A097':'20261023T121505Z-fleet03-A097-cross-route-transfer','A079':'20261023T130748Z-fleet03-A079-correlated-auxiliaries','A082':'20261023T121241Z-fleet03-A082-finite-inequalities'}
for a,r in critical.items():
 folder=BASE/'agents'/a/'runs'/r
 required+=list(folder.glob('*.md'))+list(folder.glob('*.json'))
for p in sorted(set(required)):
 try:
  raw=p.read_bytes();raw.decode('utf-8-sig');receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'full_text_read':True})
 except Exception as e:errors.append({'path':str(p),'error':repr(e)})
dump('COMPLETE_SAVED_REPORT_MAP.json',reports);dump('CLAIM_DEPENDENCY_COUNTEREXAMPLE_MAP.json',claims);dump('SOURCE_MANIFEST.json',receipts)
result={'baseline_run':OLD.parent.name,'baseline_reports':852,'baseline_claims':1527,'baseline_policy':'Prior immutable run receipts imported, not claimed re-read this stage; new reports fully read. No bulk re-opening of unchanged papers/old reports.','new_report_reads':new,'new_claim_records':newc,'report_count':len(reports),'protocol_bundles':sum(x['protocol_bundle'] for x in reports),'claim_records':len(claims),'packets':len({Path(x['path']).parents[2].name for x in reports}),'source_receipts':len(receipts),'read_errors':errors,'runtime_seconds':time.perf_counter()-start}
dump('INTAKE.json',result);print(json.dumps(result))
