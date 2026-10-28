from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
def rd(p):return Path(p).read_text(encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads(rd(R/'out/PERSISTENCE_RECEIPT.json'))
for row in receipt['artifacts']:
 assert sha(R/row['path'])==row['sha256'],row['path']
for row in receipt['rolling_files']:
 assert sha(row['path'])==row['sha256'],row['path']
claims=json.loads(rd(R/'CLAIMS.json'))
for c in claims:
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
 assert c['review_records'][-1]['substantive_repair_supplied'] is False
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=rd(R/'REPORT.md');assert 'first unsupported universal line' in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert len(rd(R.parents[1]/'STATUS.md').splitlines())==2
certificate=json.loads(rd(R/'out/CERTIFICATE.json'))
assert certificate['exact_assertions']==5515 and len(certificate['profiles_data'])==417 and len(certificate['paths_data'])==30
assert {p['source_mass'] for p in certificate['paths_data']}=={'1','1/2'}
assert any(p['discarded_negative_reset_credit']['prime_log'] for p in certificate['paths_data'])
artifacts=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
receipt['artifacts']=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in artifacts]
receipt['checks'].append('Independent final readback verified all prior artifact and rolling-file hashes; negative reset credits actually discarded in certificate')
(R/'out/PERSISTENCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','hashed_artifacts':len(artifacts),'source_masses':['1','1/2'],'negative_credit_discard_exercised':True,'full_FEI':'OPEN'}))
print(rd(R.parents[1]/'STATUS.md').strip())
