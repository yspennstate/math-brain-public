"""Persist exact stage19 claim/progress and verify actual local receipts."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];ROOT=HOME.parents[1]
P=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def rd(p):return Path(p).read_text(encoding='utf-8')
def wr(p,s):Path(p).write_text(s,encoding='utf-8',newline='\n')
def obj(p):return json.loads(rd(p))
def dump(p,x):wr(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
protocol=obj(P);field=obj(R/'out/FIELD.json');direct=obj(R/'out/DIRECT.json');witness=obj(R/'out/U_WITNESS.json')
assert field['status']==direct['status']==witness['status']=='PASS'
assert field['counts']=={'prefix_nodes':366,'prefix_queries':182,'pivot_queries':366,'reset_children':732,'post_reset_queries':3724}
assert direct['counts']=={'entries':96,'pivot_cuts':1248,'reset_children':2496,'post_reset_queries':3648}
assert field['exact_assertions']+direct['direct_assertions']==410709
for row in witness['records']:assert row['r_v']==['15/34','19/34']
assert direct['non_affine_negative_control']['expected_reset_KL']['exact']=={'2':'1','3':'-9/16'}

cid='A061-AFFINE-PHASE-PIVOT-RESET-OLD-CAP'
statement=('For every finite uniform Boolean source F(v,z,y)=(-1)^(v A(z,y))g(y), with affine parity A, '
 'arbitrary Boolean core g and ANY normalized source-supporting inherited reference Q, K+2M(g) plus accumulated actual outcome KL '
 'is a supermartingale along every adaptive interleaving of ordinary y and mask z queries while v remains protected. '
 'Before v an inherited-reference stop is admitted. After querying v, each child may independently keep its reference or make ONE actual intermediate product reset, '
 'then take any physical adaptive continuation with inherited stops or one final product conversion-and-stop. Full terminal H+KL is retained. '
 'No lifted-reference, zero pivot outcome KL or zero erasure hypothesis is needed. The reset drop is K_child+H(g)>=0. '
 'For every l>=2 in the original field selector fixture, one expected reserve M_h is enough, so the already booked cap W=3l+2<5Sbar/7 still pays with ZERO extra owner allocation; '
 'after old unrelated omega<=Sbar/4 more than Sbar/28 remains in the SAME supplied original owner. '
 'Dropping affinity is false: F=(-1)^(v*y0*y1*y2), g=1 and Q=p_F has zero entry K+2Mcore but expected post-v product KL 1-(9/16)log2(3)>0.')
hyp=[
 'Uniform finite physical cube; bits for entropy/KL; predictable coordinate choices, fair physical outcomes, bounded stopping; no coordinate queried twice.',
 'Q normalized and positive wherever actual p_F is positive. Every physical query uses the actual coherent kernel, extended fairly on source-zero rows, and its actual normalized reference transport.',
 'The displayed phase is affine in all mask/core variables. Before protected v only ordinary and mask coordinates may be queried. Stops there retain inherited KL; no pre-v product conversion is paid.',
 'At v children are core g times a character, hence each actual full H=H(g), M_full=M(g). An optional immediate intermediate reset may occur separately in each child, followed by arbitrary continuation and at most a final terminal conversion. No second intermediate reset.',
 'Field owner conclusion only for the explicit GF(2^l) bilinear fixture, l>=2, original uniform root reference and fixed initial selector. SAME original expected Sbar and omega<=Sbar/4 are supplied, not created by this theorem.',
 'Previous theta must be a nested pending booking of this SAME policy/reference class; add W-theta once. Old unrelated consumed charges stay spent. The branch allocation is expected-root, not a uniform per-child cap.',
 'No union with arbitrary pre-v product-stop policies is claimed. No universal2M<=CI, non-affine phase payment or fresh-pivot availability is inferred.'
]
claims=[dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A061/fleet03; A065/A087 predecessor envelope mechanisms credited'],
 proof_source={'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':[str(R/'out'/n) for n in ['FIELD.json','DIRECT.json','U_WITNESS.json']]},
 proof_dependencies=[
 {'claim':'A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION@1','scope':'Field fixture and original owner; previously independently reconstructed by A064/A087; critical actual GF4 source rechecked here.'},
 {'claim':'A065-ADAPTIVE-ORDINARY-PREFIX-INTERMEDIATE-RESET-OLD-CAP@1','scope':'Earlier booked W and policy class; new generic proof reconstructs the KL/M ingredients and extends only the stated prefix class. Predecessor author/exact checked, independent review pending.'}],
 review_records=[{'reviewer':'A061','verdict':'AUTHOR_CHECKED_NOT_INDEPENDENT_ACCEPTANCE','scope':'Direct character sums and non-lifted reference implementation independent from field FWHT oracle;410709 primary checks; generic analytic proof and negative control.'}],
 status='AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW',supersedes=[],
 refutes=['UNREGISTERED-CANDIDATE: the same K+2Mcore affine-pivot reset theorem holds with arbitrary non-affine phase A'],
 first_unproved_line=None,next_consumers=['A064','A065','A087','A094','B20'])]
assert set(claims[0])==set(protocol['required_per_run']['claim_fields']);dump(R/'CLAIMS.json',claims)

progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B13',packet_id='A061',gap_id='G-R-MISMATCH',
 attempt_id='A061-stage19-affine-pivot-arbitrary-reference',method='Core marginal entropy concavity plus full actual KL chain; protected affine phase pivot; exact actual-source replay and non-affine Boolean negative control.',
 mathematical_delta='Closed u-before-v AND arbitrary u/ordinary interleavings before one intermediate reset at SAME old W, with arbitrary supporting inherited references and nonzero pivot O. No extra owner booking if W already pending; explicit4-bit counterexample to dropping affine phase.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACTS',mathematical_status='SCOPED_ALL_DIMENSIONAL_CONDITIONAL_THEOREM_PROVED; NEW_REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=['A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION@1','A061-ORIGINAL-MARGINAL-ENVELOPE-ALL-HISTORIES@1','A065-ADAPTIVE-ORDINARY-PREFIX-INTERMEDIATE-RESET-OLD-CAP@1'],
 claims_created_or_changed=[cid+'@1'],source_artifacts=[str(R/x) for x in ['PROOF.md','FROZEN_SPEC.json','DIRECT_SPEC.json','WITNESS_SPEC.json','out/FIELD.json','out/DIRECT.json','out/U_WITNESS.json']],
 next_consumers=['A064','A065','A087','A094','B20'],
 next_action='Pay the non-affine residual phase contribution at a genuinely mixed pivot from the SAME unused original owner, retaining old debits and both full terminals; use the explicit4-bit failed extension as a guard. A087/A094 independently review the new affine-pivot theorem.',
 stagnant_substantive_attempts=0,blockers=[
 'Universal non-affine phase liability and unused influence-scale original-owner supply remain unproved; full FEI OPEN.',
 'New claim independent review pending. Earlier A061 all-history claim has A087 independent HOLDS at its stated scope.',
 'Formal compiler not admitted: memok exit1 physical1.8GB/commit10.3GB free; no formal certificate.',
 'Archive-to-main check returned404 Branch not found; no git or remote mutation. Supervisor archive/mirror/downstream-use receipts pending.',
 'Brain self-care degraded/unverified: stale personal notes and failed attachment integrity/renderer; affected notes not used as mathematical premises.'],packet_ids=['A061'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
dump(R/'out/ARCHIVE_RECEIPT.json',{'status':'BLOCKED_REQUESTED_BRANCH_ABSENT','repository':'yspennstate/math-open-problems','requested_branch':'main','readback':'Fresh GitHub GET branches/main returned404 Branch not found','remote_mutation':False,'git_executed':False,'commit':None,'next':'Supervisor established archive copy; no new branch created.'})
sources=[P,ROOT/'BOARD.md',ROOT/'claude/B13/STREAM_NOTES.md',
 ROOT/'agents/A064/runs/20261023T034109Z-fleet03-A064-global-debt-potential/PROOF.md',
 ROOT/'agents/A064/runs/20261023T034109Z-fleet03-A064-global-debt-potential/CLAIMS.json',
 ROOT/'agents/A065/runs/20261023T043836Z-fleet03-A065-stopping-rule-falsifier/PROOF.md',
 ROOT/'agents/A065/runs/20261023T043836Z-fleet03-A065-stopping-rule-falsifier/CLAIMS.json',
 ROOT/'agents/A087/runs/20261023T020220Z-fleet03-A087-restriction-referee/CLAIMS.json',
 HOME/'runs/20261023T002802Z-fleet03-A061-entropy-process/PROOF.md',
 HOME/'runs/20261023T002802Z-fleet03-A061-entropy-process/code/check.py']
dump(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
dump(R/'out/ADVERSARIAL_REVIEW.json',{
 'status':'AUTHOR_RECONSTRUCTION_NOT_EXTERNAL_ACCEPTANCE',
 'strongest_failure_case':'Mcore omits phase/mask entropy; a hidden non-affine phase could make pivot children non-character functions, invalidating H/M equality.',
 'check':'Direct negative arm actually fails the phase-free extension:4-bit Boolean point source, exact Q=p_F, zero initial K/Mcore, positive expected reset KL. Affinity is explicitly retained.',
 'other_checks':['Core influence is not full carrier influence; physical core-edge averaging alone is used before v.',
 'Full actual inherited Q is transported in order; no source-only reference cache or lifted-reference replacement.',
 'Explicit after-u non-lifted witness r=(15/34,19/34) exercises positive pivot O; zero-O shortcut would fail.',
 'Pre-reset cut retains BOTH actual KLs; signed reset drop exactlyK_child+Hcore.',
 'Endpoint influences0/1 and constant/parity/defect cores included; deterministic mask spectral coordinates retained.',
 'ONE original2Mcore allocation, expected-root field cap and old quarter maintained; no bank renewal or incomparable policy union.',
 'All-l and arbitrary-depth result analytic; finite enumeration not extrapolated.'],
 'source_reconstruction':'A065 predecessor argument HOLDS at its stated ordinary-prefix scope by the new proof restricted to no u reveal; author supplied predecessor mechanism, so not a new independent full-chain acceptance.'})

report=f'''# A061 stage19: other-carrier exposure before reset, without reference symmetry

## exact target, quantifiers, hypotheses and units

Close A065's explicitly unpaid u-before-v boundary using the SAME original expected owner and actual inherited references. PROOF.md proves a general all-dimensional theorem for F(v,z,y)=(-1)^(v A(z,y))g(y), affine A, arbitrary Boolean g and ANY normalized source-supporting Q. Before protected v, admit arbitrary adaptive interleavings of mask z and ordinary y queries, including ordinary queries after u. Stops there retain inherited KL. At v, each child may keep its reference or actually reset once, then continue under any physical rule with inherited or final-product stops. Full terminal H+KL is retained. Units bits; finite fair physical filtration. No pre-v product stop or second intermediate reset is paid. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

BOARD dated2026-10-23 05:15UTC; B13 lead v2; own STATUS and prior stage18 proof/helper; execution protocol2026-10-11-execution-v2. A087 20261023T020220Z CLAIMS records independent HOLDS for A061 stage18 and A065's interposed cut. A064 20261023T034109Z PROOF/CLAIMS pays immediate reset/continuation but leaves an earlier-prefix guard. A065 20261023T043836Z PROOF/CLAIMS pays ALL ordinary prefixes and names u-before-v as next unpaid. These were consumed rather than repeated. A065 §§1–4 supplies the predecessor reference envelope/old cap, reconstructed here without assuming lift symmetry. All source hashes are in out/SOURCE_RECEIPTS.json. No new external-paper theorem is used; original campaign/paper intake remains inherited. Current owner deadline governs the older protocol clock.

## complete derivation or exact first unsupported line

Use actual full K=KL(p_F||Q), but Mcore=sum h2(Inf_j(g)). An ordinary query has DeltaMcore>=0 by physical core-edge averaging; a mask query has DeltaMcore=0. The exact physical KL chain gives K-parent minus mean K-child=E+O. Thus P=K+2Mcore has drift E+O+2DeltaMcore>=O throughout arbitrary pre-v interleavings. No special reference law survives or is needed. At v both actual child functions are character multiples of g, so their FULL entropy and marginal entropy are Hcore,Mcore. Keeping K_child+2Mcore at the pre-reset boundary pays the v step by its actual E+O. Actual reset plus continuation has potential TCcore+Mcore=2Mcore-Hcore, with EXACT drop K_child+Hcore>=0. Afterwards K+M_full pays all physical continuations and full inherited/product terminal KL; full H stays explicit. PROOF.md gives filtration and all one-step increments.

For the all-l field fixture the expected initial core reserve is M_h, since selector G/H receive0 and2M_h with fair weights. M_h<=6<8 at l2 and M_h<39l/16<3l+2 for l>=3. Hence the SAME old W=3l+2 already covers every new u/ordinary interleaving; additional owner allocation is0 if W is already pending. Include nested theta once, top up W-theta only; consumed unrelated omega remains spent. With omega<=Sbar/4 and unchanged W<5Sbar/7, the SAME original balance remains>Sbar/28. The older13/48 reserve was for final conversion only; the present5/7 cap is A065's unchanged, broader intermediate-reset allocation, not a revised numerical estimate of that earlier theorem.

The stronger reference scope is real: g=1, phase v(u+y0), ambient Q(s)=(s+1)/136. For EITHER u outcome, subsequent v predicts(15/34,19/34), with O_v=-(1/2)log2(285/289)>0. The proof pays this actual O; the old lifted guard O_v=0 would fail.

An unregistered extension dropping affinity is FALSE on actual Boolean F=(-1)^(v*y0*y1*y2), core g=1, Q=p_F. Initial K=Mcore=0, but after v then product reset the expected KL is1-(9/16)log2(3)>0, certified by2^16>3^9. The first false line is that arbitrary phases only translate core spectra; the non-affine child creates entropy and marginal entropy. This refutes that proposed reserve extension, NOT FEI. No unsupported line remains inside the stated affine theorem. The next unpaid universal line is influence-priced NON-AFFINE phase liability, or a paid selection rule producing an eligible affine pivot and unused original owner.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json, DIRECT_SPEC.json and WITNESS_SPEC.json precede their runs. All commands use python -X utf8 from this run directory. Integer/rational arithmetic and certified outward logarithm bounds decide every sign; floating time measurements do not certify mathematics. No dimension escalation, GPU, detached job, or computation over300MB was started.

- `python -X utf8 code/audit.py pilot`: PASS,{obj(R/'out/PILOT.json')['exact_assertions']} assertions,6 prefix histories/12 reset children/76 post-reset queries, {obj(R/'out/PILOT.json')['seconds']:.3f}s. First pilot reached final save with the output directory missing; fixed the directory creation and repeated the bounded pilot. The first save exception is preserved in out/DEVELOPMENT_LOG.json; no mathematical failure was suppressed.
- `python -X utf8 code/audit.py`: out/FIELD.json PASS,{field['exact_assertions']} assertions,{field['seconds']:.3f}s. Actual9-bit GF4 selector,366 ordered prefix histories,182 pre-v queries,366 v queries,732 actual reset children,3724 post-reset queries. EVERY length0–2 ordered prefix from u and six ordinary directions, all outcomes; no order/reference quotient. Full integer FWHT versus physical-edge counts; Fraction normalized actual references, exact prime-log chains and96-bit outward32-term atanh signs.
- `python -X utf8 code/direct.py`: out/DIRECT.json PASS,{direct['direct_assertions']} direct assertions,{direct['seconds']:.3f}s.96 source/reference entries, six selected2-bit cores, ALL affine L,c, uniform/non-lifted ascending references, BOTH u/data orders and all outcomes:1248 pivot cuts,2496 actual reset children,3648 continuation queries. Separate direct character sums, physical edges, transport and product construction. Scalar interval helper shared/pinned; not an external independent review. Includes the genuine non-affine negative control.
- `python -X utf8 code/witness.py`: out/U_WITNESS.json PASS,{witness['overlapping_extracted_assertions']} extracted overlapping assertions,{witness['seconds']:.3f}s, exact after-u prediction(15/34,19/34). This replays an already covered case to expose its numerical reference prediction.

Primary exact total410709 =264525 field +146184 direct. Pilot13789, direct auxiliary scalar86880 and extracted77 checks are excluded to avoid overlap inflation. All-n/all-depth theorem comes from the analytic proof, not enumeration. Fresh memok exit1: free physical1.8GB (required4.0), commit10.3GB. Proposed512MB scalar formal check NOT_ADMITTED; compiler never started; no Lean theorem/axiom verdict claimed. Lightweight jobs were estimated120MB and65MB. Nothing else was killed or shed. Brain self-care is degraded/unverified: owner-model91.3h/state-of-mind75.9h stale, attached document integrity failure and wake-render exception; affected personal/context notes were not proof premises.

## proof dependencies and changed downstream conclusions

New claim {cid}@1 is author proved/exactly checked, awaiting independent review. The field fixture depends on A061-PRODUCT-REFERENCE-LOCAL-PRICE-OBSTRUCTION@1; A065-ADAPTIVE-ORDINARY-PREFIX-INTERMEDIATE-RESET-OLD-CAP@1 supplies the existing old pending cap and is reconstructed at scope. A087's acceptance of prior A061 stage18 is recorded, not misrepresented as review of this new theorem. Source statement hashes here are raw UTF-8 exact_statement hashes, avoiding the earlier combined-object hash convention noted by A087. No predecessor source tree was edited. A065's u-before-v target is closed, including arbitrary further ordinary interleavings, with arbitrary reference support and no extra old-owner debit. The affine phase cannot simply be removed; the actual Boolean control exposes that next barrier. Local named consumers are A064/A065/A087/A094/B20; handoff files are not downstream-use receipts.

## one next mathematical action and independent reviewer

Pay the residual NON-AFFINE phase contribution at one genuinely mixed pivot using the SAME unused original influence-scale owner, with old debits and both full terminals retained. Use the explicit zero-core-reserve4-bit control as the mandatory guard; adding another u/ordinary depth in the solved affine fixture cannot resolve it. A087/A094 should independently reconstruct the new arbitrary-reference phase-pivot theorem and original-cap splice; A065 can consume the closed target but predecessor contribution is not an independent full-chain acceptance.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved with proof, frozen specs, code and exact outputs; two-line STATUS and dated WORKLOG/LEARNED updated. out/PERSISTENCE_RECEIPTS.json records actual SHA256 hashes and sizes, reread and checked by code/finalize.py together with protocol fieldsets and statement hash. No local save blocker. Fresh archive GET branches/main returned404 Branch not found; no git, new branch or remote mutation. Supervisor archive/mirror, independent acceptance and downstream mathematical use remain pending and are not claimed.

**Universal bridge:** C019 stopping-tree payment and C024 history transfer advance by removing BOTH the u-before-v eligibility boundary and the lifted-reference/zero-outcome-KL assumption for all adaptive affine-phase prefixes. The SAME old W=3l+2 still leaves>Sbar/28 after the old quarter, with zero new owner allocation if already booked. The actual4-bit non-affine control locates the universal obstruction at newly created phase entropy/marginal entropy, rather than at reference symmetry. NEXT prices that missing phase contribution against a real original influence owner, the shortest remaining step toward a universal paid process rather than another isolated affine-class calculation.
'''
wr(R/'REPORT.md',report)
wr(HOME/'STATUS.md',
 'STATE: A061 stage19 complete: ANY u/ordinary interleaving before affine v-reset paid SAME old W, arbitrary Q/nonzero O allowed;410709 primary exact assertions PASS; new review pending; FEI OPEN.\n'
 'NEXT: A087/A094 review A061-AFFINE-PHASE-PIVOT-RESET-OLD-CAP@1 at runs/20261023T051706Z-fleet03-A061-entropy-process; pay NON-AFFINE phase liability from SAME unused owner;4-bit failed extension is the guard.\n')
entry='\n2026-10-23 stage19 (20261023T051706Z): consumed A087 acceptance of stage18, A064 intermediate-reset proof and A065 ordinary-prefix extension. Closed arbitrary u/ordinary interleavings before one affine-pivot reset, ANY supporting actual Q, with K+2Mcore; exact reset drop Kchild+Hcore and arbitrary later physical continuation. SAME old W=3l+2, old quarter/full terminals, spare>Sbar/28; zero extra if booked.410709 primary exact assertions (264525 field+146184 direct),13789 pilot/86880 auxiliary/77 extracted excluded. Non-lift after-u prediction15/34,19/34 proves nonzero pivot O. Actual4-bit non-affine control has positive expected reset KL1-(9/16)log3 from zero core bank, refuting phase-free extension only. First pilot save-directory error repaired/replayed; memok exit1 blocked formal compiler; archive main404, no remote mutation. New review/full FEI open.\n'
if entry.strip() not in rd(HOME/'WORKLOG.md'):wr(HOME/'WORKLOG.md',rd(HOME/'WORKLOG.md')+entry)
learned='''
Stage19 durable fact (2026-10-23): For F=(-1)^(v A(z,y))g(y), AFFINE A, ANY source-supporting actual Q, and v unqueried, K+2Mcore has drift E+O+2DeltaMcore>=O under arbitrary mask/core interleavings. Mask queries leave core M unchanged. At v both children are characters times g, FULL M=Mcore,H=Hcore. Pre-reset Kchild+2Mcore falls to actual TCcore+Mcore by exactlyKchild+Hcore>=0; then generic K+M_full pays all physical continuations/final product stop. No lift/Ov=0 hypothesis, no per-descendant renewal. All-l field expected reserveMh fits SAME oldW=3l+2<5Sbar/7; after old quarter spare>Sbar/28. Before-v stops keep inherited KL; arbitrary product stops there and second intermediate resets are excluded. Concrete non-lift Q(s)=(s+1)/136 for phase v(u+y0): after EITHER u outcome, v predicts15/34,19/34, Ov=-(1/2)log(285/289)>0. Dropping AFFINITY is FALSE: F=(-1)^(v*y0*y1*y2), g=1,Q=p_F has entryK=Mcore=0 but expected reset KL1-(9/16)log3>0 (2^16>3^9). This is a reference-reserve obstruction, not FEI disproof.410709 primary checks; analytic all-depth/all-l proof; independent new review pending. Next pay non-affine phase liability from real original influence owner, not deeper affine prefixes.
'''
if learned.strip() not in rd(HOME/'LEARNED.md'):wr(HOME/'LEARNED.md',rd(HOME/'LEARNED.md')+learned)
assert obj(R/'PROGRESS.json')==obj(R/'PACKET_DELTA.json')
assert len(rd(HOME/'STATUS.md').splitlines())==2
assert claims[0]['statement_sha256']==hashlib.sha256(obj(R/'CLAIMS.json')[0]['exact_statement'].encode('utf-8')).hexdigest()
assert claims[0]['proof_source']['sha256']==sha(R/'PROOF.md')
for heading in protocol['required_per_run']['report_fields']:assert '\n## '+heading+'\n' in rd(R/'REPORT.md')
assert rd(R/'REPORT.md').rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000;receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=HOME/name;receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'LOCAL_SAVED_HASH_READBACK_PASS','files':receipts,'scope':'Local persistence only; not mirror/publication or downstream-use receipt.'})
for row in obj(R/'out/PERSISTENCE_RECEIPTS.json')['files']:assert sha(row['path'])==row['sha256']
print(json.dumps({'status':'PASS','receipt_files':len(receipts),'protocol_fieldsets':'PASS','statement_hash':'PASS','exact_primary_assertions':410709,'full_fei':'OPEN','new_independent_review':'PENDING','formal':'NOT_ADMITTED','remote':'NO_MUTATION'}))
