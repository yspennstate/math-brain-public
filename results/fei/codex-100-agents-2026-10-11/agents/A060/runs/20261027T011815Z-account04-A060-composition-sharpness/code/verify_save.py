from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
def read(n):return json.loads((ROOT/n).read_text(encoding='utf-8'))
def write(n,o):(ROOT/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
checks=[]
for n in ('PROGRESS.json','PACKET_DELTA.json'):
    expected={x.split(' (')[0] for x in protocol['progress_fields']}
    assert set(read(n))==expected,(n,set(read(n))^expected)
    checks.append(n+' exact protocol fields PASS')
assert read('PROGRESS.json')==read('PACKET_DELTA.json')
assert read('PACKET_DELTA.json')['packet_ids']==['A060']
for c in read('CLAIMS.json'):
    assert set(c)==set(protocol['claim_fields'])
    assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
    assert sha(ROOT/c['proof_source']['path'])==c['proof_source']['sha256']
checks.append('claim exact fields and statement/proof hashes PASS')
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['report_fields']:assert '# '+heading in report,heading
assert report.rstrip().split('\n\n')[-2]=='# Universal bridge'
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (AGENT/'STATUS.md').read_text(encoding='utf-8').startswith('STATE: ')
checks.append('all required report headings; Universal bridge last; two-line status PASS')
files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
assert all(p.stat().st_size<20_000_000 for p in files)
checks.append('file sizes under20MB PASS')
assert read('out/all.json')['status']=='PASS'
assert read('out/FORMAL_STATUS.json')['whole_theorem_Lean_certified'] is False
write('out/SCHEMA_VALIDATION.json',{'status':'PASS','checks':checks})
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json' and '__pycache__' not in p.parts]
receipt={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files],'rolling':[{'path':str(AGENT/n),'sha256':sha(AGENT/n)} for n in ('STATUS.md','WORKLOG.md','LEARNED.md')],'external_adoption':'UNVERIFIED'}
write('out/PERSISTENCE_RECEIPT.json',receipt)
for entry in read('out/PERSISTENCE_RECEIPT.json')['files']:assert sha(ROOT/entry['path'])==entry['sha256']
print(json.dumps({'schema':'PASS','persistence_readback':'PASS','saved_files':len(files),'main_exact_assertions':read('out/all.json')['checks']}))
