from pathlib import Path
import json,hashlib,datetime

R=Path(__file__).resolve().parents[1]; A=R.parents[1]
ROOT=Path('~/brain_workers/FEI100_20261011')
SRC=ROOT/'agents/A012/runs/20261023T140756Z-account03-A012-sparse-activation-accounting'
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(p,text):p.write_text(text,encoding='utf-8',newline='')
def js(p,obj):put(p,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
audit=load(R/'out/AUDIT.json'); up=load(R/'out/U_POLICY.json')
assert audit['status']==up['status']=='PASS'
assert audit['certificate_sha256']==sha(SRC/'out/FULL.json')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
claim=load(SRC/'CLAIMS.json')[0]
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
claim['review_records'].append({'reviewer':'A086 account04, independent source reconstruction; no substantive repair of v9','at':stamp,'verdict':'HOLDS unchanged at stated signed-cost supplied-source scope','evidence':{'derivation':str(R/'DERIVATION.md'),'certificate':str(R/'out/AUDIT.json'),'prescribed_U':str(R/'out/U_POLICY.json'),'assertions':audit['assertions'],'independent_tensor_method':'sum of local Bellman entry potentials, global finite backward induction'},'limits':'No arbitrary-core initial source; no positive-part execution tariff; no Lean certification. State count is 2121 potential rows +108 mandatory conversion entries.'})
claim['status']='INDEPENDENT_RECONSTRUCTION_HOLDS_AT_V9_SCOPE; FULL_FEI_OPEN'
js(R/'CLAIMS.json',[claim])
paths=[SRC/x for x in ['REPORT.md','DERIVATION.md','CLAIMS.json','out/FULL.json','code/replay21.py','code/owner21.py']]
paths += [ROOT/'BOARD.md',ROOT/'claude/B18/STREAM_NOTES.md',A/'STATUS.md',A/'LEARNED.md',ROOT/'agents/A011/runs/20261027T025625Z-account04-A011-representation-existence/REPORT.md',ROOT/'agents/A011/runs/20261027T025625Z-account04-A011-representation-existence/DERIVATION.md']
paths += sorted((A/'runs').glob('20261023T140222Z*/REPORT.md'))
js(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths if p.is_file()])
js(R/'out/ATTEMPTS.json',{'initial_failures':[{'reason':'reviewer counted only ordinary potential records as all augmented states','observed':{'potential_rows':2121,'conversion_entries':108,'raw_restrictions':729},'mathematical_effect':'none; all reference and Bellman inequalities already passed before count assertion','repair':'count both reachable entry types; mathematical domain unchanged'}],'final_run':audit,'formal_check':load(R/'out/LEAN_ADMISSION.json')})
progress={
'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B18','packet_id':'A086','gap_id':'C024-ALL-PHYSICAL-POLICY-ORIGINAL-OWNER-REVIEW','attempt_id':'A086-stage22-A012-v9-independent-certificate','method':'Independent direct-character spectra, reachable augmented-state traversal, rational log enclosure, every Bellman edge, additive global tensor potential',
'mathematical_delta':'A012 v9 independently HOLDS unchanged: EVERY physical policy on the supplied six-bit block, margin>19/1024 and hence>1/64; prescribed U margin>3/5; all finite disjoint tensors/interleavings paid from SAME original account. No arbitrary-core supplier.',
'deliverable_status':'COMPLETE_LOCAL; MIRROR_AND_DOWNSTREAM_ADOPTION_UNVERIFIED','mathematical_status':'SCOPED_EXACT_CERTIFICATE_AND_ANALYTIC_TENSOR_PROOF; FULL_FEI_OPEN; NO_LEAN_CERTIFICATION',
'claim_versions_used':[{'claim_id':claim['claim_id'],'version':9,'statement_sha256':claim['statement_sha256']},{'claim_id':'A011 v6','scope':'report and derivation read to avoid repeating already accepted correction; not a proof premise'}],
'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':9,'change':'independent A086 HOLDS review; original statement unchanged'}],
'source_artifacts':[str(R/'DERIVATION.md'),str(R/'out/AUDIT.json'),str(R/'out/U_POLICY.json'),str(R/'FROZEN.json'),str(SRC/'out/FULL.json')],
'next_consumers':['A011','A012','A013','A094','B03','B18','B20'],
'next_action':'A011/A012/A050 supply ONE noncircular influence-priced INITIAL complete reference for arbitrary Boolean collision cores in a required hereditary interface, or specify a required stricter admission and pay all actual query KL/old debits/full terminals. A094 independently audits original ownership; do not extend this closed seed history.',
'stagnant_substantive_attempts':0,'blockers':['Universal arbitrary-core initial O(I) source remains unpaid.','Fresh memory gate refused compiler: physical5.0GB, commit3.6GB; no Lean process started.','Session wake executed but current-session complete health receipt not independently verified; no brain note adopted as premise.'],'packet_ids':['A086']}
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
report=f'''# A086 stage22: A012 all-policy source theorem independently holds

## exact target, quantifiers, hypotheses and units

Verdict HOLDS unchanged for A012-DISJOINT-PRIVATE-MUX-ADMISSION@9, statement SHA256 {claim['statement_sha256']}. Every deterministic adaptive physical stop/query policy on its actual six-bit supplied source is paid from SAME original K=4+2/ln2 account, old b=5/(4ln2) retained, mandatory CURRENT half-profile conversion charged in full, and every complete terminal retained. Margin>19/1024 bit implies the stated>1/64. Prescribed original U policy has margin>3/5. Every finite disjoint tensor and arbitrary interleaving inherits>m/64. Costs use SIGNED entropy increments plus actual complete conversion KL and terminal CE. Positive parts, extra execution fees, opaque arbitrary cores and new initial sources are outside this statement. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Full execution protocol2026-10-11-execution-v2, current BOARD05:25UTC, B18 notesv2 and A086 rolling handoff; complete A012 stage21 REPORT/DERIVATION/CLAIMS, full certificate and source checker passages; A011 stage22 REPORT/DERIVATION including withdrawal of v5 transaction interpretation. A031's board-reported acceptance made another v6 audit duplicative, so this stage consumes the still-requested A012 disinterested review. Campaign/supplement mandatory files and all four context texts were whole decoded for intake/hashes with targeted passages; this is not a new independent audit of those papers. INTAKE.json and SOURCE_RECEIPTS.json distinguish access from theorem reconstruction. One read-only math recall returned no adopted premise.

## complete derivation or exact first unsupported line

DERIVATION.md gives actual truth-table definition, mandatory reference laws, full signed telescope, finite-policy induction and an independent additive-potential tensor proof. No substantive repair of A012v9 is supplied. Direct traversal finds2121 ordinary potential rows and108 compulsory conversion entries, giving2229 augmented states; all729 raw restrictions are rebuilt. The initial reviewer's count assertion omitted entry states; that local checker error is documented and corrected without changing the mathematical domain. Duplicate rows/transactions and missing reachable states are rejected. All normalization, cover, ghost masses, constant terminals and beta>1 cases are checked. The additive tensor potential remains a super-solution under any adaptively selected block operation and pays all full terminal KL and fees from ONE original product owner.

First unsupported universal line: supply an ORIGINAL dimension-independent influence-priced complete source/current-reference eligibility theorem for arbitrary Boolean collision cores, or a noncircular required admission/contraction with all old bookings and actual query losses paid. No part of this finite-source review claims that line.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec FROZEN.json precedes execution. Command from A086: python -B -X utf8 runs/{R.name}/code/audit.py. Final output: PASS,{audit['assertions']} exact assertions,{audit['seconds']:.3f}s,729 raw restrictions,2229 augmented states,108 transactions,2642 physical query pairs. It exercises{audit['ghost_atom_occurrences']} ghost atom occurrences,{audit['constant_state_occurrences']} constant-target state occurrences and{audit['beta_above_one_states']} states with beta>1. These are occurrences across augmented states, not distinct functions. All unqueried-coordinate influences are checked separately in addition to total/shared ownership identities. Root-zero and deleted-state controls fail their corresponding exact acceptance predicates. Prescribed U uses sixteen full terminals and four weighted fees; U_POLICY.json reports PASS.

Integer direct-character Walsh sums and Fraction arithmetic reconstruct spectra/reference marginals;24-term atanh expansions with proved geometric tails and outward2^-64-nat rounding bound all logs. Strict margin comparison is rational; decimal margin about{audit['margin_bits_lower_decimal_evidence_only']:.8f} is diagnostic only. The certificate covers T6=482455353348902740055257 syntactic policies by induction, without enumerating them. Source helpers were not imported. Compiler admission returned exit1 (physical free5.0GB, commit3.6GB); KEY_STEP.lean records the two-child algebraic telescope but is UNCOMPILED. Attained rung: exact finite certificate plus analytic tensor proof, no Lean certification. No new search, dimension escalation, heavy job, GPU, remote compute or detached process.

## proof dependencies and changed downstream conclusions

A012 v9 statement/hash retained verbatim; its A013 original-owner correction and tensor-method attribution remain. The audit independently checks the owner identities and uses a different tensor argument, so it does not rely on accepting A013's earlier finite policy enumeration. A086 supplies a disinterested scoped review, not a repair/contributor acceptance. Local CLAIMS adds that review and leaves the universal source OPEN. A011v5 query-KL objection is already consumed by A011v6; no obsolete v5 transaction claim is restored. No shared index or another agent's output is changed.

## one next mathematical action and independent reviewer

{progress['next_action']} This is the universal supplier obstruction, rather than another history count for the paid seed.

## actual persistence receipts or precise save blocker

REPORT/CLAIMS/PROGRESS/PACKET_DELTA, proof, frozen spec, independent helper and exact outputs are saved under this A086 run. Final schema/hash/size checks and file hashes are in FINAL_VALIDATION.json and FILE_RECEIPTS.json. STATUS has exactly two lines; WORKLOG/LEARNED record this stage. Supervisor mirror and downstream adoption remain unverified. Required session wake/checklist administrative commands are distinguished from research writes; a current complete session-health receipt was not verified and no affected notes supplied a mathematical premise. The fresh memory refusal is recorded honestly. All research output remains in A086; no git, mail, brain writes, deletion, trading paths, other-agent mutations or process shedding.

Universal bridge: C024 receives an independent acceptance of the entire supplied-source ALL-physical-policy theorem, including mandatory current-profile conversions and arbitrary disjoint-tensor interleavings, with>19/1024 bit per original block and the stated>m/64 product reserve. C019's original stopping account is checked without renewing diminished capacity; C020's arbitrary-core initial source remains unpaid. NEXT asks for that necessary original supplier/admission from the SAME unused influence, so it addresses the all-dimensional FEI bottleneck rather than extending this closed six-bit example. Full FEI remains OPEN.
'''
put(R/'REPORT.md',report)
put(A/'STATUS.md','STATE: Stage22 COMPLETE_LOCAL: A012v9 ALL physical-policy theorem independently HOLDS;2229 states/108 conversions/729 restrictions;'+str(audit['assertions'])+' exact checks PASS;additive tensor proof;FEI OPEN.\nNEXT: A011/A012/A050 supply ORIGINAL arbitrary-core O(I) complete source or required paid admission, retaining old bills/query KL/BOTH terminals;A094 audit;no more histories of the closed six-bit seed.\n')
def append(p,text):
    with p.open('r',encoding='utf-8',newline='') as f:old=f.read()
    newline='\r\n' if '\r\n' in old else '\n'
    with p.open('a',encoding='utf-8',newline='') as f:f.write(text.replace('\n',newline))
append(A/'WORKLOG.md',f'\n{stamp}: Stage22 independently reconstructed A012v9 ALL-policy certificate: {audit["assertions"]} exact checks PASS,729 raw restrictions,2121 potential rows+108 mandatory entries=2229 states,2642 query pairs. Main margin>19/1024, U>3/5, additive tensor potential proves all interleavings. Initial checker count error repaired; no source theorem changed. Compiler held by memok exit1. Universal original supplier and FEI OPEN. Run {R.name}.\n')
append(A/'LEARNED.md','\nStage22 durable: A012v9 certificate has2121 ordinary potential rows plus108 mandatory conversion entries, totaling2229 augmented states. Count operation-entry states as well as stored potentials. Independent direct spectra/rational logs confirm margin>19/1024 from SAME original K=4+2/ln2, old5/(4ln2); prescribed U>3/5. Sum LOCAL Bellman entry potentials to prove arbitrary disjoint-tensor adaptive interleavings directly: one block changes, all other summands stay fixed. Keep actual beta>1 vacuum-ray laws nonnegative; do not call them convex mixtures. Cost convention signed entropy increments is essential; this is not A011v5 conversion-only ledger. Original arbitrary-core initial O(I) supplier remains unpaid.\n')
protocol=load(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
required=lambda xs:{s.split(' (')[0] for s in xs}
assert set(progress)==required(protocol['progress_fields'])
assert set(claim)==set(protocol['claim_fields'])
assert load(R/'PACKET_DELTA.json')==load(R/'PROGRESS.json')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(p.stat().st_size<20_000_000 for p in R.rglob('*') if p.is_file())
receipts=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in R.rglob('*') if p.is_file() and p.name not in ['FILE_RECEIPTS.json','FINAL_VALIDATION.json']]
js(R/'out/FILE_RECEIPTS.json',receipts)
js(R/'out/FINAL_VALIDATION.json',{'status':'PASS','at':stamp,'protocol_key_sets':'exact','statement_hash':'unchanged verified','matching_progress_delta':True,'all_files_under_20MB':True,'two_line_status':True,'audit_assertions':audit['assertions'],'scoped_verdict':'HOLDS','full_fei':'OPEN','mirror_verified':False,'checklist_task':'T-20261027-040'})
print(json.dumps({'status':'PASS','assertions':audit['assertions'],'states':audit['reachable_augmented_states'],'source_claim_version':claim['version'],'files':len(receipts),'report':str(R/'REPORT.md')}))
