import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];BASE=AGENT.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
old=AGENT/'runs/20261014T015635Z-fleet05-A052-critical-source-structure'
dependencies=json.loads((old/'out/REVIEW_RECORDS.json').read_text())
a55run=AGENT.parent/'A055/runs/20261014T033719Z-fleet05-A055-extremal-obstruction-referee'
c55=json.loads((a55run/'CLAIMS.json').read_text())[0]
review={'claim_id':c55['claim_id'],'version':c55['version'],'statement_sha256':c55['statement_sha256'],
 'reviewer':'A052','verdict':'HOLDS_SECTIONS1_TO3_ONLY','scope':'Joint-zero rigidity; dyadic floor; point-defect formula. No full admission-chain acceptance.',
 'review_source':str(ROOT/'REVIEW_AND_SCOPE.md'),'review_sha256':sha(ROOT/'REVIEW_AND_SCOPE.md'),'contributor_conflict':False,'registry_adoption':'PENDING'}
put('out/REVIEW_RECORDS.json',[review])
statement='For every nonconstant finite uniform-cube Boolean sign f with positive ratio R=H(f)/I(f) and every physical descendant ratio at most R, max_i Inf_i(f)<exp(3)*2^-R. For any least-essential-dimension FEI(K) violator, K>=0, deficit D>0 and actual child reserves S_i>=0, likewise max_i Inf_i<exp(3)*2^-K. For singleton minority Fourier rows e_t,q_t,c_t=4e_t(1-e_t), any lambda>=2/ln2 and any real K, define rho=(1+2^(K-lambda))^-1, r=log2(1+2^(lambda-K)), Lambda_i=sum q_t KL_2(Ber(e_t)||Ber(rho)), A_i=sum q_t[lambda e_t-j(c_t)] and O_i=Inf_i-beta_i. The exact identity D_K(f)+S_i+K O_i+Lambda_i+A_i=r holds on arbitrary roots with actual signed S_i. For a physical pair, complete product-reference row KL G_ij and conditional spectral mutual information Z_ij satisfy Lambda_i+Lambda_j+(K-lambda)(O_i+O_j)=G_ij+Z_ij, hence 2D_K+S_i+S_j+lambda(O_i+O_j)+G_ij+Z_ij+A_i+A_j=2r. The complete pair bank also obeys D_K+S_ij+G_ij+lambda I_ij-J_ij=2r, with nonnegative final channel gap; the analogous block identity has a*r. On critical witnesses all these residuals are nonnegative and minority tail mass at e_t>=u>rho is bounded by (r-D-S_i-K O_i)/(r+(K-lambda)u-h2(u)). Every proper pair of a minimal K-witness has C_ij<12 exp(3)*2^-K. These are weighted structural restrictions and exact reserve identities, not a selected-block theorem or universal FEI resolution.'
hyp=['Actual Boolean signs on finite uniform cubes; all entropies and KL in bits; zero Fourier rows omitted',
     'Physical-descendant ratio criticality requires nonconstant f and R>0; constants have zero deficit',
     'Threshold reserve positivity requires least essential dimension among all Boolean K-violators, K>=0, and proper cuts',
     'Gibbs equalities use the same K,lambda,rho at both coordinates; arbitrary roots retain actual signed child reserves',
     'lambda>=2/ln2; minority tail denominator asserted positive only for u>rho; identities permit full cuts but critical use requires proper cuts',
     'No sharp Boolean exp(3) coefficient, dimension-independent selected pair, deficit lower bound or global optimizer is assumed']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A052-CRITICAL-WEAK-INFLUENCE-GIBBS-BANK','version':1,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':digest,'contributors':['fleet05/A052'],
 'proof_source':{'path':str(ROOT/'WEAK_CRITICAL_PROOF.md'),'sha256':sha(ROOT/'WEAK_CRITICAL_PROOF.md'),'locator':'Sections1--4'},
 'proof_dependencies':dependencies,'review_records':[],'status':'AUTHOR_PROVED_SCOPED_STRUCTURAL_APPLICATION_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['claude/B11','A051','A053','A055','A002','A090','A094','B20']}
put('CLAIMS.json',[claim])
result=json.loads((ROOT/'out/CHECK.json').read_text());total=result['assertions_checker']+result['assertions_refund_library']
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B11','packet_id':'A052','gap_id':'G-R-SELECT',
 'attempt_id':'A052-critical-Gibbs-compatibility-5','method':'Critical singleton marginal entropy bound; exact Gibbs KL decomposition; compatible complete pair reference; direct Boolean/canonical prime-log certificate',
 'mathematical_delta':f'Proved max influence<exp(3)2^-R on actual physical ratio-critical sources, and threshold analog. Restored minority KL and recentring slack, merged both into one normalized pair Gibbs reference with orientation correction and full child bank. Scoped A055 rigidity review HOLDS. {total:,} exact assertions PASS.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'CRITICAL_WEAK_INFLUENCE_AND_COMPATIBLE_GIBBS_BANK_PROVED; UNIVERSAL_SELECTED_BLOCK_PAYMENT_AND_FEI_OPEN',
 'claim_versions_used':dependencies,'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'NARROW_WEIGHTED_CRITICAL_SOURCE_RESTRICTION'},review],
 'source_artifacts':['WEAK_CRITICAL_PROOF.md','REVIEW_AND_SCOPE.md','code/check_gibbs.py','code/exact_library.py','code/phase_library.py','code/refund_library.py','out/FROZEN_SPEC.json','out/FROZEN_ADDENDUM.json','out/CHECK_V1.json','out/CHECK.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Prove a proper pair has complete Gibbs KL plus actual channel gap at least2r on a genuine minimal K-witness, using compatible conditional minority tails and signed merging refunds without spending either singleton reserve twice.',
 'stagnant_substantive_attempts':0,'blockers':['No uniformly selected pair saturates the exact complete bank; weak influences and small absolute collision do not lower-bound D or child reserves','New scoped theorem awaits independent review; remote mirrors and shared adoption unverified'],
 'packet_ids':['A052']}
put('PROGRESS.json',progress);put('PACKET_DELTA.json',progress)
sources=[BASE/'BOARD.md',BASE/'claude/B11/STREAM_NOTES.md',
 Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),
 old/'SIGNED_PAIR_PROOF.md',old/'DEPENDENCY_REVIEW.md',old/'out/REVIEW_RECORDS.json',
 a55run/'REPORT.md',a55run/'PROOF.md',a55run/'CLAIMS.json',
 AGENT.parent/'A051/runs/20261014T041948Z-fleet05-A051-near-extremizer-definition/REPORT.md',
 AGENT.parent/'A051/runs/20261014T041948Z-fleet05-A051-near-extremizer-definition/RELATIVE_TRANSPORT.md',
 AGENT.parent/'A053/runs/20261014T022917Z-fleet05-A053-near-tensor-perturbations/REPORT.md']
put('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
report=f'''# exact target, quantifiers, hypotheses and units

A052/B11 stage {ROOT.name}. Seek a weighted structural restriction forced by actual physical-descendant ratio criticality and an exact relative bank on least-essential-dimension FEI(K) violators. Uniform finite Boolean cubes; entropy/KL bits. R>0 in ratio criticality; K>=0 for threshold positivity. The Gibbs identities hold even on arbitrary roots with signed child reserves. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read own STATUS, updated BOARD agent states/B11 and neighboring stream details, and full B11 STREAM_NOTES v2 (unchanged2026-10-11 23:3xZ). Protocol revision2026-10-11-execution-v2 retains the field sets read in preceding stages, reloaded by the schema checker. Read A055 stage4 REPORT and PROOF sections1--7; its CLAIMS IDs/hashes were inspected. Read A051 stage5 REPORT and RELATIVE_TRANSPORT sections1--3 excerpt, and A053 stage4 REPORT. These new admission/control constructions are consumed for mechanism scope; their entire proof chains are not represented as independently accepted. The stale lead beta target is complete; the live dependency now rules out absolute refund floors and root-only weak-influence admission. Needed A055 singleton and A051 pair scalar interfaces are the exact versions independently reconstructed in A052 stage4. No new web or paper theorem is used. Exact source hashes are in out/SOURCE_MANIFEST.json.

# complete derivation or exact first unsupported line

WEAK_CRITICAL_PROOF.md is the full proof. Actual child inequalities give R Inf_i<=L_i. Marginal conditional entropy and the reviewed channel bound give L_i<=h2(Inf_i)+(2/ln2)Inf_i. The elementary entropy bound implies Inf_i<exp(3)2^-R; the same argument applies at a minimal threshold K. This needs no virtual phase descendant. A sharp implicit scalar endpoint is also recorded, without a sharp Boolean claim.

The exact Gibbs identity restores minority KL Lambda and the row recentring slack A: D+S_i+K O_i+Lambda_i+A_i=r. Correcting minority reflections by (K-lambda)O_i merges the two singleton KLs into complete joint product-reference KL plus conditional mutual information. Hence 2D+S_i+S_j+lambda O_sum+G_pair+Z_pair+A_i+A_j=2r. The whole physical pair bank is D+S_pair+G_pair+lambda I_pair-J_pair=2r. Both are exact; all reference atoms and actual children are retained. Weighted minority tails and the pair collision bound12exp(3)2^-K follow. These are structural restrictions, not free reserves to spend twice.

First unsupported line: a uniformly selected proper pair/larger block whose complete Gibbs KL and actual channel gap exhausts its available ar bank. Weak influence and absolute smallness alone do not contradict D>0; the remaining cost must be compared with the SAME retained root/child account. The A051/A055 wrappers explicitly fail child eligibility, so their small defect is not admitted as a critical example.

# executed validation with domain, arithmetic, commands and outputs

Both specs precede execution; estimates70MB, caps55sec, no >300MB job needing memok. No GPU, background job or automatic dimension escalation. First pilot passed69,043 checks in10.730265sec and is preserved in CHECK_V1.json. A frozen addendum added the subsequently derived compatible-pair identities on the unchanged domain before the strengthened execution:

    python -X utf8 runs\\{ROOT.name}\\code\\check_gibbs.py

Final PASS: {total:,} assertions ({result['assertions_checker']:,} checker plus {result['assertions_refund_library']:,} exact refund checks), helper runtime{result['runtime_seconds']:.6f}sec. All276 Boolean tables n1,2,3;804 singleton cuts;784 pair cuts including full n2 pairs solely for identities; every proper descendant used for ratio-critical classification; five fixed point controls n4..8. All70 nonconstant small ratio-critical tables, including48 positive-ratio tables, are exactly classified;16 n3 K2 violations retain certified smaller children. These finite cases do not claim to exhibit a high-K violating witness.

Integer FWHT agrees with direct characters through n3; physical edges independently reconstruct influence. Fraction arithmetic and canonical prime-log identities exactly check KL, orientation correction, both complete pair banks, and weighted minority tails. At K4,8,16 the finite checker uses lambda=3>2/ln2 so every reference/log argument is rational; the sharper transcendental lambda=2/ln2 assertion is analytic. Forty-term atanh with proved geometric tail and outward96-bit logs certifies signs; no floating proof decision. The exp(3) influence certificate is tested as H_natural/I+ln(Inf_i)<3, avoiding numerical exponentiation. Rigidity and five point-defect formulas are checked from actual truth tables. Named critical records and rational diagnostic values are persisted in CHECK.json.

# proof dependencies and changed downstream conclusions

REVIEW_AND_SCOPE.md independently accepts A055-GLOBAL-ORIENTATION-REFUND-RIGIDITY@1 sections1--3 only (zero rigidity, dyadic floor and point formula), with no substantive repair. No full admission-chain acceptance is asserted. This consumes a live review before the narrow new structural application. The two earlier reviewed scalar interfaces remain exact accepted dependencies, recorded with source hashes; previous run files and shared indices are untouched. Source A053 acceptance of the preceding A052 full pair chain and A055/A051 scoped acceptances are consumed without inflating their scope.

Changed conclusion: every high-ratio physically critical source, not just a near-code class, is confined to exponentially weak influences. The remaining pair problem can use one normalized product reference that retains minority heterogeneity, orientation reflection cost, mutual information and physical child deficits exactly. Qualitative full support or an absolute defect floor cannot replace these weighted constraints. This changes from the closed absolute-refund mechanism to compatible relative KL ownership; it pays no universal selected-block bill.

# one next mathematical action and independent reviewer

Next: use the compatible minority-tail and joint Gibbs constraints together with exact signed merging refunds to force a proper pair with G_pair+lambda I_pair-J_pair>=2r on a genuine minimal K-witness. Such a pair contradicts D+S_pair>0 through the exact bank. Do not treat the two singleton r banks or discarded KL as independent unspent funding. Immediate consumers A051/A055/A053 and B11; independent reviewers A090/A094 should reconstruct the strict entropy bound, orientation reflection identity and both complete child ledgers. No messages were sent to others.

# actual persistence receipts or precise save blocker

All four protocol files, proof/review notes, frozen specs, code and both exact outputs are saved locally. PROGRESS/PACKET_DELTA are byte-identical; schemas, hashes and20MB cap are checked in out/ARTIFACT_MANIFEST.json. Rolling STATUS, WORKLOG and LEARNED are updated only in A052. New theorem independent review, shared adoption and external mirrors are pending; no local save blocker.

**Universal bridge:** This stage moves C019 stopping-tree payment and its C020 complete-reference interface through B11's critical-source target: it proves the dimension-free structural scale maxInf<exp(3)2^-R and replaces discarded singleton Gibbs slack by one compatible normalized pair KL bank retaining all child deficits, mutual information and orientation. Quantitatively every minimal K-witness has pair collision<12exp(3)2^-K and an exact2r bank;{total:,} exact checks validate the finite identities. No universal FEI constant improves. What remains is uniformly selecting a pair/block that exhausts that bank. NEXT uses the new weighted compatibility constraints in that precise critical contradiction, rather than another weak-root wrapper or isolated class bound.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text(f'STATE: Stage5 complete: critical maxInf<exp(3)2^-R; exact compatible singleton/pair Gibbs KL banks; {total:,} exact checks PASS; scoped rigidity reviewed; FEI OPEN.\nNEXT: Force a critical-witness pair to exhaust its complete2r Gibbs/channel bank using weighted minority tails and signed refunds; A090/A094 review pending.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} {ROOT.name}: read new absolute-floor/admission obstructions; scoped A055 rigidity review HOLDS. Derived physical-ratio-critical maxInf<exp(3)2^-R and exact Gibbs KL slack/tail bank, then compatible whole-pair normalized reference via actual orientation reflection correction. Frozen strengthened repeat on same281-function domain passed{total:,} checks in{result["runtime_seconds"]:.6f}s. No full FEI, selected-pair price or high-K computed witness claimed.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage5: genuine physical ratio criticality forces every influence<exp(3)2^-R, because R*d<=L<=h2(d)+(2/ln2)d. Exact singleton Gibbs bank includes minority KL and recentring slack. Actual conditional inclusion KL differs from minority KL by (K-lambda)O; thus both conditional references merge into joint complete Gibbs KL plus conditional MI. Complete pair bank D+S_pair+G_pair+lambda I_pair-J_pair=2r retains one physical budget. Absolute weak influences and small refunds remain insufficient; selection must exhaust the SAME bank, not spend either singleton r twice.\n')
protocol=json.loads(sources[2].read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert all(x in report for x in protocol['required_per_run']['report_fields'])
receipts=[]
for f in ROOT.rglob('*'):
    if f.is_file() and '__pycache__' not in f.parts:
        assert f.stat().st_size<20*1024*1024
        receipts.append({'path':str(f.relative_to(ROOT)),'sha256':sha(f),'bytes':f.stat().st_size})
put('out/ARTIFACT_MANIFEST.json',{'status':'PASS','schema_checks':'PASS','files':receipts})
print(json.dumps({'status':'SAVED_SCHEMA_HASH_CHECKS_PASS','files':len(receipts),'assertions':total,'claim_sha256':digest}))
