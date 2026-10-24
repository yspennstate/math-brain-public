import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
source=AGENT.parent/'A051/runs/20261013T215311Z-account05-A051-near-extremizer-definition'
dep=json.loads((source/'CLAIMS.json').read_text())[0]
statement='Let K>=0 and let f be a least-essential-dimension Boolean violation D_K(f)=H(f)-K I(f)>0 of uniform-cube FEI(K). For every nonempty proper physical block A of a coordinates, let w_t be the retained child Fourier row, q_t=E w_t^2, z_t=w_t^2/q_t on positive rows, c_t=E(z_t-1)^2, C_A=sum_t q_t c_t and Gamma_A=sum_t q_t log2(1+c_t). Then C_A>0: identical squared spectra of all physical children are impossible. More quantitatively set h_t=sign(w_t), sign(0)=1, eta_t=min(1,||w_t/sqrt(q_t)-h_t||_2), eta=sum_t q_t eta_t. With psi_a(s)=h2(s)+s log2(2^a-1) up to s=1-2^-a and psi_a(s)=a thereafter, D_K(f)<=Gamma_A+psi_a(eta)+K a eta. Since eta<=sqrt(C_A), if C_A<=1/4 then D_K(f)<=log2(1+C_A)+h2(sqrt(C_A))+sqrt(C_A) log2(2^a-1)+K a sqrt(C_A). This uses FEI(K) on actual Boolean row phases of smaller dimension, not an assumption that phases are physical descendants. Nonstrict physical-descendant ratio criticality alone does not imply C_A>0, as witnessed by a product of two quadratic two-bit signs. No uniform K or FEI resolution follows.'
hyp=['All functions are actual Boolean signs on finite uniform cubes; entropy in bits',
     'Dimension minimality is among all Boolean K-violators, measured in essential coordinates',
     'A is nonempty and proper; zero-q rows omitted; K>=0',
     'For the quantitative square-root bound only, C_A<=1/4',
     'No full FEI theorem, all-dimensional optimizer or physical realization of row phases is assumed']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
review={'claim_id':dep['claim_id'],'version':dep['version'],'statement_sha256':dep['statement_sha256'],
        'reviewer':'A052','verdict':'HOLDS_AT_EXACT_STATED_SCOPE','review_source':str(ROOT/'REVIEW_A051.md'),
        'review_sha256':sha(ROOT/'REVIEW_A051.md'),'supplied_substantive_repair':False,
        'validation':str(ROOT/'out/CHECK.json'),'registry_adoption':'NOT_CLAIMED'}
put('out/REVIEW_RECORDS.json',[review])
claim={'claim_id':'A052-CRITICAL-BOOLEAN-PHASE-EXCLUSION','version':1,'exact_statement':statement,'hypotheses':hyp,
       'statement_sha256':digest,'contributors':['account05/A052'],
       'proof_source':{'path':str(ROOT/'CRITICAL_PHASE_PROOF.md'),'sha256':sha(ROOT/'CRITICAL_PHASE_PROOF.md'),'locator':'Sections 1--3'},
       'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_SCOPED_APPLICATION_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],'refutes':['A least-essential-dimension fixed-threshold FEI violator can have an isospectral proper block'],
       'first_unproved_line':None,'next_consumers':['claude/B11','A051','A053','A055','A018','A090','A094','B20']}
put('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B11','packet_id':'A052','gap_id':'G-R-SELECT',
 'attempt_id':'A052-critical-Boolean-phase-3','method':'Independent collision-interface review; lower-dimensional Boolean row-phase induction; entropy continuity and exact direct-character certificates',
 'mathematical_delta':'Independently accepts A051 joint-collision descent v1. Proves every dimension-minimal K-violator has positive collision on every proper block, and a quantitative near-isospectral deficit bound. Separates physical ratio criticality from dimension minimality by an exact essential four-bit tensor witness. 69,395 exact checks PASS.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_PHASE_RESTRICTION_PROVED; UNIVERSAL_BLOCK_SELECTION_AND_FULL_FEI_OPEN',
 'claim_versions_used':[review],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'SCOPED_CRITICAL_PHASE_APPLICATION'},review],
 'source_artifacts':['CRITICAL_PHASE_PROOF.md','REVIEW_A051.md','code/check_phase.py','code/exact_library.py','out/CHECK.json','out/NAND48.json','out/FROZEN_SPEC.json','out/FROZEN_SPEC_V2.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Seek a proper block on dimension-minimal K-witnesses whose signed collision plus Boolean-phase approximation error is below D_K(f), with row mass and complete terminal deficits retained; start from small-collision rows rather than repeat the solved NAND root.',
 'stagnant_substantive_attempts':0,
 'blockers':['The near-phase error grows with block size and K; no dimension-independent selection/payment bound is proved','Independent review of the new scoped phase application and external adoption remain pending'],
 'packet_ids':['A052']}
put('PROGRESS.json',progress);put('PACKET_DELTA.json',progress)
sources=[source/'REPORT.md',source/'CLAIMS.json',source/'JOINT_CHANNEL_PROOF.md',source/'out/CONTROL_NAND6_case0006.json',
 AGENT.parent/'A018/runs/20261011T221538Z-account05-A018-shared-data-collision-law/REPORT.md',
 AGENT.parent/'A053/runs/20261012T014744Z-account05-A053-near-tensor-perturbations/REPORT.md',
 AGENT.parent.parent/'BOARD.md',AGENT.parent.parent/'claude/B11/STREAM_NOTES.md',
 Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),
 AGENT/'runs/20261012T003906Z-account05-A052-critical-source-structure/code/recentred_census.py',
 AGENT/'runs/20261012T003906Z-account05-A052-critical-source-structure/PROGRESS.json',
 AGENT/'runs/20261012T003906Z-account05-A052-critical-source-structure/out/WITNESS_SUMMARY.json']
put('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
result=json.loads((ROOT/'out/CHECK.json').read_text())
report=f'''# exact target, quantifiers, hypotheses and units

A052/B11 stage {ROOT.name}. All-dimensional target: a structural restriction on least-essential-dimension fixed-K Boolean FEI violations under every proper physical cut. Entropies are in bits; K>=0. Full FEI is OPEN. Physical-descendant ratio criticality is a weaker hypothesis and is kept separate.

# sources actually read, revisions and theorem locators

Read the full execution protocol revision 2026-10-11-execution-v2, current BOARD (2026-10-13 22:15 UTC), own STATUS and preceding stage outputs, and B11 STREAM_NOTES v2 (2026-10-11 23:3xZ). The lead's old beta-composition target was completed last stage. New A051 stage3 JOINT_CHANNEL_PROOF sections1--5, REPORT, CLAIMS and NAND control are read and independently reconstructed. A018 baseline REPORT's row classification and zero-channel guard were read; A053 stage2 REPORT's continuity/individual-child scope was consulted, not adopted as a proof premise. Those report reads were partial tool views, not audits of their full proof chains. No new paper or web result is needed. Exact consulted source hashes are in out/SOURCE_MANIFEST.json.

# complete derivation or exact first unsupported line

CRITICAL_PHASE_PROOF.md gives a complete elementary proof. Zero row collision turns normalized rows into actual Boolean signs on the queried block. Minimality among all Boolean K-violators permits FEI(K) on those phases, pricing B_A<=K I_A; physical children price the terminal deficit. This rules out every isospectral proper block. The near-phase proof bounds Fourier-law TV by modulus error, applies an explicitly proved maximal-coupling entropy inequality and influence range bound, and concludes D_K<=Gamma+psi_a(eta)+Ka eta, with eta<=sqrt(C_A). The explicit small-C inequality is saved in the proof. No phase is assumed to be a physical descendant. A four-bit quadratic tensor has all physical child ratios<=2 and a zero-channel full-factor block; the weaker ratio-critical exclusion is false.

First unsupported line: a dimension-independent K and a rule selecting a proper block whose collision plus phase-error budget is below D_K(f), or directly B_A+Gamma_A<=K I_A, on every dimension-minimal K-witness. The error currently depends on a,K and can dominate the deficit. Positive collision alone is not payment.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede both executions; estimates60MB and maximum55 seconds, no >300MB job or memok requirement. The initial spec erroneously counted 278 small tables/280 total; the corrected v2 spec states 276 small/278 total. The original is preserved, the actual domain never changed. v2 added quantitative phase-lemma tests after the first successful pilot.

    python -X utf8 runs\\{ROOT.name}\\code\\check_phase.py

Completed final v2: {result['assertions']:,} assertions, {result['runtime_seconds']:.6f} seconds helper runtime; all276 Boolean tables n=1,2,3, 1552 proper cuts of nonconstant tables;62 named NAND cuts;14 four-bit tensor cuts. All16 three-bit K=2 violations have every smaller child at or below K and positive collision at all96 proper cuts. Direct character sums and physical edge counts reconstruct Walsh/influence independently of A051 code. Fraction arithmetic verifies signed convolution identities and rational squared TV/modulus inequalities, avoiding square roots. Entropy signs use 40-term atanh tails with 96-bit outward rational enclosures. Every row entropy-continuity and influence-error inequality is checked exactly. No floating-point sign is accepted. The initial v1 pilot passed45,876 checks in2.401567 seconds; its stdout was returned, while CHECK.json was replaced by the successful strengthened v2 output.

NAND48.json independently matches the exact H,B,J,Gamma source vectors and truth hash; unique collision-affordable mask48 and singleton costs>3.19 are checked. Its sole nonconstant child has positive root-ratio deficit. This child prevents classifying the root as critical; it is retained throughout.

# proof dependencies and changed downstream conclusions

REVIEW_A051.md and out/REVIEW_RECORDS.json independently accept {dep['claim_id']}@1 at its exact stated scope; no substantive repair was supplied. Global adoption is not claimed. The new phase proof rederives its needed entropy, restriction and collision facts and has no pending theorem dependency. A051's analytic review of the previous A052 collapse is now consumed from its source; no duplicate collapse search is run. The stream cap is respected by reviewing a live source-complete candidate before this narrowly scoped application. Source registry pending candidates are not silently relabelled.

Changed downstream conclusion: zero-channel arbitrary-phase obstructions are excluded specifically on dimension-minimal threshold witnesses, even though they remain valid against unconditional prescribed-block payment and against physical ratio criticality alone. This is why criticality improves the argument without reviving component pruning: all lower-dimensional Boolean phases are available only under the stronger, explicitly named minimality hypothesis. The robust bound records the exact price for leaving that zero-channel boundary.

# one next mathematical action and independent reviewer

Next: select a proper block on a dimension-minimal K-witness with sufficiently small signed collision and Boolean-phase approximation error to contradict the saved deficit bound, keeping row masses and terminal deficits. A051/A055 and B11 lead are immediate consumers; A090/A094 should independently reconstruct the norm-to-TV bound, concave entropy cap, and distinction between essential-dimension minimality and physical descendants. No outbound messages were sent.

# actual persistence receipts or precise save blocker

The four protocol files, two proof/review notes, code and exact outputs are saved in this run. PROGRESS and PACKET_DELTA are byte-identical. out/ARTIFACT_MANIFEST.json checks hashes, field sets and the20MB cap. Rolling STATUS, WORKLOG and LEARNED are updated only in A052. External mirrors, registry adoption and review of the new phase theorem are pending, not claimed.

**Universal bridge:** This stage moves C019 stopping-tree payment through B11's critical block-selection target: it independently admits the signed-collision interface, then excludes all exactly isospectral proper blocks of a least-dimensional threshold violation by paying their Boolean row phases and preserving child deficits. The quantitative advance is the explicit deficit bound Gamma+psi_a(eta)+Ka eta, checked at69,395 finite assertions; no universal constant improves. What remains is a dimension-independent selection/payment bound for the nonzero-collision remainder. NEXT targets that exact critical-source implication rather than another isolated class result, because a uniform contradiction to the minimal-witness deficit would settle full FEI.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: Stage 3 complete: A051 collision claim independently accepted; dimension-minimal K-violators have no isospectral proper block; quantitative phase bound; 69,395 exact checks PASS; FEI OPEN.\nNEXT: Select a critical-witness block with signed collision plus Boolean-phase error below its deficit; A090/A094 review pending.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} Stage3 {ROOT.name}: consumed A051 joint certificate rather than duplicate it; independent analytic and direct-character review HOLDS. Derived lower-dimensional Boolean-phase zero-channel exclusion and robust deficit bound. Exhaustive n<=3 + NAND6 + quadratic tensor:69,395 exact assertions PASS. Initial frozen count typo disclosed/corrected before strengthened repeat; no domain change. Full FEI remains open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage3 durable lesson: dimension minimality among ALL Boolean K-violators licenses actual Boolean row phases on every smaller queried block. Thus an isospectral proper block cannot occur in a minimal K-violation. Physical-descendant ratio criticality alone does not license these phases; equal-ratio quadratic tensors refute that stronger claim. Near phases give D_K<=Gamma+psi_a(eta)+Ka eta, eta<=sqrt(weighted row chi-square). The error is dimension/threshold dependent; no universal selection follows. A051 joint collision v1 independently accepted at its exact scoped statement.\n')
protocol=json.loads(sources[8].read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert all(h in report for h in protocol['required_per_run']['report_fields'])
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and '__pycache__' not in p.parts:
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size})
put('out/ARTIFACT_MANIFEST.json',{'status':'PASS','schema_checks':'PASS','file_count':len(receipts),'files':receipts})
print(json.dumps({'status':'SAVED_SCHEMA_CHECKS_PASS','claim_sha256':digest,'reviewed_claim_sha256':dep['statement_sha256'],'files':len(receipts)}))
