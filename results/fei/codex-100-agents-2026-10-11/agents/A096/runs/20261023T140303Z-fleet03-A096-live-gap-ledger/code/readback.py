"""Open the delivered report and re-check every persisted actual byte hash."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];HOME=ROOT.parents[1]
receipt=json.loads((ROOT/'out/LOCAL_PERSISTENCE.json').read_text(encoding='utf-8'))
for x in receipt['files']:assert hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256'],x['path']
for x in receipt['rolling_files']:assert hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'],x['path']
claims=json.loads((ROOT/'CLAIMS.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256'] for c in claims)
assert claims[0]['claim_id']=='A096-ADOPTED-A050-OCCUPIED-WITNESS-HEREDITY'
assert claims[1]['claim_id']=='A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT'
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8');assert len(report)<22000;print(report)
print((HOME/'STATUS.md').read_text(encoding='utf-8'))
print('FINAL ARTIFACT READBACK PASS:',len(receipt['files']),'run files and3 rolling files; explicit source adoption, statement hashes and actual bytes verified.')
