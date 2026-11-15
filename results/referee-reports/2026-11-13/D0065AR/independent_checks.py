"""Referee calculations, written independently of the submitted code."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
import csv, json, math, resource
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

out = Path('data'); out.mkdir(exist_ok=True)
records = list(csv.DictReader(open('claim_files/data/brw_samples.csv')))
submitted = json.loads(Path('claim_files/data/simulation_summary.json').read_text())
results = {'nice': os.getpriority(os.PRIO_PROCESS,0), 'csv_records':len(records), 'groups':[]}

def ks(values, cdf):
    y=np.sort(values); f=cdf(y); n=len(y)
    return float(max(np.max(np.arange(1,n+1)/n-f),np.max(f-np.arange(n)/n)))

for s in submitted['summaries']:
    d,n=s['d'],s['n']; alpha=math.sqrt(2*d)
    group=sorted([r for r in records if int(r['d'])==d and int(r['depth'])==n],key=lambda r:int(r['trial']))
    assert [int(r['trial']) for r in group]==list(range(1024))
    maxima=np.array([float(r['centered_max']) for r in group])
    masses=np.array([float(r['seneta_heyde_mass_proxy']) for r in group[:256]])
    median=float(np.median(maxima[256:640]))
    C=math.exp(brentq(lambda z:float(np.mean(np.exp(-math.exp(z)*masses*np.exp(-alpha*median))))-.5,-20,20))
    mix=lambda x:np.exp(-C*np.exp(-alpha*x[:,None])*masses).mean(axis=1)
    plain_location=median+math.log(math.log(2))/alpha
    plain=lambda x:np.exp(-np.exp(-alpha*(x-plain_location)))
    derived={'C_SH_proxy':C,'validation_KS':ks(maxima[640:],mix), 'plain_gumbel_KS':ks(maxima[640:],plain),
             'median':float(np.median(maxima)), 'mean':float(np.mean(maxima)),
             'standard_deviation':float(np.std(maxima,ddof=1)),
             'negative_D_count':sum(float(r['signed_derivative_mass'])<=0 for r in group),
             'SH_proxy_median':float(np.median([float(r['seneta_heyde_mass_proxy']) for r in group])),
             'D_median':float(np.median([float(r['signed_derivative_mass']) for r in group]))}
    errors={k:abs(v-s[k]) for k,v in derived.items()}
    assert max(errors.values())<1e-10, errors
    results['groups'].append(dict(d=d,depth=n,computed=derived,max_error=max(errors.values())))

# Independent gamma integral in exponential coordinates, rather than integrating the Gumbel density.
results['gamma']=[]
for d in [1,2,3]:
    alpha=math.sqrt(2*d)
    for q in [.5,1,2]:
        s=q/alpha
        value,error=quad(lambda u:u**s*math.exp(-u),0,np.inf,epsabs=2e-12,epsrel=2e-12)
        integral=value*3**(-q)*2**(-s)
        formula=3**(-q)*math.gamma(1+s)*2**(-s)
        assert abs(integral-formula)<2e-11
        results['gamma'].append(dict(d=d,q=q,integral=integral,formula=formula,error=abs(integral-formula)))

# Direct maximum/centering formula versus its expansion, for arbitrary maxima.
results['perturbation']=[]
for d in [1,2,3,10]:
    alpha=math.sqrt(2*d); b=3/(2*alpha); delta=.7
    for n in [2,10,100,10000]:
        scale=1+delta/n; variance=scale**2*n; U=.37
        maximum=alpha*n-b*math.log(n)+U
        direct=scale*maximum-alpha*variance+b*math.log(variance)
        expanded=scale*U+alpha*n*(scale-scale**2)+b*((1-scale)*math.log(n)+2*math.log(scale))
        assert abs(direct-expanded)<1e-10
        results['perturbation'].append(dict(d=d,n=n,exact_shift=direct-U,limit_shift=-alpha*delta,algebra_error=abs(direct-expanded)))

# A fresh small BRW run checks the normalizations and the perturbation on actual maxima.
# It is a hierarchical illustration, never evidence that a Euclidean supremum was simulated.
rng=np.random.default_rng(130650)
results['fresh_brw']=[]
for d,depth in [(1,12),(2,6)]:
    alpha=math.sqrt(2*d); t=depth*math.log(2); vals=[]; deriv=[]; proxy=[]
    for trial in range(256):
        leaves=np.zeros(1)
        for _ in range(depth):
            leaves=np.repeat(leaves,2**d)+rng.normal(0,math.sqrt(math.log(2)),len(leaves)*2**d)
        weights=np.exp(alpha*leaves-2*d*t)
        vals.append(float(leaves.max()-alpha*t+3/(2*alpha)*math.log(t)))
        deriv.append(float(np.sum((alpha*t-leaves)*weights)))
        proxy.append(float(math.sqrt(math.pi*t/2)*weights.sum()))
    results['fresh_brw'].append(dict(d=d,depth=depth,trials=256,median=float(np.median(vals)),nonpositive_derivative=sum(z<=0 for z in deriv),positive_sh=all(z>0 for z in proxy)))

results['dkw_384_95']=math.sqrt(math.log(40)/(2*384))
results['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert results['peak_rss_bytes']<4_000_000_000
(out/'independent_checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(dict(records=len(records),groups=len(results['groups']),max_summary_error=max(x['max_error'] for x in results['groups']),max_gamma_error=max(x['error'] for x in results['gamma']),nice=results['nice'],peak_rss_bytes=results['peak_rss_bytes'],fresh_brw=results['fresh_brw']),indent=2))
