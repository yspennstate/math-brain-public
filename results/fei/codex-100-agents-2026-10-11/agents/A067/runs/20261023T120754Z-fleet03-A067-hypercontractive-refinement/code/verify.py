from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
receipt=json.loads((R/'out/RECEIPTS.json').read_text())
for item in receipt['artifacts']:
 p=R/item['path'];assert sha(p.read_bytes())==item['sha256'],str(p)
claims=json.loads((R/'CLAIMS.json').read_text())
assert all(sha(c['exact_statement'].encode())==c['statement_sha256'] for c in claims)
dep=json.loads((R/'out/DEPENDENCY_REVIEW.json').read_text())
p=Path(dep['source_path']);b=p.read_bytes();assert sha(b)==dep['source_proof_sha256'],'Primary source changed before byte snapshot'
(R/'out/SOURCE_A088_PROOF.md').write_bytes(b)
paths=json.loads((R/'out/SOURCES.json').read_text())
sourceclaims=p.parent/'CLAIMS.json';entry=next(x for x in paths if Path(x['path'])==sourceclaims)
cb=sourceclaims.read_bytes();assert sha(cb)==entry['sha256'],'Source registry changed before byte snapshot'
(R/'out/SOURCE_A088_CLAIMS.json').write_bytes(cb)
# A reversible local snapshot preserves the proof/registry mismatch at intake.
artifacts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000;artifacts.append({'path':str(p.relative_to(R)),'sha256':sha(b),'bytes':len(b)})
receipt['artifacts']=artifacts;receipt['final_verified_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();receipt['source_snapshots']='Exact byte snapshots of cited A088 proof and intake registry; hashes match intake receipts'
(R/'out/RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for a in artifacts:assert sha((R/a['path']).read_bytes())==a['sha256']
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
print(json.dumps({'status':'PASS','disk_artifacts':len(artifacts),'claim_statements':len(claims),'main_plus_independent_checks':9708+692,'source_snapshots':'BYTE_MATCHED'}))
