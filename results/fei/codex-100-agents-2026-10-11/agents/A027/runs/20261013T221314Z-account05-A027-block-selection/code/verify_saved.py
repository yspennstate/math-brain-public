import json,hashlib
from pathlib import Path
run=Path(__file__).resolve().parents[1]
# Metadata repair only: pilot has four physical variables; full has five.
path=run/'out'/'pilot.json'; p=json.loads(path.read_text()); p['largest_truth_table_size']=16
path.write_text(json.dumps(p,indent=2)+'\n',encoding='utf-8')
receipt_path=run/'out'/'PERSISTENCE_RECEIPT.json'; receipt=json.loads(receipt_path.read_text())
receipt['metadata_correction']='Pilot maximum truth table size corrected from full-domain upper bound 32 to actual 16; no mathematical output or domain changed.'
receipt['files']=[{'path':str(path.relative_to(run)),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()} for path in sorted(run.rglob('*')) if path.is_file() and path!=receipt_path]
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for entry in receipt['files']:
    path=run/entry['path']
    assert path.stat().st_size==entry['bytes']<20*1024*1024
    assert hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256']
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
print(json.dumps({'status':'PASS','verified_files':len(receipt['files']),'report':str(run/'REPORT.md')}))
