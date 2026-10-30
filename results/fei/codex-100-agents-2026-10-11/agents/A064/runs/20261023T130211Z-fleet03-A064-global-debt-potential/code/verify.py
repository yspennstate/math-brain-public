from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
SOURCE=AGENT.parent/'A061/runs/20261023T113614Z-fleet03-A061-entropy-process'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8',newline='\n')

def main():
 schema=read(ROOT/'out/SCHEMA.json');claims=read(ROOT/'CLAIMS.json');progress=read(ROOT/'PROGRESS.json')
 assert set(progress)==set(schema['required_progress_fields'])
 assert progress['protocol_revision']=='2026-10-11-execution-v2'
 assert progress['packet_ids']==['A064'] and progress['stream']=='B13'
 assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
 assert len(claims)==2
 for c in claims:
  assert set(c)==set(schema['required_claim_fields'])
  assert Path(c['proof_source']['path']).is_file()
  assert sha(Path(c['proof_source']['path']))==c['proof_source']['sha256']
 original=read(SOURCE/'CLAIMS.json')[0]
 assert {k:v for k,v in claims[1].items() if k!='review_records'}=={k:v for k,v in original.items() if k!='review_records'}
 assert claims[1]['review_records'][:-1]==original['review_records']
 assert claims[1]['review_records'][-1]['verdict']=='INDEPENDENT_RECONSTRUCTION_HOLDS_UNCHANGED'
 assert claims[0]['statement_sha256']==hashlib.sha256(claims[0]['exact_statement'].encode('utf-8')).hexdigest()
 assert claims[0]['first_unproved_line'] is None
 assert claims[0]['status']=='AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW'
 results=[read(ROOT/'out'/n) for n in ['MAIN.json','A061_AUDIT.json','RARE_BRANCH.json','INITIAL_CAPITAL.json']]
 assert all(r['status']=='PASS' for r in results)
 total=sum(r['exact_assertions'] for r in results)
 assert total==claims[0]['review_records'][0]['certificate_assertions_excluding_pilot']
 assert results[0]['counts']['states']==256*2*13
 assert results[0]['counts']['ordinary_transports']==9216
 assert results[0]['counts']['negative_eligibility_sectors']==0
 assert results[1]['B']=={'2':'3','7':'-1/2'}
 assert results[1]['full_mean_terminal_H']=={'2':'9/2'}
 assert results[2]['actual_dummy_counts']==[1,2] and results[2]['maximum_actual_dimension']==13
 assert results[3]['point_dimensions']==[2,4,6,8]
 spec=read(ROOT/'out/FROZEN_SPEC.json');amend=read(ROOT/'out/AUDIT_SPEC_AMENDMENT.json')
 assert sha(ROOT/'code/exact.py')==spec['helper_version']
 for name,digest in amend['current_code_sha256'].items():assert sha(ROOT/'code'/name)==digest
 for p in read(ROOT/'out/SOURCE_PINS.json')['pins']:assert sha(Path(p['path']))==p['sha256']
 report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
 for field in schema['report_fields']:assert '## '+field in report
 assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
 status=(AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines()
 assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
 assert str(total) in status[0] and 'FEI OPEN' in status[0]
 assert 'degraded/unverified' in report and 'brain' in report.lower()
 receipt={'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),'protocol_schema':'exact claim and progress keysets','compatibility_copy':'byte-identical','source_claim':'payload unchanged except appended independent review','new_statement_sha256':claims[0]['statement_sha256'],'proof_hashes':'match','exact_primary_assertions':total,'pilot_excluded':read(ROOT/'out/PILOT.json')['exact_assertions'],'research_jobs_left_running':False,'external_review':'pending A087/A094','mirror_verification':'unobserved; supervisor-owned'}
 write(ROOT/'out/VERIFY.json',receipt)
 manifest={'run_files':[],'rolling_files':[],'manifest_self':'excluded to avoid circular hash'}
 for p in sorted(ROOT.rglob('*')):
  if p.is_file() and p!=ROOT/'out/MANIFEST.json':
   assert p.resolve().is_relative_to(AGENT.resolve())
   assert p.stat().st_size<20*1024*1024
   manifest['run_files'].append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
 for name in ('STATUS.md','WORKLOG.md','LEARNED.md'):
  p=AGENT/name;manifest['rolling_files'].append({'path':str(p),'sha256':sha(p)})
 write(ROOT/'out/MANIFEST.json',manifest)
 again=read(ROOT/'out/MANIFEST.json')
 for item in again['run_files']:assert sha(ROOT/item['path'])==item['sha256']
 for item in again['rolling_files']:assert sha(Path(item['path']))==item['sha256']
 print(json.dumps({'status':'PASS','run_files_hashed_and_read_back':len(again['run_files']),'rolling_files_read_back':3,'primary_exact_assertions':total,'pilot_separate':receipt['pilot_excluded'],'new_claim_review':'pending','full_FEI':'OPEN'}))
if __name__=='__main__':main()
