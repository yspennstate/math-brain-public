from pathlib import Path
import json, hashlib
from datetime import datetime, timezone

root=Path(__file__).resolve().parent.parent
agent=root.parent.parent
reportroot=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
def sha(b): return hashlib.sha256(b).hexdigest()
def write(name,obj): (root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
files=[reportroot/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += [supp/'sources'/n for n in ['ERASURE_REDUCTION.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ADDENDUM_11_26_CRITICAL_RARE_MOMENT.md','ADDENDUM_11_44_COMPONENT_ENTROPY_COUNTEREXAMPLE.md','ROUTE_MAP_CURATED.md']]
files += list(context.glob('*.txt'))
files += list((reportroot/'runs').rglob('REPORT.md'))
files += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
records=[]
for p in files:
    b=p.read_bytes()
    records.append({'path':str(p),'sha256':sha(b),'bytes':len(b),'reading_scope':'Full protocol; shared-state navigation and relevant proof/scope sections, as listed in REPORT.md' if p.name!='EXECUTION_PROTOCOL.json' else 'Full protocol'})
write('out/SOURCE_MANIFEST.json',{'generated_at':datetime.now(timezone.utc).isoformat(),'local_byte_pins':records,'missing_at_start':[r'~\brain_workers\FEI100_20261011\claude\B11\STREAM_NOTES.md'],'remote_verification':False})
main='EXISTENCE_AND_LIMITS.md'
statement1=('For actual Boolean signs on finite uniform cubes with entropy in bits, let C_* be the extended supremum of H/I over nonconstants. Fixed-dimensional maxima M_n exist, increase to C_*, and satisfy M_n<=n*2^(n-1). For every finite 0<=C<C_*, there exists a witness H>CI of least essential physical dimension; such witnesses approximate C_* along thresholds approaching C_* (or increasing to infinity). Disjoint tensor products add H,I,D_C and violating products have a violating factor. Balancing k tensor copies gives deficit kD_C-C. Balanced singleton activation has H=pH(g)+2rp(2-p)+h((1-p)^2), I=p(I(g)+r). For every nonconstant f, the activated balanced sequence k=m^2,r=m has R tending to R(f) with I and minority probability tending to zero. These operations preserve threshold admission after sufficient amplification but do not generally preserve dimension-criticality; arbitrary restriction need not preserve H/I. No global optimizer attainment is asserted.')
statement2=('Fix finite C>=0 and an actual Boolean dimension-critical C-witness f, meaning H(f)>CI(f) and its essential physical dimension is minimal among all such witnesses. Every proper physical restriction has deficit D_C<=0, and f has no proper nonconstant disjoint tensor factorization. For every nonempty block A of its essential coordinates, L_A-CI_A>=D_C(f)>0, with L_A=H(f)-E H(f_a)=H(Z_A|Z_Ac)+I(a;T), where a is uniform and T is sampled from the actual child Fourier spectrum. Every finite adaptive physical restriction tree satisfies D_C(f)=sum_internal pi_v(L_v-Cd_v)+sum_leaves pi_lD_C(f_l); with proper leaves the internal sum is at least D_C(f). No component-pruning, connectedness, or inherited descendant-criticality conclusion is asserted.')
claims=[]
ids=['A051-THRESHOLD-CRITICAL-EXISTENCE','A051-CRITICAL-BLOCK-DEFICIT']
for cid,statement,loc in zip(ids,[statement1,statement2],['sections 1--2','section 3']):
    claims.append({'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['Actual Boolean signs on finite uniform cubes','Entropy in bits; constants never divided by influence','Fixed finite C>=0; existence of a violation where criticality is invoked'],'statement_sha256':sha(statement.encode()),'contributors':['account05/A051'],'proof_source':{'path':str(root/main),'sha256':sha((root/main).read_bytes()),'locator':loc},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A052','A053','A055','A090','A094','B20']})
write('CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B11','packet_id':'A051','gap_id':'FEI-B11-A051-INITIAL','attempt_id':'A051-INITIAL-1','method':'Fixed-threshold well ordering; exact tensor/activation ledger; physical block Parseval and adaptive deficit telescoping','mathematical_delta':'Proved minimal-dimension witness existence at each fixed violated constant and finite near-supremum approximation without optimizer attainment; established all-block necessary deficit constraints and separated threshold-safe embeddings from criticality-preserving reductions. Exact finite identity checker passed 22298 assertions.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING','mathematical_status':'PACKET_PROVED_ON_PAGE_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':cid,'version':1} for cid in ids],'source_artifacts':['REPORT.md','EXTREMALITY_DEFINITION.tex',main,'CLAIMS.json','out/FROZEN_SPEC.json','code/check_identities.py','out/CHECK_OUTPUT.json','out/SOURCE_MANIFEST.json','out/RECEIPTS.json'],'next_consumers':['A052','A053','A055','A090','A094','B20'],'next_action':'A090/A094 independently reconstruct claims; A052 derive quantitative structure from all-block M_A+J_A>=CI_A+D_C(f), preserving component-obstruction scope.','stagnant_substantive_attempts':0,'blockers':['Independent review and supervisor mirror verification pending; Claude B11 notes absent at start (nonblocking).'],'packet_ids':['A051']}
write('PROGRESS.json',progress); write('PACKET_DELTA.json',progress)
(agent/'STATUS.md').write_text('STATE: A051 packet proved on page and saved locally: critical-witness existence, reduction ledger, all-block deficit constraints; 22,298 exact checks passed; review pending; full FEI OPEN.\nNEXT: A090/A094 review; A052 use actual all-block criticality inequalities for quantitative structure; A053/A055 keep threshold admission distinct from dimension-criticality.\n',encoding='utf-8')
receipt=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        b=p.read_bytes(); receipt.append({'path':str(p.relative_to(root)),'sha256':sha(b),'bytes':len(b)})
for n in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=agent/n; b=p.read_bytes(); receipt.append({'path':str(p),'sha256':sha(b),'bytes':len(b)})
write('out/RECEIPTS.json',{'saved_at':datetime.now(timezone.utc).isoformat(),'local_persistence_only':True,'remote_mirror_verified':False,'independent_acceptance':False,'files':receipt})
protocol=json.loads((reportroot/'EXECUTION_PROTOCOL.json').read_text())
req=protocol['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in req['progress_fields']}
assert all(set(c)==set(req['claim_fields']) for c in claims)
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
assert all(x['bytes']<20_000_000 for x in receipt)
assert all((root/'REPORT.md').read_text().find('## '+x)>=0 for x in req['report_fields'])
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','claims':len(claims),'receipt_files':len(receipt),'progress_fields':len(progress),'claim_fields':len(claims[0]),'root':str(root)},indent=2))
