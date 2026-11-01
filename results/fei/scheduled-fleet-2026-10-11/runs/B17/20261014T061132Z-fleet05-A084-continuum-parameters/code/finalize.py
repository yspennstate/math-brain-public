from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];SHARED=AGENT.parents[1]
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2),encoding='utf-8')
def digest(p):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
protocol=read(P);validation=read(ROOT/'out/VALIDATION.json')
assert validation['all_checks_passed'] and validation['exact_or_interval_assertions']==2506
assert validation['scalar_diagnostics']==108 and validation['actual_physical_query_cases']==8
assert read(ROOT/'out/PHYSICAL_SUMMARY.json')['positive_curvatures']==2
wit=read(ROOT/'out/PIVOTAL_WITNESSES.json')
assert [r['minimum_pivotal_weight'] for r in wit['J']]==[1,0,0,0,2,0]
statement=('Let h be the six-bit Boolean sign negative exactly on binary indices {0,1,2,4,8,16,32,6,17,40}, with one bits denoting negative inputs, and J(x)=-h(x xor1). '
    'For every nonconstant Boolean core g on every finite uniform cube, oriented to P(g=-1)=p with 0<p<=1/16, form F=k(g_1,...,g_6) from six identical disjoint copies, k in {h,J}. '
    'For any actual physical coordinate i in block j, retain C(p_vec)=H_(p_vec)(k)-sum_l q_l h2(4p_l(1-p_l)), where q_l are the full heterogeneous outer pivotal probabilities, and define Delta C=C_parent-(C_child+ +C_child-)/2 using the true uniform query weights. '
    'Then Delta C<=(5/4)Inf_(j,i)(F), with sharper coefficients1/2 for h,1/8 for J directions1,2,3,5, and3/4 for J direction0. Direction4 uses5/4. '
    'Writing d=Inf_i(g), beta=ghat({i}), q=q_j, the stronger bias-dependent inequality is Delta C<=q beta^2 log2(1+16(1-q)/(9q)); the full exact decrement is Delta H(F)=q Delta H(g)+Delta C. '
    'For the selected mean x and fixed other five output laws, the non-affine terminal correction has C_j second derivative -2 sum_T d_T^2 log2((a_T+x d_T)^2/(x^2 d_T^2)), and its central second difference is the exact nonnegative tent-kernel integral of that logarithmic density. '
    'The bound covers every real attainable bias and singleton shift, beta=0, irrelevant coordinates, a constant child and integrable coefficient-zero singularities. It is a signed upper bound at the first query with identical starting biases, not an absolute-value price, an inherited-core payment, a hereditary heterogeneous-history bound or a universal FEI theorem.')
hypotheses=['Actual finite-dimensional uniform-cube Boolean core; nonconstant and minority-negative oriented',
    'Minority bias0<p<=1/16; six identical independent copies on disjoint physical supports',
    'Specified h or J; all directions kept separately, binary coordinate indices0 through5',
    'One actual uniform physical query and its two true weights1/2; all complete terminal entropies retained',
    'Entropy in bits; normalized biased outer spectrum used only as an exact expansion; physical total/coordinate influence']
sha=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest()
consumers=['A072','A075','A089','A074','A092','A087','A094','A080','B15','B17','B20']
claim={'claim_id':'A084-RARE-PHYSICAL-TERMINAL-CURVATURE','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':sha,'contributors':['A084'],
    'proof_source':{'proof':str(ROOT/'PROOF.md'),'report':str(ROOT/'REPORT.md'),'validation':['out/PIVOTAL_WITNESSES.json','out/SCALAR_FIXTURES.json','out/PHYSICAL_SUMMARY.json','out/VALIDATION.json'],'failed_preliminary_hypothesis':'out/FAILED_SINGLE_NEGATIVE_WITNESS.json'},
    'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_SOURCE_BOUND_LOCAL_PHYSICAL_PAYMENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(ROOT/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B17','packet_id':'A084','gap_id':'G-R-SELECT','attempt_id':'A084-continuum-5',
    'method':'Fixed-other-law logarithmic curvature identity, exact Green-kernel integral, Jensen/Parseval continuum envelope and analytic rare pivotal-witness endpoint reductions',
    'mathematical_delta':'Closes first physical-query terminal-curvature payment for every dimension and all real p<=1/16: Delta C<=5Inf/4, improved1/2 for h,1/8 for four J directions and3/4 for J direction0. 2506 assertions,108 scalar diagnostics and8 complete physical fixtures passed. Failed preliminary weight-one hypothesis for J direction4 preserved and corrected to weight2.',
    'deliverable_status':'ARTIFACT_COMPLETE_LOCAL_PAYMENT_REVIEW_PENDING','mathematical_status':'FIRST_QUERY_CURVATURE_PAID_INHERITED_CORE_AND_HEREDITARY_PAYMENT_OPEN_FULL_FEI_OPEN',
    'claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
    'source_artifacts':['REPORT.md','PROOF.md','FROZEN_SPEC.json','code/verify.py','out/PIVOTAL_WITNESSES.json','out/FAILED_SINGLE_NEGATIVE_WITNESS.json','out/SCALAR_FIXTURES.json','out/PHYSICAL_SUMMARY.json','out/VALIDATION.json','out/SOURCE_RECEIPTS.json'],
    'next_consumers':consumers,'next_action':'Carry the SAME complete child account through one subsequent heterogeneous query; quantify the actual curvature and unused inherited child surplus after the first debit. A072/A089/A075/A074/A092 independently reconstruct current proof.',
    'stagnant_substantive_attempts':0,'blockers':['No blocker at proved first-query target; independent review pending.','Inherited arbitrary-core decrement lacks a noncircular unused child-surplus payment.','Identical-bias first-query price is not proved hereditary under later heterogeneous physical histories.'],'packet_ids':['A084']}
assert set(progress)=={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:save(ROOT/name,progress)
inputs=[P,SHARED/'BOARD.md',SHARED/'claude/B17/STREAM_NOTES.md',AGENT/'STATUS.md',
    SHARED/'agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge/PROOF.md',
    SHARED/'agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge/REPORT.md',
    SHARED/'agents/A080/runs/20261014T034416Z-fleet05-A080-universal-counterexample-standard/PROOF.md',
    SHARED/'agents/A072/runs/20261014T044904Z-fleet05-A072-exact-walsh-engine/REPORT.md',
    SHARED/'agents/A072/runs/20261014T044904Z-fleet05-A072-exact-walsh-engine/NEXT_INTERFACE.md',
    SHARED/'agents/A072/runs/20261014T044904Z-fleet05-A072-exact-walsh-engine/CLAIMS.json']
save(ROOT/'out/SOURCE_RECEIPTS.json',[dict(digest(p),role='Read-only source, current bytes at persistence; mutable board/status not a historical immutable snapshot') for p in inputs])
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
(AGENT/'STATUS.md').write_text('STATE: A084 stage5 author proof complete: all-real rare first-query Delta C<=5Inf/4, h<=Inf/2, dominant J<=Inf/8; 2506 assertions/108 diagnostics/8 complete physical fixtures PASS; review pending, FEI OPEN.\nNEXT: Carry SAME full child account through one further heterogeneous physical query; pay inherited core excess from genuinely unused surplus, without renewing first-query or composition budgets; A072/A089/A075/A074/A092 review.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp}: Stage5 read all board/B17/status/protocol. A075/A080/A072 already close mixed-cycle entropy budget; retired own prior NEXT instead of duplicating. Consumed A072 physical DeltaC handoff. Derived fixed-other-law C_j second derivative=-2 logarithmic admission slope and exact Green-kernel physical central difference. Jensen/Parseval+Boolean singleton caps provide all-real rare envelope. Initial proposed3/4 generic price FAILED actual J direction4 weight-one pivotal hypothesis; archived counts, corrected to weight-two and generic5/4. h1/2, dominant J1/8, J0 3/4. Diagnostic initially could not save to missing out; helper creates owned out. Corrected pilot315 checks1.3816s; final2506 checks8.3613s with108 scalar diagnostics and8 actual36-bit compressed queries,16 children including constant endpoint. Added24 full parent/both-child entropy/influence checks and reran within frozen scope. Complete inherited core remains unpaid; no FEI or hereditary price claimed. Saved exact proof, failure witness and protocol files; review pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage5 durable: Holding other output laws fixed, C_j(x)=sum ell((a+xd)^2)+(1-x^2)sum ell(d^2)+q x^2log2(x^2), up to affine terms. Thus C_j second derivative=-2L_j(x), L=sum d^2log2((a+xd)^2/(x^2d^2)). Physical DeltaC is its exact tent-kernel integral, NOT a simultaneous-all-bias derivative. Jensen/Parseval gives DeltaC<=q beta^2 log2(1+(1-q)/(ell^2q)). Rare identical p<=1/16 impliesell>=3/4 and beta^2/Inf_i<=2p. h price<=1/2; J dominant directions1,2,3,5<=1/8; J0<=3/4; J4<=5/4. J4 first pivotal assignments have weight2, so a universal weight-one witness assumption is false. Coefficient-zero singularities are integrable and create negative curvature credits; cancellation before differentiating covers constant children. Local first-query DeltaC payment does not pay inherited arbitrary core or subsequent heterogeneous histories. See stage5 PROOF.md and exact witness counts.\n')
save(ROOT/'out/CHECKPOINT.json',{'state':'COMPLETE_AUTHOR_PROOF_WITH_EXECUTED_CHECKS','generic_physical_rate':'5/4','h_rate':'1/2','J_rates':{'0':'3/4','1':'1/8','2':'1/8','3':'1/8','4':'5/4','5':'1/8'},'first_unproved_universal_line':'Inherited core decrement and later heterogeneous physical history','new_independent_review':'pending','full_FEI':'OPEN'})
assert read(ROOT/'PROGRESS.json')==read(ROOT/'PACKET_DELTA.json')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json' and '__pycache__' not in p.parts:
        row=digest(p);assert row['bytes']<20*1024*1024;row['path']=str(p.relative_to(ROOT));files.append(row)
save(ROOT/'out/RECEIPTS.json',{'required_files_verified':['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'],'protocol_schema':'PASS','statement_hash_verified':True,'compatibility_copy_verified':True,'checks':validation,'pivotal_witness_weights_verified':[1,0,0,0,2,0],'independent_review':'pending','supervisor_copy':'pending','mirror_verification':'not performed','rolling_files':[digest(AGENT/f) for f in ['STATUS.md','WORKLOG.md','LEARNED.md']],'files':files})
for row in files:assert digest(ROOT/row['path'])['sha256']==row['sha256']
print(json.dumps({'saved':ROOT.name,'claim':claim['claim_id']+'@1','files_receipted':len(files),'readback':'PASS','full_FEI':'OPEN'}),flush=True)
