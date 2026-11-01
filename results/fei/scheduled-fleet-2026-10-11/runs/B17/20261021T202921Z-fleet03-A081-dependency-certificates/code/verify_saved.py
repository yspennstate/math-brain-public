from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=read(R/'out/PERSISTENCE_RECEIPTS.json')
for f in receipt['files']:
    p=R/f['path'];assert p.stat().st_size==f['bytes'];assert sha(p)==f['sha256']
g=read(R/'PROOF_DEPENDENCIES.json')
nodes={n['claim_id']+'@'+str(n['version']):n for n in g['nodes']}
assert nodes['FEI-FINAL@1']['status']=='OPEN'
assert len(nodes)==76
for p in read(R/'out/SOURCE_PINS.json'):assert sha(R/p['snapshot'])==p['sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert read(R/'out/GRAPH_VALIDATION.json')['status']=='PASS'
assert len(read(R/'out/GRAPH_VALIDATION.json')['guards'])==12
assert read(R/'out/EXACT_CHECK.json')['assertions']==72109
assert read(R/'out/SCHEMA_VALIDATION.json')['status']=='PASS'
assert read(R/'CLAIMS.json')[0]['review_records'][-1]['reviewer_contributed_repair'] is False
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert report.rstrip().split('\n\n')[-1].startswith('This stage moves C024')
assert 'RUNTIME_UNVERIFIED' in report
assert 'Verdict: HOLDS' in (R/'REVIEW.md').read_text(encoding='utf-8')
history={'pilot_failure':'Exact-zero CE release not resolved by subtraction of outward intervals; repaired by exact rational-log term cancellation.','serialization_failure':'Unrounded interval denominator growth exceeded Python integer-to-string digit limit; repaired by outward dyadic log enclosure.','final_replay':'PASS,72109 assertions; no mathematical assertion disabled; pilot subset not double-counted.'}
(R/'out/CHECKER_REPAIR_HISTORY.json').write_text(json.dumps(history,indent=2),encoding='utf-8')
out={'status':'PASS','previous_receipt_files_rehashed':len(receipt['files']),'new_source_snapshots_rehashed':len(read(R/'out/SOURCE_PINS.json')),'nodes':len(nodes),'full_fei':'OPEN','remote_copy':'UNVERIFIED','lean':'RUNTIME_UNVERIFIED'}
(R/'out/FINAL_READBACK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='PERSISTENCE_RECEIPTS.json']
receipt['files']=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(out))
