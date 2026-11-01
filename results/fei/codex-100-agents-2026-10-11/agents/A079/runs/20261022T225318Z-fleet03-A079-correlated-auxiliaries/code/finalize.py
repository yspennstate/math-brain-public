"""Small metadata finalizer; no search, compiler, external publication, or shared write."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
H=Path(r'~');C=H/'brain_workers/FEI100_20261011'
P=H/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
protocol=read(P);val=read(R/'out/validation.json');pilot=read(R/'out/pilot_summary.json')
spec=read(R/'FROZEN_SPEC.json')
assert val['status']==pilot['status']=='PASS'
assert val['helper_sha256']==pilot['helper_sha256']==spec['sha256']==sha(R/'code/check.py')
assert val['seconds']<55 and pilot['seconds']<55
assert (R/'FROZEN_SPEC.json').stat().st_mtime < (R/'out/pilot_summary.json').stat().st_mtime-pilot['seconds']
for name in ['review_controller.json','generic_lift.json','sourced_step.json','collision_guard.json']:
 assert read(R/'out'/name)['status']=='PASS'
assert read(R/'out/generic_lift.json')['gate_cases']==1782
assert read(R/'out/generic_lift.json')['source_step_cases']==5832
dp=read(R/'out/review_controller.json');assert dp['represented_trees']==238145
assert dp['locally_failing_rate4']==10 and dp['root_max']=={'2':'1','3':'-9/16'}

orig32=C/'agents/A032/runs/20261021T215120Z-fleet03-A032-boolean-phase-realizability'
orig96=C/'agents/A096/runs/20261021T210221Z-fleet03-A096-live-gap-ledger'
orig97=C/'agents/A097/runs/20261021T232544Z-fleet03-A097-cross-route-transfer'
cs=read(orig32/'CLAIMS.json')
source=next(x for x in cs if x['claim_id']=='A032-FIXED-SIBLING-CONTROLLER-STOPPING-TRANSPORT')
old=next(x for x in cs if x['claim_id']=='A079-FIXED-NONFAIR-SIBLING-SEED-TRANSPORT')
assert source['statement_sha256']==hashlib.sha256(source['exact_statement'].encode('utf-8')).hexdigest()
assert source['statement_sha256']=='ece8fb4ce6e744704a458001a65ba0f869140ddfac51a491a215720b6134958c'
review=dict(source)
review['review_records']=list(source['review_records'])+[{'reviewer':'A079','verdict':'HOLDS_AT_STATED_SCOPE','at':stamp,'source':str(R/'REVIEW_A032.md'),'method':'Independent full seed-cancellation reconstruction and exact81-state Bellman optimization; no author implementation or repair','formal_verification':'NOT_CLAIMED','registry_adoption':'UNVERIFIED'}]
review['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A079_LOCAL_REGISTRY_ADOPTION_UNVERIFIED'
old=dict(old);old['status']='A032_INDEPENDENT_ACCEPTANCE_CONSUMED_BY_A079_UNCHANGED_STATEMENT'
assert old['statement_sha256']==hashlib.sha256(old['exact_statement'].encode('utf-8')).hexdigest()

statement=('Fix A079 four-bit complementary rows a,b and F_h=a+z*b*h for any Boolean seed h on '
'a disjoint uniform physical cube. For any controller restriction s and normalized finite-cost '
'source reference R, define the normalized tagged wrapper reference by Q(0,U,T)=ahat_s(U)^2*1[T=empty] '
'and Q(1,U,T)=bhat_s(U)^2*R(T). Then CE_wrapper=k_s+beta_s*CE(h,R), '
'seed erasure and seed influence equal beta_s times the source quantities, and every prescribed '
'source reset increment with BOTH complete child references equals beta_s times its source increment. '
'Controller queries conserve the mean beta-weighted source bank and release the actual structural JS. '
'Every supplied source continuation interface W satisfying its actual local erasure-plus-child-cost '
'inequalities therefore lifts to V(s,v)=k_s+beta_s*W(v) for every finite admitted adaptive mixed '
'controller/seed stopping tree leaving z unqueried, preserving all old debits and complete terminals. '
'If W_root<=K*I(h)-rho with K>=2,rho>=0, the SAME K pays the wrapper and retains original reserve '
'K*17/8-[5-(9/16)log2(3)]+3*rho/8. Any later physical z query and arbitrary no-reset continuation '
'are paid by the full marginalized-reference chain rule. A generic initial source price and a '
'fresh reference reset after biased z-sector collision are not asserted.')
claim={'claim_id':'A079-TAGGED-REFERENCE-SAME-BANK-LIFT','version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean signs; independent uniform physical controller/address/seed cubes; fixed displayed a,b',
 'Only the specified tagged wrapper references are admitted; this is not arbitrary incoming joint-reference closure',
 'Every source interface W is already paid on ALL source actions actually admitted; both child references and prior debits retained',
 'z is unqueried during mixed lifting; following its deletion only no-reset continuation is asserted',
 'Entropy and CE bits; original coordinate influence; finite source CE; zero sectors handled without division'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A079'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':['out/validation.json','out/generic_lift.json','out/sourced_step.json','out/collision_guard.json'],'formal_verification':'NOT_LAUNCHED_MEMORY_GATE'},
 'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PAPER_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A032','A034','A088','A094','A096','A097','B16','B20']}
claims=[old,review,claim]
for x in claims:assert set(x)==set(protocol['required_per_run']['claim_fields'])
save(R/'CLAIMS.json',claims)
next_action=('After a sourced active reset, delete physical z and price ONE prescribed fresh child reset '
'with actual signed empty-frequency interference, both full terminal references, previous controller/source '
'debits and SAME diminished original bank. A032/A088/A094 review; A096/A097 consume.')
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B16','packet_id':'A079',
 'gap_id':'G-PHASE-COND','attempt_id':'A079-stage7-tagged-reference-same-source-bank-lift-v1',
 'method':'Independent controller Bellman certificate; exact tagged-reference tensor lift; same-bank finite-tree induction; sourced canonical active reset and biased phase guard',
 'mathematical_delta':'A032 controller-only theorem independently HOLDS. An already paid source history lifts through ALL admitted wrapper-controller/seed interleavings at unchanged K>=2, with actual normalizers and complete inherited terminals; last-address no-reset continuation paid. Fresh reset after address collision and generic initial source price remain open.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_AND_EXACT_CERTIFICATES',
 'mathematical_status':'FULL_FEI_OPEN; generic conditional lifting paper proof, independent review pending; Lean not launched after memory gate1',
 'claim_versions_used':[{'claim_id':source['claim_id'],'version':1,'statement_sha256':source['statement_sha256'],'use':'independent review'},
 {'claim_id':old['claim_id'],'version':1,'statement_sha256':old['statement_sha256'],'use':'A032 acceptance consumed'},
 {'claim_id':'A096-CANONICAL-ACTIVE-RESET-SAME-ANCESTOR','version':1,'use':'conditional full-history application; eight actual source steps independently checked'},
 {'claim_id':'A097-MIXED-ACTIVE-CONTROL-RESET-SAME-ANCESTOR','version':1,'use':'conditional application at original admission, not full independent acceptance'}],
 'claims_created_or_changed':[source['claim_id']+'@1: A079 independent acceptance',old['claim_id']+'@1: A032 acceptance consumed',claim['claim_id']+'@1'],
 'source_artifacts':['REPORT.md','PROOF.md','REVIEW_A032.md','HANDOFF.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','code/Bank.lean','out/validation.json','out/review_controller.json','out/generic_lift.json','out/sourced_step.json','out/collision_guard.json','out/LEAN_ADMISSION.json','out/SOURCE_MANIFEST.json','out/PERSISTENCE_RECEIPT.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Full FEI initial generic priced source remains OPEN','Fresh reset after physical z deletion not priced','New lifting independent review and registry/mirror adoption unverified','Fresh memok exited1: physical0.7GB; Lean not launched'],
 'packet_ids':['A079']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
save(R/'out/LEAN_ADMISSION.json',{'status':'HELD_NOT_LAUNCHED','memok_exit_code':1,'physical_free_gb':'0.7','physical_requirement_gb':'4.0','commit_free_gb':'19.4','commit_requirement_gb':'8.0','source_path':'code/Bank.lean','source_sha256':sha(R/'code/Bank.lean'),'formal_target_verified':False,'scope':'natural-number monotonicity of one weighted original bank only; no formalization claimed'})

sources=[]
def rec(p,role):sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'role':role})
rec(P,'complete current execution protocol read')
rec(C/'BOARD.md','coordination selected related rows; hash at final save, board is live')
rec(C/'claude/B16/STREAM_NOTES.md','lead v2 complete read')
for p in [orig32/'PROOF.md',orig32/'REPORT.md',orig32/'PROGRESS.json',orig32/'CLAIMS.json',orig96/'DERIVATION.md',orig96/'CLAIMS.json',orig97/'DERIVATION.md',orig97/'CLAIMS.json']:
 rec(p,'source derivation/claim actually read; source applications conditional where indicated')
rec(A/'runs/20261021T153136Z-fleet03-A079-correlated-auxiliaries/PROOF.md','productive predecessor seed transport')
save(R/'out/SOURCE_MANIFEST.json',{'saved_at':stamp,'sources':sources,'wake':'degraded stale owner-model/state-of-mind notes disclosed; not used as premises','source_reviews':'A032 independently reconstructed; A096/A097 full chain not newly accepted here'})

rp=R/'REPORT.md';text=rp.read_text(encoding='utf-8')
text=text.replace('optimization,+not','optimization,\nnot').replace('optimization,\\+not','optimization,\nnot')
text=text.replace('Actual final assertion total/runtime are in out/validation.json.',f'Final PASS:{val["assertions"]} exact assertions in{val["seconds"]:.4f}s; the count includes support-positivity checks at occupied CE atoms. Outputs are in out/validation.json.')
rp.write_text(text,encoding='utf-8',newline='')
(A/'STATUS.md').write_text('STATE: Stage7 saved: A032 all-controller bound independently HOLDS; paid source histories lift through all admitted controller/seed mixtures at SAME K>=2 while z remains;246958 exact assertions PASS; FEI OPEN.\nNEXT: Delete z after sourced reset and price prescribed fresh child reference with signed vacuum collision, both full terminals and SAME remaining bank; A032/A088/A094 review, A096/A097 consume.\n',encoding='utf-8',newline='')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
 f.write(f'\n{stamp} stage7 fleet03: A032 controller stopping@1 independently HOLDS via81-state/108-transition integer-power Bellman certificate (238145 trees represented). Derived normalized tagged-reference CE=k+beta*c and same-bank mixed source/controller lift at unchanged K>=2, with all prior debits and full terminals. Pilot1312 assertions/0.1560s; final246958 assertions/21.4196s PASS:1782 generic gates,5832 reset identities,8 sourced active-reset roots at19 states and biased z-collision. Fresh memok1 at0.7GB; Lean not launched. Full FEI and new reset after z remain OPEN; protocol files saved.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\n2026-10-23 stage7 durable facts:\n- A032 fixed-sibling controller stopping@1 independently HOLDS: exact81-state Bellman proof represents238145 trees, root max1-(9/16)log2(3)<1/8,10 local rate4 failures retained. A032 acceptance of our fixed-sibling@1 consumed.\n- For each u restriction of F=a+zbh, tagged actual-sector reference Q_s,R has CE=k_s+beta_s CE(h,R), even for biased seeds. Seed erasure/influence and every complete reset increment scale EXACTLY bybeta_s; both child reference costs stay distinct.\n- If a supplied source history W is already paid at rateK>=2, V=k_s+beta_s W pays ALL finite admitted adaptive controller/seed interleavings at the SAME K while z remains unqueried. Controller queries conserve mean beta-weighted source reserve and release actual JS. All previous debits and full terminals remain; no original reserve is reissued. This does NOT initially price an arbitrary Boolean source.\n- Conditional application to A096/A097 keeps original admission and source bank. Eight canonical active-reset roots independently checked, including positive full inherited constant off-child cost and scaled release>=beta_s e.\n- z deletion with the full marginalized reference is paid by conditional occupancy KL, as are later no-reset continuations. A FRESH reset after z is unpaid: biased child vacuum probabilities169/1024 and25/1024 exhibit the signed collision. Keep -beta_s R(h) cancellation before Shannon source pricing.\n- Pilot1312 and final246958 exact assertions PASS on separately frozen domains; no pooling with prior stage. Lean was NOT launched after memok1 at0.7GB free. New lifting paper proof awaits independent review; FEI OPEN.\n')

for heading in protocol['required_per_run']['report_fields']:assert '# '+heading in text
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
save(R/'out/PERSISTENCE_RECEIPT.json',{'saved_at':stamp,'status':'LOCAL_FILES_AND_EXACT_PROTOCOL_SCHEMAS_VERIFIED','final_assertions':val['assertions'],'pilot_assertions_separate':pilot['assertions'],'frozen_spec_before_pilot':True,'helper_sha_verified':True,'progress_delta_identical':True,'formal_target_verified':False,'new_theorem_independent_review':'PENDING','remote_mirror':'NOT_VERIFIED','files':files})
print(json.dumps({'status':'PASS','files':len(files),'final_assertions':val['assertions'],'pilot_assertions':pilot['assertions'],'FEI':'OPEN','Lean':'NOT_LAUNCHED_MEMORY_HOLD'}))
