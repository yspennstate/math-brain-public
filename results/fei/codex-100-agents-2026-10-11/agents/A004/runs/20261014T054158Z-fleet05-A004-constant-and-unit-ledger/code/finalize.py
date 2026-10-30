from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
import arithmetic as A
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];TEAM=HOME.parent.parent
stamp=datetime.now(timezone.utc).isoformat()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
validation=load(R/'out/VALIDATION.json');assert validation['status']=='PASS' and validation['assertions']==8637 and validation['runtime_seconds']<60
protocol=load(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
source=TEAM/'agents/A003/runs/20261014T050612Z-fleet05-A003-minimal-target-formulation/CLAIMS.json'
sourceclaims=load(source);old=next(c for c in sourceclaims if c['claim_id']=='A003-RETAINED-POINT-SHADOW-SHARP-ALLOWANCE')
ownreview=next(c for c in sourceclaims if c['claim_id']=='A004-KL-SHADOW-EXCLUSIVE-TERMINAL-TRANSFER')
assert hashlib.sha256(ownreview['exact_statement'].encode()).hexdigest()==ownreview['statement_sha256']
sourcecomputed=hashlib.sha256(json.dumps({'statement':old['exact_statement'],'hypotheses':old['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert sourcecomputed==old['statement_sha256']
sf=source.parent/'code/finalize.py';b=sf.read_bytes();(R/'out/sources/A003-finalize.py').write_bytes(b)
manifest=load(R/'out/SOURCE_MANIFEST.json')
if not any(q['path']==str(sf) for q in manifest):manifest.append({'path':str(sf),'snapshot':'out/sources/A003-finalize.py','bytes':len(b),'sha256':sha(sf)})
save(R/'out/SOURCE_MANIFEST.json',manifest)
review={'reviewer':'A004','at_utc':stamp,'verdict':'ACCEPT_AT_ORIGINAL_NEW_POINT_ALLOWANCE_SCOPE_WITHOUT_REPAIR','source_statement_sha256':old['statement_sha256'],
 'scope':'All-d retained point formulas, sharp A0/A1 allowances, actual terminal owner and certified independent tensor continuation. Not a second independent review of A004 own ancestor or A096 discarded-loss theorem.',
 'method':'Independent physical vertex/selector spectra, closed formula subtraction, direct all-d logarithm/limit reconstruction, full terminal tensor spectra and exact sign checks',
 'substantive_repair':False,'proof_source':str(R/'DERIVATION.md'),'locator':'section 1','validation':str(R/'out/VALIDATION.json')}
old['review_records'].append(review);old['status']='INDEPENDENTLY_ACCEPTED_LOCAL_BY_A004_NEW_POINT_BOUND_SOURCE_ADOPTION_PENDING'
# Certificate readback on frozen outputs, no additional search or dimensions.
small=load(R/'out/SMALL_EDIT_CERTIFICATE.json');form={int(k):Q(v) for k,v in small['maximum']['allowance_log_form'].items()}
expected={2:Q(12),7:Q(-49,4),5:Q(25,2),3:Q(-9,2)};assert form==expected
lo,hi=A.bounds(form);assert Q(-499,1000)<lo<=hi<Q(-498,1000)
def rounded(lo,hi):
 z=1<<100;return {'lower':str(Q((lo*z).__floor__(),z)),'upper':str(Q((hi*z).__ceil__(),z))}
padded=[]
for rec in load(R/'out/ENDPOINTS.json'):
 if rec['label']!='padded_AND3':continue
 bank={int(k):Q(v) for k,v in rec['B_shadow'].items()};surplus={int(k):Q(v) for k,v in rec['terminal_S4'].items()}
 margin=A.add(surplus,A.mul(-1,bank),{2:-Q(rec['delta'])})
 ml,mh=A.bounds(margin);assert ml>0 and rec['children_K4_certified']
 padded.append({'n':rec['n'],'incident_pivots':rec['incident_pivots'],'whole_bank_margin':rounded(ml,mh),'claim':'S4-Q-delta>0 on actual full terminal laws'})
l,u=A.ln_interval(Q(2))
save(R/'out/CERTIFICATE_READBACK.json',{'status':'PASS','main_assertions':validation['assertions'],'extra_fixed_output_checks':{'max_expression':True,'max_rational_bounds':True,'padded_positive_whole_bank_margins':3},'max_allowance':rounded(lo,hi),'padded_controls':padded,
 'A0_bits':rounded(2/u-2,2/l-2),'A1_bits':rounded(2/u-1,2/l-1),'A0_nats':'2-2ln2','A1_nats':'2-ln2','terminal_price_nats':'4ln2'})
save(R/'out/LAUNCH_RECEIPT.json',{'event':'Premature dependent launch while setup command yielded session 66724','first_checker_result':'ModuleNotFoundError: arithmetic; exit 1 before mathematical assertions','resolution':'Waited for setup exit 0; reran unchanged frozen checker; PASS','mathematical_failure':False})
statement=('For every d=1,2,3 uniform-cube Boolean sign b and every vertex v with b(v)=1, let c=b-2*1_v, delta=2^-d, k the number of b-pivotal incident edges at v, and g the selector with children b,c. '
 'The physical influence difference is I(c)-I(b)=2delta(d-2k); its full actual terminal surplus S_K=K[I(b)+I(c)]/2-[H(b)+H(c)]/2 equals K I(b)-H(b)+Kdelta(d-2k)-[H(c)-H(b)]/2. '
 'All 1060 positive-endpoint pairs through dimension three have both children price-four certified, and max[(B_selector(g)-S4)/delta]=12-(49/4)log2(7)+(25/2)log2(5)-(9/2)log2(3), strictly between -499/1000 and -498/1000. Thus B_selector(g)<=S4 on this complete finite domain, and the Maj3 inherited bank B_selector(g)+delta<=S4+(1+Rmax)delta with 1+Rmax<502/1000. '
 'For b=+1 iff its first three bit labels are zero, with respectively one, two or three additional dummy bits, and c its origin flip, k=3, the whole bank B_selector(g)+delta<S4; I(b)=3/4 and I(c)=1/2,11/16,3/4 respectively. The six-bit flip is influence-neutral but changes full entropy. '
 'Sign reversal covers negative endpoints. These finite exact certificates do not establish an arbitrary-dimensional non-point extension, universal FEI or renewal of the same terminal surplus.')
new={'claim_id':'A004-POINT-EDIT-TERMINAL-LEDGER','version':1,'exact_statement':statement,
 'hypotheses':['Actual uniform Boolean signs; full Fourier entropy in bits; ordinary physical influence; positive endpoints chosen by global sign symmetry',
 'Complete finite d=1,2,3 domain only for the maximum; separate specified padded AND3 controls at d=4,5,6',
 'S4 is actual fair unused terminal surplus, not a renamed root influence budget; all encoder charges use the same surplus once'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A004'],
 'proof_source':{'path':str(R/'DERIVATION.md'),'locator':'sections 2-4','exact_certificate':str(R/'out/SMALL_EDIT_CERTIFICATE.json'),'validation':str(R/'out/VALIDATION.json'),'readback':str(R/'out/CERTIFICATE_READBACK.json')},
 'proof_dependencies':[],'review_records':[],'status':'FINITE_DOMAIN_EXACT_CERTIFICATE_AND_LEDGER_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A003','A026','A096','A027','A087','A094','B01','B06','B20']}
claims=[ownreview,old,new];save(R/'CLAIMS.json',claims)
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B01','packet_id':'A004','gap_id':'C018-C019-SIGNED-TERMINAL-COLLISION','attempt_id':'A004-destroyed-edge-owner-stage-5',
 'method':'Independent sharp point allowance review; exhaustive exact finite vertex edits; physical destroyed-edge and neutral entropy ledger; source review adoption',
 'mathematical_delta':'A003 all-d sharp retained point allowance accepted; A003 acceptance of prior A004 criterion consumed. 1060 finite point-edit banks fit actual S4; exact negative maximal allowance and three padded AND3 whole-bank controls certified. 8637 main assertions PASS; no arbitrary non-point extension.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_AND_FINITE_CERTIFICATE_SAVED','mathematical_status':'SCOPED_POINT_ALLOWANCE_ACCEPTED_FINITE_DESTROYED_EDGE_CASES_CLOSED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':old['version'],'statement_sha256':old['statement_sha256'],'status':'new positive point bound independently accepted here'},{'claim_id':ownreview['claim_id'],'version':ownreview['version'],'statement_sha256':ownreview['statement_sha256'],'status':'A003 source-bound independent review adopted locally'}],
 'claims_created_or_changed':[{'claim_id':old['claim_id'],'version':1,'change':'A004 independent acceptance appended at new point-bound scope'},{'claim_id':ownreview['claim_id'],'version':1,'change':'A003 original review consumed; no statement changes'},{'claim_id':new['claim_id'],'version':1,'change':'complete finite certificate and exact ledger; review pending'}],
 'source_artifacts':['REPORT.md','DERIVATION.md','CLAIMS.json','out/SOURCE_MANIFEST.json','out/VALIDATION.json','out/SMALL_EDIT_CERTIFICATE.json','out/ENDPOINTS.json','out/CERTIFICATE_READBACK.json','out/LAUNCH_RECEIPT.json'],
 'next_consumers':new['next_consumers'],'next_action':'Carry the SAME remaining S4 and reference through a proper data query on the neutral six-bit padded AND3 pair, recording nonconstant terminals and signed release without renewal.',
 'stagnant_substantive_attempts':0,'blockers':['No local persistence blocker. New finite certificate awaits independent review; arbitrary non-point/history payment and full FEI open; supervisor adoption/mirrors unverified.'],
 'packet_ids':['A004']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
assert set(progress)=={k.split(' (',1)[0] for k in protocol['required_per_run']['progress_fields']}
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
report=(R/'REPORT.md').read_text(encoding='utf-8')
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
save(R/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields':'EXACT','progress_fields':'EXACT','report_fields':'ALL_PRESENT','packet_delta':'BYTE_IDENTICAL','source_hashes':'VERIFIED_WITH_SOURCE_CONVENTIONS','main_assertions':validation['assertions']})
(HOME/'STATUS.md').write_text('STATE: A004 stage 5 complete: A003 sharp point allowance independently accepted; 1060 vertex edits and unequal-amplitude destroyed/neutral AND3 banks certified; 8,637 assertions PASS; full FEI OPEN.\nNEXT: A003/A096/A087/A094 review; carry SAME remaining S4/reference through a proper data query on the neutral six-bit AND3 pair, with full terminals and no bank renewal.\n',encoding='utf-8')
log=f'\n{stamp}: Stage 5 accepted A003 sharp retained point allowance and consumed its independent review of A004 terminal criterion. Exhaustive 1060 positive-endpoint edits through d3: 522 destroyed/522 created/16 neutral, exact maximum R in(-.499,-.498), all Q<=actualS4. Padded AND3 d4,5,6 whole banks Q+delta<S4; neutral d6 entropy changes despite equal influence. 8637 assertions PASS in {validation["runtime_seconds"]:.3f}s. Premature checker launch before setup helper copy failed at import only; waited and unchanged checker passed. Saved source-bound review, finite certificates and rolling files; arbitrary history reserve and FEI open.\n'
if 'Stage 5 accepted A003 sharp retained point allowance' not in (HOME/'WORKLOG.md').read_text(encoding='utf-8'):
 with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(log)
lesson='Stage 5 durable facts: A003-RETAINED-POINT-SHADOW-SHARP-ALLOWANCE@1 accepted by A004 for the new all-d positive point bound; A003 independent acceptance of A004 prior criterion consumed. A0=2/ln2-2 bits =2-2ln2 nats; A1=2/ln2-1 bits =2-ln2 nats. A vertex flip at k incident pivots changes I by2delta(d-2k), but fair terminal capacity byKdelta(d-2k); retain destroyed debit -2Kkdelta and half entropy change. All1060 d<=3 point edits have Q<=S4, exact normalized max12-(49/4)log7+(25/2)log5-(9/2)log3 in(-.499,-.498). Padded AND3 origin edits d4/5/6 have k3 and Q+delta<S4; d6 neutral I but entropy changes. These initial finite payments do not renew a bank at the next data split; continue with SAME remaining owner/reference.'
if lesson not in (HOME/'LEARNED.md').read_text(encoding='utf-8'):
 with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+lesson+'\n')
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and '__pycache__' not in str(p) and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000;receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=HOME/name;receipts.append({'path':'../../'+name,'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/RECEIPTS.json',{'status':'SAVED_LOCAL_READBACK_VERIFIED','at_utc':stamp,'files':receipts,'remote_or_shared_verification':False})
print(json.dumps({'status':'LOCAL_COMPLETE','schema':'PASS','main_assertions':validation['assertions'],'independent_source_review':1,'finite_certificate':1,'receipted_files':len(receipts)}))
