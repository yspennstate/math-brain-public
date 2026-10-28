from pathlib import Path
import json, hashlib
RUN=Path(__file__).resolve().parents[1]
OWN=RUN.parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj): (RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
proto=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
claims=read(RUN/'CLAIMS.json'); progress=read(RUN/'PROGRESS.json')
assert all(set(c)==set(proto['claim_fields']) for c in claims)
assert set(progress)=={x.split(' (')[0] for x in proto['progress_fields']}
assert progress['packet_ids']==['A094']
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
sourcepath=OWN.parents[1]/'agents/A095/runs/20261021T180853Z-account03-A095-restricted-result-extraction/CLAIMS.json'
source=read(sourcepath)[0]
assert all(claims[0][k]==source[k] for k in ['exact_statement','hypotheses','statement_sha256'])
canonical=json.dumps({'exact_statement':source['exact_statement'],'hypotheses':source['hypotheses']},sort_keys=True,ensure_ascii=False,separators=(',',':'))
assert hashlib.sha256(canonical.encode('utf-8')).hexdigest()==source['statement_sha256']
assert hashlib.sha256(claims[1]['exact_statement'].encode('utf-8')).hexdigest()==claims[1]['statement_sha256']
save('out/HASH_CONVENTIONS.json',{'source_claim':source['claim_id'],'source_convention':'SHA256 UTF-8 json.dumps({exact_statement,hypotheses},sort_keys=True,ensure_ascii=False,separators=(comma,colon))','source_hash_verified':True,'source_declared_hash':source['statement_sha256'],'source_plain_statement_hash':hashlib.sha256(source['exact_statement'].encode('utf-8')).hexdigest(),'new_claim_convention':'SHA256 of exact_statement UTF-8','new_claim_hash_verified':True})
source_checks=[]
for row in read(RUN/'out/SOURCE_RECEIPTS.json'):
    current=sha(Path(row['path']))
    source_checks.append({'path':row['path'],'intake_sha256':row['sha256'],'current_sha256':current,'unchanged':current==row['sha256']})
    if Path(row['path']).name!='BOARD.md':
        assert current==row['sha256'],row['path']
save('out/SOURCE_RECHECK.json',{'scope':'Live BOARD may change concurrently; immutable mathematical source hashes must match. Intake receipts are preserved.','sources':source_checks})
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
headings=[line.strip().lstrip('#').strip() for line in report.splitlines() if line.startswith('#')]
required=proto['report_fields']
assert all(any(field.lower() in heading.lower() for heading in headings) for field in required),(required,headings)
assert 'Universal bridge' in report.split('\n\n')[-1] or headings[-1]=='Universal bridge'
status=(OWN/'STATUS.md').read_text(encoding='utf-8').splitlines()
assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
main=read(RUN/'out/MAIN_RESULTS.json')
assert main['assertions']==11302 and main['reset_cases']==58
assert not read(RUN/'out/LEAN_RECEIPT.json')['compiler_started']
files=[p for p in RUN.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20*1024*1024 for p in files)
save('out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_exact_field_sets':True,'progress_exact_field_set':True,'progress_delta_byte_identical':True,'source_statement_and_hypotheses_unchanged':True,'both_hash_conventions_verified':True,'immutable_mathematical_source_hashes_verified':True,'live_board_changed_since_intake':any(not row['unchanged'] for row in source_checks),'report_required_headings_present':True,'universal_bridge_last':True,'rolling_status_two_lines':True,'all_files_under_20MiB':True,'mathematical_checks':11302,'reset_cases':58,'formal_certificate':False})
targets=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[OWN/name for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
save('out/PERSISTENCE_RECEIPTS.json',{'scope':'Local files only; no external adoption or mirror receipt claimed','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(targets)]})
print(json.dumps({'artifact_validation':'PASS','claims':len(claims),'reset_cases':58,'exact_checks':11302,'receipt_files':len(targets),'status':status},ensure_ascii=False))
