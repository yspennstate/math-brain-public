"""Finite-generator and bookkeeping checks independent of the submitted code."""
import os
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
                  VECLIB_MAXIMUM_THREADS='1', MKL_NUM_THREADS='1')
import csv
import json
import math
from pathlib import Path
import subprocess
import numpy as np
from scipy.sparse import csr_matrix

ROOT=Path(__file__).resolve().parent

def generator(n, q):
    states=np.arange(1<<n)
    spins=(states[:,None] >> np.arange(n)[None,:]) & 1
    legal=np.empty_like(spins, dtype=bool)
    for x in range(n):
        legal[:,x]=(spins[:,x-1] if x else True) | (spins[:,x+1] if x<n-1 else True)
    rows=[]; cols=[]; vals=[]
    for s in states:
        total=0.
        for x in range(n):
            if legal[s,x]:
                rate=(1-q) if spins[s,x] else q
                rows.append(s);cols.append(s^(1<<x));vals.append(rate);total+=rate
        rows.append(s);cols.append(s);vals.append(-total)
    Q=csr_matrix((vals,(rows,cols)),shape=(1<<n,1<<n))
    pi=q**spins.sum(axis=1)*(1-q)**(n-spins.sum(axis=1))
    return Q,pi,spins

def uniformized_expectation(Q, f, t):
    """Poisson expansion of exp(tQ)f, using sparse products, no dense BLAS."""
    rate=float(np.max(-Q.diagonal()))
    if t==0 or rate==0:return f.astype(float)
    mean=rate*t
    steps=math.ceil(mean+20*math.sqrt(mean+1)+100)
    log_tail_bound=-mean+steps*(1+math.log(mean/steps))
    assert log_tail_bound < math.log(1e-30)
    weight=math.exp(-mean)
    vec=f.astype(float)
    answer=weight*vec
    mass=weight
    for k in range(1,steps+1):
        vec=vec+(Q@vec)/rate
        weight*=mean/k
        answer+=weight*vec
        mass+=weight
    assert abs(mass-1)<1e-12
    assert np.isfinite(answer).all()
    return answer

old_path=ROOT/'data'/'validation.json'
old=json.loads(old_path.read_text()) if old_path.exists() else None
if old is not None and not (ROOT/'data'/'validation_dense_first.json').exists():
    (ROOT/'data'/'validation_dense_first.json').write_text(json.dumps(old,indent=2)+'\n')
output={'simulation_checks':[], 'drift_checks':[],
        'exact_expectation_method':'Poisson uniformization of exp(tQ), omitted tail <1e-30'}
for q, tag in [(0.55,'055'),(0.6,'060'),(0.75,'075')]:
    path=ROOT/'data'/f'finite_q{tag}.csv'
    process=subprocess.run([str(ROOT/'simulate_referee'),str(q),'200000',str(71913+int(q*100)),
                            '7','1','100','0',str(path)],check=True,capture_output=True,text=True)
    Q,pi,spins=generator(7,q)
    dense=Q.toarray()
    detailed=pi[:,None]*dense
    row_error=float(np.abs(dense.sum(axis=1)).max())
    balance_error=float(np.abs(detailed-detailed.T).max())
    stationarity_error=float(np.abs(np.sum(pi[:,None]*dense,axis=0)).max())
    rows=list(csv.DictReader(path.open()))
    zvalues=[]; comparisons=[]
    for t in [0.1,0.5,1.,2.,4.,8.,12.,24.]:
        chosen=[r for r in rows if float(r['time'])==t]
        N=sum(int(r['n']) for r in chosen)
        k=sum(int(r['origin_infected']) for r in chosen)
        exact=float(uniformized_expectation(Q,spins[:,3],t)[1<<3])
        se=math.sqrt(exact*(1-exact)/N)
        z=(k/N-exact)/se
        zvalues.append(abs(z))
        comparisons.append(dict(time=t,expected=exact,measured=k/N,se=se,z=z))
    previous=next((r for r in old['simulation_checks'] if r['q']==q),None) if old else None
    comparison_error=max(abs(a['expected']-b['expected']) for a,b in zip(comparisons,previous['comparisons'])) if previous else None
    if comparison_error is not None:assert comparison_error<1e-12
    output['simulation_checks'].append(dict(q=q,trajectories=200000,
        row_error=row_error,balance_error=balance_error,stationarity_error=stationarity_error,
        max_abs_z=max(zvalues),comparisons=comparisons,run_stats=process.stderr.strip(),
        max_difference_from_previous_exact_calculation=comparison_error))

for q in [.25,.5,.55,.6,.75,.9]:
    n=9
    Q,pi,spins=generator(n,q)
    for theta in [1.05,1.2,1.8]:
        lam=(theta-1)*(q/theta-(1-q))
        b=q*(theta-1)/theta
        residual=-math.inf
        for x in range(n):
            d=np.array([min([abs(y-x) for y in range(n) if row[y]]+[x+1,n-x]) for row in spins])
            V=theta**d
            residual=max(residual,float(np.max(Q@V+lam*V-b)))
        output['drift_checks'].append(dict(q=q,theta=theta,lam=lam,max_generator_residual=residual))

smoke=subprocess.run([str(ROOT/'simulate_referee'),'.55','1000','981','31','0','10','1',
                      str(ROOT/'data'/'bookkeeping_smoke.csv'),'4'],check=True,capture_output=True,text=True)
output['bookkeeping_smoke']=smoke.stderr.strip()
(ROOT/'data'/'validation.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='drift_checks'},indent=2))
print('Largest drift residual:',max(r['max_generator_residual'] for r in output['drift_checks']))
assert max(r['max_generator_residual'] for r in output['drift_checks'])<1e-10
assert max(r['row_error'] for r in output['simulation_checks'])<1e-12
assert max(r['balance_error'] for r in output['simulation_checks'])<1e-12
assert max(r['stationarity_error'] for r in output['simulation_checks'])<1e-12
