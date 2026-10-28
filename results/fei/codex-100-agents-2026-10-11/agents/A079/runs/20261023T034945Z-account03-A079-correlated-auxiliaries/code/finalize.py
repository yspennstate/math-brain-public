"""Schema/hash/persistence checks; writes only A079 artifacts and rolling files."""
from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
P=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
protocol=read(P);v=read(R/'out/validation.json');pilot=read(R/'out/pilot_summary.json');b=read(R/'out/boundary.json');spec=read(R/'FROZEN_SPEC.json');bspec=read(R/'BOUNDARY_SPEC.json')
assert v['status']==pilot['status']==b['status']=='PASS'
assert v['helper_sha256']==pilot['helper_sha256']==spec['sha256']==b['core_sha256']==sha(R/'code/check.py')
assert b['helper_sha256']==bspec['sha256']==sha(R/'code/boundary.py')
assert v['signed_cases']==2200 and v['query_actions']==6064 and v['assertions']==745981
assert pilot['signed_cases']==64 and pilot['query_actions']==200 and pilot['assertions']==45740
assert b['signed_cases']==64 and b['query_actions']==144
assert v['seconds']<180 and pilot['seconds']<55 and b['seconds']<45
assert (R/'FROZEN_SPEC.json').stat().st_mtime < (R/'out/pilot_summary.json').stat().st_mtime-pilot['seconds']
assert (R/'BOUNDARY_SPEC.json').stat().st_mtime < (R/'out/boundary.json').stat().st_mtime-b['seconds']
audit=read(R/'out/adversarial_audit.json');aspec=read(R/'AUDIT_SPEC.json')
assert audit['status']=='PASS' and audit['delayed_two_query_paths']==16 and audit['beta_transitions']==108
assert audit['helper_sha256']==aspec['sha256']==sha(R/'code/audit.py') and audit['core_sha256']==sha(R/'code/check.py')
assert audit['seconds']<45
assert read(R/'out/funded_fixture.json')['status']=='PASS' and read(R/'out/support_guard.json')['status']=='PASS'
orig=BASE/'agents/A032/runs/20261023T013017Z-account03-A032-boolean-phase-realizability'
sourceclaims=read(orig/'CLAIMS.json')
source=next(x for x in sourceclaims if x['claim_id']=='A032-SIGNED-TAG-VACUUM-TAIL-RESET')
old=next(x for x in sourceclaims if x['claim_id']=='A079-TAGGED-REFERENCE-SAME-BANK-LIFT')
assert source['statement_sha256']=='a8eaef0443d2816feeef2b939d7fd28498792dd1561d0bd3da7168a2e134885e'
source=dict(source);source['review_records']=list(source['review_records'])+[dict(reviewer='A079',at=stamp,verdict='HOLDS_AT_STATED_SCOPE',source=str(R/'REVIEW_A032.md'),method='Independent signed Fourier reconstruction and direct-character exact reset identities, prime-log KL and integer-power signs; no author code or repair',formal_verification='NOT_CLAIMED')]
source['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A079_LOCAL_REGISTRY_ADOPTION_UNVERIFIED'
old=dict(old);old['status']='A032_INDEPENDENT_ACCEPTANCE_CONSUMED_BY_A079_UNCHANGED_STATEMENT'
statement=('For the actual Boolean F=a+z*b*h with A079 fixed four-bit complementary rows a,b, '
'let a normalized finite-CE source reference and all previous source/controller debits already be paid. '
'After the signed z reset, references with each true signed vacuum atom and tail b_hat(U)^2 times '
'a calibrated supplied seed reference are closed under every finite adaptive mixed controller/seed '
'query tree with prescribed coherent CURRENT-reference block calibrations: each exact local '
'erasure-plus-mean-child-CE increment equals minus the conditional occupancy KL minus the mean '
'of both child block KLs. For seed queries the partition has individual vacuum atoms and one entire '
'tail block; for controller queries it has individual vacuum atoms and one tail block per remaining '
'controller frequency. All full terminal normalizers, signed vacuum collisions, reference-only '
'atoms and old debits are accounted for. At the ORIGINAL root, if E h=+/-1/2 and R(empty)=1/2, '
'A032 first tail mixture of ANY prescribed target at weight1/8 saves strictly more than1/64. '
'After arbitrary paid coherent continuations, a SECOND genuine conditional-nonempty profile change '
'to63/64 of its CURRENT tail plus1/64 of ANY prescribed normalized target may be performed on '
'ANY adaptive antichain across BOTH z branches. Its total added CE is at most(3/8)log2(64/63) '
'<3/256, because reach-weighted beta sums to at most3/8. Therefore the SAME original account '
'funds it and retains strictly more than1/256, with no influence-rate increase or reserve renewal; '
'later current-reference coherent calibrations remain paid. Constant seeds and zero sectors use '
'the explicit point-law formulas without tail division. The exact non-point four-bit seed negative '
'at indices{0,1,2,4} has two nonconstant active-bit children of means1/4,3/4 and realizes both '
'tail mixtures and a subsequent physical query. Entropy/CE/KL units are bits. No universal '
'initial influence price, unlimited target-profile changes or full FEI is asserted.')
claim={'claim_id':'A079-POST-TAG-SECOND-TAIL-RESET-SAME-REFUND','version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean independent uniform physical cubes; displayed complementary rows and actual signed means',
 'Initial normalized finite-CE source and every earlier debit are already paid; no arbitrary-seed price supplied',
 'Explicit numeric refund only at original root beta=3/8, mean+/-1/2, source empty1/2, first target mixture1/8',
 'Second mixture1/64 performed once on an adaptive antichain; BOTH tag branches and every complementary full terminal retained',
 'Intervening and later resets are the prescribed CURRENT-reference block calibrations, not arbitrary tail reoptimization',
 'All entropy/CE/KL bits; zero sectors and constant seeds handled explicitly'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A079'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':['out/validation.json','out/boundary.json','out/funded_fixture.json','out/support_guard.json','out/adversarial_audit.json'],'formal_verification':'NOT_CLAIMED'},
 'proof_dependencies':[{'claim_id':source['claim_id'],'version':1,'statement_sha256':source['statement_sha256'],'scope':'Independently accepted exact first-reset refund; reconstructed again in PROOF section1'},
 {'claim_id':old['claim_id'],'version':1,'statement_sha256':old['statement_sha256'],'scope':'Conditional supplied initial source/history admission only; no new universal price'}],
 'review_records':[],'status':'AUTHOR_PAPER_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A032','A088','A094','A096','A097','B16','B20']}
claims=[old,source,claim]
for c in claims:
 assert set(c)==set(protocol['required_per_run']['claim_fields'])
 assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest()
save(R/'CLAIMS.json',claims)
next_action=('Review second genuine tail reset at SAME ancestor account; then fund a conditional-nonempty '
'profile change for an arbitrary seed using physical phase energy or a proved amortized source inequality, '
'without an initially assumed entropy price or renewal of the finite gadget refund. A032/A088/A094 '
'review; A096/A097 consume exact non-point source fixture at unchanged admission.')
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B16','packet_id':'A079',
 'gap_id':'G-PHASE-COND','attempt_id':'A079-stage8-post-tag-second-tail-reset-same-refund-v1',
 'method':'Independent A032 signed reset review; coherent vacuum/tail block-KL projection; reach-beta martingale; second nonempty profile target funded from actual saved first refund',
 'mathematical_delta':'A032 signed tag reset independently HOLDS; A032 acceptance of prior lift consumed. Arbitrary current coherent seed/controller calibrations paid; SECOND genuine1/64 tail change on an adaptive frontier funded by original first refund>1/64 with>1/256 left, both complete terminals retained. Universal source price remains OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_PROOF_REVIEW_EXACT_CERTIFICATES',
 'mathematical_status':'FULL_FEI_OPEN; new conditional extension author-proved and exactly checked; external independent review pending; formal verification not claimed',
 'claim_versions_used':[{'claim_id':c['claim_id'],'version':1,'statement_sha256':c['statement_sha256']} for c in (old,source)],
 'claims_created_or_changed':[old['claim_id']+'@1: A032 acceptance consumed',source['claim_id']+'@1: A079 independently HOLDS',claim['claim_id']+'@1'],
 'source_artifacts':['REPORT.md','PROOF.md','REVIEW_A032.md','CLAIMS.json','FROZEN_SPEC.json','FROZEN_SPEC_v1.json','BOUNDARY_SPEC.json','code/check.py','code/check_v1.py','code/boundary.py','out/validation.json','out/pilot_summary.json','out/boundary.json','out/funded_fixture.json','out/support_guard.json','out/ATTEMPT1.json','out/SOURCE_MANIFEST.json','out/PERSISTENCE_RECEIPT.json','AUDIT_SPEC.json','code/audit.py','out/adversarial_audit.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal initial influence-priced source remains OPEN','Unlimited new nonempty-tail targets not paid; finite refund cannot be renewed','New extension independent review, registry/mirror adoption and formal verification unverified'],
 'packet_ids':['A079']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
sources=[]
def rec(p,role):sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'role':role})
rec(P,'execution protocol read in full')
rec(BASE/'BOARD.md','selected related rows read at stage start; hash at final save of live file')
rec(BASE/'claude/B16/STREAM_NOTES.md','lead v2 read in full')
for name in ['PROOF.md','CLAIMS.json','REPORT.md']:rec(orig/name,'A032 current reset statement and proof independently reviewed')
for agent,run in [('A096','20261023T010221Z-account03-A096-live-gap-ledger'),('A097','20261023T021120Z-account03-A097-cross-route-transfer')]:rec(BASE/'agents'/agent/'runs'/run/'DERIVATION.md','read context; not an unreviewed theorem premise')
rec(OWN/'runs/20261022T225318Z-account03-A079-correlated-auxiliaries/code/check.py','previous productive exact helper inspected; no A032 implementation copied')
save(R/'out/SOURCE_MANIFEST.json',{'saved_at':stamp,'sources':sources,'wake':'DEGRADED_UNVERIFIED_STALE_OWNER_MODEL_AND_STATE_CONTEXT_NOT_USED','math_recall':'one multiwording read-only weak match; no answering card used','remote_persistence':'UNVERIFIED'})
rp=R/'REPORT.md';text=rp.read_text(encoding='utf-8')
text=text.replace('FINAL_VALIDATION_PLACEHOLDER',f'Final PASS: {v["assertions"]} exact assertions in {v["seconds"]:.4f}s. A separately frozen sparse-support boundary check passed {b["assertions"]} assertions on64 signed fixtures/144 queries in {b["seconds"]:.4f}s; it uses true-support-only old references, empty-zero/point endpoints and point targets that introduce reference-only labels. Counts are separate, not pooled. Outputs: out/validation.json and out/boundary.json.')
rp.write_text(text,encoding='utf-8',newline='')
assert 'FINAL_VALIDATION_PLACEHOLDER' not in text
for h in protocol['required_per_run']['report_fields']:assert '# '+h in text
assert text.rstrip().endswith('of the fixed controller reserve.')
state=(f'STATE: Stage8 saved: A032 signed reset independently HOLDS; second genuine1/64 tail change paid from SAME tag refund with>1/256 left; {v["assertions"]} main + {b["assertions"]} boundary +2781 adversarial exact checks PASS; FEI OPEN.\n'
'NEXT: A032/A088/A094 review second tail reset; A096/A097 consume non-point source. Fund arbitrary-seed nonempty-profile liability from physical phase energy, without assumed initial source price or finite-refund renewal.\n')
(OWN/'STATUS.md').write_text(state,encoding='utf-8',newline='')
marker=R.name
wp=OWN/'WORKLOG.md';w=wp.read_text(encoding='utf-8')
if marker not in w:
 with wp.open('a',encoding='utf-8',newline='') as f:f.write(f'\n{stamp} {marker}: Stage8 independently accepted A032 signed-tag reset@1 and consumed A032 review of prior lift. Derived exact current coherent block-calibration chain after seed/controller queries, then funded SECOND genuine1/64 conditional-tail target from retained first tag refund>1/64; original bank unchanged, reserve>1/256. Pilot45740/1.5016s; full745981/24.4162s; boundary{b["assertions"]}/{b["seconds"]:.4f}s PASS, separate counts. First pilot strict beta=0 checker error retained and fixed; no author theorem repair. Actual n4 seed active children means1/4,3/4 both nonconstant; four signed terminals and later query verified. New extension awaits external review; full FEI/source price OPEN. No research left running.\n')
lp=OWN/'LEARNED.md';l=lp.read_text(encoding='utf-8')
if marker not in l:
 with lp.open('a',encoding='utf-8',newline='') as f:f.write('\n'+stamp+' '+marker+' durable facts:\n- A032-SIGNED-TAG-VACUUM-TAIL-RESET@1 independently HOLDS without repair; source signed mean cannot be replaced by sqrt(reference vacuum), which can create occupied zero and infinite CE.\n- After z deletion coherent reference has actual signed vacuum and B_U^2 times supplied calibrated seed tail. A seed query plus fresh coherent reset is exact block calibration (individual vacuum atoms, ONE entire tail); controller query uses individual vacuum atoms plus ONE tail block per remaining U. Local erasure/reset increment is -conditional occupancy KL -mean of BOTH full child block KLs. Arbitrary finite mixed adaptive continuations paid, not arbitrary target-tail reoptimization.\n- At original beta3/8, actual seed mean+/-1/2, source empty1/2, first1/8 target mixture saves>1/64. A SECOND genuine1/64 conditional-tail target on ANY adaptive antichain costs at most(3/8)log2(64/63)<3/256, retaining>1/256 from SAME first refund. Integer certificates21^18>2^79 and64^32<2*63^32. No reserve renewal at descendants.\n- Non-point n4 seed with negatives{0,1,2,4} has active bit0 children means1/4,3/4, both nonconstant; full signed terminals and follow-on query realized exactly. Initial arbitrary-seed CE still has no universal influence price. Scalar KL/calibration identities are not new Booleanity admission constraints.\n- New extension paper proof and exact certificates await independent review. Full FEI remains OPEN; zero universal constant improvement.\n')
(R/'CHECKPOINT.md').write_text('COMPLETE_LOCAL: proof/review and exact main/boundary certificates saved. New extension pending independent review. No stage research process left running. FEI and universal initial source pricing OPEN.\n',encoding='utf-8',newline='')
assert len(state.splitlines())==2 and (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
save(R/'out/PERSISTENCE_RECEIPT.json',dict(status='PASS_LOCAL_SCHEMAS_HASHES_RESULTS_AND_FILES_VERIFIED',saved_at=stamp,files=files,main_assertions=v['assertions'],boundary_assertions=b['assertions'],adversarial_assertions=audit['assertions'],pilot_assertions_separate=pilot['assertions'],progress_delta_identical=True,formal_proof='NOT_CLAIMED',new_claim_independent_review='PENDING',remote_mirror='UNVERIFIED',rolling=[{'path':str(p),'sha256':sha(p)} for p in (OWN/'STATUS.md',wp,lp)]))
print(json.dumps(dict(status='PASS',files=len(files),main_assertions=v['assertions'],boundary_assertions=b['assertions'],pilot_assertions=pilot['assertions'],FEI='OPEN',new_review='PENDING',research_running=False)))
