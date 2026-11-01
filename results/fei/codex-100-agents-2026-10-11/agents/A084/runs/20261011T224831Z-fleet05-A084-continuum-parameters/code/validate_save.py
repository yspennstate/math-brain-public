from pathlib import Path
from fractions import Fraction as R
import json,hashlib,datetime
from certify import bound,hpoint,add,mul,sub,ONE
root=Path(__file__).resolve().parents[1]; agent=root.parents[1]
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
checks=0
for name in ['POSITIVE_RECTANGLE','COMPACT_COVER']:
    obj=json.loads((root/'out'/f'{name}.json').read_text()); area=R(0)
    for leaf in obj['leaves']:
        box=tuple(map(R,leaf['box']));v=tuple(map(R,leaf['F_interval']))
        assert bound(box)==v
        assert leaf['sign']==('positive' if v[0]>0 else 'negative' if v[1]<0 else 'unresolved')
        area+=(box[1]-box[0])*(box[3]-box[2]);checks+=2
    b=tuple(map(R,obj['initial_box']));assert area==(b[1]-b[0])*(b[3]-b[2]);checks+=1
# Check the alternative conditional-entropy formula at fresh rational biases.
for p,q in [(R(1,10),R(1,5)),(R(3,20),R(3,10)),(R(7,10),R(11,20)),(R(9,10),R(3,4))]:
    r=4*q*(1-q);t=p*r;b=4*p*(1-p)*q*q
    alternate=sub(sub(sub(hpoint(t),mul((p,p),hpoint(r))),mul((1-t,1-t),hpoint(b/(1-t)))),mul((t,t),hpoint(p)))
    v=bound((p,p,q,q));assert max(v[0],alternate[0])<=min(v[1],alternate[1]);checks+=1
result=json.loads((root/'out'/'RESULT.json').read_text())
statement='For the independent Bernoulli biased AND sign g(X,Y)=(-1)^(XY), physical A={X}, J_A-M_A is strictly positive for every real (p,q) in [1/10,3/20] x [1/5,3/10]. The continuous boundary identities and pointwise asymptotics are those in REPORT equations (3)-(7). The full-square sign map remains open.'
hyp=['Independent Bernoulli(p), Bernoulli(q)','Actual two-bit Boolean gate and normalized product Fourier basis','Shannon entropy in bits','Boundary expressions interpreted as continuous limits']
sha=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A084-AND-CONTINUUM-CERTIFICATE','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':sha,'contributors':['A084'],'proof_source':{'path':str(root/'REPORT.md'),'certificates':['out/POSITIVE_RECTANGLE.json','out/COMPACT_COVER.json'],'checker':'code/certify.py'},'proof_dependencies':[],'review_records':[],'status':'RESTRICTED_CERTIFICATE_CHECKED_REVIEW_PENDING_FULL_MAP_OPEN','supersedes':[],'refutes':['tax-free J_A<=M_A throughout the certified rectangle'],'first_unproved_line':'Number, geometry and exhaustive signs of the additional zero curves in the open bias square; 902 compact boxes remain unresolved.','next_consumers':['A090','A094','B09','A041','A046','A064']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
(root/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B17','packet_id':'A084','gap_id':'G-BIASED-TAX','attempt_id':'A084-continuum-1','method':'Exact rational log interval subdivision plus analytic zero-line and four-edge asymptotics','mathematical_delta':'Positive real bias rectangle certified by 64 boxes; 94 negative compact boxes; exact boundary identities; full sign map open with 902 unresolved boxes. Existing biased-AND obstruction refined; no universal candidate opened.','deliverable_status':'ARTIFACT_COMPLETE_PARTIAL_TARGET','mathematical_status':'RESTRICTED_REGION_CERTIFIED_GLOBAL_TARGET_OPEN','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'scope':'restricted numerical certificate and boundary reduction, not a new broad FEI candidate'}],'source_artifacts':['REPORT.md','CLAIMS.json','FROZEN_SPEC.json','code/certify.py','out/POSITIVE_RECTANGLE.json','out/COMPACT_COVER.json','out/RESULT.json','out/SOURCE_MANIFEST.json'],'next_consumers':['A090','A094','B09','A041','A046','A064'],'next_action':'Enclose F/(q-1/2) with analytic h(r) cancellation; test and prove/refute p-monotonicity on each side to isolate extra zero curves.','stagnant_substantive_attempts':0,'blockers':['Analytic joint-corner and extra-zero-curve classification remains unproved; no access blocker.'],'packet_ids':['A084']}
# Protocol's final entry is a descriptive label; compatibility instructions
# explicitly prescribe the actual JSON key packet_ids.
expected={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
for n in ['PROGRESS.json','PACKET_DELTA.json']:(root/n).write_text(json.dumps(progress,indent=2),encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A084 restricted continuum certificate saved: 64 positive and 94 negative boxes; boundary reductions proved; full sign map and FEI OPEN; review pending.\nNEXT: Enclose F/(q-1/2), resolve extra zero curves by p-monotonicity; A090/A094 review the exact certificate.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: Read protocol/board/B17 target. Derived AND formulas and q=1/2 identity. Binary64 pilot showed extra sign transitions. Fraction interval run (57.235s) certified entire positive rectangle with 64 leaves, 94 negative compact leaves; retained 902 unresolved leaves. Proved pointwise boundary asymptotics; full map remains open. Validation rechecked every saved interval and alternative conditional-entropy formula; review and mirror pending.\n')
(agent/'LEARNED.md').write_text('For Bernoulli biased AND with A={X}, r=4q(1-q), t=pr, masses ((1-2pq)^2,4p(1-p)q^2,p^2r,p(1-p)r), F=J-M=2h(t)-p h(r)-H(masses). F=0 on q=1/2 and the p=0,p=1,q=0 edges; F(p,1)=-h(4p(1-p)). The full real rectangle [1/10,3/20] x [1/5,3/10] has F>0 by 64 exact rational interval leaves. A fixed-bias boundary asymptotic does not cover joint corners. Fixed log precision cannot certify arbitrarily small margins; zero curves require analytic cancellation/divided differences. Full FEI remains open.\n',encoding='utf-8')
receipts=[]
for f in root.rglob('*'):
    if f.is_file() and f.name!='RECEIPTS.json' and '__pycache__' not in f.parts:
        data=f.read_bytes();assert len(data)<20*1024*1024
        receipts.append({'path':str(f.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
receipt={'checks_passed':checks,'checks':'Every saved box interval recomputed; leaf sign checked; total rational area checked; four alternative conditional formula overlaps; exact protocol JSON key sets checked. This is same-author verification, not independent acceptance.','files':receipts,'mirror_verified':False,'independent_review':'pending','full_sign_map':'OPEN'}
(root/'out'/'RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'checks_passed':checks,'files_receipted':len(receipts),'status':'saved; full map open'}),flush=True)
