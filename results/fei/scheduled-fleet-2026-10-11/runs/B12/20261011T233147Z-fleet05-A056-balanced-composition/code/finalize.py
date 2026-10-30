from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
def dump(p,z): p.write_text(json.dumps(z,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
proto_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
proto=json.loads(proto_path.read_text(encoding='utf-8'))
checks=json.loads((run/'out/checks.json').read_text(encoding='utf-8'))
assert checks['physical_splits']==16384 and checks['all_exact_assertions_passed']
assert checks['negative_L_cases']>0
for z in checks['fixtures']:
    assert z['I_coordinate_F']=='1/4' if 'dictator' in z['name'] else z['I_coordinate_F']=='3/8'
assert 4*5**5<3**9
root=Path(r'~\brain_workers\FEI100_20261011')
paths=[proto_path,root/'BOARD.md',root/'claude/B12/STREAM_NOTES.md',
    agent/'runs/20261011T214407Z-fleet05-A056-balanced-composition/REPORT.md',
    agent/'runs/20261011T214407Z-fleet05-A056-balanced-composition/COMPOSITION_INTERFACE.json',
    root/'agents/A057/runs/20261011T220314Z-fleet05-A057-coherent-restriction-remainder/REPORT.md',
    root/'agents/A091/runs/20261011T214848Z-fleet05-A091-composition-referee/REPORT.md']
manifest=[]
for p in paths:
    b=p.read_bytes(); manifest.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
dump(run/'out/source_manifest.json',manifest)
consumers=['A057','A059','A060','A024','A091','A090','B20']
statement='For every disjoint Boolean substitution F=h(g_1,...,g_k) on independent uniform physical blocks and coordinate i in child j, write h=A+y_j B in the current other-output normalized product basis, m=E g_j, v=1-m^2, beta=g_jhat({i}), t=beta^2, C_T=a_T+m b_T, q=sum b_T^2. With e(s,t)=phi(s)+phi(t)-phi(s+t), d(a,b)=phi(a^2)+phi(b^2)-(phi((a+b)^2)+phi((a-b)^2))/2, phi(s)=s log2(1/s), M(t)=sum e(C_T^2,t b_T^2), N(t)=sum[d(C_T,beta b_T)-e(C_T^2,t b_T^2)], B_i(F)=q[B_i(g_j)-e(m^2,t)]+M(t) and D_i(F)=q[D_i(g_j)-d(m,beta)]+M(t)+N(t). For v>0, 0<=t<=v, M(t)<=min{M(v),(t/v)M(v)+q t log2(v/t)}, M(v)=B_j^mu(h), and 0<=N(t)<=(2/ln2)qt. The log and N terms cost at most [(2+2/e)/ln2] times consumed physical query influence in any represented stopping tree. Constants are absorbed at v=0. The corrected residual M(t)-q e(m^2,t) may be negative; AND2(OR2,OR2) gives 1/4-(9/8)log2(3)+(5/8)log2(5)<0.'
claim={'claim_id':'A056-DISJOINT-COMPOSITION','version':2,'exact_statement':statement,
       'hypotheses':['Boolean sign functions','independent uniform physical inputs','mutually disjoint child blocks','current means and normalized output product basis','entropy in bits','physical coordinate query; deterministic outputs fixed before division'],
       'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['fleet05/A056'],
       'proof_source':{'path':str(run/'REPORT.md'),'locators':'equations (1)-(12); code/check.py exact finite corroboration'},
       'proof_dependencies':[],'review_records':[], 'status':'FOCUSED_INTERFACE_EXTENSION_PROVED_LOCALLY_REVIEW_PENDING',
       'supersedes':[{'claim_id':'A056-DISJOINT-COMPOSITION','version':1,'scope':'Extends the adopted coefficient/mean interface; earlier identities remain valid'}],
       'refutes':['Extending the balanced nonnegative erasure correction to arbitrary biased children without its subtracted empty pair'],
       'first_unproved_line':None,'next_consumers':consumers}
dump(run/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B12','packet_id':'A056',
    'gap_id':'FEI-B12-BIASED-DESCENDANT-ERASURE-TRANSPORT','attempt_id':'A056-stage2-biased-erasure-1',
    'method':'Focused repair of recentered composition interface; exact empty-pair sector reconstruction and finite prime-log certificate',
    'mathematical_delta':'Exact biased-child B_i/D_i splits and positive-sector envelope; logarithm+JS query bank survives biased physical descendants. Signed erasure correction can be negative. Universal gate/child/terminal reserve remains unpaid.',
    'deliverable_status':'COMPLETE_LOCAL; copying pending','mathematical_status':'INTERFACE_PROVED_LOCAL_REVIEW_PENDING; UNIVERSAL_C019_PAYMENT_OPEN; FULL_FEI_OPEN',
    'claim_versions_used':[{'claim_id':'A056-DISJOINT-COMPOSITION','version':1,'acceptance':'A091 stage1 independent reconstruction and B12 lead adoption; source-pinned in manifest','role':'consumed baseline; proof independently reconstructed'}],
    'claims_created_or_changed':[{'claim_id':'A056-DISJOINT-COMPOSITION','version':2}],
    'source_artifacts':['REPORT.md','BIASED_ERASURE_INTERFACE.json','code/check.py','out/FROZEN_SPEC.json','out/pilot.json','out/checks.json','out/source_manifest.json'],
    'next_consumers':consumers,
    'next_action':'A057/A059 apply positive-sector biased split on source-pinned sparse-bent stopping tree and retain terminal entropy; A091 review after A057 queue priority.',
    'stagnant_substantive_attempts':0,'blockers':['Universal nonreusing current-gate/child/terminal reserve bound unproved','B12 review cap: this is the lead-directed focused interface repair; broad candidates not opened'],
    'packet_ids':['A056']}
assert set(progress)=={x.split(' ')[0] for x in proto['required_per_run']['progress_fields']}
assert set(claim)==set(proto['required_per_run']['claim_fields'])
dump(run/'PROGRESS.json',progress); dump(run/'PACKET_DELTA.json',progress)
assert json.loads((run/'PACKET_DELTA.json').read_text())==json.loads((run/'PROGRESS.json').read_text())
report=(run/'REPORT.md').read_text(encoding='utf-8')
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert len(report.split('## Universal bridge')[1].strip().split('\n\n'))==1
(agent/'STATUS.md').write_text('STATE: A056 v1 adopted by A091/B12; biased B_i/D_i interface v2 complete locally, 16384 exact splits passed; C019/full FEI OPEN.\nNEXT: A057/A059 test nonempty child + biased gate erasure + terminal reserve on sparse-bent physical tree; A091 review v2 after A057.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} — Stage 2 consumed A091 acceptance and B12 v2 direction. Derived biased erasure and physical entropy-decrement split with exact empty-pair subtraction, positive M envelope and query-paid log+JS. All 16384 physical splits and 4 fixtures passed exact prime-log/Fraction certificates in {checks["runtime_seconds"]:.6f}s. Negative L cases {checks["negative_L_cases"]}; negative signed JS cases {checks["negative_J_cases"]}. AND(OR2,OR2) refutes nonnegative biased correction by 12500<19683. Universal residual still open; completed focused v2 interface, no broad new class candidate.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''
## Stage 2: physical biased-child erasure

With h=A+y_jB expanded in the current other-output normalized product basis, m=E g_j, v=1-m^2, beta=g_jhat({i}), t=beta^2, C=a+m b, q=sum b^2: B_i(F)=q[B_i(g_j)-e(m^2,t)]+M(t), D_i(F)=q[D_i(g_j)-d(m,beta)]+M(t)+N(t). Here e(s,t)=(s+t)h2(t/(s+t)), d(a,b) is the raw physical pair entropy decrement, M=sum e(C^2,t b^2), N=sum j(C,beta b). Empty-pair subtraction is mandatory; nonempty sectors are positive.

M(v)=B_j^mu(h) of the current normalized biased outer spectrum. M(t)<=min{M(v),(t/v)M(v)+q t log2(v/t)}; N<=(2/ln2)qt. Boolean |beta|<=Inf_i(g_j), so log+N cost at most [(2+2/e)/ln2] consumed physical query influence, once per tree node, even at biased descendants.

Signed corrections L=M-q e(m^2,t) and K=N-q j(m,beta) need not be positive. AND of two OR2 children gives L=1/4-(9/8)log2(3)+(5/8)log2(5)<0 exactly by 12500<19683. Use positive sectors or retain negative credits; never reuse balanced-L positivity below root. OR2 has B_i=1 and D_i=2 (both physical children have zero spectral entropy); its empty pair has e=1/2,d=1.

Stage-2 checker exhausts 16384 disjoint physical splits plus 4 fixtures with exact rational prime-log vectors, independent physical-child decrements and integer-product signs. The universal next gap is the expected nonempty-child/current-gate/terminal reserve on a stopping tree, not another chain-rule reproduction. A056 v1 was independently accepted by A091 and adopted by B12; v2 extension awaits review.
''')
dump(run/'out/artifact_validation.json',{'protocol_fields':'PASS','claim_digest':'PASS','delta_equality':'PASS','negative_L_integer_certificate':{'lhs':4*5**5,'rhs':3**9,'comparison':'<','verdict':'PASS'},'universal_bridge_final_paragraph':'PASS','finite_exact_splits':16384,'fixtures':4})
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='receipts.json' and '__pycache__' not in p.parts:
        b=p.read_bytes(); assert len(b)<20_000_000
        receipts.append({'path':str(p.relative_to(run)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
dump(run/'out/receipts.json',{'saved_at_utc':stamp,'local_only':True,'files':receipts})
print(json.dumps({'saved':True,'exact_splits':checks['physical_splits'],'negative_L':checks['negative_L_cases'],'negative_K':checks['negative_J_cases'],'files':len(receipts),'review':'pending','full_FEI':'OPEN'},indent=2))
