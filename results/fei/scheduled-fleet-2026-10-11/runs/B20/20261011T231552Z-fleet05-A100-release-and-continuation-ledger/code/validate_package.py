from pathlib import Path
import json, hashlib
from datetime import datetime, timezone
RUN=Path(__file__).resolve().parents[1]; AGENT=RUN.parent.parent
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))['required_per_run']
checks=[]
def check(name,ok):
    checks.append({'check':name,'pass':bool(ok)})
    assert ok,name
claims=json.loads((RUN/'CLAIMS.json').read_text(encoding='utf-8'))
for c in claims:
    check('claim_fields '+c['claim_id'],set(c)==set(protocol['claim_fields']))
    check('statement sha256',hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256'])
p=json.loads((RUN/'PROGRESS.json').read_text(encoding='utf-8'))
fields=[x.split(' (')[0] for x in protocol['progress_fields']]
check('progress exact fields',set(p)==set(fields))
check('primary packet',p['packet_id']=='A100' and p['packet_ids']==['A100'])
check('compatibility copy',(RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes())
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['report_fields']: check('report '+field,'## '+field in report)
check('universal bridge final paragraph',report.rstrip().split('\n\n')[-1].startswith('Universal bridge:'))
check('ten questions',len(json.loads((RUN/'out'/'NEXT_TEN_QUESTIONS.json').read_text(encoding='utf-8')))==10)
check('two line STATUS',len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2)
check('62 exact assertions',json.loads((RUN/'out'/'TAX_TREE_CHECK.json').read_text())['assertions_passed']==62)
check('zero forced status changes',json.loads((RUN/'out'/'CORRECTION_DELTA.json').read_text(encoding='utf-8'))['status_changes_required_by_two_corrections']==[])
files=[]
for path in sorted(RUN.rglob('*')):
    if not path.is_file() or path.name in ['PERSISTENCE_RECEIPTS.json','PACKAGE_VALIDATION.json']: continue
    b=path.read_bytes(); check('size cap '+str(path.relative_to(RUN)),len(b)<20_000_000)
    if path.suffix=='.json': json.loads(b.decode('utf-8-sig'))
    files.append({'path':str(path.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
receipts={'observed_utc':datetime.now(timezone.utc).isoformat(),'local_files':files,'remote_copy_verified':False,'public_release_performed':False,'self_exclusion':['out/PERSISTENCE_RECEIPTS.json','out/PACKAGE_VALIDATION.json']}
(RUN/'out'/'PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
for entry in files:
    check('readback '+entry['path'],hashlib.sha256((RUN/entry['path']).read_bytes()).hexdigest()==entry['sha256'])
out={'checks':checks,'passed':len(checks),'failed':0,'local_files_verified':len(files),'meaning':'Artifact schema/byte integrity only, not mathematical theorem acceptance.'}
(RUN/'out'/'PACKAGE_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
