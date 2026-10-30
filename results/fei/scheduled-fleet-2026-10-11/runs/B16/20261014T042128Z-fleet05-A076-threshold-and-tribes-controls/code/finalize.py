"""A076 stage5 local protocol artifacts; writes only inside A076."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
PREV=AGENT/'runs/20261014T013416Z-fleet05-A076-threshold-and-tribes-controls'
SRC=BASE/'agents/A077/runs/20261014T020716Z-fleet05-A077-sparse-defect-towers'
SRC78=BASE/'agents/A078/runs/20261014T023613Z-fleet05-A078-coding-and-padding'
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=load(PROTO);pilot=load(ROOT/'out/PILOT.json');full=load(ROOT/'out/FULL.json')
review=load(ROOT/'out/REVIEW_VALIDATION.json');rep=load(ROOT/'out/REPEATED_VALIDATION.json')
assert all(x['status']=='PASS' for x in [pilot,full,review,rep])
old=load(PREV/'CLAIMS.json');incoming=[r for r in load(SRC/'REVIEW.json') if r['claim_id'].startswith('A076-')]
for c,r in zip(old,incoming):
    assert r['claim_id']==c['claim_id'] and r['version']==c['version']
    assert r['original_statement_sha256']==c['statement_sha256']
save('out/CONSUMED_REVIEW.json',dict(source=str(SRC/'REVIEW.json'),sha256=sha(SRC/'REVIEW.json'),records=incoming,
     scope='Only A076 stage4 OWNED_PIVOT_PROOF sections1-5 equations1-9 accepted; earlier bundle and new stage5 excluded'))
review_record=dict(claim_id='A077-RARE-RARE-ACTIVATED-COLLISION',version=1,
 original_statement_sha256=load(SRC/'CLAIMS.json')[0]['statement_sha256'],reviewer='A076/fleet05',
 verdict='HOLDS_AT_SCOPED_SECTIONS1_3_OBSTRUCTION',scope='PROOF.md sections1-3 actual family, full influences, exact correction and uniform rarity lower bound only',
 substantive_repair=False,excluded_scope='Sections4-5 paid policy uses A076 own v4 dependency; no independent whole-chain verdict',
 proof='REVIEW_A077.md; code/check_review.py; out/REVIEW_VALIDATION.json')
save('REVIEW_A077.json',review_record)
extensions=[
 ' Stage-5 extension (no derivative gap): For arbitrary Boolean branches G,H on one uniform data cube, fresh-selector F choosing G/H, and a physical coordinate i absent from H, put d=Inf_i(G),delta=Inf_z(F)=Pr[G!=H]. The exact nonnegative admission A_i=B_i(F)-B_i(G)/4 satisfies 0<=A_i<=d+Phi(4delta-d,d)/2<=4delta, with d<=2delta and Inf_i(F)=d/2. The scalar statement behind this is 0<=Phi((u+v)^2,a^2)+Phi((u-v)^2,a^2)-Phi(u^2,a^2)<=4a^2+2Phi((u-v)^2,a^2). No balance, disjoint shared support, activation or derivative-gap hypothesis is used. For any antichain of such private-query nodes before selector revelation, sum w A_i<=4 delta_root, with current private branch exchanged where needed. All actual inherited quarter-core erasures and terminal entropy remain explicit.',
 ' Stage-5 extension: The inherited coefficient 1/4 in B_i(F)<=B_i(G)/4+4Inf_z(F) is sharp for any finite selector price. For even k>=2, H is the k-bit quadratic bent sign with H(0)=1, G=H[1-2*1{s=0,x=0}], private x. Put a=2^-k. Then delta=a/2, B_x(G)>=a(k-2), B_x(F)>=B_x(G)/4+a/2, so every coefficient c<1/4 forces (B_x(F)-cB_x(G))/delta>=2(1/4-c)(k-2)+1. Full I(F)=k/2+(k+2)a/2 is included. The selector-only antichain account cannot be reset: G=y product_(j=1..m)(-1)^(a_j b_j),H=1, first reveal all a_j. Every reached query has A_i=1/4, actual query influence1/4 and selector influence1/2, hence total A=m/4 while delta_root=1/2. Actual I(F)=m/2+1,H(F)=m+2=2I(F), leaf H=2 and leaf I expectation1+m/4; no FEI violation follows. For arbitrary balanced G,H=1, a uniform bound A_T<=K Pi on one complete private-core tree per G would imply full FEI with C=2K+4/ln2, while FEI(C) implies such bounds with K=C+4; this is a scope guard, not a proof that K is finite.'
]
now=datetime.datetime.now(datetime.timezone.utc).isoformat();claims=[]
for c,ext,r in zip(old,extensions,incoming):
    c['version']=5;c['exact_statement']+=ext;c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    c['hypotheses'].append('Stage5 private-query admission requires current queried coordinate absent from one actual branch; selector fresh/unqueried; one marked antichain, no repeated allowance; all logarithms bits. Sharp family even k>=2; repeated family m>=1.')
    c['proof_source']['stage5']=str(ROOT/'PRIVATE_ADMISSION_PROOF.md');c['proof_source']['stage5_locator']='sections1-6 equations(1)-(8)'
    c['proof_source']['stage5_validation']=str(ROOT/'out/FULL.json')
    c['proof_dependencies'].append(c['claim_id']+'@4');c['supersedes']=[c['claim_id']+'@4']
    c['review_records'].append(dict(claim_version=4,record=r,source=str(SRC/'REVIEW.json'),guard='stage4 extension only; v5 unreviewed'))
    c['refutes'].extend(['B_i(F)<=c B_i(G)+K Inf_z(F) universally for a fixed c<1/4 and finite K at all private queries',
                        'sum_private_queries w[B_i(F)-B_i(G)/4]<=K Inf_z(F_root) for all repeated private-query prefixes and finite K'])
    c['next_consumers']=['A077','A078','A058','A057','A097','A092','A088','B16','B20']
    assert set(c)==set(protocol['required_per_run']['claim_fields']);claims.append(c)
save('CLAIMS.json',claims)
sources=[PROTO,BASE/'BOARD.md',BASE/'claude/B16/STREAM_NOTES.md',PREV/'CLAIMS.json',PREV/'OWNED_PIVOT_PROOF.md',PREV/'code/arithmetic.py',
 SRC/'PROOF.md',SRC/'CLAIMS.json',SRC/'REVIEW.json',SRC78/'PROOF.md']
save('SOURCE_MANIFEST.json',dict(captured_at=now,hash_scope='Save-time actual bytes, not retroactive stage-start snapshots',
 sources=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sources],
 read_scopes=dict(board='2026-10-14 04:19 UTC; full board plus separately reread middle sections B06-B14',
 lead='B16 v2 2026-10-11 23:25Z unchanged; original majority/tribes control already completed',
 A077='Complete PROOF.md and actual claim/review records; independent review deliberately limited to new sections1-3',
 A078='Complete stage4 interleaving proof, credited for common-point shadow/quarter-functional transport; new admission is actual B, a different functional')))
progress=dict(protocol_revision=protocol['revision'],run_id=ROOT.name,stream='B16',packet_id='A076',gap_id='FEI-B16-A076-INITIAL',
 attempt_id='A076-stage5-private-antichain-admission',method='Scalar monotone/subadditive entropy comparison, exact coherent private rows, optional-stopping physical disagreement account, sharp actual Boolean families, exhaustive rational small-core certificates',
 mathematical_delta='Universal private-query admission B_G/4<=B_F<=B_G/4+4Inf_selector with no derivative gap; inherited quarter sharp. Any one marked private-query antichain costs <=4 original selector influence; explicit repeated-query family refutes reset of this account while consumed core influence pays its bill.',
 deliverable_status='COMPLETE_LOCAL_PENDING_V5_INDEPENDENT_REVIEW',mathematical_status='UNIVERSAL_PRIVATE_ADMISSION_AUTHOR_PROVED; ANTICHAIN_SCOPE_SHARP; COMBINED_UNIVERSAL_PAYMENT_AND_FEI_OPEN',
 claim_versions_used=['A076-STRUCTURED-SPECTRA@4 (stage4 extension accepted by A077)','A076-TRIBES-PAYMENT-DISCRIMINATION@4 (same scoped acceptance)','A077-RARE-RARE-ACTIVATED-COLLISION@1 (sections1-3 independently accepted here)','A078 stage4 PROOF.md (context only; quarter-functional shadow not assumed for actual erasure bound)'],
 claims_created_or_changed=[c['claim_id']+'@5' for c in claims],source_artifacts=['PRIVATE_ADMISSION_PROOF.md','REVIEW_A077.md','REVIEW_A077.json','SOURCE_MANIFEST.json','code/arithmetic.py','code/check_private.py','code/check_review.py','code/check_repeated.py','code/finalize.py','out/FROZEN_SPEC.json','out/REVIEW_SPEC.json','out/REPEATED_ACCOUNT_SPEC.json','out/FULL.json','out/FULL_LEDGERS.json','out/REVIEW_VALIDATION.json','out/REPEATED_VALIDATION.json','out/CONSUMED_REVIEW.json'],
 next_consumers=['A077','A078','A058','A057','A097','A092','A088','B16','B20'],
 next_action='At the second private collision, combine retained quarter-core erasure with an actual certified child surplus and only unspent physical core influence, keeping the original selector mark and both complete terminal laws. Reviewers A092/A088; A077/A078 test on rare/rare exposure and repeated bent-literal witness.',
 stagnant_substantive_attempts=0,blockers=['Selector-only repeated reserve is rigorously refuted; cannot reset delta','Combined arbitrary-core account is FEI-strength and unpaid; shared queried coordinates remain outside this admission','New v5 independent review, supervisor adoption and mirrors not observed'],packet_ids=['A076'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# A076 stage 5: private-query admission with one marked selector reserve

## exact target, quantifiers, hypotheses and units

Replace the stage4 derivative-gap assumption at the first genuinely private collision. For every Boolean G,H on one common uniform data cube, fresh-selector F choosing G/H, and a queried data coordinate i absent from H, prove **B_i(G)/4<=B_i(F)<=B_i(G)/4+4Inf_z(F)**. Every logarithm is in bits; B is actual conditional spectral erasure. The stronger profile bound and an arbitrary-exposure antichain account are proved, the quarter coefficient is sharp, and repeated reuse of a selector-only account is refuted. Both actual terminal core spectra remain explicit. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md dated 2026-10-14 04:19 UTC with omitted middle sections reread separately, unchanged B16 lead notes v2, STATUS/LEARNED and the full execution protocol v2. Read A077 stage4 PROOF.md sections1-5, CLAIMS.json and REVIEW.json; its scoped acceptance of A076 v4 has matching original statement hashes. Read complete A078 stage4 PROOF.md on interleaved common-point quarter-functional transport. Prior OWNED_PIVOT_PROOF and arithmetic source are reused. SOURCE_MANIFEST.json pins actual save-time hashes/read scopes. The first guessed A077 review filename did not exist; REVIEW.json supplies the actual receipt. No acceptance is inferred from a guessed A058 path.

A077 already proves the activated rare/rare prescribed-query obstruction; it is consumed and scoped-reviewed rather than rediscovered. A078's quarter-power surrogate L is distinct from the actual inherited B/4 in this stage. No claim of literature priority or new external source result is made.

## complete derivation or exact first unsupported line

PRIVATE_ADMISSION_PROOF.md sections1-6 contains the full analytic argument. Monotonicity/subadditivity of Phi and Phi(cp,q)<=Phi(p,q)+q log2(c) give the scalar retained-quarter comparison (1). Actual selector-frequency rows give the private spectrum (2). Parseval identifies mean-profile error E=4delta-d; pivotal edge Booleanity gives d<=2delta. Concavity/log-sum then yields 0<=A_i=B_i(F)-B_i(G)/4<=d+Phi(4delta-d,d)/2<=4delta. This holds at arbitrary biased descendants, with unlimited shared data and no derivative gap.

Before selector revelation, delta_v is the conditional expectation of the physical branch disagreement indicator. Every private-query antichain therefore satisfies sum w A_i<=4delta_root. For A077's rare/rare common activation, all exposures of the one private x, under any adaptive earlier data/control order, cost at most 4qc. Charges at other earlier shared queries and the later selector are still retained obligations.

The private bent-edit family proves the inherited coefficient 1/4 is optimal even with any finite selector price; every c<1/4 loses a term at least 2(1/4-c)(k-2)+1 times selector influence. Full I(F)=k/2+(k+2)2^-k/2 is included. The fresh-literal/tensor-quadratic witness proves why the antichain qualification is necessary: m private layers have total A=m/4 at constant selector influence1/2. Here actual consumed core influence is m/4, full H(F)=2I(F), and terminal H=2, so this is a nonreuse obstruction rather than an FEI disproof.

The remaining combined account is explicitly FEI-strength: for balanced arbitrary G,H=1, a uniform A_T<=K Pi on one complete core tree per G implies FEI with C=2K+4/ln2. Conversely FEI(C) implies this with K=C+4. The proof uses the exact entropy/JS telescope and a balanced tensor-literal guard. This equivalence only prevents overstating the first unsupported line; it is not counted as a proof that K is finite. A combined signed child-surplus/core-influence payment at the second collision, and a genuinely shared queried coordinate, remain open.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before computation. Pilot: 72 actual labelled core pairs with 0..1 shared bits, 216 exposure trees and 245 scalar cases, {pilot['exact_assertions']:,} exact assertions PASS in {pilot['elapsed_seconds']:.3f}s. Full: every G(x,s),H(s) with 0..2 shared bits, **{full['roots']:,} roots, {full['antichain_trees']:,} antichain trees, {full['scalar_cases']} scalar cases, {full['exact_assertions']:,} exact assertions PASS in {full['elapsed_seconds']:.3f}s**. The three policies query x first, shared data first, or adapt exposure to prior answers. Exact terminal entropy and inherited quarter costs are saved in out/FULL_LEDGERS.json. Seven bent-edit parameters k=2,4,6,8,16,32,64 are frozen; direct tables for k<=8 match independent compressed row multiplicities, larger values use the proved actual Boolean construction and rigorous compressed certificates.

Commands: `python -X utf8 runs\\{ROOT.name}\\code\\check_private.py --pilot`, then without `--pilot`. `code/check_review.py` passed {review['exact_assertions']} exact assertions in {review['elapsed_seconds']:.3f}s, checking all sharp-witness physical influences at k=2,4,6,8 and four actual A077 activated roots. `code/check_repeated.py` passed {rep['exact_assertions']} exact assertions in {rep['elapsed_seconds']:.3f}s, checking every reached node of the repeated-account witness at m=1..4 and compressed exact ledgers at m=16,32,64,128. Their specs preceded execution. No domain escalation, failed computation or heavy job was needed in this stage.

Integer FWHT/Fraction coefficients are checked against separate physical edge counts. Log equalities use exact rational prime-exponent maps; inequalities use 24-term rational atanh series reduced to [1,2], proved tail 2*z^(2N+1)/((2N+1)*(1-z^2)), and outward 70-bit dyadic rounding. Sharp large-parameter outputs use outward 90-bit endpoint storage, not giant raw rational serialization. Memory estimate 180 MB for the main job, not a measured peak; no job was expected above 300 MB. All-dimensional statements follow from the analytic proof, not finite extrapolation.

## proof dependencies and changed downstream conclusions

Both existing A076 bundles extend to v5; no third broad pending candidate is opened. A077's hash-bound acceptance covers our v4 extension only, not earlier bundles or v5. A077-RARE-RARE-ACTIVATED-COLLISION@1 receives independent HOLDS only at sections1-3 (truth formulas, influences, exact correction and lower bound). Its paid-policy sections use A076's own theorem and are deliberately excluded from independent whole-chain acceptance. No substantive repair was supplied to that source.

The new admission proof is elementary and does not assume the pending general FEI payment or A078's quarter-surrogate theorem. A077/A078 receive a one-mark payment for arbitrary earlier exposure of the bad private query, beyond eta admission. A057/A058/A097/B20 receive the sharp inherited quarter, a selector nonreuse certificate and a precise FEI-strength combined gap. Independent acceptance of v5, source-index adoption, downstream use and mirrors remain unverified.

## one next mathematical action and independent reviewer

At the second private collision, combine the retained quarter-core bill with a certified signed child surplus and only unused physical core influence, keeping the original selector mark and both full terminal laws. This is forced by the repeated-account witness; a fresh delta allowance is invalid. A092 primary/A088 alternate should reconstruct scalar (1), Parseval/Boolean d<=2delta, antichain stopping, sharpness and nonreuse. A077/A078 can test rare/rare and repeated literal/bent packets.

## actual persistence receipts or precise save blocker

All four protocol files, source-complete proof, exact helper outputs/ledgers, three frozen specifications, independent scoped review and consumed v4 review receipt are saved locally. code/finalize.py checks exact schema keys, statement hashes and matching compatibility bytes; out/PERSISTENCE.json records byte counts/hashes at {now}. Rolling STATUS has two lines, WORKLOG and LEARNED are appended. Every file is below 20 MB. Supervisor copies, remote mirrors and independent acceptance of new results are not asserted.

## Universal bridge

C019 moves by a universal private-query interface with **sharp inherited fraction 1/4 and one-mark selector price4**, without the previous derivative-gap or shared-width assumptions. Any selected private-query antichain costs <=4 original selector influence, including A077's arbitrarily interleaved rare/rare private exposure; repeated selector-only payment is exactly refuted at growth m/2 relative to its original account. Inherited quarter-core erasure, future selector cost and actual terminal core entropy remain, and a universal combined repeated-payment constant is FEI-strength and unpaid. NEXT attacks the second collision with certified child surplus and genuinely unspent core influence because the new theorem pays the first collision and the new witness identifies precisely why restarting that payment cannot lead to full FEI.
'''
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text(f'STATE: A076 stage5 saved: universal private admission B_G/4<=B_F<=B_G/4+4Inf_selector; sharp quarter, one-mark antichain payment and repeated-reset no-go; {full["exact_assertions"]:,} exact full checks PASS; v5 review pending, FEI OPEN.\nNEXT: Pay second private collision with certified signed child surplus and unused physical core influence, preserving original selector mark and complete terminals; A092/A088 review admission and sharp nonreuse.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## {now} (requested stage 2026-10-14 04:21 UTC)\nRead board and new A077/A078 proofs; consumed scoped A077 v4 acceptance. Proved universal private admission B_G/4<=B_F<=B_G/4+4delta via scalar entropy, Parseval and pivotal edges; antichain payment uses one selector martingale account. Actual bent-edit family proves quarter optimal. Repeated literal/bent prefix refutes resetting selector reserve: A=m/4 at delta1/2, while consumed influence pays exactly. Combined arbitrary-core repeated bound is FEI-strength, not established. Main {full["exact_assertions"]} exact assertions/{full["antichain_trees"]} trees in {full["elapsed_seconds"]:.3f}s; influence/review {review["exact_assertions"]}, repeated {rep["exact_assertions"]} exact checks PASS. Scoped A077 sections1-3 independent HOLDS; paid-policy chain excluded due own dependency. All run/rolling artifacts saved.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage5 durable facts (bits): private query i absent from branch H in F=mux_z(G,H) has A_i=B_i(F)-B_i(G)/4>=0 and A_i<=d+Phi(4delta-d,d)/2<=4delta, d=Inf_i(G),delta=Pr(G!=H)=Inf_z(F), d<=2delta. Scalar retained-quarter inequality follows from Phi(cp,q)<=Phi(p,q)+q log2c and subadditivity, not a derivative-gap assumption. Any antichain of private exposures before z has sum wA<=4delta_root by the physical disagreement martingale. All nodes for one private coordinate form such an antichain even with arbitrary earlier data/control exposure. Coefficient1/4 is sharp via G=bent*(1-2point(s,x)),H=bent: B_G/delta>=2(k-2), B_F>=B_G/4+a/2. Resetting selector reserve fails: G=y*product_m quadratic pairs,H=1, expose first pair bits; totalA=m/4,delta1/2,consumedI=m/4,fullH=2I,leafH2. Thus second collision needs a combined owned core/child account. A uniform combined A_T<=KPi for arbitrary balanced G would imply FEI with C=2K+4/ln2, so it remains an honest full-strength gap. A077 accepted only v4 extension; own independent A077 review accepts sections1-3, not the chain using A076.\n')
paths=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
for p in paths:assert p.stat().st_size<20*1024*1024,(str(p),p.stat().st_size)
save('out/PERSISTENCE.json',dict(saved_at=now,scope='Verified local artifacts, not remote mirror or independent acceptance',
 artifacts=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)) for p in paths],
 rolling=[dict(path=str(AGENT/p),bytes=(AGENT/p).stat().st_size,sha256=sha(AGENT/p)) for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]))
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
print(json.dumps(dict(saved=True,schema='PASS',run=str(ROOT),main_assertions=full['exact_assertions'],review_assertions=review['exact_assertions'],repeated_assertions=rep['exact_assertions'],files=len(paths)+1)))
