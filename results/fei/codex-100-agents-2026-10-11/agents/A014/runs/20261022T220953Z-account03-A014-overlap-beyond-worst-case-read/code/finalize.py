from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
old=R.parent/'20261014T054454Z-account05-A014-overlap-beyond-worst-case-read'
now=datetime.now(timezone.utc).isoformat()
def read(p):return p.read_text(encoding='utf-8-sig')
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,v):write(p,json.dumps(v,indent=2,ensure_ascii=False)+'\n')
full=json.loads(read(R/'out/check.json'));pilot=json.loads(read(R/'out/pilot.json'))
assert full['graphs']==249 and full['queries']==1233 and full['boundary_pairs']==256
assert full['elapsed_seconds']<300 and pilot['elapsed_seconds']<60
parent_claim=json.loads(read(old/'CLAIMS.json'))[0]
new_statement=('For every indicator C(x,y) on any finite uniform cube, s=E C in (0,1), f=1-2C, v=4s(1-s), '
'write c_b(T) for its two normalized Fourier rows. The law R(T,xi)=(c_0(T)^2+c_1(T)^2)/(4s) is normalized, '
'r=R(empty) lies in [s/2,1/2], and the true blocker spectrum is at most 2R. '
'Let P be the output spectrum conditioned nonempty, Rstar=R conditioned nonempty, and L=2(1-r)/(1-s)>1. '
'For every fixed probability q positive on support(Rstar), S=(L Rstar-P)/(L-1) is a probability and '
'D(P||q)=L D(Rstar||q)-(L-1)D(S||q)+L JS_(1/L)(P,S). '
'For Q(empty)=1-v and Q(A)=v q(A) otherwise, '
'0<=CE(f,Q)-H(f)<=8s(1-r)D(Rstar||q)+(3+log2(e))I(f)<8s(1-r)D(Rstar||q)+(9/2)I(f). '
'No disjointness, nesting, separator or maximum-read bound is needed. Constants use the empty point mass. '
'If q=M/Z is an occupation reference, the full +v log2 Z term remains. '
'For the triangle independent-set blocker queried at any vertex, s=1/2, r=5/16, L=11/4, I=3/2, '
'P has four atoms 1/4 and Rstar has atom 5/11 at the queried singleton and six atoms 1/11. '
'For any c<11/4 and finite K, positive fixed references q exist with D(P||q)>c D(Rstar||q)+K I. '
'This refutes coefficient-one arbitrary-reference transport, not occupation-specific transport or FEI. '
'The frozen lambda=1/Delta occupation law on all 249 labelled connected cut-free graphs on 3,4,5 vertices '
'satisfies the displayed transport bound for all 1233 queried vertices by exact rational interval checks. '
'Inherited row KL and complete terminal costs remain unpaid universally.')
statement=parent_claim['exact_statement']+' ADDITION AT VERSION 5: '+new_statement
claim={k:parent_claim[k] for k in parent_claim}
claim.update(version=5,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 hypotheses=parent_claim['hypotheses']+['New transport: arbitrary indicator on a finite uniform cube, 0<s<1; bits; fixed complete nonempty reference positive on Rstar support.','Triangle lower bound varies arbitrary positive reference, not the fixed occupation law; all queried and private coordinates relevant.'],
 proof_source={'prior_version_source':str(old/'CLAIMS.json'),'prior_version_sha256':hashlib.sha256((old/'CLAIMS.json').read_bytes()).hexdigest(),'new_proof':str(R/'DERIVATION.md'),'finite_certificate':str(R/'out/check.json'),'locators':['Equations (1)-(6)','A relevant-query obstruction']},
 proof_dependencies=[{'claim_id':parent_claim['claim_id'],'version':4,'scope_used':'Prior exact occupation implementation and complete normalization; earlier bundled statements retained with earlier review status.'}],
 review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[{'claim_id':parent_claim['claim_id'],'version':4}],
 refutes=parent_claim['refutes']+[{'statement':'For arbitrary complete q, D(P||q)<=D(Rstar||q)+K I with universal finite K','witness':'triangle blocker with q_epsilon({y})=epsilon and remaining q proportional to Rstar; necessary coefficient 11/4','scope':'arbitrary-reference transport only; not the frozen occupation reference'}],
 first_unproved_line='Pay 8s(1-r) D(Rstar||q) and all inherited terminals from genuinely unused SAME original influence reserve, without renewing the additive allowance at successive queries.',
 next_consumers=['A008','A009','A015','A086','A094','B03'])
dump(R/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B03','packet_id':'A014',
'gap_id':'A014-ARBITRARY-OVERLAPPING-BLOCKER-REFERENCE-COST','attempt_id':'A014-stage17-nonseparating-row-KL',
'method':'Exact row mixture domination, complementary-law KL identity, edge-isoperimetric additive payment, triangle reference obstruction, bounded exact graph certificates',
'mathematical_delta':'Removed separator/disjoint-private hypotheses for row conversion; all reference debt retained with coefficient 8s(1-r); additive <9I/2. Triangle forces conditional debt amplification >=11/4 for arbitrary references. No universal FEI claim.',
'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_PROOF_AND_EXACT_FINITE_CERTIFICATE; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
'claim_versions_used':[{'claim_id':parent_claim['claim_id'],'version':4}],
'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':5}],
'source_artifacts':[str(old/'REPORT.md'),str(old/'code/check.py'),str(R/'DERIVATION.md'),str(R/'out/check.json')],
'next_consumers':['A008','A009','A015','A086','A094','B03'],
'next_action':'Price the weighted same-reference row KL on a non-separator graph family using genuinely unused original influence, with full terminals and old debit retained; independently review triangle sharpness and isoperimetry conversion.',
'stagnant_substantive_attempts':0,'blockers':['Universal occupation row/reference cost unpaid','Independent review and supervisor remote copy unverified','Lean compute admission held before compiler launch'], 'packet_ids':['A014']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report=f'''# A014 stage 17: non-separating row KL transport

## exact target, quantifiers, hypotheses and units

For every finite uniform Boolean blocker C(x,y), remove the separator assumption from the exact row-reference conversion, with every reference cost retained. Bits throughout; f=1-2C, s=E C, v=4s(1-s). For 0<s<1 and any fixed nonempty reference q positive on the incoherent row support, the complete output reference satisfies CE-H <=8s(1-r)D(Rstar||q)+(3+log2(e))I <8s(1-r)D(Rstar||q)+9I/2. This pays conversion only. The full FEI conjecture and the unrestricted linear-hypergraph target remain OPEN.

## sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2; BOARD dated 2026-10-22 22:07 UTC, B03 section; B03 lead STREAM_NOTES v2; A014 STATUS, LEARNED, prior stage-5 REPORT, CLAIMS and exact checker. The source scanner read and hashed the requested campaign README, CURRENT_STATUS, registries, packet and next-action indices, plan TeX, supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and all four supplied paper text versions, inspecting B03/C020 locators. These broader sources were inventoried for scope, not independently re-audited. C020 remains the whole-set witness target. Math recall returned neighboring material, no supporting occupation theorem; none is used as authority. The previous exact occupation implementation is the only substantive inherited code dependency. No novelty claim or new external literature claim is made.

## complete derivation or exact first unsupported line

DERIVATION.md equations (1)-(6) give the full proof. Normalized rows obey P_C<=2R on the SAME remaining cube without private factorization. Conditioning gives P<=L Rstar, L=2(1-r)/(1-s). The complementary probability S gives the exact signed KL identity, retaining -(L-1)D(S||q). Edge isoperimetry and Poincare pay the additive binary-label term from <9I/2 of the same physical influence. The log Z normalizer remains in complete CE. Constant outputs and zero rows are handled explicitly.

The relevant triangle query gives an actual monotone blocker with L=11/4 and exact fixed masses. For positive references concentrating a vanishing epsilon at one saturated atom, every smaller inherited-KL coefficient fails with any finite additive K I. This is an obstruction to arbitrary-reference coefficient-one transport, not a FEI counterexample and not an occupation-specific obstruction.

First unsupported line: pay 8s(1-r)D(Rstar||q) PLUS complete inherited terminals from unused ORIGINAL influence after old bookings. Applying this theorem repeatedly with a new 9I/2 allowance would double-spend; no such iteration is claimed.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes all computation. The first pilot reached graph assertions but failed to persist because out/ had not been created; out/README.txt records the error. The same unchanged pilot was retried after creating that directory. Successful pilot: {pilot['labelled_candidates']} labelled candidates, {pilot['graphs']} triangle graph, {pilot['queries']} queries, 256 arbitrary two-bit row pairs, {pilot['assertions']} assertions, {pilot['elapsed_seconds']:.6f} seconds.

Full: {full['labelled_candidates']} labelled candidate graphs on n=3,4,5, selecting ALL {full['graphs']} connected graphs with no cut vertex, {full['queries']} queried vertices and {full['all_nonempty_sets']} graph/nonempty-set pairs; 256 arbitrary row pairs include zero, constant, identical and nonnested rows. No symmetry reduction. {full['assertions']} exact assertions PASS in {full['elapsed_seconds']:.6f} seconds. Integer FWHT, rational mass, exact independently convolved occupation factors, and outward rational logarithm intervals from the prior pinned helper are used. All probabilities, nonempty normalizers, pointwise domination, complementary probabilities, KL identity intervals and additive/final payment signs are checked. The finite run validates these frozen references; no all-graph occupation cost theorem is inferred.

Commands from A014: `python -X utf8 runs/{R.name}/code/check.py --pilot` and the same without --pilot. Outputs: out/pilot.json, out/check.json and out/checkpoint.json. Estimated memory 100 MB; no >300 MB job, memory gate or GPU was needed. The full mathematical run stayed within its 300-second frozen cap. Shell startup delays are separate from the recorded checker elapsed time.

Lean command attempted: `python -X utf8 lean_check.py --stmt "example (a b : ℝ) : (a + b)^2 ≤ 2 * (a^2 + b^2) := by nlinarith [sq_nonneg (a-b)]"`. Admission returned SETUP_UNVERIFIED (hung window or under 5500 MB free); no compiler process started, no retry. Rung: proof with exact finite certificates, NOT Lean-checked, pending independent review.

## proof dependencies and changed downstream conclusions

A014 bundled interface advances from version 4 to 5 rather than opening another broad candidate. The new row transport and triangle obstruction are proved from explicit finite probabilities and elementary Fourier identities. The occupation formula is inherited from stage 5, whose source-bound queue/subprobability theorem still has its existing review status. Prior claims are retained with their original dependencies. The former disjoint-private separator requirement is removed for CONVERSION; constructing a cheap reference is still unpaid. The factor-one inherited KL repair is explicitly refuted for arbitrary positive references, including a relevant triangle query.

## one next mathematical action and independent reviewer

Use the same normalized occupation reference to pay its weighted row KL on one non-separator family from a demonstrably unused original influence account, retaining both terminals and any old debit. A008/A009 should audit occupation support and complete normalization; A015 should stress the leafless shared-core debt; A086/A094 should reconstruct the exact KL identity, the isoperimetric payment and the triangle coefficient obstruction. No review messages were sent and no acceptance is asserted.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved locally with the derivation, frozen spec, code and exact outputs. out/RECEIPTS.json checks protocol key sets, equality of progress copies, statement hash and SHA256/size of local artifacts. Rolling STATUS has two lines; WORKLOG and LEARNED are updated. Independent review, supervisor copy, GitHub persistence, mirror verification and downstream adoption remain unverified. Wake flagged stale personal-context notes; they were not used. No trading process, external message, git command, GPU, background service or deletion was initiated.

## Universal bridge

C020 advances by a complete non-separator conversion inequality with inherited row KL explicit, together with a relevant Boolean obstruction proving that coefficient-one arbitrary-reference transport cannot close the gap. The additive cost is <9I/2; no full-FEI constant is reduced because the weighted occupation row debt and old terminal costs remain unpaid. NEXT targets precisely that remaining debt on a genuinely overlapping component using one unused original influence account. This is the shortest surviving route here toward full FEI because it tests the cost required by the universal whole-set code, rather than adding another class whose entropy is already paid by factorization.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: A014 stage17 saved: separator-free inherited row-KL conversion <9I/2; triangle requires coefficient 11/4; '+str(full['assertions'])+' exact assertions PASS; review pending; FEI OPEN.\nNEXT: Pay weighted SAME occupation row KL from unused ORIGINAL influence with full terminals/old debit; A008/A009/A015 consume, A086/A094 review.\n')
for filename,text in [('WORKLOG.md',f'\n{now} Stage17: removed separator/disjoint-private assumptions for row conversion; full inherited row debt retained; relevant triangle rules out coefficients below11/4 for arbitrary references. Pilot {pilot["assertions"]}, full {full["assertions"]} exact checks,249 graphs/1233 queries; first pilot output-directory error repaired without changing domain. Lean held before compile. Universal occupation payment and full FEI remain open.\n'),('LEARNED.md','\nStage17: for any indicator C split on one uniform bit, R(T,xi)=(c0(T)^2+c1(T)^2)/(4s), r in[s/2,1/2], P_C<=2R, and conditioned P<=L Rstar with L=2(1-r)/(1-s). For every complete reference q positive on Rstar, full output CE-H<=8s(1-r)D(Rstar||q)+(3+log2(e))I<weighted debt+9I/2. This is conversion only, with +v log Z retained. Exact identity subtracts (L-1)D(S||q), S=(LRstar-P)/(L-1); do not discard signed credit before it is needed. Triangle independent-set blocker: s1/2,r5/16,L11/4,I3/2; P has four1/4 atoms,Rstar has5/11 at queried singleton and1/11 at six others. Vanishing q at a saturated singleton forces inherited KL multiplier at least11/4 for arbitrary references, even nested rows and relevant query. This does not refute occupation-specific references or FEI. Do not renew the additive allowance at every query.\n')]:
 p=A/filename;write(p,read(p)+text)
protocol=json.loads(read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')))
expected_progress={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert len(read(A/'STATUS.md').splitlines())==2
receipts={'saved_at_utc':now,'protocol_fields_pass':True,'progress_delta_equal':True,'statement_sha256_pass':True,'independent_review':'pending','remote_copy':'unverified','lean':'SETUP_UNVERIFIED; no compiler started','files':[]}
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  data=p.read_bytes();assert len(data)<20*1024*1024
  receipts['files'].append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump(R/'out/RECEIPTS.json',receipts)
print(json.dumps({'run':R.name,'graphs':full['graphs'],'queries':full['queries'],'assertions':full['assertions'],'protocol_fields':'PASS','files_hashed':len(receipts['files']),'full_fei':'OPEN'}))
