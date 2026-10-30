from pathlib import Path
import json, hashlib, datetime

r=Path(__file__).resolve().parents[1]
a=r.parents[1]
def read(p): return p.read_text(encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x): p.write_text(x,encoding='utf-8',newline='\n')
receipt=json.loads(read(r/'out/LOCAL_RECEIPT.json'))
assert all(sha(r/q['path'])==q['sha256'] for q in receipt['files'])
spec=json.loads(read(r/'out/PRE_MAIN_AMENDMENT.json'))
assert sha(r/'code/check.py')==spec['check_sha256']
assert sha(r/'code/arithmetic.py')==spec['arithmetic_sha256']
status=read(a/'STATUS.md')
assert len(status.splitlines())==2 and status.startswith('STATE:') and status.splitlines()[1].startswith('NEXT:')
report=read(r/'REPORT.md')
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
result={'status':'PASS','time_utc':now,'saved_receipt_hashes_checked':len(receipt['files']),'main_helper_pins':'MATCH','status_lines':2,'report_readback':'Universal bridge paragraph verified','compatibility_copy':'IDENTICAL','administrative_first_attempt':'Failed after successful report/helper readback: one-off Path(.) was relative so parents[1] raised IndexError. This script resolves its own absolute path. No mathematical computation or artifact was changed by that failed read-only command.'}
save(r/'out/READBACK.json',json.dumps(result,indent=2)+'\n')
save(a/'WORKLOG.md',read(a/'WORKLOG.md')+f'\n{now} Final local readback: initial read-only one-off used relative Path(.) and raised IndexError selecting agent parent, after confirming report tail and helper hashes. Corrected absolute-path readback passes saved hash receipt, both main helper pins, two-line STATUS and identical compatibility copy; no math rerun.\n')
receipt['time_utc']=now
receipt['readback']='PASS; see out/READBACK.json'
receipt['files']=[{'path':str(p.relative_to(r)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(r.rglob('*')) if p.is_file() and p.name!='LOCAL_RECEIPT.json']
assert all(q['bytes']<20_000_000 for q in receipt['files'])
receipt['rolling_files']=[{'path':str(a/n),'sha256':sha(a/n)} for n in ('STATUS.md','WORKLOG.md','LEARNED.md')]
save(r/'out/LOCAL_RECEIPT.json',json.dumps(receipt,indent=2)+'\n')
print(json.dumps(result))
