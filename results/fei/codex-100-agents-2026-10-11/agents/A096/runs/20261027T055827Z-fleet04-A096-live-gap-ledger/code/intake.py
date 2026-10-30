"""Incremental ledger intake; no source writes and no unchanged report rereads."""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT.parents[3]; OUT=ROOT/'out'
OLD=ROOT.parents[1]/'runs/20261023T140303Z-fleet03-A096-live-gap-ledger/out'
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dump(n,x):(OUT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
start=time.perf_counter(); reports=load(OLD/'COMPLETE_SAVED_REPORT_MAP.json'); claims=load(OLD/'CLAIM_DEPENDENCY_COUNTEREXAMPLE_MAP.json'); known={r['path'] for r in reports}; nr=nc=0; errors=[]
for i in range(1,101):
    home=BASE/'agents'/f'A{i:03d}'/'runs'
    if not home.is_dir():continue
    for folder in sorted(home.iterdir()):
        p=folder/'REPORT.md'
        if folder==ROOT or str(p) in known or not p.is_file():continue
        try:
            raw=p.read_bytes(); txt=raw.decode('utf-8-sig'); complete=all((folder/n).is_file() for n in ('CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'))
            row={'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'full_report_read':True,'protocol_bundle':complete,'intake_run':ROOT.name}; reports.append(row); nr+=1
            cp=folder/'CLAIMS.json'
            if cp.is_file():
                cr=cp.read_bytes(); obj=json.loads(cr.decode('utf-8-sig')); entries=obj if isinstance(obj,list) else obj.get('claims',[obj])
                for c in entries:
                    if isinstance(c,dict):
                        claims.append({'claim_source':str(cp),'claim_file_sha256':hashlib.sha256(cr).hexdigest(),'report_sha256':row['sha256'],'full_report_read':True,'protocol_bundle':complete,**{k:c.get(k) for k in ('claim_id','version','statement_sha256','exact_statement','status','proof_dependencies','review_records','refutes','supersedes','first_unproved_line','next_consumers')}}); nc+=1
        except Exception as e:errors.append({'path':str(p),'error':repr(e)})
receipts=[]
for agent,filenames in [('A050',['REPORT.md','PROOF.md','CLAIMS.json']),('A011',['REPORT.md','DERIVATION.md','CLAIMS.json']),('A094',['REPORT.md','CLAIMS.json']),('A097',['REPORT.md','PROOF.md','CLAIMS.json'])]:
    folder=sorted((BASE/'agents'/agent/'runs').iterdir())[-1]
    for name in filenames:
        p=folder/name; raw=p.read_bytes(); raw.decode('utf-8-sig');receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
dump('COMPLETE_SAVED_REPORT_MAP.json',reports);dump('CLAIM_DEPENDENCY_COUNTEREXAMPLE_MAP.json',claims);dump('SOURCE_RECEIPTS.json',receipts)
result={'baseline':str(OLD),'baseline_reports':len(reports)-nr,'baseline_claims':len(claims)-nc,'new_reports_read':nr,'new_claim_records':nc,'reports':len(reports),'claims':len(claims),'complete_bundles':sum(r['protocol_bundle'] for r in reports),'read_errors':errors,'seconds':time.perf_counter()-start,'interpretation':'Complete texts decoded and indexed, not independent mathematical acceptance. Prior immutable receipts inherited explicitly.'}
dump('INTAKE.json',result); print(json.dumps(result))
