from pathlib import Path
import json, hashlib
from datetime import datetime, timezone

run=Path(__file__).resolve().parents[1]
agent=run.parent.parent
root=agent.parent.parent
protocolpath=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocolpath.read_text(encoding='utf-8-sig'))
old=run.parent/'20261011T233317Z-account05-A066-semigroup-dissipation'
first=run.parent/'20261011T214539Z-account05-A066-semigroup-dissipation'
a088=root/'agents/A088/runs/20261012T024518Z-account05-A088-booleanity-referee'
a067=root/'agents/A067/runs/20261012T004014Z-account05-A067-hypercontractive-refinement'
checks=json.loads((run/'out/CHECK_FULL.json').read_text(encoding='utf-8'))
consumers=['B14','A067','A070','A064','A088','A094','B06','B20']
proof=str(run/'DERIVATION.md')
dep={'claim_id':'A066-HEAT-ENTROPY-IDENTITY','version':1,'proof_source':str(first/'DERIVATION.md'),'acceptance_scope':'Prior source-bound A067/A088 acceptance; finite-cube endpoint integrability and identity only.'}
component={'claim_id':'A066-POSITIVE-RESTRICTION-HEAT-LEDGER','version':1,'proof_source':str(old/'DERIVATION.md'),'acceptance_scope':'Only sections 1-3 all-block identity, singleton proofs, and exact character/tensor admission. Unqualified serialized block-tree price rejected; replaced by v2.'}
statements=[
 'For every Boolean sign on a finite uniform cube, with natural logarithms, K=(H_nat-p_empty ln(1/p_empty))/2=integral J, every physical block B obeys 2[K(f)-E_y K(f_y)]=M_B^++C_B^++ell_B. q_T=sum_{U subset B}p_{U union T}=E_y p_y(T), M_T=sum_U p_{U union T}ln(q_T/p_{U union T}), C_T=E_y p_y(T)ln(p_y(T)/q_T), plus omits T=empty, and ell_B=sum_{nonempty U subset B}p_U ln(1/p_U); all terms nonnegative. This identity telescopes for every finite adaptive block-query tree with terminal K retained. ONLY for singleton-query trees, the cumulative paid channel-plus-level charge is <=beta[I(root)-E I(leaf)], beta=2+2/e^2, because C_i^+<=2(Inf_i-p_{i}) and |hat f({i})|<=Inf_i. No such price is asserted for arbitrary block-query trees. Also 0<=B_nat-R_nat<=(1+2/e)I; R_nat=sum_i M_i^+, B_nat=sum_i H_nat(S_i|S_without_i). For F_m=y product_j g(x^(j)) on disjoint copies, R_nat(F_m)=m B_nat(g), I(F_m)=m I(g)+1. Hence the optimal universal constants for R_nat/I and B_nat/I coincide. A universal R_nat<=A I implies FEI bits constant (A+2)/ln2 via C018; A remains unproved.',
 'For every Boolean sign and physical block B, any singleton refinement querying exactly B with the same actual children satisfies C_B^++ell_B=P_ref+D_ref, D_ref=R_ref-M_B^+, where R_ref=sum_internal w M_i^+ and P_ref=sum_internal w(C_i^++ell_i)<= (2+2/e^2)I_B. D_ref is signed and must be retained in any block-tree payment. For f_n=1-2 indicator of one vertex, I=n2^(1-n), q=2^-n, whole-cube block M_B^+=C_B^+=0, ell_B/I=4(1-1/n)(1-q)ln2. A complete singleton refinement has R_ref/I=C_ref^+/I=[2-(4/n)(1-q)]ln2, L_ref/I=(4/n)[1-(n+1)q]ln2, P_ref/I=2(1-2q)ln2. Thus the block price tends to 4ln2, refined paid price to 2ln2, and retained transfer to 2ln2. At n=128, ell_B/I>11/4>2+2/e; appending an irrelevant coordinate produces the same obstruction with B a proper ambient subset. No universal price of the retained transfer is asserted.'
]
claims=[]
ids=['A066-POSITIVE-RESTRICTION-HEAT-LEDGER','A066-BLOCK-REFINEMENT-HEAT-TRANSFER']
for j,statement in enumerate(statements):
    c={'claim_id':ids[j],'version':2 if j==0 else 1,'exact_statement':statement,
       'hypotheses':['Finite uniform cube; Boolean outputs in {-1,1}','Natural logarithms; zero-mass log terms vanish','Actual physical restrictions; influence prices only for singleton queries unless explicit D_ref retained','Finite trees; terminal K retained'],
       'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
       'contributors':['account05/A066']+(['account05/A088 (v1 scope objection and countercertificate; no acceptance of v2 asserted)'] if j==0 else []),
       'proof_source':proof,
       'proof_dependencies':[dep,component] if j==0 else [{'claim_id':ids[0],'version':2,'proof_source':proof,'acceptance_scope':'Author-proved; pending independent review'}],
       'review_records':[{'reviewer':'A088','review_source':str(a088/'REPORT.md'),'reviewed_version':1,'verdict':'GAP_SCOPE_CLARIFICATION on v1; singleton components valid; new v2 not yet reviewed'}] if j==0 else [],
       'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[{'claim_id':ids[0],'version':1}] if j==0 else [],
       'refutes':[{'claim_id':ids[0],'version':1,'scope':'Serialized unqualified cumulative channel-plus-level <=(2+2/e) influence drop for all block-query trees','witness':'n128 Boolean point defect, whole relevant block; proper-block variant by dummy coordinate','source':str(run/'out/CHECK_FULL.json')}],
       'first_unproved_line':None,'next_consumers':consumers}
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    claims.append(c)
(run/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')

sources=[protocolpath,root/'BOARD.md',root/'claude/B14/STREAM_NOTES.md',agent/'STATUS.md',agent/'LEARNED.md',old/'DERIVATION.md',old/'CLAIMS.json',old/'code/check_restrictions.py',first/'DERIVATION.md',a088/'REPORT.md',a088/'CLAIMS.json',a088/'out/A066_BLOCK_SCOPE_CERTIFICATE.json',a067/'REPORT.md']
manifest=[]
for p in sources:
    data=p.read_bytes()
    manifest.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
(run/'out/SOURCES.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
(run/'out/V1_SCOPE_SOURCE.json').write_bytes((old/'CLAIMS.json').read_bytes())
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A066','gap_id':'G-A066-HEAT-INTEGRAL','attempt_id':'A066-joint-budget-scope-repair-03',
 'method':'Consume A088 scope objection; joint singleton channel/level debit; exact signed block refinement and all-n Boolean defect ledger',
 'mathematical_delta':'Correct v1 scope and sharpen singleton tree budget from 2+2/e to 2+2/e^2, a rigorous gain >0.46 nats per queried influence. Exact block transfer records conditional erasure instead of hiding it. 3908 exhaustive block/order cases and 128 compressed point defects checked; full FEI and universal C018/C019 payment open.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW','mathematical_status':'SCOPE_REPAIR_AND_JOINT_PAID_FRAGMENT_AUTHOR_PROVED; UNIVERSAL_ERASURE_PAYMENT_AND_FEI_OPEN',
 'claim_versions_used':[dep,component,{'claim_id':'A088-BLOCK-TREE-HEAT-BUDGET-OBSTRUCTION','version':1,'proof_source':str(a088/'REPORT.md'),'acceptance_scope':'Review objection consumed; n128 rational witness reconstructed locally, not an independent acceptance of our new claims.'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version']} for c in claims],
 'source_artifacts':['REPORT.md','DERIVATION.md','SPEC.json','code/check_joint.py','code/finalize.py','out/CHECK_PILOT.json','out/CHECK_FULL.json','out/SOURCES.json','out/V1_SCOPE_SOURCE.json','out/PERSISTENCE.json'],
 'next_consumers':consumers,'next_action':'A094 independently reconstruct beta and signed refinement; B20 substitute v2 singleton scope for v1 unqualified price. Price retained erasure/positive transfer with Boolean cancellation and one physical influence account, admitting arbitrary cores and retaining leaves.',
 'stagnant_substantive_attempts':0,'blockers':['No universal bound for retained conditional-erasure or positive block-refinement transfer; full FEI remains open.'],'packet_ids':['A066']}
fields={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==fields
for name in ['PROGRESS.json','PACKET_DELTA.json']:
    (run/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')

report='''# A066 B14: scope repair and a sharper singleton heat budget

## exact target, quantifiers, hypotheses and units

For every Boolean sign on every finite uniform cube, pay the physical singleton heat drop while retaining conditional erasure and terminal entropy. Natural logarithms throughout. The integral is K(f)=(H_nat(f)-p_empty ln(1/p_empty))/2, with J_f(t)=sum_S |S|p_S exp(-2t|S|)ln(1/p_S). Prior endpoint proof applies: for each finite f the integrand is bounded at zero and bounded by exp(-2t)J_f(0) at infinity. No dimension-independent integrable pointwise envelope is used. This stage repairs a scope error and proves a quantitative paid fragment; it does not prove FEI.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2; BOARD snapshot 2026-10-13 21:55 UTC; B14 STREAM_NOTES v2 (2026-10-11 23:25 UTC); own STATUS/LEARNED and prior heat/row derivations. A088 run 20261012T024518Z REPORT, claims and out/A066_BLOCK_SCOPE_CERTIFICATE.json: the unqualified v1 block-tree price is false, although the singleton proofs and all-block identity hold. A067 run 20261012T004014Z REPORT: its padding-access reserve is already handled and is not duplicated here. Source paths and byte hashes are in out/SOURCES.json. The stale lead target was completed in stage 2; protocol dispatch now consumes the useful A088 objection.

## complete derivation or exact first unsupported line

DERIVATION.md supplies the proof. For every singleton i, set d=Inf_i, p=hat f({i})^2. Deleting the empty residual row gives C_i^+<=2(d-p). Combining its debit with ell_i=p ln(1/p), using sqrt(p)<=d and maximizing 2x(ln(1/x)-1), gives C_i^++ell_i<=(2+2/e^2)d. This replaces the prior separate charge 2+2/e by beta=2+2/e^2, gaining 2/e-2/e^2>0.46 nats per queried influence. The improved price telescopes ONLY over singleton queries.

The all-block identity remains exact. Refining B into singleton queries gives C_B^++ell_B=P_ref+D_ref, where D_ref=R_ref-M_B^+ is signed and P_ref<=beta I_B. This explicitly retains the missing conditional-erasure charge. In the all-n Boolean point-defect family, original block cost/I tends to 4ln2, refined paid cost/I to 2ln2, and retained transfer/I to 2ln2. The n128 objection is reconstructed with ln2>842/1215 and e>8/3; adding one irrelevant coordinate shows that merely requiring a proper block is insufficient.

The first unsupported line is a universal influence payment for the retained singleton erasure bill (and actual terminal entropy), or equivalently universal R_nat<=A I. Prior exact character/tensor admission shows that this is the same optimal-constant obstruction as C018 erasure B<=K I. This stage neither drops the signed transfer nor asserts its universal price.

## executed validation with domain, arithmetic, commands and outputs

SPEC.json was saved before execution. Run from the agent folder: `python -X utf8 runs/20261013T215841Z-account05-A066-semigroup-dissipation/code/check_joint.py pilot`, followed by the same command with `full`. All Boolean truth tables through n=3, every nonempty block, every block ordering: 3908 cases, including 804 singleton root cases. Exact integer Walsh/Fraction arithmetic and canonical formal logarithms verify the block identity, physical influence drop and signed refinement; rigorously enclosed logarithms check the joint price. Compressed point-defect dimensions 1..128 and direct spectra dimensions 1..8 verify the all-n formulas in their finite domains. The universal all-n conclusion comes from the displayed geometric-series proof, not extrapolation. No symmetry reduction for exhaustive truth tables.

Full run: 40584 assertions passed in 5.2701 seconds; pilot 963 in 0.0420 seconds. Runtime numbers are observational only. The checker reuses the prior exact log/Walsh helper with SHA256 1329c2f63854214e2938d67704e8b0c48c0116ed3f414bb74b69b4392f032bbb. Logs use a positive 24-term atanh series and proved tail; e uses a factorial series and geometric tail; stored bounds are rounded outward to 80-bit dyadic rationals. The n128 strict rational gap matches A088's independent certificate exactly. Job memory estimate <80MB, so the >300MB memok trigger did not apply. No heavy or background jobs were launched.

## proof dependencies and changed downstream conclusions

A066-HEAT-ENTROPY-IDENTITY v1 supplies the finite heat identity and endpoint integrability. The old restriction-ledger v1 is used only at its valid block-identity, singleton-proof and arbitrary-core-admission components. Its serialized unqualified tree-budget clause is superseded by A066-POSITIVE-RESTRICTION-HEAT-LEDGER v2; the original is preserved and copied to out/V1_SCOPE_SOURCE.json. A088 supplied the scope objection and existing witness and is acknowledged as a diagnostic contributor; there is no claim that it has accepted v2. New signed transfer is A066-BLOCK-REFINEMENT-HEAT-TRANSFER v1, author-proved pending review.

B20 and downstream consumers must replace any use of the unqualified block-tree price by singleton-only v2 or retain D_ref. Majority/defected-address calibration v1 used only the unchanged block identity and remains valid at that dependency scope, as A088 recorded. Conditional direct heat FEI coefficient improves by 2/e-2/e^2 if the residual is paid; the stronger existing C018 implication (A+2)/ln2 is unchanged. No improved proved universal FEI constant is claimed.

## one next mathematical action and independent reviewer

Price the retained conditional-erasure/positive refinement transfer using full Boolean cancellation with one physical influence account; reject any candidate that loses arbitrary cores or terminal costs. A094 should independently reconstruct beta and signed refinement; A088 may review the new scalar strengthening but its supplied v1 scope correction is not counted as independent acceptance of the repaired version. B14/B20 receive source-bound substitution instructions through these files, with no messages or shared-index mutations by this worker.

## actual persistence receipts or precise save blocker

All four protocol files, DERIVATION.md, frozen SPEC.json, code and output certificates are saved in this run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. out/PERSISTENCE.json records reread SHA256/byte counts and JSON schema checks; each file is below 20MB. Local save is verified. Supervisor mirroring, central adoption, independent review of the new versions and downstream mathematical use are not asserted.

**Universal bridge:** This stage moves C019 stopping-tree payment's proved channel-plus-level fragment by replacing 2+2/e with 2+2/e^2, and repairs its block scope by an exact signed transfer into the same C018 conditional-erasure residual. It pays no universal amount of that residual: a dimension-independent bound for retained erasure (plus actual leaf entropy) remains exactly missing. NEXT attacks that unpaid universal account while admitting arbitrary Boolean cores, making it the shortest remaining route from this heat mechanism to full FEI; another isolated defect or majority result cannot close it.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
stamp='2026-10-13T21:58:41Z stage'
(agent/'STATUS.md').write_text('STATE: A066 stage 3 saved: v1 scope repaired in v2; singleton paid heat budget 2+2/e^2; exact signed block transfer; 40584 exact checks PASS; FEI OPEN; new review pending.\nNEXT: A094 reconstruct joint budget/transfer; B20 substitute singleton-only v2; pay retained C018/C019 erasure with arbitrary cores and terminal costs retained.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+': Consumed A088 scope objection; preserved old run, issued singleton-only ledger v2, proved joint beta=2+2/e^2, and exact block refinement transfer. Pilot/full passed (68/3908 block-order cases; full 40584 assertions in 5.2701s). Reconstructed n128 rational obstruction; closed all-n defect redistribution, including proper-block dummy guard. No universal erasure price or full FEI. Next is retained universal payment.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+': CORRECTION: prior serialized ledger v1 tree price must be read only for singleton queries; its unqualified all-block reading is false (A088 n128 point defect). v2 supersedes that scope. Joint singleton debit C_i^+<=2(d_i-p_i), ell_i=p_i ln(1/p_i), |hat f({i})|<=d_i gives beta=2+2/e^2, improving separate 2+2/e. For any block refinement, block paid cost=P_ref+(R_ref-M_B^+); the signed transfer is retained conditional erasure, not free. For point defects, block/I ->4ln2, refined paid/I ->2ln2, transfer/I ->2ln2. Appending a dummy coordinate makes the same obstruction a proper block. Universal C018/C019 residual remains unpaid; conditional direct heat coefficient improves, existing stronger C018 FEI implication unchanged.\n')

assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        data=p.read_bytes(); assert len(data)<20*1024*1024
        if p.suffix=='.json': json.loads(data.decode('utf-8-sig'))
        receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=agent/name; data=p.read_bytes()
    receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
assert len((agent/'STATUS.md').read_text().splitlines())==2
(run/'out/PERSISTENCE.json').write_text(json.dumps({'verified_at_utc':datetime.now(timezone.utc).isoformat(),'schema_checks':'Claims exact keys; progress exact keys; identical packet delta; required report headings and final bridge; all JSON parsed; STATUS two lines','local_saved':True,'mirror_verified':False,'new_independent_review':False,'files':receipts},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'saved':True,'run':str(run),'claim_versions':[(c['claim_id'],c['version']) for c in claims],'receipted_files':len(receipts),'full_assertions':checks['assertions']}))
