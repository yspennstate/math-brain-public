"""Persist A068 stage metadata, source pins and local receipts."""
from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
RUN=ROOT.name
def sha(data): return hashlib.sha256(data).hexdigest()
def save(name,obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
validation=json.loads((ROOT/'out/validation.json').read_text(encoding='utf-8'))
core=json.loads((ROOT/'out/quadratic_core.json').read_text(encoding='utf-8'))
assert validation['status']==core['status']=='PASS'
assert validation['actual_boolean_lift_cases']==16658
assert validation['quadratic_control_cases']==3106
assert core['all_quadratic_phase_cases']==2198
source_root=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
sources=[]
for p,scope in [(source_root/'baseline/current-threshold-paper.tex','rank/noise/reference/centering/width proofs and locators'),
                (source_root/'SEED_LEMMAS.md','full; existing effective-piece and normalized-prior interfaces'),
                (source_root/'sources/ERASURE_REDUCTION.md','sections 1-6'),
                (source_root/'sources/OVERLAPPING_PRODUCT_NOTE.md','full short source note'),
                (source_root/'sources/ROUTE_MAP_CURATED.md','sections 1-4; signed-translation reduction especially 2.1')]:
    sources.append({'path':str(p),'sha256':sha(p.read_bytes()),'read_scope':scope,'used_in_proof':p.name=='current-threshold-paper.tex'})
for p in context.glob('*.txt'):
    sources.append({'path':str(p),'sha256':sha(p.read_bytes()),'read_scope':'introductions and rank/width/encoding locators; not a full independent proof reconstruction','used_in_proof':False})
save('out/SOURCES.json',sources)
statement=('For every regular Boolean h on q distinct private data bits and every finite list of arbitrary degree-at-most-two F2 control polynomials Q_i on m independent uniform bits, F(x,z)=h(x_i*(-1)^Q_i(z)) satisfies H(F)<=C_reg*I_x(F)+2*I_z(F)<=C_reg*I(F), C_reg=log2(4+e)+2log2(e*pi)<8.937; moreover H(F)<=C_reg*D_x(F)+2*I_z(F). Its data-indexed spectral packets have exact probabilities hhat(S)^2*2^(-rank B_S) on the affine Fourier support of the quadratic phase sum_i_in_S Q_i, and a normalized rank reference pays all packet ranks. For every odd q>=5, the nonlinear cyclic controlled-majority family has I_x=q*c_q, I_z=3*q*c_q/4 and H/I<=(4*C_reg+6)/7, while it is non-unate and selector influence per control tends to zero.')
deps=[{'claim_id':'C001','version':'supplement 2026-10-11 / baseline current source',
       'source_sha256':sources[0]['sha256'],
       'locators':['lem:pivotal-antichain','lem:antichain-noise','lem:ranktail','lem:levelentropy','eq:euler-reference','eq:euler-cost','thm:A'],
       'acceptance':'recovered baseline; local dependency reconstruction recorded; no new external acceptance claimed'}]
claim={'claim_id':'A068-QUADRATIC-CONTEXT-RANK-REFERENCE','version':1,'exact_statement':statement,
       'hypotheses':['uniform independent physical data/control coordinates','h regular in oriented total-desirability sense','each data coordinate private and distinct','each Q_i has F2 degree at most two; controls may overlap arbitrarily','entropy in bits; D_x=sum min(data influences,1-data influences)','cyclic separation formula uses odd q>=5'],
       'statement_sha256':sha(statement.encode()),'contributors':['A068/fleet05'],
       'proof_source':{'run_id':RUN,'path':str(ROOT/'REPORT.md'),'supplement':str(ROOT/'NEW_RANK_GEOMETRY.tex'),'validation':str(ROOT/'out/validation.json'),'separate_core_check':str(ROOT/'out/quadratic_core.json')},
       'proof_dependencies':deps,'review_records':[],
       'status':'AUTHOR_PROVED_EXACT_CHECKS_PASSED_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],'refutes':[], 'first_unproved_line':None,
       'next_consumers':['A070','A088','A094','B02','B04','B08','B12','B20']}
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B14','packet_id':'A068',
          'gap_id':'G-A068-CONTEXT-RANK-REFERENCE','attempt_id':'A068-stage1-quadratic-context',
          'method':'context-dependent pivotal orientations, exact private-data Fourier packets, quadratic affine-flat cost, normalized Euler reference',
          'mathematical_delta':'Proved complete H<=C_reg I_x+2 I_z on systematic quadratic-control regular gates; paid nonlinear spectral fiber rank; exhibited non-unate cyclic low-selector-energy family beyond width and positive-energy bounds. Linear-control reduction explicitly credited to recovered signed translations.',
          'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'CLASS_TARGET_PROVED_LOCALLY_FULL_FEI_OPEN_REVIEW_PENDING',
          'claim_versions_used':deps,'claims_created_or_changed':['A068-QUADRATIC-CONTEXT-RANK-REFERENCE@1'],
          'source_artifacts':['REPORT.md','NEW_RANK_GEOMETRY.tex','WIDTH_SEPARATION_EXAMPLE.md','CLAIMS.json','out/SOURCES.json','out/FROZEN_SPEC.json','out/QUADRATIC_CORE_SPEC.json','code/check.py','code/quadratic_core.py','out/pilot.json','out/validation.json','out/quadratic_core.json','out/RECEIPTS.json'],
          'next_consumers':['A070','A088','A094','B02','B04','B08','B12','B20'],
          'next_action':'Identify one pair of private data coordinates; derive exact signed two-row collision/reference cost and retain normalization and phase cross terms.',
          'stagnant_substantive_attempts':0,
          'blockers':['B14 STREAM_NOTES.md absent at stage start','independent review and supervisor mirror/adoption pending; not blockers to local class proof'],
          'packet_ids':['A068']}
save('PROGRESS.json',progress)
save('PACKET_DELTA.json',progress)
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('Full results are in out/validation.json; this paragraph is finalized after reading that output.',
    f"Full results: {validation['assertions']:,} assertions passed, 0 failed, in {validation['runtime_seconds']:.3f} seconds (within the frozen 180-second bound). A separate direct-character transform and F2 row-elimination implementation checked all {core['all_quadratic_phase_cases']:,} quadratic phases in dimensions 0 through 4: {core['assertions']:,} assertions passed in {core['runtime_seconds']:.3f} seconds. It verifies polar-matrix rank against exact affine spectral support size. This separate implementation is not independent human/agent review.")
report=report.replace('    python -X utf8 runs/20261011T222313Z-fleet05-A068-antichain-beyond-one-order/code/check.py\n',
    '    python -X utf8 runs/20261011T222313Z-fleet05-A068-antichain-beyond-one-order/code/check.py\n    python -X utf8 runs/20261011T222313Z-fleet05-A068-antichain-beyond-one-order/code/quadratic_core.py\n')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A068 quadratic-context rank reference proved locally: H<=C_reg I_x+2 I_z; 461,872 exact assertions passed; independent review pending; full FEI OPEN.\nNEXT: A088/A094 review; analyze one private-data identification with exact signed two-row collisions and normalization.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' Linear systematic parity lifts were recognized as recovered signed-translation symmetry applications. Changed mechanism to nonlinear quadratic control fibers. Completed context-antichain/reference proof and cyclic width/low-selector separation; 448,684 main assertions and 13,188 separate quadratic-core assertions passed. Artifacts saved locally; external review/mirror pending.\n')
(AGENT/'LEARNED.md').write_text('''# A068 durable results

For F(x,z)=h(x_i a_i(z)) with distinct private data bits, the Fourier law is exactly P(S,T)=hhat(S)^2 ahat_S(T)^2, where a_S=product of controls indexed by S. Therefore H(F)=H(h)+E H(a_S), I_x=I(h), and I_z=E I(a_S). Distinct data labels are the reason there are no coherent collisions.

Regular h retains predecessor-fiber pivotal antichains in orientations depending on the exterior control assignment. Resampling data predecessors fixes that assignment, so the sharp signed rank mean 1+ln 2 remains valid.

Every degree<=2 F2 phase has squared Fourier law uniform on an affine space of dimension rank of its alternating polar matrix. Its entropy rank is at most twice influence. Thus arbitrary overlapping quadratic controls give H(F)<=C_reg I_x+2I_z, with complete normalized Euler/affine-fiber reference. Nonlinear cyclic controlled majority has I_x=q c_q, I_z=3q c_q/4 and is not unate; selector influence per control tends to zero.

Linear controls have singleton Fourier fibers and H(F)=H(h). This is already a recovered signed-translation reduction, not the stage's new mechanism. General controls make E H(a_S)<=K E I(a_S) FEI-equivalent at a dictator base, so do not silently generalize quadratic payment to arbitrary controls.

Next missing structural step: identify two private data bits, deriving signed two-row collisions rather than incoherent mixture entropy. Full FEI remains open. Main proof: runs/20261011T222313Z-fleet05-A068-antichain-beyond-one-order/REPORT.md. Independent review pending; novelty unverified beyond local sources.
''',encoding='utf-8')
receipts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        data=p.read_bytes()
        assert len(data)<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':sha(data)})
save('out/RECEIPTS.json',{'saved_at_utc':now,'run_id':RUN,'local_only':True,'mirror_verified':False,'files':receipts})
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','run_id':RUN,'local_files':len(receipts),
                  'main_assertions':validation['assertions'],'quadratic_core_assertions':core['assertions'],
                  'claim_status':claim['status'],'full_fei':'OPEN'},indent=2))
