from pathlib import Path
import copy, hashlib, json
from datetime import datetime, timezone

root=Path(__file__).resolve().parents[1]; agent=root.parents[1]; workers=agent.parents[1]
reports=Path(r'~\mop_fei100\reports\fei-2026-10-11')
previous=agent/'runs'/'20261013T220854Z-account05-A007-root-normalization'
a008=workers/'agents'/'A008'/'runs'/'20261013T222820Z-account05-A008-gate-label-compression'
a006=workers/'agents'/'A006'/'runs'/'20261014T011124Z-account05-A006-posterior-forest-optimization'
a015=workers/'agents'/'A015'/'runs'/'20261014T001450Z-account05-A015-minterm-barrier-analysis'
forest=reports/'source_material'/'reductions'/'paper'/'forests.tex'
stamp=datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data): Path(p).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

sources=[reports/'EXECUTION_PROTOCOL.json',workers/'BOARD.md',workers/'claude'/'B02'/'STREAM_NOTES.md',
         a008/'CLAIMS.json',a008/'COMPLETE_MASS.md',a008/'REPORT.md',a006/'REPORT.md',
         a015/'SINGLETON_INTERFACE.md',previous/'CLAIMS.json',previous/'LIFT.md',previous/'code'/'check_lift.py',forest]
save(root/'out'/'SOURCES.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
original=next(c for c in json.loads((a008/'CLAIMS.json').read_text(encoding='utf-8-sig')) if c['claim_id']=='A008-COMPLETE-QUEUE-DEGREE-WEIGHTED-DETERMINANT-MASS')
reviewed=copy.deepcopy(original)
reviewed['review_records'].append({'reviewer':'A007','verdict':'HOLDS_AT_ORIGINAL_FORMAL_STATEMENT_NO_REPAIR',
    'proof_source':str(root/'REVIEW_A008.md'),'validation':str(root/'out'/'EXACT_CHECK.json'),
    'method':'Reconstruct original conditioned queue and all operator/integral/bound/ambiguity clauses; independent chronological-event probability sum versus determinant operator on 503 minors',
    'reviewer_supplied_substantive_repair':False,
    'source_scope_correction':'Auxiliary t_singleton=1/2 sentence in COMPLETE_MASS.md is false, as A006 already observed. The unchanged formal theorem keeps t explicit. Both endpoint orders on width two give t_singleton=1/4.',
    'timestamp_utc':stamp})
reviewed['status']='INDEPENDENTLY_RECONSTRUCTED_FORMAL_SCOPE_LOCAL_ADOPTION_PENDING'
statement=("For every nonconstant uniform Boolean g=2B-1 with its full finite signed prime-conjunction table, positive fixed feasible lambda, one fixed full order per gate, every r>=1 and fixed 0<beta<=1 with beta sum lambda<=1, use F=2A_r B-1, p=2^-r, lambda'=beta lambda, pi'=p pi and core-first orders. For every covered nonempty data T, each actual base partition forest rho with roots R and tree components V_a, and every core ownership map alpha:U->V on nonempty U, there is an injective distributed-core component-tree lift to distinct actual activated partition events. For c=|R|>=2 its exact added-event multiplicity rooted at a is u_a product_(k=1)^(c-2)(|U|+k), where u_a counts core coordinates owned in V_a; for c=1 it is one. Its selected surrogate mass is exactly p S(T)G_dist,U(T) defined in DISTRIBUTED_LIFT.md, and contains the previous root-star family. Retaining the same base posterior and signed log[D'/(pD)], the full optimized activated residual satisfies R_F<=pR_g+(7/2)pI(g)+(6/5+log2(e)/4)I_core(F)+Psi_dist with Psi_dist<=Psi of the old lift. For equal-width base clauses, root/component history cancels from the added-root sum, giving the exact occupation sum Z_tau(u) in that proof. Exact strict mass gain occurs on an overlapping two-clause positive-spectrum set. No dimension-independent Psi_dist payment or universal FEI closure is asserted; surrogate mass is not exact queue probability.")
new={'claim_id':'A007-DISTRIBUTED-CORE-COMPONENT-LIFT','version':1,'exact_statement':statement,
    'hypotheses':['finite uniform cube; nonconstant g=2B-1; all nonempty signed prime conjunctions',
        'globally fixed positive feasible lambda and one full physical support order per gate',
        'fresh positive r>=1 conjunction core; fixed beta in (0,1] with beta sum lambda<=1',
        'original actual once-per-gate partition forests; roots restricted to one per original source SCC',
        'components in the distributed construction are actual base forest trees, not source SCCs',
        'core ownership ranges only over already-used data gates; fixed deterministic root/coordinate orders',
        'bits, gamma=6/5; size/subset/count/multiset factors not equated with surrogate B weights',
        'equal-width occupation collapse conditional on common base pi=2^-w; unequal widths retain component-dependent root weights'],
    'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A007'],
    'proof_source':{'path':str(root/'DISTRIBUTED_LIFT.md'),'certificate':str(root/'out'/'EXACT_CHECK.json'),'overlap_witness':str(root/'OVERLAP_CERTIFICATE.md')},
    'proof_dependencies':[{'source':str(forest),'sha256':sha(forest),'locators':['original queue','eq:forestconditioning','eq:forestcost','thm:posteriorforest'],'status':'SOURCE_COMPLETE_BASELINE'},
        {'claim_id':'A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS','version':1,'status':'PREVIOUSLY_INDEPENDENTLY_ACCEPTED_BY_A007','use':'exact computation of the base posterior; component determinant also proved directly'}],
    'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
    'first_unproved_line':None,'next_consumers':['A006','A008','A009','A010','A014','A015','A086','A094','B02','B03','B20']}
claims=[reviewed,new]
save(root/'CLAIMS.json',claims)
nextaction='Pay the signed Psi_dist expectation using the exact occupation sum Z_tau and its unequal-width component-weighted counterpart under the SAME base assignment posterior, with beta scaling and nonempty-root normalization retained; A086/A094 reconstruct the distributed lift.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B02','packet_id':'A007',
    'gap_id':'C020/PI-J-JOINT-COST','attempt_id':'A007-stage4-distributed-core-ownership',
    'method':'Whole formal complete-queue review; inverse-trace distributed-core lift; incoming component Laplacian and factorial moments; equal-width occupation collapse; exact event/probability certification',
    'mathematical_delta':'A008 complete-mass formal v1 independently accepted with its known auxiliary singleton-probability error isolated. Distributed lift includes every previous root-star event, preserves all base data witnesses and improves Psi_dist<=Psi. Equal-width component/root history cancels into exact occupation sum Z_tau. 70,464 full exact assertions, 5,004 distributed traces, 251 strict positive-spectrum gains; universal expected payment remains open.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_INTERFACE_PROVED_UNIVERSAL_PIJ_AND_FEI_OPEN',
    'claim_versions_used':[{'claim_id':reviewed['claim_id'],'version':1,'status':reviewed['status'],'use':'complete-probability accounting review; no missing-factor substitution'},
        {'claim_id':'A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS','version':1,'status':'PREVIOUS_A007_WHOLE_ACCEPTANCE'},
        {'claim_id':'A007-ACTUAL-DATA-WITNESS-ROOT-LIFT','version':1,'status':'AUTHOR_PROVED_REVIEW_PENDING','use':'continuation target and comparison; paid constants reconstructed directly here'}],
    'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
    'source_artifacts':['REPORT.md','DISTRIBUTED_LIFT.md','REVIEW_A008.md','OVERLAP_CERTIFICATE.md','FROZEN_SPEC.json','code/check.py','code/finalize.py','out/PILOT.json','out/EXACT_CHECK.json','out/SOURCES.json','out/RECEIPTS.json'],
    'next_consumers':new['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,
    'blockers':['Psi_dist<=K I(F) remains unproved for arbitrary overlapping signed prime tables','new narrow continuation requires independent reconstruction; prior root-lift acceptance not inferred','local review does not verify shared registry or remote mirror adoption'],
    'packet_ids':['A007']}
save(root/'PROGRESS.json',progress); save(root/'PACKET_DELTA.json',progress)

report="""# A007 stage 4: distribute the core without losing the data witness

## exact target, quantifiers, hypotheses and units

C020 whole-set witness cost / the B02 lead's PI-J target. For every finite nonconstant Boolean g=2B-1 with its full signed prime-conjunction table, fix positive feasible lambda and one full order per gate. For every r>=1 activate through a fresh positive common conjunction F=2A_r B-1, p=2^-r. Choose beta globally with 0<beta<=1 and beta sum lambda<=1, and fix lambda'=beta lambda with all fresh coordinates first. Costs are bits, gamma=6/5. The reference is fixed before the Fourier set; posterior ownership choices are actual events of that reference, not a free selector between references.

This stage allows every assignment of selected core coordinates to already-used data gates while preserving the entire base data witness. It proves an exact actual-event multiplicity and mass formula, improves the old signed joint debt Psi_dist<=Psi, and collapses component/root history into an explicit occupation sum when clause widths agree. It does not prove an absolute influence bound on that debt. R below is the complete surrogate residual, excluding the separately retained h2(variance) and K_ref I terms.

## sources actually read, revisions and theorem locators

Read BOARD.md (2026-10-14 01:41 UTC), B02 STREAM_NOTES.md v2 (2026-10-11 23:35 UTC), own STATUS and prior stage's LIFT/CLAIMS; reread the full execution protocol revision 2026-10-11-execution-v2. Long board output required follow-up middle chunks. Read A008 stage-3 COMPLETE_MASS.md, CLAIMS.json and REPORT.md; A006 stage-4 REPORT.md, including its independent complete-mass review and auxiliary singleton-probability correction; A015 stage-3 SINGLETON_INTERFACE.md, including actual witness-label erasure and physical allocation boundary. Reread forests.tex original queue, source-SCC partition interface, eq:forestconditioning, eq:forestcost and thm:posteriorforest. Hashes are out/SOURCES.json; mutable board hashes reflect final saved source bytes. Earlier campaign/paper baseline reads remain inherited and are not claimed as newly reread.

The lead's original A009/activated-tribes task is already completed. The current board adds an exact complete-queue interface and warns against confusing factorial surrogate mass with actual probabilities; graph matching/star coverage has also been addressed by A006. Accordingly this stage resumes the productive signed activation gap and consumes/reviews the new complete-mass dependency before any new broad candidate. It does not repeat graph matching, sparse affine calibration, or a variational identity. It does not claim the stream-wide review cap has disappeared.

## complete derivation or exact first unsupported line

DISTRIBUTED_LIFT.md contains the all-dimensional proof. For a base actual forest, remove neither its data assignment nor its edges. Distribute selected core U over its used gates, then connect the old tree components through core-attached edges in an acyclic component tree. The surviving root can be above the core-owning gate within its old tree. Reading the activated event, deleting core edges, and replaying the fixed original queue order recovers the unique old forest and core ownership. This proves disjoint actual events across old forests, assignments and all attachment permutations.

For c>=2 old roots, let u_a count core coordinates owned anywhere in the old tree rooted at a. The component incoming Laplacian minor is X I-1 q^t, so its determinant is q_a X^(c-2). A direct column expansion proves this formula. The factorial monomial map counts genuine repeated-slot child-label sequences and gives the exact count u_a(u+1)...(u+c-2). For c=1 the count is one for every ownership map. Summing roots gives (u)_(c-1); equal base rarity makes the added-root weighted sum independent of the old trees. The remaining ownership multiplicity is the explicit multinomial congestion sum Z_tau(u), with the same old assignment posterior retained.

The selected surrogate mass is exactly p S(T)G_dist,U(T), at least the earlier root-star mass. Its signed normalization is still log[D'/(pD)] with D=prod(1+lambda pi)-1=2^Lambda Z. This term is kept in the exact identity before using <=log beta. Empty selected core and core-only one-gate events retain their prior exact masses. Directly rechecking binomial reciprocal identities pays private ranks and extra empty-core rarity by (7/2)p I(g), and core rank plus core-only normalization by [6/5+log2(e)/4]I_core(F). Thus

    R_F <= p R_g+(7/2)p I(g)+[6/5+log2(e)/4]I_core(F)+Psi_dist,
    Psi_dist <= Psi.

The precise first unsupported line is Psi_dist<=K I(F), uniformly over arbitrary overlapping signed prime tables with suitable globally fixed feasible weights. Equal-width history cancellation does not pay congestion, beta labels or the base assignment posterior. Nor does positivity/strict improvement on finite cases establish a universal expected-cost bound.

OVERLAP_CERTIFICATE.md gives a positive-spectrum strict witness with B=(x0 AND x1) OR (x0 AND x2), r=1, T={0,1}, U={core}, lambda0=lambda1=1/2 and beta=1. D=17/64 and D'=33/256. The old two-event mass is 1/16+(1/32)(1/3)^(6/5); the distributed family adds exactly (1/32)(2/9)^(6/5)>0. The physical Fourier coefficient is 1/8. The improvement is an exact positive algebraic summand with the SAME retained log D', not a numerical entropy estimate or FEI disproof.

REVIEW_A008.md reconstructs the whole formal complete-queue claim without repair: conditioned root odds, labels once per used gate, original subset/size factors, degree-dependent count/multiset operator, beta/exponential/simplex representation, coefficient bounds, sunflower separation and final output aggregation. A006 already identified the auxiliary t_singleton=1/2 sentence as false. This stage confirms it: with both endpoint orders on width two t_singleton=1/4. The formal theorem keeps t explicit and is accepted unchanged; the auxiliary source sentence is not accepted. No such substitution enters the distributed proof.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the jobs. Pilot: all four nonconstant labelled monotone n=2 prime tables, r=1, 233 assertions PASS in 0.003294 helper seconds. Full fixed domain: all 22 labelled nonconstant monotone prime tables on n=2,3 with each r=1,2,3, plus the heterogeneous prime table {01,12,023} on n=4 with r=1,2. Thus 68 activated Boolean functions. Every covered nonempty data set, eligible assignment, base actual partition trace, selected nonempty core, ownership map and acyclic component attachment is enumerated; no symmetry reduction or random search. Counts repeated across r are reported as executed cases, not unique mathematical assignments.

The final full check passed 70,464 assertions in 1.352211 helper seconds: 475 data-assignment cases, 509 base events, 3,759 core maps, 5,004 distributed events, 2,346 old root-star events, 503 complete-operator root minors, 2,581 equal-width root-collapse checks and 1,653 exact occupation-sum checks. Old traces are deduplicated and explicitly included. Strict mass gain occurs in 284 covered cases, of which 251 have positive activated spectral mass. The latter is verified by integer FWHT, not presumed from combinatorial coverage. Pilot assertions are separate; superseded intermediate outputs are not added to totals.

Arithmetic is integer truth tables/FWHT and independent pivotal-edge influence, exact Fraction normalization/probabilities, sparse integer determinant polynomials, explicit chronological event keys, and formal rational-base powers z^(6/5). Irrational structural weights are not rounded or called rational. The complete-mass review compares direct chronological count/multiset probability sums with N_s applied to determinant monomials, separately checks its beta/simplex moment formula and both exact bounds, and retains original algebraic subset factors symbolically. The new actual-event proof and all-r constants are analytic, not extrapolated from these small cubes.

Commands from this run directory:

    python -X utf8 code/check.py --pilot
    python -X utf8 code/check.py
    python -X utf8 code/finalize.py

Only A007's own prior independent checker helpers are reused via reading/compiling their source; no A008/A006 author code is imported and no prior artifact is written. All jobs were frozen below 150 MB and 60 seconds, one at a time; the >300 MB memok trigger did not apply. Memory is an estimate, not a measured peak. No automatic dimension escalation, GPU, window, background job, git, external message or brain mutation was used. No mathematical check failed in this stage.

## proof dependencies and changed downstream conclusions

A008-COMPLETE-QUEUE-DEGREE-WEIGHTED-DETERMINANT-MASS v1 receives local independent acceptance at its original formal statement/hash, with the known auxiliary source error scoped separately and no repair to the formal theorem. A007 remains an independent reviewer for that statement. The accepted A006 determinant interface computes the correct base posterior. The distributed component determinant and all paid constants are proved directly here; the previous A007 v1 remains independently unreviewed and is used as a comparison/continuation target, not as evidence of universal payment. A015's singleton interface and A006 graph result are dispatch context, not new theorem premises.

New A007-DISTRIBUTED-CORE-COMPONENT-LIFT v1 is author-proved/exactly-checked and pending independent review. It removes the artificial restriction that only old roots can own core coordinates and gives a strict superset of the old valid runs. For equal widths, added-root history cost collapses exactly into Z_tau, while unequal widths retain component-weighted rare-root costs. This improves the same whole-set functional and preserves signed normalization; the unknown absolute PI-J constant is unchanged.

## one next mathematical action and independent reviewer

Pay the signed Psi_dist expectation using Z_tau and its unequal-width component-weighted counterpart under the SAME base assignment posterior, retaining beta labels and the nonempty-root normalizer. The core distribution mechanism is now explicit; the next step must bound its expectation or provide an actual Boolean obstruction to this selected mechanism. A086/A094 should independently reconstruct the inverse trace, the root-not-core-owner case, c=1 boundary, component-minor factorial count and signed ledger. A006/A008 can insert the component polynomial into their existing complete-mass calculations; A015 can couple physical allocation to this whole-set posterior. No external message was sent.

## actual persistence receipts or precise save blocker

All four protocol files, distributed proof, scoped whole-review note, exact overlap certificate, frozen spec, code and outputs are saved only in the authorized A007 stage directory. Rolling STATUS has exactly two STATE/NEXT lines; WORKLOG and LEARNED are appended. out/RECEIPTS.json records sizes and SHA256, checks exact protocol field sets and matching PROGRESS/PACKET_DELTA, preserves the reviewed formal statement/hash, and verifies local file bytes after saving. Every file is below 20 MB. Supervisor registry adoption and GitHub/brain mirror copying are unobserved; no local save blocker.

## Universal bridge

This stage moves C020 whole-set witness cost / PI-J by replacing root-only activation stars with an invertible distributed-core component-tree family, proving exact u_a(u+1)...(u+c-2) actual-event multiplicity and Psi_dist<=Psi with every negative normalization term retained; equal-width clauses now reduce added-root history to an explicit occupation sum, and 251 positive-spectrum finite cases show strict gain. A008's whole formal probability interface is independently accepted with its auxiliary singleton correction isolated. The universal constant is still unproved: Psi_dist and a universally paid base reference remain. NEXT bounds that signed occupation/component-weighted expectation under the same posterior, which directly attacks the surviving general congestion/scale-label obstruction rather than adding another isolated family estimate.
"""
(root/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A007 stage 4 complete: A008 formal complete mass independently accepted with known auxiliary t error isolated; distributed-core lift includes old stars, equal-width root history collapses; 70,464 exact checks, 251 positive-spectrum strict gains; Psi_dist/PI-J/FEI OPEN.\nNEXT: Pay signed Psi_dist via exact occupation sum and unequal-width component weights under the same base posterior, retaining beta labels and normalization; A086/A094 review distributed lift.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+' -- Stage 4: read board/lead and new A008/A006/A015 dependencies. Independently accepted A008 complete-mass formal v1, retaining its explicit t and isolating the already-reported auxiliary t=1/2 error. Distributed all selected core coordinates among existing data owners and connected old tree components; invertible actual-event map proved, component Laplacian gives u_a(u+1)...(u+c-2). Equal-width root history cancels into exact occupation sum. 70,464 full exact assertions PASS, 5,004 distributed events, 251 strict positive-spectrum gains; two-overlapping-clause algebraic certificate saved. Signed Psi_dist remains unpaid; no mathematical check failure. Local artifacts/rolling files saved; mirror unverified.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''\n## Stage 4 durable additions

- Core ownership need not be restricted to old roots. Any used gate can own selected core coordinates; an old root above that owner can remain the surviving root. Delete only added core-attached edges and replay the original queue to invert the event.
- Treat actual base forest TREE components, not source SCCs, as the connecting vertices. For c>=2 the root-a minor is q_a X^(c-2); exact factorial event count is u_a(u+1)...(u+c-2). For c=1 count is one for every core assignment. Sum over roots is (u)_(c-1).
- Equal clause widths make pi_a/prod_R pi common, so added-root history cancels into (u)_(c-1)pi^(1-c) times the exact multinomial congestion occupation sum Z_tau. The same old assignment posterior remains; unequal widths retain component-weighted rarity.
- Distributed mass contains all old root-star events. Hence Psi_dist<=Psi with the same signed normalizer and paid constants: R_F<=pR_g+(7/2)pI(g)+(6/5+log2(e)/4)I_core(F)+Psi_dist. No universal Psi_dist payment follows merely from the improvement.
- Exact overlapping witness: base clauses {01},{02}, lambda=1/2, beta=1, r=1, T={0,1}, U={core}, Fourier coefficient 1/8. Old mass 1/16+(1/32)(1/3)^(6/5); distributed mass adds (1/32)(2/9)^(6/5)>0. Root need not own the core. Keep common log D'=log(33/256).
- A008 formal complete-queue v1 independently holds with all subset/size/count/multiset factors explicit. Its auxiliary t_singleton=1/2 sentence is false (A006 already flagged it); both endpoint orders on width two give t_singleton=1/4. Surrogate factorial mass is never exact queue probability.
''')

protocol=json.loads((reports/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(progress)=={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
assert reviewed['exact_statement']==original['exact_statement'] and reviewed['statement_sha256']==original['statement_sha256']
assert json.loads((root/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((root/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('## Universal bridge\n')[1].count('\n')==1
files=[p for p in root.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']+[agent/name for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipts=[]
for p in sorted(files):
    assert p.stat().st_size<20*1024*1024
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save(root/'out'/'RECEIPTS.json',{'timestamp_utc':stamp,'protocol_schema':'PASS','local_only':True,'files':receipts})
for item in receipts: assert sha(item['path'])==item['sha256']
print(json.dumps({'status':'PASS','claims':len(claims),'receipt_files':len(receipts),'run':str(root),'full_fei':'OPEN'}))
