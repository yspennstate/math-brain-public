"""Critical Boltzmann perimeter walks and their marked cyclic boundary.

All native libraries are single-threaded; no finite truncation of the step law.
The only censoring is explicit stopping at the time/space limits.
"""
import os
for var in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[var]='1'
import math, random
from functools import lru_cache

@lru_cache(maxsize=50000)
def h(p):
    if p<=0: return 0.0
    # Central binomial asymptotic has relative error O(p^-4) here.
    if p>10000:
        return 2*math.sqrt(p/math.pi)*(1-1/(8*p)+1/(128*p*p)+5/(1024*p**3))
    return math.exp(math.lgamma(2*p+1)-2*math.lgamma(p+1)-p*math.log(4)+math.log(2*p))

def hdown(p):
    return 1.0 if p==0 else h(p)/(2*p)

def w(m):
    return hdown(m-1)/(2*m)

def nu_negative_pure(m,K):
    return w(m)*(K-1)/(m+K-1)

def sample_K(rng,model):
    if model=='quadrangulation': return 2
    if model=='octangulation': return 4
    beta={'dyadic_beta_080':.8,'dyadic_beta_035':.35}[model]
    t=2**(-beta)
    J=1+int(math.log1p(-rng.random())/math.log(t))
    return 2**J

def step(rng,p,model):
    """Sample the exact Doob kernel, up to ordinary floating-point arithmetic.

    Each component has nu(K-1)=1/h(K),
    nu(-m)=w(m)*(K-1)/(m+K-1), with w a Sibuya(1/2) law.
    Rejection proposal has mass A+1, A=h(p+K-1)/(h(p)h(K)).
    The beta/geometric representation samples Sibuya without tail truncation.
    """
    K=sample_K(rng,model)
    A=h(p+K-1)/(h(p)*h(K))
    while True:
        if rng.random()<A/(1+A): return K-1
        if p==1: continue
        q=rng.betavariate(.5,.5)
        if q<=0: continue
        if q>=1: m=1
        else:
            lu=math.log(max(rng.random(),1e-300))
            lq=math.log1p(-q)
            if lu<=(p-1)*lq: continue  # sampled m >= p, killed
            m=1+int(lu/lq)
        accept=(K-1)/(m+K-1)*h(p-m)/h(p)
        if rng.random()<accept: return -m

def boundary_step(rng,boundary,delta):
    """Uniform adapted peeling, with bitsets on original boundary corners.

    A positive jump inserts 2*delta fresh corners after the peeled edge's
    first endpoint. A negative jump -m removes 2*m edges. The 2*m-1 inner
    corners disappear into the finite hole; the arc endpoints are identified.
    A fair coin chooses which side contains the finite hole.
    """
    n=len(boundary)
    i=rng.randrange(n)
    b=boundary[i:]+boundary[:i]
    if delta>=0:
        return [b[0]]+[0]*(2*delta)+b[1:]
    m=-delta
    if rng.getrandbits(1):
        # Reverse orientation while keeping the same selected edge.
        b=[b[1],b[0]]+list(reversed(b[2:]))
    end=2*m
    return [b[0]|b[end]]+b[end+1:]

def run_path(seed,model,p0=8,max_steps=2000,max_edges=20000):
    rng=random.Random(seed)
    boundary=[1<<j for j in range(2*p0)]
    p=p0; initial_mask=(1<<(2*p0))-1
    root_time=None; all_time=None; max_p=p; macro=0
    for n in range(1,max_steps+1):
        d=step(rng,p,model)
        if d<0 and -d>=3*p/4: macro+=1
        p+=d; max_p=max(max_p,p)
        if 2*p>max_edges:
            return dict(model=model,seed=seed,p0=p0,steps=n-1,root_corner_time=root_time,
                        neighbourhood_time=all_time,censor='edge_cap',max_perimeter=p,macro_drops=macro)
        boundary=boundary_step(rng,boundary,d)
        assert len(boundary)==2*p and p>0
        mask=0
        for label in boundary: mask|=label
        assert mask & ~initial_mask == 0
        if root_time is None and not mask&1: root_time=n
        if mask==0:
            all_time=n
            return dict(model=model,seed=seed,p0=p0,steps=n,root_corner_time=root_time,
                        neighbourhood_time=all_time,censor='',max_perimeter=max_p,macro_drops=macro)
    return dict(model=model,seed=seed,p0=p0,steps=max_steps,root_corner_time=root_time,
                neighbourhood_time=all_time,censor='time_cap',max_perimeter=max_p,macro_drops=macro)
