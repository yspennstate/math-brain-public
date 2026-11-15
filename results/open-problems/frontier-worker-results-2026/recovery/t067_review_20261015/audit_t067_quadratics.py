"""Independent exact vertex-minimum check of the d156 finite gate.

Uses saved rigorous endpoint upper bounds as premises; does not audit their
producers or the analytic replacement lemma. Imports no solver code.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import hashlib
import json
import argparse

HERE = Path(__file__).resolve().parent
ROOT = Path('~/brain_workers/w682')
proof = ROOT/'proofs/T067-PIECEWISE-D0-001_v1.md'
assert hashlib.sha256(proof.read_bytes()).hexdigest() == '9a8a26b8c0631b4549f29bdc7ee231130a080a680408394bb75e0a8c16986226'
endpointfile = ROOT/'checks/piecewise_raw_endpoint_verification.json'
parser=argparse.ArgumentParser()
parser.add_argument('--own-endpoints',action='store_true')
args=parser.parse_args()
if args.own_endpoints:
    paths=sorted((HERE/'t067_own_endpoints').glob('endpoint_*.json'))
    assert len(paths)==86,'Independent endpoints are incomplete'
    own=[json.loads(p.read_text(encoding='utf-8')) for p in paths]
    assert len({r['source_sha256'] for r in own})==1
    assert len({r['s'] for r in own})==86
    endpointfile=HERE/'T067_OWN_ENDPOINT_MAP.json'
    manifest={'endpoint_g_upper':{r['s']:r['g_upper'] for r in own},
        'source_files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    endpointfile.write_bytes((json.dumps(manifest,indent=2)+'\n').encode('utf-8'))
data = json.loads(endpointfile.read_text(encoding='utf-8'))
uppers = {F(k): F(v) for k,v in data['endpoint_g_upper'].items()}
points = [F(10,100-i) for i in range(86)]
assert set(uppers) == set(points)
L = F(16013,200000)
assert 156*L*L > 1 and L <= F(1,10)
B4 = F(25,288) + F(49,100)*L/(1-L)
B3 = F(1,6) + F(49,20)*L*B4
B1 = F(5,24) + F(49,20)*L*B3
CU = (F(1,48)+F(49,160)*L*B4
    + F(1,10)*(F(1,24)+B3*(1/(1-L)+1+L/2)+F(1,6))
    + B1/(4*(1-L)**2)+F(1,15)+1/(40*(1-L)**4))
CM = F(1,60)+F(5,48)+L**2/36+(2+4*L**2+L**4)/40
saved = json.loads((ROOT/'checks/piecewise_cutoff_independent.json').read_text(encoding='utf-8'))
assert CU == F(saved['CU']) and CM == F(saved['CM'])
factor = F(81,156)
answers = []
for index,(a,b) in enumerate(zip(points,points[1:])):
    slope = (uppers[b]-uppers[a])/(b-a)
    cuts = sorted({a,b} | ({F(2,15)} if a < F(2,15) < b else set()))
    for left,right in zip(cuts,cuts[1:]):
        low = right <= F(2,15)
        q = 16-factor*(5*CU+CM if low else CM)
        linear = 1-slope-16*(a+b)-(0 if low else factor*F(2,3)*CU)
        const = 16*a*b-uppers[a]+slope*a
        candidates = [left,right]
        if q > 0:
            vertex = -linear/(2*q)
            if left < vertex < right:
                candidates.append(vertex)
        argmin = min(candidates,key=lambda s:q*s*s+linear*s+const)
        minimum = q*argmin*argmin+linear*argmin+const
        assert minimum > 0, (index,str(left),str(right))
        # Cross-check the expanded quadratic against the unexpanded definition.
        middle = (left+right)/2
        direct = (middle-uppers[a]-slope*(middle-a)-16*(middle-a)*(b-middle)
            -factor*(CU*min(5*middle*middle,F(2,3)*middle)+CM*middle*middle))
        assert direct == q*middle*middle+linear*middle+const
        answers.append((minimum,index,left,right,argmin))
worst = min(answers)
result = {'at':datetime.now().astimezone().isoformat(),'claim':'T067-PIECEWISE-D0-001 v1',
    'status':'PASS conditional finite arithmetic gate only','method':'Exact quadratic endpoints and stationary vertices; no Bernstein certificate imported',
    'original_intervals':85,'segments_after_moment_kink_split':len(answers),
    'minimum_gap_float':float(worst[0]),'minimum_gap_exact':str(worst[0]),
    'worst_interval':worst[1],'minimizer':str(worst[4]),
    'CU':str(CU),'CM':str(CM),
    'endpoint_file_sha256':hashlib.sha256(endpointfile.read_bytes()).hexdigest(),
    'limit':'Saved endpoint bounds, analytic general-L replacement constants, derivative estimates and BP transfer remain premises. This does not promote the d156 theorem.'}
if args.own_endpoints:
    result['status']='PASS finite arithmetic gate with independently rebuilt endpoints'
    result['limit']='All 86 endpoint enclosures rebuilt by the lead at 180-bit Arb on the full signed grid. General-L replacement, softmax derivative constants, curvature and BP transfer still require analytic audit; this alone does not promote d156.'
outname='T067_OWN_FINITE_GATE_RECEIPT.json' if args.own_endpoints else 'T067_FINITE_GATE_RECEIPT.json'
(HERE/outname).write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
print(json.dumps({k:v for k,v in result.items() if k not in ('minimum_gap_exact','CU','CM')}))
