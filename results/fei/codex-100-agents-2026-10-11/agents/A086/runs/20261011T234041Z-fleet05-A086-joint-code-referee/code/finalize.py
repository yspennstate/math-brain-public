from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1]; AGENT=RUN.parents[1];TEAM=AGENT.parents[1];OUT=RUN/'out'
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
PREV=AGENT/'runs/20261011T214823Z-fleet05-A086-joint-code-referee'
now=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def shastatement(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
protocol=json.loads((BASE/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
originals={
 'A003':TEAM/'agents/A003/runs/20261011T221324Z-fleet05-A003-minimal-target-formulation',
 'A007':TEAM/'agents/A007/runs/20261011T215236Z-fleet05-A007-root-normalization',
 'A008':TEAM/'agents/A008/runs/20261011T221357Z-fleet05-A008-gate-label-compression',
 'A012':TEAM/'agents/A012/runs/20261011T215648Z-fleet05-A012-sparse-activation-accounting'}
inputs=[TEAM/'BOARD.md',TEAM/'claude/B18/STREAM_NOTES.md',AGENT/'STATUS.md',BASE/'EXECUTION_PROTOCOL.json',BASE/'source_material/reductions/paper/forests.tex',SUP/'SEED_LEMMAS.md',SUP/'sources/ERASURE_REDUCTION.md',PREV/'JOINT_CODE_REVIEW.md',PREV/'out/SOURCE_MANIFEST.json']
for folder in originals.values():inputs+=list(folder.glob('*.md'))+list(folder.glob('*.tex'))+[folder/'CLAIMS.json']
manifest=[]
for p in inputs:
    data=p.read_bytes()
    try:data.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:data.decode('cp1252');enc='cp1252'
    manifest.append({'path':str(p),'bytes':len(data),'sha256':sha(p),'encoding':enc})
previous=json.loads((PREV/'out/SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
forest=BASE/'source_material/reductions/paper/forests.tex'
old=next(m for m in previous if m['path']==str(forest))
assert old['sha256']==sha(forest),'Reused forest dependency changed'
save(OUT/'SOURCE_MANIFEST.json',manifest)
claims=[];used=[]
for packet,folder in originals.items():
    original=folder/'CLAIMS.json'
    for claim in json.loads(original.read_text(encoding='utf-8')):
        canonical=shastatement(claim)
        statement_only=hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
        assert claim['statement_sha256'] in [canonical,statement_only],claim['claim_id']
        hash_convention='canonical statement+hypotheses' if claim['statement_sha256']==canonical else 'statement text only'
        claim['review_records'].append({'reviewer':'A086/fleet05','at':now,'verdict':'HOLDS_AT_STATED_SCOPE','source':str(RUN/'JOINT_CODE_REVIEW.md'),'source_sha256':sha(RUN/'JOINT_CODE_REVIEW.md'),'method':'Independent analytic reconstruction of complete originals, independent integer Walsh/Fraction and rigorous rational-log normalizer, prefix, admission and composition checks.','source_claims_sha256':sha(original),'source_statement_hash_convention':hash_convention,'canonical_statement_hypotheses_sha256':canonical,'repair_contribution':False})
        claim['status']='INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE'
        claim['proof_source']={'original':claim['proof_source'],'original_claims_path':str(original),'original_claims_sha256':sha(original),'review':str(RUN/'JOINT_CODE_REVIEW.md')}
        claims.append(claim);used.append({'claim_id':claim['claim_id'],'version':claim['version'],'status':'HOLDS_AT_STATED_SCOPE'})
derived={'claim_id':'A086-ACTIVATION-REFERENCE-DEBT-PROJECTION','version':1,
 'exact_statement':'For every balanced finite uniform Boolean core g and every r>=1, put p=2^-r,F=1+A_r(g-1),v=p(2-p),Pplus=P_F conditioned on nonempty output. For every subprobability reference Q positive on the support of Pplus, let M=sum Q,q=Q/M,beta=1/(2-p),gamma=q(data spectral set nonempty),and q_g=q(data set | nonempty data). Then vD(Pplus||Q)=-v log2 M+vD_Ber(beta||gamma)+pD(P_g||q_g)+v(1-beta)D(Unif(nonempty control subsets)||q(control | empty data))+p sum_T P_g(T)D(Unif(all control subsets)||q(control | data T)). Consequently vD(Pplus||Q)>=pD(P_g||q_g). Infinite missing-support debt is interpreted in the extended sense. This localizes complete reference debt, without asserting cheap universal references or a lower bound by seed entropy.',
 'hypotheses':['balanced actual Boolean core on a finite uniform data cube','fresh independent r>=1 point controls','base-two entropy and divergence','Q is a complete nonempty-output subprobability positive on target support','conditionals defined in finite-debt case; data reference may have additional support'],
 'statement_sha256':'','contributors':['A086/fleet05'],
 'proof_source':{'path':str(RUN/'ACTIVATION_DEBT_PROJECTION.md'),'validation':str(OUT/'BRIDGE_RESULTS.json')},
 'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A003','A005','A007','A008','A011','A012','A089','A094','A096','B20']}
derived['statement_sha256']=shastatement(derived);claims.append(derived)
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
save(RUN/'CLAIMS.json',claims)
gap={'universal_bridge':'C020','full_fei_status':'OPEN','original_verdicts':used,
 'gaps':[
 {'gap_id':'G-J-COST','exact_first_unsupported_line':'For every Boolean seed, construct one globally fixed admissible complete structural reference and bound its entire spectral expected cost by an absolute multiple of original physical influence.','status':'OPEN'},
 {'gap_id':'G-J-ACTIVATED-DATA-REFERENCE','exact_first_unsupported_line':'For a proposed A003 forest envelope or A008 dictionary on g_t=z product f, exhibit the induced nonempty-data law q_g_t and pay p_t D(P_g_t||q_g_t) together with sector, control and normalization debt.','status':'OPEN_CONSTRUCTION_AND_PAYMENT','consumers':['A003','A008','A089','A096'],'retained_quantities':['actual p_t','core tH(f)','core tI(f)+1','v_t and reference mass','complete codebook','remaining conditional KL terms']},
 {'gap_id':'G-J-PHYSICAL-LABEL','exact_first_unsupported_line':'Erase or avoid the control-first physical leaf label before claiming influence payment on activated literal. Its posterior lower bound tends to two bits.','status':'SOURCE_OBSTRUCTION_ACCEPTED','consumers':['A011','A012']},
 {'gap_id':'A086-PROJECTION-REVIEW','exact_first_unsupported_line':'Independent acceptance of the new projection identity has not yet occurred.','status':'INDEPENDENT_REVIEW_PENDING','consumers':['A094','A085']}],
 'no_original_source_error_found':True,'a011_original_remains_accepted_under_its_admission':True}
save(RUN/'JOINT_CODE_GAPS.json',gap)
main=json.loads((OUT/'EXACT_RESULTS.json').read_text(encoding='utf-8'));proj=json.loads((OUT/'BRIDGE_RESULTS.json').read_text(encoding='utf-8'))
assert main['failures']==proj['failures']==0
assert main['seconds']<60 and proj['seconds']<60
total=main['assertions']+proj['assertions'];assert total==119345
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B18','packet_id':'A086','gap_id':'G-J-COST','attempt_id':'A086-JOINT-CODE-INDEPENDENT-RECONSTRUCTION-2','method':'Independent complete-source proof reconstruction, exact code/normalizer/admission checks, conditional-KL localization of activated core debt',
 'mathematical_delta':'Five original v1 claims independently accepted at stated scopes. New all-dimensional exact activation-reference debt projection exposes p D(P_g||q_g). Final exact checks: 119345 assertions, no failures. No universal constant improved.',
 'deliverable_status':'COMPLETE_LOCAL_LEAD_DIRECTED_REVIEW','mathematical_status':'FIVE_ORIGINAL_CLAIMS_REVIEWED_ONE_DERIVED_INTERFACE_PENDING_REVIEW_FULL_FEI_OPEN','claim_versions_used':used,
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'new author-proved interface' if c is derived else 'local independent review; statement unchanged'} for c in claims],
 'source_artifacts':[{'path':str(RUN/'JOINT_CODE_REVIEW.md'),'sha256':sha(RUN/'JOINT_CODE_REVIEW.md')},{'path':str(RUN/'ACTIVATION_DEBT_PROJECTION.md'),'sha256':sha(RUN/'ACTIVATION_DEBT_PROJECTION.md')},{'path':str(OUT/'SOURCE_MANIFEST.json'),'sha256':sha(OUT/'SOURCE_MANIFEST.json')},{'path':str(OUT/'EXACT_RESULTS.json'),'sha256':sha(OUT/'EXACT_RESULTS.json')},{'path':str(OUT/'BRIDGE_RESULTS.json'),'sha256':sha(OUT/'BRIDGE_RESULTS.json')}],
 'next_consumers':['A003','A005','A007','A008','A011','A012','A089','A094','A096','B20'],
 'next_action':'Consume an actual A003/A008 activated arbitrary-balanced-tensor reference; compute induced core-data law and entire debt from the projection, retaining seed entropy and actual activation probability.',
 'stagnant_substantive_attempts':0,'blockers':['Universal admissible data-reference construction/payment remains open.','Independent review of the new projection and supervisor adoption/mirror receipts remain pending.'],'packet_ids':['A086']}
expected=[x.replace(' (one primary ID, for compatibility)','') for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(expected)
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+x in report for x in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
(AGENT/'STATUS.md').write_text('STATE: Stage 2 complete locally: A003 (both), A007, A008, A012 independently accepted at scope; 119,345 exact assertions passed; core-reference debt projection proved pending review; full FEI OPEN.\nNEXT: Audit induced data law and full debt of a concrete A003/A008 activated arbitrary-tensor reference; A094/A085 review projection and saved five-claim reconstruction.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' '+RUN.name+': Followed B18 v2 directive. Reconstructed A003 two claims, A007 root normalizer, A008 output quotient, A012 admission/posterior obstruction; five HOLDS at scope, no source repair. Main checker V2 passed 89093 exact assertions; corrected own expectation weighting and preserved V1. Derived full activation-reference KL projection; 468 cases/30252 exact assertions passed. All results saved; universal C020 construction/payment remains open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+now+'\n- A003 full optimized forest bound is exactly H+vD(Pplus||U), not H plus only a normalizer. Actual distinct-run sums enforce U subprobability.\n- A007: common-core normalization cancels one r-bit root rarity; multiple-root exceptions are p^2-suppressed. Base gate/shape debt remains.\n- A008: a physical OUTPUT quotient code can realize latent posterior erasure; a RECORD code cannot subtract its latent entropy from transmitted length. Measure code lengths under the target spectrum, not the reference.\n- A012: hereditary class membership reflects arbitrary balanced tensor cores exactly. Activated-literal physical leaf posterior lower bound tends to two bits, although original physical influence tends to zero. This does not refute A011 boundary admission.\n- For balanced g activation, v=p(2-p), nonempty data mass under Pplus is beta=1/(2-p), and complete reference debt contains exactly pD(P_g||q_g) plus nonnegative mass, binary-sector and control conditional debts. Pay every term on the same reference; no root theorem silently pays data KL.\n')
save(OUT/'SCHEMA_VALIDATION.json',{'checked_at':now,'claim_fields':'PASS','statement_hashes':'PASS','progress_fields':'PASS','report_fields':'PASS','report_ends_in_universal_bridge':'PASS','compatibility_bytes':'PASS','reused_forest_hash_unchanged':'PASS','accepted_original_versions':5,'derived_pending_versions':1,'final_exact_assertions':total})
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']:receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save(OUT/'PERSISTENCE_RECEIPTS.json',{'at':now,'files':receipts,'adoption':'SUPERVISOR_PENDING','mirror':'NOT_VERIFIED'})
print(json.dumps({'schema':'PASS','original_claims_accepted':5,'derived_claim_pending_review':1,'exact_assertions':total,'receipted_files':len(receipts),'run':str(RUN)}))
