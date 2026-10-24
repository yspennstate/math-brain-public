"""Reconcile actual referee receipts, resubmit the reviewed DRAFT, and report."""
from pathlib import Path
from datetime import datetime, timezone
import subprocess
import os
import json

ROOT=Path('~')
JOB=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
referee=ROOT/'brain_workers/w524/VERDICTS.jsonl'
verdicts=[json.loads(x) for x in referee.read_text(encoding='utf-8-sig').splitlines()]
c3=next(v for v in verdicts if v.get('claim')=='P0297-w523-C3')
boundary=next(v for v in verdicts if v.get('claim')=='P0297-w523-L1-L2')
assert c3['verdict']=='KEEP' and boundary['verdict']=='KEEP'
assert all(v.get('independent_reviewer')=='w524' for v in [c3,boundary])
receipt={'observed_at':now,'source_path':str(referee),'verdicts':[boundary,c3],'scope':'Own L1/L2 algebra and C3 fixed-gamma counterexample only; original target is not solved.','login_independence_verified':False,'formal_proof_receipt':None}
(JOB/'INDEPENDENT_REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False),encoding='utf-8')
with (JOB/'RESUME_ROWS.jsonl').open('a',encoding='utf-8') as f:
    f.write(json.dumps({'id':'P0297-w523-resume-02','verdict':'REFEREE_KEEP_CONFIRMED','subjects':['P0297-w523-L1','P0297-w523-L2','P0297-w523-C3'],'scope':receipt['scope'],'source':str(referee),'receipt':'INDEPENDENT_REVIEW_RECEIPT.json','login_eligibility':'Not independently verified; no two-login admission claim.'})+'\n')

claims_path=JOB/'CLAIMS.jsonl'
claims=[json.loads(x) for x in claims_path.read_text(encoding='utf-8').splitlines()]
for row in claims:
    if row['id'] in {'P0297-w523-L1','P0297-w523-L2','P0297-w523-C3'}:
        row['status']='independently checked proof'
        row['independent_reviewer']='w524'
        row['independent_review_receipt']='INDEPENDENT_REVIEW_RECEIPT.json'
        row['independently_checked']=True
        if row['id']=='P0297-w523-C3':
            row['remaining_gap']='None in the source-backed fixed-gamma counterexample after the scoped referee KEEP. The actual LFPP normalization exponent and original target remain undetermined; no novelty or formal-machine certification is claimed.'
        else:
            row['remaining_gap']='None in this deterministic algebraic statement after the scoped referee KEEP. It does not determine xi_gamma or prove a theorem about critical metrics.'
claims_path.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')

states_path=JOB/'BRAIN_STATES.json'
states=json.loads(states_path.read_text(encoding='utf-8'))
old_submitted=states['submitted']['path']
bundle=json.loads((JOB/'bundle_local_001.json').read_text(encoding='utf-8'))
for e in bundle['entries']:
    s=e['statement']
    s=s.replace('DRAFT, independent review pending. ', 'Scoped campaign derivation independently checked by the named referee. ')
    s=s.replace('REFUTED AUXILIARY BRIDGE; draft campaign audit pending. ', 'REFUTED AUXILIARY BRIDGE; scoped campaign counterexample independently checked. ')
    s=s.replace('DRAFT source-backed counterexample, independent review pending. ', 'Source-backed counterexample independently checked in the scoped campaign review. ')
    e['statement']=s
    e['source']['revision']='campaign-derivation-2026-10-10-scoped-referee-keep'
    assert e['kind']=='concept' and e['proof_text'] is None
bundle['review_state']='C3 and its source-backed inputs independently checked by w524; concept-only DRAFT; integration pending'
bundle['review_evidence']={'claim':'P0297-w523-C3','verdict':'KEEP','receipt':str(JOB/'INDEPENDENT_REVIEW_RECEIPT.json')}
bundle['supersedes_submitted_draft']=old_submitted
local=JOB/'bundle_local_002.json'
payload=json.dumps(bundle,indent=2,ensure_ascii=False).encode('utf-8')
local.write_bytes(payload)
inbox=(ROOT/'math-brain-inbox/w523').resolve()
assert inbox.parent==(ROOT/'math-brain-inbox').resolve() and inbox.name=='w523'
destination=inbox/'bundle_002.json'
part=inbox/'bundle_002.json.part'
if destination.exists():
    assert destination.read_bytes()==payload,'Different existing reviewed draft preserved.'
else:
    assert not part.exists(),'Existing incomplete part preserved; inspect it before retry.'
    assert part.resolve().parent==inbox and destination.resolve().parent==inbox
    with part.open('xb') as f:
        f.write(payload)
    part.rename(destination)
assert destination.read_bytes()==payload
states['prepared'].update(state=True,local_artifact=str(local),kind='concept-only; scoped C3 independent KEEP recorded')
states['submitted'].update(state=True,path=str(destination),atomic_complete_then_rename=True)
states['submission_history']=[{'path':old_submitted,'state':'earlier unreviewed concept draft; preserved'},{'path':str(destination),'state':'review metadata reconciled; submitted'}]
states['reviewed']={'state':True,'reviewer':'w524','receipt':str(JOB/'INDEPENDENT_REVIEW_RECEIPT.json'),'scope':'L1-L2 and C3; no original-target solution or cross-login admission certificate'}
for name in ['ingested','retrievable']:
    states[name]={'state':False,'receipt':None,'verification_status':'No independent receipt observed; not certified.'}
states_path.write_text(json.dumps(states,indent=2),encoding='utf-8')
source_path=JOB/'SOURCE_STATUS.json'
source=json.loads(source_path.read_text(encoding='utf-8'))
source['independent_reviewer']='w524; scoped KEEP for L1-L2 and C3 verified from actual verdict file'
source['independent_review_receipt']='INDEPENDENT_REVIEW_RECEIPT.json'
source['brain_submission'].update(prepared=True,submitted=True,reviewed=True,ingested=False,retrievable=False,path=str(destination))
source_path.write_text(json.dumps(source,indent=2,ensure_ascii=False),encoding='utf-8')

# The resumed user instruction explicitly requests a hooks1000 proposal and a progress event.
hook=json.loads((JOB/'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8').strip())
hook['evidence']=str(JOB/'ATTEMPT.md')+' C3; '+str(JOB/'MEASUREMENTS.json')+' dependent_set_bridge; '+str(JOB/'INDEPENDENT_REVIEW_RECEIPT.json')
assert len(hook['text'])<=300 and all(hook.get(k) for k in ['id','area','event','cue','fire_when','silent_when','text','evidence','proposer'])
proposal=ROOT/'primary_directive/hooks1000/proposals/math-w523.jsonl'
assert proposal.resolve().parent==(ROOT/'primary_directive/hooks1000/proposals').resolve()
existing=[]
if proposal.exists():
    existing=[json.loads(x) for x in proposal.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
same=[x for x in existing if x.get('id')==hook['id']]
if same:
    hook_state='already present; existing evidence preserved'
else:
    with proposal.open('a',encoding='utf-8',newline='\n') as f:
        f.write(json.dumps(hook,ensure_ascii=False)+'\n')
    hook_state='appended for the next proposal audit; no global hook implementation'
recheck=[json.loads(x) for x in proposal.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
assert sum(x.get('id')==hook['id'] for x in recheck)==1
hook_receipt={'path':str(proposal),'id':hook['id'],'state':hook_state,'proposal_present_verified':True,'global_hook_implemented':False}
(JOB/'HOOK_SUBMISSION_RECEIPT.json').write_text(json.dumps(hook_receipt,indent=2),encoding='utf-8')

env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1')
def run(args,timeout=45):
    try:
        r=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=timeout,env=env)
        return {'command':args,'returncode':r.returncode,'stdout':r.stdout[:3000],'stderr':r.stderr[:1500]}
    except subprocess.TimeoutExpired:
        return {'command':args,'timeout_seconds':timeout,'state':'Completion not certified; inspect destination before any retry.'}

event='P0297 w523: verified w524 KEEP for the thick-point KPZ counterexample and boundary lemmas; submitted reviewed concept draft bundle_002 and one hook proposal; ingestion unverified.'
progress_args=['python','-X','utf8',str(ROOT/'primary_directive/pd_progress.py'),'--event',event,'--agent','w523','--row','S1.P0297.w523.C3','--evidence',str(JOB/'INDEPENDENT_REVIEW_RECEIPT.json')]
progress=run(progress_args)
(JOB/'PROGRESS_POST_RECEIPT.json').write_text(json.dumps(progress,indent=2,ensure_ascii=False),encoding='utf-8')
print('PROGRESS_RESULT',json.dumps(progress,ensure_ascii=False))

comm=str(ROOT/'<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py')
team_read=run(['python','-X','utf8',comm,'read','--as','w523','--max','8'],timeout=30)
print('TEAM_READ_RESULT',json.dumps(team_read,ensure_ascii=False))
routes=[]
mesh=str(ROOT/'<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py')
body='P0297 resume: actual w524 KEEP for C3 and L1-L2 saved. Latest concept draft: ~/math-brain-inbox/w523/bundle_002.json. Receipt and review packet: ~/brain_workers/w523/INDEPENDENT_REVIEW_RECEIPT.json and REVIEW_PACKET.md. Original LFPP exponent remains open in this attempt; ingestion unverified.'
for who in ['w522','w524']:
    result=run(['python','-X','utf8',mesh,'send','--agent','w523','--to',who,'--topic','P0297-reviewed-draft-handoff','--kind','message','--body',body,'--idempotency-key','w523-P0297-reviewed-draft-002'],timeout=30)
    routes.append(result)
    print('PEER_ROUTE_RESULT',who,json.dumps(result,ensure_ascii=False))
(JOB/'RESUME_COORDINATION_RECEIPTS.json').write_text(json.dumps({'team_read':team_read,'peer_routes':routes},indent=2,ensure_ascii=False),encoding='utf-8')

summary={'observed_at':now,'draft_content_verified':True,'referee_keep_verified':True,'latest_draft':str(destination),'entries':len(bundle['entries']),'relations':len(bundle['relations']),'hook':hook_receipt,'progress':progress,'new_math_experiment_run':False,'previous_measurements_preserved':True,'ingestion_certified':False,'retrieval_certified':False,'original_problem_solved':False}
(JOB/'RESUME_VERIFICATION.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')
print('RESUME_COMPLETE',json.dumps({k:v for k,v in summary.items() if k not in ['progress','hook']},ensure_ascii=False))
