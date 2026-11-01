from pathlib import Path
import hashlib, json, datetime

ROOT=Path(__file__).resolve().parents[3]
RUN=Path(__file__).resolve().parents[1]
SHARED=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CONTEXT=Path(r'~\brain_workers\FEI100_20261011\context')
files=[SHARED/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
files += [SUP/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += sorted((SUP/'sources').glob('*.md'))+sorted(CONTEXT.glob('*.txt'))
files += sorted((SHARED/'runs').rglob('REPORT.md'))
TEAM=ROOT.parents[1]
files += [TEAM/'BOARD.md']
for agent,runid in [('A022','20261011T215800Z-fleet05-A022-one-point-surgery'),('A051','20261011T214321Z-fleet05-A051-near-extremizer-definition')]:
    p=TEAM/'agents'/agent/'runs'/runid
    files += [p/'REPORT.md',p/'CLAIMS.json']
    if agent=='A051': files.append(p/'EXISTENCE_AND_LIMITS.md')
rows=[]
for p in files:
    b=p.read_bytes()
    try: s=b.decode('utf-8-sig')
    except UnicodeDecodeError: s=b.decode('cp1252')
    rows.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(s.splitlines()),'read_scope':'Full file loaded and hashed; relevant locators inspected in assistant context, not every unrelated line analyzed'})
(RUN/'out'/'SOURCE_MANIFEST.json').write_text(json.dumps({'files':rows,'missing_coordination_source':str(TEAM/'claude'/'B11'/'STREAM_NOTES.md'),'no_remote_readback':True},indent=2)+'\n',encoding='utf-8')
statement='For every Boolean sign f on the n-dimensional uniform cube, its one-point surgery g=f-2*f(a)*1_a has the exact signed spectrum, influence, second-derivative and plaquette identities in HIDDEN_TENSOR_DIAGNOSTIC.md sections 1-2, with uniform entropy error E_n=h2(2^(1-floor(n/2)))+n*2^(1-floor(n/2)) for n>=4. Every one-point surgery of a nontrivial coordinate tensor product in n>=2 is tensor-prime and full-Fourier-support. For every fixed nonconstant d-bit Boolean sign h, surgeries G_t of the balanced powers z*h^(tensor t) have H(G_t)/I(G_t)->H(h)/I(h), connected plaquette graphs and cut-plaquette sum 4td*2^(-td-1)->0; thus the simultaneous qualitative class has the same optimal FEI constant as all Boolean signs. These embeddings do not preserve dimension-criticality for a threshold violated by h, since for t>=2 a proper physical restriction away from surgery exposes +/-h.'
hyp=['Uniform cube; entropy and logarithms in bits','One-point surgery at an arbitrary vertex; n>=2 for full support and primitivity, n>=4 for stated entropy envelope','Tensor primitivity means no factorization over any nontrivial partition of physical coordinates','h fixed and nonconstant; t arbitrary positive integer, with limit t->infinity','No assertion of an actual core with unbounded H/I; no all-descendant criticality admission']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A053-NEAR-TENSOR-CURVATURE-ADMISSION','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A053/fleet05'],'proof_source':'HIDDEN_TENSOR_DIAGNOSTIC.md sections 1-7; NEAR_TENSOR_PERTURBATIONS.tex; code/check_near_tensor.py; out/EXACT_CHECK.json','proof_dependencies':[],'review_records':[],'status':'SOURCE_COMPLETE_ANALYTIC_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Unversioned shortcut: qualitative tensor primitivity or connected multiplicative-curvature graph excludes arbitrary hard tensor cores','Unversioned shortcut: positive raw additive mixed-derivative energy detects tensor nonfactorization'],'first_unproved_line':None,'next_consumers':['A022','A051','A052','A054','A055','A090','A094','B20']}
(RUN/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
original=TEAM/'agents'/'A051'/'runs'/'20261011T214321Z-fleet05-A051-near-extremizer-definition'
original_hash=hashlib.sha256((original/'EXISTENCE_AND_LIMITS.md').read_bytes()).hexdigest()
assert original_hash=='123fcf33fb47d6823a28afd1a9f282e6f1d0f3bc38a929987510933c0bf020c8'
review=[]
for c in json.loads((original/'CLAIMS.json').read_text(encoding='utf-8-sig')):
    review.append({'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'proof_sha256':original_hash,'reviewer':'A053/fleet05','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent analytic reconstruction; original executable not rerun','contributor_conflict':False,'source':'REVIEW_A051.md','registry_adoption':'PENDING_SUPERVISOR'})
(RUN/'out'/'REVIEW_A051.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B11','packet_id':'A053','gap_id':'G-A053-CRITICAL-QUANTITATIVE-SEPARATION','attempt_id':'A053-near-tensor-1','method':'Exact Boolean point surgery, factorization parity and plaquette criterion, signed Walsh second moments, maximal-coupling entropy continuity, balanced tensor limit','mathematical_delta':'Exact cross-cut curvature 4*2^-n, additive second-moment and covariance formulas, uniform entropy/influence errors; arbitrary-core simultaneous qualitative prime/full-support/connected admission; explicit failed criticality restriction','deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING','mathematical_status':'PACKET_SCOPE_PROVED_LOCALLY_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':['A053-NEAR-TENSOR-CURVATURE-ADMISSION@1'],'source_artifacts':['REPORT.md','HIDDEN_TENSOR_DIAGNOSTIC.md','NEAR_TENSOR_PERTURBATIONS.tex','out/FROZEN_SPEC.json','out/FROZEN_SPEC_V2.json','out/EXACT_CHECK.json','out/SOURCE_MANIFEST.json','code/check_near_tensor.py'],'next_consumers':['A022','A051','A052','A054','A055','A090','A094','B20'],'next_action':'Apply all-proper-descendant deficit tests to a candidate quantitative separation from near-products; identify a paid proper-block erasure or an explicit critical counterexample, reviewed by A090/A094','stagnant_substantive_attempts':0,'blockers':['B11 STREAM_NOTES.md absent; no mathematical access blocker','Independent review and supervisor adoption/mirror pending'],'packet_ids':['A053']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:
    (RUN/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
protocol=json.loads((SHARED/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all(x in report for x in protocol['required_per_run']['report_fields'])
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        b=p.read_bytes(); assert len(b)<20_000_000
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=ROOT/name; b=p.read_bytes()
    receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(RUN/'out'/'PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_field_sets_checked':True,'files':receipts,'remote_mirror':'NOT_VERIFIED','independent_review_of_A053':'PENDING'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','source_files_hashed':len(rows),'persisted_files':len(receipts),'protocol_fields':'EXACT_MATCH','claim_sha256':digest},indent=2))
