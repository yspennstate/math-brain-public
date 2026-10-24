import json, hashlib
from pathlib import Path
from datetime import datetime, timezone

root=Path(__file__).resolve().parents[1]
agent=root.parents[1]
campaign=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
context=Path('~/brain_workers/FEI100_20261011/context')
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
sources=[campaign/f for f in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources += [supp/f for f in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += list((supp/'sources').glob('*.md'))+list(context.glob('*.txt'))
sources += [Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B07/STREAM_NOTES.md')]
sources += list((campaign/'runs').rglob('REPORT.md'))
prior=Path('~/brain_workers/FEI100_20261011/agents/A031/runs/20261011T214115Z-account05-A031-convolution-identity')
sources += [prior/'REPORT.md',prior/'DERIVATION.md',prior/'CLAIMS.json']
save(root/'out/source_receipts.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':'source inventory; precise inspected sections and uses in REPORT.md'} for p in sources])

statement=('For every integer d>=1, a Boolean sign on disjoint uniform physical X,Y cubes whose distinct X Fourier labels S_j have size <=d and whose partial rows are unit quadratic signs on affine Y partition cells A_j of codimension k_j has H(S_Y|S_X)=sum_j 2^(-k_j)(k_j+r_j)<=2 I_Y, H(S_X)=sum_j 2^(-k_j)k_j, and H(f)=sum_j 2^(-k_j)(2k_j+r_j)<=4 I_Y, where r_j is the quadratic polar rank restricted to the direction space of A_j. Admission is stable under every coordinate Y restriction and X restrictions preserving injective projected labels. Every admitted Boolean tensor factor on fresh Y bits is a quadratic phase. Full physical restriction closure of unbounded ordinary addressing contains every Boolean sign, so a conditional bound on that closure is FEI-strength.')
claim={'claim_id':'A034-QUADRATIC-AFFINE-ROW-CONDITIONAL','version':1,'exact_statement':statement,'hypotheses':['Independent uniform physical cubes X,Y','Actual Boolean sign','Pairwise distinct X labels, each of size <= integer d>=1','Each partial row is a unit quadratic sign supported on one affine Y partition cell','Entropy in bits; influence is squared Fourier mean degree'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account05/A034'],'proof_source':{'path':str(root/'CONDITIONAL_PHASE_THEOREM.tex'),'sha256':sha(root/'CONDITIONAL_PHASE_THEOREM.tex')},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Full physical restriction stability as a weaker-than-FEI completion for unbounded addressing'],'first_unproved_line':None,'next_consumers':['A003','A079','A088','A094','B07','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(root/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':root.name,'stream':'B07','packet_id':'A034','gap_id':'G-PHASE-COND','attempt_id':'A034-G-PHASE-COND-01','method':'Signed quadratic polar cancellation on affine physical rows; exact integer Walsh and rational energy checks; tensor and restriction admission proof','mathematical_delta':'Conditional residual completely paid at 2 I_Y on quadratic affine partition rows, stable under all Y restrictions; exact joint cost <=4 I_Y. Arbitrary fresh-Y tensor factors excluded unless quadratic. Full X restriction closure shown FEI-strength. A031 two v1 claims independently reconstructed at stated scope.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'RESTRICTED_THEOREM_AUTHOR_PROVED; UNIVERSAL_GAP_OPEN; INDEPENDENT_REVIEW_PENDING','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['CONDITIONAL_PHASE_THEOREM.tex','PHASE_SCOPE.md','REVIEW_A031.md','out/validation.json','out/source_receipts.json'],'next_consumers':claim['next_consumers'],'next_action':'Derive the exact entropy and Y-energy change when one X restriction merges two affine quadratic rows; retain the conditional residual and terminal debt. Reviewers A088 and A094.','stagnant_substantive_attempts':0,'blockers':['No universal payment for colliding X labels or nonquadratic rows','Independent review and supervisor mirror/adoption pending'],'packet_ids':['A034']}
expected_progress={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
save(root/'PROGRESS.json',progress);save(root/'PACKET_DELTA.json',progress)
val=json.loads((root/'out/validation.json').read_text())
report=f'''# A034 phase-energy transfer

## exact target, quantifiers, hypotheses and units
For actual Boolean signs on disjoint uniform physical cubes X,Y with integer X-degree bound d>=1, retain and pay H(S_Y|S_X) under a proved stable condition that excludes arbitrary fresh-Y Boolean tensor factors. Entropy is in bits. Result: quadratic affine partition rows with distinct X labels satisfy H(S_Y|S_X)=sum alpha(k+r)<=2 I_Y, H(S_X)=sum alpha k, and H(f)=sum alpha(2k+r)<=4 I_Y. This is a restricted theorem, not a full FEI proof. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators
EXECUTION_PROTOCOL.json was read in full, revision {protocol['revision']}. Campaign README, CURRENT_STATUS, registries, A034 packet and B07 next action, the board and B07 lead notes v1 (2026-10-11 22:40 UTC) were inspected. The plan's Boolean phase section, equations H(p_X)<=(2/ln2)I_Y+2(d-1) and entropy chain rule, and A034 acceptance tests identify the unpaid conditional term. Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source excerpts provide scope guards; ROUTE_MAP_CURATED and erasure/conditional/tensor excerpts were inspected, not adopted as theorem premises. Earlier B05, B09, B19 reports were read as context, with no unreviewed mathematical dependency. Threshold 38pp Section 8, Proposition 8.1 and Corollary 8.2 were read: the affine-cell character case is already baseline. This stage extends it to quadratic cell phases and exact conditional rank payment. Current percolation introduction and Theorems 3.1-3.2, both earlier-version introductions, and threshold entropy/selector locators were inspected; none is a proof premise. A031 REPORT, CLAIMS and full DERIVATION were read and analytically independently reconstructed in REVIEW_A031.md before the narrow new result. Local source hashes are in out/source_receipts.json; that inventory does not claim every page was mathematically reread. No novelty claim or web literature survey is made.

## complete derivation or exact first unsupported line
The complete proof is CONDITIONAL_PHASE_THEOREM.tex. On an affine physical cell a+V, the signed square-Walsh identity averages the quadratic polar character over v; it vanishes unless the difference w lies in the polar kernel. The remaining signed sum on that kernel is either its full size or zero. Hence the normalized row spectrum is uniform on an affine coset of dimension k+r. Its entropy is k+r, while every varying coordinate costs half a unit of expected spectral degree and there are at least k+r varying coordinates. Distinct X labels retain each row without coherent collision. The chain rule keeps the whole conditional entropy, rather than charging a marginal twice. Empty labels and zero influence are covered.

Restriction stability is exact for all Y coordinate restrictions, and for X restrictions that keep projected labels distinct. A fresh-Y tensor factor must be a quadratic phase by fixing one occupied physical row point. Conversely, full physical restriction closure of ordinary addressing recovers any Boolean truth table by setting the data bits to that table. Thus demanding all X restrictions creates an FEI-strength endpoint. The first unsupported universal inference is an influence payment after X labels collide or after nonquadratic row phases are admitted. No assertion of universal stability or unrestricted conditional payment is made.

The normalized non-Boolean control psi_N=N^(-1/2)sum_i y_i has conditional entropy log2 N but I_Y=1, violating the constant-two inequality for N>=5. Thus the statement cannot be inferred from normalization and marginal degree alone. The class excludes cubic tensor phases by their unique degree-three binary monomial. It allows quadratic tensor factors, whose entropy is explicitly paid.

## executed validation with domain, arithmetic, commands and outputs
Frozen specs v1 and v2 preceded their executions. v2 strengthened restricted-row Fourier validation after finding that the initial third-difference checks alone were too weak; the domain stayed fixed. Final command: python -X utf8 runs/{root.name}/code/check.py. It passed {val['assertions']:,} exact assertions in {val['runtime_seconds']:.3f} seconds: 37,743 affine row cases through four Y bits (all quadratic and linear parts through three bits; seven fixed homogeneous quadratic parts at four bits), 2,778 full Boolean cases from all 926 affine partitions through three bits and three phase profiles, 54,024 nonempty one-Y-coordinate restricted rows, and 256 three-bit addressing restriction witnesses. Integer Walsh transforms and Fraction arithmetic verify flatness, affine spectral support, exact dyadic entropy, physical-edge energy, joint chain rule and the two inequalities. No floating logarithmic comparison is used. Memory estimate 50 MB, pilot cap 55 seconds, no heavy job, GPU, dimension escalation, or memok-triggering estimate. v1 output is preserved as out/validation_v1.json. All-dimensional statements rest on the analytic proof, not extrapolation of the finite domain.

## proof dependencies and changed downstream conclusions
No campaign theorem version is a proof premise; the proof is self-contained finite Fourier algebra, quadratic polar cancellation, elementary binary linear algebra and the entropy chain rule. Corollary 8.2 is a recovered special case and novelty boundary. One bundled restricted theorem awaits A088/A094 review. REVIEW_A031.md records independent acceptance at stated scope for A031-SIGNED-ENTROPY-ANCHOR v1 and A031-ANCHOR-POSITIVE-PAYMENT-NOGO v1; no repair or registry change was made. Their calibration is generic as the lead correctly observed. Consumers A003/A079 may use this conditional interface only under the explicit row admission. They may not claim all-restriction heredity, bounded-law-count admission, or general conditional completion.

## one next mathematical action and independent reviewer
Derive the exact conditional entropy and Y-energy ledger when a single X coordinate restriction merges two quadratic affine rows, preserving the terminal residual. A088 should reconstruct the quadratic-kernel proof and fresh-factor guard; A094 should audit the full-restriction closure obstruction. No messages were sent. These are source-bound handoffs for supervisor ingestion.

## actual persistence receipts or precise save blocker
REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved with exactly the protocol's specified claim/progress field sets. Proof, scope, prior-claim review, frozen specs, code and validation outputs are saved locally, with source and artifact SHA256 receipts under out/. STATUS.md, WORKLOG.md and LEARNED.md are current. Local save blocker: none. Supervisor copy, GitHub mirroring, Brain ingestion, independent acceptance of the new theorem, downstream adoption and publication are not claimed. All writes stayed inside A034; no git, external messaging, live Brain writes or other-agent edits occurred.

Universal bridge: This stage moves the B07 lead's G-PHASE-COND bridge by paying the full conditional residual at sharp constant 2 for quadratic affine physical rows, with exact joint constant 4 and a proved fresh-tensor guard. Universal FEI still lacks admission of arbitrary rows and payment through colliding labels; full physical restriction closure is proved FEI-strength. The next two-row collision ledger is the shortest structural step toward a universal restriction payment because it examines the precise point where proved Y-stability fails under X restriction, while retaining terminal entropy, rather than adding another isolated selector calibration.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A034 local restricted theorem complete: quadratic affine rows pay full conditional entropy <=2 I_Y and joint H<=4 I_Y; 729799 exact assertions PASS; review pending; full FEI OPEN.\nNEXT: A088/A094 review; derive exact two-row collision ledger after one X restriction, retaining conditional residual and terminal cost.\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} A034 stage: read protocol/board/lead and affine-selector baseline; independently reconstructed A031 two v1 claims. Extended affine cell signs to quadratic phases using polar-kernel cancellation. Proved full conditional payment, Y restriction stability, quadratic-only fresh tensor admission and all-X-heredity FEI-strength obstruction. Frozen exact pilot v1 passed; v2 strengthened restricted-row checks, {val["assertions"]} assertions PASS in {val["runtime_seconds"]:.3f}s. Saved all artifacts; full FEI OPEN.\n')
(agent/'LEARNED.md').write_text('''# Durable mathematical facts

For distinct X character labels S_j and affine physical Y partition cells A_j, with quadratic signs on each cell, put alpha_j=2^-k_j and r_j=polar rank on its direction space. Then H(S_X)=sum alpha k; H(S_Y|S_X)=sum alpha(k+r)<=2I_Y; H=sum alpha(2k+r)<=4I_Y. The normalized row spectrum is uniform on an affine coset of dimension k+r. Every varying spectral coordinate is fair and costs 1/2, so correlation does not invalidate the payment. The linear-phase special case was already in threshold paper Corollary 8.2; novelty not claimed.

This admission is closed under all Y coordinate restrictions and X restrictions preserving distinct projected labels. Every fresh-Y Boolean tensor factor of an admitted function must be a quadratic phase, by fixing a physical point in a nonzero row. It does not admit arbitrary Boolean factors. Demanding all X restrictions is FEI-strength: ordinary addressing restricted at its data bits gives any Boolean truth table.

Bounded count of conditional laws and laws of Boolean restrictions alone do not exclude h(X)g(Y). Low X degree does not pay H(g). Normalized psi_N=sum y_i/sqrt N has H=log2 N and I=1; it refutes the constant-two conditional bound outside Boolean quadratic admission.

A031 signed anchor identity and its two positive-cost no-gos were independently reconstructed analytically in REVIEW_A031.md. Their point-defect calibration alone is generic: pmax(H-Hinf)^2<=(1-pmax)Var(ell) is a probability inequality. Preserve the lead's objection. No shared review/adoption mutation is implied.

The next universal obstruction is coherent row collision under an X restriction, with conditional entropy and terminal cost retained. Finite passes prove only their frozen domain; the all-dimensional restricted theorem rests on its signed polar-kernel derivation.
''',encoding='utf-8')
receipts=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='artifact_receipts.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(root/'out/artifact_receipts.json',receipts)
print(json.dumps({'saved_files':len(receipts),'claim_fields_exact':True,'progress_fields_exact':True,'packet_delta_identical':(root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes(),'validation_assertions':val['assertions'],'local_only':True},indent=2))
