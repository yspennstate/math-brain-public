#!/usr/bin/env python3
"""Reproduce tables; distinguish finite-horizon observations from true renewals."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:
    os.setpriority(os.PRIO_PROCESS,0,10)
import csv, json, math
from pathlib import Path
import numpy as np
from scipy.special import gammaln
from scipy.stats import beta

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'
MODELS={
 'd2_moderate':[.55,.5,.5,.5],
 'd3_moderate':[.55,.5,.5,.5,.5,.5],
 'd2_trapping':[.10,.08,.08,.08],
 'd3_trapping':[.07,.05,.05,.05,.05,.05],
}
def cp(k,n,tail=.025):
    return (0. if k==0 else float(beta.ppf(tail,k,n-k+1)),
            1. if k==n else float(beta.ppf(1-tail,k+1,n-k)))

def geometry(rng):
    rows=[]
    for d in (2,3):
        for S in (.5,1.,2.,4.,10.):
            a=rng.dirichlet(np.ones(2*d),size=200000)*S
            omitted=np.sum(np.abs(a[:,:d]-a[:,d:]),axis=1)<=1
            x=min(1.,1/S)
            exact=3*x*x-2*x**3 if d==2 else 10*x**3-15*x**4+6*x**5
            empirical=float(omitted.mean())
            rows.append({'d':d,'S':S,'n':len(a),'exact':exact,'empirical':empirical,
                         'z_error':(empirical-exact)/math.sqrt(max(exact*(1-exact)/len(a),1e-30))})
    return rows

def explicit_constants():
    # Example outside (6.1), fixed a=.25 and all transverse weights .1.
    result=[]
    for d in (2,3):
        a=.25; others=[a]+[.1]*(2*d-2); Sstar=1+sum(others)
        r=.05
        logeta=max(gammaln(Sstar)+gammaln(z-r)-gammaln(Sstar-r)-gammaln(z) for z in others)
        exponent=121*d**4+3001*d*(1+logeta/r)**2
        logC=exponent*math.log(3)
        p=a/Sstar; M=15*d+6
        # C dwarfs other lower bounds; L=ceil(C), reported through logarithms.
        assert logC>math.log((M+1)/p**2)
        log10_L_lower=logC/math.log(10)
        # Using L=ceil(C)<=2C: this smaller b is a completely explicit example.
        log10_b=math.log10(a/4)-(M+1)*(log10_L_lower+math.log10(2))
        result.append({'d':d,'a':a,'transverse_each':.1,'r':r,'M':M,'p':p,
                       'log_eta':float(logeta),'log10_C':log10_L_lower,
                       'log10_example_b':log10_b,
                       'kappa_at_b_zero':2*sum(others)-max(a,.2)})
    return result

def main():
    rng=np.random.default_rng(20261113137)
    slab=list(csv.DictReader((DATA/'slab_counts.csv').open()))
    table=[]; fits=[]
    for row in slab:
        n=int(row['replicates']); b=int(row['back']); c=int(row['censored'])
        # Bonferroni: one-sided 97.5% endpoint coverage gives joint >=95%.
        lower=0. if b==0 else float(beta.ppf(.025,b,n-b+1))
        upper=1. if b+c==n else float(beta.ppf(.975,b+c+1,n-b-c))
        table.append({**row,'p_back_by_cap':b/n,'p_not_front_by_cap':(b+c)/n,
                      'q95_lower':lower,'q95_upper':upper})
    with (DATA/'slab_intervals.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=table[0]);w.writeheader();w.writerows(table)
    for name in MODELS:
        rows=[x for x in table if x['model']==name and int(x['censored'])==0 and int(x['back'])>0]
        if len(rows)<3:continue
        L=np.array([int(x['L']) for x in rows]); y=-np.log([float(x['p_back_by_cap']) for x in rows])
        for gamma in (.5,.75,1.):
            A=np.column_stack((np.ones(len(L)),L**gamma))
            co=np.linalg.lstsq(A,y,rcond=None)[0]
            fits.append({'model':name,'gamma':gamma,'intercept':float(co[0]),'slope':float(co[1]),
                         'rms_residual':float(np.sqrt(np.mean((A@co-y)**2))),
                         'warning':'descriptive small-scale fit, not an asymptotic gamma estimate'})
    proxies=list(csv.DictReader((DATA/'renewal_proxies.csv').open()))
    tail=[]
    for name in MODELS:
        for H in (10000,30000,100000):
            vals=[int(x['tau_proxy']) for x in proxies if x['model']==name and int(x['horizon'])==H]
            for t in (10,100,1000,10000,30000):
                if t>=H:continue
                k=sum(x>t for x in vals); lo,hi=cp(k,len(vals))
                tail.append({'model':name,'horizon':H,'t':t,'n':len(vals),'proxy_survivors':k,
                             'proxy_tail':k/len(vals),'proxy95_lower':lo,'proxy95_upper':hi,
                             'true_tail95_lower':lo,
                             'true_tail_upper':'unknown'})
    with (DATA/'renewal_tail_lower_bounds.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=tail[0]);w.writeheader();w.writerows(tail)
    # Horizon monotonicity of the proxy is a mathematical invariant.
    byrep={}
    for x in proxies:byrep.setdefault((x['model'],x['replicate']),[]).append((int(x['horizon']),int(x['tau_proxy'])))
    for key,vals in byrep.items():
        vals.sort();assert all(vals[i][1]<=vals[i+1][1] for i in range(len(vals)-1)),key
    sampler=list(csv.DictReader((DATA/'sampler_check.csv').open())); maxz=0
    for x in sampler:
        a=MODELS[x['model']];S=sum(a);p=float(x['theoretical_mean']);n=int(x['n'])
        sd=math.sqrt(p*(1-p)/(S+1)/n)
        maxz=max(maxz,abs(float(x['empirical_mean'])-p)/sd)
    trap=[]
    for name,a in MODELS.items():
        d=len(a)//2;S=sum(a);i=int(np.argmax(np.array(a[:d])+np.array(a[d:])))
        kappa=2*S-a[i]-a[i+d]
        n=200000
        # Exit probabilities are sampled directly, avoiding cancellation in 1-p*q.
        u=rng.beta(S-a[i],a[i],n);v=rng.beta(S-a[i+d],a[i+d],n)
        with np.errstate(divide='ignore',invalid='ignore'):
            neglogpq=-np.log1p(-u)-np.log1p(-v)
            rounds=np.floor(rng.exponential(size=n)/neglogpq)
        assert not np.isnan(rounds).any()
        for cycles in (1,10,100,1000,10000,100000):
            k=int(np.sum(rounds>=cycles))
            logexact=(gammaln(a[i]+cycles)-gammaln(a[i]) + gammaln(a[i+d]+cycles)-gammaln(a[i+d])
                      +2*gammaln(S)-2*gammaln(S+cycles))
            exact=float(np.exp(logexact));lo,hi=cp(k,n)
            trap.append({'model':name,'cycles':cycles,'kappa':kappa,'n':n,'survivors':k,
                         'empirical':k/n,'exact':exact,'ci_lower':lo,'ci_upper':hi})
    with (DATA/'pair_trap_tail.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=trap[0]);w.writeheader();w.writerows(trap)
    output={'models':{name:{'alpha':a,'S':sum(a),'drift':[a[i]-a[i+len(a)//2] for i in range(len(a)//2)],
                          'kappa':2*sum(a)-max(a[i]+a[i+len(a)//2] for i in range(len(a)//2))}
                       for name,a in MODELS.items()},
            'fits':fits,'geometry_checks':geometry(rng),'explicit_constants':explicit_constants(),
            'checks':{'proxy_horizon_monotonicity':True,'sampler_largest_abs_z':maxz,
                      'all_slab_counts_sum':all(int(r['back'])+int(r['front'])+int(r['censored'])==int(r['replicates']) for r in slab)}}
    (DATA/'analysis.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
