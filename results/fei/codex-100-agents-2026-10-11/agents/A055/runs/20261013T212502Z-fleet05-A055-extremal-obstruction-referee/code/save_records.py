from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
TEAM=Path(r'~\brain_workers\FEI100_20261011')
CANON=Path(r'~\mop_fei100\reports\fei-2026-10-11')
PROTOCOL=json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
STAMP=datetime.now(timezone.utc).isoformat()

def write(name,obj):
    payload=json.dumps(obj,indent=2,ensure_ascii=False)+'\n'
    assert len(payload.encode('utf-8'))<20*1024*1024
    (ROOT/name).write_text(payload,encoding='utf-8')
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

statement=('For every fixed nonconstant uniform-cube Boolean sign g, h=(1-g)/2, c=1-Eg, and F_r=1+1_(y=0)(g-1), the proper positive-influence block minimum phi(F_r) converges to lambda(g)=min(4,min_(nonempty B subset data,I_B(g)>0) Lambda_B(h)/E_B(h)), with the explicit uniform error in DERIVATION (7); the data block B may be all data. Every mixed block obeys the exact compressed physical restriction identities (1)--(4), including growing control subsets. A control singleton with d=2^-r c has B_i=2d-2d^2+Phi((1-d)^2,d^2), beta_i=min(d,1-d), and L_i=4d+A(d)-A(2d)/2, so its actual normalized decrement tends to 4 and its R2 upper price tends to 2+2/ln2. Exact shifted-empty-row data singleton identities are (11). For every nonconstant seed f, its C013 family g_m=z*f^(tensor m), r_m=ceil(2log2(m+1)), has phi(F_m)->0 although H(F_m)/I(F_m)->H(f)/I(f); its balancing-bit R2 price is bounded explicitly by (12)--(13) and eventually fails every fixed violated positive threshold C. Terminal entropy 2^-r_m*m*H(f) and influence 2^-r_m*m*I(f) remain unpaid. For the explicit three-bit point-defect seed and C=2, r=1 passes all root singleton averaged-decrement and R2 inequalities but the balancing-plus-control block fails, with phi=2; individual child criticality already fails at r=1. At r=2 both balancing and control singleton R2 inequalities fail by certified positive gaps. This is an activation criticality obstruction and a closed rarity limit, not a universal paid block rule or full FEI result.')
new={
 'claim_id':'A055-RARE-ACTIVATION-BLOCK-LIMIT','version':1,
 'exact_statement':statement,
 'hypotheses':['Uniform physical cubes; actual Boolean signs; entropy in bits','g nonconstant on a fixed n>=1 cube; c=1-Eg>0; r>=1; phi uses nonempty proper physical blocks with positive influence','Lambda_B(h) is the raw-indicator entropy decrement and E_B(h)=I_B(g)/4; zero log terms use continuity','For the diagonal C013 limit, f fixed and nonconstant; r_m and g_m exactly as stated; no assumed unbounded-ratio seed','The first-failure boundary refers only to the named seed, C=2, and r=1,2; averaged and individual descendant tests are distinguished'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A055/fleet05'],
 'proof_source':{'path':str(ROOT/'DERIVATION.md'),'sha256':digest(ROOT/'DERIVATION.md'),'locators':'sections 1--6; CRITICAL_CLASS_EMBEDDINGS.tex; out/FULL_SUMMARY.json; out/REPLAY.json; out/FIRST_FAILURE.json'},
 'proof_dependencies':[], 'review_records':[],
 'status':'SOURCE_COMPLETE_ANALYTIC_PROOF_AND_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],
 'refutes':['Unversioned surrogate: C013 arbitrary-seed preserving activations are themselves hard proper-block descent obstructions','Unversioned admission shortcut: passing all root singleton averaged criticality/R2 inequalities certifies every individual proper child'],
 'first_unproved_line':None,
 'next_consumers':['A001','A005','A021','A027','A028','A051','A052','A053','A090','A094','B11-lead','B20']}

q51=TEAM/'agents/A051/runs/20261011T233123Z-fleet05-A051-near-extremizer-definition/CLAIMS.json'
r51=next(x for x in json.loads(q51.read_text(encoding='utf-8')) if x['claim_id']=='A051-PROPER-BLOCK-DESCENT-SQUEEZE')
r51['review_records']=r51['review_records']+[{'reviewer':'A055/fleet05','verdict':'ACCEPT_AT_STATED_SCOPE','review_source':str(ROOT/'REVIEWS.md'),'method':'Independent co-singleton physical-edge and finite-optimizer reconstruction; no acceptance of separate NAND certificate claim','contributor_repair':False}]
r51['status']='INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE_PENDING_REGISTRY_ADOPTION'
q52=TEAM/'agents/A052/runs/20261012T003906Z-fleet05-A052-critical-source-structure/CLAIMS.json'
r52=json.loads(q52.read_text(encoding='utf-8'))[0]
r52['review_records']=r52['review_records']+[{'reviewer':'A055/fleet05','verdict':'ACCEPT_ANALYTIC_SUBSTATEMENT_ONLY','accepted_scope':'Distributional superadditivity, singleton and cap minimum equalities, explicit tensor obstruction constructions','unreviewed_scope':'All bundled 1150 NAND and seven seed/hybrid finite decisions','review_source':str(ROOT/'REVIEWS.md'),'method':'Independent chain-rule/Jensen reconstruction and exact tensor reasoning','contributor_repair':False}]
# Do not promote the entire finite-plus-analytic bundle from a partial review.
claims=[r51,r52,new]
write('CLAIMS.json',claims)

verdicts={
 'units':'bits',
 'fixed_core_activation':{'preserved':['Actual Booleanity','All labelled core blocks and all control-cardinality blocks enumerated exactly','Raw-indicator rare-block limiting law'],'resolved_limit':'lambda(g)=min(4,min_B Lambda_B(h)/E_B(h))','ratio_limit':'H(F_r)/I(F_r)->4 for fixed nonconstant g','unresolved':'A universally paid raw-indicator/joint-channel bound on genuinely critical sources'},
 'C013_diagonal_activation':{'preserved':['Arbitrary seed ratio in the diagonal limit','I(F_m)->0','Rare negative output','Exact terminal seed entropy and influence'],'violated':['Genuine all-descendant threshold criticality for any violated fixed C>0, eventually already at the balancing R2 singleton'],'quantitative':'phi(F_m)<=u_m->0; exposed terminal deficit equals p_m*m*D_C(seed)','scope':'Cheap root block does not certify the arbitrary terminal core'},
 'control_singleton':{'actual_price_limit':'4','R2_upper_price_limit':'2+2/ln2','excess':'2/ln2-2','scope':'Upper surrogate and actual decrement are different'},
 'named_C2_boundary':{'seed':'three-bit point defect, balanced by z','r1':'All root singleton averaged and R2 tests pass; mixed z/control block fails; phi=2; individual singleton child already violates C','r2':'Both balancing and control root R2 inequalities fail with certified gaps','scope':'No universal ordering of blocks or descendants claimed'},
 'universal_status':'FULL_FEI_OPEN'}
write('EXTREMAL_SCOPE_VERDICTS.json',verdicts)

progress={
 'protocol_revision':PROTOCOL['revision'],'run_id':ROOT.name,'stream':'B11','packet_id':'A055',
 'gap_id':'G-B11-CRITICAL-CLASS-ADMISSION','attempt_id':'A055-stage2-rare-block-limit',
 'method':'Exact mixed-block activation compression, uniform raw-indicator entropy remainder, centered singleton pair prices, C013 balancing descent, exact certified finite replay and scoped independent reviews',
 'mathematical_delta':'Closed the all-proper-block fixed-core rarity limit with an explicit uniform error; proved phi->0 for arbitrary-seed preserving C013 wrappers; separated actual control price 4 from R2 price 2+2/ln2; certified a mixed-block failure missed by every root singleton test at r=1; retained terminal arbitrary-seed deficit',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF',
 'mathematical_status':'SCOPED_ACTIVATION_TARGET_PROVED;_NEW_CLAIM_REVIEW_PENDING;_UNIVERSAL_PROPER_BLOCK_PAYMENT_AND_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A051-PROPER-BLOCK-DESCENT-SQUEEZE','version':1,'use':'Independent analytic review and interpretation; not a premise of the activation limit'},{'claim_id':'A052-OPTIMAL-RECENTRING-SINGLETON-COLLAPSE','version':1,'use':'Independent analytic substatement review; finite count acceptance not claimed'},{'claim_id':'CLAUDE-B11-R2','version':1,'use':'Necessary criticality interface independently rederived from elementary scalar/physical identities in REVIEWS.md'}],
 'claims_created_or_changed':[{'claim_id':new['claim_id'],'version':1,'change':'New scoped activation limit, singleton ledger and diagonal obstruction'},{'claim_id':r51['claim_id'],'version':1,'change':'Local independent full analytic acceptance record'},{'claim_id':r52['claim_id'],'version':1,'change':'Local analytic-only acceptance record; full bundled status unchanged'}],
 'source_artifacts':['REPORT.md','DERIVATION.md','CRITICAL_CLASS_EMBEDDINGS.tex','EXTREMAL_SCOPE_VERDICTS.json','REVIEWS.md','out/FULL_SUMMARY.json','out/FULL_CERTIFICATES.json','out/cases/','out/REPLAY.json','out/FIRST_FAILURE.json','out/FROZEN_SPEC_V3.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':new['next_consumers'],
 'next_action':'Consume A052 NAND case 0006 mask 48 and separate actual joint-channel cancellation from the singleton surrogate while retaining individual terminal deficits; seek fixed-K payment on genuinely child-certified sources',
 'stagnant_substantive_attempts':0,'blockers':[], 'packet_ids':['A055']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)

validation={name:json.loads((ROOT/'out'/name).read_text(encoding='utf-8')) for name in ['PILOT_SUMMARY.json','FULL_SUMMARY.json','REPLAY.json','FIRST_FAILURE.json','FULL_V2_ABORTED.json']}
validation['successful_full_assertions']=sum(validation[x]['assertions'] for x in ['FULL_SUMMARY.json','REPLAY.json','FIRST_FAILURE.json'])
write('out/VALIDATION_SUMMARY.json',validation)

sources=[CANON/'EXECUTION_PROTOCOL.json',CANON/'CURRENT_STATUS.md',TEAM/'BOARD.md',TEAM/'claude/B11/STREAM_NOTES.md',q51,q52]
sources += [TEAM/'claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring'/name for name in ['REPORT.md','CLAIMS.json']]
sources += [TEAM/'agents/A051/runs/20261011T233123Z-fleet05-A051-near-extremizer-definition'/name for name in ['REPORT.md','UNIVERSAL_DESCENT_SQUEEZE.md']]
sources += [TEAM/'agents/A052/runs/20261012T003906Z-fleet05-A052-critical-source-structure'/name for name in ['REPORT.md','SINGLETON_COLLAPSE.md']]
sources += [TEAM/'agents/A053/runs/20261012T014744Z-fleet05-A053-near-tensor-perturbations'/name for name in ['REPORT.md','CLAIMS.json']]
sources += [AGENT/'runs/20261011T230118Z-fleet05-A055-extremal-obstruction-referee'/name for name in ['EMBEDDING_PROOF.md','REVIEW_A053.md','out/SOURCE_MANIFEST.json']]
manifest=[{'path':str(path),'bytes':path.stat().st_size,'sha256':digest(path),'scope':'Source locators in REPORT.md; no remote readback asserted'} for path in sources]
write('out/SOURCE_MANIFEST.json',{'local_sources':manifest,'baseline_paper_provenance':'Retained from prior A055 manifest; no new remote paper audit claimed'})

claim_fields=set(PROTOCOL['required_per_run']['claim_fields'])
for claim in claims:assert set(claim)==claim_fields
progress_fields={'packet_ids' if x.startswith('packet_ids (') else x for x in PROTOCOL['required_per_run']['progress_fields']}
assert set(progress)==progress_fields
assert json.loads((ROOT/'PACKET_DELTA.json').read_text(encoding='utf-8'))==progress
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in PROTOCOL['required_per_run']['report_fields']:assert '# '+field in report
assert report.rstrip().split('\n')[-1].startswith('This stage moves')

(AGENT/'STATUS.md').write_text('STATE: A055 stage 2 complete: all-block rare limit, C013 phi->0 with terminal seed debt, exact R2/actual first-failure boundary; 126794 assertions PASS; new review pending, full FEI OPEN.\nNEXT: A090/A094 review; use A052 NAND case 0006 mask 48 for terminal-inclusive joint-channel cancellation on genuinely child-certified sources.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+STAMP+': Stage 20261013T212502Z: consumed board/B11 v2 and A051--A053 corrections; independently accepted A051 squeeze and analytic-only A052 collapse. Derived the all-block rare-activation raw-indicator limit with uniform remainder and C013 phi->0 through the balancing singleton. Closed exact C=2 boundary: r1 root singleton averages pass but mixed tag block fails; individual child already violates. r2 singleton/R2 tests detect failures. Repaired lost ln2 interval correlation, stopped expensive repetitive v2 large-r sweep at last checkpoint 720 roots/284.19 seconds, and froze a smaller v3 validation domain. Full/replay/boundary passed 126794 assertions. Saved all protocol files and terminal-inclusive gap.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nFor fixed nonconstant g, rare activation phi tends to min(4,min_B Lambda_B((1-g)/2)/E_B((1-g)/2)); data B may be all core bits. The limit needs a uniform argument for growing control block size, not just fixed-k expansion. In the amplified C013 family z*f^m, phi->0 because the balancing Bayes error is p*(Ef)^(2m), while H/I still retains the seed. Terminal entropy p*mH(f) and influence p*mI(f) remain unpaid. A control singleton has actual limiting price 4 but R2 upper price 2+2/ln2. Root averaged singleton tests can all pass while an individual singleton child already violates: the C2 balanced point-defect example at r1 has exact phi2 and mixed-tag failure. Collect powers of two exactly before rigorous log interval evaluation at very small p; separately bounding nearly equal logs loses their common ln2 correlation.\n')

receipts=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and path.name!='RECEIPTS.json':
        assert path.stat().st_size<20*1024*1024
        receipts.append({'path':str(path.relative_to(ROOT)),'bytes':path.stat().st_size,'sha256':digest(path)})
write('out/RECEIPTS.json',{'saved_at_utc':STAMP,'protocol_field_sets':'PASS','artifact_sizes':'PASS_ALL_UNDER_20_MB','artifact_hashes':receipts,'rolling_files':[{'path':str(AGENT/name),'sha256':digest(AGENT/name)} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']],'supervisor_copy':'PENDING_NOT_CLAIMED','mirror_verification':'PENDING_NOT_CLAIMED','new_claim_independent_review':'PENDING'})
print(json.dumps({'status':'PASS','protocol_field_sets':'PASS','claims':len(claims),'saved_artifacts':len(receipts),'successful_full_assertions':validation['successful_full_assertions']},indent=2))
