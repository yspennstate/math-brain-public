"""Equation (10), derived afresh using truncated unit increments.
The original Lebesgue integral is integrated against Gaussian endpoints.
Unit increments are conditioned to exceed -h; their probability Phi(h)^(m+1)
is restored explicitly. Conditional Brownian noncollision probabilities are
computed by two Gaussian determinant ratios. No claim code is used.
"""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1', MKL_NUM_THREADS='1')
import math,csv,time,resource
import numpy as np
from scipy.special import ndtr, ndtri, erf
from scipy.stats import qmc
from scipy.integrate import quad

def noncollision(x,y,t):
    # Monge dual scaling: all matrix entries <=1, diagonal entries=1.
    # Row and column scale factors cancel against the diagonal Gaussian density.
    v=np.zeros_like(y)
    v[:,1:]=np.cumsum(.5*(x[:,:-1]+x[:,1:])*np.diff(y,axis=1),axis=1)
    logs=(x[:,:,None]*(y[:,None,:]-y[:,:,None])-(v[:,None,:]-v[:,:,None]))/t[:,None,None]
    assert float(np.max(logs))<1e-6
    k=np.exp(np.minimum(logs,0.))
    val=np.linalg.det(k)
    assert np.min(val)>-1e-9 and np.max(val)<1+1e-7
    return np.maximum(val,0.)

def slab(h,m,power,seed):
    u=qmc.Sobol(2*m+4,scramble=True,seed=seed).random_base2(power)
    u+=2.**-31  # midpoint of each 30-bit Sobol cell; excludes exact theta=0
    theta=u[:,0]; count=len(u)
    # U_i is the complete unit Brownian increment, i=0,...,m.
    unit=ndtri(ndtr(-h)+ndtr(h)*u[:,1:m+2])
    mid=ndtri(u[:,m+2:])
    b=np.column_stack([np.zeros(count),np.cumsum(unit,axis=1)])
    x=b+h*np.arange(m+2)
    y=np.empty_like(x)
    y[:,:-1]=x[:,:-1]+theta[:,None]*unit+np.sqrt(theta*(1-theta))[:,None]*mid[:,:-1]
    y[:,-1]=x[:,-1]+np.sqrt(theta)*mid[:,-1]
    good=np.all(np.diff(y,axis=1)>0,axis=1)
    total=0.; indices=np.flatnonzero(good)
    for start in range(0,len(indices),1024):
        z=indices[start:start+1024]
        first=noncollision(x[z],y[z],theta[z])
        second=noncollision(y[z,:-1],x[z,1:]-h,1-theta[z])
        total+=float(np.sum(first*second))
    return ndtr(h)**(m+1)*total/count

def first_slab(h):
    # For t<=1, conditional on its endpoints Z is a variance-2 bridge.
    # v=(Z0+Zt)/2 and d=(Zt-Z0)/2 are independent normals.
    def survival(t):
        def integrand(v):
            gap=(h-v)/math.sqrt(t)
            return math.exp(-v*v/(2-t))/math.sqrt(math.pi*(2-t))*(erf(gap)-2*gap/math.sqrt(math.pi)*math.exp(-gap*gap))
        return quad(integrand,-np.inf,h,epsabs=2e-10)[0]
    return quad(survival,0,1,epsabs=2e-9)[0]

def r(h):
    ph=math.exp(-h*h/2)/math.sqrt(2*math.pi); q=ndtr(h)
    return q*q-h*ph*q-ph*ph

def tail(h,m):
    q=r(h)
    return q**(m//2)*(1+q)/(1-q) if m%2==0 else 2*q**((m+1)//2)/(1-q)

def main():
    print('nice',os.getpriority(os.PRIO_PROCESS,0),flush=True)
    power=15; scrambles=8
    with open('data/independent_slabs.csv','w') as f,open('data/independent_constants.csv','w') as g:
        w=csv.writer(f); w.writerow(['alpha','m','estimate','scramble_se','samples_per_scramble','scrambles'])
        v=csv.writer(g); v.writerow(['alpha','slabs','estimate','scramble_se','tail_bound','first_slab_reference','first_slab_estimate'])
        for alpha,M in [(0.,12),(.5,18),(1.,28)]:
            sums=np.zeros(scrambles); first=None; start=time.monotonic()
            ref=first_slab(alpha)+first_slab(-alpha)
            for m in range(M):
                arr=np.array([slab(alpha,m,power,843211+10000*m+rep)+(slab(-alpha,m,power,986421+10000*m+rep) if alpha else slab(alpha,m,power,986421+10000*m+rep)) for rep in range(scrambles)])
                sums+=arr
                if m==0: first=float(arr.mean())
                w.writerow([alpha,m,arr.mean(),arr.std(ddof=1)/math.sqrt(scrambles),2**power,scrambles]); f.flush()
                if m in (0,3,7,M-1): print(alpha,m,arr.mean(),'sum',1+sums.mean(),'seconds',round(time.monotonic()-start,1),flush=True)
            result=[alpha,M,1+sums.mean(),sums.std(ddof=1)/math.sqrt(scrambles),tail(alpha,M)+tail(-alpha,M),ref,first]
            v.writerow(result); g.flush(); print('RESULT',result,flush=True)
    print('peak_rss',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
if __name__=='__main__':main()
