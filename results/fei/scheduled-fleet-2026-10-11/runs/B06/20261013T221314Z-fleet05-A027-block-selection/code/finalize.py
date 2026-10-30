import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]; team=agent.parents[1]
previous=agent/'runs'/'20261011T234627Z-fleet05-A027-block-selection'
other=team/'agents'/'A028'/'runs'/'20261012T011208Z-fleet05-A028-stopping-tree-payment'
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
now=datetime.now(timezone.utc).isoformat()
def dump(path,obj): (run/path).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
v=json.loads((run/'out'/'validation.json').read_text()); pilot=json.loads((run/'out'/'pilot.json').read_text())
assert v['status']==pilot['status']=='PASS' and v['partitions']==23232
claims=json.loads((previous/'CLAIMS.json').read_text(encoding='utf-8'))
old=next(c for c in claims if c['claim_id']=='A027-PARTIAL-CORE-ACTIVATION-TRANSPORT')
statement=old['exact_statement']+' Version 2 retains every version-1 component unchanged and strengthens the core-only transport: for every arbitrary Boolean controller a=1-2c on a DISJOINT uniform physical cube, p=Pr(a=-1), F=1+c(u-1), and every finite actual core-only stopping tree, Pi_I(F)=p Pi_I(u) and |Pi_H(F)-p Pi_H(u)|<=(4+12/ln(2))Pi_I(F), with 4+12/ln(2)<22. The controller spectral entropy cancels linearly across the core bias martingale, while all controller entropy remains in actual activated terminals. Their influence reserve is p E I(u_leaf)+Pr(u=-1)I(a). If the specified proper core partition has Pi_H(u)<=K Pi_I(u) and actual activated leaves have H<=L I, then H(F)<=max(K+4+12/ln(2),L)I(F). Ordinary controller FEI K_a and uniform core-leaf FEI K_l suffice for L=max(K_a+6,K_l), by the independently reconstructed A028 scalar correction. No universal paid core partition, arbitrary-controller certificate, or shared-support extension is asserted.'
new=dict(old); new.update(version=2,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),proof_source=str(run/'DERIVATION.md'),proof_dependencies=['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@1 (unchanged character/regular class and surcharge witness only)','C006/B06-R2 actual physical-tree influence conservation','A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@2 sections 1-2 only (independently reconstructed in INDEPENDENT_REVIEW.md; optional terminal certificate)'],review_records=[],status='PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',supersedes=[{'claim_id':old['claim_id'],'version':1,'reason':'same candidate extended; no previous component withdrawn'}],hypotheses=['Uniform independent physical controller and core cubes; Boolean signs; entropy bits','Controller a is arbitrary; controls remain unqueried throughout the actual core-only partition','Proper selection corollary leaves a physical core coordinate unqueried on every path','Paid core partition and actual terminal entropy certificates are explicit additional assumptions'],next_consumers=['A028','A029','A064','A065','A082','A087','A094','A097'])
claims=[c for c in claims if c['claim_id']!=old['claim_id']]+[new]
dump('CLAIMS.json',claims)
review={'claim_id':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT','version':2,'reviewer':'A027','verdict':'HOLDS_AT_SCOPED_SECTIONS_1_2_6','source':str(other/'REPORT.md'),'source_sha256':sha(other/'REPORT.md'),'review_artifact':'INDEPENDENT_REVIEW.md','scope':'Exact arbitrary-controller spectrum, C0 scalar correction, control-first terminal payment, FEI-equivalence. No acceptance asserted for unchanged KL component or strong nesting component.','independence':'new prime-log checker and independent coefficient/convexity reconstruction; no repairs supplied','assertions':v['assertions'],'status':'LOCAL_REVIEW_SAVED_REGISTRY_ADOPTION_UNOBSERVED'}
dump('out/A028_SCOPED_REVIEW.json',review)
nextaction='Build the actual projected core partition when point controls and core queries interleave: assign each active leaf weight w*p_leaf/p, keep one signed bias reserve, and require a terminal-inclusive payment without repeatedly charging the same core influence. A028 owns arbitrary controller-first trees and shared-control two-event extension; do not duplicate them.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B06','packet_id':'A027','gap_id':'G-R-SELECT','attempt_id':'A027-G-R-SELECT-003','method':'Consume and independently reconstruct A028 controller identity; cancel linear controller entropy using actual core bias martingale; bound remaining scalar potential globally','mathematical_delta':'Same partial-core candidate extended from point controllers to every disjoint Boolean controller, additive rate improved from 12+8/ln2 to 4+12/ln2<22; complete terminal budgets preserved. A028 sections 1,2,6 independently reviewed at scope.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT; EXTENDED_CANDIDATE_REVIEW_PENDING','mathematical_status':'PROVED_ARBITRARY_CONTROLLER_CORE_ONLY_TRANSPORT; UNIVERSAL_SELECTION_AND_FULL_FEI_OPEN','claim_versions_used':new['proof_dependencies'],'claims_created_or_changed':['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@2','A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@2 scoped review only'],'source_artifacts':['DERIVATION.md','INDEPENDENT_REVIEW.md','FROZEN_SPEC.json','code/check.py','code/finalize.py','out/pilot.json','out/validation.json','out/A028_SCOPED_REVIEW.json','SOURCE_READS.json'],'next_consumers':new['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['A universal paid proper core partition with certified activated terminals remains unproved','New version independent acceptance and mirror/adoption unobserved'],'packet_ids':['A027']}
dump('PROGRESS.json',progress); dump('PACKET_DELTA.json',progress)
sources=[]
for path,scope in [(protocol,'Entire protocol reread; revision 2026-10-11-execution-v2'),(team/'BOARD.md','Stage-opening board; relevant B05/B06 and cross-stream ownership/terminal findings inspected'),(team/'claude'/'B06'/'STREAM_NOTES.md','Entire v2 lead directions read; proper partial-core ownership followed'),(agent/'STATUS.md','Stage-opening own status'),(agent/'LEARNED.md','Prior durable facts and endpoint guard'),(previous/'DERIVATION.md','Own previous exact point-activation transport proof'),(previous/'code'/'check.py','Checker representation inspected; current proof uses independent prime-log implementation'),(previous/'CLAIMS.json','Prior exact statements retained'),(other/'REPORT.md','Arbitrary-controller sections 1,2,6 independently reconstructed; other bundled parts read but not reviewed'),(other/'CLAIMS.json','Version and source pin observed')]:
    sources.append({'path':str(path),'sha256':sha(path),'scope':scope})
dump('SOURCE_READS.json',{'observed_at':now,'sources':sources,'literature_scope':'No new paper-priority assertion. Prior campaign/paper readings remain recorded in earlier runs; no new theorem from an unread source is used.'})
report=f'''# A027 stage 3: arbitrary-controller proper-core transport

Full FEI remains OPEN. This stage extends the existing partial-core candidate, and independently reconstructs a scoped part of A028's new dependency. The universal existence of a paid proper stopping partition remains unproved.

## exact target, quantifiers, hypotheses and units

For every Boolean controller a=1-2c and Boolean core u on DISJOINT uniform physical cubes, set p=Pr(a=-1), d=Pr(u=-1), F=1+c(u-1). Every finite adaptive core-only physical tree satisfies Pi_I(F)=p Pi_I(u) and |Pi_H(F)-p Pi_H(u)|<=kappa Pi_I(F), kappa=4+12/ln2<22. Entropy is in bits; Hplus is the RAW nonempty spectral contribution. Controls remain unqueried. Proper trees leave at least one core coordinate on each path. The identity works more generally; properness is an explicit selection requirement, never inferred from W=[n].

If the specified proper core partition has rate K and its actual activated terminals have certified entropy rate L, then H(F)<=max(K+kappa,L)I(F). Arbitrary controller/core-terminal certificates are additional hypotheses, never supplied by the transport identity. This extends the old point-controller bound and retains all previous character/regular-terminal results and surcharge-four obstruction unchanged.

## sources actually read, revisions and theorem locators

Read the current BOARD, B06 STREAM_NOTES v2, own STATUS and LEARNED, and the entire execution protocol revision 2026-10-11-execution-v2. SOURCE_READS.json pins consulted artifacts. The lead's partial-core target is already completed at point-controller scope; this stage consumes A028's useful new arbitrary-controller identity to strengthen the same target. A028 retains ownership of controller-first selection and shared-control two-event work.

A028 stage 20261012T011208Z REPORT sections 1,2,6 and CLAIMS version 2 were reconstructed independently. Own prior DERIVATION, checker, and claims were consulted for continuity. Existing paper/regular-terminal dependencies remain pinned in prior runs; no new literature priority or unread theorem is claimed.

## complete derivation or exact first unsupported line

DERIVATION.md gives the complete proof. Direct spectrum summation yields H(F)=pH(u)+dHplus(a)+R(p,d), retaining the constant coefficient. Across an actual core partition, sum w d_leaf=d, so dHplus(a) cancels EXACTLY even if its dimension or entropy is arbitrarily large. Differentiating the remaining scalar potential gives |partial_d R|<=p(8+24/ln2). Coupling queried physical edges bounds total expected bias variation by Pi_I(u)/2; their combination proves kappa=4+12/ln2. All deterministic endpoints are explicit and no leaf bias is assumed small.

The complete unspent influence is p E I(u_leaf)+d I(a); queried influence is p Pi_I(u). Thus terminal certificates are paid once from a separate actual budget. Taking u identically -1 leaves F=a with zero core-query budget, making the controller terminal debt impossible to discard.

INDEPENDENT_REVIEW.md reconstructs A028's controller correction via convexity of phi(t)+12bt^2, b=1/ln2, and independently checks C0=2+2b+b/sqrt(e)<6. HOLDS applies only to the exact spectrum, scalar correction, control-first terminal implication and FEI-equivalence, not every component of the bundled claim. No repair was required.

First unsupported universal line: every Boolean core admits a proper partition with bounded Pi_H/Pi_I and uniformly certified ACTUAL activated terminals, without assuming arbitrary-controller or residual-core FEI. The improved transport supplies neither existence nor those certificates. Shared physical support is excluded throughout.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before search: all 22 Boolean controllers of dimensions 0,1,2; all 16 two-bit cores with two proper singleton partitions; additionally all 256 three-bit cores with four adaptive policies (root coordinate 0, each child independently stops or queries coordinate 1). No symmetry quotient; both biases/constants included; physical core coordinate 2 remains unqueried in the adaptive family. Total {v['partitions']:,} actual proper partitions, maximum 32-entry truth table.

Commands from A027: `python -X utf8 runs/{run.name}/code/check.py --pilot` and the same without `--pilot`. Pilot passed {pilot['assertions']:,} assertions on 704 partitions in {pilot['elapsed_seconds']:.3f}s. Full run passed {v['assertions']:,} assertions in {v['elapsed_seconds']:.3f}s. The full proof identities are checked as EXACT canonical prime-log vectors, stronger than overlap of entropy intervals. Independent physical edge counts, restricted truth tables, bias martingale, terminal reserve, and 6,072 activated-pair identities are checked. Rational log intervals certify rate 22 and the consumed A028 correction at rational 6; sharper analytic constants use the written proof.

The helper uses 24-term rational atanh expansions with positive explicit remainder, binary range reduction, division by a positive ln2 enclosure, and outward dyadic rounding to denominator 2^52. No floating sign is a certificate. Estimated memory 160 MB, runtime cap 60 seconds; the >300 MB gate did not apply. No heavy job, GPU, automatic dimension increase, or formal-kernel claim. The pilot assertion-count metadata was corrected to exclude the separately counted partition total; the mathematical checks and domain did not change.

## proof dependencies and changed downstream conclusions

The transport itself uses direct Fourier algebra and the recovered physical-tree budget plus finite martingale variation. It does not depend on the arbitrary controller satisfying FEI. The optional terminal estimate L=max(K_a+6,K_l) uses the scoped, independently reconstructed A028 scalar correction together with explicit controller/core-leaf certificates.

The same A027 candidate is extended to version 2; no additional broad candidate is opened at the stream's review cap. Prior version components remain immutable and retained, including its exact surcharge-four witness. The locally saved scoped A028 review does not assert acceptance of its unchanged KL or stronger-conjunction components. A029/A064/A065/A082/A097 may use the transport on one ACTUAL leaf partition; controls remain terminal, and repeated reuse of the same core influence is invalid.

## one next mathematical action and independent reviewer

{nextaction} This tests a concrete ownership/cancellation interface beyond simply improving class constants. A087 is the primary reviewer of version 2; A094 challenges terminal and history transfer; A082 can test the terminal interface using its certified finite-dimensional class. These are source-bound handoffs, not delivered messages or acceptance receipts.

## actual persistence receipts or precise save blocker

All four protocol files, proof, scoped review, frozen spec, checker and outputs, source hashes, and persistence receipt are saved in this immutable run within A027. STATUS is two lines; WORKLOG and LEARNED are updated locally. The receipt checks exact protocol key sets, statement hashes, required report fields, file sizes and identical PROGRESS/PACKET_DELTA. Supervisor copying, mirror verification and independent acceptance of the extended A027 candidate remain unobserved.

## Universal bridge

This stage moves C019 at the proper partial-core transport interface by canceling arbitrary controller spectral entropy exactly and reducing the proven additive transport constant from 12+8/ln2 to 4+12/ln2<22. It also supplies an independent scoped reconstruction of A028's scalar controller payment. The unpaid universal obligation remains selection of a proper core partition with certified actual terminal entropy; no controller entropy has disappeared from the final ledger. NEXT projects interleaved point-control/core trees onto one physical core partition and tests a single signed reserve with terminal debt retained. This is the shortest continuation toward universal FEI because it addresses nonreusing ownership in adaptive histories, whereas more disjoint controller classes would leave the same core-selection and terminal certificate gap.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: Stage 3 complete locally: arbitrary-controller partial-core transport kappa=4+12/ln2<22 proved; 273,064 exact assertions PASS; A028 scalar payment scoped HOLDS; FEI OPEN.\nNEXT: Project interleaved point-control/core trees onto one actual core partition with a single signed reserve and full terminal debt; A087/A094 review A027 transport v2.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(f'\n{now} — {run.name}: Consumed A028 stage2 arbitrary-controller identity and independently reconstructed sections1,2,6. Extended existing A027 transport candidate to arbitrary disjoint controllers by exact cancellation of linear controller entropy; kappa=4+12/ln2<22, all terminal control influence reserved. Frozen704-case pilot and23,232-partition census PASS273,064 exact assertions in{v["elapsed_seconds"]:.3f}s. No shared-support claim. Universal proper-core selection remains first unsupported line. Scoped A028 HOLDS saved; new A027 version2 awaits review.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f: f.write('''
## Stage 3: arbitrary-controller partial-core transport

For any Boolean controller a=1-2c on DISJOINT inputs, p=Pr(a=-1), d=Pr(u=-1), V=4p(1-p), F=1+c(u-1): H(F)=pH(u)+dHplus(a)+R(p,d), R=4d(1-d)eta(p^2)+2d(1-d)V+V E(d)+E(1-2pd)-pE(1-2d). Hplus is raw nonempty entropy. The dHplus(a) term cancels exactly across any actual core-only partition. |R_d|<=p(8+24/ln2) and bias martingale variation<=Pi_I(u)/2 yield |Pi_H(F)-pPi_H(u)|<=(4+12/ln2)Pi_I(F), kappa<22, independent of controller dimension/spectral entropy. This strengthens point-only rate12+8/ln2 while retaining its old sharpness obstruction.

Terminal reserve remains p E I(u_leaf)+d I(a). Controller entropy cancellation is a decrement identity, not terminal entropy payment: u=-1 gives F=a with zero core query budget. Specified core partition at rateK and actual activated leaf allowanceL imply root max(K+kappa,L). A028 reconstructed scalar correction gives L=max(K_a+6,K_l) if controller/core-leaf FEI certificates are explicit. Shared controller/core physical support is excluded.

A028 stage2 sections1,2,6 independently reconstructed and HOLDS at that scope, using new exact canonical prime-log checker. This does not review every bundled KL/strong nesting component. Full frozen validation23,232 proper partitions/273,064 assertions PASS;6,072 exact controller/core identity pairs, maximumfive variables. New A027 version2 pending independent acceptance. Next target is projected interleaved point-control/core partition with single physical ownership and actual terminal debt, not another arbitrary-controller class theorem.
''')
schema=json.loads(protocol.read_text(encoding='utf-8'))['required_per_run']
assert set(progress)=={k.split(' (')[0] for k in schema['progress_fields']}
assert all(set(c)==set(schema['claim_fields']) for c in claims)
assert all(hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256'] for c in claims)
assert all(field in report for field in schema['report_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((agent/'STATUS.md').read_text().splitlines())==2
files=[]
for path in sorted(run.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE_RECEIPT.json':
        assert path.stat().st_size<20*1024*1024
        files.append({'path':str(path.relative_to(run)),'bytes':path.stat().st_size,'sha256':sha(path)})
dump('out/PERSISTENCE_RECEIPT.json',{'status':'PASS','observed_at':now,'schema_checks':'exact keys, statement hashes, report fields, compatibility identity, two-line STATUS, size caps PASS','files':files,'rolling_files':[{'path':str(agent/p),'sha256':sha(agent/p)} for p in ['STATUS.md','WORKLOG.md','LEARNED.md']],'mirror_verification':'UNOBSERVED','independent_review_of_A027_v2':'PENDING'})
print(json.dumps({'status':'PASS','files_saved':len(files)+1,'partitions':v['partitions'],'assertions':v['assertions'],'claim_version':2,'full_FEI':'OPEN'}))
