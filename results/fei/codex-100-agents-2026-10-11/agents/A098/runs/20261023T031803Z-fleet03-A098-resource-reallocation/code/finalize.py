from pathlib import Path
import json,hashlib,datetime,copy
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';OWN=RUN.parents[1];BASE=RUN.parents[3]
CAN=Path(r'math-open-problems/reports\fei-2026-10-11')
def read(p):return p.read_text(encoding='utf-8-sig')
def save(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=json.loads(read(OUT/'RESULT.json'));pilot=json.loads(read(OUT/'PILOT_RESULT.json'));assert r['status']==pilot['status']=='PASS'
protocol=json.loads(read(CAN/'EXECUTION_PROTOCOL.json'))
census=json.loads(read(OUT/'PACKET_CENSUS.json'));latest={x['packet']:x for x in census}
changes=json.loads(read(OUT/'CHANGED_SOURCES.json'));sources=json.loads(read(OUT/'SOURCE_LEDGER.json'))
src=Path(latest['A097']['latest_complete_report']);sourceclaims=json.loads(read(src/'CLAIMS.json'))
claims=copy.deepcopy(sourceclaims)
for c in claims:
    c['review_records'].append({'reviewer':'A098','run_id':RUN.name,'verdict':'HOLDS_AT_EXACT_SUPPLIED_REFERENCE_SCOPE','scope':'Full stated first-frontier theorem and original-source repeated-calibrated-return theorem independently reconstructed, including dependency and endpoints; integrated negative-cell18/7e claim is NOT independently accepted. No repair supplied.','method':'Independent analytic reconstruction; different rational-law grid; butterfly Walsh and separately counted physical edges; fixed outward rational log intervals','proof':'REVIEW.md sections1-4','validation':r})
    c['status']='INDEPENDENT_ANALYTIC_RECONSTRUCTION_HOLDS_AT_STATED_SCOPE'
save(RUN/'CLAIMS.json',claims)
pending=[];errors=[];claimfiles=0
for p in sorted((BASE/'agents').glob('A[0-9][0-9][0-9]/runs/*/CLAIMS.json')):
    if RUN in p.parents:continue
    claimfiles+=1
    try:raw=json.loads(read(p))
    except Exception as ex:errors.append({'source':str(p),'error':str(ex)});continue
    if isinstance(raw,dict):raw=raw.get('claims',[raw])
    if not isinstance(raw,list):continue
    for x in raw:
        if isinstance(x,dict) and any(s in str(x.get('status','')).upper() for s in ['PENDING','UNREVIEWED']):
            pending.append({'source':str(p),'claim_id':x.get('claim_id'),'version':x.get('version'),'statement_sha256':x.get('statement_sha256'),'status':x.get('status'),'review_records':x.get('review_records',[])})
save(OUT/'REVIEW_QUEUE_CANDIDATES.json',{'snapshot_at':now,'claim_files':claimfiles,'parse_failures':errors,'method':'Explicit historical PENDING/UNREVIEWED records. Retains stale statuses and exact source versions. Not an accepted current-queue total or proof of cap compliance.','records':pending})
lanes=[
 ('A001','Preserve current both-branch prescribed canonical reset continuation; retire old min-ratio duplication.','One next active data query plus prescribed reset using actual conditional-KL refund and diminished original quota3, both terminals and old debits.','A004/A090'),
 ('A045','Keep native mixed-profile/merged-reference mechanism; scalar half-tax work remains consumed.','Pay complete merged signed reference cost with one degree-weighted owner, including normalization and terminal costs.','A041/A044/A091'),
 ('A073','Consume independently reviewed dummy local step and the new original-source absorption theorem; stop vacuum-only return searches.','On the chosen A050/A046 non-point fixture, certify occupied support and the actual conditional-NONEMPTY old/new atom quotient after the paid query.','A085/A092'),
 ('A040','Consume A046 original-source retirement; preserve new non-point correlated incoming-reference work.','Independently check A046 post-x/a correlated reset and the next active-data paired-S eligibility using same Q, old quarter and accumulated reset debit.','A092'),
 ('A046','Preserve productive correlation-preserving non-point reset continuation; no root-tax repetition.','Query active data after the a-child reset; certify actual paired S and remaining original allowance before any second nonempty-profile reset.','A040/A050/A092'),
 ('A089','Keep signed common-kernel transfer mechanism; retired min-ratio job stays retired.','Query core1 data in the negative terminal with incomingA and donorA already spent, parked2tau untouched, full old labels and both terminals.','A072/A074/A092'),
 ('A097','Consume all repeated ORIGINAL-source vacuum-calibrated return liability; new theorem independently HOLDS here.','Construct ONE actual changed conditional-NONEMPTY profile transaction on A050/A046 source; bound reach*(shape likelihood bill minus binary-KL refund) by a named unused original allowance after old bookings.','A094/A085'),
 ('A096','Retire stale original-source-return NEXT; supplied-likelihood theorem is independently reconstructed here.','For the SAME selected non-point query, derive a useful occupied-source likelihood floor and certify its payment from original source surplus; do not assume a universal influence-priced supplier.','A085/A094'),
 ('A003','Parallel vacuum absorption is compatible with A097; consolidate aliases instead of proving it again.','Maintain MINIMAL_TARGET(4) signed shape-minus-vacuum bill with every old sibling/booking; challenge whether the chosen original allowance is actually unused.','A092/A094'),
 ('A050','Keep native correlation-preserving source supplier and actual paired-bank certificate.','Provide exact incoming Q, source reference, paid x/a history, old-quarter debit and full terminals for the next prescribed correlated reset.','A047/A049/A092'),
 ('A085','Consume already saved direct-final-calibration guard; separate adversarial work from construction.','Try to break the selected nonempty-profile payment with ghost atoms, small occupied likelihood, nonconstant sibling and an exhausted owner.','A092'),
 ('A086','Preserve native A011 arbitrary-core v2/second-edit review; do not redirect to now-closed vacuum absorption.','Audit SAME original C0/U_star through source-prefix floors and the second representation edit, including both terminals and old debits.','A094'),
 ('A099','Update exact chain after independent source-bound acceptance; keep integrated negative-cell assembly conditional.','Alias the A003/A097 absorption identity and delete only its canonical-return liability; leave explicit nonempty-profile and generic source-price leaves.','A094/A092')]
allocation={'snapshot_at':now,'authority':'Local proposed source-bound handoff for supervisor adoption only; no external message, live dispatch, index edit or other-agent mutation.','workers_created':0,'schedules_created':0,'historical_six_lanes_refreshed':6,'canonical_claim_for_full_supplied_return':'A097-ORIGINAL-SOURCE-CANONICAL-RETURN-COMMUTATION@1','parallel_mechanism':'A003 vacuum absorption is compatible; retain provenance as an alias, no automatic statement/version merge.','retired_tasks':['Three duplicate min-ratio jobs and three scalar-tax reviews remain retired; preserve A082/A090 current productive tasks.','Vacuum-only ORIGINAL-source returns including final calibration are complete within supplied hypotheses.','Dummy point-source reset grids are consumed; do not duplicate A073/A026 outputs.'],'lanes':[dict(zip(['packet','dispatch_evidence','distinct_next_lemma','independent_reviewer'],x)) for x in lanes]}
save(RUN/'CHECKPOINT_ALLOCATION.json',allocation)
lines=['# Checkpoint allocation: genuine nonempty-profile payment','',f'Snapshot {now}. Local delta awaits supervisor adoption; existing identities and capacity remain fixed.','', '| Packet | Distinct next lemma | Review |','|---|---|---|']
lines += [f'| {x[0]} | {x[2]} | {x[3]} |' for x in lanes]
(RUN/'CHECKPOINT_ALLOCATION.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B20','packet_id':'A098','gap_id':'C024-CONDITIONAL-NONEMPTY-PROFILE-PAYMENT-SAME-ANCESTOR','attempt_id':'A098-stage18-source-absorption-review-and-reallocation',
 'method':'Consume changed live sources, independently reconstruct full supplied-likelihood and calibration-absorption proof chain, exact rational adversarial validation, and source-bound reallocation to actual changed-profile cost',
 'mathematical_delta':'A097 original-source repeated canonical-return theorem and A096 first-frontier dependency independently HOLD at exact supplied-reference scope. Canonical returns incur zero additional cost after first reset. Only actual nonempty-profile change and generic source pricing remain unpaid; no universal FEI constant improvement.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; SHARED_ADOPTION_AND_REMOTE_MIRRORS_UNVERIFIED','mathematical_status':'INDEPENDENT_PROOF_RECONSTRUCTION_HOLDS_FOR_SUPPLIED_REFERENCE_CHAIN; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'source':str(src/'CLAIMS.json')} for c in sourceclaims],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Independent exact-scope HOLDS without repair; original statement and hash preserved'} for c in claims],
 'source_artifacts':['REVIEW.md','out/SOURCE_LEDGER.json','out/PACKET_CENSUS.json','out/CHANGED_SOURCES.json','out/REVIEW_QUEUE_CANDIDATES.json','out/FROZEN_SPEC.json','out/RESULT.json','out/COMPUTE_ADMISSION.json','CHECKPOINT_ALLOCATION.json'],
 'next_consumers':['A097','A096','A003','A073','A050','A046','A085','A099','B20 supervisor'],
 'next_action':'Pay one actual conditional-NONEMPTY reference-profile reset after a paid A050/A046 non-point query from SAME diminished original bank; keep both complete terminals, actual binary-KL refund and all prior debits.',
 'stagnant_substantive_attempts':0,
 'blockers':['A generic influence-priced source and likelihood floor for all Boolean functions remain unconstructed.','Integrated negative-cell18/7e assembly remains conditional at this independent-review scope.','Formal compiler admission refused; proof is analytic with exact finite validation, not Lean-checked.','Local allocation needs supervisor adoption; no external dispatch is asserted.','Brain wake remains degraded: stale owner-model/state-of-mind notes are not premises.'],'packet_ids':['A098']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
a=r['stats']['algebra'];s=r['stats']['structural'];g=r['stats']['global']
report=f'''# A098 stage18: original-source returns closed, nonempty-profile payment isolated

## exact target, quantifiers, hypotheses and units

Compare current output against campaign milestones, consume delivered next steps before reallocating existing packets, and independently reconstruct the COMPLETE supplied-reference chain A096 first-frontier -> A097 arbitrary repeated ORIGINAL-source calibrated returns. For every Boolean g on a finite uniform cube, supply the stated finite subprobability comparison D, normalized S,Q, and occupied-support likelihood gamma>0. Every physical query, reset choice and stopping tree is finite and may be adaptive. All costs are ideal bits; B is spectral erasure conditional entropy; reaches are actual uniform physical probabilities. No universal influence-priced supplier or all-dimensional FEI conclusion is assumed.

## sources actually read, revisions and theorem locators

Read own STATUS and previous stage17 review/allocation, current BOARD2026-10-23 03:14 UTC and B20 lead notes v2 still dated2026-10-11. Execution-v2 was read completely. Read-only intake covers required canonical README/status/registries/packet/action files and TeX plan, prior canonical reports, supplement/source text, all four manuscript text exports and all100 latest packet reports/claims/statuses. out/SOURCE_LEDGER has {len(sources)} byte receipts; CHANGED_SOURCES records {len(changes)} latest report paths differing from stage17's intake. These are source/evidence counts, not numbers of new theorems. out/REVIEW_QUEUE_CANDIDATES reads {claimfiles} historical claim files without silently dropping explicit pending statuses; it preserves exact source versions and is not a certified current review-queue total.

Critical originals read fully: A097 {src.name} DERIVATION1--4 and CLAIMS; A09620261023T010221Z DERIVATION1--5; A08520261022T234859Z PROOF1--5; A09920261022T231100Z report/claims; A003 parallel absorption and A050/A079 supplied non-point sources. Exact A096 hash8b8a71cb... and A097 hash852163b4... are preserved in CLAIMS. The context manuscripts are background only, not new proof dependencies. The old static21 October endpoint is superseded by the owner's23 October14:49 UTC endpoint. Actual save time {now}; the supplied run identifier is not a claim of continuous work since its timestamp. No web search is required for this internal exact proof audit.

## complete derivation or exact first unsupported line

REVIEW.md reconstructs the full exact-scope proof. First, actual squared child spectra average to the parent spectral marginal, so finite occupied support propagates to both physical children. Every nonconstant actual node has a positive source nonempty normalizer. Write Cal(R,z)=alpha R+beta delta_empty, alpha>0; beta can be negative and is never treated as a mixture weight. Marginalization fixes delta_empty, so every nonempty output atom and the entire output nonempty mass are scaled by the SAME alpha. Final calibration cancels alpha exactly: Cal(M Cal(R,z),w)=Cal(MR,w). Constant endpoints are explicit and no zero factor is canceled.

Reconstructing the sole dependency: the subprobability CE chain pays query erasures and all comparison terminals by c. At a first reset, source dominance and final calibration can only reduce CE. At a retained terminal, root likelihood domination plus weighted AM-GM pays nonempty and vacuum losses by L[(1-m)+m Var(leaf)], L=log2(1/gamma), m=P_g(empty). Finite law of total variance bounds their sum by(1-m^2)L. Prune at first reset nodes and replace each selected leaf by its whole continuation. Every subsequent ORIGINAL-source return is a CURRENT-reference calibration with signed cost minus binary KL. Hence the WHOLE finite tree remains <=c+(1-m^2)L, with no reset-count/depth factor and all old siblings/debits retained. This independently accepts both exact source theorem versions without repair; the integrated negative-cell18/7e dependency chain is NOT independently accepted here.

The check that would falsify an overbroad conclusion is also executed: after an actual parity3 query both children are nonconstant parity2; changing the conditional nonempty profile from occupied probability1/2 to1/3 costs log2(3)-1>1/2 bit (9>8). Thus arbitrary profile reoptimization is NOT free. An uncalibrated raw return is also outside the theorem. The exact next bill is (1-z)E_(P+)log2(Q+/R+) - D_Ber(z||Q(empty)), for prescribed R(empty)=z=P(empty), with all complete normalizers and ghost mass. For a constant node the shape term is absent. This reuses the campaign's minimal-target interface; it is not a newly invented source of credit.

First unsupported universal line: construct and pay a useful influence-priced source/likelihood floor for EVERY Boolean function, or at the immediate local frontier fund one genuine conditional-NONEMPTY profile change from a named unused original bank after a paid non-point query. The absorption identity supplies neither. Rung: analytic proof independently reconstructed with exact finite validation; NOT Lean-checked.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC precedes evaluation. Run python -X utf8 runs/{RUN.name}/code/check_return.py --pilot, then without --pilot. Pilot: all16 two-bit tables,48 supplied sources,192 ledger policies, {pilot['assertions']} assertions PASS in {pilot['runtime_seconds']:.6f}s. Main: {r['assertions']} exact assertions PASS in {r['runtime_seconds']:.6f}s. This differs from stage17's9152 assertions because it tests a different theorem and domain; pilot and main counts are separate, not added.

The rational census has330 eight-atom denominator4 laws, {a['pre_admissibility_tuples']} pre-admissibility tuples and {a['admissible_tuples']} checked identities, including {a['negative_affine_beta']} with negative affine beta. Endpoint exclusions are explicit actual-path/finite-CE conditions. Structural checks use ALL{s['Boolean_tables']} labelled three-bit tables, {s['source_roots']} supplied source roots and {s['physical_transitions']} checked physical transitions. Global CE validation uses32 declared Boolean fixtures and384 declared deterministic adaptive policies, not all possible three-bit trees; {g['positive_first_resets']} positive FIRST resets, {g['later_nonidentity_calibrations']} later nonidentity calibrations and {g['old_nonconstant_terminals']} old nonconstant terminal occurrences exercise the delicate cases.

Independent implementation uses integer butterfly Walsh transforms versus the author's direct character sums, separately counted pivotal edges, Fraction marginals/calibrations, exact law equality, and16-term outward rational atanh logs with explicit positive tail2z^33/[33(1-z^2)] and binary range reduction. No floating sign, parameter search, symmetry reduction, precision refinement or automatic dimension increase. Finite certificates corroborate the independent analytic proof; they are not extrapolated to all dimensions. Estimated memory110MB, peak unmeasured; no checker expected above300MB.

Fresh memok exited1: physical free1.3GB<4.0GB; commit free12.3GB>=8.0GB. Lean was NOT launched. KEY_STEP.lean contains only scalar normalization cancellation and is an unexecuted target, not a compiler/axiom certificate. The intake compute snapshot and later admission are different times, explaining the different physical-free readings. Existing render/agent work was left running; no GPU, remote compute, detached job, worker or schedule was created.

## proof dependencies and changed downstream conclusions

CLAIMS preserves original statements, versions and hashes for A096 first-frontier and A097 repeated-return, appending an independent exact-scope HOLDS record. No substantive repair is supplied, so this is an independent acceptance rather than a contributor reconstruction. The proof dependencies are acyclic: basic entropy/KL disintegration and finite total variance -> A096 first-frontier -> A097 absorption/tree extension. No acceptance of unrelated source-price, integrated activation assembly or full FEI is implied.

Milestone2: all100 latest packet sources are covered locally; canonical adoption and complete queue reconciliation remain unverified. Milestone4: quantitative restricted payments and rigorous obstructions continue. Milestone5: CHECKPOINT_ALLOCATION refreshes the six historical duplicate lanes and adds distinct source-bound next transactions using existing identities/capacity. Milestone8: supplied-reference history transfer is now all-dimensional, but its source-price hypotheses remain unpaid. Milestone9: the present complete supplied-reference dependency chain has a new independent reconstruction; other pending candidates still need exact-scope review. Milestone10: an exact open frontier and failed-route archive exist, while neither a complete accepted FEI proof nor a rigorous divergent Boolean ratio family is supplied by the inspected work. Current extended deadline remains controlling.

Our stage17 retained-off-branch NEXT is superseded by A096/A085/A097's newer results. A003's parallel vacuum absorption is compatible; alias the mechanism while preserving source provenance. A073/A026 point-source dummy grids are consumed, and no further vacuum-only return job is useful. Canonical-return charge improves by ZERO additional bits beyond the first-frontier allowance, rather than adding a reset-count tax. The universal FEI constant improves by zero. The source's conditional special-family18/7e margin is for a BROADER exit policy than its earlier18/12e policy, so these are distinct scope bounds, not a numerical correction; neither integrated assembly is independently certified by this run.

Allocation preserves productive A001 both-branch work, A045 complete merged reference, A040/A046 correlation-preserving non-point continuation and A089 signed donor repair. A073 now certifies actual changed-profile atoms rather than repeating dummy/calibration proofs. A097 constructs the weighted nonempty bill; A096 supplies the chosen non-point likelihood/payment interface; A003 guards old-bank ownership; A050 supplies the original correlated fixture; A085 falsifies; A099 updates the exact open leaves. A086 keeps its productive A011 second-edit review instead of being redirected to a closed return identity. All handoffs are LOCAL proposals for authorized supervisor adoption, not asserted external dispatch. No new broad candidate is opened under unresolved review-cap accounting.

## one next mathematical action and independent reviewer

On A050/A046's already paid non-point x/a history, fix ONE actual prescribed conditional-NONEMPTY child reference, record full incoming Q, old-quarter and accumulated reset debits, actual binary-KL refund, both complete terminal costs and the remaining original signed owner. Prove or refute payment of its weighted shape-minus-vacuum bill from that SAME unused allowance. A097 constructs; A050/A046 supply the fixture; A073 independently certifies atom/support quotients; A085 challenges and A094/A092 review. A098 next consumes that exact transaction, not another source-return grid.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA, REVIEW, frozen spec, independent checker/results, source census/change receipts, historical pending-status inventory, compute noncertificate and concrete allocation delta are local. out/SCHEMA_CHECK and MANIFEST validate exact protocol fields, original claim hashes, compatibility copy, two-line STATUS, required report sections and20MB ceilings by readback. Rolling WORKLOG/LEARNED append this stage. All research writes remain in A098. No shared source, other agent folder, brain store, git state, trading path, process workload or schedule is changed. Supervisor adoption, copies and remote mirrors remain unverified; these are the supervisor's authorized publication route. Session checklist bookkeeping is separate.

## Universal bridge

This stage advances C024 history transfer, feeding C019/C018, by independently accepting arbitrary repeated SAME-ORIGINAL-source canonical resets for every supplied Boolean source meeting the first-frontier hypotheses, at ZERO extra reset cost: final vacuum calibration absorbs all previous calibrations under marginalization. The proof includes the complete first-frontier dependency and all old siblings, ghost mass and erasure debits. Universal FEI improves by zero because generic source/likelihood pricing is still unpaid. The next actual conditional-NONEMPTY profile change on the inherited non-point A050/A046 source cannot be canceled by this identity; paying its precise signed likelihood quotient from the diminished original owner is the shortest available route to hereditary universal payment rather than another isolated point-source entropy result.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text(f'STATE: Stage18 saved: A097 repeated ORIGINAL-source canonical returns and A096 first-frontier independently HOLD; {r["assertions"]} exact checks PASS; FEI OPEN.\nNEXT: A097/A050/A046 pay ONE actual conditional-NONEMPTY profile reset from SAME diminished original bank, old debits/both terminals retained; A073 certify atoms; A085/A094 review.\n',encoding='utf-8')
for name,line in [('WORKLOG.md',f'{now} Stage18: independently reconstructed A096 supplied-likelihood frontier and A097 arbitrary repeated original-source calibrated-return theorem without repair; {r["assertions"]} exact assertions,9801 rational identities,384 declared ledgers PASS. Canonical returns cost zero after first reset; changed-profile parity guard positive. Consumed newer exit results, refreshed six historical lanes and distinct non-point conditional-NONEMPTY targets. Lean admission refused; no other work stopped. Full FEI OPEN.'),('LEARNED.md','Stage18: For any coordinate-deletion marginal M, Cal(M Cal(R,z),w)=Cal(MR,w) on the finite-CE actual Boolean-path domain. Affine beta may be negative; alpha>0 cancels only on a nonconstant node, while constant descendants use explicit vacuum laws. After first ORIGINAL-source reset every later calibrated return costs minus binary KL. A096 first-frontier source/floor bound c+(1-m^2)log2(1/gamma), m=squared mean, therefore extends to arbitrary repeated original-source returns with no reset-count factor. Full supplied-reference dependency chain independently reconstructed; integrated18/7e assembly remains conditional. Changing the conditional NONEMPTY law escapes absorption: parity2 occupied1/2 ->1/3 costs log2(3)-1>1/2. Next weighted shape-likelihood bill minus actual vacuum refund must use a genuinely unused original bank; universal supplier remains open.')]:
    with (OWN/name).open('a',encoding='utf-8') as f:f.write('\n'+line+'\n')
fields=set(protocol['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields
for c,original in zip(claims,sourceclaims):
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert c['exact_statement']==original['exact_statement'] and c['statement_sha256']==original['statement_sha256']
assert read(RUN/'PROGRESS.json')==read(RUN/'PACKET_DELTA.json')
assert len(read(OWN/'STATUS.md').splitlines())==2
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
save(OUT/'SCHEMA_CHECK.json',{'status':'PASS','progress_fields':'exact','claim_fields':'exact','report_fields':'all present','progress_equals_delta':True,'two_line_status':True,'source_statements_and_hashes_preserved':True,'result':r})
manifest=[]
for p in RUN.rglob('*'):
    if p.is_file() and p.name!='MANIFEST.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        manifest.append({'path':str(p.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(OUT/'MANIFEST.json',{'saved_at':now,'files':manifest,'remote_copy':'UNVERIFIED'})
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','assertions':r['assertions'],'local_files':len(manifest),'packet_sources':len(census),'changed_latest_sources':len(changes),'historical_claim_files':claimfiles,'queue_parse_failures':len(errors)}))
