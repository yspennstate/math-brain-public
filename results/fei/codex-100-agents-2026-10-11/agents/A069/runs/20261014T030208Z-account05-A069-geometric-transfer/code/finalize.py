from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1];ROOT=A.parents[1]
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
review=ROOT/'agents/A070/runs/20261014T005025Z-account05-A070-analytic-route-referee'
stage3=A/'runs/20261014T000110Z-account05-A069-geometric-transfer'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads(P.read_text(encoding='utf-8-sig'))
res=json.loads((R/'out/CHECK.json').read_text())
assert res['status']=='PASS' and res['cases']==1282 and res['elapsed_seconds']<55
accepted=json.loads((review/'CLAIMS.json').read_text())[0]
assert accepted['claim_id']=='A069-BOOLEAN-MASK-REFUND' and accepted['review_records']
dep={'claim_id':accepted['claim_id'],'version':accepted['version'],'statement_sha256':accepted['statement_sha256'],'acceptance':'Independent A070 at exact scope; no repair','source':str(review/'CLAIMS.json')}
statement=('For Boolean g(X) independent of private coordinates Z and Boolean mask q(X,Z), suppose every X-edge has private-averaged mask-disagreement probability p_e<=theta<=1/2. For every K,M>=0, K I(g)+M I(q)<=max(M,(K+M theta)/(1-theta)) I(gq). On a fixed complete hierarchy, Gamma(g)<=K I(g) and W(q)<=M I(q) therefore imply H(gq)<=max(M,(K+M theta)/(1-theta)) I(gq). For compatible two-subcube XOR masks on nonempty C,U,V,Y with source g(C,Y), p=2^-|U|+2^-|V|-2^(1-|U|-|V|)<=1/2 and M=12 applies to T=(T_Y,(T_C,(T_U,T_V))). For g(x,Y) with unequal cores h_+,h_- and x in C at depth d<=1 within T_C, let B=(Gamma_Y(h_+)+Gamma_Y(h_-))/2, equal to the average complete code cost of the actual final Y terminals. Then H(gq)<=Gamma_T(gq)<=B+2 I_Y(gq)+(4d+20) I_(C,U,V)(gq). If both Gamma_Y(h_sigma)<=K I(h_sigma), H(gq)<=max(K+2,4d+20) I(gq). No payment of arbitrary source codes or private-coordinate-dependent sources is asserted.')
hyp=['Actual Boolean signs on finite uniform cubes; entropy and code lengths in bits; physical pivotal influence.',
     'Source independence of private Z is essential to the abstract edge averaging; the edge condition is uniform over X edges.',
     'The SAME complete fixed hierarchy pays source, mask and output; no sample-dependent reference selection.',
     'Compatible-mask application has nonempty common and exclusive blocks and identical common assignment; operation is sequential XOR flips.',
     'Unequal-core specialization uses one common Y tree and chooses the distinguished shared coordinate at depth at most one inside C.',
     'Retained-B bound admits constant cores; paid-code corollary requires both specified inequalities and does not omit their root bits.',
     'No overlapping-product entropy subadditivity, real-valued extension, same-constant induction or physical stopping-tree ownership is assumed.']
claim={'claim_id':'A069-SOURCE-BLIND-SHARED-EDGE-TRANSFER','version':1,'exact_statement':statement,'hypotheses':hyp,
       'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
       'contributors':['account05/A069'],'proof_source':{'path':str(R/'DERIVATION.md'),'sha256':sha(R/'DERIVATION.md'),'locators':'Sections1-3, equations(1)-(7)'},
       'proof_dependencies':[dep],'review_records':[],'status':'AUTHOR_PROVED_EXACT_CHECKS_PASSED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
       'first_unproved_line':None,'next_consumers':['A070','A088','A094','A067','B14','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields']);save(R/'CLAIMS.json',[claim])
nxt='Permit one private-coordinate source dependence; retain both actual terminal bills and compute the disagreement-correlation reserve in one common output reference, first preserving all banks on A070 g=q*y.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A069','gap_id':'G-A069-STABLE-ENCODING',
 'attempt_id':'A069-stage4-source-blind-shared-edge','method':'Exact conditional physical-edge averaging, complete Boolean tree-code transfer, partial Parseval and both actual final terminal costs',
 'mathematical_delta':'C020 conditional paid-source transfer with arbitrary common-control sharing; explicit unequal-core family has complete retained terminal bound B+2I_Y+24I_controls (20 for singleton common block). Private source correlation and universal paid references remain open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT; NEW_REVIEW_AND_MIRRORS_PENDING','mathematical_status':'SCOPED_THEOREM_AUTHOR_PROVED; FULL_FEI_OPEN',
 'claim_versions_used':[dep,{'claim_id':'A070-MASK-REFUND-BOOLEANITY-AND-EDGE-CONVERSION-AUDIT','version':1,'use':'Consumes signed-conversion obstruction, independently accepted by A088; not a positive-payment dependency'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','FROZEN_SPEC_V2.json','code/check.py','code/check_v1.py','out/PILOT_V1.json','out/CHECK.json','out/REVIEW_RECEIPTS.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':claim['next_consumers'],'next_action':nxt,'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A069']}
assert set(progress)=={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
save(R/'out/REVIEW_RECEIPTS.json',{'previous_stage3_claim':accepted['claim_id'],'statement_sha256':accepted['statement_sha256'],'review_records':accepted['review_records'],'review_source_sha256':sha(review/'CLAIMS.json'),'new_stage_review':'PENDING'})
sources=[P,ROOT/'BOARD.md',ROOT/'claude/B14/STREAM_NOTES.md',stage3/'PROGRESS.json',stage3/'code/finalize.py',review/'DERIVATION.md',review/'CLAIMS.json',ROOT/'agents/A067/runs/20261014T020120Z-account05-A067-hypercontractive-refinement/DERIVATION.md',ROOT/'agents/A088/runs/20261014T024038Z-account05-A088-booleanity-referee/REPORT.md']
save(R/'out/SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'hash_time':'stage finalization'} for p in sources])
report=(R/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('This stage moves C020')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
save(R/'out/SCHEMA_CHECK.json',{'claim_fields':'PASS','progress_fields':'PASS','report_fields':'PASS','statement_hash':'PASS','compatibility_copy':'IDENTICAL','exact_cases':res['cases'],'exact_assertions':res['exact_assertions']})
(A/'STATUS.md').write_text('STATE: A069 stage4 complete: source-blind shared-edge transfer, both unequal actual terminal bills retained; max(K+2,24) family bound (20 for one common bit); 1282 cases / 14352 exact checks PASS; stage3 independently accepted by A070; FEI OPEN.\nNEXT: A070/A088 review; allow one private-coordinate source dependence and compute its correlation reserve under one common reference, preserving both child bills and all A070 cancellation banks.\n',encoding='utf-8')
marker='2026-10-14 03:02 UTC stage 4:'
if marker not in (A/'WORKLOG.md').read_text():
 with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(marker+' Read board/B14 lead and source-bound A070/A067/A088 results. Consumed independent A070 stage3 acceptance. Proved shared-edge mask probability <=1/2 for sources independent of private blocks, weighted source/mask-to-final conversion, and unequal-core actual terminal bound B+2I_Y+24I_controls. V1 pilot stopped at55s guard; explicit reflection-reduced V2 passed1282 cases/14352 assertions in1.9016114s. All-dimensional proof recorded; private correlation/universal paid source remain open. New review and mirror pending.\n')
fact='Stage 4 shared-edge transfer:'
if fact not in (A/'LEARNED.md').read_text():
 with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
  f.write(fact+' If source g(X) is independent of private Z and mask flip probability on every X-edge is <=theta<=1/2, weighted bill K I(g)+M I(q) is <=max(M,(K+Mtheta)/(1-theta)) I(gq). The two source-disagreement cases are p and1-p; this prices signed influence cancellation without declaring refund-alone payment.\n')
  f.write('Compatible overlapping subcube XOR masks have shared boundary flip p=a+b-2ab<=1/2 for a,b<=1/2. A source may depend on ALL common controls but must not see private U,V. With accepted W(mask)<=12I(mask), paid source code K transfers at2K+12. This property is derived directly, not spatially assumed.\n')
  f.write('For g(x,Y) with arbitrary unequal cores, one common Y tree gives B=average Gamma_Y of actual final terminals. Gamma_T(g)=B+2Var(g)+2(d+1)P(h_+!=h_-), where shared x has tree depth d<=1. Final code<=B+2I_Y+(4d+20)I_controls. Both paid core codes K give max(K+2,20) at d0 or max(K+2,24) at d1. Constants keep root-bit cost in B and do not automatically satisfy Gamma<=K I.\n')
  f.write('Private-coordinate source dependence invalidates conditional edge averaging by correlation. A070 g=q*y witness keeps its signed bank-59/2; neither new transfer nor A067 independent-seed access includes that source. Next requires a correlation reserve with both actual terminal bills and one physical budget.\n')
assert len((A/'STATUS.md').read_text().splitlines())==2
files=sorted(p for p in R.rglob('*') if p.is_file() and p.name!='RECEIPTS.json')+[A/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
for p in files:assert p.stat().st_size<20_000_000
save(R/'out/RECEIPTS.json',{'scope':'LOCAL_ONLY; new independent review, supervisor copy and mirrors pending','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]})
print(json.dumps({'schema':'PASS','cases':res['cases'],'exact_assertions':res['exact_assertions'],'statement_sha256':claim['statement_sha256'],'receipts_sha256':sha(R/'out/RECEIPTS.json')},indent=2))
