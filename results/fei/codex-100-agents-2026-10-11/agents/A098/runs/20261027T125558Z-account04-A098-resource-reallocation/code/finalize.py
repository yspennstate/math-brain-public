from pathlib import Path
import json,hashlib,copy,datetime

R=Path(__file__).resolve().parents[1];O=R/'out';AG=R.parent.parent
CAN=Path(r'math-open-problems/reports\fei-2026-10-11')
def read(p):return p.read_text(encoding='utf-8-sig')
def put(p,s):p.write_bytes(s.encode('utf-8'))
def save(p,x):put(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
P=json.loads(read(CAN/'EXECUTION_PROTOCOL.json'))
census=json.loads(read(O/'PACKET_CENSUS.json'))
V=json.loads(read(O/'VALIDATION.json'));F=json.loads(read(O/'INTERFACE_FEE.json'))
assert V['status']==F['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()

# Consume the new complete A093 dependency after the initial board/intake snapshot.
a093=Path(r'agents\A093\runs\20261027T124307Z-account04-A093-literature-and-priority')
claims=[]
sources=next(x for x in census if x['packet']=='A097')['claims']+json.loads(read(a093/'CLAIMS.json'))
assert len(sources)==3
for source in sources:
 c={k:copy.deepcopy(source[k]) for k in P['required_per_run']['claim_fields']}
 assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
 c['review_records'].append({'reviewer':'A098','at':now,'verdict':'INDEPENDENT_ANALYTIC_RECONSTRUCTION_HOLDS_UNCHANGED',
   'source_statement_sha256':c['statement_sha256'],'proof':'REVIEW.md',
   'finite_checks':'out/VALIDATION.json and out/INTERFACE_FEE.json; different domains, counts not pooled as an exhaustive census',
   'scope':'A097 two full exact statements; A093 full finite guard by explicit fixture and analytic input/output/coordinate symmetry. No whole A011/A012 bundled acceptance.',
   'formal_verification':'NOT_LEAN_CHECKED'})
 c['status']='A098_INDEPENDENT_SCOPED_REVIEW_HOLDS_UNCHANGED';claims.append(c)
save(R/'CLAIMS.json',claims)

review=read(R/'REVIEW.md')
review=review.replace('This reviews the exact two A097 stage22 claims, not the entire A012 bundled claim or the A011 v5 statement.','This reviews the exact two A097 stage22 claims and the newly completed A093 forward-fee guard, not the entire A012 bundled claim or the A011 v5 statement.')
review=review.replace('## Exact forward-fee guard (A093\'s board candidate)',"## Exact forward-fee guard (A093's completed source)")
review=review.replace('This certifies the A093 BOARD candidate directly from literal Walsh sums and rational likelihood products; it does not accept an unseen completed A093 claim or assert novelty.','The completed A093 run20261027T124307Z DERIVATION sections1--3 and CLAIMS were subsequently read in full and byte-pinned in out/NEW_A093_SOURCE_RECEIPTS.json. This independently certifies A093-FORWARD-TRUE-KERNEL-HANDOFF-DEFICIT@1 unchanged (statement hash291b4429e2ae930044be8521ea95b4699c21ec26f27b41924b91f7cc884de33b), rather than treating a board summary as a proof. Input translations and output complementation change Fourier signs without changing the squared laws; they can swap the two actual children. Coordinate permutations preserve the symmetric AND3 law and uniform reference. Thus the full16-table/3-coordinate source scope follows analytically from the explicit fixture; our helper does not claim a48-query exhaustive replay. No novelty is asserted.')
put(R/'REVIEW.md',review)

updates={
 'A001':'Consume A051/A052 exact critical-child budgets to construct a well-founded original payment; do not substitute the FEI-equivalent demand CE<=C I as a proof.',
 'A011':'Preserve v6 inherited-policy payment. Any v5 fresh-floor interpretation must retain its actual query losses; for a REQUIRED switch from projection, pay A093 forward G from SAME unused owner.',
 'A012':'Consume A098/A097 full projection-ledger reviews; price only a REQUIRED true-kernel/other-interface switch using forward D(new||old) and actual G, retaining all query losses and old U.',
 'A040':'Bound cumulative selected-policy actual likelihood/conversion invoices from ONE original source; complete initial CE and both terminals remain charged.',
 'A045':'Preserve productive arbitrary-prime high-order payment after all existing carry/source debits. Do not restore retired half-tax work.',
 'A046':'Inherited continuation is paid at its stated scope. Compare only a REQUIRED positive floor/interface with inherited caps and charge its exact excess to actual original surplus.',
 'A047':'Supply a genuinely required terminal/interface constraint incompatible with inherited continuation; otherwise consume the original source/critical-child payment route.',
 'A048':'Preserve protected-anchor work and price a necessary anchor change/initial proper-core source. Ghost presence and reverse divergence alone are not actual forward fees.',
 'A050':'Decide one useful required policy interface: inherited true-kernel, projection+affine, or a paid switch. Keep complete original source and terminal surplus; do not label arbitrary switches affine.',
 'A051':'Preserve full conditional-Gibbs child bank; fund an ORIGINAL high-K block without dropping occupied divergence, Pi, old debit or complete child reserves.',
 'A052':'Exploit exact Boolean parity/child reserve beyond the current dimension-dependent threshold; fund one ORIGINAL pair when n is far above K.',
 'A056':'Price INITIAL original-spectrum/shared-label source using full Boolean convolution; transport is already paid within its exact interface.',
 'A062':'Retain indecomposable product-source obstruction; supply a nonproduct/affine-selected original owner and selected policy with full physical query bill.',
 'A070':'Use exact Boolean cancellation, not approximate norms, to fund an original-source Bellman payment with both child liabilities and all old debits.',
 'A073':'Preserve certified sign-boundary results; supply exact signs only for a REQUIRED new admission and actual forward fee. No optional precision-grid escalation.',
 'A079':'Preserve sharper latent-capacity progress; initial compatible nonproduct payment remains unpaid and inherited references do not renew latent credit.',
 'A082':'Test actual physical branch inheritance of the structured residual with full phase/outcome dependence; frequency-deletion closure is not child transport.',
 'A083':'Consume completed high-moment review and preserve the stronger all-coordinate guard; no additional dedicated moment-matching calibration job. Fund original source instead.',
 'A085':'Audit actual signed admission and fee orientation from CURRENT original B-C-U; reject double credit of prepaid mismatch and retain complementary terminals.',
 'A093':'Consume A098 independent full-scope forward-fee review; route G=(3/32)log2(5) as a charged interface guard, not a counterexample to either correctly scoped history theorem.',
 'A094':'Integrate A011v6 and A097/A012 with their DIFFERENT reference conventions; retain old-v5 objection only at its unrepaired fresh-floor interpretation and charge any required A093 forward G.',
 'A096':'Affine source projection is paid in the specified interface; construct a useful ORIGINAL source/structured branch inheritance rather than repeat moment constraints.',
 'A097':'Consume both A098 full statement reviews and A093 exact forward guard; transfer only allowed affine updates or charge required non-affine G from genuine remaining owner.',
 'A098':'At next checkpoint consume a noncircular original-source/critical-child invoice or a REQUIRED interface payer; preserve the exact query/fee convention before routing.',
 'A099':'Add exact A097 affine/full-query claims and A093 forward-fee guard; distinguish A011v6 inherited policies from projection policies, with original source and required switch unpaid.',
 'A100':'Propagate v5 query-loss objection, v6 inherited-policy repair and projection theorem as different exact scopes; do not keep a repaired inherited gap falsely open.'}
allocation=[]
for row in census:
 aid=row['packet'];native=row['status'].split('NEXT:',1)[-1].strip() if 'NEXT:' in row['status'] else 'Resume productive native packet with exact gap.'
 allocation.append({'packet_id':aid,'stream':'B'+str((int(aid[1:])-1)//5+1).zfill(2),
  'decision':'REFRESH_SOURCE_BOUND_NEXT_LEMMA' if aid in updates else 'PRESERVE_PRODUCTIVE_NATIVE_PACKET',
  'next_action':updates.get(aid,native),'source_report':str(a093) if aid=='A093' else row['latest_complete_report'],
  'adoption':'LOCAL_RECOMMENDATION_UNVERIFIED','capacity':'EXISTING_ONLY'})
save(R/'CHECKPOINT_ALLOCATION.json',{'at':now,'packets':allocation,'refreshed':len(updates),'preserved':100-len(updates),
 'new_workers':0,'new_schedules':0,'external_dispatch':False,'historical_duplicate_lanes':['A001','A040','A089','A045','A046','A073'],
 'rule':'Old duplicate jobs stay retired; preserve productive current native work, including A082/A090. Source-complete new dependency beats stale board status.'})

milestones=[]
for m in P['checkpoints']:
 text={2:'Baseline inherited;100 current packet sources mapped; no indexing-implies-acceptance claim.',
 4:'Exact restricted interfaces and rigorous route obstructions exist; this stage checks three source versions.',
 5:f'{len(updates)} distinct local source-bound next actions refreshed;{100-len(updates)} native actions preserved; no capacity added.',
 8:'Full projection/affine and inherited-policy mechanisms paid conditionally; noncircular original payment remains open.',
 9:'Three independent scoped reviews complete locally; full universal-chain review and supervisor adoption remain unverified.',
 10:'Universal proof or Boolean divergent counterfamily absent; final mathematical target NOT MET. Exact frontier and continuation saved.'}[m['day']]
 milestones.append({**m,'observed_status':'PARTIAL' if m['day']!=10 else 'FULL_TARGET_NOT_MET','evidence':text})
save(O/'MILESTONE_COMPARISON.json',{'at':now,'milestones':milestones,
 'deadline_reconciliation':'Protocol21-Oct and packet23-Oct historical endpoints preserved. Explicit27-Oct stage continuation creates no new schedule or clock.',
 'review_queue':'Review-only stage creates no new broad candidate. Latest-source census does not clear all archived pending claims.'})
save(O/'SCOPE_DELTA.json',{'old_v5':'A094 query-loss objection holds for its full-transaction reading.',
 'v6':'A011 repairs inherited-policy payment; do not route the old equation6 objection against a formula it no longer uses.',
 'projection':'A097 affine/full-fee history transfer holds in spectral-projection convention.',
 'forward_switch':'A093 exact positive G is an additional invoice when such a switch is actually required.',
 'universal':'Original influence-priced source/descent and useful compatible stopping policy unpaid.'})
save(O/'FORMAL_STATUS.json',{'status':'NOT_RUN_COMPUTE_DISTRESS','basis':'Observed disk-critical state,0.4GB free; no compiler or memok-required heavy job started.','rung':'Analytic reconstruction plus exact finite checks; not Lean-checked.'})
save(O/'OPERATIONAL_RECEIPTS.json',{'task':'T-20261027-074','working_exit_code':0,
 'useless_work':'Read-only scan completed; no demonstrated own duplicate work stopped. Other workers untouched.',
 'compute_snapshot':'2026-10-27 14:58:04 local;disk_critical;disk_free_gb0.4;mem_avail_mb4068;commit_used_pct89.9. This is a timestamped observation, not a claim it persisted.',
 'brain_selfcare':'DEGRADED_UNVERIFIED: model194.7h,state179.3h,dream51.7h stale at stage warning; excluded from mathematical premises.',
 'research_mutations':'A098 only; required checklist tool owns its external operational receipt.',
 'git_messages_brain_writes':'NONE','jobs_left_running':'NONE'})

progress={'protocol_revision':P['revision'],'run_id':R.name,'stream':'B20','packet_id':'A098',
 'gap_id':'C024-ARBITRARY-CORE-COMPATIBLE-TARGET-AND-ORIGINAL-PAYER',
 'attempt_id':'A098-stage22-full-query-affine-transfer-and-forward-fee-review',
 'method':'Independent finite analytic reconstruction, exact literal-Walsh/prime-log certification and source-bound checkpoint allocation',
 'mathematical_delta':'A097 affine/full-query transfer and high-moment witness hold unchanged; newly completed A093 forward-fee guard independently holds. Main41737 exact assertions;separate23 fixed-interface checks. Universal constant gain0.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'THREE_SCOPED_INDEPENDENT_REVIEWS_HOLD_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims],
 'claims_created_or_changed':[c['claim_id']+'@1 independent review only' for c in claims],
 'source_artifacts':['REVIEW.md','CHECKPOINT_ALLOCATION.json','out/MILESTONE_COMPARISON.json','out/SCOPE_DELTA.json','out/FROZEN_SPEC.json','out/PILOT.json','out/VALIDATION.json','out/INTERFACE_FEE.json','out/SOURCE_LEDGER.json','out/NEW_A093_SOURCE_RECEIPTS.json'],
 'next_consumers':['A011','A012','A050','A051','A052','A093','A094','A096','A097','A099','A100','B20 supervisor'],
 'next_action':'Fund one ORIGINAL critical-child/source invoice or a REQUIRED non-affine interface conversion; use actual forward G, query KL, old U and both full terminals. No repeated paid histories or moment matching.',
 'stagnant_substantive_attempts':0,
 'blockers':['Noncircular arbitrary-core initial source/selected descent unpaid.','Useful compatible terminal policy/necessary interface payer unpaid.','No Lean certification under compute distress.','Supervisor adoption,remote save and downstream use unverified.','Brain continuity notes stale; excluded from proof.'],
 'packet_ids':['A098']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)

report=f'''# A098 stage22: retain query losses; charge the correct interface fee

## exact target, quantifiers, hypotheses and units

Independently review A097's EVERY finite adaptive physical-query/affine-calibration history theorem in its specified projection convention and its EVERY even n>=4 actual Boolean high-moment control. Consume the newly completed A093 exact finite forward-fee objection. Compare the protocol checkpoints and reallocate distinct next lemmas within existing capacity. Units bits; uniform finite Boolean cubes. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD, B20 STREAM_NOTESv2, own STATUS/prior stage21 artifacts and protocol2026-10-11-execution-v2; latest REPORT/CLAIMS/PROGRESS and status for all100 packets. Detailed A097 PROOF1--4, A012 DERIVATION2--4/6, A011v6/A094 exact ledger sources, A052 current proof. Initial intake408 byte receipts plus3 newly completed A093 source receipts;100 latest report paths changed since the previous census. These are source-refresh counts, not newly proved theorem counts. Prior canonical campaign/index/supplement/four-paper intake is explicitly inherited from stage21; unchanged papers are not claimed reread or freshly audited. A093 current REPORT/DERIVATION/CLAIMS and A083/A050 current statuses were read after the first board snapshot; completed high-moment work is not assigned another dedicated job. Exact source locators and hashes are saved. No recalled background card is a premise and no new literature claim is made.

## complete derivation or exact first unsupported line

REVIEW.md reconstructs support-safe finite affine information projection, both-child physical KL/CE identities, the two-point bound and exact original-source telescope. The FULL bill is oldU+CEroot+sum reached JS minus paid-update slack; the extra constant stays2/ln2, with retired influence retained. A097's two registered statements hold unchanged. The high-moment family has H/I=2 and refutes only a local query-loss shortcut; it is not an FEI counterfamily.

The exact new source consumption is A093's forward-fee guard, also independently reconstructed unchanged: actual AND3 with original uniform reference CE=3=4I has a required-by-that-handoff update bracket averaged over BOTH children equal to(3/32)log2(5)>0. An integer-power certificate proves the sign. Input/output/coordinate symmetries analytically cover the full48-query source scope; our separate fixed-fixture checker does not claim an exhaustive48-query replay. AND2's reverse infinity is distinguished from its finite FORWARD1bit fee. Neither guard refutes the correct A011/A012/A097 theorem scopes or proves an original bank insolvent.

First unsupported universal line: a Booleanity-based noncircular ORIGINAL source/descent with useful terminal eligibility, or actual payment for a REQUIRED incompatible interface. A bare universal complete CE<=C I supplier is already FEI-equivalent. A011 old-v5 full-transaction objection, its v6 inherited-policy repair and A097's projection interface are distinct, not conflicting values of one ledger.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec saved before pilot. Commands from this run: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/interface_fee.py. Pilot PASS1585 assertions in0.119s, excluded from main. Main PASS{V['exact_assertions']} assertions in{V['seconds']:.3f}s:all278 labelled n0..3 roots,2412 direct reference queries,556 adaptive trees,5044 visited query nodes,2632 profile updates,11 affine/boundary fixtures,3 actual high-moment roots n4,6,8 with315 inclusion moments and15 erased-reference queries. Scalar masses1 and1/2, oldquarter, nonconstant optional stops and every terminal retained. Exact integer literal Walsh/Fraction/prime-exponent identities plus24-term natural-log intervals with proved remainder certify the checks. No numerical sign is treated as proof. Finite analytic arguments supply unrestricted dimensions, adaptivity and continuum parameters.

Separate interface helper PASS23 assertions on TWO fixed actual Boolean fixtures using rational likelihood products without author-helper imports. It certifies forward1/reverse-infinite AND2 and AND3 exponentiated child excess125. These23 checks are reported separately, not used to imply another exhaustive census. Stage21's122244 and this stage's41737 concern different frozen domains and are not cumulative or directly comparable.

Checks that could fail: affine minimizer boundary support, full fee direction, common projection reference on both children, actual query contraction, JS constant, mass penalty, old booking, unused terminal influence, Boolean realizability, moment order, and forward/reverse support. Each is treated in REVIEW and explicit fixtures. No compiler was launched under observed disk-critical distress; NOT Lean-checked. Estimated100MB; pilot/main caps55/180s; no >300MB job, GPU, detached work or automatic dimension escalation. The read-only operational scan found no demonstrated own duplicate to stop; existing workers stayed untouched.

## proof dependencies and changed downstream conclusions

CLAIMS.json preserves the exact three source statements/hypotheses/hashes and adds A098 independent review records only. A012 DERIVATION2--4 is accepted as a scoped dependency; no blanket acceptance of its bundled activation theorem or A011 numerical reserve is inferred. A093 was consumed from its complete source once it landed, rather than left as a stale board candidate. Source status, local acceptance, supervisor adoption and remote save remain separate.

CHECKPOINT_ALLOCATION covers100 packets:{len(updates)} source-bound next actions refreshed,{100-len(updates)} productive native actions retained. Six historical duplicate lanes remain retired from their old tasks while newer productive work survives. No new worker, schedule, external dispatch, git, message, shared index or brain-store mutation. Required operational checklist tooling owns its external receipts; research writes stay in A098. Review-only stage opens no new broad candidate and does not clear archival queues from latest-report counters. Historical deadline records are preserved; this explicitly requested27-Oct continuation changes no schedule.

## one next mathematical action and independent reviewer

A051/A052 fund an ORIGINAL high-K block invoice with exact genuine child reserves and unused quotient rank; A001 consumes that well-founded payment. A050/A011 separately state whether a useful policy NEEDS projection, inherited true-kernel, or a switch. A097/A012 pay only their allowed updates; a required switch must charge actual forward G from remaining original capacity. A094/A085 audit oldU, query KL and full complementary terminals; A099/A100 integrate and propagate the three exact scopes. Do not extend already-paid seed histories or moment-matching controls.

## actual persistence receipts or precise save blocker

The four exact-schema protocol files, review,100-packet allocation, frozen specification, two helpers, exact outputs, source hashes, scope delta and milestone comparison are local. code/finalize.py checks source statement hashes, exact protocol fields, byte-identical progress/delta, all required files<20MB and two-line STATUS, and writes out/PERSISTENCE.json. WORKLOG/LEARNED append this stage. Checklist completion receipt is saved separately after finalization; shared lock failure, if any, is an administrative blocker. Supervisor copying, mirrors, adoption and downstream use remain unverified.

Brain self-care remains degraded/unverified: stage wake warning reports personal-model194.7h, state-of-mind179.3h and dream51.7h stale; affected continuity guidance is excluded from mathematical premises. Snapshot at14:58:04 local reports disk_critical with0.4GB free,4068MB available memory and89.9% live commit; it is a timestamped observation, not a claim it persisted. No running work was stopped or throttled; all own mathematical checks ended.

## Universal bridge

C024 history transfer within C019 advances by independent full-scope acceptance of A097's affine/full-query payment and high-moment boundary, and by independent acceptance of A093's exact correct-direction interface invoice(3/32)log2(5). The transferred additive rate stays2/ln2 and the universal FEI constant improves by zero. Original Booleanity-based source/child-reserve payment and useful compatible terminal eligibility remain unpaid. NEXT targets one ORIGINAL critical-block invoice or one genuinely required interface payer, because generic histories and high moments are now accounted for and another optional calibration or isolated class cannot cross the universal bridge.
'''
put(R/'REPORT.md',report)
put(AG/'STATUS.md','STATE: Stage22 saved: A097 full-query affine transfer/high-moment and A093 forward-fee guard independently HOLD;41737 main+23 separate exact checks PASS;FEI OPEN.\nNEXT: A051/A052 fund ORIGINAL critical block; A050/A011 specify REQUIRED interface; A094/A085 audit actual forward G/query KL/old U/BOTH terminals.\n')
with (AG/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
 f.write(f'\n{now} Stage22 {R.name}:100 latest packets/408 initial source receipts;consumed3 new A093 source receipts after board snapshot. A097 affine full-query ledger/high-moment theorem and A093 exact forward guard independently HOLD unchanged.41737 main assertions/2412 queries/556 adaptive trees PASS;separate23 interface checks certify AND3 average3log2(5)/32 and AND2 forward1/reverseinfinite. {len(updates)} next actions refreshed;{100-len(updates)} native targets preserved. No compiler under disk-critical state. Original payment/required interface/FEI OPEN;mirror/adoption unverified.\n')
with (AG/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\nStage22 durable: projection-query payment must retain L=D(P||Q)-D(piP||piQ); CE child change is -B-L. Affine information projection containing true P pays its FULL forward fee exactly by target-KL decrease, including feasible boundaries and unchanged scalar mass. Full policy bill=oldU+CEroot+sum reachedJS-sum update slack, with JS<=2Inf/ln2 on retired influence. This is a supplied-source theorem. Reference conventions cannot be renamed freely: matched AND2 has infinite reverse but forward1bit fee; actual AND3/uniform root CE=4I has true-kernel replacement average G=3log2(5)/32>0. A093 full guard independently holds; positive G need not make an existing original bank insolvent. Oldv5 query omission, v6 inherited repair and projection theorem must travel as distinct scopes.\n')

assert set(progress)=={s.split(' (')[0] for s in P['required_per_run']['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(allocation)==100 and len({a['packet_id'] for a in allocation})==100
for c in claims:assert set(c)==set(P['required_per_run']['claim_fields'])
assert len(read(AG/'STATUS.md').splitlines())==2
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(O/'PERSISTENCE.json',{'status':'PASS_LOCAL_READBACK','at':now,'files':files,'schemas':'EXACT_PROTOCOL_FIELDS_PASS','source_statement_hashes':'PASS','remote':'UNVERIFIED','adoption':'UNVERIFIED','rolling':[{'path':str(AG/f),'sha256':sha(AG/f)} for f in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'status':'PASS_LOCAL_READBACK','claims_reviewed':len(claims),'main_assertions':V['exact_assertions'],'separate_interface_assertions':F['exact_assertions'],'packets':100,'refreshed':len(updates),'preserved':100-len(updates),'files_hashed':len(files)}))
