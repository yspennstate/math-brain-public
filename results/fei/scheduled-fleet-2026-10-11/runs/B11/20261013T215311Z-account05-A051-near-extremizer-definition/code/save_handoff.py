"""Persist protocol records and local receipts. Writes only inside A051."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parent.parent
AGENT=ROOT.parent.parent
BASE=AGENT.parent.parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
run=ROOT.name
statement=('For every finite uniform-cube Boolean sign and queried physical block A, define '
 'Gamma_A=sum_T q_T log2(E_a w_T(a)^4/q_T^2) on positive-q retained rows and V_A=B_A+Gamma_A. '
 'Then 0<=J_A<=Gamma_A<=|A|, L_A<=V_A, Gamma is additive under disjoint tensor products with aligned queried blocks, '
 'and Gamma=0 exactly when all squared child row coefficients coincide. Its exact signed convolution representation is '
 'sum_T q_T log2(1+sum_(V nonempty)(sum_U fhat(U,T)fhat(U xor V,T))^2/q_T^2). '
 'For n>=2, K_col(n)=max_f min_(nonempty proper A,I_A>0) V_A/I_A satisfies M_n<=K_col(n)<=n M_n/(n-1), '
 'where M_n is the finite maximum of H/I on at most n bits. Therefore lim K_col(n)=sup M_n as extended reals. '
 'A least-essential-dimension fixed-K violating witness exists whenever any such violation exists, and every proper block '
 'satisfies V_A>=K I_A+D_K(f). On the exact named six-bit NAND case0006, mask48 uniquely satisfies V_A/I_A<R(f), '
 'with V_A/I_A<47/20<12/5<R(f), while every singleton cost exceeds 319/100; its nonconstant physical child has positive '
 'root-ratio deficit. These are finite certificates and structural identities, not a universal FEI payment theorem.')
claim={
 'claim_id':'A051-JOINT-COLLISION-DESCENT','version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean signs on finite uniform cubes; entropy in bits; zero-q rows omitted',
 'n>=2 and nonconstant f for normalized minima; irrelevant coordinates permitted',
 'Proper physical queried sets; full queried factors permitted only when the overall cut remains proper',
 'Minimality is fixed-threshold essential-dimension minimality, not inherited ratio criticality',
 'No global optimizer, universal K or independent-agent acceptance is assumed'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account05/A051'],
 'proof_source':{'path':str(ROOT/'JOINT_CHANNEL_PROOF.md'),'sha256':digest(ROOT/'JOINT_CHANNEL_PROOF.md'),
 'locator':'Sections 1--5; out/CONTROL_NAND6_case0006.json and out/INDEPENDENT_REPLAY.json'},
 'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_AND_EXACTLY_REPLAYED_PENDING_INDEPENDENT_AGENT_REVIEW',
 'supersedes':[],'refutes':['The joint collision upper certificate also collapses to singleton minimization'],
 'first_unproved_line':None,'next_consumers':['claude/B11','A052','A053','A055','A018','A090','A094','B20']}
save('CLAIMS.json',[claim])
review={'claim_id':'A052-OPTIMAL-RECENTRING-SINGLETON-COLLAPSE','version':1,'reviewer':'account05/A051',
 'verdict':'ACCEPT_ANALYTIC_SCOPE_ONLY','accepted_scope':'Distributional and capped collapse; analytic tensor and strict-product obstruction',
 'not_reviewed':'1150-shape and seven-seed census counts; cited logarithmic-Sobolev dependency',
 'review_source':str(ROOT/'REVIEW_A052.md'),'review_sha256':digest(ROOT/'REVIEW_A052.md'),'repair_supplied':False}
save('out/SOURCE_REVIEW.json',review)
sources=[
 Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),BASE/'BOARD.md',BASE/'claude/B11/STREAM_NOTES.md',
 AGENT/'runs/20261011T233123Z-account05-A051-near-extremizer-definition/UNIVERSAL_DESCENT_SQUEEZE.md',
 AGENT/'runs/20261011T233123Z-account05-A051-near-extremizer-definition/code/descent_compositions.py',
 BASE/'agents/A052/runs/20261012T003906Z-account05-A052-critical-source-structure/REPORT.md',
 BASE/'agents/A052/runs/20261012T003906Z-account05-A052-critical-source-structure/SINGLETON_COLLAPSE.md',
 BASE/'agents/A052/runs/20261012T003906Z-account05-A052-critical-source-structure/CLAIMS.json',
 BASE/'agents/A053/runs/20261012T014744Z-account05-A053-near-tensor-perturbations/REPORT.md',
 BASE/'agents/A055/runs/20261013T212502Z-account05-A055-extremal-obstruction-referee/REPORT.md',
 BASE/'agents/A055/runs/20261013T212502Z-account05-A055-extremal-obstruction-referee/REVIEWS.md',
 BASE/'agents/A018/runs/20261011T221538Z-account05-A018-shared-data-collision-law/REPORT.md',
 BASE/'agents/A018/runs/20261011T221538Z-account05-A018-shared-data-collision-law/COLLISION_BLOCK_INTERFACE.tex',
 BASE/'agents/A018/runs/20261012T010436Z-account05-A018-shared-data-collision-law/REPORT.md',BASE/'agents/A054/LEARNED.md']
save('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources if p.is_file()])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':run,'stream':'B11','packet_id':'A051',
 'gap_id':'B11-UNIVERSAL-PROPER-BLOCK-SELECTION','attempt_id':'A051-stage3-joint-collision',
 'method':'Scoped independent dependency review; signed row fourth-moment upper certificate; finite-maxima/minimal-witness proof; frozen exact pilot and direct-character replay',
 'mathematical_delta':'Joint V=B+Gamma permits proper-block gains: NAND6 mask48 cost<2.35 while all singleton costs>3.19. Tensor-additive Gamma and co-singleton equality preserve M_n<=K_col(n)<=nM_n/(n-1). Child deficits remain explicit; additive recentring collapse independently accepted at analytic scope.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; supervisor mirror pending',
 'mathematical_status':'SELF_CONTAINED_JOINT_CERTIFICATE_AND_FINITE_EXTREMALITY_PROVED; UNIVERSAL_BLOCK_SELECTION_AND_FULL_FEI_OPEN',
 'claim_versions_used':['A052-OPTIMAL-RECENTRING-SINGLETON-COLLAPSE@1 (analytic clauses independently reviewed; no finite census acceptance)',
 'A051-PROPER-BLOCK-DESCENT-SQUEEZE@1 (context; new proof self-contained)'],
 'claims_created_or_changed':['A051-JOINT-COLLISION-DESCENT@1','A052-OPTIMAL-RECENTRING-SINGLETON-COLLAPSE@1 scoped review record only'],
 'source_artifacts':['JOINT_CHANNEL_PROOF.md','REVIEW_A052.md','out/SOURCE_MANIFEST.json','out/SUMMARY.json','out/INDEPENDENT_REPLAY.json','out/CONTROL_NAND6_case0006.json'],
 'next_consumers':['claude/B11','A052','A053','A055','A090','A094','B20'],
 'next_action':'Use dimension-critical fixed-K inequality to select a proper block paying B plus signed-convolution Gamma; separate zero-channel h(x)y core entropy obstruction and retain child/terminal deficits; independently reconstruct the new finite squeeze.',
 'stagnant_substantive_attempts':0,
 'blockers':['No uniform bound on K_col(n) or critical-witness block-selection theorem','New A051 claim awaits independent-agent review; no mirror verification',
 'A054 stage2 REPORT absent locally despite BOARD status; only rolling LEARNED read and not used as proof dependency'],
 'packet_ids':['A051']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
(AGENT/'STATUS.md').write_text('STATE: A051 stage3 saved: joint collision block certificate; NAND6 mask48 cost<2.35 versus singleton costs>3.19; finite K_col squeeze; 30340+1663 exact checks; A052 analytic collapse reviewed; full FEI OPEN.\nNEXT: A090/A094 review; A052/A055 select a uniformly paid signed-collision block on dimension-critical witnesses, retaining child/terminal deficits and the h(x)y zero-channel entropy obstruction.\n',encoding='utf-8')
tag='2026-10-13 21:53 UTC stage (run '+run+')'
entry=tag+': Read updated BOARD/B11 direction and own status; consumed A052 singleton-collapse obstruction and A055 terminal warning. Independently accepted analytic collapse/capped collapse/tensor clauses, explicitly excluding bundled census and log-Sobolev dependency. Replaced additive beta with joint collision Gamma; proved J<=Gamma, signed-convolution formula, tensor additivity and exact co-singleton equality. Derived M_n<=K_col(n)<=nM_n/(n-1) and dimension-minimal fixed-threshold necessity without a global optimizer. Frozen all n<=3 plus four controls: 280 tables/1736 blocks, 30340 exact checks in 2.317s. Direct-character independent replay: 168 blocks/1663 checks in 0.632s. Unique NAND6 mask48 has V<2.35<R, all singleton costs>3.19, and a positive surviving child deficit. No universal K; no external review or mirror claimed. All protocol and rolling artifacts saved locally.\n'
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+entry)
lesson='''
- Stage3 joint collision certificate: for actual child Fourier rows w_T, q_T=E w_T^2, Gamma_A=sum q_T log2(E w_T^4/q_T^2). Jensen under row posterior gives J_A<=Gamma_A<=|A|; signed convolution k_V=sum_U fhat(U,T)fhat(U xor V,T) gives Gamma=sum q log2(1+sum_(V!=0)k_V^2/q^2). Cancellation occurs before squaring. Gamma tensor-adds and is zero iff squared child row laws agree.
- The certificate V=B+Gamma does not collapse to singletons: exact NAND6 case0006 mask48 uniquely has V/I_A<R, with V<2.35<R (R>2.40), while all singleton costs exceed3.19. Three children are constants; the fourth has positive root-ratio deficit between0.44 and0.45. This pays a block comparison, not a critical source or its terminal entropy.
- Co-singleton queries have one-bit Boolean children and squared row values0/1, so Gamma=J and V=H exactly. Thus finite K_col(n)=max_f min_A V_A/I_A satisfies M_n<=K_col(n)<=nM_n/(n-1), with extended limit C_*. Minimal fixed-K witnesses force V_A>=K I_A+D_K for every proper block; no global optimizer is needed. Uniform selection/payment remains equivalent to the hard all-dimensional problem.
- Zero channel alone cannot pay B: F=h(x)y gives Gamma=J=0, B=H(h), I_A=I(h). Selecting the prescribed h block at universal price already asks full FEI for h. Preserve the terminal deficit telescope.
- A052 analytic collapse reviewed via Bayes prediction risks and conditional-mutual-information gaps; capped collapse and quadratic tensor formulas accepted. Its composite finite census and log-Sobolev channel dependency are outside this review. Stage3 30340 exact checks plus1663 direct-character replay checks passed; no new independent-agent acceptance claimed.
'''
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(lesson)
save('out/ARTIFACT_MANIFEST.json',{'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'files':[{'path':str(p.relative_to(ROOT)),'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_MANIFEST.json'],
 'rolling':[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']],
 'external_mirror_verified':False,'independent_agent_review':'pending'})
print(json.dumps({'run':run,'claim_sha256':claim['statement_sha256'],'files':len(list(ROOT.rglob('*'))),'progress_keys':len(progress)}))
