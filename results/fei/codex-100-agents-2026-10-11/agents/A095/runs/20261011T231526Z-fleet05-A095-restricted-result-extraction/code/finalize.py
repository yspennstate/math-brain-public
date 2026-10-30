from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
CAMPAIGN=Path('~/mop_fei100/reports/fei-2026-10-11')
PUSH=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
CONTEXT=Path('~/brain_workers/FEI100_20261011/context')
LEAD=Path('~/brain_workers/FEI100_20261011/claude/B19')
protocol=json.loads((CAMPAIGN/'EXECUTION_PROTOCOL.json').read_text(encoding='utf8'))
source_paths=[CAMPAIGN/name for name in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
source_paths += [PUSH/name for name in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
source_paths += sorted((PUSH/'sources').glob('*.md'))
source_paths += sorted(CONTEXT.glob('*.txt'))
source_paths += [AGENT.parents[1]/'BOARD.md',LEAD/'STREAM_NOTES.md',LEAD/'PAPER_AUDIT_38pp.md',LEAD/'runs/20261011T224700Z-claude-B19-paper-audit-rankcode/CLAIMS.json']
source_paths += sorted((CAMPAIGN/'runs').rglob('REPORT.md'))
sources=[]
for path in source_paths:
    if path.exists():
        data=path.read_bytes()
        sources.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'scope':'Source bytes loaded; mathematical locators actually used are identified in REPORT.md'})
    else:sources.append({'path':str(path),'status':'MISSING'})
(ROOT/'out/SOURCE_RECEIPTS.json').write_text(json.dumps({'saved_at_utc':datetime.now(timezone.utc).isoformat(),'sources':sources,'earlier_report_count':len(list((CAMPAIGN/'runs').rglob('REPORT.md')))},indent=2)+'\n',encoding='utf8')

def claim(cid,statement,hypotheses,deps,refutes=()):
    return {'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A095'],'proof_source':{'path':str(ROOT/'REPORT.md')},'proof_dependencies':deps,'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':list(refutes),'first_unproved_line':None,'next_consumers':['A090','A085','B02','B03','B14','B20']}

claims=[claim('A095-ORDERED-PIVOTAL-HEIGHT',
    'For every uniform-cube Boolean f and coordinate order sigma, if each predecessor fiber of supp(d_i f) admits an orientation with increasing-chain height at most integer r_i>=1 (orientations may depend on the fixed future), then H(f)<=[log2(4+e)+log2(pi^2/4)]I(f)+(2/ln2)sum_i Inf_i(f) min{r_i(1+ln2),2+gamma+2ln r_i}. Fixed uniform-r classes are closed under physical restrictions with induced orders; sum_i Inf_i ln r_i<=K I implies a dimension-independent constant [log2(4+e)+log2(pi^2/4)]+(2/ln2)(2+gamma+2K).',
    ['Boolean sign function','uniform measure','entropy in bits','rank and gamma use natural logarithms','each r_i is a positive integer','no global consistency of fiber orientations required'],
    ['cube edge-isoperimetry','Sperner theorem','Euler hyperbolic-sine product','Gibbs inequality','REPORT.md sections 1-2']),
    claim('A095-RANK-KL-EQUIVALENCE',
    'For every Boolean f and every order sigma, normalize Q_(sigma,k)(S)=prod_{i in positions_sigma(S)}i^(-2)/Z_(n,k), set beta_(n,k)=ln(Z_(n,k)(k!)^2), D_sigma=sum_k P(|S|=k)D_nat(P(S||S|=k)||Q_(sigma,k)), and T_sigma=2R_sigma-D_sigma. Then (ln2)H(f)=H_nat(|S|)+T_sigma+E beta, with 0<=beta_(n,k)<=k ln(pi^2/4). If K_T=sup_nonconstant_f min_sigma T_sigma/I(f) and C_FEI=sup H/I, then K_T/ln2<=C_FEI<=log2(4+e)+log2(pi^2/4)+K_T/ln2 in the extended real sense. Thus K_T finite iff uniform-cube FEI holds.',
    ['Boolean sign function','uniform measure','H in bits, D and beta in nats','zero-mass levels omitted','k=0 reference assigns mass one to empty set'],
    ['REPORT.md sections 1 and 4','cube edge-isoperimetry','Euler hyperbolic-sine product','entropy and KL chain identities'])]

lead_claims=json.loads((LEAD/'runs/20261011T224700Z-claude-B19-paper-audit-rankcode/CLAIMS.json').read_text(encoding='utf8'))
for original in lead_claims:
    if original['claim_id'] not in ('B19-RANKCODE-REDUCTION','B19-RANKCODE-GLOBAL-ORDER-NOGO'):continue
    review=dict(original)
    review['review_records']=original['review_records']+[{'reviewer':'A095','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent all-parameter reconstruction; signed integer Walsh/Fraction regression','proof_source':str(ROOT/'REPORT.md'),'sections':'1 and 3','validation_assertions':27177}]
    review['status']='ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED_LOCALLY'
    # A metadata correction never changes the theorem statement or source.
    actual_hash=hashlib.sha256(review['exact_statement'].encode()).hexdigest()
    if actual_hash!=review['statement_sha256']:
        review['review_records'].append({'reviewer':'A095','verdict':'SOURCE_STATEMENT_HASH_METADATA_MISMATCH','declared_sha256':review['statement_sha256'],'recomputed_utf8_sha256':actual_hash,'statement_changed':False,'action':'Local statement hash corrected; original source untouched.'})
        review['statement_sha256']=actual_hash
    claims.append(review)

for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
(ROOT/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf8')
progress={
    'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B19','packet_id':'A095','gap_id':'G-A095-RANK-MINUS-KL-C020','attempt_id':'A095-stage1','method':'Analytic restricted-result extraction, independent rank-code reconstruction, frozen integer-Walsh/Fraction/rational-log validation',
    'mathematical_delta':'Closed hereditary bounded pivotal-height criterion with fiber-dependent orientations; extracted exact normalized Euler rank-minus-KL equivalence; independently reconstructed B19 universal reduction and all-order XOR-of-AND obstruction. Universal FEI payment remains open.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'RESTRICTED_THEOREM_AND_EQUIVALENCE_AUTHOR_PROVED_REVIEW_PENDING; FULL_FEI_OPEN',
    'claim_versions_used':['B19-RANKCODE-REDUCTION@1 (independently reconstructed)','B19-RANKCODE-GLOBAL-ORDER-NOGO@1 (independently reconstructed)'],
    'claims_created_or_changed':[c['claim_id']+'@1' for c in claims],
    'source_artifacts':['REPORT.md','CLAIMS.json','out/FROZEN_SPEC.json','out/VALIDATION.json','out/SOURCE_RECEIPTS.json','code/validate.py'],
    'next_consumers':['A090','A085','B02','B03','B14','B20'],
    'next_action':'Independently review the two new claims; derive a normalized rank-local reference for two blocks sharing one physical coordinate, retaining complete selection, KL and terminal-core costs.',
    'stagnant_substantive_attempts':0,
    'blockers':['New statements await independent review; supervisor mirror/adoption unobserved. Lead REPORT.md absent but audit/CLAIMS contained proofs; no mathematical source gap. Universal rank-minus-KL payment unproved.'],
    'packet_ids':['A095']}
# The protocol annotates packet_ids in its field list; compatibility section
# explicitly specifies packet_ids as the JSON key, without that annotation.
assert set(progress)=={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
serialized=json.dumps(progress,indent=2)+'\n'
for name in ('PROGRESS.json','PACKET_DELTA.json'):(ROOT/name).write_text(serialized,encoding='utf8')
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
receipts=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE_RECEIPTS.json':
        data=path.read_bytes();assert len(data)<20*1024*1024
        receipts.append({'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
for name in ('STATUS.md','WORKLOG.md','LEARNED.md'):
    path=AGENT/name;data=path.read_bytes()
    receipts.append({'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(ROOT/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'saved_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Local only; mirror and supervisor adoption not observed','schema_checks':'PASS','receipts':receipts},indent=2)+'\n',encoding='utf8')
print(json.dumps({'schema':'PASS','claims':len(claims),'new_unreviewed_candidates':2,'receipts':len(receipts),'source_receipts':len(sources),'run':str(ROOT)}))
