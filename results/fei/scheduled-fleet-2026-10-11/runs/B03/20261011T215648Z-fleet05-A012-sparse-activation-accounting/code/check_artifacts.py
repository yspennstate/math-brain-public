from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
P=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8'))['required_per_run']
progress=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for c in json.loads((R/'CLAIMS.json').read_text(encoding='utf-8')):
    assert set(c)==set(protocol['claim_fields'])
    s=json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'))
    assert hashlib.sha256(s.encode()).hexdigest()==c['statement_sha256']
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all(x in report for x in protocol['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
receipt=json.loads((R/'out'/'PERSISTENCE_RECEIPTS.json').read_text(encoding='utf-8'))
for x in receipt['files']:
    p=Path(x['path']);assert p.stat().st_size==x['bytes'];assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'];assert p.stat().st_size<20_000_000
assert len((R.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert progress['packet_ids']==['A012']
print(json.dumps({'status':'PASS','protocol_fields_exact':True,'progress_delta_identical':True,'claim_hashes_valid':True,'receipt_files_verified':len(receipt['files']),'under_20_MB_each':True}))
