from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1]
path=RUN/'out'/'PERSISTENCE_RECEIPTS.json'
r=json.loads(path.read_text(encoding='utf-8'))
def receipt(p):
    data=p.read_bytes()
    return dict(path=str(p),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
# Refresh after the report's final runtime transcription and this verifier.
r['files']=[receipt(p) for p in sorted(RUN.rglob('*')) if p.is_file() and p!=path]
r['saved_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
r=json.loads(path.read_text(encoding='utf-8'))
for item in r['files']+r['rolling_files']:
    assert receipt(Path(item['path']))==item
    assert item['bytes']<20*1024*1024
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
required=protocol['required_per_run']
claim=json.loads((RUN/'CLAIMS.json').read_text())[0]
progress=json.loads((RUN/'PROGRESS.json').read_text())
assert set(claim)==set(required['claim_fields'])
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
assert set(progress)=={x.split(' (')[0] for x in required['progress_fields']}
assert progress==json.loads((RUN/'PACKET_DELTA.json').read_text())
assert progress['packet_ids']==['A097']
print(json.dumps(dict(schema='PASS',statement_hash='PASS',file_hashes='PASS',run_files=len(r['files']),rolling_files=len(r['rolling_files']),all_files_under_20_MB=True,full_fei='OPEN'),indent=2))
