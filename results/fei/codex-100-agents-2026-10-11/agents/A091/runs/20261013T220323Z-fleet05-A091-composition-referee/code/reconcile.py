from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];BASE=A.parents[1]
def rd(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def wr(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
folder=BASE/'agents/A058/runs/20261012T020138Z-fleet05-A058-overlapping-compositions'
claims=rd(R/'CLAIMS.json');src=next(c for c in rd(folder/'CLAIMS.json') if c['claim_id']==claims[0]['claim_id'])
assert src['statement_sha256']==claims[0]['statement_sha256']
claims[0]['review_records']=src['review_records']+claims[0]['review_records'];wr(R/'CLAIMS.json',claims)
receipts=rd(R/'out/SOURCE_RECEIPTS.json')
for file in ['REPORT.md','REVIEW_A057.md','CLAIMS.json']:
    p=folder/file;receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'scope':'Prior scoped cap acceptance and separate shared-variable contraction; consumed at final board reconciliation'})
wr(R/'out/SOURCE_RECEIPTS.json',receipts)
p=rd(R/'PROGRESS.json');p['mathematical_delta']=p['mathematical_delta'].replace('A057 capped fresh-activation bank v1 independently accepted','Second independent reconstruction of A057 capped fresh-activation bank v1 accepted, preserving A058 prior scoped review')
p['claims_created_or_changed'][0]['change']='Preserved A058 prior acceptance and appended independent A091 review; no statement/hash/author change'
p['claim_versions_used'].append({'claim_id':src['claim_id'],'version':1,'source':'A058 REVIEW_A057.md','scope':'Prior independent acceptance retained; this stage is a second reconstruction'})
wr(R/'PROGRESS.json',p);wr(R/'PACKET_DELTA.json',p)
with (R/'out/INTAKE.md').open('a',encoding='utf-8') as f:f.write('\nFinal board reconciliation: A058 had already accepted A057 cap v1. Its REPORT, REVIEW_A057 and CLAIMS were consumed; this run supplies the second independent reconstruction, not the first acceptance. A058 contraction work is distinct from the physical shared-control priority tree here.\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Final reconciliation: preserved A058 prior cap acceptance and relabeled this as a second independent review. A058 physical-contraction scope differs from the priority tree. Initial final readback passed all artifact hashes but used a relative-path STATUS parent index and raised IndexError; STATUS was read successfully by its explicit agent path, with no mathematical check affected.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nProvenance correction: A058 already accepted A057 capped bank before this stage; A091 supplies a second requested reconstruction. A058 identifies shared variables by contraction, which is distinct from an ancestry-valid physical query and cannot be assigned its influence telescope.\n')
receipt=rd(R/'out/RECEIPTS.json');receipt['final_reconciliation']='A058 prior independent cap acceptance preserved; second-review labeling corrected; final artifact hash readback passes.'
receipt['files']=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(R.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='RECEIPTS.json']
wr(R/'out/RECEIPTS.json',receipt)
for row in receipt['files']:assert sha(R/row['path'])==row['sha256']
assert rd(R/'PROGRESS.json')==rd(R/'PACKET_DELTA.json')
assert len((A/'STATUS.md').read_text().splitlines())==2
print(json.dumps({'status':'PASS','final_readback_files':len(receipt['files']),'preserved_independent_reviews':len(claims[0]['review_records'])}))
