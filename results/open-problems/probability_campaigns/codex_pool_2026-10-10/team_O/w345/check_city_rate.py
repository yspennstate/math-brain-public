"""Numerical finite-case diagnostics for the newly verified spatial rate lemma."""
import json
import math
from pathlib import Path
import time
ROOT=Path(__file__).resolve().parent
started=time.perf_counter()
cases=0
def compositions(n):
    if n==0:
        yield ()
    else:
        for first in range(1,n+1):
            for tail in compositions(n-first):
                yield (first,)+tail
for t in range(1,11):
    for populations in compositions(t):
        M=len(populations)
        for beta in (0.5,1.0,2.0,2.1,3.0,4.0,6.0,10.0):
            q=2/beta
            lhs=sum(N**q for N in populations)
            rhs=M**max(1-q,0)*t**q
            assert lhs<=rhs*(1+1e-12)
            c0=0.7
            K=(2*math.pi)**(beta/2)*c0
            u=K*t*M**max(beta/2-1,0)
            area_upper=math.pi*(c0/u)**q*lhs
            assert area_upper<=0.5+1e-12
            cases+=1
path=ROOT/'measurements.json'
data=json.loads(path.read_text(encoding='utf-8'))
for K in (0.1,1.0,10.0):
    kappa=1/(32*(1+K))
    for log_t in (1000.0,1e6,1e8):
        m=math.floor(kappa*log_t)
        assert log_t/(4*(1+K))>=4*m
        cases+=1
new=dict(name='P0218_verified_model_disk_and_population_bound',cases=cases,status='PASS',seconds=time.perf_counter()-started,scope='Numerical checks of all positive population compositions for total population 1..10 and eight beta values, plus d=0 process thresholds; the continuum area argument is proved in the accompanying text.')
data['checks']=[check for check in data['checks'] if check['name']!=new['name']]+[new]
data['check_groups']=len(data['checks'])
data['cases']=sum(check['cases'] for check in data['checks'])
data['additional_commands']=['python -B -X utf8 check_city_rate.py']
data['additional_python_seconds']=new['seconds']
path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(new))
