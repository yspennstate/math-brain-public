"""Checkpoint the completed, measured, unaudited same-task packet."""
import datetime
import json
from pathlib import Path

root=Path(__file__).resolve().parent
def read(name):return json.loads((root/name).read_text(encoding='utf-8'))
handoffs=read('handoff_receipts.json')
assert len(handoffs)==3 and all(x['returncode']==0 for x in handoffs)
followup=read('followup_review_receipt.json')
integrator=read('source_integrator_handoff.json')
assert followup['returncode']==integrator['returncode']==0
assert read('final_progress_receipt.json')['returncode']==0
releases=read('claim_release_receipts.json')
assert releases[1]['returncode']==0
assert releases[0]['returncode'] in (0,4)  # Original claim's TTL expired before closing.
observed=read('brain_state_observation.json')
assert observed['submitted'] and observed['expected_entries']==12
for name in ('verification_receipt.json','patch_validation_receipt.json',
             'bundle_validation_receipt.json','followup_validation_receipt.json'):
    assert read(name)['failures']==0,name
route=read('route_receipt.json')
assert route['default_cli_complete_hypotheses'] and route['retained_unverified_statuses']
receipts=[read(name) for name in ('submission_receipt.json','followup_submission_receipt.json')]
assert all(r['submitted'] for r in receipts)
bundles=[json.loads(Path(r['draft_path']).read_text(encoding='utf-8')) for r in receipts]
entries=sum(len(b['entries']) for b in bundles)
relations=sum(len(b['relations']) for b in bundles)
assert (entries,relations)==(12,9)
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
assert len(claims)==len({c['claim_id'] for c in claims})==12
messages={x['to']:json.loads(x['stdout'])['message_id'] for x in handoffs}
followup_id=json.loads(followup['stdout'])['message_id']
integrator_id=json.loads(integrator['stdout'])['message_id']
source=read('SOURCE_STATUS.json')
source['review_handoffs']={**messages,'w383_followup':followup_id,'codex-01a12190_source':integrator_id}
source['independent_audit']='Original and follow-up proof packets delivered to w383; independent verdicts pending. C1 forwarded to integrator for a different-model source KEEP; no KEEP claimed.'
source['source_clarification']['review_route']={'supervisor':'claude-4a88bc43','integrator':'codex-01a12190',
    'message_id':integrator_id,'required_verdict':'different-model KEEP','verdict':'pending',
    'live_store_modified':False}
source['draft_entry_count']=entries
source['draft_relation_count']=relations
source['claim_row_count']=len(claims)
(root/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2),encoding='utf-8')
for c in claims:
    if c['claim_id']=='w381-C1':recipient,message='codex-01a12190',integrator_id
    elif c['claim_id']=='w381-R1':recipient,message='claude-4a88bc43',messages['claude-4a88bc43']
    else:recipient,message='w383',followup_id if c['claim_id'] in {'w381-L8','w381-L9'} else messages['w383']
    c['review_submission']={'recipient':recipient,'message_id':message,
                            'packet':'~/brain_workers/w381/REVIEW_PACKET.md'}
    c['audit_status']='submitted for review; independent verdict pending'
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
complete={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'state':'NEEDS_REVIEW',
    'claim_rows':len(claims),'draft_entries':entries,'draft_relations':relations,'consistency_checks':2388,
    'followup_numerical_check':False,'formal_check':False,'independent_proof_audit':False,
    'target_solved':False,'current_openness':'UNKNOWN','source_integrator_message':integrator_id,
    'referee_followup_message':followup_id,'brain_states':source['brain_states']}
(root/'completion_checks.json').write_text(json.dumps(complete,indent=2),encoding='utf-8')
status=(root/'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0]='STATE: NEEDS_REVIEW'
status[1]='NEXT: w383 audits L2--L5 and L8--L9; next proof step is comparing Var T(0,x) uniformly for n<=|x|<=2n under Uniform[1,2].'
status.append('2026-10-10: COMPLETE MEASURED PACKET: 12 claim rows, two submitted DRAFTs with 12 entries and 9 exact-support relations; 2,388 original consistency cases pass; one-query exact target hits 0 to 1; all four patch checks pass. L8/L9 have exact written proofs pending independent review, with no numeric/formal check claimed.')
status.append('2026-10-10: Original proof '+messages['w383']+'; continuation '+followup_id+'; source-to-integrator '+integrator_id+'. Latest exact-ID observation: ingested='+str(observed['ingested'])+', retrievable='+str(observed['retrievable'])+'; independent review pending. No live integration, source correction or recall deployment performed.')
status.append('2026-10-10: Hardest remaining target gap: matched global exponents for an actual iid undirected lattice law. Concrete next proof step: uniform two-sided variance power regularity for Uniform[1,2], with global wandering matching still required.')
status.append('2026-10-10: Final progress event logged. Own variance-regularity mesh claim released; original terminal-bias claim already expired (release returned no matching live claim). C1 source review remains with the integrator for different-model KEEP.')
(root/'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
print(json.dumps(complete,indent=2))
