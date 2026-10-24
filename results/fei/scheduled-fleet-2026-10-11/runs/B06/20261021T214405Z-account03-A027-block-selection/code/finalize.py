from pathlib import Path
import json,hashlib,datetime
run=Path(__file__).resolve().parents[1]
home=run.parents[1]
old=home/'runs/20261014T104101Z-account05-A027-block-selection'
def write(path,text):path.write_text(text,encoding='utf-8',newline='\n')
def js(path,obj):write(path,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
v=json.loads((run/'out/validation.json').read_text(encoding='utf-8'))
ind=json.loads((run/'out/independent.json').read_text(encoding='utf-8'))
assert v['status']==ind['status']=='PASS' and v['cases']==400
lean_stmt='example (d b : ℝ) (hb0 : 0 ≤ b) (hb1 : b < 1/3) (hd0 : 0 ≤ d) (hd1 : d ≤ b) (heq : 1 - 4*b + 2*b^2 = 0) : 0 ≤ 1 - 4*d + 2*d^2 := by nlinarith [mul_nonneg (sub_nonneg.mpr hd1) (show 0 ≤ 4 - 2*(d+b) by linarith)]'
js(run/'out/lean_attempt.json',{'status':'RUNTIME_UNVERIFIED','elapsed_seconds':120.8,'lean_source_sha256':'34e7c0dbb85fbdf25208754deb1c2fa8a222d7e49f0c9e88edbe1a710fb46546','translation_fidelity':'UNVERIFIED','statement':lean_stmt,'rung':'No Lean certificate; analytic proof and rational certificate only','admission':'memok PASS before Mathlib hook; physical free12.5GB, commit free17.9GB','compiler_import_axiom_audit':'Not reached; no trusted formalization claim'})
js(run/'out/memok_receipt.json',{'observed_output':'OK: physical free 12.5 GB (need 4.0), commit free 17.9 GB (need 8.0)','scope':'Fresh admission for potentially>300MB Mathlib hook; exact Python jobs estimated<240MB','peak_memory':'unmeasured'})
claims=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8-sig'))
c=next(c for c in claims if c['claim_id']=='A027-PARTIAL-CORE-ACTIVATION-TRANSPORT')
extension=' Version 6 retains the prior scoped components and adds: let b=1-1/sqrt(2), F=1+((1-a)/2)(u-1), p=Pr(a=-1) in [0,1/4] union {1/2}, and d=Pr(u=-1)<=1/16. For EVERY finite actual core-only restriction tree with every complete terminal core bias<=b, Pi_H(F)-p Pi_H(u)=R(p,d)-E R(p,d_leaf)<=0. The same nonpositive correction holds at EVERY prefix frontier of that tree. Thus positive local activation debits are paid from ONE previously accumulated signed ancestor refund, while BOTH full activated terminal entropies and terminal influence p E I(u_leaf)+d I(a) remain. If the ACTUAL projected core decrement is independently paid at K and every complete activated terminal at L, the specified tree gives H(F)<=max(K,L) I(F). No controller query is permitted in this new endpoint clause. The actual seven-bit core with two core gates above the stage6 selector witness has d=7/128, final core biases0,3/16,1/4 and a positive selector correction; its original signed ancestor account pays it. A separate direct-character/rational certificate reproduces the positive debit and final negative correction. No universal paid core partition or terminal FEI certificate is inferred.'
c['version']=6;c['exact_statement']+=extension
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
c['hypotheses'] += ['For new endpoint clause: untouched disjoint controller p<=1/4 or p=1/2; root negative bias<=1/16; EVERY complete core leaf bias<=1-1/sqrt(2)', 'Core tree finite and physical; complete terminal entropy retained; no spectral-reference injection', 'Conditional FEI conclusion still requires independently paid actual core decrement K and complete terminal allowance L']
c['proof_source']=str(run/'DERIVATION.md')
c['proof_dependencies']=['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@5 (all previous scoped components retained)','A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@2 exact arbitrary-controller remainder','A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@5 curvature formula','out/validation.json exact tangent certificate','out/independent.json independent implementation of scalar/witness certificate']
c['review_records'].append({'reviewer':'A027 self-reconstruction only','verdict':'EXACT_INTERNAL_REPLAY_PASS; NOT_INDEPENDENT_ACCEPTANCE','scope':'new scalar tangent, eligible curvature comparison, actual positive-exit tree and full terminal ledger','evidence':['out/validation.json','out/independent.json'],'lean':'RUNTIME_UNVERIFIED; no compiler/axiom acceptance'})
c['status']='PROVED_LOCAL_ANALYTIC_AND_EXACT_CERTIFICATE; VERSION6_INDEPENDENT_REVIEW_PENDING'
c['supersedes']='A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@5 (retains all prior scoped statements)'
c['first_unproved_line']='Universal construction of useful proper core partition with paid core decrement and full activated terminals; unrestricted root/leaf biases and interleaved controller transfer remain open.'
c['next_consumers']=['A028','A029','A030','A064','A087','A094']
js(run/'CLAIMS.json',claims)
next_action='Insert one actual point-controller exposure between the saved ancestor core refund and positive selector exit; pay its channel and transfer the SAME original supporting-line account with both full terminals retained. Do not reset the account or assume core/terminal FEI.'
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B06','packet_id':'A027','gap_id':'G-R-SELECT','attempt_id':'A027-G-R-SELECT-017',
 'method':'Change from local signed-child funding to one global supporting-line ancestor refund; compare eligible controller curvatures; certify scalar tangent and actual positive-exit tree',
 'mathematical_delta':'Root bias<=1/16 plus complete leaf biases<=1-1/sqrt2 makes the full signed activation correction nonpositive for untouched controllers p<=1/4 or p=1/2, including all point controllers. Every actual prefix account remains nonnegative even across positive local exits; complete terminals retained. 400 cases/12757 assertions,84 positive exits; independent direct-character replay16 assertions.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT; VERSION6_REVIEW_PENDING',
 'mathematical_status':'ANALYTIC_ENDPOINT_PAYMENT_WITH_EXACT_SCALAR_CERTIFICATE; LEAN_RUNTIME_UNVERIFIED; FULL_FEI_OPEN',
 'claim_versions_used':['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@5','A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@2'],
 'claims_created_or_changed':['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@6'],
 'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','FROZEN_VALIDATION.md','SOURCE_READS.json','code/exact.py','code/check.py','code/independent.py','code/finalize.py','out/pilot.json','out/validation.json','out/independent.json','out/PILOT_FAILURE.json','out/lean_attempt.json','out/memok_receipt.json'],
 'next_consumers':['A028','A029','A030','A064','A087','A094'], 'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['No universal paid proper core decrement and complete terminal FEI certificates','New clause requires sparse root, endpoint bias band and untouched eligible controller','Version6 independent acceptance and supervisor mirrors unobserved','Lean hook timed out; no formal certificate'], 'packet_ids':['A027']}
js(run/'PROGRESS.json',progress);js(run/'PACKET_DELTA.json',progress)
report='''# A027 stage17: one ancestor refund pays a positive bias exit

The signed activation correction can be paid through a genuinely positive core query without renewing the controller reserve. The new endpoint criterion keeps one signed account nonnegative at every actual frontier. Full FEI remains OPEN: neither the core entropy decrement nor complete terminal entropy is automatically paid.

## exact target, quantifiers, hypotheses and units

For every Boolean core u and disjoint Boolean controller a under uniform physical input, put p=Pr(a=-1), d=Pr(u=-1), F=1+((1-a)/2)(u-1), and b=1-1/sqrt(2). Assume p in [0,1/4] union {1/2}, d<=1/16, and a finite actual core-only tree whose EVERY complete core leaf has negative probability<=b. Then Pi_H(F)-p Pi_H(u)<=0, including at every prefix frontier. Entropy is in bits; influence counts physical cube edges. All nontrivial point controllers are eligible. No controller bit is queried during this new clause.

The complete terminal influence is p E I(u_leaf)+d I(a). Both complete activated terminal entropies remain in the identity. A separately certified core decrement price K and complete activated-terminal allowance L give H(F)<=max(K,L)I(F) for this specified partition. This conditional conclusion does not supply K,L or a universal proper partition. The fixed example queries only three of seven core coordinates and leaves four core coordinates plus the original controller untouched.

## sources actually read, revisions and theorem locators

Read the full execution protocol2026-10-11-execution-v2, current BOARD snapshot2026-10-21 21:46UTC, B06 STREAM_NOTESv2, STATUS, LEARNED and WORKLOG. Inspected campaign README/CURRENT_STATUS, B06 actions/packet/claim/obstruction routing, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING, and prior A027 run inventory. The later10 local stage directories have no REPORT/PROGRESS products; the last substantive local source remains stage6. The user-provided campaign endpoint23Oct14:49UTC supersedes the older21Oct date printed in those source snapshots.

Read the full stage6 REPORT/DERIVATION and exact helper/checker, and prior progress/claim metadata. Consumed the version2 activation identity and version5 curvature proof, already reconstructed in the earlier substantive stages. Source-only readings: recovered BLOCK_RESTRICTION_IDENTITY sections1-3 and ERASURE_REDUCTION; threshold38pp Proposition8.6 equations75-79 (including empty data row), with earlier threshold and both percolation abstract/scope excerpts. These excerpts do not establish any imported universal theorem; no new percolation result is used. Text source bytes in those paper exports decode as cp1252, not UTF8; the failed initial UTF8 read is not treated as evidence of source corruption. SOURCE_READS records exact files and scope. The math-store two-wording recall returned generic restriction definitions and unrelated block-tree leads; none is a new proof dependency.

The wake reported stale personal-context sources (60.2h and44.8h), disclosed in commentary; no mathematical premise comes from them. Compute state was read, and the interventions ledger inspected. The latest sampled governor status was ok, available physical memory10925MB, commit availability15788MB and disk42.3GB. These sampled values differ from the later memok receipt because they are separate measurement times. No load was stopped or throttled.

## complete derivation or exact first unsupported line

DERIVATION supplies the all-dimensional analytic proof. The exact identity H(F)=pH(u)+dHplus(a)+R(p,d) cancels controller spectral entropy linearly over the ACTUAL core bias martingale. On d<=b, D(p,d)>=D(1/2,d) for p<=1/4: D decreases up to p=1/4, and D(1/4,d)-D(1/2,d)=(1/4)ln((1-d)^2/[d(2-d)])>=0. Thus R(p,d)/p-2R(1/2,d) is convex. The p=1/2 case is exact equality; p=0 and d=0 close separately without dividing by zero.

For A(d)=R(1/2,d), the tangent at s=1/16 supports A throughout [0,3/10]. A is convex up to d_star and concave thereafter; the ONLY extra scalar sign is A(3/10)-A(s)-(3/10-s)A'(s)>17/1000, certified by two independent rational log implementations. Smaller t<=s tangents also support A. Adding the convex comparison gives the supporting line for R at the actual root. Every frontier bias is a conditional average of its final descendants, hence stays<=b. Averaging the supporting line proves the signed correction nonpositive at every frontier. This is one conserved endpoint refund, not a new positive bank at each node.

The fixed seven-bit core places TWO actual core gate bits before the old selector with child biases3/16,1/4. Root bias7/128 is admitted, and all final biases are<=b. The selector has a strictly positive local correction; earlier core queries earn the refund paying it. With one independent dictator controller, original total influence19/64 equals queried15/128 plus full terminal23/128. Exact full spectra retain both nonconstant terminals. The independent replay gives positive local correction interval [5006565719671997/2305843009213693952,40052525757375977/18446744073709551616] and full signed correction interval [-49624143727981687/2305843009213693952,-396993149823853495/18446744073709551616]. Their signs are certified, not floating evidence.

First unsupported universal line: for an arbitrary Boolean function produce a useful proper core tree with paid core decrement and complete activated terminals while securing the root/endpoint conditions or paying their violation. A sparse root is not a free universal reduction, and small terminal bias is not a terminal FEI certificate. Interleaved controller queries change p and need a separate transfer argument. The omitted controller range(1/4,1/2) cannot be inserted into the curvature proof: p=3/8,d=2/7 gives D(p,d)<D(1/2,d). This refutes the intermediate curvature helper only, not the endpoint theorem on that omitted range or FEI.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC and FROZEN_VALIDATION precede their searches. Helper exact.py is pinned to a4e7bc617754627eefeeff73263ab12a8628fb660e16118aaa1c0e5dd3698217. Scalar discovery checks98 fixed expressions and does not supply the continuum proof. Main domain is all25 ordered pairs from five explicit four-bit child signs, gated behind two core bits, with16 actual labeled controllers (all eligible tables through2bits plus one3bit point controller):400 cases, maximum total dimension10, no symmetry quotient. Exact integer Walsh/Fraction spectra, independently counted physical edges, prime-log expressions and rational24-term atanh enclosures check complete identities, every prefix account, the retained original controller, and both terminals. The implementation clears bounded caches between controller groups.

From A027 run python -X utf8 runs/20261021T214405Z-account03-A027-block-selection/code/check.py --pilot; then the same command without --pilot. First pilot failed after the cases because uncached Hplus was included in cache cleanup; out/PILOT_FAILURE preserves it. Version1.1 removes that erroneous cleanup entry without changing the domain, hypotheses or arithmetic. Rerun pilot:4 cases,138 assertions PASS in0.113s. Full:400 cases,12757 assertions PASS in16.285s, including84 positive local exits. No failed mathematical assertion is hidden by the implementation repair.

Run python -X utf8 runs/20261021T214405Z-account03-A027-block-selection/code/independent.py. Separate direct character sums (no helper import), physical edges and32-term rational atanh enclosures reproduce the scalar tangent, positive selector debit, full negative correction and terminal ledger:16 assertions PASS in0.057s. This is an independent implementation by the same author, not an independent reviewer. These finite cases are not exhaustive over arbitrary cores or dimensions.

Each exact Python job has60s mathematical cap and expected memory<=240MB; peak RAM unmeasured. No GPU or automatic dimension increase. Fresh memok PASS before the potentially>300MB Mathlib hook: physical free12.5GB, commit free17.9GB. The required Lean hook attempted the key polynomial implication d<=b<1/3, 1-4b+2b^2=0 =>1-4d+2d^2>=0. It returned RUNTIME_UNVERIFIED after120.8s, source hash34e7c0dbb85fbdf25208754deb1c2fa8a222d7e49f0c9e88edbe1a710fb46546 and translation fidelity UNVERIFIED. No compilation, transitive-axiom acceptance or Lean proof is claimed. Rung: analytic proof plus exact scalar certificate; independent review pending.

## proof dependencies and changed downstream conclusions

Version6 extends the SAME A027 partial-core candidate, preserving prior scoped claims and refutations. It opens no separate broad candidate at the stream review cap. The new argument needs the existing exact remainder and curvature formula, not an unproved arbitrary-core FEI premise. It upgrades the stage6 local-safe-band mechanism to a signed ancestor payment across positive local exits under the explicit endpoint conditions. A028/A029/A030/A064 may retain one nonnegative signed refund account there; they still owe all core and terminal payments. No shared registry, other agent folder, brain record or remote mirror was mutated. Independent acceptance, index adoption and downstream use are unobserved.

## one next mathematical action and independent reviewer

Insert one actual point-controller exposure between the saved ancestor core refund and positive selector exit; pay its channel and transfer the SAME original supporting-line account with both full terminals retained. Do not reset the account or assume core/terminal FEI. A087 should independently reconstruct the scalar support and original-input reach weights; A094 should challenge controller-range exclusions, every-frontier conservation and full terminal bookkeeping. These names are handoff targets only; no external message or review receipt is asserted.

## actual persistence receipts or precise save blocker

All four protocol products, derivation, frozen specs, code and outputs are saved only inside A027. STATUS has exactly STATE/NEXT; WORKLOG and LEARNED append this stage. out/PERSISTENCE_RECEIPT verifies the exact protocol keys, statement hashes, identical PROGRESS/PACKET_DELTA, report fields and file sizes. Local artifacts are complete. Supervisor copying, remote persistence and independent acceptance remain unverified. Checklist entry T-20261022-010 is closed only after this local validation.

## Universal bridge

This stage moves C019 stopping-tree payment and C024 history transfer by replacing local safe-band sign checks with one original signed ancestor account. For root bias<=1/16 and final biases<=1-1/sqrt(2), eligible untouched controllers admit zero total activation surcharge at every frontier, even when an actual later query has a positive correction. The saved positive-exit witness is paid with both full terminals and the original controller owner retained. Universal paid core decrement, full terminal certificates, unrestricted bias geometry and controller interleaving remain open. NEXT transfers this same account through one real controller exposure; it addresses the remaining shared-history payment directly instead of adding another isolated class or assuming an FEI-equivalent proper selection theorem.
'''
write(run/'REPORT.md',report)
write(home/'STATUS.md','STATE: Stage17 locally complete: SAME ancestor refund pays positive bias exits under root/leaf criterion;400 cases/12757 exact checks+independent replay PASS;FEI OPEN,v6 review pending,Lean unverified.\nNEXT: Transfer SAME supporting-line account through one actual point-control exposure before positive DATA exit;retain both terminals;A087/A094 review v6.\n')
with (home/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write('\n'+now+' — '+run.name+': Replaced local exit-child funding by conserved supporting-line ancestor refund. Root<=1/16, leaves<=1-1/sqrt2, untouched p<=1/4 or p=1/2 imply every-frontier nonpositive signed correction. Actual positive selector exit paid with same owner and both terminals. Frozen pilot cleanup bug preserved/repaired;4cases/138checks PASS;full400cases/12757checks/84positive exits PASS;independent direct character16checks PASS. Lean algebra hook RUNTIME_UNVERIFIED120.8s after memok PASS. Samecandidatev6 awaiting A087/A094;full FEI/core and terminal payment OPEN.\n')
with (home/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('\n## Stage17: a single ancestor refund, not renewed local funding\n\nFor untouched disjoint controllers p in[0,1/4] union{1/2}, root core bias<=1/16 and EVERY actual terminal core bias<=b=1-1/sqrt2 imply Pi_H(F)-pPi_H(u)<=0 at EVERY frontier. Proof: D(p,d)>=D(1/4,d)>=D(1/2,d) on[0,b];the exact quarter-balanced difference is(1/4)ln((1-d)^2/[d(2-d)]). R(p,d)/p-2R(1/2,d) is convex. The balanced remainder tangent at1/16 supports through3/10 because its exact endpoint gap>17/1000 and its curvature changes once. Smaller root tangents also support. Bias martingale yields one nonnegative ancestor-refund account;positive local exits can spend it,with complete terminal entropy retained.\n\nActual two-core-gate lift of the3/16,1/4 sibling witness has root7/128,positive final selector debit,and full influence19/64=15/128+23/128.400cases/12757checks include84positive exits;separate direct-character32-term rational replay PASS16checks. Curvature comparison is FALSE atp3/8,d2/7:do not silently generalize to all controller biases. Small leaf bias supplies no FEI terminal certificate;theorem keeps core/terminal K,L premises and untouched-controller condition. Lean hook timed out120.8s:analytic proof+exact scalar sign,not Lean-checked. NEXT changes p by one actual control query while carrying this same original account.\n')
sourcepaths=[Path(r'~/brain_workers/FEI100_20261011/BOARD.md'),Path(r'~/brain_workers/FEI100_20261011/claude/B06/STREAM_NOTES.md'),old/'REPORT.md',old/'DERIVATION.md',old/'CLAIMS.json',old/'PROGRESS.json']
root=Path(r'~/mop_fei100/reports/fei-2026-10-11')
sourcepaths += [root/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
js(run/'SOURCE_READS.json',{'recorded_at':now,'read_scope':'Full protocol,board,B06 notes,own rolling state and stage6 derivation/report/code;campaign summaries and targeted B06 schema/routing/plan passages;paper abstracts/scope and threshold38ppProp8.6 only;not complete reread of all paper text','sources':[{'path':str(p),'sha256':sha(p)} for p in sourcepaths if p.exists()],'proof_imports':['A027 remainder identity@2','A027 curvature@5'],'math_recall':'One two-wording read-only query; generic/unrelated leads; no new premise'})
protocol=json.loads((root/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
cf=set(protocol['required_per_run']['claim_fields'])
assert all(set(item)==cf for item in claims)
assert all(item['statement_sha256']==hashlib.sha256(item['exact_statement'].encode('utf-8')).hexdigest() for item in claims)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert all(h in report for h in protocol['required_per_run']['report_fields'])
assert len((home/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in run.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipt={'status':'PASS','at':now,'protocol_schema':'exact keys checked','claim_statement_hashes':'PASS','delta_identical':True,'report_fields':'PASS','rolling_status_two_lines':True,'local_persistence':'verified','mirror_independent_review':'unverified','files':[{'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
js(run/'out/PERSISTENCE_RECEIPT.json',receipt)
print(json.dumps({'status':'PASS','files':len(files),'version':6,'main_assertions':v['assertions'],'independent_assertions':ind['assertions'],'full_FEI':'OPEN'}))
