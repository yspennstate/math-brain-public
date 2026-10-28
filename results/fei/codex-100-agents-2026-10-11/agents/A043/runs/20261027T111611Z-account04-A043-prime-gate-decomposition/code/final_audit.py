from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];out=R/'out'
def h(b):return hashlib.sha256(b).hexdigest()
# Precise terminology: Jhi need not be lower semicontinuous.
p=R/'code/finalize.py';s=p.read_text(encoding='utf-8');s=s.replace('lower-semicontinuity guard','lower-limit bound');p.write_text(s,encoding='utf-8')
p=R/'CLAIMS.json';claims=json.loads(p.read_text(encoding='utf-8'))
for c in claims:
 c['exact_statement']=c['exact_statement'].replace('lower-semicontinuity guard','lower-limit bound')
 c['statement_sha256']=h(c['exact_statement'].encode('utf-8'))
p.write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert 'Full FEI remains OPEN' in report and '1591 assertions' in report and '595 assertions' in report
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((R.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert json.loads((out/'exact_results.json').read_text(encoding='utf-8'))['status']=='PASS'
assert json.loads((out/'review_results.json').read_text(encoding='utf-8'))['status']=='PASS'
for c in claims:assert c['statement_sha256']==h(c['exact_statement'].encode('utf-8'))
proof=(R/'PROOF.md').read_text(encoding='utf-8')
for phrase in ['n+2','fixed n','B={z,x_i}','7/16','TOGETHER WITH all essential binary gates']:
 assert phrase in proof,phrase
manifest=json.loads((out/'persistence_receipts.json').read_text(encoding='utf-8'))
for row in manifest['files']:
 p=R/row['path'];assert p.exists()
 if p.name not in ('finalize.py','CLAIMS.json'):assert h(p.read_bytes())==row['sha256'],str(p)
audit={'status':'PASS','full_fei':'OPEN','source_review':'HOLDS_SCOPED','completion':'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW','lean':'RUNTIME_UNVERIFIED','main_assertions':1591,'review_assertions':595,'checks':['scope and binary base included','all four block cases','fixed-dimensional finite limit','actual dyadic-jump control and retained rare atoms','dummy-core and m=2 source negative controls','exact statement hashes','unchanged artifact hashes','packet identity','two-line rolling status']}
(out/'final_audit.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
manifest['files']=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='persistence_receipts.json':
  b=p.read_bytes();assert len(b)<20_000_000
  manifest['files'].append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':h(b)})
(out/'persistence_receipts.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','files':len(manifest['files']),'claims':len(claims),'main':1591,'review':595}))
print(report)
