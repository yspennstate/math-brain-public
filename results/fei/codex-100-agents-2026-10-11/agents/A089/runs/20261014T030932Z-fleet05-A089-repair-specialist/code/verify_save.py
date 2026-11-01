from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
rpath=ROOT/'out/RECEIPTS.json';receipt=json.loads(rpath.read_text())
receipt['exact_mathematical_assertions']=58043;receipt['runtime_cap_assertions']=14
receipt['files']=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipt['files'].append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
rpath.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
status=(AGENT/'STATUS.md').read_text(encoding='utf-8').replace('58057 exact checks','58043 exact math checks')
(AGENT/'STATUS.md').write_text(status,encoding='utf-8');assert len(status.splitlines())==2
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+' Count clarification:58057 recorded assertions include14 per-case runtime-cap predicates;58043 are exact mathematical predicates. Report, STATUS and receipts distinguish them; no proof, job or certificate changed.\n')
for row in receipt['files']:assert hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()==row['sha256']
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
assert set(json.loads((ROOT/'CLAIMS.json').read_text())[0])==set(protocol['required_per_run']['claim_fields'])
assert set(json.loads((ROOT/'PROGRESS.json').read_text()))=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
print(json.dumps({'artifact_hashes_verified':len(receipt['files']),'exact_math_assertions':58043,'runtime_cap_assertions':14,'schemas_and_delta':'PASS','rolling_status':'two lines; current'}))
