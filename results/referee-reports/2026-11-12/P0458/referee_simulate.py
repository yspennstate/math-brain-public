"""Root-degree simulation independent of the authors' programs.

Conditional on the root cutoff X, its k preferred scores are iid U(0,X).
Retain those above a deterministic lower threshold. For retained vertices,
generate every shared edge and a separate binomial for all external edges.
The retained rejections have their EXACT joint law. The probability of an
omitted rejection is <=(n-1)*a*P(Bin(n-2,a)>=k).

For fixed r use Y=n(1-U) and retain Y<=B=80. The omitted-rejection
probability is <=(n-1)/n * integral_B^n P(Bin(n-2,y/n)<r)dy.
We compute a rigorous exponential/polynomial upper bound for this tail.
"""
import argparse
import ctypes as ct
import json
import math
import time
import numpy as np
from scipy import integrate, optimize, special, stats

lib=ct.CDLL('./referee_pairs.so')
lib.shared_counts.argtypes=[ct.c_size_t,ct.POINTER(ct.c_double),ct.POINTER(ct.c_int64),ct.POINTER(ct.c_uint64)]

def shared(u,c,state):
    lib.shared_counts(len(u),u.ctypes.data_as(ct.POINTER(ct.c_double)),
                      c.ctypes.data_as(ct.POINTER(ct.c_int64)),ct.byref(state))

def interior(n,k,reps,rng,state):
    s=math.sqrt(k*(n-k)/n)
    a=max(0.,k/n-8*s/n)
    bound=(n-1)*a*stats.binom.sf(k-1,n-2,a)
    h=np.empty(reps,dtype=np.int64)
    for t in range(reps):
        x=rng.beta(k+1,n-k-1)
        m=rng.binomial(k,max(0.,(x-a)/x))
        u=rng.uniform(a,x,m) if m else np.empty(0)
        c=rng.binomial(n-1-m,u).astype(np.int64)
        shared(u,c,state)
        h[t]=np.count_nonzero(c>=k)
    return h,float(bound)

def fixed_r(n,r,reps,rng,state):
    b=80.
    q=b/n
    h=np.empty(reps,dtype=np.int64)
    for t in range(reps):
        m=rng.binomial(n-1,q)
        y=rng.uniform(0.,q,m)
        if m<=r:
            h[t]=0
            continue
        cutoff=np.partition(y,r-1)[r-1]
        c=rng.binomial(n-1-m,y).astype(np.int64)
        shared(y,c,state)
        h[t]=np.count_nonzero((y>cutoff)&(c<r))
    # For i<r, Bin(n-2,y/n) mass <= y^i/i! exp(-c*y)
    # with c=(n-r-1)/n, valid on 0<=y<=n.
    c=(n-r-1)/n
    bound=(n-1)/n*sum(special.gammaincc(i+1,c*b)/c**(i+1) for i in range(r))
    return h,float(bound)

def limit_cdf_cont(y):
    if y<=0: return 0.
    def g(z): return math.exp(-z*z/2)/math.sqrt(2*math.pi)+z*special.ndtr(z)
    z=optimize.brentq(lambda z:g(z)-y,-40,max(40,y+1))
    return float(special.ndtr(z))

def limit_cdf_fixed(h,r):
    def integrand(a):
        lam=math.exp(-a)*sum((r-l)*a**l/math.factorial(l) for l in range(r))
        return stats.poisson.cdf(h,lam)*math.exp(-a)*a**(r-1)/math.factorial(r-1)
    return integrate.quad(integrand,0,160,epsabs=2e-12,epsrel=2e-12)[0]

def summarize(h,n,k,r,bound,exact):
    count=len(h)
    mean=float(np.mean(h)); var=float(np.var(h,ddof=1))
    m4=float(np.mean((h-mean)**4))
    sem=math.sqrt(var/count); sev=math.sqrt(max(0.,m4-var*var)/count)
    values,counts=np.unique(h,return_counts=True)
    empirical=np.cumsum(counts)/count
    if r:
        mu=r*math.comb(2*r,r)/4**r
        m2=sum((r-l)*(r-j)*math.factorial(r-1+l+j)/(math.factorial(r-1)*math.factorial(l)*math.factorial(j)*3**(r+l+j)) for l in range(r) for j in range(r))
        targetvar=mu+m2-mu*mu
        maxh=int(values[-1])
        lf=np.array([limit_cdf_fixed(i,r) for i in range(maxh+1)])
        ef=np.array([np.mean(h<=i) for i in range(maxh+1)])
        ks=float(np.max(abs(lf-ef)))
        normalized=(mean,var,sem,sev)
    else:
        mu=1/math.sqrt(math.pi)
        targetvar=1/3+(math.sqrt(3)-2)/(2*math.pi)
        s=math.sqrt(k*(n-k)/n)
        lf=np.array([limit_cdf_cont(i/s) for i in values])
        ks=float(max(np.max(abs(empirical-lf)),np.max(abs(empirical-counts/count-lf))))
        normalized=(mean/s,var/(s*s),sem/s,sev/(s*s))
    ex=exact[f'{n},{k}']
    zmean=(mean-ex['eh'])/sem
    zvar=(var-ex['var'])/sev
    result=dict(n=n,k=k,r=r,reps=count,mean=mean,var=var,se_mean=sem,se_var=sev,
                norm_mean=normalized[0],norm_var=normalized[1],norm_se_mean=normalized[2],norm_se_var=normalized[3],
                limit_mean=mu,limit_var=targetvar,ks=ks,omission_bound=bound,zmean=zmean,zvar=zvar)
    print(json.dumps(result),flush=True)
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--n',type=int,required=True)
    ap.add_argument('--reps',type=int,default=12000)
    ap.add_argument('--fixed-reps',type=int,default=80000)
    ap.add_argument('--seed',type=int,default=20261112)
    args=ap.parse_args()
    rng=np.random.default_rng(args.seed+args.n)
    state=ct.c_uint64(args.seed+31*args.n)
    exact=json.load(open('referee_numeric.json'))
    start=time.monotonic()
    rows=[]; saved={}
    for k in (args.n//4,args.n//2,math.isqrt(args.n)):
        h,bound=interior(args.n,k,args.reps,rng,state)
        rows.append(summarize(h,args.n,k,0,bound,exact))
        saved[f'k{k}']=h
        if time.monotonic()-start>230:
            raise RuntimeError('time budget reached; lower reps')
    for r in (1,2,5):
        h,bound=fixed_r(args.n,r,args.fixed_reps,rng,state)
        rows.append(summarize(h,args.n,args.n-1-r,r,bound,exact))
        saved[f'r{r}']=h
        if time.monotonic()-start>270:
            raise RuntimeError('time budget reached; lower reps')
    json.dump(rows,open(f'referee_sim_{args.n}.json','w'),indent=2)
    np.savez_compressed(f'referee_samples_{args.n}.npz',**saved)
    print(f'elapsed_seconds={time.monotonic()-start:.3f}',flush=True)

if __name__=='__main__': main()
