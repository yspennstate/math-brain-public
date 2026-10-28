"""Seal post-publication metadata, preserving the immutable remote proof snapshot."""
from pathlib import Path
import contextlib,hashlib,importlib.util,io,json,sys
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=load(ROOT/'out/PUBLISH_RECEIPT.json')
assert r['head_verified'] and r['files_verified']==r['files_expected']==19 and not r['mismatches']
commit=r['commit'];url='https://github.com/'+r['repository']+'/commit/'+commit
pending=load(ROOT/'out/PUBLISH_COMMIT.json');assert pending['commit']==commit
pending['branch_update']='VERIFIED_ON_MASTER';pending['remote_files_verified']=19;save(ROOT/'out/PUBLISH_COMMIT.json',pending)
p=BASE/'STATUS.md';lines=p.read_text(encoding='utf-8').splitlines();assert len(lines)==2
lines[0]+=' GitHub snapshot verified '+commit[:7]+'.'
lines[1]=lines[1].replace('created; branch update pending.','verified on master; brain mirror still unverified.')
p.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
with (BASE/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n2026-10-23 publication receipt: '+url+'; tree '+r['tree']+'; parent '+r['parent']+'. All19 snapshot file Git blob hashes match the named-file-scanned local package; master head verified; workflow runs0 at readback. Source route explicitly uses master. No local git commands or shared-checkout edits. New theorem review and brain mirror remain pending. Post-publication receipt metadata remains local for supervisor adoption.\n')
with (BASE/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n2026-10-23 version binding: statement_sha256 is source-defined, not necessarily hash of bare statement. A071 hashes sorted compact JSON with statement,hypotheses; A072 uses exact_statement,hypotheses. Preserve both original conventions and digests; the initial bare-text checker failure was my convention assumption, not a source defect.\n')
p=ROOT/'REPORT.md';text=p.read_text(encoding='utf-8')
note='Checkpoint receipt: the19-file mathematical snapshot is saved at '+url+' on master (the explicit open-problem routing exception), tree '+r['tree']+'. Remote head and every file Git blob hash were independently read back; associated workflow runs were0. out/PUBLISH_RECEIPT.json is the local exact readback receipt. This paragraph, publication receipts, subsequent progress/rolling updates and final persistence inventory are post-publication metadata for the supervisor, and are not claimed to be inside their own earlier commit. The proof, claim statements and mathematical validation are unchanged. Brain mirror and independent acceptance of the new theorem remain unverified.\n'
assert '**Universal bridge:**' in text
p.write_text(text.replace('**Universal bridge:**',note+'\n**Universal bridge:**',1),encoding='utf-8',newline='\n')
progress=load(ROOT/'PROGRESS.json');progress['deliverable_status']='COMPLETE_LOCAL_ARTIFACTS_CHECKED; GITHUB_19_FILE_SNAPSHOT_VERIFIED; POST_PUBLICATION_METADATA_LOCAL; BRAIN_MIRROR_UNVERIFIED'
progress['blockers']=[x.replace('supervisor mirror verification pending','brain mirror verification pending') for x in progress['blockers']]
save(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
# Required repository checkpoint notice, not a mathematical review request.
mp=Path(r'~\<private-repo>\12_cognitive_architecture\agent_mesh\agent_mesh.py')
spec=importlib.util.spec_from_file_location('a089_mesh_finish',mp);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
agent='codex-A089-stage10-save';logs=[]
commands=[['--json','inbox','--agent',agent,'--pending'],['--json','send','--agent',agent,'--to','all','--topic','repo:math-open-problems','--body','Checkpoint A089 stage10 archived on master at '+commit+' [skip ci]. Exact19-file remote hash readback PASS; workflow runs0. New mathematical reserve theorem awaits independent review; full FEI and initial owner funding remain OPEN.'],['--json','bye','--agent',agent,'--status','done','--summary','A089 own-run archival snapshot verified; no remaining job; new theorem review and initial funding open.']]
for cmd in commands:
    out=io.StringIO()
    with contextlib.redirect_stdout(out),contextlib.redirect_stderr(out):rc=m.main(cmd)
    logs.append({'command':cmd[1],'exit':rc,'response':out.getvalue()})
save(ROOT/'out/PUBLISH_CLOSEOUT.json',logs)
assert logs[-1]['exit']==0,logs[-1]
protocol=load(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
pf=set(protocol['required_per_run']['progress_fields']);pf.remove('packet_ids (one primary ID, for compatibility)');pf.add('packet_ids')
assert set(load(ROOT/'PROGRESS.json'))==pf
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((BASE/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for c in load(ROOT/'CLAIMS.json'):
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    legacy=c['claim_id']=='A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS'
    key='statement' if legacy else 'exact_statement'
    d=hashlib.sha256(json.dumps({key:c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=legacy).encode('utf-8')).hexdigest()
    assert d==c['statement_sha256']
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json')
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt=load(ROOT/'out/PERSISTENCE.json');receipt['files']=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
receipt['rolling']=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in [BASE/'STATUS.md',BASE/'WORKLOG.md',BASE/'LEARNED.md']]
receipt['github_snapshot']={'commit':commit,'files':19,'remote_hashes_verified':True,'workflow_runs_observed':r['ci'].get('workflow_runs'),'post_publication_metadata':'local only; not inside earlier commit','brain_mirror_verified':False}
save(ROOT/'out/PERSISTENCE.json',receipt)
reloaded=load(ROOT/'out/PERSISTENCE.json')
assert all(sha(ROOT/x['path'])==x['sha256'] for x in reloaded['files'])
assert all(sha(Path(x['path']))==x['sha256'] for x in reloaded['rolling'])
assert load(ROOT/'out/VALIDATION.json')['status']=='PASS'
print(json.dumps({'status':'PASS','commit':commit,'remote_snapshot_files_verified':19,'local_files_hashed':len(files),'schemas':'PASS','mesh_notice_exit':logs[1]['exit'],'mesh_claim_released':True,'remaining_jobs':'NONE','review':'PENDING','initial_funding':'OPEN','full_FEI':'OPEN','brain_mirror':'UNVERIFIED'}))
