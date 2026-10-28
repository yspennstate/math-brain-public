from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parents[1]
P=Path('math-open-problems/reports/fei-2026-10-11');RUN=R.name
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):
 (R/p).write_text(v if isinstance(v,str) else json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def append(p,s):
 old=p.read_text(encoding='utf-8') if p.exists() else ''
 if RUN not in old:p.write_text(old+'\n'+s,encoding='utf-8')
proto=read(P/'EXECUTION_PROTOCOL.json');c=read(R/'out/CHECK.json');v=read(R/'out/INDEPENDENT.json');pilot=read(R/'out/PILOT.json')
assert c['status']==v['status']=='PASS'
for helper,spec,key in [('check_compactness.py','FROZEN_SPEC.json','helper_sha256'),('independent.py','FROZEN_INDEPENDENT.json','helper_sha256')]:
 assert sha(R/'code'/helper)==read(R/'out'/spec)[key]
assert c['utility_sha256']==sha(R/'code/exact_utils.py')==read(R/'out/FROZEN_SPEC.json')['utility_sha256']
assert c['root_tables']==278 and c['roundings']==1082 and c['rank_family_checks']==556
assert c['assertions']+v['assertions']==15085
sources=[P/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B11/STREAM_NOTES.md',Path('~/AGENTS.md')]
for agent,run,names in [
 ('A051','20261021T193146Z-account03-A051-near-extremizer-definition',['AFFINE_SELECTION.md','CLAIMS.json']),
 ('A051','20261023T002518Z-account03-A051-near-extremizer-definition',['REPORT.md','RESET_BUDGET.md','CLAIMS.json']),
 ('A052','20261023T014825Z-account03-A052-critical-source-structure',['REPORT.md','RANK_PAIR_PROOF.md','REVIEW_A051.md','CLAIMS.json']),
 ('A002','20261023T010524Z-account03-A002-hardness-preserving-transformations',['REPORT.md','CLAIMS.json']),
 ('A005','20261023T035753Z-account03-A005-noncircular-endpoint-referee',['REPORT.md'])]:
 for name in names:sources.append(TEAM/'agents'/agent/'runs'/run/name)
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'provenance':'observed mutable local bytes; reading scope stated in REPORT'} for p in sources])
statement=('For a Boolean sign f on a finite or countable uniform product cube with finite Fourier entropy and influence, let delta_m be squared Fourier mass outside labels contained in [m], T_H its entropy contribution and T_I its degree-weighted mass. For m>=1 and delta_m<=1/8, g=sign E[f|X_1,...,X_m] with sign(0)=+1 obeys P(f!=g)<=delta_m/2, |I(f)-I(g)|<=m delta_m+T_I, and |H(f)-H(g)|<=T_H+h2(sqrt(2delta_m))+m sqrt(2delta_m). Thus affine compression/minimization gives an actual Boolean gstar of dimension at most m with D_K(gstar)>=D_K(f)-E_m(K), where E_m is the displayed entropy bound plus K(m delta_m+T_I), for every K>=0. Conversely for every nonconstant full-affine-span affine-influence-minimal finite Boolean seed g, taking t=2^k disjoint seed copies and activating their product on k zero controls yields actual full-span affine-influence-minimal F_k with L2 distance squared from 1 at most 4*2^-k, I(F_k)->I(g), H(F_k)->H(g), and |D_K(F_k)-D_K(g)|<=2^-k[(10+2K)k+15]. For every fixed spectral window the entropy and influence outside it tend to H(g) and I(g). Bounded influence and L2 convergence therefore do not supply the entropy/influence tail control needed for optimizer arguments. No infinite optimizer or universally paid pair is asserted.')
claim={'claim_id':'A051-TAIL-CERTIFIED-FINITE-APPROXIMATION-AND-ESCAPE','version':1,'exact_statement':statement,'hypotheses':['Normalized real Walsh coefficients; uniform finite or countable product; entropy bits; K>=0','Approximation requires finite H,I, m>=1 and explicitly delta_m<=1/8; zero coefficients and sign ties have stated conventions','Escape requires a fixed nonconstant finite Boolean seed with full affine spectral span and full affine influence minimality; k>=2, t=2^k, controls precede all data coordinates'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A051'],'proof_source':str(R/'COMPACTNESS.md'),'proof_dependencies':['A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1','Elementary Parseval, conditional variance, maximal finite-alphabet coupling and actual signed activation coefficients','A002-ACTIVATED-FULL-AFFINE-RESET-LEDGER@1 and A055 activation context motivate the construction; displayed activation profile and preservation are rederived'],'review_records':[],'status':'AUTHOR_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A052','A055','A005','A002','A090','A094']}
save('CLAIMS.json',[claim])
save('out/REVIEW_RECORDS.json',[{'source_claim_id':'A052-RANK-RELEASE-ORIGINAL-PAIR-PAYMENT','version':1,'source_statement_sha256':'ae8d73daa7c9e75e490620bf1e9c987dead51f19d9a214086a7a52e2065a519d','reviewer':'A051','disposition':'HOLDS_WITHOUT_REPAIR_SCOPED','scope':'RANK_PAIR_PROOF Sections1--2: candidate-basis threshold integral, exact executable release and complete original-child signed bank/eligibility. Sections3--5 paid-fragment estimates are not newly independently accepted.','proof':str(R/'REVIEW_A052.md'),'certificate':str(R/'out/CHECK.json')},{'source_claim_id':'A051-FULL-AFFINE-CHILD-RELEASE-BUDGET','version':1,'source_statement_sha256':'458cfc425aa95401d3f2f68a63f1805f406f31044ab52da1575729b20f09e91d','reviewer':'A052','disposition':'SOURCE_BOUND_SCOPED_ACCEPTANCE_OBSERVED','scope':'Section2 equation3 smaller-child bank/eligibility and Section3 finite adaptive reset telescope, unchanged without repair; excludes new all-k budgets and perturbation bound','source':str(TEAM/'agents/A052/runs/20261023T014825Z-account03-A052-critical-source-structure/REVIEW_A051.md')}])
progress={'protocol_revision':proto['revision'],'run_id':RUN,'stream':'B11','packet_id':'A051','gap_id':'G-R-SELECT','attempt_id':'A051-stage9-tail-certified-approximation-and-escape','method':'Consume new rank-ownership review; change from repeated local pair accounting to explicit compactness/finite approximation admission, with SAME-K actual Boolean escape and independent exact replay','mathematical_delta':'Explicit tail budget transfers fixed-K deficit to a finite canonical Boolean table. Actual full-span affine-minimal bounded-I family converges in L2 to1 while retaining arbitrary seed H,I and ratio, so bare compactness cannot replace finite critical selection. A052 rank/bank Sections1--2 independently accepted without repair.','deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_VERIFIED','mathematical_status':'NARROW_APPROXIMATION_AND_OBSTRUCTION_PROVED_AUTHOR_LEVEL; UNIVERSAL_FEI_OPEN','claim_versions_used':['A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1','A051-FULL-AFFINE-CHILD-RELEASE-BUDGET@1 (reviewed source scope only)','A052-RANK-RELEASE-ORIGINAL-PAIR-PAYMENT@1 (Sections1--2)','A002-ACTIVATED-FULL-AFFINE-RESET-LEDGER@1 (report context; activation profile rederived)'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':[str(R/'COMPACTNESS.md'),str(R/'REVIEW_A052.md'),str(R/'out/CHECK.json'),str(R/'out/INDEPENDENT.json'),str(R/'out/SOURCE_RECEIPTS.json')],'next_consumers':claim['next_consumers'],'next_action':'A052/A055 force one original proper-pair independent-rank funding step on a genuine finite least-dimensional K-witness with SAME unused nonnegative smaller-affine-child reserves, mixed T and complete terminals; A002/A005 independently review tail bound and SAME-K escape before any compactness-based optimizer argument.','stagnant_substantive_attempts':0,'blockers':['Full FEI remains open: no universal lower funding/selection of an original proper pair','New approximation/escape theorem has no independent-agent review yet','Tail error is an explicit additional hypothesis, not obtained from bounded influence or L2 convergence','Brain self-care degraded/unverified: owner-model/state-of-mind notes stale; mathematical checks do not repair personal-context freshness'],'packet_ids':['A051']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A051/B11 stage9: make near-extremal finite approximation admissible without assuming an optimizer. For every K>=0, give an explicit error transferring D_K=H-KI from an actual finite/countable Boolean sign to a finite canonical Boolean table, and decide whether bounded influence plus L2 convergence supplies that error. It does not. Entropy is in bits; all Boolean outputs, spectral signs and countable-coordinate embeddings are explicit. Full FEI remains OPEN. Owner deadline23October2026 14:49UTC governs over the older protocol date.

# sources actually read, revisions and theorem locators

BOARD header23October05:05UTC, B11 STREAM_NOTESv2, own stage8 STATUS, machine AGENTS and protocol2026-10-11-execution-v2 consumed. Fresh substantive reads: A05201:48 REPORT, RANK_PAIR_PROOF Sections1--5, REVIEW_A051 and current claim ID/hash; A00201:05 REPORT/current claim ID; A00503:57 REPORT; current board A055 scoped paid-pair hardness acceptance. Earlier campaign/registry/four-manuscript reads are retained from previous stages, not represented as fresh audits. out/SOURCE_RECEIPTS pins observed mutable bytes; only stated read scopes support claims. One read-only two-wording math recall supplied older Boolean/induction guards and no needed compactness theorem; no outside literature or novelty premise is used.

The unchanged lead's old point-defect assignment was closed earlier. Dispatch consumes the new rank/bank dependency and changes mechanism to the packet's explicit finite-approximation admission. The escape theorem is an all-dimensional negative control for that admission, not another proposed universal proof by local payment. Brain self-care remains degraded/unverified because owner-model and state-of-mind notes are stale; current instructions and proof files govern and this stage does not repair that personal-context freshness.

# complete derivation or exact first unsupported line

COMPACTNESS Sections1--4 contain the proof. Round the actual conditional mean on the first m bits, then use e<=delta/2, physical edge mismatch and finite-alphabet spectral coupling. The exact sufficient deficit error is E_m(K)=T_H+h2(sqrt(2delta))+m sqrt(2delta)+K(T_I+m delta), for delta<=1/8. Finite affine compression/minimization preserves H and can only increase D_K. Thus D_K(f)>E_m(K) gives a concrete finite Boolean violation; no infinite optimizer is used. Sufficient vanishing tails and m sqrt(delta)->0 imply finite approximation, but those hypotheses are explicitly additional.

For ANY canonical nonconstant seed, tensor t=2^k copies first and activate on k zero controls. Actual signed coefficient summation proves |H(F_k)-Hseed|<=2^-k(10k+15), I(F_k)=Iseed+k2^-k(1-mu^t) and ||F_k-1||_2^2<=4*2^-k. Full affine span/minimality persist; the proof checks every type of parity and the replicated support rank. The fixed-K deficit error is at most2^-k[(10+2K)k+15], so any certified positive seed deficit survives at an explicitly selectable finite k. For each fixed spectral window entropy and influence escape to its complement. The seed ratio is retained while F_k converges even almost surely to1. This invalidates entropy-continuity/optimizer admission from L2 compactness plus bounded I, including on the canonical reduced class. It does not prove that an optimizer cannot exist, or that any unspecified K has a violating seed.

FIRST UNSUPPORTED UNIVERSAL LINE: force an adequate independent cheap-parity rank at one ORIGINAL proper pair of a genuine finite least-dimensional positive K-witness, paying its signed bill with SAME unused nonnegative smaller-affine-child reserves, mixed T and every terminal. The new approximation/escape results do not select that pair or establish a universal constant.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs in out precede both jobs. From A051 run python -B -X utf8 runs/{RUN}/code/check_compactness.py --pilot, then without --pilot; run code/independent.py under the same run. A pre-run syntax check caught and corrected an unmatched closing parenthesis before specification freeze or mathematical execution. No failed mathematical pilot was hidden.

Pilot:22 labelled roots,58 roundings,44 rank families,894 assertions PASS in{pilot['runtime_seconds']:.6f}s. Full:278 labelled roots n0..3,1082 initial-coordinate Boolean roundings,556 rank families,300 small-tail continuity cases and five fixed activated bent/point fixtures maxn10;{c['assertions']} exact assertions PASS in{c['runtime_seconds']:.6f}s. Every source parity basis through3bits is enumerated to independently compare threshold integration with the finite optimum. The source edge identities, zero-error/zero-coefficient cases, tied costs, rank0, all sign ties and K0,1,2,4 deficit transfers are retained. Every directional cost and affine-support rank is checked on the five named activation fixtures; these fixtures are not a class census.

Independent direct-character and physical-edge replay:{v['assertions']} assertions PASS in{v['runtime_seconds']:.6f}s on three actual activated roots maxn6, every coefficient/prefix rounding, plus rational rate monotonicity guards k2..20. Combined final full count15085, excluding pilot and prior stages. Arithmetic: integer Walsh or separate direct characters, exact Fraction, prime-log entropy identities, rational32-term atanh enclosures, integer square-root outward bounds. No floating sign decisions. The all-k theorem and countable-product approximation are analytic proofs, not extrapolations from fixtures. The replay is a second implementation by A051, not independent-agent acceptance.

Jobs capped55s, estimated50--90MB RAM with observed peak unmeasured; no job expected above300MB, so no large-job admission was needed. Initial compute snapshot had5.7GB physical free/11.7GB commit free and87.7percent CPU. Shared pressure reports were treated as data; no existing work changed. No GPU, detached work, dimension escalation, Lean attempt or formal verification is claimed.

# proof dependencies and changed downstream conclusions

REVIEW_A052 independently reconstructs RANK_PAIR_PROOF Sections1--2 unchanged without repair: finite rank integral, executable centered release, and the SAME complete child bank/eligibility. Its all-k15/4 paid fragment is context, not newly accepted. Source-bound A052 REVIEW_A051 independently accepts my stage8 bank equation and finite adaptive telescope; no broader acceptance of all-k/perturbation claims is inferred. The new theorem uses prior finite affine reduction; the tensor/activation coefficient profile and minimum-basis preservation are rederived. Review records and source statement hashes are saved. No registered source theorem is refuted. No universal FEI constant improves. The exact changed conclusion is that any compactness-based extremality admission must include tail information, while the finite least-dimension/maximal-deficit selector continues to be valid without it.

# one next mathematical action and independent reviewer

{progress['next_action']}

A090/A094 should challenge the coupling factor, influence edge factor, zero-mean/full-span endpoints, shifting-coordinate embedding and complete retained seed deficit. This saved source-bound handoff sends no messages. No seed-positive deficit is assumed where none has been certified.

# actual persistence receipts or precise save blocker

All four protocol files, proof, scoped independent review, frozen specs, helper code and exact outputs saved under A051 only. Finalizer validates exact schema field sets, statement hash, byte-identical compatibility copy, seven required report headings,20MB cap and two-line STATUS. out/PERSISTENCE_RECEIPT hashes every run artifact and rolling file; a second reopen verifies the hashes. Local save is verified once out/HANDOFF_CHECK is PASS. New independent-agent acceptance, registry adoption, supervisor copying and brain ingestion remain unverified. No git, brain writes, outside-folder research writes or stopped existing work. No stage job remains running after final verification.

## Universal bridge

C019 stopping-tree payment through B11 critical selection gains a rigorous admission boundary: an explicit tail-funded finite Boolean approximation preserves fixed-K deficit up to a stated error, while a SAME-K canonical Boolean escape family disproves the missing continuity inference from bounded influence/L2 alone. It also receives independently reconstructed rank-release ownership from A052. Universal constant gain is0; original-pair lower-funding from genuine nonnegative child reserves remains open. NEXT returns to that exact finite critical class and SAME unused bank, avoiding both an assumed infinite optimizer and weak affine endpoints that retain arbitrary seed difficulty. This targets the unpaid universal implication rather than another isolated class bound.
'''
save('REPORT.md',report)
status='STATE: A051 stage9 saved: tail-certified finite Boolean approximation; SAME-K canonical bounded-I escape defeats bare L2 optimizer admission;15085 exact checks PASS; A052 rank/bank Sections1--2 scoped HOLDS; FEI OPEN.\nNEXT: A052/A055 fund one ORIGINAL pair on genuine finite critical witnesses from SAME nonnegative affine-child reserves and independent quotient rank; A002/A005 review explicit tail budget and seed-preserving escape.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
append(A/'WORKLOG.md',f'2026-10-23 stage9 {RUN}: consumed new paid-pair hardness/rank results; independently reconstructed A052 rank/bank Sections1--2. Proved explicit conditional-sign finite approximation and arbitrary-seed SAME-K entropy/influence escape inside full-span affine minima.15085 exact checks PASS. Bounded I and L2 compactness cannot license optimizer continuity. Universal original-pair critical selection remains unpaid; no new FEI constant.\n')
append(A/'LEARNED.md',f'{RUN}: For delta outside first-m spectral labels, conditional-sign rounding has e<=delta/2, |dI|<=m delta+T_I and |dH|<=T_H+h2(sqrt(2delta))+m sqrt(2delta), delta<=1/8. Canonicalization can only improve D_K. Never infer these tail hypotheses from bounded I: t=2^k tensor copies of ANY canonical full-span nonconstant seed, activated on k controls, converge in L2/a.s. to1 while H,I converge to seed values; |dD_K|<=2^-k[(10+2K)k+15]. The actual family stays affine-minimal/full-span. This blocks bare compactness admission, not existence of every optimizer or FEI itself. A052 independent cheap-rank integration owns overlapping swaps; Sections1--2 accepted unchanged.\n')
req=proto['required_per_run']
assert set(claim)==set(req['claim_fields'])
pf={v.split(' (')[0] for v in req['progress_fields']};assert set(progress)==pf
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for head in req['report_fields']:assert '# '+head in report
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipt=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name not in {'PERSISTENCE_RECEIPT.json','HANDOFF_CHECK.json'}:
  assert p.stat().st_size<20_000_000
  receipt.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:receipt.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save('out/PERSISTENCE_RECEIPT.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'actual local save only; remote/brain adoption unverified','files':receipt})
for row in read(R/'out/PERSISTENCE_RECEIPT.json')['files']:
 p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
assert read(R/'CLAIMS.json')[0]['statement_sha256']==hashlib.sha256(statement.encode()).hexdigest()
save('out/HANDOFF_CHECK.json',{'status':'PASS','assertions':15085,'files_reopened':len(receipt),'schemas':'exact field sets verified','claim_sha256':claim['statement_sha256'],'remote_copy':'unverified','new_independent_agent_review':'pending','full_fei':'OPEN'})
print(json.dumps(read(R/'out/HANDOFF_CHECK.json')))
