from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];OWN=R.parents[1];BASE=OWN.parents[1];O=R/'out';now=datetime.now(timezone.utc).isoformat()
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
v=json.loads((O/'validation.json').read_text(encoding='utf-8'));ind=json.loads((O/'independent.json').read_text(encoding='utf-8'))
assert v['PASS'] and ind['PASS'] and v['controller_seed_pairs']==2038 and ind['fixtures']==2
assert v['seconds']<180 and ind['seconds']<45
P=Path(r'math-open-problems/reports\fei-2026-10-11')
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
src=BASE/'agents/A079/runs/20261022T225318Z-account03-A079-correlated-auxiliaries'
claims=json.loads((src/'CLAIMS.json').read_text(encoding='utf-8'))
c=next(x for x in claims if x['claim_id']=='A079-TAGGED-REFERENCE-SAME-BANK-LIFT')
assert sh(src/'PROOF.md')==c['proof_source']['sha256']
c['review_records'].append({'reviewer':'A032','at':now,'verdict':'HOLDS_AT_STATED_SCOPE','source':str(R/'REVIEW_A079.md'),'method':'Independent full normalized-reference factorization, source/controller local erasure interface and finite-tree induction; no author code or repair','formal_verification':'NOT_CLAIMED'})
c['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A032_LOCAL_ADOPTION_UNVERIFIED'
statement=('For the actual Boolean F_h=a+z*b*h with A079 fixed four-bit ternary row a and b=1-a^2, after ANY physical controller restriction, let A=ahat,B=bhat,beta=E b^2,m=E h,r=m^2,p=hhat^2. For EVERY normalized source reference R of finite CE(p,R), t=R(empty), every normalized prescribed nonempty-frequency law S and0<=epsilon<1, define M=(1-epsilon)R_tail+epsilon S and complete fresh child references Q_sigma(U,empty)=(A_U+sigma*m B_U)^2 and Q_sigma(U,T)=B_U^2*(1-r)*M_T for T nonempty. Constant-seed and zero-sector endpoints use the explicit formulas in PROOF.md without tail division. Relative to the full normalized incoming tagged reference Q(0,U,T)=A_U^2*1[T=empty], Q(1,U,T)=B_U^2 R_T, the exact erasure-plus-mean-child-CE reset increment is -JS_z-beta*d(r||t)+beta*(1-r)*(D(p_tail||M)-D(p_tail||R_tail)). Hence it is nonpositive whenever (1-r)*log2(1/(1-epsilon))<=d(r||t). Both actual signed child spectra and all prior source/controller debits remain; eligible frontier replacements and subsequent current-reference no-reset queries preserve the SAME already paid incoming source account. At the original root, for EVERY Boolean seed of mean+/-1/2, t=1/2 and epsilon=1/8 fund ANY prescribed S with increment strictly below-1/64. The actual seed[-1,1,1,1] and positive source reference[1/9,8/27,8/27,8/27] show that substituting sqrt(t)=1/3 for actual m=1/2 in the coherent minus-child vacuum creates normalized reference mass0 at a true atom of mass1/256, so child CE is infinite. All CE/KL/entropy units are bits. No universal initial source price, generic arbitrary reset or full FEI theorem is asserted.')
n={'claim_id':'A032-SIGNED-TAG-VACUUM-TAIL-RESET','version':1,'exact_statement':statement,
'hypotheses':['Actual Boolean independent uniform physical cubes and displayed complementary rows, including their actual restricted signs','Normalized finite-CE supplied source reference; it is already paid for the history application','Both full actual z children retained; fresh tail S is normalized and0<=epsilon<1','Free reset requires the explicit binary-KL/likelihood-floor eligibility condition; no arbitrary source price or bank renewal','Entropy, cross entropy and KL in bits; actual original physical influences'],
'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A032'],
'proof_source':{'path':str(R/'PROOF.md'),'sha256':sh(R/'PROOF.md'),'certificates':['out/validation.json','out/independent.json','out/fixed_resets.json','out/support_obstruction.json'],'formal_verification':'NOT_LAUNCHED_MEMORY_GATE'},
'proof_dependencies':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'scope':'Independently accepted supplied paid interface for the history application; reset algebra reconstructed directly'}],
'review_records':[],'status':'AUTHOR_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A079','A034','A033','A088','A094','A096','A097','B07-lead','B20']}
outclaims=[c,n]
for x in outclaims:
    assert set(x)==set(protocol['required_per_run']['claim_fields'])
    assert hashlib.sha256(x['exact_statement'].encode('utf-8')).hexdigest()==x['statement_sha256']
save(R/'CLAIMS.json',outclaims)
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B07','packet_id':'A032','gap_id':'G-PHASE-COND','attempt_id':'A032-stage18-signed-tag-tail-reset-v1',
'method':'Consume A079 paid-source lifting; actual signed tag collision; exact source occupancy KL finances a prescribed tail-reference mixture; independent direct truth-table support and CE certificate',
'mathematical_delta':'A079 tagged same-bank lift independently HOLDS; one fresh reset after tag deletion paid under explicit likelihood floor, with arbitrary target tail weight1/8 and>1/64 release for mean+/-1/2 and incoming vacuum1/2. Exact actual-Boolean occupied-zero witness rejects naive reference-derived phase. Universal initial source price remains OPEN.',
'deliverable_status':'COMPLETE_LOCAL; independent review and remote adoption unverified','mathematical_status':'CONDITIONAL_REFERENCE_TRANSFER_PROOF_EXACT_CERTIFICATES; FULL_FEI_OPEN; NO_LEAN_CERTIFICATE',
'claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'acceptance':'A032 independent reconstruction HOLDS at stated paid-source scope'}],
'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Local independent review appended'},{'claim_id':n['claim_id'],'version':1,'change':'New conditional reset and actual-Boolean support obstruction'}],
'source_artifacts':['PROOF.md','REVIEW_A079.md','FROZEN_SPEC.json','PILOT_SPEC.json','FULL_REPLAY_SPEC.json','INDEPENDENT_SPEC.json','code/check.py','code/independent.py','out/validation.json','out/independent.json','out/support_obstruction.json','out/ATTEMPTS.json','out/SOURCE_RECEIPTS.json'],
'next_consumers':n['next_consumers'],
'next_action':'From the resulting signed child reference with its actual1/8 target component and prior tag/reset debit, expose one active seed bit and price a specified next fresh reference from SAME remaining source account, keeping both complete child terminals.',
'stagnant_substantive_attempts':0,'blockers':['Universal initially influence-priced source interface unpaid','Arbitrary later reset without floor/refund or unused bank unpaid','New conditional reset external independent review pending','Lean admission failed; no compiler launched','Supervisor publication, registry adoption and remote persistence unverified'],
'packet_ids':['A032']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
formal={'status':'NOT_LAUNCHED_MEMORY_GATE','memok_exit':1,'observed_stdout':'WAIT: physical free 1.6 GB (need 4.0), commit free 18.8 GB (need 8.0)','source':str(R/'code/Core.lean'),'source_sha256':sh(R/'code/Core.lean'),'target':'A032_reset_power_guard','compiler_launched':False,'meaning':'Only integer guard prepared; no target/compiler/axiom certificate and no formal entropy translation'}
save(O/'formal_attempt.json',formal)
paths=[(BASE/'BOARD.md','Stage-start peer frontier inspected; end-stage source bytes pinned here'),(BASE/'claude/B07/STREAM_NOTES.md','Lead v2; old finite endpoint retired'),(OWN/'STATUS.md','Prior checkpoint before rolling update'),(P/'EXECUTION_PROTOCOL.json','Full current schema read'),(OWN/'runs/20261021T215120Z-account03-A032-boolean-phase-realizability/PROOF.md','Own previous actual-controller proof'),(OWN/'runs/20261021T215120Z-account03-A032-boolean-phase-realizability/REPORT.md','Prior stage scopes, exact certificates and next unpaid action'),(src/'PROOF.md','Full source paid-interface proof reconstructed'),(src/'CLAIMS.json','Exact accepted source version'),(src/'HANDOFF.md','Explicit post-tag fresh-reset boundary'),(BASE/'agents/A033/runs/20261022T210100Z-account03-A033-derivative-hierarchy/NO_GO.md','Actual-Boolean fixed-controller all-history obstruction inspected, not adopted as new proof premise'),(BASE/'agents/A096/runs/20261023T010221Z-account03-A096-live-gap-ledger/DERIVATION.md','Sections1--2 current-vacuum calibration context; not an assumed unreviewed theorem')]
manifest=[]
for p,role in paths:
    text=p.read_text(encoding='utf-8');manifest.append({'path':str(p),'sha256':sh(p),'bytes':p.stat().st_size,'read_role':role})
save(O/'SOURCE_RECEIPTS.json',manifest)
count=v['checks']+ind['checks']
old=(OWN/'STATUS.md').read_text(encoding='utf-8')
(OWN/'STATUS.md').write_text(f'STATE: Stage18 saved: A079 paid-source lift independently HOLDS; signed tag fresh reset mixes arbitrary target tail at1/8 with>1/64 release in biased case;{count} exact checks PASS; occupied-zero witness; FEI OPEN.\nNEXT: A079/A088/A094 review; expose one active seed bit from CURRENT signed child reference, retaining actual target mixture, old tag/reset debit, both full terminals and SAME remaining source account.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} stage18: A079-TAGGED-REFERENCE-SAME-BANK-LIFT@1 independently HOLDS. Derived exact signed post-tag fresh-reference increment -JS-beta*binaryKL+beta*(1-r)*tailKL-change. Actual vacuum calibrated and7/8 old tail plus1/8 arbitrary target paid with>1/64 slack for root beta3/8, seed mean+/-1/2, source vacuum1/2. Naive sqrt(reference vacuum) phase creates occupied zero: true1/256 versus reference0 on actual Boolean child. Final primary{v["checks"]} checks/{v["reset_cases"]} resets/{v["seconds"]:.4f}s plus independent{ind["checks"]} direct/integer-power checks/{ind["seconds"]:.4f}s PASS. Initial syntax error and60s full timeout preserved; explicit same-domain180s replay completed. memok exited1; no Lean launched. No git/mail/brain writes/background jobs, no other work stopped. NEXT actual seed query/current-reference reset with same unused bank.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n\nStage18: For actual F=a+zbh and arbitrary finite-CE supplied R, the correct tag-child vacuum reference is (ahat+/-E[h]*bhat)^2. Matching that whole signed vacuum and carrying a tail mixture M gives exact reset increment -JS_z-beta*d(r||t)+beta*(1-r)[D(p_tail||M)-D(p_tail||R_tail)], r=(E h)^2,t=R0. A target mixture M=(1-eps)R_tail+eps*S costs at most beta*(1-r)log2(1/(1-eps)); do not call arbitrary tail refresh free. For r1/4,t1/2,eps1/8, slack>beta/24 (root>1/64), exact power guard21^18>2^79. Substituting sqrt(R0) for actual signed mean can create an occupied zero despite normalized reference/finite incoming CE: h[-1,1,1,1],R0=1/9 gives true vacuum1/256 and naive0. Both actual children, old reference-only atoms and same original source reserve must persist. This is conditional reference transport/generic KL accounting, NOT a new Booleanity admission inequality or universal source price.\n')
report=(R/'REPORT.md').read_text(encoding='utf-8')
needle='Executed commands, observed counts/timings and PASS receipts are in\nout/validation.json and out/independent.json, summarized in\nout/PERSISTENCE_RECEIPT.json.'
replacement=f'Commands from A032: python -B -X utf8 runs/<this-run>/code/check.py and\npython -B -X utf8 runs/<this-run>/code/independent.py. Final primary PASS:\n{v["controller_seed_pairs"]} controller/seed pairs,{v["reset_cases"]} reset cases,{v["checks"]} exact\nchecks in{v["seconds"]:.4f}s, including{v["strict_root_biased_resets"]} strict biased root resets.\nIndependent PASS:{ind["checks"]} direct/integer-power checks on{ind["fixtures"]} complete\nreset fixtures plus the support witness in{ind["seconds"]:.4f}s. Full outputs are\nout/validation.json and out/independent.json; persistence checks are in\nout/PERSISTENCE_RECEIPT.json.'
assert needle in report;report=report.replace(needle,replacement)
(R/'REPORT.md').write_text(report,encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report
assert report.rfind('# Universal bridge')>0
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert not (R/'out/lean').exists()
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024**2 for p in files)
receipt={'at':now,'all_protocol_fields_verified':True,'statement_hashes_verified':True,'packet_delta_identical':True,'packet_ids':['A032'],'status_two_lines':True,'primary':v,'independent':{k:x for k,x in ind.items() if k!='results'},'total_completed_exact_checks':count,'formal_status':formal['status'],'prior_full_timeout_is_incomplete':True,'local_only':True,'remote_adoption':'UNVERIFIED','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sh(p)} for p in files]}
save(O/'PERSISTENCE_RECEIPT.json',receipt)
print(json.dumps({'saved_files':len(files)+1,'exact_checks':count,'pairs':v['controller_seed_pairs'],'resets':v['reset_cases'],'seconds':v['seconds'],'independent_checks':ind['checks'],'largest_bytes':max(p.stat().st_size for p in files),'status':(OWN/'STATUS.md').read_text(encoding='utf-8')},indent=2))
