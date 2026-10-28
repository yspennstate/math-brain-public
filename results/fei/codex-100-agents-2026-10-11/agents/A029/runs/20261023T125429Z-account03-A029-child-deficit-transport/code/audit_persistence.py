from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];AG=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=read(R/'out/ARTIFACTS.json')
assert all(sha(R/x['path'])==x['sha256'] for x in old)
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+k in report for k in protocol['report_fields'])
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert len((AG/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256'] for c in read(R/'CLAIMS.json'))
save(R/'out/LIFECYCLE.json',{'entry':'T-20261023-469','research_status':'COMPLETE_LOCAL_REVIEW_HANDOFF','shared_closure':'NOT_MUTATED_IN_THIS_FINAL_SAVE','reason':'Specific stage instruction restricts writes to A029 and makes brain/shared trees read-only. Shared checklist and supervisor mirror remain unverified. No shared research write or git operation was made.','brain_selfcare':'DEGRADED_UNVERIFIED; stale owner-model/state-of-mind/dream context, not used for mathematical evidence','own_arithmetic_jobs_remaining':0})
save(R/'out/PERSISTENCE_AUDIT.json',{'status':'PASS','existing_manifest_entries_rechecked':len(old),'protocol_report_fields':len(protocol['report_fields']),'progress_delta_identical':True,'all_claim_statement_hashes_match':True,'rolling_status_lines':2,'metadata_correction':'Initial field validator compared the descriptive protocol label packet_ids (one primary ID, for compatibility) literally with packet_ids. Normalized descriptor and reran successfully; no mathematical check changed.'})
with (AG/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+' stage9 persistence audit: corrected descriptive packet_ids schema-label comparison; rerun PASS. Rechecked saved byte hashes and report headings; all claim statement hashes and PROGRESS/PACKET_DELTA match. Shared checklist closure/mirror unverified under A029-only write boundary; see out/LIFECYCLE.json. No mathematical check or scope changed.\n')
manifest=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and '__pycache__' not in str(p) and p.name!='ARTIFACTS.json':
  assert p.stat().st_size<20*1024*1024
  manifest.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/ARTIFACTS.json',manifest)
print(json.dumps({'status':'PERSISTENCE_PASS','files':len(manifest),'own_arithmetic_jobs_remaining':0,'peer_review':'PENDING','full_fei':'OPEN'}))
