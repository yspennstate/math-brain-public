"""Persist A065 protocol deliverables and verify their exact local schemas."""
from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
B=A.parents[1]
P=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8'))
def read(p): return p.read_text(encoding='utf-8-sig')
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
main=json.loads(read(R/'out/EXACT.json')); amp=json.loads(read(R/'out/AMPLIFICATION.json'))
assert main['status']==amp['status']=='PASS'
assert main['assertions']==17590 and main['parameter_triples']==162
assert (R/'REVISED_SPEC.json').is_file()
lean_receipts=list((R/'out/lean').glob('*/RECEIPT.json')) if (R/'out/lean').exists() else []
# Wrapper receipt names may vary; index actual files without pretending success.
lean_files=list((R/'out/lean').glob('*/*')) if (R/'out/lean').exists() else []
lean_text='\n'.join(read(p) for p in lean_files if p.suffix in ['.json','.txt'])
lean_result=json.loads(read(R/'out/LEAN_RESULT.json'))
lean_pass=lean_result.get('status')=='VERIFIED_TARGET' and lean_result.get('formal_target_verified') is True
formal=('Lean VERIFIED_TARGET for constant_branch_forces_constant, core Bool XOR lemma only; full entropy/adaptive theorem is an analytic proof with exact checks.' if lean_pass else 'Core Lean attempt RUNTIME_UNVERIFIED after47.633s timeout with no compiler verdict; source/compiler hashes in out/LEAN_RESULT.json. Full theorem is an analytic proof with exact checks, not Lean-certified.')

src87=B/'agents/A087/runs/20261023T143823Z-account03-A087-restriction-referee'
src61=B/'agents/A061/runs/20261023T135818Z-account03-A061-entropy-process'
source_paths=[P,B/'BOARD.md',B/'claude/B13/STREAM_NOTES.md',src87/'PROOF.md',src87/'REPORT.md',src87/'CLAIMS.json',src61/'PROOF.md',src61/'REPORT.md',A/'runs/20261023T133350Z-account03-A065-stopping-rule-falsifier/PROOF.md']
sources=[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in source_paths]
save(R/'out/SOURCE_RECEIPTS.json',sources)
sourceclaims=json.loads(read(src87/'CLAIMS.json'))
save(R/'out/SOURCE_CLAIMS_READ.json',sourceclaims)
review={'source':str(src87/'PROOF.md'),'source_sha256':digest(src87/'PROOF.md'),
        'scope':'Section4 FULL H+KL=M(g), any incoming supporting reference, immediate pivot and BOTH actual product stops; quantitative m(m-1)/(m+1) bound.',
        'verdict':'HOLDS_WITHOUT_REPAIR','reconstruction':'PROOF sections3--5 reconstruct terminal identity and strictly generalize it via activation and bounded adaptive exposure.',
        'excluded':'No new independent full-chain acceptance of hereditary GU or old A065-owned history results. No source or shared registry changed.',
        'external_review_of_new_work':'PENDING A087/A094'}
save(R/'out/REVIEW.json',review)
statement=('For every integers m>=2,t>=1,L>=1,0<=k<=m-1, let d=2^(1-m), N=L/d, g be the product of N disjoint point_m signs, and F=1+A_t(g-1) with A_t a fresh all-zero point activation and delta=2^(-t). F has full Fourier support and admits no physical disjoint tensor factorization into two nonconstant signs. For every finite adaptive fair physical rule revealing controls first and then at most k coordinates per original point block, installing actual coordinate-marginal product references at ALL terminals, every original account paying full terminal H+KL and nonnegative actual outcome losses without outside infusion must have Capital>=delta*N*2^(-k)*(m-k)*h2(2^k*d)>=delta*L*(m-k)*(m-k-1), independently of its supporting initial reference. I(F)=delta*(Lm+t*(1-(1-d)^N)) and H(F)<=(4+6/(Lm))*I(F)<=7I(F). The first lower bound is sharp among the prescribed rules. For even m>8C+2,t=m,k=m/2, required terminal cost minus C*I(F) tends to infinity with L. No affine indecomposability, generic extra-reserve lower bound, universal stopping-rule failure, or FEI counterfamily is asserted.')
cid='A065-RARE-ACTIVATION-PHYSICAL-PRIME-SHALLOW-RESET-OBSTRUCTION'
claim={'claim_id':cid,'version':1,'exact_statement':statement,
       'hypotheses':['Uniform physical cube; Boolean signs; base2 units','Integers m>=2,t>=1,L>=1,0<=k<=m-1','Finite adaptive fair rule; controls first; distinct physical core reveals bounded by k per original block','ALL final references actually replaced by actual coordinate-marginal products; FULL terminal H+KL is funded','Capital means TOTAL original funding including any initially booked source H/K; no renewed/external owner','Initial reference normalized and source-supporting; full source-zero reference rows allowed','Physical tensor primeness only, not affine primeness'],
       'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
       'contributors':['A065; A061/A087 credited for original product-terminal obstruction'],
       'proof_source':{'path':str(R/'PROOF.md'),'sha256':digest(R/'PROOF.md'),'locators':'sections1--9'},
       'proof_dependencies':[],
       'review_records':[{'reviewer':'A065 author self-audit','verdict':'EXACT_CHECKS_PASS_ANALYTIC_PROOF','evidence':['out/EXACT.json','out/AMPLIFICATION.json','out/DEVELOPMENT_LOG.json'],'formal_scope':formal}],
       'status':'PROOF_AUTHOR_CHECKED_EXTERNAL_REVIEW_PENDING','supersedes':[],'refutes':['Cheap TOTAL original capital for every shallow actual-product terminal rule on every physically tensor-prime full-support Boolean source'],
       'first_unproved_line':'None in the scoped analytic result. Universal source funding, affine-prime strengthening, and selected deeper/nonproduct policies remain open.',
       'next_consumers':['A061','A062','A064','A087','A094','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(R/'CLAIMS.json',[claim])
next_action=('A087/A094 independently review the activated all-adaptive shallow-cut lower bound and total-capital scope. Test an explicitly selected nonproduct or sufficiently deep terminal policy for an arbitrary core, retaining full H+KL and signed E/O; fund it from SAME unused original influence. Do not infer affine primeness or claim a universal reference supplier.')
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B13','packet_id':'A065','gap_id':'C019-SELECTED-RULE-ORIGINAL-CAPITAL','attempt_id':'A065-stage21-rare-prime-shallow-terminal-falsifier',
          'method':'Consume A087 full-terminal objection; analytic activation/physical-prime embedding plus harmonic all-adaptive exposure barrier, exact Boolean Walsh/edge and outward-log audit',
          'mathematical_delta':'A087 immediate full-terminal corollary locally reconstructs without repair. New rare-activated full-support physical-tensor-prime source defeats EVERY bounded-per-block-depth product-terminal rule: Capital/I>=(m-k)(m-k-1)/(m+t) at L1; shared-gate L amplification makes expected unpaid cost unbounded while H/I<=7. Full FEI OPEN.',
          'deliverable_status':'COMPLETE_LOCAL_SAVED_READBACK_VERIFIED','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_CHECKED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
          'claim_versions_used':[{'source':str(src87/'PROOF.md'),'version':'20261023T143823Z section4'}],
          'claims_created_or_changed':[{'claim_id':cid,'version':1,'change':'new scoped quantitative obstruction'}],
          'source_artifacts':sources,'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
          'blockers':['No universal influence-priced ORIGINAL arbitrary-core owner or sufficient selected terminal policy.','Physical tensor primeness does not establish affine indecomposability.','External review, supervisor archive/mirror and downstream use unverified.'],
          'packet_ids':['A065']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress); (R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())

report=f'''# A065 stage21: rare activation leaves shallow product stopping unpaid

## exact target, quantifiers, hypotheses and units

Test cheap ORIGINAL TOTAL funding for every shallow actual-product terminal rule on arbitrary cores. PROOF sections1--9 give all integer m>=2,t>=1,L>=1 and 0<=k<=m-1, every finite fair adaptive policy of the declared control-first/per-block-depth class, any supporting original reference, and FULL H+KL at both terminals. Units bits. The roots are physically tensor prime with full Fourier support; affine primeness is not asserted. Capital includes initially booked H/K, so this is not an automatic extra-reserve lower bound. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2 read completely; board and B13v2 at stage start; own STATUS/LEARNED/WORKLOG and stage20; A08720261023T143823Z PROOF sections1--6 and A06120261023T135818Z PROOF sections1--5. New dependency is A087 section4 full-terminal refinement; local verdict HOLDS without repair (out/REVIEW.json). Base README/status/claim-obstruction-packet registries/stream actions/plan and 100-agent supplement were consulted for dispatch. Four supplied paper abstracts and restriction/composition locators were read as context only; their text exports are cp1252, not UTF8. No paper theorem is an unpaid premise. Exact relied-on source hashes/byte sizes are in out/SOURCE_RECEIPTS.json. One read-only multiwording math recall returned no proof of the new bound; no brain write. Current explicit resumption overrides historical campaign endpoints without changing any schedule. Wake stale personal/dream records were disclosed and excluded as premises.

## complete derivation or exact first unsupported line

For N=L*2^(m-1) point_m factors and ONE shared rare t-control activation, all core influences are delta*d and all control influences delta*a_L. Hence I=delta(Lm+t a_L). A constant control branch forces every putative disjoint second factor constant; all coordinates are relevant. The explicit coefficients show full support. On an active point block, M_r=r h2(2^(1-r)) dominates the harmonic potential 2^(-(r-r0))M_r0 for r0=m-k. Sum over blocks and use finite fair-tree induction. EVERY allowed adaptive rule has expected terminal M at least delta*N*2^(-k)(m-k)h2(2^k d), with equality for full allowed exposure. Actual product installation makes H+KL=M, regardless of incoming reference. Thus at L1 Capital/I>=(m-k)(m-k-1)/(m+t). At even m,t=m,k=m/2 this is >=(m-2)/8. At fixed even m>8C+2 and L growing, unpaid cost after C I is >=delta[L((m/2)(m/2-1)-Cm)-Cm], which tends to infinity. Exact activation entropy separately gives H/I<=7; these are no FEI counterexamples.

Every side condition is retained: k=m-1 gives zero bound, k=m is excluded from the h2 expression, m2/t1 checked, a_L and delta positive, denominators nonzero, deterministic spectral marginals allowed. A deeper complete rule has zero terminals; retaining inherited nonproduct P gives terminal H instead of M. These show why the depth and actual-product hypotheses matter. Fairness is used exactly in the harmonic two-child average. No tensorization of inherited reference kernels is used. No universal owner supplier or affine-prime obstruction is established. First unpaid line: supply a sufficient explicitly SELECTED deep/nonproduct rule for arbitrary cores with complete costs bounded by SAME unused original O(I) capital.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC preceded search; REVISED_SPEC fixes helperv1.1 with the SAME bounded domain. `python -X utf8 code/check.py`: {main['assertions']} exact predicates PASS, {main['parameter_triples']} parameter triples, four actual activated Boolean sources on5,6,7,13bits, direct Walsh/physical-edge influence agreement, all coefficients/full support, all109 nontrivial physical cuts on the three smallest fixtures, eight point spectra and finite GU guards, all26 residual states/22 adaptive actions on two point3 blocks. Runtime {main['seconds']:.3f}s. `python -X utf8 code/amplify.py`: {amp['assertions']} exact predicates PASS on260 coefficient cases C0..64, m=8C+4,L1/2/8/64; runtime {amp['seconds']:.4f}s. Those are algebra checks of the infinite-family coefficient, not giant truth tables. Arithmetic: integer FWHT, Fractions, rational log atoms and40-term atanh with positive tail; full quotient uses ALL FOUR signed rational corners. Code cache keys are exact rationals. Accepted v1.1 runtime4.263s differs from the rejected v1 runtime21.707s because this was a corrected-kernel rerun on a shared machine, not a larger domain or extra passing cases. Frozen memory estimate65MB, runtime55s; no GPU, heavy search or automatic escalation.

The first output's negative-log interval quotient used only two corners. Author audit found and repaired it before acceptance; INITIAL_OUTPUT_NOT_CERTIFIED.json is retained and NOT counted as a second passing certificate. Corrected same-domain rerun is the sole accepted main result. out/DEVELOPMENT_LOG.json records this. {formal} Memory admission before the core check was OK (6.5GB physical and15.9GB commit free); receipts pin actual source/compiler. No Mathlib job was launched because its documented footprint exceeds the1.5GB job limit. The finite certificate is author verification, not independent peer review.

## proof dependencies and changed downstream conclusions

The new proof is self-contained from explicit Boolean spectra, binary entropy concavity and finite-tree induction. A061/A087 receive attribution for the product-terminal starting obstruction. A087 FULL-terminal inequality is independently reconstructed locally without source repair; its hereditary GU proof is not newly accepted as a full chain here, and no GU extension to activated roots is claimed. Downstream rules must now state physical decomposability, per-block exposure depth, actual terminal reference, and TOTAL capital versus extra-reserve scope. Existing signed E/O corrections, old debits, full siblings and completed one-installation2A results remain in force. One new scoped claim only; external review pending.

## one next mathematical action and independent reviewer

{next_action}

## actual persistence receipts or precise save blocker

All four protocol files, proof, frozen/revised specs, standalone code, exact output, source review and compiler receipts saved within A065; finalizer verifies actual readback, exact field sets, statement/proof hashes, compatibility byte equality, two-line STATUS and file-size limits. Receipts: out/PERSISTENCE_RECEIPTS.json. No shared source/index edits, git, messaging, brain writes or deletion. Supervisor archive/mirror and actual downstream adoption unverified. Bounded checks finished; no research service or detached process was launched. Wake health warning remains an unrelated external-state issue.

**Universal bridge:** C019 stopping-tree payment advances by a quantitative falsifier that survives rare activation, full Fourier support, physical tensor primeness and EVERY adaptive bounded-per-block exposure rule: at t=m,k=m/2 TOTAL terminal capital/I grows at least (m-2)/8, and shared activation makes expected unpaid cost itself diverge. C024 is protected by making no inherited-kernel tensor claim. What remains is influence-priced ORIGINAL funding for a sufficiently selected deep or nonproduct terminal policy on arbitrary cores, with signed erasure/outcome terms, old bills and full H+KL retained. NEXT tests that exact selection/funding step against this broader guard, rather than extending an already-paid product history or claiming FEI from a special class.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: Stage21 saved: rare physical-tensor-prime full-support roots defeat ALL shallow product-stop rules; capital/I>=(m-2)/8, expected unpaid cost unbounded;17590+585 exact checks; FEI OPEN.\nNEXT: A087/A094 review TOTAL-capital/physical-prime scope; select deep/nonproduct arbitrary-core rule and fund FULL costs from SAME unused original O(I); affine primeness unproved.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} stage21 {R.name}: consumed A087 full-terminal corollary; new ONE-shared-gate activation makes physical tensor-prime/full-support roots while ALL k-per-block-depth rules force sharp terminal M bound. t=m,k=m/2 gives capital/I>=(m-2)/8; growing module multiplicity L makes absolute unpaid cost unbounded, H/I<=7. Corrected signed interval division before sole accepted same-domain rerun;17590 main+585 amplification predicates PASS. {formal} No universal supplier or affine-prime result. Saved locally; external review/mirror pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n## Stage21 rare physical-tensor-prime shallow-reset guard\nFor F=1+A_t(g-1), g a product of N=L*2^(m-1) point_m signs, I=2^-t[Lm+t(1-(1-d)^N)], d=2^(1-m). Every fair control-first adaptive rule querying <=k<=m-1 bits per original block before actual terminal marginal-product reset has FULL expected H+KL >=2^-t N2^-k(m-k)h2(2^k d)>=2^-t L(m-k)(m-k-1); sharp by full allowed exposure. A single inactive control gives a constant branch, forcing physical disjoint-tensor primeness; all Fourier coefficients are nonzero. This does NOT prove affine primeness. For L1,t=m,k=m/2, capital/I>=(m-2)/8; for fixed even m>8C+2, growing L makes terminal bill-CI grow unbounded. Shared gate avoids claiming inherited reference tensorization. All sources obey H/I<=7. Capital means TOTAL original H/K/funding, not extra reserve over prebooked inherited KL. Actual product terminal and bounded depth are essential: complete resolution/nonproduct P terminals escape. Signed interval division MUST take all four quotient corners; first v1 output was rejected and retained, v1.1 rerun accepted.\n')

assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
for field in protocol['required_per_run']['report_fields']: assert field in report
assert report.rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert digest(R/'PROOF.md')==claim['proof_source']['sha256']
paths=[p for p in R.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20_000_000 for p in paths)
receipts={'saved_at':stamp,'schema_checks':'PASS','compatibility_bytes_equal':True,'formal_scope':formal,
          'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in paths],
          'rolling':[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],
          'external_review':'PENDING','remote_mirror':'UNVERIFIED','full_fei':'OPEN'}
save(R/'out/PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'status':'SAVED_READBACK_VERIFIED','files':len(paths),'assertions':main['assertions']+amp['assertions'],'formal_scope':formal,'full_fei':'OPEN'}))
