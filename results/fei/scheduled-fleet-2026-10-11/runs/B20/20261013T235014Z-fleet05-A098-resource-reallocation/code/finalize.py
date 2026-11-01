from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];OWNER=RUN.parents[1];TEAM=OWNER.parents[1];OUT=RUN/'out'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def readj(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,j): p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=readj(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
packets=readj(OUT/'PACKET_CENSUS.json');streams=readj(OUT/'STREAM_CHECKPOINT.json')
ledger=readj(OUT/'SOURCE_LEDGER.json')
source=TEAM/'agents/A001/runs/20261013T213937Z-fleet05-A001-quantifier-audit'
claim=next(c for c in readj(source/'CLAIMS.json') if c['claim_id']=='A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION')
extras=[TEAM/'claude/B20/SYNTHESIS.md',source/'REPORT.md',source/'CLAIMS.json',
 TEAM/'agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger/DERIVATION.md',
 TEAM/'agents/A073/runs/20261013T234148Z-fleet05-A073-certified-logarithms/REFUND_REVIEW.md',
 TEAM/'agents/A073/runs/20261013T234148Z-fleet05-A073-certified-logarithms/REPORT.md',
 TEAM/'agents/A023/runs/20261013T223305Z-fleet05-A023-amortized-rarity-budget/REPORT.md']
for p in extras:
 b=p.read_bytes();ledger.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'scope':'Critical source read for this stage'})
save(OUT/'SOURCE_LEDGER.json',ledger)
record={'reviewer':'A098','timestamp':now,'verdict':'ACCEPT_INFLUENCE_ONLY_REFERENCE_SUBCLAIM_ONLY',
 'scope':'A001 v1 final all-dimensional tribes orbit obstruction CE/I>=w/18, including labeled nonexchangeable influence-only rules. Earlier activated-parity, product-prior and bent-majorant clauses are not independently accepted by this record.',
 'method':'Independent orbit minimax reconstruction, canonical pairing enumeration, character-sum versus Walsh and physical-edge checks, exact factorized binomial certificates',
 'proof_source':str(RUN/'REPORT.md'),'validation_source':str(OUT/'ORBIT_REVIEW_CHECK.json'),
 'source_statement_sha256':claim['statement_sha256'],'reviewer_contributed_repair':False}
claim['review_records']=claim.get('review_records',[])+[record]
claim['status']='INFLUENCE_ONLY_REFERENCE_SLICE_INDEPENDENTLY_ACCEPTED_BY_A098; BUNDLED_OTHER_CLAUSES_PENDING_FULL_REVIEW'
save(RUN/'CLAIMS.json',[claim]);save(OUT/'REVIEW_RECORD.json',record)
save(OUT/'STATEMENT_HASH_NOTES.json',{'recorded_source_hash':claim['statement_sha256'],
 'recomputed_statement_hypotheses_hash':hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'policy':'Preserve source identifier; bind review to unchanged statement, hypotheses and byte-pinned source. Partial review is excluded from full-claim acceptance counts.'})
decisions=[
 ('A001','CONTINUE_PRODUCTIVE_NEW_MECHANISM',1,'B05 minimum-coordinate census','Use A073 accepted complete refund; propose one signed-Boolean lower bound for terminal-core divergence, retaining complete Q and one cross-degree budget. Do not repeat tensor/activation normalization.','A096/A073','A086/A094'),
 ('A045','CONTINUE_PRODUCTIVE_NEW_MECHANISM',1,'Singleton half-tax review','Construct one higher-degree reference using actual signed bias and empty-sector cancellation; include the complete normalizer and terminal costs.','A041/A024/A096','A091/A085'),
 ('A073','CONSUME_NEW_SIGNED_BOOLEAN_CANDIDATE_WHEN_AVAILABLE',1,'AND/half-tax grid','Independently certify the first source-versioned terminal-core inequality from A001/A096 against complete Q. Refund normalizer is now accepted; cyclic-code recovery remains a separate input blocker.','A001/A096','A085/A092'),
 ('A040','CONSUME_NEW_DEPENDENCY_FOR_REVIEW',2,'B05 minimum-coordinate census','Independently reconstruct A023 all-width three-event single-separator reserve, including terminal entropy and Q_bad<=I-d_X; no reuse of the reserve at multiple ancestors.','A023 stage3 REPORT','A088'),
 ('A046','CONTINUE_LOCALIZED_PAYMENT_TEST',2,'Singleton half-tax review','Stress-test extension of the three-event reserve to a multi-bit separator using one physical account and signed output/spectral correction. Freeze finite cases before computation; report first reused reserve or a valid layer transport.','A023 stage3 REPORT/A050 accepted refund','A087/A092'),
 ('A089','PRESERVE_PRODUCTIVE_UNFINISHED_NATIVE_PACKET',None,'B05 minimum-coordinate census','Finish fixed-K six-bit witness admission audit with all newly relevant coordinates and original influence cutoffs. Consume localized-reserve work only after this productive packet; no forced rotation.','A089 stage2 REPORT/A090 tail theorem','A090/A094')]
deltas=[]
for aid,action,route,old,target,dependency,reviewer in decisions:
 p=next(x for x in packets if x['packet_id']==aid)
 latest=next((x['path'] for x in reversed(p['runs']) if x.get('files',{}).get('REPORT.md')),None)
 deltas.append({'packet_id':aid,'action':action,'retired_duplicate_obligation':old,'route':route,
  'distinct_next_lemma':target,'source_dependency':dependency,'independent_reviewer':reviewer,
  'current_status':p['status_text'],'current_report':latest,
  'observed_downstream_use':'EXPLICIT_A098_RETIREMENT_RECEIPT' if aid in ['A001','A040'] else 'DISTINCT_PRODUCTIVE_WORK_OBSERVED; deployment not inferred',
  'deployment_status':'LOCAL_SOURCE_BOUND_DISPATCH_ONLY; supervisor adoption unverified'})
save(RUN/'CHECKPOINT_ALLOCATION.json',{'run_id':RUN.name,'snapshot_at':now,
 'capacity':{'streams':20,'packets':100,'new_workers':0,'new_schedules':0,'retired_duplicate_obligations':6},
 'keepers':{'minimum_ratio_calibration':'A082','singleton_half_tax_review':'A090'},
 'packet_deltas':deltas,'all_packet_coverage':[{'packet_id':p['packet_id'],'stream':p['stream'],
 'action':'SOURCE_BOUND_REFRESH' if p['packet_id'] in [d['packet_id'] for d in deltas] else 'PRESERVE_NATIVE_PRODUCTIVE_WORK_AND_REVIEW_GATE',
 'status':p['status_text']} for p in packets],
 'stream_review_evidence':streams,
 'guard':'Resume productive work; consume new dependencies; no broad candidate at the genuine complete-unreviewed cap. Snapshot hash joins are navigation evidence, not proof audits.'})
def totals(s):return {'packets_with_status':sum(x['packets_with_status'] for x in s),
 'complete_local_runs':sum(x['complete_runs'] for x in s),
 'exact_scope_review_match_ids':sum(len(x['exact_statement_review_matches']) for x in s),
 'source_complete_unmatched_ids':sum(len(x['source_complete_unmatched_candidates']) for x in s)}
previous=readj(OWNER/'runs/20261012T024601Z-fleet05-A098-resource-reallocation/out/STREAM_CHECKPOINT.json')
comparison={'previous':totals(previous),'current':totals(streams),
 'claim_records':len(readj(OUT/'CLAIM_CENSUS.json')),'sources':len(ledger),
 'milestones':[{**x,'assessment':('PARTIAL: all100 packet coverage and closed-fragment reuse; full baseline adoption, dependency review and nonduplication not globally verified' if x['day']==2 else 'NOT_YET_DUE at stage timestamp; route obstructions and review handoffs prepared')} for x in protocol['checkpoints']],
 'limits':'Not atomic; unique claim IDs collapse versions in stream totals. Stale/superseded claims and scoped results require human queue triage. Never infer workers, wall-time capacity or whole-claim acceptance from a partial verdict.'}
save(OUT/'CHECKPOINT_COMPARISON.json',comparison)
checks=readj(OUT/'ORBIT_REVIEW_CHECK.json')
report=f'''# A098 stage 3: checkpoint refresh and influence-only reference obstruction review

## exact target, quantifiers, hypotheses and units

Compare actual post-Day-2 mathematical outputs with the protocol milestones and refresh six previously retired duplicate obligations within twenty native streams and 100 logical packets. Preserve productive work, especially A089's unfinished six-bit admission audit. Saved handoffs do not modify shared indices, other agents or schedules.

Independently review only the final influence-only-reference clause of A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION@1. For every integer w>=2, put k=2^w and n=kw. Let f be the sign of OR of k disjoint width-w point conjunctions. For any single complete spectral subprobability Q used for every coordinate permutation of f, some permutation has CE(P,Q)/I(f)>=w/18. Equal labeled influences force an influence-only rule, even a nonexchangeable rule, to use this same Q. All entropy and CE are in bits; I is ordinary physical flip influence. This is a mechanism obstruction, not an unbounded H/I family or a FEI disproof.

## sources actually read, revisions and theorem locators

At stage start read BOARD snapshot 2026-10-13 23:49 UTC, own STATUS, and B20 STREAM_NOTES v2 (2026-10-11 23:39Z), then SYNTHESIS. The lead's six retirements remain valid, but its T12 and low-influence frontiers are stale relative to current proofs; this report consumes the newer results rather than restarting those targets. Protocol 2026-10-11-execution-v2 was read in full. The read-only intake ingested canonical README/status/registries/packet actions/plan and earlier reports, supplemental campaign and source files, all available context manuscript text versions, and all 100 packets' reports and metadata. SOURCE_LEDGER pins {len(ledger)} read receipts; machine intake is navigation, not an independent audit of every theorem.

Critical mathematical originals read: A001 stage3 REPORT sections 2-5 and CLAIMS; A096 stage3 DERIVATION equations (1)-(6), cutoff and unpaid-line sections; A073 stage3 REFUND_REVIEW and REPORT, complete Q and support-conditioning mutation; A023 stage3 REPORT, all-width three-event controller reserve and terminal entropy. Six affected packets' latest reports/statuses were compared. The intake caught A073's report finalized at 23:51 UTC, newer than BOARD: the initially apparent stale lane is now productive and the refund audit is independently accepted. Original files were never changed or imported as executable code.

## complete derivation or exact first unsupported line

**Independent orbit minimax reconstruction.** Let P_pi be the squared Fourier law of a coordinate permutation, and let barP average these laws over all permutations. For any subprobability Q of mass z<=1, linearity and Gibbs give

    max_pi CE(P_pi,Q) >= CE(barP,Q)
                     = H(barP)+D(barP||Q/z)-log2(z) >= H(barP).

Zero mass on a positive barP atom gives infinite CE and is handled directly. The averaged law is uniform within each degree: barP(S)=W_|S|/binom(n,|S|). Every P_pi has identical degree totals W_d. Consequently CE(P_pi,barP)=H(barP) for every pi, and Q=barP is admissible. Thus the exact minimax identity is

    inf_{{Q: sum Q<=1}} max_pi CE(P_pi,Q)
       = H(barP) = H(W)+sum_d W_d log2 binom(n,d).        (1)

This reconstructs the obstruction independently and also identifies its exact reference optimum. It does not assume Q itself is exchangeable; symmetry enters the averaged actual Boolean laws. For influence-only rules the reference is held fixed across this orbit, since each coordinate's influence is the same and permutation-invariant metadata are unchanged.

**All-width Boolean lower bound.** Write delta=1/k and A_j for each block point indicator. For f=1-2[1-prod_j(1-A_j)], every Fourier atom supported on a nonempty subset T of exactly one block has squared magnitude 4 delta^2 (1-delta)^{{2(k-1)}}. There are k binom(w,m) such atoms of degree m. Disjoint block supports prevent double counting. Hence the mass in these atoms with m>=ceil(w/2) is

    4k delta^2 a sum_{{m>=ceil(w/2)}} binom(w,m),
    a=(1-1/k)^{{2(k-1)}}.

The binomial sum is at least 2^{{w-1}} by complementary pairing. Integrating 1/(1-t)<=1/(1-u) on [0,u] gives ln(1-u)>=-u/(1-u), so a>=exp(-2)>1/9. The latter follows from e<3: j!>=2^{{j-1}} for j>=2, strict at j=3, bounds the exponential series by 3. Thus the specified spectral mass is at least 2/9.

For these degrees, binom(n,m)=prod_{{j=0}}^{{m-1}}(n-j)/(m-j)>=(n/m)^m>=k^m, since m<=w. Therefore log2 binom(n,m)>=wm>=w^2/2. All other degree-location terms and H(W) are nonnegative. Equation (1) is at least w^2/9.

A coordinate is pivotal exactly when its other w-1 block bits are positive and every other block fails. Its influence is 2delta(1-delta)^{{k-1}}, equal for all n coordinates. Consequently I=2w(1-delta)^{{k-1}}<=2w. Combining these identities gives, for some coordinate permutation and every common Q,

    CE(P_pi,Q)/I >= w/18.

All quantities come from actual Boolean functions. No finite-width extrapolation is used: the preceding derivation holds for every integer w>=2. The independent record accepts this clause without repair. It does not accept the other three clauses bundled in A001@1, and is deliberately excluded from full-claim queue acceptance.

**Current universal frontier.** A096's T12 payment was already independently accepted by A098 stage2. A090's parity-tail low-influence completeness is now independently accepted by A096. A073 has independently accepted A096's terminal-inclusive refund and demonstrated that conditioning Q on derivative support removes the activation refund. These are consumed, not rederived here. The first unpaid line for the complete joint reference P(i,T)=p_(T+i)/I, Q(i,T)=(e_i/I)(p_T+p_(T+i)) is

    D(P_f||Q_f) >= sum_i (e_i/I)log2(1/e_i) - K          (OPEN)

for one finite K and every terminal Boolean f. Equivalently M<=KI, with M<=B<=M+I/ln2. The root and T12 erasure layers are paid; R_ge2 remains unpaid. The orbit obstruction excludes a complete spectral reference based only on influence data; it does not exclude this function-specific conditional-edge reference or retained-KL payment. Activation refunds its own rarity while retaining the arbitrary seed bill.

For route 2, A023's three-event single-separator calculation gives Q_bad<=I-d_X and retains terminal core entropy. Its reserve is spent once: repeating it at arbitrary-depth separator ancestors is the first unsupported extension. A040 is assigned reconstruction of that precise result; A046 tests its multi-bit reserve transport. Neither task assumes the universal extension.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC was saved before computation: helper A098-independent-orbit-v1; all 105 unlabeled perfect matchings on eight coordinates (w=2,k=4), and exactly seven factorized widths 2,3,4,6,8,10,12. Least-unused-coordinate recursion enumerates each matching once; block names and within-block order do not change the function. No atom symmetry is assumed in the checker. Integer Walsh transforms are independently checked against direct character sums for all 256 atoms and against physical flip counts. Exact Fraction orbit averages are checked uniform at each degree; every orbit law has the same degree totals, certifying the symbolic equality CE(P_pi,barP)=H(barP). Fixed symbolic cases check mass, integer-power and binomial inequalities; they are controls for the analytic all-width proof, not its substitute.

Executed commands from A098:

    python -X utf8 runs/{RUN.name}/code/intake.py
    python -X utf8 runs/{RUN.name}/code/orbit_review.py pilot
    python -X utf8 runs/{RUN.name}/code/orbit_review.py

Pilot: one actual Boolean case, 266 checks, 0.220 seconds. Full pass: 105 actual orbit cases plus seven factorized cases, {checks['assertions']:,} assertions, {checks['runtime_seconds']:.3f} seconds, PASS. Each completed case was flushed to disk immediately. At w=2 every influence is 27/128 and I=27/16; all exact averaged masses are in ORBIT_AVERAGE.json. No floating entropy estimate, author helper import, dimension escalation, background task or new worker was used. Memory estimate 60 MB, not measured peak; no >300 MB job was planned, so memok was not required. Frozen runtime limit 55 seconds was enforced.

## proof dependencies and changed downstream conclusions

The reviewed slice is reconstructed from Fourier character orthogonality, physical pivotal counting, finite permutation averaging, subprobability Gibbs and elementary binomial/log inequalities. No unreviewed FEI bound is a proof premise. CLAIMS preserves A001@1's unchanged bundled statement and recorded source hash, appending only a partial independent review. STATEMENT_HASH_NOTES stores the separate statement-plus-hypotheses digest; differing historical identifiers are not mathematical refutations.

Day-2 baseline checkpoint assessment is PARTIAL, not passed globally: all 100 packets have status coverage, recovered fragments are reused and the six duplicate tasks have moved to distinct work, but global baseline adoption, dependency review and complete nonduplication are not verified. Source-complete unmatched records remain in every stream; stream-specific exact matches and conservative review gates are saved. Counts include historical/scoped candidates and are not an audited number of genuinely pending broad candidates. At the cap, resume, repair or review before opening another broad candidate.

CHECKPOINT_ALLOCATION records source-bound refreshes: A001 signed-Boolean terminal-core candidate, A045 signed-bias normalized reference, A073 certification of the next sourced candidate, A040 single-separator reserve review, A046 multi-bit reserve test, and A089 productive six-bit admission kept ahead of any new route-2 work. A082 remains the sole minimum-ratio calibration lane and A090 the singleton endpoint review lane. A001 and A040 explicitly cite A098 retirement; the other four have distinct productive outputs, which is observed alignment rather than claimed deployment. The other 94 packets retain native productive work and review gates. No extra authorized capacity is inferred. Day-4 quantitative obstructions are now available; Day-5 reassignment recommendations are prepared early, not declared deployed.

## one next mathematical action and independent reviewer

Consume one source-versioned signed-Boolean lower bound for the terminal-core divergence with complete Q and one cross-degree influence ledger. A001/A096 own its mathematical construction; A073 certifies its normalizer and decisive signs. A086/A094 independently reconstruct the remaining clauses of the A001 bundle and challenge this orbit review. A040's distinct review consumes A023's current single-reserve theorem; A046 tests the first multi-layer extension. Do not repeat T12, activation refund, tail completeness or bounded-family argmin searches.

## actual persistence receipts or precise save blocker

This run saves REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA, FROZEN_SPEC, CHECKPOINT_ALLOCATION, independent code and exact outputs. Schema/readback and SHA256 receipts are generated in out/SCHEMA_CHECK.json and out/MANIFEST.json. Rolling STATUS has two lines; WORKLOG appends this stage and LEARNED saves the durable theorem and scope limits. Every write is under A098. Local file completion is distinct from independent review, shared-registry adoption, mirror verification and downstream mathematical use. Supervisor adoption and remote copies remain unobserved, not blocked by a requested permission.

## Universal bridge

This stage moves C018 by independently closing the influence-only complete-reference obstruction slice, with exact worst-case orbit cost H(barP) and the all-width CE/I>=w/18 lower bound; the universal constant improves by exactly zero. Root/T12 payment and normalized terminal-refund transport are already closed fragments. What remains is a signed-Boolean terminal-core divergence lower bound, equivalently a single uniform payment of R_ge2, and for route 2 a separator reserve conserved across layers without repeated spending. NEXT targets that retained terminal bill using complete function-specific Q because influence-only priors, more rarity refunds and another bounded-ratio census cannot pay it. This is the shortest surviving route to full FEI rather than another isolated class result.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B20','packet_id':'A098',
 'gap_id':'G-BOOLEANITY','attempt_id':'A098-stage3-checkpoint-orbit-review',
 'method':'100-packet checkpoint census, source-bound nonduplicate dispatch refresh, independent Boolean orbit minimax reconstruction',
 'mathematical_delta':'A001 influence-only complete-reference slice independently accepted: CE/I>=w/18 for all w>=2; exact orbit minimax H(barP). Consume A073 accepted terminal refund; full FEI open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_ADOPTION_PENDING',
 'mathematical_status':'SCOPED_OBSTRUCTION_SLICE_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':claim['claim_id'],'version':1,'scope':'Influence-only reference clause only'},
 {'claim_id':'A096-TERMINAL-KL-REFUND-AUDIT','version':1,'scope':'A073 independent acceptance consumed for dispatch; not a proof premise'},
 {'claim_id':'A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS','version':1,'scope':'A096 review consumed; no repeat audit'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'Partial independent acceptance only; full bundle still pending'}],
 'source_artifacts':['out/SOURCE_LEDGER.json','out/PACKET_CENSUS.json','out/CLAIM_CENSUS.json','out/STREAM_CHECKPOINT.json','out/CHECKPOINT_COMPARISON.json','CHECKPOINT_ALLOCATION.json','FROZEN_SPEC.json','out/ORBIT_REVIEW_CHECK.json','out/ORBIT_AVERAGE.json','out/SYMBOLIC_SUMMARY.json','out/REVIEW_RECORD.json'],
 'next_consumers':['A001','A040','A045','A046','A073','A089','A096','A099','A100','A086','A094','B20 supervisor'],
 'next_action':'Consume one sourced signed-Boolean terminal-core KL payment with complete Q and one cross-degree budget; preserve productive admission work and complete remaining bundle reviews.',
 'stagnant_substantive_attempts':0,'blockers':['Universal terminal-core payment unproved','Multi-layer separator reserve unproved','Global baseline adoption and mirrors unverified'], 'packet_ids':['A098']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
(OWNER/'STATUS.md').write_text('STATE: Stage3 saved: A001 influence-only-reference slice independently accepted (CE/I>=w/18); 29,150 exact checks PASS; six dispatches refreshed, FEI OPEN.\nNEXT: A001/A096 signed-Boolean terminal-core KL payment with complete Q; A073 certify; A040 review single reserve, A046 test layers; preserve A089 admission.\n',encoding='utf-8')
with (OWNER/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} — Stage {RUN.name}: read updated board/lead and ingested 100 packets. Caught newly completed A073 refund review after board snapshot; avoid stale repeat. Independently reconstructed A001 influence-only reference slice via exact minimax orbit identity and all-width tribes lower bound; pilot 266 checks, full 29,150 checks/4.178s PASS. Partial acceptance only, bundle not closed. Refreshed six retired obligations, preserving A089 productive admission. Day2 checkpoint partial; no workers/schedules/shared writes. Full FEI open.\n')
with (OWNER/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage3: For the permutation orbit of any fixed squared Boolean spectrum, inf_Q(subprobability) max_pi CE(P_pi,Q)=H(barP)=H(degree)+E log2 binom(n,degree). Q may be label-dependent; the average law is the minimax optimum. On tribes with 2^w blocks of width w, one-block high-degree mass>=2/9 gives H(barP)>=w^2/9 while I<=2w, hence some orbit element CE/I>=w/18 for any influence-only rule. This is not FEI failure and does not exclude function-specific conditional-edge/KL references. A073 accepted A096 complete terminal refund; support conditioning deletes rarity credit. Read live reports after board because the board can lag a completed review. Preserve productive A089 admission rather than mechanically rotate. Partial bundle acceptance never clears the full-claim queue.\n')
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (RUN/'PACKET_DELTA.json').read_bytes()==(RUN/'PROGRESS.json').read_bytes()
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert len((OWNER/'STATUS.md').read_text().splitlines())==2
manifest=[]
for p in RUN.rglob('*'):
 if p.is_file() and p.name!='MANIFEST.json':
  b=p.read_bytes();assert len(b)<20*1024*1024
  manifest.append({'path':str(p.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(OUT/'SCHEMA_CHECK.json',{'status':'PASS','exact_progress_fields':True,'exact_claim_fields':True,'report_fields_present':True,'delta_byte_identical':True,'rolling_status_two_lines':True,'files_under_20MB':True})
save(OUT/'MANIFEST.json',manifest)
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','run':str(RUN),'checkpoint':comparison['current'],'checks':checks,'review':'PARTIAL_SLICE_ONLY'}))
