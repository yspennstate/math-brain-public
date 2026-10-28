from pathlib import Path
import json,hashlib,datetime,copy

root=Path(r'~\brain_workers\FEI100_20261011')
agent=root/'agents/A045';run=Path(__file__).resolve().parents[1]
source=root/'agents/A042/runs/20261023T055815Z-account03-A042-bias-endpoint-certificates'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):p.write_text(s,encoding='utf-8',newline='')
def dump(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
proto=load(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
checks=load(run/'out/CHECKS.json');pilot=load(run/'out/PILOT.json')
assert checks['status']==pilot['status']=='PASS' and checks['cases']==512
assert checks['runtime_seconds']<55 and pilot['runtime_seconds']<55
claim=load(source/'CLAIMS.json')[0]
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']=='98e11ccae0ed368bb734645e1f9f9dd583bfef482baebad65715d6c8da745590'
assert sha(source/'PROOF.md')==claim['proof_source']['sha256']=='bc9adf9f87e3f9f11e4e9ece021a060e22ad5129cf833238feca4c1554b8967e'
review={'claim_id':claim['claim_id'],'version':1,'statement_sha256':claim['statement_sha256'],'proof_sha256':sha(source/'PROOF.md'),'reviewer':'A045/account03','verdict':'HOLDS_AT_STATED_SCOPE','scope':'Full exact one-selector endpoint theorem, including sharp outer J bound, actual physical spectrum, full ordinary KL and signed reference transfer, constants/contractions, and explicitly OPEN arbitrary-seed supplier. Optional A044 normalizer bound uses prior-stage independent review.','independence':'Fresh analytic reconstruction, multilinear Mobius transform checked against centered physical moments, complete per-label likelihood reconstruction, canonical prime-log identities; source code not executed or copied.','repair_supplied':False,'contributor_conflict':False,'proof':'PROOF.md Sections1-2','checks':'out/CHECKS.json','at':stamp}
dump(run/'out/A042_REVIEW.json',review)
claim=copy.deepcopy(claim);claim['review_records'].append(review);claim['status']='INDEPENDENT_RECONSTRUCTION_HOLDS_AT_STATED_SCOPE_FULL_FEI_OPEN'
statement=('For every finite Boolean seed g at any independent product law after deterministic contraction, and every finite set of physically disjoint independent selector wires X_j with probabilities epsilon_j=2^-k_j, k_j>=1, put epsilon=product epsilon_j, a=(1-Eg)/2, V=4a(1-a), L_sel=sum(1-epsilon_j), D_sel=sum[(1-epsilon_j)+epsilon_j*k_j], K_sel=sum k_j. For 0<a<1 let j_a satisfy1/2<2^j_a*a<=1 and b=4^-j_a. For F=1-product X_j+(product X_j)g the actual complete spectrum in PROOF.md Section3 gives Delta_F=epsilon Delta_g+epsilon[4a L_sel-4a^2(1-epsilon)] and J_F=epsilon J_g+ln4*epsilon[4a D_sel+4a^2(j_a-1)(1-epsilon)-4a^2 epsilon K_sel]. All coefficient shifts are exact integers with zero carry. The actual outer gate satisfies sharp J_outer<=3ln4 Delta_outer; consequently a seed J<=KDelta premise is preserved with max(K,3ln4). The complete flat normalizer and full ordinary KL satisfy Z_F=epsilon Z_g+4b epsilon(1-epsilon), K_F=epsilon K_g+w*d_Bern(s||t), w=4a epsilon(1-a epsilon), s=4a^2 epsilon(1-epsilon)/w,t=4b epsilon(1-epsilon)/Z_F. Thus at fixed seed and selector product, Z_F and K_F are independent of selector shape, whereas J_F and I_F generally are not. The full outer-gate/seed reference retains epsilon K_g and signed conversion w ln(Z_F/Z_outer)-epsilon V ln(Z_g/V), whose positive first term is at most epsilon(Z_g-V). Constants and deterministic selectors contract physically; a negative constant seed with several selectors is not generally a signed literal. Reused wires and spectral-conditioning substitutes are excluded. These are exact conditional transfer identities, not a universal seed J payment or a proof of full FEI.')
new={'claim_id':'A045-MULTISELECTOR-COMPLETE-SEED-TRANSFER','version':1,'exact_statement':statement,'hypotheses':['Actual Boolean seed and independent product physical law, with deterministic coordinates contracted','Finite independent dyadic selectors on physically disjoint wires and blocks','Full complete flat or actual outer-gate/seed reference; ordinary KL with actual empty mass','No equality with every sequential binary reference asserted; reference conversion replaces its KL','Original allocation charged once; universal inherited seed supplier remains open'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A045/account03'],'proof_source':{'path':'PROOF.md','sha256':sha(run/'PROOF.md'),'checks':'out/CHECKS.json'},'proof_dependencies':[{'claim_id':claim['claim_id'],'version':1,'statement_sha256':claim['statement_sha256'],'acceptance':'Full independent reconstruction in PROOF.md Sections1-2 and out/A042_REVIEW.json; only one-selector induction premise used.'}],'review_records':[],'status':'ANALYTIC_FINITE_DEPTH_COROLLARY_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A042','A044','A041','A043','A091']}
dump(run/'CLAIMS.json',[claim,new])
progress={'protocol_revision':proto['revision'],'run_id':run.name,'stream':'B09','packet_id':'A045','gap_id':'G-BIASED-PROFILE-OWNERSHIP','attempt_id':'A045-stage9-independent-activation-seed-transfer','method':'Full independent source review and exact multiselector physical-spectrum/complete-reference reconstruction','mathematical_delta':'A042 actual dyadic activation endpoint independently HOLDS. Finite-depth multiselector transfer explicitly retains epsilon J_seed and epsilon ordinary KL_seed; normalizer and full KL depend only on selector product while J/I retain selector shape. No renewed original seed account.','deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SOURCE_REVIEW_HOLDS_SCOPED_COROLLARY_PENDING_REVIEW_FULL_FEI_OPEN','claim_versions_used':[claim['claim_id']+'@1; '+claim['statement_sha256']],'claims_created_or_changed':[new['claim_id']+'@1','independent review of '+claim['claim_id']+'@1'],'source_artifacts':['PROOF.md','out/A042_REVIEW.json','out/FROZEN_SPEC.json','code/check.py','out/PILOT.json','out/CHECKS.json','out/SOURCE_RECEIPTS.json'],'next_consumers':new['next_consumers'],'next_action':'A042/A044 independently review multiselector exact KL and zero-carry transfer; pay arbitrary inherited seed J from SAME unused original deficit with old debits, complete reference, signed conversion and both full terminals retained.','stagnant_substantive_attempts':0,'blockers':['Universal arbitrary-seed J/Delta supplier is OPEN; activation does not pay it.','New corollary independent review and supervisor copy/mirror ingestion unverified.','Checklist working and done calls failed: shared checklist lock held too long; no lock changed.','Brain self-care degraded/unverified: personal-model/state-of-mind/latest-dream freshness; excluded as mathematical premises.'],'packet_ids':['A045']}
dump(run/'PROGRESS.json',progress);dump(run/'PACKET_DELTA.json',progress)
paths=[root/'BOARD.md',root/'claude/B09/STREAM_NOTES.md',source/'STATUS.md',source/'CLAIMS.json',source/'REPORT.md',source/'PROOF.md',agent/'runs/20261023T041958Z-account03-A045-biased-realizability-referee/PROOF.md']
receipts=[]
for p in paths:
 if p.exists():receipts.append({'path':str(p),'sha256':sha(p),'read_scope':'current source mathematical text; previous-stage proof retained as baseline' if p.name=='PROOF.md' else 'current stage intake'})
dump(run/'out/SOURCE_RECEIPTS.json',receipts)
dump(run/'out/FORMAL_STATUS.json',{'status':'NOT_ATTEMPTED','reason':'Exact rational certificates and analytic proof suffice for this scoped review; no compiler, heavy job, GPU or background job launched.','memory_estimate_MB':90,'observed_peak_MB':None})
report=f'''# A045 stage9: independent activation realizability review

## exact target, quantifiers, hypotheses and units

Independently review A042-DYADIC-ACTIVATION-ENDPOINT-CERTIFICATE@1 in full, then reconstruct the exact complete physical spectrum and inherited seed bill after ANY FINITE number of independent dyadic selector activations of ANY finite Boolean seed under an independent product law. Contract deterministic inputs first. Natural-log corrected entropy and ordinary KL; J includes ln4 and Delta=I-Var. Shared wires and spectral-conditioning substitutes are excluded. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

BOARD written23Oct11:14UTC, B09 lead STREAM_NOTES v2 (older11Oct guidance), own rolling STATUS/LEARNED and prior stage8 PROGRESS/CLAIMS/proof baseline; current A042/A044/A090/A091 STATUS; A042 stage9 REPORT, CLAIMS and full PROOF Sections1-5 at {source}; full execution protocol revision{proto['revision']} and machine-wide AGENTS.md. A042 exact statement hash {claim['statement_sha256']} and proof hash {review['proof_sha256']} reproduced. Source code was not executed or copied. Current board supersedes the lead's already-refuted scalar-tax target; prior LEARNED records that obstruction. Older campaign/paper intake remains prior-stage context, not a new literature review. Current owner deadline23Oct14:49UTC supersedes old protocol dates. The stale personal-context brain wake is excluded from mathematical premises. One read-only math-brain query returned weak-match conditioning/Booleanity cards; these were contextual controls only, not proof dependencies (out/MATH_RECALL.json).

## complete derivation or exact first unsupported line

PROOF.md independently reconstructs every mathematical interface of A042@1, including sharp outer J<=3ln4 Delta, constants/unit atoms, exact endpoint error, full ordinary-KL chain and signed normalizer conversion. Verdict HOLDS at stated conditional scope; no source repair or contributor conflict. The optional A044 normalizer inequality relies on our already-complete prior review, not another claimed independent reconstruction.

The finite-depth corollary gives each actual selector/seed Fourier label and exact integer cell shift. It shows J_F=epsilon J_seed+J_outer, Delta_F=epsilon Delta_seed+Delta_outer and pays J_outer at the same sharp constant by induction. The full seed ordinary KL persists as epsilon KL_seed. At fixed seed and selector product, the complete flat Z and KL are identical across selector shapes although J/I can differ. This is a conditional extension of the reviewed mechanism, not a new broad universal supplier. A negative constant seed with multiple selectors is an AND sign; the one-selector signed-literal conclusion is not extrapolated. Both actual empty atom and all occupied terminal labels remain in the account.

The exact first unsupported line toward full FEI is payment of arbitrary inherited J_seed from SAME genuinely unused original degree-weighted capacity, after previous debits and complete reference conversion. Neither normalizer control nor zero carry pays it. No full FEI constant or Boolean counterfamily is claimed.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was written before execution. Before the pilot, version1.1 changed only the pilot selection from the first16 rows (all constants) to indices17*k,k=0..15, covering nonconstant and multiselector branches; no computation had yet run and the512-case main domain did not change. Commands: python -X utf8 code/check.py --pilot and python -X utf8 code/check.py. Pilot: {pilot['assertions']} assertions on16 cases plus controls PASS in{pilot['runtime_seconds']:.6f}s. Main: {checks['assertions']} assertions on512 cases plus controls PASS in{checks['runtime_seconds']:.6f}s, with{checks['nonconstant_seed_cases']} nonconstant-seed and{checks['multiselector_nonconstant_cases']} multiselector nonconstant cases. Enumeration is16 labeled two-bit seeds times4 laws times4 selector laws, plus256 labeled three-bit seeds at one prescribed law/selector. Maximum physical dimension4; no symmetry reduction or escalation.

Multilinear Mobius coefficients are independently checked against centered physical moments using Fraction arithmetic. Complete per-label likelihood identities and canonical prime-log dictionaries verify entropy/KL identities exactly, without floating comparisons. Mandatory controls test same-wire reuse, physical restriction versus spectral absence, and deterministic zero/one selectors. Maximum outer J/Delta in ln4 units was{checks['outer_max_J_over_Delta_in_ln4_units']}; its sharp witness is{json.dumps(checks['sharp_witness'])}. This finite count differs from prior stage's61233 because this is a new frozen activation audit, not a rerun of the flat/tree formula census. The arbitrary-dimension/depth statement uses the written proof and induction. No formal compilation or measured peak RAM is claimed. Estimated90MB jobs were below300MB; no heavy-job memory admission was needed. No GPU, detached work, dimension escalation or existing-workload change occurred.

## proof dependencies and changed downstream conclusions

A042@1 now has an independent source-complete reconstruction of its stated conditional claim. The new multiselector corollary awaits independent review; it uses only the reconstructed one-selector inequality for induction. Source acceptance does not accept a universal seed bound. Ordinary KL and signed conversion retain the original seed allocation once; neither dropping epsilon KL_seed nor renewing epsilon(Z_seed-V) is permitted. No shared source, registry or another agent's files were changed.

## one next mathematical action and independent reviewer

A042/A044 reconstruct the multiselector sector conditioning and negative-constant guard; A041/A043/A091 challenge ownership of inherited seed J and KL after a real paid history. The single next action is an original-capacity supplier for arbitrary seed J (or its complete reference bill), retaining all old debits, signed conversion and both full terminals. Additional rare wrappers alone do not supply it.

## actual persistence receipts or precise save blocker

All four protocol files and proof/spec/code/results are local to this designated A045 run. The finalizer checks exact key sets, source hashes, PASS domain/counts, byte-identical PACKET_DELTA, each artifact under20MB and rolling STATUS exactly two lines; local SHA256 receipts are saved. WORKLOG/LEARNED are appended. Supervisor copying, mirror verification, brain ingestion, independent corollary review and publication are distinct and unobserved. The checklist working and done calls both failed because its shared lock was held too long; no lock was removed. Brain self-care remains degraded/unverified: owner-model97.7h, state-of-mind82.3h, dream33.0h at wake, affecting personal-context guidance; mathematical premises came from current files and exact derivations. No research job is left running, and existing workloads remain untouched.

## Universal bridge

This stage advances C020 whole-set witness cost and C024 history transfer by independently accepting A042's sharp actual activation scale payment, then exposing the complete finite-depth selector/seed spectrum, zero carries and inherited ordinary KL at every selector shape with no fresh original bank. It closes that realizability/transfer interface, not the universal supplier: arbitrary epsilon J_seed and epsilon KL_seed survive, and their original account cannot be renewed. The shortest route to full FEI is to pay that SAME inherited arbitrary-seed complete bill from unused original influence after genuine history, rather than adding another activation wrapper or isolated gate census.
'''
write(run/'REPORT.md',report)
status='STATE: Stage9 complete: A042 activation endpoint independently HOLDS; exact multiselector complete-reference transfer retains epsilon J/KL_seed; '+str(checks['assertions'])+' exact main checks PASS; FEI OPEN.\nNEXT: A042/A044 review multiselector sectors; pay arbitrary inherited seed J from SAME unused original deficit, old debits/full ordinary KL/signed conversion/BOTH terminals retained.\n'
write(agent/'STATUS.md',status)
tag=run.name
for filename,entry in [('WORKLOG.md',f'\n{stamp} {tag}: A042@1 full independent reconstruction HOLDS, no source repair. Fixed512-case Mobius/centered-moment/prime-log audit {checks["assertions"]} assertions PASS; pilot{pilot["assertions"]} PASS. Multiselector shape changes J/I while complete Z/KL depend on product; seed J/KL persists. No full FEI supplier. Checklist working lock failure; personal-context wake degraded.\n'),('LEARNED.md','\nStage9: For F=1-A+Ag with independent dyadic selector product A, every occupied seed label has integer scale shift |U|+sum_notU k_j; pure selector labels have j_a+|U|-1+sum_notU k_j. Thus zero carries and J_F=epsilon J_g+J_outer, with sharp J_outer<=3ln4 Delta_outer by one-selector induction. Complete flat Z_F=epsilon Z_g+4b epsilon(1-epsilon), and full KL_F=epsilon KL_g+w d_Bern(s||t), depend only on selector product, although I/J retain individual selector shape. Reusing a selector changes the actual empty mass; spectral absence is not physical restriction. Negative constant seed with multiple selectors is an AND sign, not a signed literal. A042 full endpoint claim independently HOLDS; arbitrary inherited seed J supplier remains OPEN.\n')]:
 old=(agent/filename).read_text(encoding='utf-8') if (agent/filename).exists() else ''
 if tag not in old if filename=='WORKLOG.md' else 'Stage9: For F=1-A+Ag' not in old:write(agent/filename,old+entry)
claimkeys=set(proto['required_per_run']['claim_fields'])
progresskeys=set(x.split(' (')[0] for x in proto['required_per_run']['progress_fields'])
for c in load(run/'CLAIMS.json'):assert set(c)==claimkeys
assert set(load(run/'PROGRESS.json'))==progresskeys
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in proto['required_per_run']['report_fields']:assert field in report
assert report.rsplit('## Universal bridge',1)[-1].strip()
dump(run/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_records':2,'progress_exact_keys':True,'compatibility_byte_identical':True,'report_all_required_fields':True,'status_exactly_two_lines':True,'at':stamp})
artifacts=[]
for p in sorted(run.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  artifacts.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(run/'out/PERSISTENCE_RECEIPTS.json',{'status':'LOCAL_SAVED_VALIDATED','at':stamp,'artifacts':artifacts,'remote_copy_verified':False,'independent_corollary_review':False})
for rec in artifacts:assert sha(run/rec['path'])==rec['sha256']
print(json.dumps({'status':'SAVED_VALIDATED','run':str(run),'assertions':checks['assertions'],'source_review':'HOLDS','artifacts_verified':len(artifacts),'full_fei':'OPEN'}))
