"""Read the saved failed gate and measure whether a bounded refinement is worth a pilot."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
mp=HERE/'T067_OWN_ENDPOINT_MAP.json'
data=json.loads(mp.read_text(encoding='utf-8'))
assert sha(mp)=='3e2da056f21fdadb6c7b4be7e4e453935dde996dc932705c52bb7862ea2840fb'
upper={F(k):F(v) for k,v in data['endpoint_g_upper'].items()}
lower={}
for filename,digest in data['source_files'].items():
    p=HERE/'t067_own_endpoints'/filename;assert sha(p)==digest
    row=json.loads(p.read_text(encoding='utf-8'));lower[F(row['s'])]=F(row['g_lower'])
scan=json.loads((HERE/'T067_CUTOFF_SCAN.json').read_text(encoding='utf-8'))
trial=next(r for r in scan['trials'] if r['D']==155)
assert not trial['passed']
failed=[r for r in trial['records'] if F(r['minimum'])<=0]
assert failed
records=[];points=set()
for r in failed:
    a,b,x,h=map(F,(r['left'],r['right'],r['minimizer'],r['minimum']))
    assert a<=x<=b
    wa,wb=(b-x)/(b-a),(x-a)/(b-a)
    optimistic=h+wa*(upper[a]-lower[a])+wb*(upper[b]-lower[b])
    records.append({'interval':r['interval'],'a':str(a),'b':str(b),'x':str(x),
        'minimum':str(h),'optimistic_at_witness':str(optimistic),
        'optimistic_at_witness_float':float(optimistic)})
    points.update([a,b])
candidates=[]
for point in sorted(points):
    predicted=[]
    for r in records:
        a,b,x,h=map(F,(r['a'],r['b'],r['x'],r['minimum']))
        weight=(b-x)/(b-a) if point==a else (x-a)/(b-a) if point==b else F(0)
        # HEURISTIC only: halving the bin width quarters the global Taylor error.
        predicted.append(h+weight*F(3,8)*(upper[point]-lower[point]))
    candidates.append({'point':str(point),'width':str(upper[point]-lower[point]),
        'predicted_worst_witness':str(min(predicted)),
        'predicted_worst_witness_float':float(min(predicted))})
selected=max(candidates,key=lambda r:F(r['predicted_worst_witness']))
out={'at':datetime.now().astimezone().isoformat(),'endpoint_map_sha256':sha(mp),
    'status':'Plan only; no new enclosure and no new cutoff theorem',
    'failed_intervals':records,'candidates':candidates,'selected_point':selected['point'],
    'optimistic_witnesses_allow_refinement':all(F(r['optimistic_at_witness'])>0 for r in records),
    'pilot_guard':'Check frontier route first; compute at most one selected endpoint on h1/32, time it, then rerun the entire exact gate. The predicted improvement is not a rigorous lower bound on the actual gain.'}
(HERE/'T067_155_REFINEMENT_PLAN.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'failed_intervals':[r['interval'] for r in records],
    'selected':selected,'optimistic_witnesses_allow_refinement':out['optimistic_witnesses_allow_refinement']}))
