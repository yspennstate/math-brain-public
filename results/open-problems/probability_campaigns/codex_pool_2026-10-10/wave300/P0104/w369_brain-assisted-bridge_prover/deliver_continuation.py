"""Sequential statement/referee handoff to the two already named peers."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MESH = '~/<private-repo>/12_cognitive_architecture/agent_mesh'
sys.path.insert(0,MESH)
import team_comm

state_path = ROOT / 'CONTINUATION_SUBMISSION_STATE.json'
state = json.loads(state_path.read_text(encoding='utf-8'))
receipts_path = ROOT / 'CONTINUATION_COMMUNICATION_RECEIPTS.json'
receipts = json.loads(receipts_path.read_text(encoding='utf-8')) if receipts_path.exists() else []
connection = team_comm.Mesh(team_comm.DB,busy_timeout_ms=10000)


def save():
    receipts_path.write_text(json.dumps(receipts,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    state['communication_receipts'] = receipts_path.name
    state_path.write_text(json.dumps(state,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')


def send(peer,topic,body,flag):
    prior = next((row for row in receipts if row.get('peer') == peer and row.get('topic') == topic and row.get('success')),None)
    if prior:
        state[flag] = True
        save()
        print(json.dumps({'peer':peer,'reused_local_receipt':True,'message_id':prior['result']['message_id']}))
        return
    try:
        result = connection.send('w369',peer,topic,body,kind='message')
        receipt = {'peer':peer,'topic':topic,'success':True,'result':result}
        state[flag] = True
    except Exception as error:
        receipt = {'peer':peer,'topic':topic,'success':False,'error':str(error)}
    receipts.append(receipt)
    save()
    print(json.dumps(receipt,ensure_ascii=False))
    if not receipt['success']:
        raise RuntimeError(f'Peer handoff failed: {peer}')


try:
    send('w370','P0104-martingale-supplement-statement',
         'Statement only before proof-packet handoff: ~/brain_workers/w369/CONTINUATION_STATEMENT_FOR_ADVERSARY.md. '
         'Narrow claim clm-32b936f060: generic fourth-moment/square-function comparison and conditional lattice exposure reduction. '
         'Please make your independent attempt from the statement before reading CONTINUATION.md. '
         'No uniform lattice budget or one-third scaling is claimed; this continues the saved L5 cross/cubic gap.',
         'statement_delivered_to_adversary')
    send('w371','P0104-supplement-and-whole-card-scope-fix',
         'Your written KEEP L0-L5 is verified and saved in REVIEW_RECEIPTS.json. '
         'Your source FIX is applied: CORRECTION.json now selects the entire original statement and gives planar Z^2 scope, '
         'distribution hypotheses and the L^2 condition for variance. Please audit that whole-card revision. '
         'Supplement proof: ~/brain_workers/w369/CONTINUATION.md L6-L7, with REVIEW_PACKET.md and CONTINUATION_CLAIMS.jsonl. '
         'L6 gives 81-factor square-function comparisons and absolute 16/4 cross/cubic bounds; L7 identifies the exact conditional FPP criterion. '
         'Eight exact martingale cases pass; statement was delivered first to w370. '
         'Separate draft: '+state['inbox_path']+'. New lemmas/source revision await your audit. No lattice budget, KPZ solution or confirmed ingestion is claimed.',
         'proof_packet_delivered_to_referee')
finally:
    connection.close()

assert state['statement_delivered_to_adversary'] and state['proof_packet_delivered_to_referee']
status = (ROOT / 'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0] = 'STATE: NEEDS_REVIEW'
status[1] = 'NEXT: w371 audit L6--L7 and the whole-card scope fix; next proof step is to bound predictable-variance and jump-fourth budgets by Var(T_n)^2.'
status.append('2026-10-10 handoff: The L6--L7 statement reached w370 before the full supplement and whole-card source fix reached w371. CONTINUATION_COMMUNICATION_RECEIPTS.json records both message ids. Six original lemmas have independent KEEP; two supplement lemmas and the source-scope revision await review. Both inbox drafts are saved; integration/retrievability remain unconfirmed. STATE is NEEDS_REVIEW, not DONE; no P0104 solution is claimed.')
(ROOT / 'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
