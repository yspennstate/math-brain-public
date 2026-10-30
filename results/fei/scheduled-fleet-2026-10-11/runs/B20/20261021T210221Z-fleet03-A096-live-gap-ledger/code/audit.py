from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(raw):return hashlib.sha256(raw).hexdigest()
receipts=load(R/'out/PERSISTENCE_RECEIPTS.json')
for x in receipts['artifacts']:
    p=R/x['path'];raw=p.read_bytes();assert len(raw)==x['bytes'] and sha(raw)==x['sha256'],p
source_by_path={x['path']:x for x in load(R/'out/SOURCE_MANIFEST.json')}
p=R/'out/COMPLETE_SAVED_REPORT_MAP.json';mapping=load(p);changed=0
for row in mapping['reports']:
    actual=source_by_path[row['source']]['sha256']
    prior=row.get('decoded_text_sha256',row['sha256'])
    changed+=int(prior!=actual)
    row['decoded_text_sha256']=prior;row['sha256']=actual
p.write_text(json.dumps(mapping,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
report=(R/'REPORT.md').read_text(encoding='utf-8')
claims=load(R/'CLAIMS.json');progress=load(R/'PROGRESS.json')
assert claims[0]['statement_sha256']==sha(claims[0]['exact_statement'].encode('utf-8'))
assert progress==load(R/'PACKET_DELTA.json')
assert '861691' in report and '1548' in report and 'rate18' in report
assert 'Universal bridge' in report and 'full FEI remains OPEN' in report
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
new=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        raw=p.read_bytes();assert len(raw)<20_000_000
        new.append({'path':str(p.relative_to(R)),'bytes':len(raw),'sha256':sha(raw)})
receipts['artifacts']=new;receipts['postsave_independent_audit']='PASS; prior receipt bytes rechecked, report/claim fidelity checked, raw source hash distinguished from decoded text hash'
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'POSTSAVE_AUDIT_PASS','source_reports':len(mapping['reports']),'byte_vs_decoded_hash_differences_explicitly_labelled':changed,'artifacts':len(new),'status_file':(A/'STATUS.md').read_text(encoding='utf-8').strip()}))
print(report[:1050])
print(report[report.index('## Universal bridge'):])
