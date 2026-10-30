from pathlib import Path
import json,hashlib,datetime

run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
run_id=run.name
pilot=json.loads((run/'out/pilot_results.json').read_text())
prefix=json.loads((run/'out/main_checkpoint.json').read_text())
suffix=json.loads((run/'out/remaining_results.json').read_text())
spec3=json.loads((run/'out/FROZEN_SPEC_V3.json').read_text())
assert prefix['case_count']==4096*spec3['start_outer_table']
assert suffix['result']=='PASS' and prefix['case_count']+suffix['case_count']==65536
main={'mode':'main','case_count':65536,'exact_assertions':prefix['exact_assertions']+suffix['exact_assertions'],'elapsed_seconds':prefix['elapsed_seconds']+suffix['elapsed_seconds'],'result':'PASS','coverage':'disjoint exhaustive prefix and suffix; prefix timed out only after saving complete outer-table chunks','prefix':prefix,'suffix':suffix}
(run/'out/main_results.json').write_text(json.dumps(main,indent=2),encoding='utf-8')
assert pilot['result']==main['result']=='PASS'
receipts=json.loads((agent/'source_receipts.json').read_text())
(run/'out/source_receipts.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
statement='For uniform Boolean F and b_j on disjoint shared blocks, private bits x_i, and any binary incidence matrix A, f=F(x_i product_j b_j^A_ji) has H(f)=H(F)+sum_j d_j H(b_j) and I(f)=I(F)+sum_j d_j I(b_j), where d_j=Pr_{T~Fhat^2}((A1_T)_j=1); H(F)=H(A1_T)+H(T|A1_T). A common FEI constant for F and the b_j transfers unchanged. Products of at-most-two-bit gates yield unconditional H(f)<=2I(f), including the all-k nonlinear common-block family H=2k+1, I=k+1/2, posterior=2k-1.'
claim={
'claim_id':'A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER','version':1,'exact_statement':statement,
'hypotheses':['uniform cube; sign-valued Boolean gates','all shared blocks pairwise physically disjoint','one private uniform bit x_i for every outer input, disjoint from all shared blocks','arbitrary binary incidence matrix; all Fourier atoms retained; entropy in bits','FEI closure implication assumes a stated bound for every outer/shared component; unconditional constant-2 corollary restricts those components to disjoint products of gates of arity at most two'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['fleet05/A058'],
'proof_source':{'path':str(run/'OVERLAP_ENTROPY_LEDGER.md'),'theorem_source':str(run/'OVERLAPPING_COMPOSITION_CLASS.tex')},
'proof_dependencies':[],'review_records':[],'status':'PROVED_LOCAL_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],
'first_unproved_line':None,'next_consumers':['A059','A060','A091','A090','B20']}
claim['statement_sha256']=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
(run/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={
'protocol_revision':'2026-10-11-execution-v2','run_id':run_id,'stream':'B12','packet_id':'A058','gap_id':'FEI-B12-A058-INITIAL','attempt_id':'A058-ANCHOR-XOR-1',
'method':'pointwise Boolean parity cancellation, private Fourier tags, exact collision posterior and physical coordinate influence',
'mathematical_delta':'Closed a non-selector shared-input composition class with arbitrary nonlinear shared-gate reuse, exact entropy/influence ledger, unchanged FEI constant transfer, and an unconditional unbounded-overlap H<=2I class. The full collision posterior is retained and can be 2k-1 bits.',
'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'RESTRICTED_CLASS_PROVED_LOCALLY; FULL_FEI_OPEN','claim_versions_used':[],
'claims_created_or_changed':['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@1'],
'source_artifacts':['OVERLAP_ENTROPY_LEDGER.md','OVERLAPPING_COMPOSITION_CLASS.tex','code/verify.py','code/verify_fast.py','out/FROZEN_SPEC.json','out/FROZEN_SPEC_V2.json','out/FROZEN_SPEC_V3.json','out/main_v1_attempt.json','out/main_checkpoint.json','out/remaining_results.json','out/pilot_results.json','out/main_results.json','out/source_receipts.json'],
'next_consumers':['A059','A060','A091','A090','B20'],
'next_action':'Derive the exact signed fiber coefficient when a single private anchor is removed, and identify the first physical posterior/normalization correction that must be paid; A091 independently reconstruct the present coefficient and physical influence law.',
'stagnant_substantive_attempts':0,'blockers':['B12 STREAM_NOTES.md absent at stage start; independent review and supervisor mirror pending, not mathematical blockers for the scoped theorem'],
'packet_ids':['A058']}
for filename in ['PROGRESS.json','PACKET_DELTA.json']:(run/filename).write_text(json.dumps(progress,indent=2),encoding='utf-8')
report=f'''# A058 overlapping compositions: locally complete restricted theorem

## exact target, quantifiers, hypotheses and units

For every finite outer arity m, number of shared gates r, binary incidence matrix A and uniform Boolean sign outer gate F, compose g_i=x_i product_j b_j(z_j)^A_ji, with one private bit per outer input and pairwise disjoint shared blocks. Close an entropy ledger for unbounded shared-input reuse, without using disjoint-child composition identities. Entropy is in bits including the empty atom. The full self-contained proof is OVERLAP_ENTROPY_LEDGER.md, and the theorem manuscript is OVERLAPPING_COMPOSITION_CLASS.tex. The exact result is H(f)=H(F)+sum d_j H(b_j), I(f)=I(F)+sum d_j I(b_j); collision posterior H(T|A1_T) is retained. This yields unchanged constant transfer and an unconditional H<=2I class based on at-most-two-bit gates. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; README.md, CURRENT_STATUS.md, CLAIM_REGISTRY.json, OBSTRUCTION_REGISTRY.json, PACKET_STATUS.json and STREAM_NEXT_ACTIONS.json; A058 contract in AGENT_ASSIGNMENTS.json; campaign plan FEI_100_agent_research_plan.tex, particularly Shared-data composition and the B12 packet contract. Read earlier B05/B09/B19 reports for obstruction scopes, not as theorem dependencies. Read BOARD.md (2026-10-11 22:16 UTC snapshot); B12 STREAM_NOTES.md did not exist.

Read supplemental CAMPAIGN.md, CLAIMS.md (C015 parity lift, C030 false overlapping subadditivity, C035 fresh-selector baseline), COUNTEREXAMPLES.md, SEED_LEMMAS.md, NATIVE_MAPPING.md and packaged sources. In particular OVERLAPPING_PRODUCT_NOTE.md distinguishes translation-averaged entropy from a chosen coherent product; ERASURE_REDUCTION.md section 4 identifies C018; ISOSPECTRAL_SPLICING_CURATED.md sections 5-6 warns against missing parity cancellation. These are context, not proof dependencies. Current and earlier threshold/percolation text versions were read through local source traversal and relevant excerpts. Threshold 38pp Proposition 7.1 gives the disjoint baseline; its shared-multiplexer section is already completed prior work. Percolation spatial hypotheses are not imported. out/source_receipts.json pins {len(receipts)} source files by SHA256 and line count. Known parity lift C015 is a special case of the present identity with a literal shared gate; no novelty claim is made for it or the underlying chain rule. The delta is multiple arbitrarily reused nonlinear blocks, their parity-activation physical influence, and the retained incidence-fiber posterior.

## complete derivation or exact first unsupported line

The complete proof expands F first, uses b_j^2=1 to reduce repeated shared factors modulo two, then derives the actual coefficient fhat(T,S)=Fhat(T) product_j c_j,U_j(T)(S_j). Private support T separates outer labels. Only after this derivation is the entropy chain rule applied to the normalized squared law. This avoids the refuted overlapping-product subadditivity claim. The posterior law is p(T|u)=p_T/q_u. Its full contribution B satisfies H(q)+B=H(F), not H(q) alone. Every physical influence is Inf_xi=Inf_i(F) or Inf_zjk=d_j Inf_k(b_j), with a separate spatial-mask derivation. Conditional transfer has no constant loss.

Every two-bit gate has H<=2I by truth-table classification; disjoint products add. Thus products of these gates may be used as outer/shared components at any size. The all-k common nonlinear gate family has H(q)=1, posterior=2k-1, H=2k+1 and I=k+1/2, showing unbounded reuse and exact equality. Even outer parity cancels the common gate completely. All proofs at the stated hypotheses are complete. The first unsupported line for removing a private anchor is a proposed influence payment for the resulting signed coherent fiber sums; no such estimate is claimed. Bent-splice selector-only increment bounds are not used: this proof keeps outer and shared data influence throughout.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json before search: pilot all 16 two-bit outer gates, all 16 two-bit shared gates, all 4 one-row incidence matrices (1,024 cases); main all 16 outer gates, all 16 gates for each of two shared blocks, all 16 two-row incidence matrices (65,536 cases). No symmetry reduction. Maximum physical dimension is six; memory estimate below 20 MB; no >300 MB job or GPU; pilot limit 60 seconds and main limit 180 seconds.

Executed from the agent directory:

    python -X utf8 runs\\{run_id}\\code\\verify.py --mode pilot
    python -X utf8 runs\\{run_id}\\code\\verify.py --mode main
    python -X utf8 runs\\{run_id}\\code\\verify_fast.py
    python -X utf8 runs\\{run_id}\\code\\verify_fast.py --resume

Pilot PASS: {pilot['case_count']:,} cases, {pilot['exact_assertions']:,} exact assertions, {pilot['elapsed_seconds']:.3f} seconds. The original main helper hit its frozen 180-second limit without checkpointing or reporting a mathematical failure; out/main_v1_attempt.json records it as INCOMPLETE_RESOURCE_LIMIT. A second helper was separately frozen in out/FROZEN_SPEC_V2.json on exactly the same domain and runtime cap. It caches finite spectra and computes dyadic entropy as an integer numerator, retaining exact Fraction prime-log posterior checks on every outer/matrix pair. It saved a checked prefix of {prefix['case_count']:,} cases before its runtime guard stopped at {prefix['elapsed_seconds']:.3f} seconds (guard checked after complete outer-table chunks). The remaining {suffix['case_count']:,} cases were separately frozen in out/FROZEN_SPEC_V3.json and passed in {suffix['elapsed_seconds']:.3f} seconds. Their disjoint union covers all 65,536 cases; aggregate {main['exact_assertions']:,} exact assertions, {main['elapsed_seconds']:.3f} seconds across the two checkpointed jobs. No mathematical assertion failed in either resource-limited attempt. Raw integer Walsh coefficients, squared dyadic masses, influence from independently counted cube edges, activation probabilities from simultaneous physical mask flips in the pilot, posterior and entropy identities were verified. No floating-point sign decisions or logarithmic interval assumptions were needed. The pilot also verified the nonlinear common-block family at k=1,2,3,4 and the cancellation extreme. Universal parameter claims follow from the proof, not the census. The edge implementation provides independent arithmetic validation of influence, but it is not an independent mathematical review.

## proof dependencies and changed downstream conclusions

No campaign claim is required as an unreviewed premise: the proof uses elementary Fourier expansion, b_j^2=1, Parseval, the finite probability chain rule, and a self-contained two-bit classification. No statement about arbitrary overlapping products is inferred. The conditional transfer requires component FEI assumptions exactly as written; r=0 retains arbitrary F, and m=r=1 with F a dictator gives H(xb)=H(b), I(xb)=1+I(b). Thus arbitrary component difficulty remains, and universal claims are unchanged. A059/A060 receive a complete reusable overlap interface rather than a selector baseline restart; A091/A090 receive a single bundled review candidate.

## one next mathematical action and independent reviewer

Remove one private anchor and derive its exact signed fiber coefficient to locate the physical posterior and normalization correction. This is a narrowly identified transition from orthogonal tagged amplitudes to actual interference. Primary independent reviewer A091 should reconstruct the coefficient law and the simultaneous-mask spatial influence; alternate A090. No reviewer acceptance is yet recorded. This candidate is bundled as one claim; the B12 board had one completed baseline A056 and an unfinished A057, so this run does not open further broad candidates after filling the observed two-claim cap.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=["A058"], both requested proof deliverables, frozen specification, code, outputs and source receipts inside the assigned run. Agent rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/artifact_receipts.json records SHA256 and byte counts and is generated after the report write. Shared indices, other agent folders and all source trees were untouched. No git, mail, brain writes, background workers or windows were used. Supervisor copying, mirror verification and independent review remain pending; local persistence is not represented as remote publication.

Universal bridge: This stage moves C018 on the explicit component class: B_erasure<=H<=2I is now paid for every incidence matrix and every amount of nonlinear shared-gate reuse under private anchors. The ledger pays the entire collision posterior once through the outer spectrum and each active shared spectrum once through its physical influence. It supplies a restricted spectral transfer interface relevant to C024, but does not analyze C024's actual reveal histories or establish closure under all physical restrictions. What remains universal is controlling signed fiber recombination when a private tag disappears, together with arbitrary component entropy. Deriving that single-anchor correction is the shortest next step because it attacks exactly the interference boundary of the transfer proof; expanding the already closed incidence census or claiming a fresh-selector baseline would not reduce the universal unpaid term.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A058 local packet complete: exact shared nonlinear-gate collision/posterior ledger and unbounded-overlap H<=2I class; 65,536 cases checked; A091/A090 review pending; full FEI OPEN.\nNEXT: A091 reconstruct signed coefficient and physical mask ledger; derive the coherent fiber correction after removing one private anchor.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'2026-10-12: Pilot passed {pilot["exact_assertions"]:,} exact assertions in {pilot["elapsed_seconds"]:.3f}s; main passed {main["exact_assertions"]:,} exact assertions over {main["case_count"]:,} cases in {main["elapsed_seconds"]:.3f}s. Saved source-complete theorem, posterior debt, all-k equality family, protocol artifacts and review handoff. Full FEI remains open; next gap is one-anchor coherent merging.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('Common nonlinear two-bit gate b with outer product of k exceptional two-bit gates: H(f)=2k+1, I(f)=k+1/2, H(incidence pattern)=1 and collision posterior=2k-1. This is an exact all-k H=2I class with unbounded read. Private anchors protect outer Fourier labels; dropping them can introduce signed coherent sums, so the normalized squared product law must not be reused there. Known C015 literal parity lift is a special case, not new progress by itself.\n')
required=['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json','OVERLAP_ENTROPY_LEDGER.md','OVERLAPPING_COMPOSITION_CLASS.tex','code/verify.py','code/verify_fast.py','code/finalize.py','out/FROZEN_SPEC.json','out/FROZEN_SPEC_V2.json','out/FROZEN_SPEC_V3.json','out/main_v1_attempt.json','out/main_checkpoint.json','out/remaining_results.json','out/pilot_results.json','out/main_results.json','out/source_receipts.json']
artifact=[]
for n in required:
    raw=(run/n).read_bytes(); assert len(raw)<20_000_000
    artifact.append({'path':n,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
(run/'out/artifact_receipts.json').write_text(json.dumps(artifact,indent=2),encoding='utf-8')
assert json.loads((run/'PROGRESS.json').read_text())==json.loads((run/'PACKET_DELTA.json').read_text())
print(json.dumps({'saved':len(required),'main_exact_assertions':main['exact_assertions'],'run':str(run),'claim_status':claim['status']}))
