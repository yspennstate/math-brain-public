"""Record read-only publication checks and refresh persistence receipts."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];O=R/'out';A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,d):p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
reason='Required publication branch main does not resolve: GitHub get-repository reports default_branch=master; get-commit main returns422 No commit found for SHA: main. No remote changes made; supervisor copy remains unverified.'
write(O/'PUBLICATION_RECEIPT.json',{'status':'BLOCKED_BRANCH_MISMATCH','repository':'yspennstate/math-open-problems','default_branch_observed':'master','required_branch':'main','get_commit_main_http_status':422,'get_commit_main_message':'No commit found for SHA: main','remote_mutations':False,'git_commands_executed':False,'reason':reason})
p=read(R/'PROGRESS.json');p['blockers'].append(reason);p['source_artifacts'].append('out/PUBLICATION_RECEIPT.json')
write(R/'PROGRESS.json',p);write(R/'PACKET_DELTA.json',p)
report=(R/'REPORT.md').read_text(encoding='utf-8');needle='Supervisor copy, brain ingestion and remote mirror are not claimed.'
assert needle in report
report=report.replace(needle,needle+' '+reason+' Receipt: out/PUBLICATION_RECEIPT.json.')
(R/'REPORT.md').write_text(report,encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 stage025441Z persistence check: '+reason+' Local schema and hash validation refreshed after recording this blocker.\n')
v=read(O/'FINAL_VALIDATION.json');v['checked_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();v['remote_mirror']='BLOCKED_BRANCH_MISMATCH'
files=[p for p in R.rglob('*') if p.is_file() and p!=O/'FINAL_VALIDATION.json' and '__pycache__' not in str(p)]
v['artifacts']=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
assert all(p.stat().st_size<20_000_000 for p in files)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
fields=set(protocol['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(read(R/'PROGRESS.json'))==fields
assert set(read(R/'CLAIMS.json')[0])==set(protocol['claim_fields'])
assert all('## '+h in report for h in protocol['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
write(O/'FINAL_VALIDATION.json',v)
assert all(hashlib.sha256((R/a['path']).read_bytes()).hexdigest()==a['sha256'] for a in read(O/'FINAL_VALIDATION.json')['artifacts'])
print(json.dumps({'status':'PASS','artifact_hashes_rechecked':len(files),'remote':'BLOCKED_BRANCH_MISMATCH','primary':v['primary_assertions'],'independent':v['independent_assertions']}))
