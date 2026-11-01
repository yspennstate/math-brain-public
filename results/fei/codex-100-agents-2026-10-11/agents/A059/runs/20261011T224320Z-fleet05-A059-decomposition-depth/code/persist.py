from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

root=Path(__file__).resolve().parents[1];agent=root.parents[1]
rid=root.name
def write(p,data):p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
statement=("For every finite balanced disjoint Boolean composition tree with literal leaves or a balanced stopping frontier, "
"delta(F)=sum_internal J(v)delta(g_v)+sum_terminal J(l)delta(Sub_l), and "
"sum_internal J(v)Lambda(g_v)<= (4+6/e)[delta(F)-sum_terminal J(l)delta(Sub_l)] in nats. "
"The exact first-charge factorization is Lambda(F)=sum_internal A(v)sum_i alpha_vi^2 ln(1/alpha_vi^2)W1(Sub_vi)+sum_terminal A(l)Lambda(Sub_l). "
"In contrast no finite K bounds sum_nonroot c J(c)Lambda(Sub_c) by K I(F): the rare-switch chain with depth d=2^(2k), r=3k, p=2^(-3k) has "
"I<=5/2 and that bank/I >=2^k(1-2^(-2k))/5 for k>=2. The same Boolean family satisfies H(F)<=6(I(F)-1) in bits.")
hyp=["Uniform finite cubes and normalized Fourier coefficients; Boolean sign functions.",
"Gate outputs and child/subformula outputs are balanced; physical child blocks are disjoint.",
"J(v) is the product of ancestor gate coordinate influences; A(v) is the product of ancestor singleton coefficients squared.",
"Lambda uses nats, H uses bits, delta=I-1; no depth or arity bound. No physical-restriction transfer is asserted."]
claim={"claim_id":"A059-GATE-VS-SUBFORMULA-DEPTH-LEDGER","version":1,"exact_statement":statement,"hypotheses":hyp,
"statement_sha256":hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
"contributors":["A059","Claude B12 lead: local Lambda/deficit lemma and target formulation"],
"proof_source":{"run":rid,"path":"PROOF.md","sections":[1,2,3,4,5]},
"proof_dependencies":[{"claim_id":"A056-DISJOINT-SUBSTITUTION","version":1,"acceptance":"A091 accepted at scope; exact identities also reconstructed here"},"Threshold paper 38pp Proposition 7.1; elementary Fourier/Boolean derivative, Bernoulli and logarithm inequalities"],
"review_records":[],"status":"PROVED_PENDING_INDEPENDENT_REVIEW","supersedes":[],
"refutes":["B12 lead v1 A059 test: universal sum_c J(c)Lambda(Sub_c)<=K I(F) for balanced disjoint trees"],
"first_unproved_line":None,"next_consumers":["A057","A060","A091","A090","A097","B12 lead","B20"]}
write(root/'CLAIMS.json',[claim])
progress={"protocol_revision":"2026-10-11-execution-v2","run_id":rid,"stream":"B12","packet_id":"A059",
"gap_id":"G-A059-DECOMPOSITION-DEPTH","attempt_id":"A059-depth-1","method":"Exact first-charge factorization, nonnegative deficit stopping identity, and analytic rare-switch counterfamily; source-bound A057 review",
"mathematical_delta":"Whole-subformula logarithm bank refuted with bounded influence and growing depth; local gate bank deficit-paid with 4+6/e nats, terminal reserve retained; physical-query transfer remains open.",
"deliverable_status":"COMPLETE_LOCAL_ARTIFACT","mathematical_status":"SCOPED_THEOREM_AND_HELPER_REFUTATION; FULL_FEI_OPEN",
"claim_versions_used":["A056-DISJOINT-SUBSTITUTION-v1","A057-COHERENT-ERASURE-SPLIT-v1 (reviewed, not required for new theorem)","A057-NONREUSING-ALPHA-LOG-PAYMENT-v1 (reviewed, not required for new theorem)","Claude B12 STREAM_NOTES v1 local Lambda lemma"],
"claims_created_or_changed":["A059-GATE-VS-SUBFORMULA-DEPTH-LEDGER-v1"],
"source_artifacts":["REPORT.md","PROOF.md","REVIEW_A057.md","CLAIMS.json","code/check.py","out/FROZEN_SPEC.json","out/validation.json","out/REVIEWS.json"],
"next_consumers":["A057","A060","A091","A090","A097","B12 lead","B20"],
"next_action":"Prove or obstruct actual-query remainder transfer to first-charge local gate budget after signed recentering, retaining terminal reserve; test rare-switch chains first.",
"stagnant_substantive_attempts":0,"blockers":["No universal transfer from physical restriction weights and biased descendants to local composition gate charges proved."],"packet_ids":["A059"]}
write(root/'PROGRESS.json',progress);write(root/'PACKET_DELTA.json',progress)
reviews=[]
for cid in ['A057-COHERENT-ERASURE-SPLIT','A057-NONREUSING-ALPHA-LOG-PAYMENT']:
    reviews.append({'claim_id':cid,'version':1,'reviewer':'A059','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent analytic Fourier-fiber reconstruction and scalar bounds; no borrowed test implementation','source':'REVIEW_A057.md','contributor_to_target':False})
write(root/'out/REVIEWS.json',reviews)
stamp=datetime.now(timezone.utc).isoformat()
(agent/'STATUS.md').write_text('STATE: A059 local theorem and counterfamily saved: gate log charges deficit-telescope; whole-subformula bank diverges; 252 exact checks PASS; A057 v1 independently accepted locally; full FEI OPEN.\nNEXT: A091/A090 review; A057 transfer recentered physical-query remainder to single-use local gate charges, retaining terminal reserve; test rare-switch chains first.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} | Stage {rid}: read protocol/board and new B12 notes; abandoned preliminary generic rare-leaf budget in favor of lead target. Independently reconstructed A057 v1 at scope. Proved local gate/terminal deficit ledger and exact root singleton first-charge identity. Refuted whole-subformula bank with r=3k,d=2^(2k) rare-switch chain; I tends to 1 but bank grows 2^k. Pilot 31 and main 252 exact checks PASS; physical biased-descendant transfer remains open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nA059 depth facts (PROOF.md): for balanced Boolean h, Lambda(h)<= (4+6/e)(I(h)-1) nats. Balanced-tree local gate charges J(v)Lambda(g_v) sum to at most that deficit budget, with explicit terminal reserve. Whole-subformula charges J(v)Lambda(Sub_v) need not: rare-switch chain d=2^(2k), r=3k has bank/I>=2^k(1-2^(-2k))/5 but I<=5/2 and H<=6(I-1) bits. Exact root first-charge identity uses ancestor singleton squares A(v) and downstream W1; each logarithm is introduced once. Do not replace an actual physical-query bank by this syntactic gate bank without a proved recentered transfer. A057 v1 accepted at balanced/finite physical-tree scope by independent reconstruction in REVIEW_A057.md.\n')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
expected=set(protocol['required_per_run']['progress_fields']);expected.discard('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((root/'PACKET_DELTA.json').read_text())==json.loads((root/'PROGRESS.json').read_text())
write(root/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_field_count':len(claim),'progress_field_count':len(progress),'compatibility_equal':True})
receipts=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        receipts.append({'path':str(p.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=agent/name;b=p.read_bytes();receipts.append({'path':'../../'+name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
write(root/'out/PERSISTENCE.json',{'created_utc':stamp,'local_readback':'PASS','mirror_verified':False,'receipts':receipts})
print(json.dumps({'status':'PASS','run':rid,'files_receipted':len(receipts),'schema':'exact field sets matched'}))
