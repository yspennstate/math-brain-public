from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'));progress=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
keys=set(protocol['required_per_run']['claim_fields'])
for c in claims:
 assert set(c)==keys,(set(c)-keys,keys-set(c))
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
pkeys=set('packet_ids' if x.startswith('packet_ids ') else x for x in protocol['required_per_run']['progress_fields'])
assert set(progress)==pkeys
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report,field
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
jobs={}
for n in ['MAIN','RESERVE','PILOT','DICTATOR','NONFLAT','SEPARATORS','FINAL_AUDIT']:
 o=json.loads((R/'out'/f'{n}.json').read_text(encoding='utf-8'));assert o['status']=='PASS';jobs[n]={'checks':o['checks'],'runtime_seconds':o.get('runtime_seconds')}
assert sum(o['checks'] for o in jobs.values())==40228
lean=json.loads((R/'out/LEAN_RESULT.json').read_text(encoding='utf-8'));assert lean['result']['status']=='RUNTIME_UNVERIFIED'
# Known execution failures are recorded, never recast as mathematical failures.
repairs=json.loads((R/'out/VALIDATION_REPAIRS.json').read_text(encoding='utf-8'))
repairs['separator_harness']='Initial NameError from omitted __file__ in private namespace; fixed and full same80-node domain rerun PASS.'
(R/'out/VALIDATION_REPAIRS.json').write_text(json.dumps(repairs,indent=2)+'\n',encoding='utf-8',newline='')
source= A.parent/'A046/runs/20261014T083236Z-account05-A046-current-candidate-intake'
paths=[protocol_path,A/'LEARNED.md',A/'WORKLOG.md',Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B08\STREAM_NOTES.md')]
paths += [source/n for n in ['REPORT.md','PROOF.md','CLAIMS.json']]
base=protocol_path.parent
paths += [base/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += list(Path(r'~\brain_workers\FEI100_20261011\context').glob('*.txt'))
receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':'source identity receipt; not independent verification of source claims'} for p in paths]
(R/'out/SOURCE_MANIFEST.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8',newline='')
# Summaries reference final main job unchanged; latest helper differs only in fixture dispatch/account serialization.
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
result={'status':'PASS','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol_schemas_exact':True,'progress_delta_identical':True,'status_two_lines':True,'total_passed_assertions':40228,'jobs':jobs,'Lean':'RUNTIME_UNVERIFIED, not formal certification','local_only':True,'shared_adoption':'UNVERIFIED','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:result[k] for k in ['status','protocol_schemas_exact','progress_delta_identical','total_passed_assertions','Lean']},indent=2))
