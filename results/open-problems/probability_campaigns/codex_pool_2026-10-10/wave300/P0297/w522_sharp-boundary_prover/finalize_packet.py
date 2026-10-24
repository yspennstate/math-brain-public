"""Close only this author packet; preserve pending independent-review states."""
import ast
from datetime import datetime, timezone
import json
from pathlib import Path

root=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
source_path=root/'SOURCE_STATUS.json'
source=json.loads(source_path.read_text(encoding='utf-8'))
source['canonical_research_store']={
    'repository':'~/math-research-brain',
    'status':'Not verified: no current P0297 card or primary live-store database located by the narrow discovery searches.',
    'scope':'Exact P0297 logical-id search in named JSON/markdown formats; test, bank, blind, harness and audit paths excluded. Store-database discovery found only audit snapshots, which were not opened.',
    'limitation':'Current owner-retirement status remains unconfirmed. No exhaustive corpus, benchmark artifact, or audit-snapshot inspection is used as mathematical evidence.'}
source_path.write_text(json.dumps(source,indent=2)+'\n',encoding='utf-8')

claim_path=root/'MESH_CLAIM_RECEIPT.json'
claim=json.loads(claim_path.read_text(encoding='utf-8'))
claim.update(released=True,release_recorded_utc=now,
             release_receipt={'agent':'w522','released':1},
             release_command='agent_mesh.py release --agent w522 --resource file:~/math-brain-inbox/w522')
claim_path.write_text(json.dumps(claim,indent=2)+'\n',encoding='utf-8')

brain_path=root/'BRAIN_STATES.json'
brain=json.loads(brain_path.read_text(encoding='utf-8'))
brain['peer_handoffs']={
    'w523':{'state':'file handoff; peer unregistered in mesh','receipt':'HANDOFF_W523.json'},
    'w524':{'state':'file handoff; peer unregistered in mesh','receipt':'HANDOFF_W524.json'}}
brain['inbox_write_claim']={'claim_id':'clm-efffd203d8','state':'released after atomic draft submission'}
brain_path.write_text(json.dumps(brain,indent=2)+'\n',encoding='utf-8')

progress_path=root/'PROGRESS_EVENT.json'
progress=json.loads(progress_path.read_text(encoding='utf-8'))
progress['row']='S1.P0297.w522.C1'
progress['event']='P0297: source-normalization repair staged (64/64 errors to 0; known anchor 10 to 4); four boundary proofs and five-concept draft submitted; independent review pending.'
progress_path.write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')

with (root/'REPORT.md').open('a',encoding='utf-8') as stream:
    stream.write('\nPeer handoffs are saved on disk: w523 and w524 were unregistered in the mesh. The narrow canonical-repository lookup did not verify current retirement status. The inbox write claim was released after submission; no live archive, store, hook or progress-page change was made by w522.\n')
with (root/'ATTEMPT.md').open('a',encoding='utf-8') as stream:
    stream.write('\nCloseout: the canonical-repository lookup did not locate a current P0297 card or primary live-store path; discovered audit snapshots were not opened. Current owner-retirement status is unconfirmed. Both named peer deliveries failed due to unregistered recipients and are preserved as file handoffs. The submitted bundle remains concept/draft material; no independent keep, formal receipt, ingestion or retrieval is certified.\n')

# Serialization/source-code packaging checks only; never promote them to proof audit.
json_files=list(root.glob('*.json'))
for path in json_files:
    json.loads(path.read_text(encoding='utf-8'))
row_counts={}
for name in ('CLAIMS.jsonl','RESULT_ROWS.jsonl','HOOK_PROPOSAL.jsonl'):
    rows=[json.loads(line) for line in (root/name).read_text(encoding='utf-8').splitlines() if line]
    row_counts[name]=len(rows)
assert row_counts['CLAIMS.jsonl']==6 and row_counts['RESULT_ROWS.jsonl']==6
hook=json.loads((root/'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8'))
assert len(hook['text'])<=300
for path in root.glob('*.py'):
    ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
assert source['current_openness']=='UNKNOWN' and not source['original_target_solved']
assert brain['reviewed']['status']=='pending'
assert all(e['kind']=='concept' and e['proof_text'] is None for e in json.loads((root/'bundle_local_001.json').read_text(encoding='utf-8'))['entries'])
receipt={'at_utc':now,'json_files_valid':len(json_files),'row_counts':row_counts,
         'helper_sources_parse':True,'hook_characters':len(hook['text']),
         'review_state':'pending w524','scope':'Artifact packaging only; not an independent or formal mathematical proof receipt.'}
(root/'FINAL_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')

status_path=root/'STATUS.md'
status=status_path.read_text(encoding='utf-8')
assert status.startswith('STATE: WORKING\n')
lines=status.splitlines()
lines[0]='STATE: NEEDS_REVIEW'
lines[1]='NEXT: w524 independently audits C1 and L1-L4 in REVIEW_PACKET.md; next target-proof step is an independent median-LFPP crossing exponent estimate.'
lines.append('2026-10-10: Author deliverables complete and measured. Five concepts/six relations submitted to math-brain-inbox/w522/bundle_001.json; source repair and hook diffs staged; six claim/result rows saved. Both peers unregistered, file handoffs preserved. Canonical current status unconfirmed; original gap and UNKNOWN openness retained. Inbox claim released; PRIMARY_DIRECTIVE.md reread at closeout. Independent review, ingestion and retrieval remain unconfirmed.')
status_path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','verification':receipt,
                  'bundle':brain['submitted']['path'],'next':lines[1]},indent=2))
