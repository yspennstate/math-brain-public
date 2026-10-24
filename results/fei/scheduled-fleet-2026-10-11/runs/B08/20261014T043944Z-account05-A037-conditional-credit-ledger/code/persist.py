from pathlib import Path
import json,hashlib,datetime
BASE=Path(__file__).resolve().parent.parent
HOME=BASE.parent.parent
TEAM=HOME.parent.parent
CANON=Path('~/mop_fei100/reports/fei-2026-10-11')
PROTOCOL=json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def save(name,data):
    (BASE/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=HOME/'runs/20261011T220010Z-account05-A037-conditional-credit-ledger'
review=TEAM/'agents/A039/runs/20261011T223903Z-account05-A039-projection-under-restrictions/DEPENDENCY_REVIEW.md'
lead=TEAM/'claude/B08/runs/20261011T225000Z-claude-B08-tc-restriction-ledger/REPORT.md'
sourceclaims=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8-sig'))
for c in sourceclaims:
    c['review_records']=[{'reviewer':'A039','verdict':'ACCEPT_AT_STATED_SCOPE','source':str(review),'sha256':sha(review),'method':'Source-bound independent analytic reconstruction and separate exact Bayes checker; no repair','registry_adoption':'NOT_VERIFIED'}]
    c['status']='INDEPENDENTLY_REVIEWED_LOCALLY_PENDING_SHARED_ADOPTION'
    if c['claim_id'].endswith('COMMON-LIFT'):
        c['review_records'].append({'reviewer':'Claude B08 lead','verdict':'ACCEPT_AS_BOOKKEEPING_AT_STATED_SCOPE','source':str(lead),'sha256':sha(lead),'locator':'Section 3.5 A037 v1','registry_adoption':'NOT_VERIFIED'})
statement='For the fixed selector core g(x0,x1,y) choosing b=(-1)^(x0*x1) or b flipped at x=0, and F_r=1+1[z=0](g-1) for every integer r>=1, p=2^-r, the control-first marginal bill satisfies D_ctrl/p=(3/8)r(r+1)+(3/4)r log2(4e/3)+epsilon_r with -9/(20 ln2)<=epsilon_r<=0. Its correlation release A_ctrl and product-reference transfer Gamma_ctrl each equal (3/8)p r^2+O(pr), while I(F_r)=p(7+3r)/4 and the retained-terminal erasure bill is O(I). At r=4, exact certified CF/SF split-tree net-erasure-with-terminal gap lies between 26/10000 and 27/10000 bits; both retain leaf entropy 1/16. The five specified CF/SF trees satisfy the terminal-inclusive compensated TC and direct common-kernel reference-reset identities; control nodes carry the dominant remaining erasure. This is a fixed-core application and no universal influence payment is asserted.'
hyp=['Uniform independent physical bits; Boolean signs; entropy/KL in bits','Specified selector/point-flipped two-bit quadratic core; live control paths and explicit terminal stops','Asymptotics as r tends to infinity for this fixed core only; no claim about arbitrary/overlapping cores','Direct Bayes transport uses a common function-specific kernel and fair extension on zero parent spectral fibers']
new={'claim_id':'A037-ACTIVATED-CORE-OWNED-CANCELLATION','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A037'],'proof_source':{'run_id':BASE.name,'files':['REPORT.md','code/tree_ledger.py','out/FROZEN_SPEC.json','out/EXACT_LEDGER.json']},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_CERTIFIED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A039','A064','A097','A023','A038','A088','A094']}
claims=sourceclaims+[new]
for c in claims:assert set(c)==set(PROTOCOL['required_per_run']['claim_fields'])
save('CLAIMS.json',claims)
validation=json.loads((BASE/'out/EXACT_LEDGER.json').read_text())
assert validation['status']=='PASS'
progress={'protocol_revision':PROTOCOL['revision'],'run_id':BASE.name,'stream':'B08','packet_id':'A037','gap_id':'G-R-MISMATCH','attempt_id':'A037-owned-control-transfer-01','method':'Lead-directed exact k=2 activated-core CF/SF physical trees; direct product/Bayes reset; all-rarity fixed-core entropy expansion','mathematical_delta':'Completed five-tree class-account benchmark and terminal reset certificates; derived three quadratic-account cancellation inside one root ledger. Recorded A039 independent acceptance of original A037 v1 without modifying originals. Universal mixed-query child-slack payment remains unproved.','deliverable_status':'COMPLETE_LOCALLY_SAVED_REVIEW_PENDING','mathematical_status':'SCOPED_APPLICATION_PROVED_FULL_FEI_OPEN','claim_versions_used':['A037-CONDITIONAL-CREDIT-CONSERVATION@1','A037-PHYSICAL-SPECTRAL-COMMON-LIFT@1','A039-COHERENT-PROJECTION-TRANSFER@1 (interface independently reconstructed only)'],'claims_created_or_changed':[new['claim_id']+'@1','A037-CONDITIONAL-CREDIT-CONSERVATION@1 review receipt','A037-PHYSICAL-SPECTRAL-COMMON-LIFT@1 review receipt'],'source_artifacts':['REPORT.md','CLAIMS.json','code/tree_ledger.py','out/FROZEN_SPEC.json','out/EXACT_LEDGER.json','out/SOURCES_READ.json'],'next_consumers':new['next_consumers'],'next_action':'Consume A038/A039 mixed shared-control fixture at one actual subsequent physical query; debit the inherited signed reset once while retaining both terminal references; check whether proposed source slack is unused.','stagnant_substantive_attempts':0,'blockers':['Universal erasure/core/terminal payment with unused child slack remains unproved','New applied cancellation claim awaits A088/A094 independent review','Supervisor adoption and mirrors unverified'],'packet_ids':['A037']}
assert set(progress)=={k.split(' (',1)[0] for k in PROTOCOL['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
paths=[CANON/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B08/STREAM_NOTES.md',lead,review,review.parent/'REPORT.md',review.parent/'CLAIMS.json',old/'REPORT.md',old/'CLAIMS.json',TEAM/'agents/A023/runs/20261011T221608Z-account05-A023-amortized-rarity-budget/REPORT.md',CANON/'runs/B05/20261011T193057Z-account01-B05-rare-restrictions/REPORT.md']
save('out/SOURCES_READ.json',{'scope':'Source interfaces and locators stated in REPORT.md; no blanket acceptance of later live occupancy claims','sources':[{'path':str(p),'sha256':sha(p)} for p in paths]})
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(HOME/'STATUS.md').write_text(f'STATE: A037 exact five-tree B05 k=2 ledger and all-rarity owned cancellation saved; {validation["assertions"]:,} exact checks PASS; original v1 independently accepted locally; FEI OPEN.\nNEXT: Consume A038/A039 shared-control mixed-query fixture; debit inherited signed reset once, retain both terminal laws, and verify unused child slack; A088/A094 review new application.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} | Stage {BASE.name}: Latest board read, lead v2 unchanged. Earlier interrupted stage dirs have no completed reports and are not mathematical completions. Consumed A039 source-bound acceptance of both A037 v1 claims. Completed lead k2,r4 CF/SF benchmark with five stopping trees, exact node/class MI/Gamma/JS/B and direct Bayes resets; retained terminals. Proved fixed-core D,A,Gamma leading 3pr^2/8 cancellation. {validation["assertions"]} exact assertions, runtime {validation["runtime_seconds"]:.3f}s; interval gap 0.0026..0.0027 and negative resets certified. New scoped claim review pending; no universal FEI payment.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''
## Fixed-core control ownership (20261014T043944Z)

- A039 independently accepted both original A037 v1 claims without repair; lead accepts the lift as bookkeeping. Shared index adoption is unverified.
- For the k2 selector bent/flip core, beta=1/4, c=3/4, Icore=7/4. F_r influence=2^-r(7+3r)/4. The live control marginal debt is p sum 2^m h2(3/2^(m+2)). D/p=(3/8)r(r+1)+(3/4)r log2(4e/3)+epsilon, -9/(20ln2)<=epsilon<=0.
- D_ctrl, correlation release and Gamma each grow as (3/8)p r^2+O(pr). The retained erasure plus terminal H is only O(pr). Their large magnitudes cancel inside one common TC ledger and must not be spent separately.
- Exact r4 five-tree certificate: CF/SF split trees retain E Hleaf=1/16, with net gap strictly 0.0026..0.0027 bit (SF higher). Weighted control nodes own most unpaid erasure. Reset totals are negative under the frozen fair-zero-fiber extension; signed resets are reference savings, not fresh influence.
- Reproduce with stage code/tree_ledger.py: Fraction probabilities, exact prime-log vectors, 96-term rational log intervals; 9,936 assertions PASS. No large-memory job. Next target is actual shared-control mixed-query ownership with both terminal references, not another disjoint rarity bound.
''')
files=[p for p in BASE.rglob('*') if p.is_file() and p.name!='ARTIFACT_SHA256.json']
for p in files:assert p.stat().st_size<20_000_000
save('out/ARTIFACT_SHA256.json',{'saved_at':stamp,'schema_check':'Exact protocol claim/progress keys; packet_ids explanatory parenthesis normalized','assertions':validation['assertions'],'runtime_seconds':validation['runtime_seconds'],'artifacts':[{'path':str(p.relative_to(BASE)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]})
assert json.loads((BASE/'PROGRESS.json').read_text())==json.loads((BASE/'PACKET_DELTA.json').read_text())
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','run':str(BASE),'new_claims':1,'source_bound_review_updates':2,'assertions':validation['assertions'],'runtime_seconds':validation['runtime_seconds'],'artifacts':len(files)},indent=2))
