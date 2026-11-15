"""Exact cutoff scan using the lead's independent 86 endpoint certificates.

This is a finite certificate conditional on the general-L analytic lemma.
No solver code or Bernstein polynomial is imported.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import hashlib
import math
import json

HERE=Path(__file__).resolve().parent
source=HERE/'T067_OWN_ENDPOINT_MAP.json'
data=json.loads(source.read_text(encoding='utf-8'))
upper={F(k):F(v) for k,v in data['endpoint_g_upper'].items()}
points=[F(10,100-i) for i in range(86)]
assert set(upper)==set(points)
for name,expected in data['source_files'].items():
    assert hashlib.sha256((HERE/'t067_own_endpoints'/name).read_bytes()).hexdigest()==expected

def check(D):
    scale=10**8
    q=math.isqrt(scale*scale//D)
    if D*q*q<scale*scale:q+=1
    L=F(q,scale)
    assert D*L*L>=1 and L<=F(1,10)
    B4=F(25,288)+F(49,100)*L/(1-L)
    B3=F(1,6)+F(49,20)*L*B4
    B1=F(5,24)+F(49,20)*L*B3
    CU=(F(1,48)+F(49,160)*L*B4
        +F(1,10)*(F(1,24)+B3*(1/(1-L)+1+L/2)+F(1,6))
        +B1/(4*(1-L)**2)+F(1,15)+1/(40*(1-L)**4))
    CM=F(1,60)+F(5,48)+L*L/36+(2+4*L*L+L**4)/40
    factor=F(81,D)
    records=[]
    for index,(a,b) in enumerate(zip(points,points[1:])):
        slope=(upper[b]-upper[a])/(b-a)
        cuts=sorted({a,b}|({F(2,15)} if a<F(2,15)<b else set()))
        for left,right in zip(cuts,cuts[1:]):
            low=right<=F(2,15)
            quadratic=16-factor*(5*CU+CM if low else CM)
            linear=1-slope-16*(a+b)-(0 if low else factor*F(2,3)*CU)
            constant=16*a*b-upper[a]+slope*a
            choices=[left,right]
            if quadratic>0:
                vertex=-linear/(2*quadratic)
                if left<vertex<right:choices.append(vertex)
            minimizer=min(choices,key=lambda t:quadratic*t*t+linear*t+constant)
            minimum=quadratic*minimizer**2+linear*minimizer+constant
            records.append({'interval':index,'left':str(left),'right':str(right),
                'minimum':str(minimum),'minimizer':str(minimizer)})
    worst=min(records,key=lambda r:F(r['minimum']))
    return {'D':D,'L':str(L),'CU':str(CU),'CM':str(CM),
        'passed':F(worst['minimum'])>0,'worst_interval':worst['interval'],
        'minimum_exact':worst['minimum'],'minimum_float':float(F(worst['minimum'])),
        'records':records}

trials=[]
for D in range(156,99,-1):
    result=check(D)
    trials.append(result)
    print(json.dumps({k:result[k] for k in ['D','passed','minimum_float','worst_interval']}),flush=True)
    if not result['passed']:break
passes=[t for t in trials if t['passed']]
assert passes
best=min(passes,key=lambda r:r['D'])
output={'at':datetime.now().astimezone().isoformat(),'status':'conditional exact finite gate',
    'best_cutoff':best['D'],'best':best,'trials':trials,
    'endpoint_map_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'scope':'Uniform analytic composition for all d>=D remains conditional on independently reviewed general-L comparison, Gaussian curvature and fixed-point premises; failed lower D is a failure of this frozen certificate, not reconstruction.'}
(HERE/'T067_CUTOFF_SCAN.json').write_bytes((json.dumps(output,indent=2)+'\n').encode('utf-8'))
print('BEST CERTIFICATE CUTOFF',best['D'],flush=True)
