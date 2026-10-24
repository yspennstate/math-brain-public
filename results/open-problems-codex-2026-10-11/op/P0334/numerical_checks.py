"""Finite stress checks only; not a numerical proof of the CLT. <100MB."""
import numpy as np
from scipy.integrate import quad
import json, pathlib, time

rng=np.random.default_rng(3341012)
# Dense spikes towards both endpoints, with a nonmonotone derivative.
knots=np.unique(np.r_[0.,1., .3,.4,.6,.7,
    [x for k in range(3,15) for x in (2.**-k,1.2*2.**-k,1-1.2*2.**-k,1-2.**-k)]])
mid=(knots[:-1]+knots[1:])/2
slopes=np.full(len(mid),.2)
for k in range(3,15):
    amp=2.**(k/4)/(k+1)
    mask=((mid>2.**-k)&(mid<1.2*2.**-k))|((mid>1-1.2*2.**-k)&(mid<1-2.**-k))
    slopes[mask]=amp
# A flat segment checks atom handling.
slopes[(mid>.3)&(mid<.4)]=0
qvals=np.r_[0.,np.cumsum(slopes*np.diff(knots))]
qm_slopes=np.where((mid>.02)&(mid<.98),.1,0.)
qmvals=np.r_[0.,np.cumsum(qm_slopes*np.diff(knots))]
rvals=qvals-qmvals
hvals=np.r_[0.,np.cumsum(np.abs(slopes-qm_slopes)*np.diff(knots))]

def interp(t,v):return np.interp(t,knots,v)
def integral_error(u,values,p):
    n=len(u)
    edges=np.unique(np.r_[np.arange(n+1)/n,knots])
    left,right=edges[:-1],edges[1:]
    idx=np.minimum((n*(left+right)/2).astype(int),n-1)
    observed=interp(u[idx],values)
    a=observed-interp(left,values);b=observed-interp(right,values)
    slope=(b-a)/(right-left)
    out=np.empty(len(a));zero=np.abs(slope)<1e-13
    out[zero]=(right-left)[zero]*np.abs(a[zero])**p
    nz=~zero
    ant=lambda z:np.sign(z)*np.abs(z)**(p+1)/(p+1)
    out[nz]=(ant(b[nz])-ant(a[nz]))/slope[nz]
    return max(0.,out.sum())

def weighted_derivative(s,p):
    return sum(abs(float(a))**p*quad(lambda t:(t*(1-t))**(p/2),l,r,epsabs=1e-12)[0]
        for a,l,r in zip(s,knots[:-1],knots[1:]))

start=time.monotonic();report={'seed':3341012,'replications':180,'checks':[]}
max_excess=0.
for n in (8,32,128,512):
    for p in (1.5,2.,4.):
        residual=[];envelope=[]
        for _ in range(180):
            u=np.sort(rng.uniform(size=n))
            residual.append(n**(p/2)*integral_error(u,rvals,p))
            envelope.append(n**(p/2)*integral_error(u,hvals,p))
            t=rng.uniform(size=1000);v=u[np.minimum((n*t).astype(int),n-1)]
            excess=np.abs(interp(v,rvals)-interp(t,rvals))-np.abs(interp(v,hvals)-interp(t,hvals))
            max_excess=max(max_excess,float(excess.max()))
        kp=weighted_derivative(slopes-qm_slopes,p)
        report['checks'].append({'n':n,'p':p,'weighted_derivative_integral':kp,
            'mean_scaled_residual_error':float(np.mean(residual)),
            'mean_scaled_envelope_error':float(np.mean(envelope)),
            'published_upper_bound':(5*p)**p*kp,
            'max_integrated_domination_excess':float(np.max(np.array(residual)-envelope))})
report['max_pointwise_domination_excess']=max_excess
report['seconds']=time.monotonic()-start
assert max_excess<1e-10
assert all(x['max_integrated_domination_excess']<1e-9 for x in report['checks'])
pathlib.Path('numerical_results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
