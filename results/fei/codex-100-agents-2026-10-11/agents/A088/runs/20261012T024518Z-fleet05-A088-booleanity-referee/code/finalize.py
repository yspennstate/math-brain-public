from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];TEAM=AGENT.parent.parent
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(statement,hyp):return hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
orig=[];claims=[];reviews=[]
sources=[(39,'20261011T223903Z-fleet05-A039-projection-under-restrictions'),(66,'20261011T233317Z-fleet05-A066-semigroup-dissipation'),(67,'20261012T004014Z-fleet05-A067-hypercontractive-refinement')]
for i,run in sources:
    p=TEAM/'agents'/('A%03d'%i)/'runs'/run/'CLAIMS.json'
    for c in json.loads(p.read_text(encoding='utf-8-sig')):
        if not c['claim_id'].startswith('A%03d-'%i):continue
        plain=hashlib.sha256(c['exact_statement'].encode()).hexdigest();combined=canonical(c['exact_statement'],c['hypotheses'])
        assert c['statement_sha256'] in [plain,combined]
        assert set(c)==set(protocol['required_per_run']['claim_fields'])
        orig.append({'path':str(p),'file_sha256':sha(p),'hash_convention':'UTF8 exact statement' if c['statement_sha256']==plain else 'canonical JSON statement+hypotheses','claim':c})
        copied=json.loads(json.dumps(c));scope=c['claim_id']=='A066-POSITIVE-RESTRICTION-HEAT-LEDGER'
        verdict='GAP_SCOPE_CLARIFICATION' if scope else 'HOLDS'
        record={'reviewer':'fleet05/A088','verdict':verdict,'acceptance':'SINGLETON_TREE_COMPONENTS_HOLD; UNQUALIFIED_BLOCK_TREE_BUDGET_REFUTED' if scope else 'ACCEPT_AT_STATED_SCOPE','method':'Independent signed physical-child/entropy/prime-log reconstruction; exact padding-reserve and coherent Bayes reference checks; strongest applicable normalized-real scope diagnostics; no source proof repaired','source':str(ROOT/'AUDIT.md'),'sha256':sha(ROOT/'AUDIT.md'),'reviewer_conflict':False,'shared_registry_adoption':'PENDING_B20'}
        if c['claim_id']=='A066-MAJORITY-DEFECTED-ADDRESS-HEAT-CALIBRATION':
            record['dependency_scope']='Uses only the independently reconstructed finite block row identity of A066-POSITIVE-RESTRICTION-HEAT-LEDGER v1 and direct signed coefficients; the ambiguous stopping-tree budget is not used.'
        copied['review_records'].append(record)
        copied['status']='INDEPENDENT_REVIEW_SCOPE_CLARIFICATION_REQUIRED' if scope else 'INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION'
        if scope:copied['first_unproved_line']='The cumulative channel-plus-level budget must specify singleton-query physical stopping trees; its unrestricted block-tree reading fails on the one-step full-block n128 Boolean point defect. Source DERIVATION equation7 proves singleton scope only.'
        claims.append(copied);reviews.append({'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'verdict':verdict,'scope_detail':record['acceptance'],'reviewer_conflict':False})
assert len(claims)==4
statement='There is no universal all-block physical-stopping-tree bound sum_h w_h(C_Bh^+(f_h)+ell_Bh(f_h)) <= (2+2/e)[I(f)-E I(f_leaf)] for all Boolean signs on finite uniform cubes, where C_B^+ is the natural-log physical-child row channel omitting the empty residual row and ell_B=sum_nonempty_U_subset_B fhat(U)^2 ln(1/fhat(U)^2). A one-step tree querying all128 coordinates of f=1-2 indicator{x=all plus} has constant leaves and rate 4*(127/128)*(1-2^-128)*ln(2)>11/4>2+2/e. This refutes the unrestricted block-tree interpretation of A066 stage2, not its correct singleton-query payment or FEI.'
hyp=['Actual Boolean sign on a finite uniform cube; entropy row costs in natural units','Physical block B may contain more than one coordinate; the certificate queries the entire128-variable cube in one node','Zero log masses contribute zero; total influence is sum_S |S|fhat(S)^2','No claim against the singleton-query restriction theorem']
new={'claim_id':'A088-BLOCK-TREE-HEAT-BUDGET-OBSTRUCTION','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':canonical(statement,hyp),'contributors':['fleet05/A088'],'proof_source':{'path':str(ROOT/'AUDIT.md'),'certificate':str(ROOT/'out/A066_BLOCK_SCOPE_CERTIFICATE.json'),'checker':str(ROOT/'code/check.py')},'proof_dependencies':[],'review_records':[],'status':'EXACT_BOOLEAN_SCOPE_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Unqualified block-query cumulative channel-plus-level payment with coefficient2+2/e'],'first_unproved_line':None,'next_consumers':['A066','A070','A094','A085','B14','B20']}
claims.append(new)
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
(ROOT/'CLAIMS.json').write_text(json.dumps(claims,indent=2),encoding='utf-8')
(ROOT/'out/ORIGINAL_CLAIMS.json').write_text(json.dumps(orig,indent=2),encoding='utf-8')
(ROOT/'out/REVIEW_RECEIPTS.json').write_text(json.dumps(reviews,indent=2),encoding='utf-8')
prior=AGENT/'runs/20261011T223053Z-fleet05-A088-booleanity-referee/CLAIMS.json'
baseline=[c for c in json.loads(prior.read_text(encoding='utf-8')) if c['claim_id'] in ['A066-HEAT-ENTROPY-IDENTITY','A067-LOCAL-BOOLEAN-GRANULARITY','A037-CONDITIONAL-CREDIT-CONSERVATION','A037-PHYSICAL-SPECTRAL-COMMON-LIFT']]
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B18','packet_id':'A088','gap_id':'G-R-MISMATCH','attempt_id':'A088-stage2-restriction-reference-review','method':'Independent Booleanity referee: exact signed restriction/Bayes/prime-log ledger and whole-padding reserve; block-scope countercertificate','mathematical_delta':'Three new scoped HOLDS reviews; A066 stage2 tree-budget scope clarification required; actual n128 Boolean all-block countercertificate; 53482 exact assertions passed; universal net erasure/reset/core-leaf payment and FEI remain open','deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_AUDIT','mathematical_status':'THREE_SCOPED_CLAIMS_REVIEWED_ONE_SCOPE_GAP_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in [x['claim'] for x in orig]+baseline],'claims_created_or_changed':reviews+[{'claim_id':new['claim_id'],'version':1,'change':'New exact Boolean scope obstruction; independent review pending'}],'source_artifacts':['REPORT.md','AUDIT.md','FROZEN_SPEC.json','out/SOURCE_MANIFEST.json','out/ORIGINAL_CLAIMS.json','out/REVIEW_RECEIPTS.json','out/VALIDATION.json','out/A066_BLOCK_SCOPE_CERTIFICATE.json'],'next_consumers':['A039','A064','A066','A067','A070','A094','A085','A097','B14','B20'],'next_action':'Audit a source-complete two-event/shared-core extension combining signed Bayes reset with one retained-core reserve and first-revelation ownership; retain both actual leaf entropies','stagnant_substantive_attempts':0,'blockers':['Universal net nonempty-context erasure and arbitrary core-leaf payment unproved','A066 serialized budget needs explicit singleton-tree scope; block-query interpretation cannot be used','Supervisor adoption and mirror verification unobserved'],'packet_ids':['A088']}
pf=[s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']];assert set(progress)==set(pf)
for name in ['PROGRESS.json','PACKET_DELTA.json']:(ROOT/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
report=(ROOT/'REPORT.md').read_text(encoding='utf-8');assert all('## '+f in report for f in protocol['required_per_run']['report_fields']);assert '## Universal bridge' in report
v=json.loads((ROOT/'out/VALIDATION.json').read_text());assert v['status']=='PASS' and v['assertions']==53482 and v['runtime_seconds']<60
certificate=json.loads((ROOT/'out/A066_BLOCK_SCOPE_CERTIFICATE.json').read_text());from fractions import Fraction
assert Fraction(certificate['gap_lower_exact'])>0
schema={'status':'PASS','claim_records':len(claims),'new_source_reviews':4,'accepted_source_reviews':3,'scope_clarifications':1,'new_boolean_scope_obstructions':1,'claim_fields_exact':True,'progress_fields_exact':True,'source_statement_hashes_valid':True,'progress_copies_identical':(ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes(),'assertions':53482}
(ROOT/'out/SCHEMA_CHECK.json').write_text(json.dumps(schema,indent=2),encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A088 stage2 complete locally: three new scoped claims HOLDS; A066 singleton-tree scope gap certified by n128 Boolean block counterexample; 53,482 exact checks PASS; FEI OPEN.\nNEXT: Audit shared-core/two-event signed reset plus one owned padding/access reserve with both terminal entropies retained; A066 clarify tree scope; A094/A085 review.\n',encoding='utf-8')
entry='2026-10-12 stage2: Independently accepted A039 coherent projection transfer, A066 majority/defected-address calibration and A067 universal padding-strip reserve at scope. A066 positive-heat ledger components hold, but its serialized cumulative budget needs singleton-query scope; n128 point-defect full-block countercertificate disproves unqualified reading. 53482 exact assertions PASS in22.124 seconds; no math checker failure. Saved five claim records (four source reviews plus one new scoped obstruction), exact protocol files and local hash receipts. Full FEI OPEN.'
if entry not in (AGENT/'WORKLOG.md').read_text(encoding='utf-8'):
 with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+entry+'\n')
facts='Singleton level payment uses |fhat(i)|<=I_i from the ternary Boolean derivative. A066 positive heat identity is block-valid, but the (2+2/e) channel-plus-level budget is singleton-tree only: an n128 point defect queried as one full block has rate4(127/128)(1-2^-128)ln2>2+2/e. Empty-context deletion preserves the optimal universal erasure constant via a fresh character times arbitrary tensor cores. A067 whole padding path admits Q_pad<=4I_removed+(1+6/ln2)I_core, with one retained-core reserve; Boolean edge connectivity pays m*d, while arbitrary core leaves remain uncertified. A039 common-kernel Bayes reset is E delta=D_out+JS-Gamma and must stay signed; neither Gamma nor absolute Delta release has universal O(I_i) price. Projection/heat bookkeeping extends to real normalized fields with suitable normalized children and is not by itself a Boolean entropy payment.'
if facts not in (AGENT/'LEARNED.md').read_text(encoding='utf-8'):
 with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+facts+'\n')
receipts=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  raw=p.read_bytes();assert len(raw)<20*1024*1024;receipts.append({'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(ROOT/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps({'local_only':True,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':receipts},indent=2),encoding='utf-8')
print(json.dumps({**schema,'artifact_count':len(receipts),'run':str(ROOT)}))
