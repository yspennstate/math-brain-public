"""Read-only verification of saved artifact bytes and protocol field sets."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R.parent.parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=read(R/'out/PERSISTENCE_RECEIPTS.json')
for item in receipt['files']:
    p=R/item['path'];assert p.stat().st_size==item['bytes'] and sha(p)==item['sha256'],p
for item in receipt['rolling']:assert sha(A/item['path'])==item['sha256']
proto=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
claim=read(R/'CLAIMS.json')[0];progress=read(R/'PROGRESS.json')
assert set(claim)==set(proto['required_per_run']['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in proto['required_per_run']['progress_fields']}
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
for field in proto['required_per_run']['report_fields']:assert '## '+field+'\n' in report
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert read(R/'out/certificate.json')['adaptive_prefix_rows']==533248
assert read(R/'out/independent_certificate.json')['assertions']==1061
print('PASS: all recorded artifact/rolling hashes, exact protocol fields, statement binding, report sections and byte-identical packet delta.')
print(report.splitlines()[0])
print(report.rsplit('## Universal bridge',1)[1].strip())
