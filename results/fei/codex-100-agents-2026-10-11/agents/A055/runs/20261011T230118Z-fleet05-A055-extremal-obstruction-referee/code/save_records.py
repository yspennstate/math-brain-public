from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
RUN_ID=ROOT.name
TEAM=Path(r'~\brain_workers\FEI100_20261011')
CANON=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')

def write(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

protocol=json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
new_statement=('For every Boolean core g and finite C>=0, disjoint tensor and r-control activation embeddings have exact failed averaged criticality tests L_Y-C I_Y-D_C(F)=-D_C(g) and -2^-r D_C(g), respectively. The two-tag wrapper K(x,0)=-1,K(x,1)=g(x),T(x,w,0)=K(x,w),T(x,w,1)=+1 has one connected negative selector cylinder, density (3-Eg)/8 in [1/4,1/2], I(T)=I(g)/4+1 and H(T)=H(g)/4+E(g) with 0<=E(g)<=9/2; tensor cores give every unrestricted limiting FEI ratio. Its two-tag block satisfies L_tags-C I_tags-D_C(T)=-D_C(g)/4, so these noncritical geometric/density admissions do not preserve threshold criticality for a violating core. Every one-point surgery J on a balanced sign product (-1)^z G(x) in N>=5 bits satisfies E_z D_C(J_z)>D_C(J)+13/32 for C>=1; therefore any such violating surgery has a violating fresh-sign child. These are exact admission obstructions, not a universal proper-block selection theorem or a disproof of FEI.')
new={
 'claim_id':'A055-CRITICAL-EMBEDDING-SHORTFALLS','version':1,
 'exact_statement':new_statement,
 'hypotheses':['Uniform physical cube; Boolean signs; entropy in bits; constants have zero deficit','D_C(f)=H(f)-C I(f); threshold criticality requires every proper physical descendant to have nonpositive deficit','Positive-dimensional core for a proper tag-block restriction; fixed nonconstant core for tensor-ratio limits','N>=5 and C>=1 only for the stated uniform fresh-sign surgery margin'],
 'statement_sha256':hashlib.sha256(new_statement.encode('utf-8')).hexdigest(),
 'contributors':['A055/fleet05'],
 'proof_source':'EMBEDDING_PROOF.md sections 1--5; CRITICAL_CLASS_EMBEDDINGS.tex; exact checker outputs',
 'proof_dependencies':[], 'review_records':[],
 'status':'SOURCE_COMPLETE_ANALYTIC_PROOF_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],
 'refutes':['Unversioned admission shortcut: tensor/activation/point-surgery preservation of a strict core threshold preserves every dimension-criticality test','Unversioned shortcut: connected thin-selector-cylinder geometry plus density in [1/4,1/2] excludes unrestricted hard cores without genuine all-descendant criticality'],
 'first_unproved_line':None,
 'next_consumers':['A005','A051','A052','A053','A054','A090','A094','B20']}
source_claim=next((TEAM/'agents/A053/runs').rglob('CLAIMS.json'))
reviewed=json.loads(source_claim.read_text(encoding='utf-8'))[0]
reviewed={k:reviewed[k] for k in protocol['required_per_run']['claim_fields']}
reviewed['review_records']=reviewed['review_records']+[{
 'reviewer':'A055/fleet05','verdict':'ACCEPT_AT_STATED_SCOPE',
 'source':str(ROOT/'REVIEW_A053.md'),
 'method':'Independent full analytic reconstruction; direct integer character sums, physical edges and plaquettes, and all cut rank-one minors on 40 fixed balanced surgery fixtures; no import of author code',
 'contributor_repair':False,'registry_adoption':'PENDING_SUPERVISOR'}]
reviewed['status']='INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE_PENDING_REGISTRY_ADOPTION'
write('CLAIMS.json',[reviewed,new])

verdicts=[
 {'class':'A051 dimension-minimal threshold witnesses','embedding':'g*h','preserved':['Actual Booleanity','Exact tensor spectrum and entropy/influence additivity'], 'violated':[{'condition':'Every proper physical descendant has D_C<=0','block':'spectator Y','exact_left_side':'L_Y-C I_Y-D_C(F)=-D_C(g)<0 for a violating core'}], 'unresolved':['Any other arbitrary-core encoding preserving all individual criticality tests']},
 {'class':'A051 dimension-minimal threshold witnesses','embedding':'1+A_r(g-1)','preserved':['Booleanity','Rare support and small influence after standard amplification','Exact arbitrary-bias activation spectrum'], 'violated':[{'condition':'All proper child deficits nonpositive','block':'all r controls','exact_left_side':'-2^-r D_C(g)'},{'condition':'Optional singleton control test','block':'one control','exact_left_side':'-D_C(F_(r-1))/2; fails iff residual activation deficit is positive'}], 'unresolved':['Universally affordable proper-block selection']},
 {'class':'A052 translation/syndrome necessary tests and A053 qualitative admissions','embedding':'one-point surgery on (-1)^z G(x)','preserved':['Tensor primitivity','Full Fourier support','Every coordinate essential','Connected multiplicative-curvature graph','Balanced-tensor limiting ratio'], 'violated':[{'condition':'Fresh-sign rank-one/singleton criticality','domain':'N>=5,C>=1,D_C(J)>0','exact_left_side':'E_z D_C(J_z)>D_C(J)+13/32'}], 'unresolved':['Quantitative separation for all genuine critical signs']},
 {'class':'A054 thin-selector-cylinder plus density critical class','embedding':'two-tag connected wrapper T','preserved':['One actual connected negative component','Proper selector block A={y}','Selector point fixes d_y=1>=|A|/2','Connected data support','Density p=(3-Eg)/8 in [1/4,1/2]','Limiting optimal FEI constant after tensor amplification'], 'violated':[{'condition':'Every proper physical restriction has nonpositive D_C','block':'two tags {w,y}','exact_left_side':'-D_C(g)/4'}], 'unresolved':['Universal admission of affordable separators with nonpositive-deficit terminal children'], 'scope':'A054 critical-class payment remains intact; geometry/density alone are FEI-hard'},
 {'class':'Full ratio criticality','embedding':'g*h','preserved':['Possible when nonconstant factors have equal ratios and no descendant improves them'], 'violated':[{'condition':'No higher-ratio child','when':'H(g)/I(g)>R(g*h)','exact_left_side':'L_Y-R(F) I_Y=-[H(g)-R(F)I(g)]<0'}], 'unresolved':['No universal equivalence or exclusion is inferred from averaged block tests alone']}
]
write('EXTREMAL_SCOPE_VERDICTS.json',{'units':'bits','verdicts':verdicts,'universal_status':'OPEN'})

progress={
 'protocol_revision':protocol['revision'], 'run_id':RUN_ID,'stream':'B11','packet_id':'A055',
 'gap_id':'G-B11-CRITICAL-CLASS-ADMISSION','attempt_id':'A055-stage1-exact-block-shortfalls',
 'method':'Independent scope review, all-dimensional exact Fourier/deficit identities, connected two-tag wrapper, centered singleton surgery exclusion, rational finite validation',
 'mathematical_delta':'Quantified tensor/activation criticality failures; arbitrary-core admission into the complete noncritical A054 geometric/density class with exact quarter-core shortfall; uniform >13/32 singleton child-deficit margin for edited balanced tensors; independent acceptance of A053 v1 at scope',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF',
 'mathematical_status':'SCOPED_ADMISSION_OBSTRUCTIONS_PROVED; UNIVERSAL_PROPER_BLOCK_DESCENT_OPEN; NEW_A055_REVIEW_PENDING',
 'claim_versions_used':[{'claim_id':'A053-NEAR-TENSOR-CURVATURE-ADMISSION','version':1,'use':'independent analytic review; not required as an unproved premise of the self-contained A055 proof'}],
 'claims_created_or_changed':[{'claim_id':new['claim_id'],'version':1,'change':'created'}, {'claim_id':reviewed['claim_id'],'version':1,'change':'independent scope review added locally for adoption'}],
 'source_artifacts':['REPORT.md','EMBEDDING_PROOF.md','CRITICAL_CLASS_EMBEDDINGS.tex','EXTREMAL_SCOPE_VERDICTS.json','REVIEW_A053.md','out/EXACT_CHECK.json','out/TAG_CHECK.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':['A005','A051','A052','A053','A054','A090','A094','B20'],
 'next_action':'Bound retained conditional Fourier entropy on a two-tag separator with every proper terminal child of nonpositive deficit; independently reconstruct the arbitrary-core geometric/density admission and its exact failed criticality test',
 'stagnant_substantive_attempts':0,'blockers':[], 'packet_ids':['A055']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)

sources=[CANON/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
sources += list((CANON/'runs').rglob('REPORT.md'))
sources += [SUP/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += [SUP/'sources'/x for x in ['BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ADDENDUM_11_26_CRITICAL_RARE_MOMENT.md']]
sources += list((TEAM/'context').glob('*.txt'))
sources += [TEAM/'BOARD.md',TEAM/'claude/B11/STREAM_NOTES.md']
for a in ['A051','A052','A053','A054']:
    sources += list((TEAM/'agents'/a/'runs').rglob('REPORT.md'))
sources += list((TEAM/'agents/A053/runs').rglob('HIDDEN_TENSOR_DIAGNOSTIC.md'))
sources += [source_claim]
sources += list((TEAM/'agents/A054/runs').rglob('CRITICAL_INTERFACE_PAYMENT.md'))
manifest=[]
for path in sources:
    b=path.read_bytes()
    try: b.decode('utf-8');encoding='utf-8'
    except UnicodeDecodeError: b.decode('cp1252');encoding='cp1252'
    manifest.append({'path':str(path),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'encoding':encoding,'read_scope':'See REPORT.md source locators; hashing/full loading does not imply full proof audit of unrelated sections'})
write('out/SOURCE_MANIFEST.json',{'local_byte_provenance':manifest,'remote_readback_claimed':False})

validation={name:json.loads((ROOT/'out'/name).read_text(encoding='utf-8')) for name in ['PILOT.json','EXACT_CHECK.json','TAG_CHECK.json']}
write('out/VALIDATION_SUMMARY.json',validation)
# The protocol annotates the final field in prose; its explicit compatibility
# rule defines the actual JSON key as packet_ids.
progress_fields=['packet_ids' if field.startswith('packet_ids (') else field for field in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(progress_fields)
assert json.loads((ROOT/'PACKET_DELTA.json').read_text(encoding='utf-8'))==progress
for c in [reviewed,new]: assert set(c)==set(protocol['required_per_run']['claim_fields'])
text=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']: assert '# '+field in text

stamp=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A055 stage complete: exact criticality shortfalls, connected two-tag FEI-hard admission, >13/32 surgery singleton exclusion; A053 v1 independently accepted locally; full FEI OPEN.\nNEXT: A090/A094 review; pay conditional Fourier entropy on a genuine critical separator with nonpositive-deficit terminal children.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+': Completed 37,737 exact embedding assertions and 3,615 two-tag assertions, after an 838-assertion pilot. Independently accepted A053 v1 without repair. Tensor/activation failed actual criticality; changed mechanism to a connected two-tag wrapper passing all A054 geometry/density requirements, but failing its tag-block criticality by D_C(g)/4. Surgery on balanced tensors fails a singleton test by more than 13/32 for N>=5,C>=1. Saved protocol-shaped records; universal proper-block selection remains open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nFor arbitrary g, two tags can create one connected negative cylinder of density (3-Eg)/8 in [1/4,1/2], with I=I(g)/4+1 and H=H(g)/4+O(1), 0<=O(1)<=9/2. Thus A054 geometry plus density alone preserves the optimal unrestricted FEI constant; all-descendant criticality fails by D_C(g)/4. A one-point edit of (-1)^z G on N>=5 bits retains signed-translation mismatch 2^(1-N); at C>=1 its averaged fresh-sign child deficit exceeds the parent by >13/32. Full Fourier support does not eliminate near-symmetry. Ratio-critical products may have equal-ratio factors, whereas positive-deficit dimension-critical products cannot contain a violating factor.\n')

receipts=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and path.name!='RECEIPTS.json':
        b=path.read_bytes(); assert len(b)<20*1024*1024
        receipts.append({'path':str(path.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
write('out/RECEIPTS.json',{'saved_at_utc':stamp,'files':receipts,'protocol_field_sets':'PASS','local_persistence':'VERIFIED','supervisor_copy':'NOT_CLAIMED','mirror_verification':'NOT_CLAIMED'})
print(json.dumps({'status':'PASS','claims':len([reviewed,new]),'protocol_field_sets':'PASS','saved_artifacts':len(receipts),'exact_assertions':validation['EXACT_CHECK.json']['assertions']+validation['TAG_CHECK.json']['assertions']},indent=2))
