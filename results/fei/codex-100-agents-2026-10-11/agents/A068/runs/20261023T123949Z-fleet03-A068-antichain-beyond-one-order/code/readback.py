from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
j=json.loads((R/'out'/'RECEIPTS.json').read_text(encoding='utf-8')); checks=0
for item in j['files']:
 p=R/item['path']; assert sha(p)==item['sha256']; assert p.stat().st_size==item['bytes']; checks+=2
for item in j['rolling']:assert sha(Path(item['path']))==item['sha256']; checks+=1
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes();checks+=1
c=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']==j['statement_sha256']; checks+=1
s=(R/'REPORT.md').read_text(encoding='utf-8')
assert s.rstrip().split('\n\n')[-2]=='## Universal bridge'; checks+=1

assert 'total source mass there exactly1' in s; checks+=1
assert '164914' in s and '195' in s and 'FULL_FEI_OPEN' in (R/'PROGRESS.json').read_text(encoding='utf-8');checks+=1
out={'status':'PASS','checks':checks,'report_sha256':sha(R/'REPORT.md'),'receipt_sha256':sha(R/'out'/'RECEIPTS.json'),'full_fei':'OPEN','independent_agent_review':'PENDING','mirror':'UNVERIFIED'}
(R/'out'/'FINAL_READBACK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
