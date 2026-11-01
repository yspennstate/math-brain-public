"""Record the completed, measured review stage; leave integration to reviewers."""
import difflib
import json
import pathlib
import subprocess

root=pathlib.Path(__file__).resolve().parent
validation=json.loads((root/'packet_validation.json').read_text(encoding='utf-8'))
send=json.loads((root/'referee_send_receipt.json').read_text(encoding='utf-8'))
assert validation['exact_patch'] and validation['acyclic']
assert send['delivered']
details=json.loads(send['stdout'])
message_id=details['message_id']
claim=json.loads((root/'CLAIM_RECEIPT.json').read_text(encoding='utf-8'))
run=subprocess.run(['python','-X','utf8',
    '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py',
    'release','--agent','w513','--all'],capture_output=True,text=True,encoding='utf-8',errors='replace')
claim['released']=run.returncode==0
claim['release_receipt']=dict(exit_code=run.returncode,stdout=run.stdout,stderr=run.stderr)
(root/'CLAIM_RECEIPT.json').write_text(json.dumps(claim,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

hook_text=(root/'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8')
hook=json.loads(hook_text)
assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when']
path='~/primary_directive/hooks1000/proposals/math-w513.jsonl'
patch=''.join(difflib.unified_diff([],hook_text.splitlines(keepends=True),fromfile='a/'+path,tofile='b/'+path))
(root/'patches/02_p0162_quantifier_hook.diff').write_text(patch,encoding='utf-8')
report=(root/'REPORT.md').read_text(encoding='utf-8')
old='Peer sending failed because no team membership was present and w514 was unregistered; a statement-first durable outbox is saved. Local hook/progress proposals await shared publication under the worker write boundary.'
new=(f'The complete referee packet was delivered to active w515 as {message_id}; referee_send_receipt.json records fanout 1 and inserted 1. '
     'The initial adversary statement remains queued after the earlier unregistered-recipient failure; w514 STATUS independently records a first bent-selector attempt saved before paired proof access. That is independence evidence, not an audit. '
     'Local hook/progress proposals await shared publication under the worker write boundary. The proposed hook has a live-path unified diff in patches/02_p0162_quantifier_hook.diff; reviewers can publish it after the hook audit.')
assert old in report
(root/'REPORT.md').write_text(report.replace(old,new),encoding='utf-8')
review=(root/'REVIEW_PACKET.md').read_text(encoding='utf-8')
review=f'Referee delivery: {message_id} to active w515; one message inserted. Independent audit remains pending.\n\n'+review
(root/'REVIEW_PACKET.md').write_text(review,encoding='utf-8')
rows=[json.loads(line) for line in (root/'PEER_OUTBOX.jsonl').read_text(encoding='utf-8').splitlines() if line]
for row in rows:
    if row['sequence']==2:
        row['state']='included in delivered complete-review packet'
        row['message_id']=message_id
(root/'PEER_OUTBOX.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
status=(root/'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0]='STATE: NEEDS_REVIEW'
status=[('NEXT: w515 audits L6 balanced composition and the empty-selector sector; after independent keeps, the coordinator submits the staged draft. The general aggregate entropy budget stays open.' if line.startswith('NEXT:') else line) for line in status]
status+=['2026-10-10: Delivered the complete review packet to w515 as '+message_id+'. Saved six typed DRAFT nodes, six supported relations, eight claim rows, the exact general gap, and two unified diffs. Draft is complete .part only; submitted/reviewed/ingested/retrievable remain false.',
         '2026-10-10: Final checks: 768 exhaustive three-bit splits passed; rare-switch m=10 ratio 14.323621; nine-bit family H/I=2.177873, composition residual 4.44e-16; final arithmetic runtime 0.048 s. Packet shape, acyclic dependencies and exact patch/staged bytes validated. Own proof is not an independent audit.',
         '2026-10-10: Narrow inbox claim '+claim['claim_id']+' released='+str(claim['released'])+'. Shared hook/progress publication is staged locally under the write restriction. No live store or global recall control changed.']
(root/'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
print(json.dumps(dict(state='NEEDS_REVIEW',referee='w515',message_id=message_id,
    claim_released=claim['released'],packet='REVIEW_PACKET.md',draft_submitted=False,
    independently_audited=False,live_integration=False)))
