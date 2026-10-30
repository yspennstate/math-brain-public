from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
progress=read(R/'PROGRESS.json');assert progress==read(R/'PACKET_DELTA.json')
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
for c in read(R/'CLAIMS.json'):
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert c['version']==11 and hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
coordination_drift=[]
for source in read(R/'SOURCE_MANIFEST.json')['sources']:
    current=sha(Path(source['path']))
    if current!=source['sha256']:
        assert Path(source['path']).name in ('BOARD.md','STATUS.md'),('IMMUTABLE_PROOF_SOURCE_CHANGED',source['path'])
        coordination_drift.append({'path':source['path'],'read_sha256':source['sha256'],'current_sha256':current,'scope':'Mutable coordination changed after read; original observation retained; not a mathematical proof dependency.'})
report=(R/'REPORT.md').read_text(encoding='utf-8')
if coordination_drift:
    report=report.replace('source/artifact hashes, fixed case counts','immutable proof-source/artifact hashes and records mutable coordination drift, fixed case counts')
    (R/'REPORT.md').write_text(report,encoding='utf-8')
assert [s[2:] for s in report.splitlines() if s.startswith('# ')]==protocol['required_per_run']['report_fields']
assert report.split('\n\n')[-1].startswith('Universal bridge:')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert read(R/'out/validation.json')['assertions']==109505
assert len(read(R/'out/MIXED_LEDGER.json'))==1022
assert read(R/'out/validation_disjoint.json')['status']=='PASS'
assert read(R/'out/validation_disjoint.json')['counts']['roots']==2592
assert len(read(R/'out/DISJOINT_LEDGER.json'))==510
receipts=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
out={'status':'PASS','saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':'reopened exact schemas, claim digests, immutable proof-source hashes, final report headings/end paragraph, two-line STATUS, case/ledger counts and file limits','coordination_drift':coordination_drift,'files':receipts}
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PERSISTENCE_PASS','files':len(receipts),'largest_bytes':max(x['bytes'] for x in receipts),'coordination_drift':coordination_drift}))
print(report.split('\n\n')[1]);print(report.split('\n\n')[-1]);print((A/'STATUS.md').read_text(encoding='utf-8'))
