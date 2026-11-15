"""Final independent checks and artifact/resource accounting."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,math,time,resource,hashlib
from pathlib import Path
import numpy as np
from tensor_windows import Moments,phi
from window_search import best_window,window_cost

def scalar_checks():
    rng=np.random.default_rng(2105);worst=0.
    for _ in range(20000):
        C,Q=2.**rng.uniform(-100,10,2);lo=(2*math.sqrt(C)-math.sqrt(Q))**2;hi=(2*math.sqrt(C)+math.sqrt(Q))**2
        P=lo+(hi-lo)*rng.random()
        err=abs(phi(P,Q)-Q*math.log2(1+C/Q))/Q;worst=max(worst,err)
        assert err<=10+1e-10
        F4=5*math.log2(5)-4
        upper=F4*Q+Q*math.log2(1+4*C/Q)
        # This inequality assumes P<=4Q+16C, satisfied by the chosen P.
        assert phi(P,Q)<=upper+1e-10*max(C,Q)
    return dict(trials=20000,largest_scalar_discrepancy=worst)

def main():
    start=time.time();quad=[]
    required=['BRIEF.md','STATUS.md','RESULTS.md','REPORT.md','PROOFS.md','BELIEF.md','LITERATURE.md','LEARNINGS.md','sources.json','tensor_validate.json','tensor_asymptotics.json','unbalanced.json','windows_scan.json','windows_validate.json','linear_audit.json','extra_checks.json','tree_estimates.json']
    assert all(Path(p).is_file() and Path(p).stat().st_size for p in required)
    for L,D in [(9,8),(15,55),(15,181),(23,715)]:
        direct=Moments(L,D).evaluate(0,3);q24=Moments(L,D).evaluate(24,3);q48=Moments(L,D).evaluate(48,3)
        quad.append(dict(L=L,D=D,direct=direct,quadrature24=q24,quadrature48=q48,error24=max(abs(direct[k]-q24[k]) for k in ['L1','L2','L3']),error48=max(abs(direct[k]-q48[k]) for k in ['L1','L2','L3'])))
    scalar=scalar_checks()
    source_checks=[]
    for r in json.load(open('sources.json')):
        actual=hashlib.sha256(Path(r['copy']).read_bytes()).hexdigest();assert actual==r['sha256'];source_checks.append(dict(copy=r['copy'],sha256=actual,match=True))
    sc=json.load(open('windows_scan.json'))
    valid=json.load(open('windows_validate.json'))
    tv=json.load(open('tensor_validate.json'))
    lin=json.load(open('linear_audit.json'))
    ex=json.load(open('extra_checks.json'))
    for r in sc['rows']:
        for z in r['rows']:
            keys=[k for k in ['L1','L2','L3'] if k in z]
            assert z['E']<=z[keys[-1]]+1e-10
            assert all(z[a]>=z[b]-1e-10 for a,b in zip(keys,keys[1:]))
            if 'block' in z:assert z['E']<=z['block']+1e-10
    assert max(r['residual'] for r in tv['rows'])<1e-8
    assert max(r['residual'] for r in valid['rows'])<1e-10
    assert ex['pm']['E_recursion_residual']<1e-12
    metrics=dict(exact_window_cases=len(sc['rows']),exact_window_coordinates=sum(len(r['rows']) for r in sc['rows']),max_truth_table_n=max(r['n'] for r in sc['rows']),brute_permutation_validations=len(valid['rows']),tensor_cases=len(tv['rows']),tensor_max_residual=max(r['residual'] for r in tv['rows']),linear_derivative_checks=sum(r['derivative_checks'] for r in lin['rows']),linear_max_residual=max(r['direct_spectral_residual'] for r in lin['rows']),max_observed_optimized_L2=max((r['minima']['L2'],r['name']) for r in sc['rows'] if 'L2' in r['minima']))
    rss=[]
    for p in Path('.').glob('*.json'):
        v=json.loads(p.read_text())
        if isinstance(v,dict) and 'maxrss_bytes' in v:rss.append(dict(file=str(p),maxrss_bytes=v['maxrss_bytes'],nice=v.get('nice')))
    assert all(x['maxrss_bytes']<3*1024**3 for x in rss)
    assert all(x['nice']>=10 for x in rss)
    files=[p for p in Path('.').rglob('*') if p.is_file()]
    byte_count=sum(p.stat().st_size for p in files)
    assert byte_count<200*1024**2
    out=dict(required_files=required,metrics=metrics,scalar_checks=scalar,quadrature_validation=quad,sources=source_checks,runs=rss,folder_bytes_at_audit=byte_count,seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    json.dump(out,open('audit.json','w'),indent=2);print(json.dumps(out,indent=2))
if __name__=='__main__':main()
