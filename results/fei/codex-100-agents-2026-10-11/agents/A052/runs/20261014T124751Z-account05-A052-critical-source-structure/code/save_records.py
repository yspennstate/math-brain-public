"""Persist stage-six local records; no searches and no writes outside A052."""
from pathlib import Path
import hashlib,json,datetime

run=Path(__file__).resolve().parents[1]
agent=run.parent.parent
root=agent.parent.parent
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
source=root/'agents/A051/runs/20261014T085227Z-account05-A051-near-extremizer-definition'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
src_claims=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8-sig'))
if isinstance(src_claims,dict): src_claims=src_claims.get('claims',[src_claims])
dep=next(c for c in src_claims if c['claim_id']=='A051-FINITE-VARIATIONAL-CRITICAL-SELECTION')
assert dep['version']==1
assert dep['statement_sha256']=='ec8b36c8bf366f717243defe14463e8371c252ed9562543465acc9857d507f80'
assert sha(source/'VARIATIONAL_SELECTION.md')=='06c74590a0cac21265e344421f203b46ed84ba2c56db362099284dde70dd4542'
main=json.loads((run/'out/CHECK.json').read_text())
guard=json.loads((run/'out/MAJORITY_GUARD.json').read_text())
assert main['status']==guard['status']=='PASS'
assert main['assertions']+guard['assertions']==149215
review={'reviewer':'A052','claim_id':dep['claim_id'],'version':1,
        'statement_sha256':dep['statement_sha256'],'source_sha256':sha(source/'VARIATIONAL_SELECTION.md'),
        'verdict':'HOLDS_FULL_STATED_ANALYTIC_SCOPE','repair_supplied':False,
        'reconstruction':str(run/'REVIEW_A051.md'),
        'validation':str(run/'out/CHECK.json'),'full_fei_status':'OPEN'}
put('out/REVIEW_RECORDS.json',[review])
statement=('For every Boolean f on a finite uniform n-cube and K>=0, with '
           'G_f=sum_S fhat(S)log2(fhat(S)^2)chi_S, kappa=2/ln2, '
           'W_lambda(E)=sum_E fG-lambda|E|-(K/2)sum_boundary(E)f(x)f(y), '
           'and b_lambda=fG-lambda+(K/2)p_f, all W_lambda(E)<=0 are equivalent '
           'to bounded antisymmetric flows on both induced sign graphs with '
           '|F_xy|<=K/2 and div F>=b_lambda. The equivalence holds for real lambda. '
           'For every edit E, Delta D_K=(4/2^n)W_kappa(E)+R(E), where '
           'R(E) is the nonnegative summed Fourier Bregman remainder of '
           'k(t)=-t^2 log2(t^2)+3t^2/ln2. Thus an exact same-dimensional '
           'deficit maximizer admits kappa-flows and satisfies '
           '-W_kappa(E)>=2^n R(E)/4 for every E. For single-sign E, this slack '
           'equals unused outward flow capacity plus divergence-minus-charge slack. '
           'An actual three-bit majority at K=6 admits all kappa-cut flows yet '
           'has a same-dimensional edit increasing D_K by exactly 7; flow '
           'feasibility alone is insufficient for finite deficit maximality.')
hyp=['Uniform finite cube; Boolean signs; H in bits; I total influence.',
     'K>=0; zero Fourier coefficient contributes zero to G.',
     'Critical admission means exact maximum of D_K among all truth tables of the same dimension, not arbitrary ratio criticality or a positive-error near maximizer.',
     'For simultaneous lower-dimensional banks choose the least-essential-dimensional positive-deficit witness and then its finite D_K maximizer.']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
gap=('Compare mandatory Bregman-refund cut slack and sign-flow transport across a '
     'selected physical pair with its actual signed Fourier interaction and SAME '
     'positive D+S reserve, using one pivotal influence owner.')
new_id='A052-SIGNED-CUT-FLOW-CURVATURE-RESERVE'
claim={'claim_id':new_id,'version':1,'exact_statement':statement,'hypotheses':hyp,
       'statement_sha256':digest,'contributors':['A052'],
       'proof_source':{'path':str(run/'MONOCHROMATIC_FLOW_PROOF.md'),'sha256':sha(run/'MONOCHROMATIC_FLOW_PROOF.md')},
       'proof_dependencies':[{'claim_id':dep['claim_id'],'version':1,'statement_sha256':dep['statement_sha256'],
                              'acceptance':'A052 independent reconstruction HOLDS; no repair','review':str(run/'REVIEW_A051.md')}],
       'review_records':[],'status':'AUTHOR_PROVED_SCOPED; INDEPENDENT_REVIEW_PENDING',
       'supersedes':[],'refutes':[{'statement':'All signed semiconvex edit-cut inequalities imply finite deficit maximality.',
                                  'version':'unversioned exploratory implication','witness':'out/MAJORITY_GUARD.json'}],
       'first_unproved_line':None,'next_consumers':['A051','A053','A055','A005','A094','B11','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
put('CLAIMS.json',[claim])
next_action=gap+' Retain all physical children; seek a paid pair rather than another geometry-only obstruction.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B11','packet_id':'A052',
          'gap_id':'G-R-SELECT','attempt_id':'stage6-signed-flow-curvature',
          'method':'Independent finite-selector review; exact two-sign maxflow representation; Fourier Bregman refund; actual Boolean scope guard.',
          'mathematical_delta':'Two sign-graph flows compress all signed cuts exactly. Maximality requires refund-dominating cut slack. Three-bit majority disproves sufficiency of flows by an exact deficit improvement of 7.',
          'deliverable_status':'COMPLETE_LOCAL_SAVED',
          'mathematical_status':'SCOPED_PROOF_COMPLETE; UNIVERSAL_PHYSICAL_PAYMENT_AND_FULL_FEI_OPEN; NEW_APPLICATION_REVIEW_PENDING',
          'claim_versions_used':[{'claim_id':dep['claim_id'],'version':1,'statement_sha256':dep['statement_sha256'],'acceptance':'independently accepted by A052'}],
          'claims_created_or_changed':[{'claim_id':new_id,'version':1,'change':'scoped downstream application; not a new universal candidate'},
                                       {'claim_id':dep['claim_id'],'version':1,'change':'independent review accepted locally; source unchanged'}],
          'source_artifacts':['MONOCHROMATIC_FLOW_PROOF.md','REVIEW_A051.md','out/CHECK.json','out/MAJORITY_GUARD.json','out/REVIEW_RECORDS.json','out/FROZEN_SPEC.json','out/FROZEN_GUARD.json','code/check_flows.py','code/majority_guard.py'],
          'next_consumers':claim['next_consumers'],'next_action':next_action,
          'stagnant_substantive_attempts':0,'blockers':[gap],'packet_ids':['A052']}
expected=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(expected)
put('PROGRESS.json',progress)
(run/'PACKET_DELTA.json').write_bytes((run/'PROGRESS.json').read_bytes())
report=f'''# A052 B11 stage 6: critical cuts, sign flows, and exact curvature reserves

## exact target, quantifiers, hypotheses and units

For every finite uniform cube and Boolean sign function, H is Fourier entropy in bits, I is total influence, and D_K=H-KI. K>=0. The target is a restriction forced by exact finite D_K maximality while retaining the actual lower-dimensional physical child and Boolean phase reserves at a minimal positive-deficit witness. The result is an exact signed-cut/flow equivalence and a necessary Fourier curvature reserve. Neither an arbitrary hard root nor an arbitrary ratio near-extremizer is admitted. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Execution protocol revision {protocol['revision']} was read in full. BOARD.md snapshot headed 2026-10-14 12:47 UTC and B11 STREAM_NOTES.md v2 (2026-10-11 23:3xZ) were read; own STATUS.md carried the preceding complete Gibbs-bank stage. The lead's earlier composition target was already handled in previous stages; consuming the new finite-selector dependency follows protocol dispatch, with no disagreement with the lead.

New proof dependency: A051-FINITE-VARIATIONAL-CRITICAL-SELECTION@1, VARIATIONAL_SELECTION.md sections1--3, source statement hash {dep['statement_sha256']}; its REPORT.md and CLAIMS.json were also read. Independent acceptance is reconstructed in REVIEW_A051.md. A053's 20261014T052310Z REPORT.md supplies the distance-three point-edit payment context; its full packing proof is not a dependency here. A005's 20261014T061827Z REPORT.md supplies the warning that Gibbs-bank exhaustion merely restates KI_A-L_A; its proof is not substituted for new payment. A002's 20261014T100104Z REPORT.md supplies the actual signed-row rate2 obstruction and whole-root compensation warning. A055's current obstruction was read on BOARD only. Own previous exact and phase libraries were read/copied locally. Earlier campaign and paper baseline reading is not claimed as a fresh independent proof dependency. Source hashes for these local read artifacts are saved in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

Full derivation: MONOCHROMATIC_FLOW_PROOF.md sections1--5. With kappa=2/ln2 and charge b=fG-kappa+(K/2)p, all signed vertex-edit cut inequalities are equivalent to capacity-K/2 antisymmetric flows in the two actual induced sign graphs. The exact union identity W(E)=W(E+)+W(E-)-K e(E+,E-) preserves the favorable signed crossing term. Finite maxflow sufficiency is proved for real capacities, not assumed from a rational approximation.

Let R(E) be the summed Fourier Bregman remainder for the convex function -t^2 log2(t^2)+3t^2/ln2. The exact identity is Delta D_K=(4/N)W_kappa(E)+R(E). At a maximizer the signed-cut slack must therefore exceed N R(E)/4. On one sign set this slack is exactly unused outward flow capacity plus absorbing vertex slack. This nonlocal refund was omitted by the weaker curvature bound; it cannot be paid with a fresh reserve. Mixed edits retain their internal pivotal-edge slack, but their Fourier refunds need not split.

Actual scope guard: three-bit majority at K=6 has H=2, I=3/2, D=-7 and fG=-2 everywhere. Its two three-leaf sign stars carry rational flows3/2 per leaf toward each center at capacity3, with lambda=5/2<kappa. Thus even all strong kappa-cut inequalities hold. Flipping the entire negative sign set produces a constant and improves D by exactly7. For this edit W_kappa=10-4kappa and R=2+4/ln2, reproducing the improvement exactly. No registered theorem is refuted: the false exploratory sufficiency implication is recorded with its actual Boolean witness.

This is not component pruning: G comes from the complete original spectrum, including component cross terms. No raw indicator spectrum replaces a physical descendant. Finite maximality, additional to physical ratio criticality, licenses the vertex edits. Flow capacities sit on agreeing edges; influence counts pivotal edges. They have not been identified as the same resource.

First unsupported line: {gap} The new scoped theorem itself has no unproved line; this is the exact universal payment gap.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications out/FROZEN_SPEC.json and out/FROZEN_GUARD.json precede their respective jobs. Main command: `python -X utf8 runs\\{run.name}\\code\\check_flows.py`, from A052. It exhausted all276 tables for n=1,2,3, all65,808 ordered vertex edits, K=1,2,3,4, 263,232 signed-cut checks and2,208 sign-flow problems. Integer Walsh transforms were independently checked by character sums; exact physical edge influence, Fraction flows, prime-log vectors and proved 40-term logarithm series tails with outward dyadic rounding were used. All148,933 assertions PASS, observed runtime {main['runtime_seconds']:.6f} seconds. Strong 8/ln2 entropy curvature and V3 were checked, not just the relaxed rational constant. Every maximal-deficit table has a saved sign certificate under out/certs/. Three-bit parities at K=3 fail the admitted cut/flow conditions as expected.

Honest finite limitation: all feasible main-census flows had no positive-charge vertices. The census alone does not demonstrate nontrivial transport. A separate frozen named majority test at n=3,K=6 supplies six positive-charge vertices and rational nonzero flows. Command: `python -X utf8 runs\\{run.name}\\code\\majority_guard.py`. It checked all256 signed cuts at lambda=5/2, the exact flows, direct Fourier Bregman remainder, and deficit gain7:282 assertions PASS. Combined149,215 exact assertions. Output paths: out/CHECK.json and out/MAJORITY_GUARD.json. No float sign decision, automatic dimension increase, GPU, or background task was used. Estimated memory90MB main/30MB guard, maximum runtimes55s/10s; neither exceeds the300MB memok threshold. Rational lambda3 census certificates do not themselves certify sharper kappa-flows; analytic selector/flow equivalence does.

## proof dependencies and changed downstream conclusions

A051@1 is independently accepted at its complete analytic scope, without repair; review receipt is out/REVIEW_RECORDS.json. The new application has statement hash {digest}, complete local proof and pending independent review. It consumes the live dependency before adding this narrow application; no broad universal claim is opened. Previous full Gibbs-bank reviews reported by A005/A053 are context only, not a new paid-step premise. Sign geometry must now respect global spectral charge transport and, for actual finite maximizers, refund-dominating cut slack. Flow feasibility alone is disproved as a characterization. There is no claimed improvement to a universal FEI constant.

## one next mathematical action and independent reviewer

{next_action} Independent reviewers: A055 for the signed graph/component-pruning scope and A094 for the complete physical/Fourier reserve transfer; A051 should consume the exact refund and source-bound review. These are local handoffs in saved records; no messages were sent.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json are saved in this run with protocol field sets checked. Local code, exact outputs, frozen specs, proof, independent review and all small-cube maximal-table certificates are saved. STATUS.md is two lines; WORKLOG.md and LEARNED.md are appended. out/ARTIFACT_MANIFEST.json records SHA256 and byte sizes for every non-cache run artifact except itself; out/SOURCE_RECEIPTS.json records read-source hashes. All artifacts are below20MB. This is a local filesystem receipt; supervisor GitHub copy, brain ingestion, independent review of the new application and downstream use are unverified. No save blocker.

## Universal bridge

This stage moves C019 stopping-tree payment through B11's exact critical-source restriction: all signed cuts compress to two physical sign-graph flows, and exact maximality requires their cut slack to cover the nonlocal Fourier curvature refund. The actual majority guard shows a lost refund can hide an improvement of7 despite every cut passing. This closes the representation and exposes a specific missing resource, with zero claimed universal constant gain. The remaining bridge is to fund the selected physical pair's signed Fourier interaction from this refund-dominating slack and the SAME unused D+S bank, counting each pivotal influence owner once. NEXT is that transfer because geometry-only component restrictions and Gibbs-bank reparametrization already fail to supply payment; another isolated class result would leave the universal gap unchanged.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
state='STATE: Stage6 complete: signed-cut two-flow equivalence and exact curvature reserve proved; majority disproves flow sufficiency by deficit gain7; 149215 exact checks PASS; A051 reviewed; FEI OPEN.\n'
state+='NEXT: Transfer mandatory Bregman-refund/sign-flow slack to selected physical-pair Fourier interaction using SAME unused D+S bank and one pivotal owner; A055/A094 review.\n'
(agent/'STATUS.md').write_text(state,encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as fp:
    fp.write('\n2026-10-14 stage 20261014T124751Z: independently reconstructed A051 finite selector; signed cuts reduced to two bounded flows; derived exact Bregman curvature refund and mandatory slack. Exhausted276 tables/65808 edits, main148933 assertions in8.049146s. Main feasible flows were trivial; frozen majority K6 guard gives nonzero flows but edit gain7,282 assertions. Saved protocol files and scoped theorem; physical/Fourier payment and full FEI remain open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as fp:
    fp.write('\nStage6 durable restriction (2026-10-14): for K>=0, W(E)=W(E+)+W(E-)-K e(E+,E-); all signed cuts iff both induced-sign capacity-K/2 flows have divergence>=fG-lambda+(K/2)p. Use the complete parent G, never a component indicator spectrum. For k=h+3t^2/ln2, exact Delta D=(4/N)W_kappa+R_k; maxima require -W_kappa>=NR_k/4. On a monochromatic cut its slack is unused outward capacity plus divergence slack. Majority3,K6 has fG=-2, two leaf-to-center flows3/2 at lambda5/2<kappa, all strong cuts, but whole-negative-set edit improves D by7; flow feasibility does not imply criticality. Agreeing-edge capacities are not pivotal influence. Lambda3 rational feasibility certificates do not alone prove kappa feasibility. Finite epsilon-maximal cuts retain N epsilon/4 and cannot silently use exact flow equivalence. A051 full finite selection/edit theorem independently accepted without repair.\n')
read_sources=[protocol_path,root/'BOARD.md',root/'claude/B11/STREAM_NOTES.md',source/'REPORT.md',source/'CLAIMS.json',source/'VARIATIONAL_SELECTION.md',
 root/'agents/A053/runs/20261014T052310Z-account05-A053-near-tensor-perturbations/REPORT.md',
 root/'agents/A005/runs/20261014T061827Z-account05-A005-noncircular-endpoint-referee/REPORT.md',
 root/'agents/A002/runs/20261014T100104Z-account05-A002-hardness-preserving-transformations/REPORT.md']
put('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in read_sources])
artifacts=[]
for p in sorted(run.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.name=='ARTIFACT_MANIFEST.json': continue
    assert p.stat().st_size<20*1024*1024,(p,p.stat().st_size)
    artifacts.append({'path':str(p.relative_to(run)),'sha256':sha(p),'bytes':p.stat().st_size})
put('out/ARTIFACT_MANIFEST.json',{'scope':'local immutable stage artifacts; manifest excludes itself and Python cache',
                               'artifacts':artifacts,'rolling_receipts':[{'path':str(agent/p),'sha256':sha(agent/p)} for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
print(json.dumps({'status':'SAVED','artifact_count':len(artifacts),'claim_statement_sha256':digest,'assertions':149215,'full_fei':'OPEN'}))
