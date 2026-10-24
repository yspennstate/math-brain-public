"""Verify the resumed handoff against files and actual queue/event receipts."""
from pathlib import Path
import json

ROOT=Path('~')
JOB=Path(__file__).resolve().parent
states=json.loads((JOB/'BRAIN_STATES.json').read_text(encoding='utf-8'))
latest=Path(states['submitted']['path'])
local=JOB/'bundle_local_002.json'
assert latest.resolve().parent==(ROOT/'math-brain-inbox/w523').resolve()
assert latest.read_bytes()==local.read_bytes()
bundle=json.loads(latest.read_text(encoding='utf-8'))
assert len(bundle['entries'])==3 and len(bundle['relations'])==2
assert all(e['kind']=='concept' and e['proof_text'] is None for e in bundle['entries'])
assert all('review pending' not in e['statement'] and 'audit pending' not in e['statement'] for e in bundle['entries'])
assert states['reviewed']['state'] is True
assert states['ingested']['state'] is False and states['retrievable']['state'] is False
receipt=json.loads((JOB/'INDEPENDENT_REVIEW_RECEIPT.json').read_text(encoding='utf-8'))
assert {r['claim'] for r in receipt['verdicts']}=={'P0297-w523-L1-L2','P0297-w523-C3'}
assert all(r['verdict']=='KEEP' and r['independent_reviewer']=='w524' for r in receipt['verdicts'])
claims=[json.loads(x) for x in (JOB/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
checked=[c for c in claims if c['id'] in {'P0297-w523-L1','P0297-w523-L2','P0297-w523-C3'}]
assert len(checked)==3 and all(c['status']=='independently checked proof' and c['independent_reviewer']=='w524' for c in checked)

hook=json.loads((JOB/'HOOK_SUBMISSION_RECEIPT.json').read_text(encoding='utf-8'))
proposal=Path(hook['path'])
assert proposal.resolve().parent==(ROOT/'primary_directive/hooks1000/proposals').resolve()
hook_lines=[json.loads(x) for x in proposal.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
assert sum(x.get('id')==hook['id'] for x in hook_lines)==1

progress=json.loads((JOB/'PROGRESS_POST_RECEIPT.json').read_text(encoding='utf-8'))
assert progress['returncode']==0 and progress['stdout'].strip()=='logged'
events=ROOT/'primary_directive/ledger/events.jsonl'
with events.open('rb') as f:
    f.seek(max(0,events.stat().st_size-131072))
    tail=f.read().decode('utf-8',errors='replace').splitlines()
own=[]
for line in tail:
    try:
        event=json.loads(line)
    except json.JSONDecodeError:
        continue
    if event.get('agent')=='w523' and event.get('row')=='S1.P0297.w523.C3' and 'bundle_002' in json.dumps(event):
        own.append(event)
assert own,'The actual progress event was not found in the bounded tail; no completion claim.'
progress['event_log_path']=str(events)
progress['event_record_verified']=own[-1]
(JOB/'PROGRESS_POST_RECEIPT.json').write_text(json.dumps(progress,indent=2,ensure_ascii=False),encoding='utf-8')
event_metadata=json.loads((JOB/'PROGRESS_EVENT.json').read_text(encoding='utf-8'))
event_metadata['state']='posted; actual event record independently read'
event_metadata['receipt']='PROGRESS_POST_RECEIPT.json'
(JOB/'PROGRESS_EVENT.json').write_text(json.dumps(event_metadata,indent=2),encoding='utf-8')

coord=json.loads((JOB/'RESUME_COORDINATION_RECEIPTS.json').read_text(encoding='utf-8'))
queued=[]
for r in coord['peer_routes']:
    assert r['returncode']==0
    metadata=json.loads(r['stdout'])
    assert metadata['fanout']==1 and metadata['to'] in {'w522','w524'}
    assert metadata['message_id']
    queued.append({'to':metadata['to'],'message_id':metadata['message_id'],'state':'queued; recipient consumption not certified'})
assert {q['to'] for q in queued}=={'w522','w524'}
for q in queued:
    path=JOB/f"HANDOFF_{q['to'].upper()}.json"
    data=json.loads(path.read_text(encoding='utf-8'))
    data.update(status=q['state'],message_id=q['message_id'],latest_draft=str(latest),independent_review_receipt=str(JOB/'INDEPENDENT_REVIEW_RECEIPT.json'))
    data['own_new_claim']='P0297-w523-C3; scoped independent KEEP by w524 received'
    data['request']='Forward the reviewed concept draft for validating-coordinator ingestion; original LFPP normalization exponent is not determined.'
    path.write_text(json.dumps(data,indent=2),encoding='utf-8')

measurement=json.loads((JOB/'MEASUREMENTS.json').read_text(encoding='utf-8'))
assert measurement['evaluations']==165 and json.loads((JOB/'COMPUTE_GATE.json').read_text(encoding='utf-8'))['status']=='consumed'
result={'command':'python -X utf8 verify_resume.py','draft_path':str(latest),'draft_entries':3,'draft_relations':2,'named_referee_keeps_confirmed':True,'own_checked_claim_rows':3,'progress_event_record_found':True,'hook_proposal_present_once':True,'peer_handoffs':queued,'prior_math_measurements_preserved':True,'new_math_experiment_run':False,'ingestion_verified':False,'retrieval_verified':False,'original_target_solved':False,'all_resume_checks_passed':True}
(JOB/'RESUME_FINAL_RECEIPT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
with (JOB/'RESUME_ROWS.jsonl').open('a',encoding='utf-8') as f:
    f.write(json.dumps({'id':'P0297-w523-resume-03','verdict':'REVIEWED_HANDOFF_VERIFIED','receipt':'RESUME_FINAL_RECEIPT.json','reviewed_claims':3,'draft_entries':3,'relations':2,'progress_record_verified':True,'hook_proposal_present_once':True,'peer_messages_queued':2,'ingestion_verified':False,'retrieval_verified':False})+'\n')
print(json.dumps(result,indent=2))
