from pathlib import Path
import json, hashlib, datetime, copy

R=Path(__file__).resolve().parents[1]; O=R/'out'; AG=R.parent.parent
CAN=Path(r'math-open-problems/reports\fei-2026-10-11')
def read(p):return p.read_text(encoding='utf-8-sig')
def put(p,s):p.write_bytes(s.encode('utf-8'))
def save(p,d):put(p,json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads(read(CAN/'EXECUTION_PROTOCOL.json'))
census=json.loads(read(O/'PACKET_CENSUS.json'))
validation=json.loads(read(O/'VALIDATION.json'))
assert validation['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()

# Reviews retain exact original statements, hypotheses and statement-only hash aliases.
claims=[]; source_receipts=[]
for aid,cid in [('A096','A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT'),('A097','A097-SIGNED-ARBITRARY-REFERENCE-FLOOR-OWNER')]:
    row=next(x for x in census if x['packet']==aid)
    original=next(x for x in row['claims'] if x['claim_id']==cid)
    cl={k:copy.deepcopy(original[k]) for k in protocol['required_per_run']['claim_fields']}
    assert hashlib.sha256(cl['exact_statement'].encode()).hexdigest()==cl['statement_sha256']
    verdict='INDEPENDENT_RECONSTRUCTION_HOLDS_UNCHANGED' if aid=='A096' else 'STATEMENT_HOLDS_WITH_POSITIVE_FACTOR_t_DERIVATIVE_ERRATUM'
    cl['review_records'].append({'reviewer':'A098','at':now,'verdict':verdict,
      'source_statement_sha256':cl['statement_sha256'],'proof':'REVIEW.md',
      'implementation':'code/check.py','exact_assertions':validation['exact_assertions'],
      'limits':'Analytic reconstruction and finite exact checks; no universal source or policy claim, no Lean certification. A097 displayed derivative needs factor t; conclusions unchanged.'})
    cl['status']=verdict
    claims.append(cl)
    src=Path(row['latest_complete_report'])
    for f in [src/'REPORT.md',src/'CLAIMS.json',src/('DERIVATION.md' if aid=='A096' else 'PROOF.md')]:
        source_receipts.append({'path':str(f),'sha256':sha(f),'bytes':f.stat().st_size})
save(R/'CLAIMS.json',claims)
save(O/'PROOF_SOURCE_RECEIPTS.json',source_receipts)
save(O/'LEAN_ADMISSION.json',{'command':'python -X utf8 lean_check.py --stmt "example (t a z : ℝ) (hz : z ≠ 0) (htz : t-z ≠ 0) : -a/z+(t-a)/(t-z)=t*(z-a)/(z*(t-z)) := by field_simp [hz, htz] <;> ring"',
 'exit_code':1,'output':'SETUP_UNVERIFIED: Compute admission held (hung window or under 5500 MB free); no new compiler process',
 'formal_rung':'NOT_LEAN_CHECKED','retry':'No retry without changed compute availability.'})
save(O/'RECALL_NOTE.json',{'tool':'math_recall.py','read_only':True,
 'queries':['Fourier entropy influence initial reference source KL stopping','Fourier spectral ghost witness inherited reference'],
 'conclusion':'Eight cards returned, mostly background or unrelated; no current ghost-source theorem supplied. No recalled card used as a proof premise; current local source proofs control. Older and newer LTF constants refer to different source versions and are not used here.'})

# Local source-bound recommendations only. No other packet, index or schedule is mutated.
tasks={
 'A001':('Construct a well-founded arbitrary-core original-source descent from nonnegative smaller-child reserves; retain all source-first conversion charges. A bare CE<=K I restatement is insufficient.',['A051','A052','A055'],'A094'),
 'A011':('Specify the minimum compatible arbitrary-core admission actually required by the adaptive policy, separating inherited witness transport from genuinely new within-cell conditionals.',['A096','A097'],'A094'),
 'A040':('Bound cumulative selected-policy actual outcome likelihood charges from one original source; retain full initial CE and every terminal. Do not reopen coordinatewise KL-price bounds.',['A049','A096'],'A049'),
 'A045':('Preserve productive arbitrary-prime high-order payment after all low/high-carry source debits; do not restore retired half-tax review.',['A044','A043'],'A091'),
 'A046':('Compare a REQUIRED floor with the actual inherited cap and moving-witness class; isolate only positive excess beyond inherited transport and price it from remaining original margin.',['A096','A097'],'A094'),
 'A047':('State a policy or terminal eligibility requirement that forces a stricter positive profile than inherited-cap continuation; otherwise close the optional-reset mechanism and consume original-source work.',['A046','A096'],'A050'),
 'A048':('Preserve productive protected-anchor replacement and its review; identify a necessary anchor change or useful original decomposition retaining nontrivial terminal entropy. Ghost presence alone is not necessity.',['A036','A096'],'A092'),
 'A050':('Decide exact compatibility of the ghost-complete inherited witness class with one useful stopping policy; write the first necessary stricter profile constraint, or accept inherited continuation and move to initial supplier/surplus.',['A096','A097'],'A047'),
 'A051':('Preserve critical-source descent: obtain an ORIGINAL high-K pair invoice funded by exact nonnegative smaller-child reserves and unused quotient rank, including mixed rows/Pi and all old debit.',['A052','A054','A055'],'A094'),
 'A052':('Use completed rank alignment to fund one ORIGINAL critical pair with genuine child reserves; route an explicit algebraic reserve inequality to A001 rather than another phase-optimality certificate.',['A051','A054','A055'],'A090'),
 'A056':('Price INITIAL per-set/shared-label source using full Boolean convolution; retain complete same-owner cost. Existing mark transport is not the next bottleneck.',['A070','A075'],'A091'),
 'A062':('Supply an original NONPRODUCT or affine-selected reference/payment for an indecomposable arbitrary core, preserving the full-support product-source obstruction and signed full terminals.',['A065','A087'],'A094'),
 'A065':('Consume the paid product-history mechanism and attack original indecomposable-core ownership; no additional automatic product-stop or product-return requirement.',['A062','A087'],'A094'),
 'A070':('Expose the precise full-Boolean convolution step needed for an original-source Bellman supersolution, retaining original bank and both children; test against normalized-real controls.',['A056','A069'],'A088'),
 'A073':('Review the already-funded finite refresh account at its current scope; pursue only a necessary compatible continuation or original source, not a larger optional refresh count.',['A050','A096','A097'],'A085'),
 'A075':('Fund the INITIAL signed coherent bank with the reduced paid drift and exact original ownership; singleton H+constant*I is still FEI-equivalent.',['A072','A089'],'A092'),
 'A079':('Retain latent-capacity obstruction while testing an inherited-marginal-closed NONPRODUCT family; distinguish source-zero ghosts from a genuinely incompatible required target.',['A032','A096'],'A094'),
 'A082':('Preserve floor-free affinity price and its supplied-account scope; test a necessary arbitrary-core conversion against actual unused surplus, not retired min-ratio calibration.',['A096','A097'],'A085'),
 'A085':('Independently review A097 signed arbitrary-current-reference price, correct derivative factor t, and verify positive/negative release cannot be booked twice.',['A097','A098'],'A094'),
 'A087':('Fund ONE selected physical terminal/reference rule; retain the obstruction to ALL-product-stop necessity. Review product repair only at its completed scope.',['A061','A064','A065'],'A094'),
 'A089':('Preserve productive coherent-bank source analysis; exploit Booleanity for initial payment rather than repeating already-paid coherence/gate drift.',['A072','A075'],'A092'),
 'A090':('Preserve source-normalizer/floor policy review; outside its admitted ratio, price a REQUIRED minimum projection from current owner. No new half-tax or min-ratio repetition.',['A004','A001','A097'],'A094'),
 'A094':('Audit one integrated source-to-terminal chain using ghost-complete transport and signed CURRENT admission, including old U, both terminal liabilities and any consumed negative release.',['A096','A097','A099','A098'],'A085'),
 'A096':('Consume A098 full-scope ghost review and connect one selected stopping surplus to full Boolean child reserves; inherited transport alone supplies no initial source price.',['A098','A051','A052'],'A094'),
 'A097':('Record the factor-t derivative erratum without changing the valid price; charge only a policy-required compatible floor to actual remaining original capacity and retain signed releases.',['A098','A050','A011'],'A085'),
 'A098':('At the next checkpoint consume the earliest original-source or policy-necessity proof/objection; check exact version and unused reserve, then route a distinct next lemma.',['A051','A052','A050','A097'],'A094'),
 'A099':('In the integrated DAG use the exact ghost-complete source version and signed current-reference floor; keep universal initial source and useful selected stopping surplus as unpaid leaves.',['A096','A097','A098'],'A094'),
 'A100':('Propagate source-bound derivative erratum and signed-release scope in local handoff artifacts; distinguish local review, supervisor adoption, remote save and downstream use.',['A098','A096','A097'],'A085')}
alloc=[]
for row in census:
    aid=row['packet']; num=int(aid[1:]); stream='B'+str((num-1)//5+1).zfill(2)
    if aid in tasks: action,deps,reviewer=tasks[aid]; decision='REFRESH_SOURCE_BOUND_NEXT_LEMMA'
    else:
        action=row['status'].split('NEXT:',1)[-1].strip() if 'NEXT:' in row['status'] else 'Resume productive unfinished native packet; require exact unpaid step before dispatch.'
        deps=[];reviewer='native independent reviewer';decision='PRESERVE_PRODUCTIVE_NATIVE_PACKET'
    alloc.append({'packet_id':aid,'stream':stream,'decision':decision,'next_lemma':action,
      'dependencies_from_packets':deps,'independent_reviewer':reviewer,
      'current_source_report':row['latest_complete_report'],
      'status':'LOCAL_RECOMMENDATION_SUPERVISOR_ADOPTION_UNVERIFIED','extra_capacity_authorized':False})
save(R/'CHECKPOINT_ALLOCATION.json',{'at':now,'packets':alloc,'existing_capacity_only':True,
 'new_workers':0,'new_schedules':0,'shared_mutations':0,
 'historical_duplicate_lanes':['A001','A040','A089','A045','A046','A073'],
 'historical_instruction':'Keep A082 calibration/A090 review ownership when relevant; do not overwrite productive newer work with the old 11-Oct assignments.',
 'dispatch_precedence':'Current source-bound productive next step supersedes stale initial routing, within existing native identity.'})
milestones=[]
for m in protocol['checkpoints']:
    day=m['day']
    result={2:'Baseline present; current local census maps100 latest reports and preserves distinct packet targets. No acceptance inferred from indexing.',
      4:'Restricted lemmas and rigorous route obstructions reported; this stage independently reviews two concrete all-finite-interface statements.',
      5:'28 local source-bound recommendations refreshed,72 productive native next actions preserved; no added capacity or external dispatch.',
      8:'Strongest surviving source/transport mechanisms continue; universal original source/descent and useful terminal eligibility remain open.',
      9:'Rolling independent review advances here for A096/A097. Two full-chain universal reconstructions remain unverified.',
      10:'Full FEI proof or Boolean counterfamily not present; accepted all-dimensional proof milestone NOT MET. Exact open frontier and continuation saved.'}[day]
    milestones.append({**m,'observed_status':'PARTIAL' if day!=10 else 'FULL_TARGET_NOT_MET','evidence':result})
save(O/'MILESTONE_COMPARISON.json',{'at':now,'milestones':milestones,
 'deadline_reconciliation':'Protocol/initial plan:2026-10-21T19:15:57Z; user packet:2026-10-23T14:49Z. Current user explicitly authorizes this26-Oct continuation stage. Neither historical endpoint is silently rewritten; no schedule is restarted or extended.',
 'latest_report_changes_since_stage20':len(json.loads(read(O/'CHANGED_SOURCES.json'))),
 'coverage':'100 latest-source packets; not an all-archive independent-acceptance census.',
 'review_cap':'Review-only stage opens no new broad candidate. Latest-source intake cannot certify retirement of every earlier unadopted candidate; preserve archival pending reviews.'})
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B20','packet_id':'A098',
 'gap_id':'C024-ARBITRARY-CORE-COMPATIBLE-TARGET-AND-ORIGINAL-PAYER',
 'attempt_id':'A098-stage21-ghost-transport-signed-admission-review',
 'method':'Independent analytic reconstruction, exact prime-exponent Boolean validation and source-bound checkpoint allocation',
 'mathematical_delta':f"A096 ghost-complete inherited transport holds unchanged; A097 signed floor statement holds with missing positive factor t corrected in displayed derivative. {validation['exact_assertions']} exact main assertions; no universal FEI constant improvement.",
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_INDEPENDENT_REVIEWS_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims],
 'claims_created_or_changed':[c['claim_id']+'@1 independent review only' for c in claims],
 'source_artifacts':['REVIEW.md','CHECKPOINT_ALLOCATION.json','out/MILESTONE_COMPARISON.json','out/FROZEN_SPEC.json','out/PILOT.json','out/VALIDATION.json','out/LEAN_ADMISSION.json','out/SOURCE_LEDGER.json','out/PROOF_SOURCE_RECEIPTS.json'],
 'next_consumers':['A096','A097','A050','A011','A051','A052','A085','A094','A099','B20 supervisor'],
 'next_action':'Consume an original-source/Boolean-child-reserve construction or a necessary stricter policy target; price it against exact unchanged original remaining capacity. Do not continue optional ghost-reset or refresh-count mechanisms.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal influence-priced original supplier/descent remains unproved; a complete CE<=K I source is already FEI-equivalent.',
             'Useful selected stopping surplus or necessary stricter compatible profile remains unpaid.',
             'Lean admission held for compute pressure; no compiler launched.',
             'Supervisor adoption, remote save and downstream use unverified.',
             'Wake stale personal-model/state/dream notes excluded from mathematical premises.'],
 'packet_ids':['A098']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)

report=f'''# A098 stage21: review inherited transport; reallocate to original payment

## exact target, quantifiers, hypotheses and units

Review every-finite-Boolean-tree ghost-complete transport and every-finite-law signed profile-floor admission at their exact supplied-source hypotheses. Compare all six protocol checkpoints with actual mathematical outputs and route distinct next lemmas inside existing A/B capacity. Bits; uniform physical cubes for Boolean statements. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2, all requested canonical indices and campaign plan, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and sources, all four context paper text versions, earlier canonical reports, current BOARD/B20 notes, all latest100 packet REPORT/CLAIMS/PROGRESS records, own prior reports and rolling files. The bounded intake records500 byte-hashed reads in out/SOURCE_LEDGER.json; latest-report paths changed for100 packets since the prior census. That source-refresh count is not100 newly accepted results. Exact A096 DERIVATION2--5 and A097 PROOF locators/hashes are in out/PROOF_SOURCE_RECEIPTS.json. Current proofs, not stale11-Oct routing, determine this stage. No external literature priority or freshness claim is made. Math recall returned background, not a supplier lemma; no card is a proof dependency.

## complete derivation or exact first unsupported line

REVIEW.md supplies an independent reconstruction of both full claims. A096 holds unchanged: zero rows admit one common stochastic completion, original witness labels survive, both reference outcomes normalize positively, and reached B+CE bills telescope against the SAME initial full allowance. A097's exact signed price and unique minimizer hold; its displayed derivative omits a positive factor t. Correct derivative is t(z-a)/(z(t-z)ln2), leaving every conclusion unchanged. The source is untouched. Signed negative conversion releases previously paid mismatch and cannot be booked twice. First unpaid universal line is an original Booleanity-based source/descent with a useful terminal policy, not another optional refresh. CE>=H makes a bare universal cheap complete source another FEI-equivalent target.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec saved before the pilot. Commands: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py, relative to this run. Pilot PASS5146 exact assertions in0.208s. First main PASS122234 in26.507s. One targeted extension added unequal-depth signed full-terminal/old-booking checks; final main PASS{validation['exact_assertions']} in{validation['seconds']:.3f}s, superseding the earlier main count (not added to it). Final domain:4824 direct query fixtures,512 complete adaptive trees,8408 visited query nodes,3488 true-zero erased rows and3712 biased reference-outcome nodes;112 rational floor laws/272 exact candidate comparisons. Literal character sums construct Boolean spectra independently. Fraction/prime-exponent identities and integer-product signs avoid floating logarithms. Analytic disintegration, log-sum inequalities and derivative signs supply the arbitrary-dimensional/continuum conclusions. Complete finite tree scope needs no limiting exchange.

The new owner checks retain reaches1/2,1/4,1/4, three full terminals, beta0 and nonzero old booking. The missing derivative factor is visible on238 off-minimizer grid instances. Lean check returned SETUP_UNVERIFIED because compute admission was held; no compiler started. Rung: analytic reconstruction plus exact finite checks, not Lean-checked. Estimated memory100MB, pilot/runtime caps55/180s, no expected>300MB job, GPU, dimension escalation or detached process. Existing work was not stopped.

## proof dependencies and changed downstream conclusions

CLAIMS.json preserves the two exact original claim versions and statement hashes, adding A098 review records only. A097 receives a local derivative erratum; neither registered conclusion changes. A096 is independently accepted at full stated scope. Initial source pricing and useful terminal eligibility remain open. CHECKPOINT_ALLOCATION maps all100 packets:28 current source-bound next lemmas refreshed,72 productive native actions retained. The six historical duplicate lanes remain retired from their old tasks without erasing newer productive work. A082/A090 current native work is preserved. No other agent folder, canonical index, brain, scheduler or external application is written. These are concrete supervisor handoffs; adoption and delivery are unverified.

Milestone comparison distinguishes partial baseline/lemmas/reallocation/review from the unmet final all-dimensional proof milestone. Protocol and user-packet historical endpoints differ; out/MILESTONE_COMPARISON preserves both and records the explicitly requested26-Oct continuation, without extending schedules. The broad unreviewed archive is not declared cleared from a latest-report census. This review-only stage opens no new candidate.

## one next mathematical action and independent reviewer

A051/A052 turn exact nonnegative smaller-child reserves and unused quotient-rank structure into one ORIGINAL critical-pair payment; A001 consumes that noncircular descent. A050/A011 separately specify a policy-required stricter profile if inherited witnesses do not suffice. A097 prices only that admission from actual remaining capacity. A085/A094 audit signed releases, all old U and both full terminal liabilities; A099 integrates the exact versions with the universal source/terminal leaves still open.

## actual persistence receipts or precise save blocker

All four protocol files, REVIEW,100-packet allocation, frozen specification, independent checker, pilot/final exact outputs, source hashes, milestone comparison and Lean hold are saved locally. code/finalize.py reads them back, checks exact schema fields, source statement hashes, byte-identical PROGRESS/PACKET_DELTA and per-file size<20MB, and writes out/PERSISTENCE.json. Rolling STATUS has exactly STATE/NEXT lines; WORKLOG/LEARNED append this stage. Supervisor copying, private mirror adoption and downstream mathematical use are unverified. Brain wake alerted stale personal-model179.1h, state-of-mind163.7h and partial dream36.1h; excluded from proof. Compute snapshot at22:40 local reports3.3GB disk free and91.6% live commit; aggregate private memory is led by Claude/Python/ffmpeg, not assumed idle. No resource-holder process was stopped or throttled.

## Universal bridge

C024 history transfer within C019 advances by an independent full-scope acceptance of arbitrary ghost-complete inherited transport and signed arbitrary-current-reference admission, with the derivative erratum isolated and all old bills/full terminals retained. The universal FEI constant improves by zero. The open original-source/Boolean-child-reserve payment and useful selected terminal surplus remain exact unpaid leaves. NEXT targets one original critical-pair reserve invoice or a genuinely required stricter admission, because inherited ghost continuation is now paid and another optional reset or restricted family cannot cross the universal bridge.
'''
put(R/'REPORT.md',report)
put(AG/'STATUS.md','STATE: Stage21 saved: A096 ghost-complete transport HOLDS; A097 signed floor statement HOLDS with factor-t derivative erratum;122244 exact checks PASS; FEI OPEN.\nNEXT: A051/A052 fund ORIGINAL critical-pair invoice from exact child reserves; A050/A011 specify REQUIRED stricter policy; A085/A094 audit SAME-owner old U/full terminals.\n')
with (AG/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
    f.write(f'\n{now} Stage21 {R.name}: read500 source receipts/100 latest packets. Independently reconstructed A096 arbitrary ghost transport and A097 signed current-reference floor; derivative missing positive t isolated, registered conclusions unchanged. Final122244 exact assertions/4824 query fixtures/512 adaptive trees PASS; ten added full-owner checks explain increase from122234.28 distinct next lemmas refreshed/72 native tasks preserved. Lean admission held, no compiler. Original supplier/necessary-policy surplus and full FEI OPEN; shared adoption/remote save unverified. No jobs stopped.\n')
with (AG/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\nStage21 durable: source-zero witness atoms do not force refresh when one common stochastic kernel is explicitly completed on zero erased rows. Positive true-law component ensures both reference outcomes>=b/2; SAME original CE pays reached B plus full terminal CE, with JS/erasure/outcome KL released once. A097 signed floor derivative is t(z-a)/(z(t-z)ln2), not the printed expression missing t; minimizer and prices unchanged. A floor crossing from an already mismatched current reference may release prepaid CE: do not re-credit it. A universal complete initial CE<=K I source already implies FEI; source pricing needs Booleanity or well-founded descent, not a new name. Keep policy necessity separate from optional reset insolvency and preserve both siblings/old debits.\n')

expected_progress={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for cl in claims:
    assert set(cl)==set(protocol['required_per_run']['claim_fields'])
    assert hashlib.sha256(cl['exact_statement'].encode()).hexdigest()==cl['statement_sha256']
assert len(read(AG/'STATUS.md').splitlines())==2
assert len(alloc)==100 and len({a['packet_id'] for a in alloc})==100
assert len(tasks)==28
assert sum(a['decision']=='PRESERVE_PRODUCTIVE_NATIVE_PACKET' for a in alloc)==72
assert read(R/'REPORT.md').rstrip().split('\n\n')[-2]=='## Universal bridge'
files=[]
for f in sorted(R.rglob('*')):
    if f.is_file() and f.name!='PERSISTENCE.json':
        assert f.stat().st_size<20*1024*1024
        files.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':sha(f)})
save(O/'PERSISTENCE.json',{'status':'PASS_LOCAL_READBACK','at':now,'files':files,
 'required_protocol_files_present':all((R/f).exists() for f in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']),
 'exact_field_sets_pass':True,'statement_hash_convention':'Preserve source statement-only SHA256 aliases.',
 'rolling_files':[{'path':str(AG/f),'sha256':sha(AG/f)} for f in ['STATUS.md','WORKLOG.md','LEARNED.md']],
 'remote_mirror':'UNVERIFIED','supervisor_adoption':'UNVERIFIED','all_writes_within_A098':True})
print(json.dumps({'status':'PASS_LOCAL_READBACK','claims_reviewed':len(claims),'packets':len(alloc),'refreshed_next_lemmas':len(tasks),'exact_main_assertions':validation['exact_assertions'],'files_hashed':len(files)}))
