"""New higher-moment and correlated-coin controls for the stationary-law theorem."""
import argparse
import json
import math
import time
import numpy as np
from numpy.polynomial import Polynomial as Poly
from package_result import ROOT,save

def consensus_moments(d,r,c,p):
    # Q=J_d/d makes S=mean(Z) an exact Markov chain with binomial noise.
    f=c*r*r;a=1-r-f;z=Poly([0.,1.]);mu=[1.]
    max_cancel=0.
    for k in range(1,5):
        transition=Poly([0.])
        for b in range(d+1):
            prob=math.comb(d,b)*(z**b)*((1-z)**(d-b))
            transition+=prob*(Poly([f*p+r*b/d,a])**k)
        coeff=list(transition.coef)+[0.]*(k+1-len(transition.coef))
        extra=max((abs(x) for x in coeff[k+1:]),default=0.)
        max_cancel=max(max_cancel,extra)
        assert extra<1e-12
        mu.append(sum(coeff[j]*mu[j] for j in range(k))/(1-coeff[k]))
    return mu,max_cancel

def run(check_only=False):
    start=time.perf_counter();c=1.3;p=.37;records=[];max_cancel=0.
    for d in (2,3,5):
        beta=[]
        for k in range(1,5):
            value=1.
            for j in range(k):value*=(2*c*d*p+j)/(2*c*d+j)
            beta.append(value)
        errors=[]
        for r in (.1,.05,.025,.0125,.00625):
            mu,cancel=consensus_moments(d,r,c,p);max_cancel=max(max_cancel,cancel)
            variance=p*(1-p)/(1+2*c*d-c*c*d*r*r)
            assert abs(mu[1]-p)<1e-9
            assert abs(mu[2]-p*p-variance)<1e-8
            error=max(abs(x-y) for x,y in zip(mu[1:],beta));errors.append(error)
            records.append(dict(d=d,r=r,stationary_moments=mu[1:],limiting_beta_moments=beta,
                                max_moment_error=error,exact_consensus_variance=variance))
        assert errors[-1]<errors[0]/8
    d=3;r=.025
    independent_variance=p*(1-p)/(1+2*c*d-c*c*d*r*r)
    common_coin_variance=p*(1-p)/(1+2*c-c*c*r*r)
    assert abs(common_coin_variance-independent_variance)>.03
    metrics=dict(rank_one_network_moment_cases=len(records),moments_per_case=4,
                 max_cancelled_polynomial_coefficient=max_cancel,records=records,
                 common_coin_control=dict(d=d,r=r,independent_variance=independent_variance,
                                          correlated_variance=common_coin_variance,
                                          absolute_change=abs(common_coin_variance-independent_variance)),
                 scope='Full stationary-law theorem; not functional process convergence.',
                 seconds=round(time.perf_counter()-start,4))
    if check_only:
        print(json.dumps({k:v for k,v in metrics.items() if k!='records'}))
        return metrics
    (ROOT/'measurements/P0087_stationary_law.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
    prior=json.loads((ROOT/'measurements/P0087.json').read_text(encoding='utf-8'))
    prior['stationary_law_checks']=metrics
    prior['scope']='Full stationary beta law, covariance and scalar generator; no functional convergence.'
    save('P0087',prior,record=False)
    row=dict(row_id='w336.P0087.stationary-law',problem_id='P0087',kind='lemma',label='proof',
             claim='Full stationary network law converges to the synchronized beta law under conditional independence.',
             proof_path='proofs/P0087.md',measurement_path='measurements/P0087_stationary_law.json',
             audit_status='pending-w346')
    with (ROOT/'results.jsonl').open('a',encoding='utf-8') as handle:handle.write(json.dumps(row)+'\n')
    with (ROOT/'progress_rows.jsonl').open('a',encoding='utf-8') as handle:
        handle.write(json.dumps(dict(agent='w336',row=row['row_id'],event='P0087: stationary beta-law proof; 15 higher-moment cases and correlated-coin control; audit pending',evidence=str(ROOT/'proofs/P0087.md')))+'\n')
    print(json.dumps({k:v for k,v in metrics.items() if k!='records'}))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check-only',action='store_true',help='Run higher-moment controls without staging or changing status.')
    run(check_only=parser.parse_args().check_only)
