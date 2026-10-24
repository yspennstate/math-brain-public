"""Record received scoped referee verdicts without promoting a live theorem."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
path = Path('~/brain_workers/w476/REVIEW.jsonl')
rows = [json.loads(s) for s in path.read_text(encoding='utf-8').splitlines() if s and 'w474-' in s]
assert {'w474-L1','w474-L2','w474-C1','w474-L3'} <= {r['claim_id'] for r in rows}
assert all(r['verdict'] in ('KEEP','KEEP_DEDUP') for r in rows)
receipt = {'source':str(path),'reviewer':'w476','rows':rows,
           'served_model_account_gate':'UNKNOWN','mathematical_scope':'Special cases and broad-bridge counterexample only; no C0052 solution.'}
(ROOT/'REFEREE_VERDICTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
claims = [json.loads(s) for s in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
for c in claims:
    if c['claim_id'] != 'w474-C2':
        c['independent_reviewer']='w475 scoped KEEP; w476 KEEP (L3 KEEP_DEDUP); served model/account gate UNKNOWN'
        c['review_receipt']=['PEER_VERDICTS.json','REFEREE_VERDICTS.json']
        c['mathematical_review_state']='scoped independently checked mathematics'
        c['promotion_state']='DRAFT; served provenance and coordinator gates pending'
(ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
life = json.loads((ROOT/'BUNDLE_LIFECYCLE.json').read_text(encoding='utf-8'))
life['reviewed']={'state':'L1-L3/C1 scoped mathematical KEEP by w475 and w476; served-identity gate UNKNOWN; source-card C2 proposal pending',
                 'referee':'w476','verdict_paths':[str(path),'~/brain_workers/w475/AUDIT_ROWS.jsonl']}
life['duplicate_handling']='Integrate L3 once; cite independent authors w474 and w475, as w476 KEEP_DEDUP instructs. w475 explicitly leaves the anchored card to w474.'
(ROOT/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(life,indent=2)+'\n',encoding='utf-8')
notes='''The submitted bundle is a frozen concept/DRAFT packet. The review-pending wording is its historical submission state. Current scoped mathematical verdicts are in REFEREE_VERDICTS.json and PEER_VERDICTS.json; account/model evidence remains UNKNOWN and no theorem promotion is authorized by those receipts alone.

Integrate the anchored contact formula once, crediting both w474 and w475. The independent matching claim is ~/brain_workers/w475/CLAIMS.jsonl, w475-C0052-contact-002. w475 explicitly leaves that anchored card to this bundle and submits different weighted-block/path concepts. Referee w476 verdict R9 is KEEP_DEDUP.

SOURCE_CARD_AUDIT.json is an additional scoped correction proposal for an existing unverified concept. It still needs its own source review. Create a corrected revision with provenance rather than altering an immutable object or preserving stale export digests. C0052 is not solved; current global openness is UNKNOWN.
'''
(ROOT/'INTEGRATION_NOTES.md').write_text(notes,encoding='utf-8')
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
report=report.replace("w475 supplied scoped KEEP for L1-L3/C1 after an independent initial contact derivation. w476's formal referee decision and served model/account evidence remain pending.","w475 and referee w476 supplied scoped mathematical KEEP for L1-L3/C1; w476 marks L3 KEEP_DEDUP and requires joint credit. Served model/account evidence remains UNKNOWN. The source-card correction C2 is a separate pending proposal.")
report=report.replace('mathematical review partial;','special-case mathematical review complete; served-provenance gate pending;')
report=report.replace('NEXT: w476 checks the proofs and source-card proposal; the next parent proof step','NEXT: coordinator verifies served provenance and the source-card proposal; the next parent proof step')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
packet=(ROOT/'REVIEW_PACKET.md').read_text(encoding='utf-8')
packet += '\nReceived: w475 scoped KEEP and w476 R1/R7/R8 KEEP plus R9 KEEP_DEDUP for L1/L2/C1/L3. See REFEREE_VERDICTS.json. Served identity gates remain UNKNOWN; C2 source-card proposal is pending. Submitted cards remain DRAFT concepts.\n'
(ROOT/'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
review=json.loads((ROOT/'REVIEW_FILES.json').read_text(encoding='utf-8'))
for name in list(review['files'])+['PEER_VERDICTS.json','REFEREE_VERDICTS.json','INTEGRATION_NOTES.md']:
    review['files'][name]={'path':str(ROOT/name),'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}
(ROOT/'REVIEW_FILES.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
with (ROOT/'RESULTS.jsonl').open('a',encoding='utf-8') as out:
    out.write(json.dumps({'row_id':'w474.S1.6','kind':'math-review-receipt','claim_ids':['w474-L1','w474-L2','w474-L3','w474-C1'],
                         'verdict':'KEEP; L3 KEEP_DEDUP','reviewers':['w475','w476'],
                         'evidence':'REFEREE_VERDICTS.json; PEER_VERDICTS.json','parent_problem_solved':False,
                         'served_model_account_gate':'UNKNOWN','source_card_C2':'pending proposal','ingested':False})+'\n')
print(json.dumps({'mathematical_verdicts':len(rows),'verdicts':[r['verdict'] for r in rows],
                  'submitted_concepts':life['submitted']['entries'],'served_gate':'UNKNOWN','ingested':False}))
