from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
main=read(R/'out/full.json');alt=read(R/'out/independent.json');red=read(R/'out/reduction.json');pilot=read(R/'out/pilot.json')
assert all(o['status']=='PASS' for o in [main,alt,red,pilot])
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
source28=read(A.parent/'A028/runs/20261023T144415Z-fleet03-A028-stopping-tree-payment/CLAIMS.json')
v28=[{'claim_id':c['claim_id'],'version':c['version']} for c in source28]
statement=('For every finite uniform Boolean binary mux on independent controller/DATA cubes, arbitrary shared Boolean sources, and ONCE-supplied support-positive canonical source/controller references with their own physical inheritance, let eta=Var(a)Pr(G!=H)=sum q_t k_t. At every reached node choose one real epsilon in [0,1/16] and replace each occupied DATA-row sector odds by ell_t=(1-epsilon)k_t+epsilon eta, keeping its reference row marginal and inherited nonempty shape, all zero-true reference mass and actual physical normalizers. Then sum q ell=eta, epsilon eta<=ell<=1-epsilon(1-eta), and the exact extra full-law KL C=sum q D_Ber(k||ell)<=31eta/160<=eta/2. Thus every finite adaptive mixed history alternating these targets with A029@4 relative-odds targets is paid from the SAME original T+eta/2 supermartingale, retaining all signed releases, old debits, both full terminal laws and actual child deficits; no new allowance is granted. Prior same4I/old1/8 prefix corollary and >121/128 reserve retain their original scope. There are actual rare point-defect targets with unbounded relative odds on the vacuum that satisfy this bound. Nevertheless this calibrated terminal class at fixed nondegenerate eta=1/2 contains AND2 times arbitrary Boolean tensor cores, with H=mH(h)+2 and I=mI(h)+1; a uniform FEI constant on the class implies full FEI with the same constant. No initial influence-priced source or terminal sufficiency is supplied.')
claim={
 'claim_id':'A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT','version':5,'exact_statement':statement,
 'hypotheses':['Finite uniform physical cubes with disjoint controller and DATA blocks; DATA sources may share every DATA variable.','Original canonical source/controller references supplied once and inherited through their own channels; finite true KL and all reference-only mass retained.','One shared epsilon per node in [0,1/16]; exact true-weighted calibration is asserted, not reference-weighted calibration.','At eta=0 or1 occupied rows remain at their true endpoint; undefined nonempty shape is never used to create mass.','Existing original eta/2 allocation actually admitted in the original quota; all prior debits and both complete physical children and terminal CE bills remain.','Membership necessity is only for the declared floor class; no universal necessity for FEI is asserted.'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A029/fleet04'],
 'proof_source':['DERIVATION.md sections1-6','REVIEW.md','out/full.json','out/independent.json','out/reduction.json'],
 'proof_dependencies':[{'claim':'A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@4','scope':'Original supplied T/S, eta supermartingale and prior literal prefix; new floor bound is proved here.'},{'source':'A028 latest exact admission','scope':'Scoped independent reconstruction in REVIEW.md; not used as an initial source supplier.'}],
 'review_records':[{'reviewer':'A029 alternate implementations','verdict':'EXACT_FINITE_REPRODUCTION_NOT_INDEPENDENT_PEER_ACCEPTANCE','source':'code/independent.py and code/reduction.py'}],
 'status':'ANALYTIC_AUTHOR_PROOF_EXACT_CHECKED_EXTERNAL_REVIEW_PENDING','supersedes':'A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@4 (retains its scoped conclusions)','refutes':[],
 'first_unproved_line':'Universal original O(I) complete source/controller allowance and a useful stopping certificate using DATA-spectrum information beyond calibrated row odds. No proof gap is asserted for the displayed scoped theorem.','next_consumers':['A028','A026','A030','A094','A096','A097']}
assert set(claim)==set(protocol['required_per_run']['claim_fields']);write(R/'CLAIMS.json',[claim])
total=main['exact_assertions']+alt['exact_assertions']+red['exact_assertions']
delta=f"Pooled odds ell=(1-eps)k+eps*eta give true-mass-preserving vacuum floors and C<=31eta/160, including unbounded relative odds, from SAME old eta/2. Nondegenerate calibrated terminal class contains AND2 times arbitrary tensor cores and is full-FEI-hard. {total} exact checks PASS; FEI OPEN."
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B06','packet_id':'A029','gap_id':'G-R-MISMATCH',
 'attempt_id':'A029-stage21-occupancy-calibrated-vacuum-transport','method':'Consume latest A028 exact-affordability/A026 nonempty-floor source; KL chord and eta envelope; direct-character alternate validation; arbitrary-core calibrated-carrier reduction',
 'mathematical_delta':delta,'deliverable_status':'COMPLETE_LOCAL_REVIEW_HANDOFF','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_CHECKS; EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN; LEAN_SETUP_UNVERIFIED',
 'claim_versions_used':['A029@4 supplied canonical interface and existing eta/2 allowance',{'A028_reviewed_source_records':v28},'A026@6 DERIVATION sections1-3 scoped review'],
 'claims_created_or_changed':['A029-FINITE-LABEL-SIGNED-CHILD-ACCOUNT@5','A028 latest exact-admission scoped review','A026@6 scoped envelope review'],
 'source_artifacts':['DERIVATION.md','REVIEW.md','out/SOURCE_RECEIPTS.json','out/full.json','out/independent.json','out/reduction.json','out/FROZEN_SPEC.json','out/INDEPENDENT_SPEC.json','out/REDUCTION_SPEC.json','out/PERSISTENCE.json'],
 'next_consumers':['A028','A026','A030','A094','A096','A097'],
 'next_action':'Consume one concrete ORIGINAL supplier/stopping certificate using DATA-spectrum structure beyond row calibration; challenge it on AND2 times arbitrary tensor cores, keep actual mH(h) terminal debt and identify first unpaid original-core line. Do not repeat floor-only reset checks.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal initial source and sufficient stopping certificate remain unpaid; calibrated floors alone retain full FEI.','Independent peer acceptance of cumulative A029 candidate pending; no mirror/adoption receipt.','Lean core check returned SETUP_UNVERIFIED: Compute status is distressed or unknown; memok returned WAIT physical free2.4GB/commit free2.9GB. No Lean certificate.','Wake owner alert: stale owner-model/state/dream notes; not used as mathematical evidence.'],
 'packet_ids':['A029']}
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
report=f'''# A029 stage21: calibrated vacuum floors, same original child allowance

## exact target, quantifiers, hypotheses and units

For every finite uniform Boolean binary mux with independent controller/DATA blocks and arbitrary shared DATA sources, price the adaptive real targets ell=(1-epsilon)k+epsilon eta, epsilon in[0,1/16], eta=Var(a)Pr(G!=H), from the already admitted original eta/2. Original support-positive source/controller references and their OWN physical inheritance are hypotheses. Every row marginal, nonempty shape, ghost mass, old debit, actual physical refund and BOTH full children/terminal bills is retained. Units bits; full FEI OPEN. Exact claim/hypotheses: CLAIMS.json.

## sources actually read, revisions and theorem locators

Fresh BOARD, B06 STREAM_NOTES v2, own STATUS/LEARNED and prior runs read. Protocol2026-10-11-execution-v2 read in full; campaign README/status/registries/packet/action/plan, supplement five documents and sources read as baseline refresh. Four supplied paper texts decoded explicitly as cp1252 (UTF-8 decoding failed); relevant composition/restriction extracts are saved, with no new paper audit or priority claim. out/SOURCE_RECEIPTS.json pins35 source files; out/SOURCE_EXCERPTS.json supplies locators. Latest A028 DERIVATION exact admission and A026@6 DERIVATION1-3 independently reconstructed in REVIEW.md. Prior A029@4 DERIVATION is the exact supplied-interface dependency. Current source/math files outrank stale wake personalization notes, which were not mathematical premises. No internet claims or new literature attributions are made.

## complete derivation or exact first unsupported line

DERIVATION1-3: joint convexity gives an endpoint chord for Bernoulli KL; averaging and -ln(1-x)<=x/(1-x) prove C<=(epsilon-ln(1-epsilon))*eta/ln2<=31eta/160<=eta/2. Shared epsilon preserves sum q ell=eta; preservation of sum r ell is neither needed nor claimed. The existing eta supermartingale therefore pays every adaptive sequence alternating pooled and old relative targets, with no increase in original allowance. Both deficits and signed refunds telescope once; parent leaf bills are replaced, never added again. Existing same4I/old1/8 literal-prefix reserve>121/128 remains inherited at its old scope, not newly numerically reproduced here.

Section4 gives actual point-defect targets with unbounded relative odds at the vacuum and vanishing influence-priced cost. Section6 shows a sharp limitation of this new class: AND2 times m disjoint copies of ANY Boolean h has all occupied k=eta=1/2, zero conversion cost, H=mH(h)+2 and I=mI(h)+1. A uniform FEI theorem for these nondegenerate calibrated terminals already implies full FEI. This is a universal reduction, not a counterexample to FEI or to paid transport. First unpaid line: an ORIGINAL influence-priced full source and a sufficient stopping rule using DATA-spectrum structure beyond these row odds. No universal constant improvement is asserted.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede their jobs: FROZEN_SPEC, INDEPENDENT_SPEC and REDUCTION_SPEC in out/. Commands: python -X utf8 code/check.py pilot; python -X utf8 code/check.py full; python -X utf8 code/independent.py; python -X utf8 code/reduction.py; python -X utf8 code/intake.py; python -X utf8 code/finalize.py (paths relative to this run). Pilot64 labelled mux representations/{pilot['exact_assertions']} assertions PASS in{pilot['seconds']:.3f}s. Main1344 labelled representations,3968 physical splits,{main['exact_assertions']} exact assertions PASS in{main['seconds']:.3f}s. No symmetry reduction. Both zero and nonzero occupancy endpoints and both query blocks are included. Main reconstructs actual Walsh probabilities, whole references, both inherited children, actual outcome/erasure refunds and exact signed conservation. Fraction arithmetic and prime-log identities; sign bounds use outward rational atanh enclosures.

Alternate checker imports no main helper:729 rational two-row laws plus6 actual n1..6 point-defect truth tables rebuilt by direct characters/physical edge counts, {alt['exact_assertions']} exact assertions PASS in{alt['seconds']:.3f}s. Separate carrier checker:66 actual Boolean carriers, every h on0..2 bits and m1..3, {red['exact_assertions']} exact assertions PASS in{red['seconds']:.3f}s. Total main+alternate+carrier={total}; pilot separate, no earlier-stage checks included. All-dimensional/real-parameter claims use analytic proofs, not extrapolation from finite checks. These are different same-author implementations, not peer acceptance.

Estimated memory160MB main/70MB alternate/40MB carrier; observed peaks unmeasured; no job above300MB launched. Fresh memok rejected large compute (physical free2.4GB; commit free2.9GB), and Lean's own core admission returned SETUP_UNVERIFIED: distressed or unknown compute. code/Accounting.lean states only the integer child-affordability algebra; it is UNCHECKED here. No Lean certification, GPU, detached research, remote compute or workload stop. A failed cmd.exe inline quoting attempt launched no mathematical search; using script paths corrected it. Small reads briefly stalled in the local tool chain and were resumed, not duplicated.

## proof dependencies and changed downstream conclusions

New bound and calibrated-carrier reduction are elementary; the physical supplied T/S interface, eta telescope and old literal prefix retain A029@4's hypotheses. A028 latest exact-affordability equivalence receives scoped HOLDS; A026@6 sections1-3 receive scoped HOLDS, excluding independent recertification of its separate prefix/necessity clauses. The same candidate advances to@5; peer review remains pending. A028/A096/A097 can now use a vacuum-regularizing target outside bounded relative odds without extra original allowance. They cannot treat calibrated terminals as FEI-certified: section6 explicitly retains arbitrary-core entropy. No canonical shared registry is edited.

## one next mathematical action and independent reviewer

A028/A026/A094 reconstruct the KL chord, true-versus-reference calibration distinction, old allowance identity and actual rare witness. A096/A097 consume the arbitrary-core carrier reduction: audit ONE proposed original supplier or stronger stopping certificate on these carriers, preserving mH(h), all old debits and both full terminal bills. This goes directly to initial core payment; more floor-only transactions are already paid and the floor-only terminal class is full-FEI-hard.

## actual persistence receipts or precise save blocker

All four protocol files, full proof/reviews, three frozen specs, scripts, exact outputs and source receipts are saved only in A029's run. Rolling STATUS is two lines; WORKLOG/LEARNED append dated findings. This finalizer checks exact protocol fields, statement hash, PASS results, compatibility-copy equality and all file sizes<20MB, then saves out/PERSISTENCE.json with local hashes. Supervisor copying, remote mirroring, canonical adoption and independent review remain unverified. Brain wake was degraded and explicitly reported. No git, mail, brain research writes, other-agent changes, deletion or trading-path action occurred. Lifecycle tooling is administrative only; no shared lock was altered.

## Universal bridge

C019 stopping-tree payment and C024 history transfer gain an occupancy-calibrated vacuum floor with unbounded relative odds, at C<=31eta/160 and ZERO extra allowance beyond the existing original eta/2<=I_controls/2. Both child deficits remain signed and counted once. The nondegenerate calibrated-terminal reduction simultaneously shows why this cannot finish FEI: its class contains arbitrary tensor cores with their complete terminal entropy. Universal constant gain is zero; full FEI remains OPEN. The shortest next route is an original-core supplier or stronger DATA-spectrum stopping certificate tested against these carriers, rather than another isolated floor or reset example.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: Stage21 saved: calibrated vacuum floors C<=31eta/160 use SAME eta/2; unbounded relative odds paid; calibrated terminals full-FEI-hard; '+str(total)+' exact checks PASS; peer review pending, FEI OPEN.\nNEXT: A028/A026/A094 review; A096/A097 audit ONE original supplier/stronger DATA-spectrum stopping certificate on AND2 tensor carriers, retaining mH(h), old debits and BOTH full terminals; no more floor-only resets.\n',encoding='utf-8')
for name,text in [('WORKLOG.md',f'\n{now} Stage21: occupancy-calibrated pooled odds paid from existing eta/2, no new budget. Main1344 representations/3968 splits plus alternate and carrier checks: {total} exact assertions PASS (pilot separate). Fixed eta1/2 calibrated carriers retain arbitrary core entropy, so floor-only terminal certificate is full-FEI-hard. Scoped A028/A026 reviews saved. Lean admission refused under compute distress, no formal certificate; full FEI OPEN.\n'),('LEARNED.md',f'\nStage21 ({now}): For true row weights q, k with mean eta, pooled ell=(1-eps)k+eps*eta preserves TRUE mean (not reference-weighted mass), lies in[eps*eta,1-eps*(1-eta)] and costs C<=[eps-ln(1-eps)]eta/ln2<=31eta/160 for eps<=1/16. Thus old eta/2 envelope pays this class plus alternating old relative-odds histories with no new grant. Rare point-defect vacuum relative factors diverge but price vanishes with eta. Strong obstruction: AND2 times m disjoint arbitrary h has ALL occupied k=eta=1/2, pooled conversion0, H=mH(h)+2,I=mI(h)+1; any FEI bound just for these calibrated terminals implies full FEI. Original supplier and sufficient DATA-spectrum stopping condition remain unpaid. {total} current exact checks PASS; no peer/Lean acceptance.\n')]:
 with (A/name).open('a',encoding='utf-8',newline='') as f:f.write(text)
write(R/'out/COMPUTE_RECEIPT.json',{'memok_exit_code':1,'memok_output':'WAIT: physical free 2.4 GB (need 4.0), commit free 2.9 GB (need 8.0)','lean_exit_code':2,'lean_output':'SETUP_UNVERIFIED: Compute status is distressed or unknown','formal_status':'NOT_CHECKED','no_work_stopped':True})
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  b=p.read_bytes();assert len(b)<20*1024*1024;files.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
assert hashlib.sha256(read(R/'CLAIMS.json')[0]['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
write(R/'out/PERSISTENCE.json',{'status':'LOCAL_FILES_READ_BACK_PASS','utc':now,'protocol_fields':'PASS','claim_fields':'PASS','statement_hash':'PASS','compatibility_bytes':'IDENTICAL','files':files,'remote_mirror':'UNVERIFIED','peer_review':'PENDING'})
print(json.dumps({'status':'LOCAL_HANDOFF_COMPLETE','total_exact_assertions':total,'file_count':len(files),'full_fei':'OPEN'}))
