from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
load=lambda p: json.loads(p.read_text(encoding='utf-8'))
protocol=load(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
P=load(R/'PROGRESS.json'); C=load(R/'CLAIMS.json'); V=load(R/'out/VALIDATION.json')
assert P==load(R/'PACKET_DELTA.json')
assert set(P)=={f.split(' (')[0] for f in protocol['progress_fields']}
for c in C:
    assert set(c)==set(protocol['claim_fields'])
    b=json.dumps(dict(statement=c['exact_statement'],hypotheses=c['hypotheses']),sort_keys=True,separators=(',',':')).encode('utf-8')
    assert hashlib.sha256(b).hexdigest()==c['statement_sha256']
report=(R/'REPORT.md').read_text(encoding='utf-8')
for f in protocol['report_fields']: assert '## '+f in report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert str(V['exact_assertions']) in report and V['status']=='PASS'
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert 'check(covariance(pt(0,1),parity,n)==cp)' in (R/'code/audit_www.py').read_text(encoding='utf-8')
assert (R/'out/FORMAL_STATUS.json').exists()
sources=load(R/'out/SOURCE_RECEIPTS.json')
assert len(sources)==2
files=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        b=p.read_bytes(); assert len(b)<20*1024**2
        files.append(dict(path=str(p.relative_to(R)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
out=dict(at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),protocol_fields='PASS',claims_fields='PASS',claim_hashes='PASS',packet_compatibility='PASS',status_two_lines='PASS',report_review='PASS',files=files,remote_copy='UNVERIFIED',independent_review='PENDING')
(R/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(validation='PASS',exact_assertions=V['exact_assertions'],runtime_seconds=V['runtime_seconds'],files=len(files),full_fei='OPEN')))
print((A/'STATUS.md').read_text(encoding='utf-8'))
print(report[:550])
