from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime,copy
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1];BASE=OWN.parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,x): (RUN/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pilot=json.loads((RUN/'out/PILOT_RESULTS.json').read_text(encoding='utf-8'))
main=json.loads((RUN/'out/MAIN_RESULTS.json').read_text(encoding='utf-8'))
assert main['status']=='PASS' and main['physical_prefix_query_cases']==29 and main['reset_cases']==58
assert main['positive_reset_cases']>0
save('out/EXACT_RESULTS.json',{'status':'PASS','physical_prefix_query_cases':29,'reset_reference_cases':58,
    'root_cases':5,'assertions':main['assertions'],'positive_reset_cases':main['positive_reset_cases'],
    'negative_reset_cases':main['negative_reset_cases'],'seconds':main['seconds'],
    'pilot_assertions_subset_not_added':pilot['assertions'],
    'all_parameter_scope':'Analytic proof in DERIVATION; finite data not extrapolated',
    'arithmetic':'Integer Walsh and physical edges; Fraction likelihoods and atom masses; rigorous outward atanh log intervals'})
save('out/LEAN_RECEIPT.json',{'status':'NOT_RUN_MEMORY_ADMISSION_FAILED','statement_file':'code/KeyStep.lean',
    'statement_sha256':sha(RUN/'code/KeyStep.lean'),'command':'python -X utf8 tools/memok.py',
    'admission_exit_code':1,'admission_output':'WAIT: physical free3.9GB (need4.0), commit free23.1GB (need8.0)',
    'compiler_started':False,'formal_target_verified':False,'scope':'Lean source written; no compiler result or theorem certification; analytic induction remains separately supplied'})
# Source statements are copied without changing their mathematical scope or original hash.
src_run=BASE/'agents/A095/runs/20261021T180853Z-account03-A095-restricted-result-extraction'
source_claim=copy.deepcopy(json.loads((src_run/'CLAIMS.json').read_text(encoding='utf-8'))[0])
plain=hashlib.sha256(source_claim['exact_statement'].encode('utf-8')).hexdigest()
source_claim['review_records'].append({'reviewer':'A094/account03/B19','at':NOW,'verdict':'HOLDS_AT_FULL_NAMED_SOURCE_SCOPE',
    'scope':'Entire A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY@1: signed profile, all-width root bound, every adaptive wide-only history, full actual terminal CE/KL and product-compatible arbitrary terminal. No narrow-query/reset scope attributed to the original.',
    'method':'Independent signed profile and literal physical path reconstruction; own original reference transport/edge checker with a new narrow-query extension',
    'proof':str(RUN/'DERIVATION.md'),'locator':'section1','validation':str(RUN/'out/MAIN_RESULTS.json'),
    'source_claims_sha256':sha(src_run/'CLAIMS.json'),'plain_statement_sha256':plain,
    'substantive_repair_supplied':False,'contributor_conflict':False})
source_claim['status']='INDEPENDENTLY_RECONSTRUCTED_AT_FULL_NAMED_SCOPE_LOCALLY'
statement='For every w>=4,m>=0, let M select the padded source h_w*h_2 and its all-zero full-point flip by one fresh fair selector, with the A095 support-completed source-spectrum incoming reference Q. Execute any finite adaptive wide-only tree; at its edited-path leaf of depth d expose one untouched width-two coordinate. Retain the complete inherited reference of its one-child and every other leaf, and every old complete query release. Reset only its zero-child, of original reach lambda=2^(-d-1), to Q_fresh=(1-eta)Q_can+eta U for any prescribed eta in[0,1/4], where Q_can is the support-completed source-spectrum reference for the actual residual source h_(w-d)*h_1, h_0=-1, with the same padding and selector, and U is uniform on every residual Fourier mask. The SAME original rate4 reserve satisfies 4I(M)-CE_root>395/256. The full reached fresh cost lambda CE_fresh<5/4 and exact reset substitution is lambda(CE_fresh-CE_old_zero). Consequently the complete old-query-release plus after-reset terminal CE ledger is strictly less than4I(M)-75/256; no ancestor bank is renewed and both full terminals remain. For eta=0 the reserve left is>139/256. Both queried children are nonconstant when d<w; d=w is an explicit boundary case. Any independent normalized positive-support finite-cost prescribed terminal reference retains its full additive CE and KL outside this core bank. Any finite subsequent no-reset continuation retains the same bound. This does not price repeated fresh resets or arbitrary Boolean cores and is not full FEI.'
new={'claim_id':'A094-NARROW-QUERY-PRESCRIBED-RESET-SAME-RATE4','version':1,'exact_statement':statement,
    'hypotheses':['Finite uniform Boolean cubes; information in bits and physical influences; ideal CE has separate integer-code rounding',
    'w>=4,m>=0; source h_w*h_2, all-zero edit, exact prescribed incoming support-completed reference',
    'Wide-only prefix may adapt/stop; only one edited-path leaf receives one narrow query and one prescribed fresh reset; eta in[0,1/4]',
    'Original physical reaches, complete old releases, inherited complementary child reference and all other terminal CE/KL retained; no descendant quota renewal',
    'Independent terminal normalized, finite-cost and positive on true support, unqueried; product-compatible zero-fiber posteriors'],
    'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
    'contributors':['A094/account03; A095 source-spectrum history and A086 full reconstruction are dependencies'],
    'proof_source':{'path':str(RUN/'DERIVATION.md'),'locators':'sections2–6','finite_certificate':str(RUN/'out/MAIN_RESULTS.json')},
    'proof_dependencies':[{'claim_id':'A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY','version':1,'status':'independently reconstructed here at full named scope; signed root estimate and complete reference inheritance used'}],
    'review_records':[],'status':'AUTHOR_ANALYTIC_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW',
    'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A086','A095','A097','A096','A039','B19','B20']}
claims=[source_claim,new];save('CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B19','packet_id':'A094',
    'gap_id':'C024-SAME-REFERENCE-PRESCRIBED-RESET-ORIGINAL-BANK','attempt_id':'A094-stage17-wide-to-narrow-reset',
    'method':'Full source-chain independent reconstruction; sharper original reserve; explicit residual sparse profile and full reset substitution',
    'mathematical_delta':'A095 all-width/all-padding/all-wide-history theorem independently HOLDS. New one narrow-query prescribed reset at SAME original rate4 after any wide prefix, eta<=1/4; full old releases and terminals retained; original surplus>395/256, fresh reached cost<5/4, final reserve>75/256. Full FEI remains OPEN.',
    'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SOURCE_RECONSTRUCTED; NEW_RESET_PROOF_REVIEW_PENDING; FULL_FEI_OPEN',
    'claim_versions_used':[{'claim_id':source_claim['claim_id'],'version':1,'scope':'full named scope; no reset attributed to source'}],
    'claims_created_or_changed':[x['claim_id'] for x in claims],
    'source_artifacts':['DERIVATION.md','out/SOURCE_RECEIPTS.json','out/MAIN_RESULTS.json','out/EXACT_RESULTS.json','out/HELPER_PROVENANCE.json','out/LEAN_RECEIPT.json'],
    'next_consumers':['A086','A095','A097','A096','B19','B20'],
    'next_action':'A086/A095 independently audit sparse residual-profile and exact reset substitution; then expose the remaining narrow coordinate and price a second specified reset from the SAME diminished ancestor reserve, preserving the actual first reset debit and complementary inherited terminals.',
    'stagnant_substantive_attempts':0,
    'blockers':['No arbitrary-core influence-priced incoming reference or repeated-reset universal invariant. Formal check not launched after memok exit1. External adoption/mirror and new independent review unverified.'],
    'packet_ids':['A094']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
paths=[BASE/'BOARD.md',BASE/'claude/B19/STREAM_NOTES.md',OWN/'runs/20261021T155244Z-account03-A094-proof-chain-challenger/REPORT.md',
    src_run/'CLAIMS.json',src_run/'DERIVATION.md',BASE/'agents/A086/runs/20261021T203248Z-account03-A086-joint-code-referee/CLAIMS.json',
    BASE/'agents/A086/runs/20261021T203248Z-account03-A086-joint-code-referee/RECONSTRUCTION.md',
    BASE/'agents/A097/runs/20261021T232544Z-account03-A097-cross-route-transfer/DERIVATION.md',
    Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in paths])
status=f'STATE: Stage17 saved: full A095 all-wide chain HOLDS; one narrow-query prescribed reset paid SAME original rate4, reserve>75/256;{main["reset_cases"]} reset cases/{main["assertions"]} exact checks PASS; FEI OPEN.\nNEXT: A086/A095 review; price second narrow query/reset from SAME diminished ancestor bank with actual first reset debit, all old releases and both complete inherited terminals retained.\n'
(OWN/'STATUS.md').write_text(status,encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{NOW} — Stage17: read full new A095/A086 all-wide source chain, accepted at exact scope. Proved explicit first narrow query/reset payment from sharper SAME root reserve; eta<=1/4 uniform contamination gives genuine positive excess in finite cases. {main["reset_cases"]} reset cases, {main["assertions"]} exact checks PASS ({main["positive_reset_cases"]} positive reset bills); pilot subset excluded from total. Full CE/KL terminals and old releases retained. Formal source saved but memok exit1 prevented compiler launch. Four protocol artifacts saved; FEI open, author reset theorem review pending.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage17 durable facts: distinguish root unused reserve4I_root-CE_root from surviving-terminal margin4E I_leaf-E CE_leaf. The h_w*h2 root has reserve>395/256 for every w>=4,m>=0. After any edited-path wide prefix, one narrow zero-child has explicit source h_t*h1 (sparse Fourier support2^t, t>=2). Its canonical complete fresh cost is<2 for t>=4 and<4 at all boundary t>=0. Quarter-uniform contamination adds<1/2 bit, so reached full reset bill<5/4. Exact substitution adds only lambda(CE_fresh-CE_old), preserving every old debit and complementary terminal; SAME root quota leaves>75/256. This is one reset, not a renewed descendant quota or a universal FEI invariant.\n')
proto=json.loads(paths[-1].read_text(encoding='utf-8'))['required_per_run']
assert all(set(c)==set(proto['claim_fields']) for c in claims)
assert set(progress)=={x.split(' (')[0] for x in proto['progress_fields']}
source_canonical=json.dumps({'exact_statement':source_claim['exact_statement'],'hypotheses':source_claim['hypotheses']},sort_keys=True,ensure_ascii=False,separators=(',',':'))
assert source_claim['statement_sha256']==hashlib.sha256(source_canonical.encode('utf-8')).hexdigest()
assert new['statement_sha256']==hashlib.sha256(new['exact_statement'].encode('utf-8')).hexdigest()
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
print(json.dumps({'saved':True,'assertions':main['assertions'],'reset_cases':58,'positive':main['positive_reset_cases']}))
