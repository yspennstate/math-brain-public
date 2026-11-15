"""Full graph Monte Carlo and independent simulation of complementary budgets."""
import ctypes as ct
import math
import time
import numpy as np
from referee_exact import moments
from referee_simulate import interior

def full_graph(n,reps,budgets,rng):
    a,b=np.triu_indices(n,1)
    result=np.zeros((len(budgets),reps),dtype=np.int64)
    for t in range(reps):
        u=np.ones((n,n))
        u[a,b]=rng.random(len(a))
        u[b,a]=u[a,b]
        for i,k in enumerate(budgets):
            threshold=np.partition(u,k-1,axis=1)[:,k-1]
            result[i,t]=k-np.count_nonzero((u[0]<=threshold[0])&(u[:,0]<=threshold))
    return result

def show(label,h,mean,var):
    sem=math.sqrt(float(np.var(h))/len(h))
    m4=float(np.mean((h-h.mean())**4))
    sev=math.sqrt(max(0.,m4-float(np.var(h))**2)/len(h))
    print(f'{label} N={len(h)} EH={h.mean():.8f} +/- {sem:.8f} VH={h.var(ddof=1):.8f} +/- {sev:.8f} exact=({mean:.8f},{var:.8f}) z=({(h.mean()-mean)/sem:.3f},{(h.var(ddof=1)-var)/sev:.3f})',flush=True)

def main():
    start=time.monotonic()
    rng=np.random.default_rng(193817)
    state=ct.c_uint64(981817)
    full=full_graph(12,100000,(4,8),rng)
    for j,k in enumerate((4,8)):
        eh,v=moments(12,k)
        show(f'full graph n=12 k={k}',full[j],float(eh),float(v))
        h,bound=interior(12,k,100000,rng,state)
        show(f'root sampler n=12 k={k} omitted<={bound}',h,float(eh),float(v))
    # A truly full n=1000 graph, to cross-check the root sampler at scale.
    full=full_graph(1000,400,(250,749),rng)
    for j,k in enumerate((250,749)):
        print(f'full graph n=1000 k={k} N=400 EH={full[j].mean():.6f} VH={full[j].var(ddof=1):.6f}',flush=True)
    hs=[]
    for k in (250,749):
        h,bound=interior(1000,k,60000,rng,state)
        hs.append(h)
        print(f'complement simulation n=1000 k={k} N={len(h)} EH={h.mean():.8f} VH={h.var(ddof=1):.8f} omission<={bound:.3g}',flush=True)
    difference=float(hs[0].mean()-hs[1].mean())
    se=math.sqrt(sum(float(h.var(ddof=1))/len(h) for h in hs))
    print(f'complement means difference={difference:.8f} SE={se:.8f} z={difference/se:.4f}')
    print(f'elapsed_seconds={time.monotonic()-start:.3f}')

if __name__=='__main__': main()
