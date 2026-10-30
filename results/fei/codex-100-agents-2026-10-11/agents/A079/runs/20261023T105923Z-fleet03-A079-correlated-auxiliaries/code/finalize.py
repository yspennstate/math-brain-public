"""A079-only protocol persistence; does not publish or mutate shared sources."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
BASE=OWN.parents[1];stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
PROTOCOL=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
protocol=read(PROTOCOL);v=read(R/'out/validation.json');pilot=read(R/'out/pilot.json');ind=read(R/'out/independent.json');spec=read(R/'FROZEN_SPEC.json');isp=read(R/'INDEPENDENT_SPEC.json')
assert v['status']==pilot['status']==ind['status']=='PASS'
assert v['helper_sha256']==pilot['helper_sha256']==spec['sha256']==sha(R/'code/check.py')
assert ind['helper_sha256']==isp['sha256']==sha(R/'code/independent.py')
old=OWN/'runs/20261023T034945Z-fleet03-A079-correlated-auxiliaries/code/check.py'
assert v['inherited_helper_sha256']==pilot['inherited_helper_sha256']==sha(old)
assert (v['assertions'],v['candidates'],v['admitted_zero_singleton'],v['isospectral_cases'])==(282717,3200,888,600)
assert (pilot['assertions'],pilot['candidates'],pilot['admitted_zero_singleton'])==(8200,128,48)
assert ind['transactions']==40 and ind['assertions']==7120
assert v['seconds']<120 and pilot['seconds']<55 and ind['seconds']<30
assert (R/'FROZEN_SPEC.json').stat().st_mtime < (R/'out/pilot.json').stat().st_mtime-pilot['seconds']
assert (R/'INDEPENDENT_SPEC.json').stat().st_mtime < (R/'out/independent.json').stat().st_mtime-ind['seconds']
phase=read(R/'out/review_A097.json');assert phase['status']=='PASS' and phase['transactions']==152
assert read(R/'out/sharp_zero_phase.json')['status']=='PASS'
src=BASE/'agents/A097/runs/20261023T062140Z-fleet03-A097-cross-route-transfer'
claims=read(src/'CLAIMS.json');source=next(c for c in claims if c['claim_id']=='A097-NONEMPTY-PHASE-BIN-FUNDED-TRANSFER')
assert source['statement_sha256']=='f8ee94db650f099b036f174a5e9d21989eee7c6110efd02901221b86b631a6a8'
review=dict(source);review['review_records']=list(source['review_records'])+[dict(reviewer='A079',at=stamp,verdict='HOLDS_AT_STATED_SUPPLIED_SOURCE_SCOPE',source=str(R/'REVIEW_A097.md'),method='Independent common-reference Pinsker/Gram/bin proof reconstruction, direct-character full CE/erasure checks; no author code or repair',formal_verification='NOT_CLAIMED')]
review['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A079_LOCAL_REGISTRY_ADOPTION_UNVERIFIED'
statement=('For ANY actual complementary physical rows a in{-1,0,1}, b=1-a^2 and independent Boolean '
'seed h, let G=a+sigma*b*h, beta=E b^2, m=E h, r=m^2,t=1-r. Supply a normalized finite-CE '
'seed reference R with R(empty)=r and its complete coherent signed wrapper reference. At EVERY '
'actual seed query i with hhat({i})=0, put rho=R({i}),theta=rho/t when t>0. Finiteness forces '
'theta<1. Let D_* be weighted conditional occupancy KL on all NONEMPTY remaining-frequency '
'pairs. Relative to the SAME current incoming reference, the exact physical erasure plus mean '
'of BOTH coherent child references formed by marginalizing R and calibrating its empty mass '
'back to r has increment -beta*D_*-beta*t*log2(1/(1-theta)). Hence a genuine change of each '
'conditional nonempty tail toward ANY prescribed normalized target with weight lambda_child<=theta '
'is funded at unchanged incoming account; lambda=theta/2 retains beta*D_*+beta*t*log2((1-theta/2)/(1-theta)). '
'Every old debit and complete terminal remains, and eligible finite histories telescope without '
'reissuing ghost credit. Constant seeds and beta=0 use explicit zero-tail conventions. This '
'includes ISOSPECTRAL zero-phase queries. For the original A079 mask and parity3 query, incoming '
'R=(1-rho)delta_123+rho delta_1 and new tail(1-lambda)delta_23+lambda delta_2 have exact full '
'increment(3/8)log2((1-rho)/(1-lambda)); both actual children are nonconstant and phase energy0. '
'Thus the worst-case lambda<=rho threshold is SHARP. Creating singleton ghost fraction theta '
'from a calibrated reference with zero such mass costs EXACTLY beta*t*log2(1/(1-theta)), so '
'manufacturing the credit is prepayment. All CE/KL/entropy units are bits. No initial universal '
'influence price, zero-credit arbitrary conversion or full FEI theorem is asserted.')
claim={'claim_id':'A079-ZERO-SINGLETON-GHOST-CREDIT-SHARP','version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean complementary rows and seed on independent uniform physical cubes; actual Fourier phases',
 'Normalized finite-CE source calibrated at actual squared mean; immediately incoming wrapper reference is the displayed coherent reference',
 'Actual queried singleton coefficient is zero; source ghost rho is read from CURRENT reference, never newly assumed free',
 'Both complete actual child references and all earlier source/tag/reset debits retained; original influence price is supplied if used',
 '0<=lambda_child<=theta; arbitrary zero-credit conversions or source reoptimization not admitted',
 'Explicit constant/zero-sector endpoint rules; all entropy/CE/KL bits'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A079'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':['out/validation.json','out/independent.json','out/sharp_zero_phase.json'],'formal_verification':'NOT_CLAIMED'},
 'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PAPER_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A097','A096','A032','A088','A094','B16','B20']}
for c in (review,claim):
 assert set(c)==set(protocol['required_per_run']['claim_fields'])
 assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest()
save(R/'CLAIMS.json',[review,claim])
next_action=('A097/A096/A032/A088/A094 review exact ghost credit and prepayment. Consume A094 A011 '
'source-prefix audit: identify one REQUIRED conversion with d=phase=rho=D_*=0 and pay it from '
'SAME unused original C0/U_star account, or prove it avoidable; retain full arbitrary-core price, '
'all previous debits and BOTH complete terminals. No manufactured ghost or fixed-bank renewal.')
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B16','packet_id':'A079',
 'gap_id':'G-PHASE-COND','attempt_id':'A079-stage9-zero-singleton-ghost-credit-sharp-v1',
 'method':'Independent A097 two-bin review; exact full erasure/conditional-occupancy ledger; singleton ghost credit; genuine conditional-tail mixture; sharp Boolean parity witnesses and exact prepayment guard',
 'mathematical_delta':'A097 supplied two-bin phase theorem independently HOLDS. Zero-singleton reference ghost rho funds ANY nonempty target at weight<=rho/(1-m^2), including isospectral phase-energy0; exact credit and parity sharpness proved. Ghost creation costs exactly its later refund. Universal initial price and zero-credit necessary conversions remain OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_PROOF_REVIEW_EXACT_CERTIFICATES',
 'mathematical_status':'FULL_FEI_OPEN; new exact conditional theorem pending independent review; formal verification not claimed',
 'claim_versions_used':[{'claim_id':source['claim_id'],'version':1,'statement_sha256':source['statement_sha256'],'scope':'independently reviewed; related context, not premise of new exact identity'}],
 'claims_created_or_changed':[source['claim_id']+'@1: independently HOLDS',claim['claim_id']+'@1'],
 'source_artifacts':['REPORT.md','PROOF.md','REVIEW_A097.md','CLAIMS.json','FROZEN_SPEC.json','INDEPENDENT_SPEC.json','code/check.py','code/independent.py','out/validation.json','out/pilot.json','out/independent.json','out/review_A097.json','out/sharp_zero_phase.json','out/SOURCE_MANIFEST.json','out/CHECKLIST_RECEIPT.json','out/PERSISTENCE_RECEIPT.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary Boolean initial source still influence-unpriced','Necessary conversions in d=phase=rho=D_*=0 nullspace not paid','New theorem independent review, registry/remote adoption and formal verification unverified'],
 'packet_ids':['A079']}
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
sources=[]
def rec(p,role):sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'role':role})
rec(PROTOCOL,'schemas reread; complete protocol read earlier in same conversation')
rec(BASE/'BOARD.md','related rows read at stage start; final live-file hash')
rec(BASE/'claude/B16/STREAM_NOTES.md','lead v2 read in full')
rec(src/'DERIVATION.md','A097 theorem independently reconstructed')
rec(src/'CLAIMS.json','exact statement copied and hash-verified for scoped review')
rec(BASE/'agents/A032/runs/20261023T054918Z-fleet03-A032-boolean-phase-realizability/PROOF.md','read arbitrary retained-core frontier; no upstream price assumed')
rec(old,'A079 inherited exact arithmetic helper; no reviewed-author implementation copied')
save(R/'out/SOURCE_MANIFEST.json',dict(saved_at=stamp,sources=sources,wake='FRESH_SESSION_WAKE_COMPLETED_WITH_OWNER_ALERT; owner97.4h/state82h/dream32.7h stale; disclosed, not used as premises',remote_persistence='UNVERIFIED',external_brain_write='NONE_BY_RESEARCH_SCRIPTS'))
rp=R/'REPORT.md';text=rp.read_text(encoding='utf-8').replace('INDEPENDENT_RESULT_PLACEHOLDER',f'Independent PASS{ind["assertions"]} exact assertions in{ind["seconds"]:.4f}s. Counts are separate, not pooled with the main or pilot.')
rp.write_text(text,encoding='utf-8',newline='')
assert 'INDEPENDENT_RESULT_PLACEHOLDER' not in text
for h in protocol['required_per_run']['report_fields']:assert '# '+h in text
assert text.rstrip().endswith('or an impermissible renewal of a fixed auxiliary reserve.')
(OWN/'STATUS.md').write_text('STATE: Stage9 saved: A097 two-bin theorem independently HOLDS; zero-singleton ghost funds SHARP lambda<=rho/(1-m^2), even isospectral phase0;282717 main+7120 independent exact checks PASS; FEI OPEN.\nNEXT: A097/A096/A032/A094 review; consume A094 A011 source-prefix audit to pay REQUIRED zero-credit conversion from SAME original C0/U_star or prove avoidable; ghost creation is exact prepayment, not universal source price.\n',encoding='utf-8',newline='')
marker=R.name
for name in ['WORKLOG.md','LEARNED.md']:
 p=OWN/name;s=p.read_text(encoding='utf-8')
 if marker not in s:
  with p.open('a',encoding='utf-8',newline='') as f:
   f.write('\n'+stamp+' '+marker+': A097 nonempty-phase-bin@1 independently HOLDS without repair. New exact zero-singleton identity: full erasure+mean child CE-parentCE=-beta D_* -beta(1-m^2)log2(1/(1-theta)), theta=R({i})/(1-m^2). ANY genuine nonempty target mixture lambda<=theta paid from SAME current ghost credit, even isospectral phase energy0; lambda=theta/2 retains explicit release. Actual parity3 source(1-rho)delta123+rho delta1 gives SHARP increment(3/8)log2((1-rho)/(1-lambda)); at rho1/32 fixed1/64 target releases(3/8)log2(63/62), at rho0 or1/128 costs positively. Ghost injection costs EXACTLY its later refund, so no universal source price is gained. Pilot8200/0.6283s; main282717/55.8115s (3200 candidates,888 admitted,600 iso/288 noniso,152 reviewed phase transactions); independent butterfly audit7120/0.6591s,40 transactions/80 complete terminals. New theorem awaits external review; FEI OPEN. Fresh wake stale owner/state/dream disclosed. No research left running.\n')
(R/'CHECKPOINT.md').write_text('COMPLETE_LOCAL: full ghost-credit proof and A097 independent review saved;282717 main+7120 independent certificates PASS. New theorem external review pending; zero-credit necessary conversion and universal initial source price OPEN. No research running.\n',encoding='utf-8',newline='')
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
save(R/'out/PERSISTENCE_RECEIPT.json',dict(status='PASS_LOCAL_PROTOCOL_SCHEMAS_HASHES_AND_COMPLETED_CERTIFICATES',saved_at=stamp,files=files,main_assertions=v['assertions'],independent_assertions=ind['assertions'],pilot_assertions_separate=pilot['assertions'],new_claim_review='PENDING',formal_proof='NOT_CLAIMED',remote_copy='UNVERIFIED',rolling=[{'path':str(p),'sha256':sha(p)} for p in (OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md')]))
print(json.dumps(dict(status='PASS',files=len(files),main=v['assertions'],independent=ind['assertions'],FEI='OPEN',new_review='PENDING',research_running=False)))
