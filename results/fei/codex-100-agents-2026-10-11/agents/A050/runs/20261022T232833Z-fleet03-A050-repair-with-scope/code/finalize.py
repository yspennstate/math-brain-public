from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parent
P=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,t):p.write_text(t,encoding='utf-8')
def js(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
check=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
pilot=json.loads((R/'out/PILOT.json').read_text(encoding='utf-8'))
mixed=json.loads((R/'out/MIXED_CHECK.json').read_text(encoding='utf-8'))
assert mixed['status']=='PASS' and mixed['histories']==16
lean=json.loads((R/'out/LEAN.json').read_text(encoding='utf-8'))
lean_status=lean.get('result',lean).get('status')
assert check['status']=='PASS' and check['physical_cases']==7 and check['symbolic_cases']==5
statement=('Let h be any uniform Boolean core, p its squared Fourier law and q a normalized dominating supplied core reference. '
 'Calibrate its empty mass once to p(empty), preserving its nonempty conditional law, to obtain q*. With B the binary KL of the old versus actual empty masses, CE(p,q*)=CE(p,q)-B. '
 'For F_h=(-1)^a on x0, h on x1b1,+1 otherwise, copy the actual six control/character sector masses and put q*(s)/16 on each of four control masks for every nonempty data frequency. '
 'This is a normalized dominating correlation-preserving complete reference Q with D(P_F||Q)=D(p||q*)/4 and CE(P_F,Q)<=3+CE(p,q*)/4. '
 'For C>=4 a supplied CE(p,q*)<=C I(h) gives root reference-inclusive margin>=C-3+C Pr(h=-1)/2. '
 'Query b then any finite adaptive fresh data-only tree in b1, retaining b0 and keeping x,a unqueried, with supplied actual H(g)<=C I(g) certificates at every core terminal. '
 'Transport the SAME Q by actual coherent kernels, fair fallback on source-zero rows, retaining all reference-only rows. '
 'For A=D(P_F||Q), e=Hroot-EHleaf-C(Iroot-EIleaf), S=E(CIleaf-Hleaf), the signed liability J=[A+e]+ leaves S-J>=C-3. '
 'At C=4 an eligible old conservative booking omega<=1/4 leaves at least3/4 from that same owner, with all source erasure/outcome and inherited terminal KL in A once. '
 'At rate4 one further x or a query on selected active data-frontier leaves, stopping at both new children and retaining b0, also leaves that margin: x child pairs have mean surplus>=2, a child pairs have mean surplus>=0, and the untouched b0 contributes1, so total S>=1. '
 'For any m>=1,r>=2 disjoint width-r point factors, choose q_r(empty)=p_r(empty), q_r(s)=(7/8)p_r(s)+(4*2^-r*(1-2^-r)/8)1_full(s) on nonempty s and q=product q_r. '
 'This is nonmatching and CE(h,q)<4I(h)-m*2^-r, so the theorem applies in every dimension including the existing canonical counterfamilies. '
 'At m512,r2, A>2 while complete-data final S=2; source-only conservative payment fails but the signed net is negative and paid. '
 'The construction compares initial references at the same reached Boolean root; it does not cancel a previously owed canonical source or pay a free descendant reset. '
 'Arbitrary-core supplied prices, mixed-query frontier eligibility and fresh inherited-reference conversion remain open; full FEI is not proved.')
claim={
 'claim_id':'A050-CORRELATION-PRESERVING-SIGNED-LIFT','version':1,'exact_statement':statement,
 'hypotheses':['Uniform finite Boolean core and independent physical x,a,b; bits throughout',
 'A normalized dominating supplied core reference with certified calibrated CE(p,q*)<=C I(h), C>=4; not asserted universally',
 'Initial calibration alone uses the binary KL refund once; no free conversion from a previously owed canonical source',
 'The exact six-sector/four-copy normalized lift in PROOF section1 defines the initial complete Q',
 'Same actual coherent channel and inherited normalized references throughout; fair source-zero fallback; all reference-only rows retained',
 'b first and fresh data-only continuation in b1; optionally at C4 query x or a once on selected active frontier leaves, stop both new children, retain b0 and all complements',
 'Actual terminal H(g)<=C I(g) certificates; signed earned query credit remains in the same account; old eligible conservative booking at rate4 is at most1/4',
 'Explicit nonmatching tensor supplier uses m>=1,r>=2; the source-only A+[e]+ assertion is excluded'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A050'],
 'proof_source':['PROOF.md','code/check.py','out/CHECK.json','code/mixed.py','out/MIXED_CHECK.json','out/SIGNED_NECESSITY.json','code/signed_payment.lean','out/LEAN.json'],
 'proof_dependencies':[],'review_records':[],
 'status':'SCOPED_ANALYTIC_PROOF_EXACT_CHECKS_REVIEW_PENDING_NOT_LEAN_CHECKED',
 'supersedes':[],'refutes':[],
 'first_unproved_line':'Supply a useful calibrated complete core reference price for an arbitrary Boolean core, and pay one prescribed conversion from an incoming different reference/mixed-query frontier after old bookings without a new bank.',
 'next_consumers':['A047','A049','A038','A039','A048','A083','A085','A092','A087','A096','A097','B10','B20']}
js(R/'CLAIMS.json',[claim])
next_action='A047/A049/A092 review correlated lift and mixed pair certificate; price ONE prescribed correlated reset AFTER the paid x/a exposure against SAME incoming Q, old quarter booking and actual remaining signed owner, retaining both full terminals.'
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B10','packet_id':'A050',
 'gap_id':'C024-SAME-REFERENCE-CERTIFIED-UNUSED-FRONTIER','attempt_id':'A050-stage7-correlated-signed-lift-v1',
 'method':'Change failed singleton reference to supplied correlated-core lift; one explicit initial calibration; analytic all-dimensional price and exact physical inherited-history checks',
 'mathematical_delta':'Normalized lift has CE_F<=3+CE_core_calibrated/4, source_KL=core_KL/4. ANY m>=1,r>=2 point-tensor supplier is nonmatching and completely priced at rate4; all data histories plus one selected x/a exposure retain>=1 signed margin, >=3/4 after old quarter. Signed necessity A>2,S=2 at m512,r2 certified. No universal FEI constant improves.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_CHECKS_INDEPENDENT_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':['A047-CANONICAL-FULL-SOURCE-PRICE-OBSTRUCTION@1','A049-MINIMAL-CANONICAL-FULL-SOURCE-COUNTERCIRCUIT@1','A048-EXACT-CANONICAL-TENSOR-SPARSE-PAYMENT@1','A050-NONPOINT-CANONICAL-GAP-REPAIR@1'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['PROOF.md','out/CHECK.json','out/MIXED_CHECK.json','out/SOURCE_RECEIPTS.json','out/LEAN.json','out/SIGNED_NECESSITY.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary-core supplier and incoming-reference conversion remain unpaid; mixed x/a histories need actual terminal eligibility',
 'Lean scalar RUNTIME_UNVERIFIED after timeout; no target/axiom verification',
 'Independent review, supervisor copying, mirror verification and downstream adoption pending'],
 'packet_ids':['A050']}
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A050/B10 stage7 repairs complete source payment after the canonical all-rate obstruction. Uniform finite Boolean signs, entropy/KL bits. The new hypothesis is a supplied complete correlated core-reference price, with one explicit initial empty-mass calibration and actual terminal certificates. The conclusion prices the complete SIGNED source/query transaction using one owner through b then arbitrary fresh data-only adaptive histories. It does not claim that source KL alone is paid, or that a previous canonical reference can be replaced for free. Current user endpoint2026-10-23T14:49Z overrides the older protocol date. Full FEI OPEN.

# sources actually read, revisions and theorem locators

Read current BOARD2026-10-22T23:29Z, unchanged B10 lead v2, own STATUS/previous stage6 proof/progress, and complete execution-v2 protocol. New primary read-only sources: A04720261021T221810 REPORT, PROOF and UNIVERSAL_REFERENCE_OBSTRUCTION; A04820261022T210915 full PROOF; A04920261022T223618 REPORT/circuit formulas and CLAIMS; A03820261022T210124 REPORT and A03920261022T222059 PROOF; A083/A092 current status. Prior campaign/manuscript reading remains previous-stage provenance, not a new full-paper audit. Read-only math recall gave contextual Booleanity/induction cautions, not a new theorem premise. SOURCE_RECEIPTS pins consulted files. The required wake reported owner-model/state-of-mind notes stale about86/71hours; the owner was told before relying on affected notes. Initial memory availability was low; all research computation stayed lightweight. No personal-context note is a mathematical dependency.

Dispatch consumes the new obstruction instead of repeating the old exact-canonical-gap NEXT: A047 proves no finite universal price for that complete singleton reference, and A048 already closes useful exact-G>2 admissions. Their independent acceptance of our stage6 repair is observed without changing its statement. No lead disagreement is needed; its original tax packet was already completed before this inherited source-payment work.

# complete derivation or exact first unsupported line

PROOF.md is self-contained. Initial calibration gives CE(p,q*)=CE(p,q)-binaryKL. A normalized Fourier-sector lift preserves the entire supplied joint core law, with KL_F=KL_core/4 and CE_F<=3+CE_core_calibrated/4. The three-bit overhead is paid by the actual base influence; at C>=4 the root inclusive margin is at least C-3+C Pr(h=-1)/2. The same-channel full KL chain includes every erasure/outcome and terminal bill once. Its exact signed identity gives S-[A+e]+ equal to the minimum of actual terminal surplus and root inclusive margin. Thus at rate4, actual certified terminal cores yield>=1 margin; an old eligible quarter booking leaves>=3/4.

For ANY m>=1,r>=2 point-defect tensor, the explicit nonmatching factor reference q_r=(7/8)p_r+(v_r/8)delta_full on the nonempty sector preserves empty mass and has CE_r<4I_r-2^-r. Tensor additivity supplies the core price and hereditary leaf certificates. This covers the exact existing canonical falsifiers, including the30-variable(9,3) circuit and A047's all-width family, without constructing huge tables. It changes Q, not the Boolean family or rate4. Earlier189/128 and67/128 bounds concern the OLD canonical small-gap sufficient test; the new>=1 signed margin uses a different initial reference and keeps earned negative edges.

The signed requirement is essential: m512,r2 has exact A=32log2(256/245)>2 with final S=2, so A alone and A+[e]+ fail. Its signed net is<-31 and positive liability is zero, paid from the same account. This is not a refund of a previous canonical debt. FIRST UNSUPPORTED UNIVERSAL LINE: supply a useful priced correlated core reference for arbitrary h and pay an actual prescribed incoming-reference conversion/mixed-query frontier after earlier bookings without renewing the source. No universal FEI constant improves.

PROOF section3 also closes ONE actual mixed controller exposure after any paid data-only prefix, at rate4. The x-pair has mean S>=2; the a-pair has mean S>=0 because its influence is1/2 and its entropy decrement is nonnegative. Retained b0 contributes1, so the complete frontier S>=1, enough for the same signed margin and old quarter. Individual a-child FEI is not assumed. Stop at both new children; fresh resets and later divergent histories are excluded.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec precedes execution; main amendments precede main execution and add symbolic witnesses only. Commands from A050: python -X utf8 -B runs/{R.name}/code/check.py --pilot, then without--pilot. Pilot PASS:{pilot['physical_cases']}physical case,{pilot['assertions']}+{pilot['primitive_assertions']}assertions,{pilot['runtime_seconds']:.3f}s. Main PASS:7physical fixtures+5symbolic cases,{check['assertions']}ledger+{check['primitive_assertions']}primitive={check['assertions']+check['primitive_assertions']}checks,{check['physical_nodes']}physical nodes,{check['retained_reference_only_rows']}reference-only erased rows retained,{check['runtime_seconds']:.3f}s. Physical tensors(1,2),(2,2),(2,3),(3,2), parity3/full uniform reference with nonzero calibration credit, constant+/-1 boundaries on a one-bit dummy cube. Maximum9physical variables. Symbolic tensor cases(9,3),(64,2),(64,3),(256,4),(512,2) use proved formulas only. No automatic dimension increase or truth-table census.

Integer Walsh spectra agree with direct pivotal edges. Fraction complete references, branch normalizers and exact atomwise likelihood products verify full source decomposition, influence telescoping and both first-data/full-data frontiers. Nonzero source KL and reference-only rows are explicitly tested. Every strict sign uses rational atanh logarithms with proved tails and outward dyadic endpoints; log-interval overlap is only a diagnostic, never the proof of a KL identity. The all-dimensional and all-history conclusions follow from PROOF, not finite extrapolation. Exact signs8^4<2*7^4 and256^16>2*245^16 certify the reference price and signed-necessity boundary. No failed mathematical main or pilot checker is counted.

Research jobs estimate100MB, frozen55s cap. Fresh memok passed before the scalar Lean check; helper target signed_payment was submitted with source hash and narrow imports. Receipt status {lean_status}; nominal45s timeout returned after about49.1s on the slow machine. No target kind, transitive axioms or dependency bytes were verified, so this stage is ANALYTIC PROOF WITH EXACT CHECKS, NOT Lean-checked. No retry is pending. Exact constants/parity boundaries also verify zero variance, zero empty mass and the calibration denominators where used.

Separately frozen MIXED_SPEC precedes the mixed pilot/main. Command python -X utf8 -B runs/{R.name}/code/mixed.py --pilot, then without--pilot. Main PASS:{mixed['histories']}actual histories,{mixed['assertions']}ledger+{mixed['primitive_assertions']}primitive checks,{mixed['physical_nodes']}physical nodes,{mixed['retained_reference_only_rows']}reference-only rows,{mixed['runtime_seconds']:.3f}s. Fixtures(1,2),(2,2),(2,3),parity3; controllers x/a on all active data leaves or only data0. The original Q, old quarter, full source releases, all inherited terminal KL and complementary branches remain. These finite checks verify the exact certificate; all-prefix eligibility is the analytic pair argument.

# proof dependencies and changed downstream conclusions

The new proof reconstructs its formulas and has no unproved FEI premise. A047's full-reference obstruction and A049's compact witness motivate the changed mechanism; no failed canonical claim is relabelled valid. A048's newer canonical admission is not duplicated. The previous A050 scoped theorem remains valid and is observed accepted by A047/A048. New theorem review is pending. Consumers may compare a completely specified correlation-preserving initial reference on the SAME Boolean falsifiers and carry it unchanged through physical data histories. They may not silently retire an already booked old-reference source, query x/a while assuming S>=2, or reset inherited references without paying conversion. A supplied arbitrary core price contains the missing universal FEI content and is not asserted.

# one next mathematical action and independent reviewer

NEXT: price ONE prescribed correlated reset AFTER the now-paid x/a exposure using the SAME incoming lifted reference, old quarter booking and actual remaining signed surplus, retaining both complete terminals. A047/A049 reconstruct the source and witness comparison; A092/A087 check ghost support and once-only ownership; A038/A039 supply further mixed-history eligibility. This is the selected unpaid inherited-reference step, not another exact canonical census.

# actual persistence receipts or precise save blocker

Saved all four exact-schema protocol files, complete PROOF/current derivation, pre-search specs, self-contained code, per-fixture and symbolic receipts, signed-necessity certificate, source hashes and Lean/admission receipt. STATUS has two lines; WORKLOG/LEARNED append. out/PERSISTENCE.json checks schema fields, statement hash, progress/delta equality and file sizes<20MB, with local readback hashes. No local blocker. Required wake/checklist infrastructure is separate from research output ownership. No git, mail/messages, protected-tree research write, other-agent write, trading-path access, deletion, detached job or remote publication. Supervisor copying, independent review, mirrors and downstream use are unverified.

Universal bridge: This stage moves C024 history transfer and C019 stopping-tree payment by replacing the universally unaffordable full singleton reference with one normalized supplied-core correlated lift, proving exact source scaling and a dimension-independent three-bit control price, and paying the complete signed transaction at SAME rate4 for every m>=1,r>=2 point-tensor core through arbitrary stated data histories AND one selected x/a exposure, leaving>=3/4 after an old quarter booking. The universal FEI constant improves by zero. Arbitrary-core supplier certificates, prescribed incoming-reference conversion and further mixed-query frontier eligibility remain unpaid. NEXT addresses that actual conversion after a paid mixed exposure, the shortest identified route because making the old canonical price more exact is proved incapable of being universal.
'''
write(R/'REPORT.md',report)
total_checks=check['assertions']+check['primitive_assertions']+mixed['assertions']+mixed['primitive_assertions']
write(A/'STATUS.md',f'STATE: A050 stage7 complete locally: correlated lift pays all point tensors and one x/a query at SAME4, >=3/4 after old quarter;12 root cases+16 mixed histories/{total_checks} checks PASS; review pending; FEI OPEN.\nNEXT: '+next_action+'\n')
for name,text in [('WORKLOG.md','2026-10-23 stage7: consumed A047 all-rate canonical obstruction, A048 exact admission and A04930-variable witness. Changed initial reference to a normalized correlated core lift with one binary-KL calibration. Exact7physical+5symbolic cases PASS17072checks in12.786s,167nodes,28ghost rows. Every m>=1,r>=2 point-tensor supplied price proved; signed necessity m512r2 A>2 but S2 and net<-31. Scalar Lean timed out, no formal status. New theorem review pending; no universal FEI constant improvement.'),('LEARNED.md','Stage7 durable: Any supplied core reference can be calibrated once at empty mass, lowering CE by exactly binaryKL. For F_h char/constant/h selector, a normalized four-copy correlated lift gives A_F=A_core_cal/4 and CE_F<=3+CE_core_cal/4. At C>=4 supplied core CE<=CI plus actual terminal certificates yield S-[A+e]+>=C-3 through b/data-only histories; old quarter leaves>=3/4 at4. This is SIGNED payment; A+[e]+ can fail. Explicit nonmatching q_point uses7/8 source plus1/8 nonempty full-mask atom, preserves empty mass and has CE_point<4I_point-delta for allr>=2; products admit ANYm. At m512r2 A=32log2(256/245)>2 but complete-data S2, signednet<-31. Never treat a new initial Q as free conversion from an owed canonical source. Arbitrary core supplier and mixed/reset eligibility remain open. Previous189/128 bound was old canonical small-gap repair, not this signed correlated lift. Main7physical+5symbolic/17072checks/28ghost rows PASS. Lean timed out; proof is analytic/exact, not formal.')]:
 with (A/name).open('a',encoding='utf-8') as f:f.write('\n'+text+'\n')
sources=[P,TEAM.parent/'BOARD.md',TEAM.parent/'claude/B10/STREAM_NOTES.md',A/'runs/20261021T171109Z-fleet03-A050-repair-with-scope/PROOF.md']
for agent,run,names in [
 ('A047','20261021T221810Z-fleet03-A047-boundary-search',['REPORT.md','PROOF.md','UNIVERSAL_REFERENCE_OBSTRUCTION.md','CLAIMS.json']),
 ('A048','20261022T210915Z-fleet03-A048-tensor-stress',['PROOF.md','CLAIMS.json']),
 ('A049','20261022T223618Z-fleet03-A049-minimal-falsifier-extraction',['REPORT.md','CLAIMS.json']),
 ('A038','20261022T210124Z-fleet03-A038-occupancy-term-audit',['REPORT.md']),
 ('A039','20261022T222059Z-fleet03-A039-projection-under-restrictions',['PROOF.md'])]:
 for n in names:sources.append(TEAM/agent/'runs'/run/n)
js(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources if p.exists()])
fields=protocol['required_per_run'];assert set(claim)==set(fields['claim_fields'])
assert set(progress)=={k.split(' (')[0] for k in fields['progress_fields']}
assert all('# '+h in report for h in fields['report_fields'])
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert check['assertions']+check['primitive_assertions']==17072
manifest=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  manifest.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
js(R/'out/PERSISTENCE.json',{'status':'PASS','local_only':True,'schema_checked':True,'full_fei':'OPEN','independent_review':'PENDING','mirror_verification':'NOT_PERFORMED','files':manifest})
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'Further stage7 mixed extension:16 histories PASS,{mixed["assertions"]+mixed["primitive_assertions"]} exact checks,{mixed["retained_reference_only_rows"]}ghost rows. Analytic paired x/a frontier certificate closes one mixed exposure after any paid data prefix; no individual a-child FEI asserted. Total stage exact checks{total_checks}. NEXT is prescribed reset after that exposure.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage7 paired mixed extension at C4: after b/data-only prefix, query x or a once at selected active leaves and stop both children. x pair meanS>=2. a pair meanS>=0 because Inf_a=1/2 and entropy decrement>=0. Retained b0 supplies1, so totalS>=1 and SAME lifted signed account retains>=1, old quarter leaves>=3/4. No individual activation-child FEI or free reset is assumed.\n')
print(json.dumps({'status':'PASS','physical_cases':7,'symbolic_cases':5,'mixed_histories':16,'exact_checks':total_checks,'ghost_rows':28+mixed['retained_reference_only_rows'],'files':len(manifest),'Lean':lean_status,'run':str(R)}))
