from pathlib import Path
import hashlib,json,datetime

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
TEAM=AGENT.parents[1]
OLD=AGENT/'runs/20261011T231526Z-fleet05-A095-restricted-result-extraction'
AUDIT=TEAM/'agents/A094/runs/20261012T044109Z-fleet05-A094-proof-chain-challenger'
LEAD=TEAM/'claude/B19'
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf8')
protocol=json.loads(PROTOCOL.read_text(encoding='utf8'))
old_claims=json.loads((OLD/'CLAIMS.json').read_text(encoding='utf8'))
previous=next(c for c in old_claims if c['claim_id']=='A095-RANK-KL-EQUIVALENCE')
updated=dict(previous)
updated['version']=2
updated['exact_statement']=previous['exact_statement']+' Concrete paid application: for any Boolean g with known bias mu and supplied normalized core reference R positive on its spectrum, empty calibration to R0(empty)=mu^2 is CE-nonincreasing. For r>=1,p=2^-r,F=1+A_r(g-1), the full reference Q(vac)=[1-p(1-mu)]^2, Q(U!=empty,T=empty)=p^2(1-mu)^2, Q(U,T!=empty)=p^2 R0(T) is normalized and has CE_F-H(F)=p D(P_g||R0) and CE_F<=p CE_g_cal+6rp(1-mu). For g=q product_j(1-2 A_(L_j)) on disjoint private blocks and a supplied terminal reference, its fixed occupied-block/uniform-nonempty-subset reference gives CE_F<=p CE_q_cal+4p sum_j I(h_j)+6rp(1-mu_g), with I(F)=p[I(q)+sum_j I(h_j)+r(1-mu_g)]. Thus a terminal cost <=C I(q) yields full cost <=max(C,6)I(F); q=1 yields CE<=6I uniformly in r, widths and number of blocks. For r=0,q=1 the same block reference has CE=H<4I. No universal terminal reference bound or incompatible shared-control extension is claimed.'
updated['hypotheses']=previous['hypotheses']+['References normalized and positive on actual support','Shared controls form one common signed conjunction; all remaining private blocks and terminal cube are disjoint','Bias is fixed known instance data; references chosen before spectral sampling','Ideal negative-log probability costs; no optional binary prefix-rounding bit included']
updated['statement_sha256']=hashlib.sha256(updated['exact_statement'].encode()).hexdigest()
updated['proof_source']={'old_exact_equivalence':str(OLD/'REPORT.md'),'new_paid_application':str(ROOT/'DERIVATION.md'),'validation':str(ROOT/'out/EXACT_RESULTS.json')}
updated['proof_dependencies']=[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':1,'status':'previous author-proved equivalence retained unchanged; not independently accepted'},'Elementary Fourier activation expansion and KL disintegration','Direct scalar JS proof in DERIVATION.md','Cube edge-isoperimetric variance-entropy bound for point defects']
updated['review_records']=[]
updated['supersedes']=[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':1,'scope':'same C020 candidate, old equivalence retained and concrete reference application added'}]
updated['next_consumers']=['A094','A086','A008','A012','B19','B20']

source_claims=json.loads((AUDIT/'CLAIMS.json').read_text(encoding='utf8'))
original=next(c for c in source_claims if c['claim_id']=='A094-CONCRETE-ACTIVATED-DICTIONARY-DEBT-AND-RANK-BOUNDARY')
review=dict(original)
review['review_records']=original['review_records']+[{'reviewer':'A095','verdict':'HOLDS_AT_FULL_STATED_SCOPE','source':str(ROOT/'REVIEW_A094.md'),'method':'Independent all-parameter analytic reconstruction, actual Fourier/edge and rational prime-log implementation, and exact diagonal certificates','substantive_repair_supplied':False,'source_claims_sha256':sha(AUDIT/'CLAIMS.json'),'stage':'20261013T213857Z'}]
review['status']='ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED_LOCALLY'
assert hashlib.sha256(review['exact_statement'].encode()).hexdigest()==review['statement_sha256']
claims=[updated,review]
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',claims)

leadpath=LEAD/'runs/20261011T224700Z-claude-B19-paper-audit-rankcode/CLAIMS.json'
leadclaims=json.loads(leadpath.read_text(encoding='utf8'))
corrections=[]
for c in leadclaims:
    if c['claim_id'] not in ('B19-RANKCODE-REDUCTION','B19-RANKCODE-GLOBAL-ORDER-NOGO'):continue
    canonical=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    plain=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    assert canonical==c['statement_sha256']
    corrections.append({'claim_id':c['claim_id'],'version':1,'source_declared_sha256':c['statement_sha256'],'canonical_statement_hypotheses_sha256':canonical,'plain_statement_sha256':plain,'verdict':'ORIGINAL_SOURCE_HASH_VALID','retracts':'A095 stage-1 SOURCE_STATEMENT_HASH_METADATA_MISMATCH diagnosis and recommendation of source reconciliation','scope':'Diagnostic/metadata correction only; theorem text, mathematical acceptance and original source unchanged'})
save('out/HASH_DIAGNOSIS_CORRECTION.json',{'stage1_claims_path':str(OLD/'CLAIMS.json'),'stage1_claims_sha256':sha(OLD/'CLAIMS.json'),'lead_claims_path':str(leadpath),'lead_claims_sha256':sha(leadpath),'canonical_serialization':'json.dumps({statement: exact_statement, hypotheses: hypotheses}, sort_keys=True, separators=(comma,colon))','corrections':corrections,'historical_run_rewritten':False})

sources=[PROTOCOL,TEAM/'BOARD.md',LEAD/'STREAM_NOTES.md',OLD/'REPORT.md',OLD/'CLAIMS.json',AUDIT/'REPORT.md',AUDIT/'AUDIT.md',AUDIT/'CLAIMS.json',AUDIT/'out/HASH_CONVENTIONS.json',AUDIT/'code/finalize.py',TEAM/'agents/A086/runs/20261011T234041Z-fleet05-A086-joint-code-referee/ACTIVATION_DEBT_PROJECTION.md',TEAM/'agents/A008/runs/20261012T005959Z-fleet05-A008-gate-label-compression/READ_ONCE_DNF.tex']
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources])
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B19','packet_id':'A095',
 'gap_id':'G-A095-RANK-MINUS-KL-C020','attempt_id':'A095-stage2-common-spine',
 'method':'Consume independent A094 audit, refine existing C020 reference candidate by biased-core calibration and common-spine transfer, frozen exact Fourier/Fraction/log-prime certificates',
 'mathematical_delta':'Explicit block cost <4I for disjoint XOR-of-defect signs; full common-spine reference cost <=6I; exact biased-core debt scales by p with terminal cost retained. A094 complete reference boundary independently accepted. Earlier hash diagnosis corrected.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT',
 'mathematical_status':'EXISTING_REFERENCE_CANDIDATE_REFINED_AT_RESTRICTED_SCOPE_PENDING_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':['A095-RANK-KL-EQUIVALENCE@1 (unchanged retained equivalence)','A094-CONCRETE-ACTIVATED-DICTIONARY-DEBT-AND-RANK-BOUNDARY@1 (independently reconstructed this stage)','A086 balanced projection reviewed scope; actual biased transfer proved directly'],
 'claims_created_or_changed':['A095-RANK-KL-EQUIVALENCE@2','A094-CONCRETE-ACTIVATED-DICTIONARY-DEBT-AND-RANK-BOUNDARY@1 (review only)'],
 'source_artifacts':['REPORT.md','DERIVATION.md','REVIEW_A094.md','CLAIMS.json','code/check.py','out/FROZEN_SPEC.json','out/EXACT_RESULTS.json','out/HASH_DIAGNOSIS_CORRECTION.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':['A094','A086','A008','A012','B19','B20'],
 'next_action':'Construct one normalized reference for two block activations with opposite shared literals, retaining weighted terminal CE and one physical influence budget.',
 'stagnant_substantive_attempts':0,
 'blockers':['New paid reference application awaits independent review; original pivotal-height candidate remains pending. Incompatible overlap and arbitrary terminal reference payment open. Supervisor adoption and mirrors unobserved.'],
 'packet_ids':['A095']}
assert set(progress)=={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
for name in ('PROGRESS.json','PACKET_DELTA.json'):save(name,progress)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
test_results=json.loads((ROOT/'out/EXACT_RESULTS.json').read_text(encoding='utf8'))
assert test_results['status']=='PASS' and test_results['runtime_seconds']<60
assert len((AGENT/'STATUS.md').read_text(encoding='utf8').splitlines())==2
receipts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ('STATUS.md','WORKLOG.md','LEARNED.md'):
    p=AGENT/name;receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save('out/PERSISTENCE_RECEIPTS.json',{'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema':'PASS','local_only':True,'new_broad_candidate_count':0,'existing_candidate_refined':'A095-RANK-KL-EQUIVALENCE@2','receipts':receipts})
print(json.dumps({'schema':'PASS','assertions':test_results['exact_assertions'],'claims':len(claims),'receipts':len(receipts),'hash_corrections_verified':len(corrections),'run':str(ROOT)}))
