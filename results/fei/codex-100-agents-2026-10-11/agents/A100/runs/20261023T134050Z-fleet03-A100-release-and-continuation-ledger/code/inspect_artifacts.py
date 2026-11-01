from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parent.parent;O=R/'out'
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
notes={'display_only_attempt':'An extra post-readback inline display used unresolved Path(\'.\').parent.parent and therefore looked for STATUS.md in the run, not A100. It failed after displaying REPORT.md. No files were mutated by that command.','correction':'Use this script resolved from __file__; inspect rolling STATUS, fresh-review tag, current manifest bytes and size domain explicitly.','mathematical_results_affected':False}
(O/'OUTPUT_INSPECTION_NOTES.json').write_text(json.dumps(notes,indent=2)+'\n',encoding='utf-8',newline='\n')
report=(R/'REPORT.md').read_text(encoding='utf-8');status=(A/'STATUS.md').read_text(encoding='utf-8');assert 'reserve is>77/32' in report and 'full FEI OPEN' in status
ledger=load(O/'THEOREM_RELEASE_LEDGER.json');fresh=[x for x in ledger['accepted'] if x['A100_full_reconstruction_this_stage']]
assert len(fresh)==1 and fresh[0]['claim_id']=='A097-NECESSARY-FLOOR-ADMISSION-SAME-ORIGINAL-OWNER'
manifest=load(O/'PERSISTENCE_RECEIPTS.json')
for x in manifest['files']:assert hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256']
assert all(p.stat().st_size<20_000_000 for p in R.rglob('*') if p.is_file())
assert len(load(O/'NEXT_TEN_QUESTIONS.json'))==10
out={'status':'PASS','report_read':True,'rolling_status_read':True,'one_fresh_full_A100_review':fresh[0]['claim_id'],'recorded_scope_acceptances':ledger['counts']['accepted_statement_versions'],'ten_questions':10,'all_files_under_20MB':True,'manifest_payloads_rechecked_before_refresh':len(manifest['files']),'full_FEI':'OPEN'}
(O/'ARTIFACT_INSPECTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out));print(status.strip())
