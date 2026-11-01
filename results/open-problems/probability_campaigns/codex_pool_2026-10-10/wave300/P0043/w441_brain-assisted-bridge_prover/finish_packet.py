"""Save final receipts and set NEEDS_REVIEW only after the deliverables pass."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent

def save(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    schema=json.loads((ROOT/'DRAFT_SCHEMA_CHECK.json').read_text(encoding='utf-8'))
    assert not schema['errors'] and schema['database_open_guard']
    state=json.loads((ROOT/'BUNDLE_STATE.json').read_text(encoding='utf-8'))
    assert state['submitted'] and state['prepared']
    submitted=Path(state['submission_path'])
    assert submitted.read_text(encoding='utf-8')==(ROOT/'drafts'/'bundle_001.json').read_text(encoding='utf-8')
    claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    assert len(claims)==6 and len({row['claim_id'] for row in claims})==6
    allowed={'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
    for row in claims:
        assert row['status'] in allowed
        assert all(k in row for k in ('statement','assumptions','source','proof','independent_reviewer','remaining_gap'))
        assert row['status']!='independently checked proof'
    check=json.loads((ROOT/'MATH_CHECKS.json').read_text(encoding='utf-8'))
    assert check['exact_joint_configurations']==4416
    guard=json.loads((ROOT/'GUARD_CHECKS.json').read_text(encoding='utf-8'))
    assert guard['after']['invalid_candidates_allowed']==0
    review=json.loads((ROOT/'REVIEW_STATE.json').read_text(encoding='utf-8'))
    review['w443']={'status':'direct delivery failed: unregistered recipient','packet':'REVIEW_PACKET.md','fallback_supervisor':'claude-4a88bc43','fallback_message_id':'msg-781cf17150','fallback_delivery':'inserted; recipient active; acknowledgment not awaited'}
    review['w442']['complete_packet_message']='msg-5fe14d634e'
    save(ROOT/'REVIEW_STATE.json',review)
    save(ROOT/'HANDOFF.json',{'worker':'w441','referee':'w443','packet':str(ROOT/'REVIEW_PACKET.md'),'direct_referee_delivery':'recipient w443 is not registered','supervisor_message_id':'msg-781cf17150','supervisor':'claude-4a88bc43','source_status':'UNKNOWN; recent exact-scope proof claim not independently verified here','remaining_target_gap':'Bernoulli-specific contradiction for critical clusters of zero anchored expansion','next':'w443 audit L002-L006 and w442 C003; save exact assumptions and verdicts before promoting or ingesting verified claims'})
    measurements=json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
    measurements['draft_schema']=schema
    save(ROOT/'MEASUREMENTS.json',measurements)
    statement=(ROOT/'STATEMENT.md').read_text(encoding='utf-8')
    statement=statement.replace('Source-level verification is in progress.','The scope was checked against Hutchcroft (2016), Conjecture 1.1, and the 24 September 2026 primary manuscript, Theorem 1.1.')
    statement=statement.replace('This is a candidate reconstruction, not a certified current open problem.','The exact statement is recovered; current openness is UNKNOWN because a recent exact-scope proof claim has not been independently verified here.')
    statement=statement.replace('NEXT: Confirm original primary-source statement and current status; communicate this statement to w442.','Statement-only first delivery to w442: msg-ad5f36607f, before proof-route sharing. NEXT: w443 audit the saved conditional lemmas and retain the full-target gap.')
    (ROOT/'STATEMENT.md').write_text(statement,encoding='utf-8')
    report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
    if 'Final handoff:' not in report:
        report += '\nFinal handoff: the eight-entry/five-relation DRAFT passed the actual integrator schema reader with database opens disabled and was submitted atomically. Direct delivery to w443 failed because that recipient is unregistered. Supervisor claude-4a88bc43 received request msg-781cf17150 with the complete packet. No acknowledgment was awaited.\n'
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    pending=ROOT/'MEASUREMENTS_PENDING.md'
    text=pending.read_text(encoding='utf-8')
    if 'Resolved:' not in text:
        pending.write_text(text+'\nResolved: measured fallback and guard receipts are complete in MEASUREMENTS.json, MATH_CHECKS.json, GUARD_CHECKS.json and DRAFT_SCHEMA_CHECK.json. This earlier note is retained as a checkpoint.\n',encoding='utf-8')
    status=(ROOT/'STATUS.md').read_text(encoding='utf-8')
    lines=status.splitlines()
    lines[0]='STATE: NEEDS_REVIEW'
    lines[1]='NEXT: w443 check L002 rational-q/Tonelli, L006 logarithmic inequality and w442 C003; supervisor has the complete packet because direct w443 delivery failed.'
    status='\n'.join(lines)+'\n'
    status+='2026-10-10: COMPLETE AND MEASURED. Six exact claim rows, eight DRAFT nodes, five quoted-end edges, proof checks and bounded guard proposal saved. Schema passed with database opens disabled; DRAFT atomically submitted. w443 unregistered; supervisor request msg-781cf17150 delivered. Full target unproved in this packet; no ingestion/retrievability or production improvement claimed.\n'
    (ROOT/'STATUS.md').write_text(status,encoding='utf-8')
    print(json.dumps({'state':'NEEDS_REVIEW','claims':6,'schema_errors':0,'draft_submitted':True,'supervisor_handoff':'msg-781cf17150','full_target_proven':False},indent=2))

if __name__=='__main__':main()
