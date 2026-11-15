"""Small Gaussian BRW experiment; unconditional shifted-Gumbel comparison only."""
import os
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'mplconfig')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'cache')
import json, csv, math, time, resource
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.special import gamma
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# The launcher already runs at nice >=10; inspect without attempting to raise priority.
try: priority=os.getpriority(os.PRIO_PROCESS,0)
except (AttributeError,OSError): priority=None
if priority is not None and priority < 10:
    os.setpriority(os.PRIO_PROCESS,0,10)
    priority=os.getpriority(os.PRIO_PROCESS,0)
soft,hard=resource.getrlimit(resource.RLIMIT_AS)
cap=min(3*1024**3,hard) if hard != resource.RLIM_INFINITY else 3*1024**3
try:
    resource.setrlimit(resource.RLIMIT_AS,(cap,hard))
    as_limit_applied=True
except (ValueError,OSError):
    as_limit_applied=False  # macOS may reject RLIMIT_AS; bounded arrays and RSS guard below.
seed=650013; trials=1024; batch=16
rng=np.random.default_rng(seed)
rows=[]; summaries=[]; start=time.monotonic()
fig,axes=plt.subplots(1,2,figsize=(10,4),constrained_layout=True)
for d,ax in zip((1,2),axes):
    b=2**d; alpha=math.sqrt(2*d); snaps=[10,12,14,16] if d==1 else [5,6,7,8]
    results={n:[] for n in snaps}
    for offset in range(0,trials,batch):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 3*1024**3:
            raise MemoryError("RSS exceeded 3 GB guard")
        field=np.zeros((batch,1))
        for n in range(1,max(snaps)+1):
            field=np.repeat(field,b,axis=1)+rng.normal(0,math.sqrt(math.log(2)),(batch,b**n))
            if n in snaps:
                t=n*math.log(2)
                maximum=field.max(axis=1)-alpha*t+1.5/alpha*math.log(t)
                weights=np.exp(alpha*field-2*d*t)
                D=((alpha*t-field)*weights).sum(axis=1)
                Z=math.sqrt(math.pi*t/2)*weights.sum(axis=1)
                results[n].extend(zip(maximum.tolist(),D.tolist(),Z.tolist()))
    for n in snaps:
        arr=np.array(results[n]); maxima,D,Z=arr.T
        # Independent samples for mass mixture, median calibration, and validation.
        masses=Z[:256]; cal=maxima[256:640]; test=np.sort(maxima[640:])
        median=float(np.median(cal))
        def cdf(x,C):
            return np.exp(-C*masses[:,None]*np.exp(-alpha*np.atleast_1d(x))[None,:]).mean(axis=0)
        C=math.exp(brentq(lambda u: float(cdf(median,math.exp(u))[0])-.5,-20,20))
        pred=cdf(test,C)
        j=np.arange(1,len(test)+1)
        ks=float(max(np.max(j/len(test)-pred),np.max(pred-(j-1)/len(test))))
        Cplain=math.log(2)*math.exp(alpha*median)
        plain=np.exp(-Cplain*np.exp(-alpha*test))
        ksplain=float(max(np.max(j/len(test)-plain),np.max(plain-(j-1)/len(test))))
        summary=dict(d=d,b=b,n=n,t=n*math.log(2),trials=trials,C_SH_proxy=C,validation_KS=ks,plain_gumbel_KS=ksplain,median=float(np.median(maxima)),mean=float(maxima.mean()),standard_deviation=float(maxima.std(ddof=1)),negative_D_count=int((D<=0).sum()),SH_proxy_median=float(np.median(Z)),D_median=float(np.median(D)),validation_sample=len(test),mass_sample=256,calibration_sample=384)
        summaries.append(summary)
        for i,(m,dm,z) in enumerate(arr):rows.append([d,n,i,m,dm,z])
        if n==max(snaps):
            grid=np.linspace(float(np.quantile(maxima,.005))-1,float(np.quantile(maxima,.995))+1,300)
            ax.step(test,np.arange(1,len(test)+1)/len(test),where='post',label='Held-out BRW maximum')
            ax.plot(grid,cdf(grid,C),label='SH mass + max Gumbel')
            ax.plot(grid,np.exp(-Cplain*np.exp(-alpha*grid)),ls='--',label='Plain max Gumbel')
            ax.set(title=f'd = {d}, b = {b}, depth = {n}',xlabel='Centered maximum',ylabel='CDF')
            ax.legend(fontsize=8)
# Check the Gamma/sign/constant identity independently by quadrature at M=2, c=3.
checks=[]
for d in (1,2):
    alpha=math.sqrt(2*d)
    for q in (.5,1.,2.):
        s=q/alpha; c=3.; mass=2.
        integ,err=quad(lambda e:e**s*math.exp(-e),0,np.inf,epsabs=1e-11)
        via_integral=c**(-q)*mass**(-s)*integ
        via_gamma=c**(-q)*mass**(-s)*gamma(1+s)
        checks.append(dict(d=d,q=q,quadrature=via_integral,gamma_formula=float(via_gamma),absolute_error=float(abs(via_integral-via_gamma)),quadrature_error=err))
with (ROOT/'data'/'brw_samples.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['d','depth','trial','centered_max','signed_derivative_mass','seneta_heyde_mass_proxy']);w.writerows(rows)
meta=dict(seed=seed,trials=trials,batch=batch,nice=priority,threads=1,address_space_limit_bytes=cap,address_space_limit_applied=as_limit_applied,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,elapsed_seconds=time.monotonic()-start,summaries=summaries,identity_checks=checks,limitations='SH proxy is finite-depth, C is fitted on separate calibration samples; tree geometry, not Euclidean star-scale simulation. No asymptotic theorem tested. No clipping of signed derivative masses; SH proxy used throughout. CDF agreement is unconditional, not a same-tree independent residual claim.')
(ROOT/'data'/'simulation_summary.json').write_text(json.dumps(meta,indent=2)+'\n')
fig.savefig(ROOT/'data'/'brw_cdf.svg')
print(json.dumps(meta,indent=2))
