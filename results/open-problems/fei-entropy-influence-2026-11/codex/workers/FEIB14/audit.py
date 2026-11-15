"""Independent direct grouping; no masked Walsh transforms in witness optimization."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import numpy as np,json,time,hashlib,resource,math
from pathlib import Path
from experiments import calc,unpack,KEYS
def hat(f):
    # Explicit character matrix, independent of the C butterfly.
    L=len(f);C=np.array([[(-1)**((s&x).bit_count()) for x in range(L)] for s in range(L)])
    return np.sum(C*np.array(f)[None,:],axis=1)/L
def phi(a,b):
    def e(x):return x*np.log2(np.maximum(x,1e-300))
    return e(a+b)-e(a)-e(b)
def cond(a,b,labels):
    # All candidate partitions evaluated by explicit 0/1 cell membership matrices.
    labels=np.atleast_2d(labels);K=int(labels.max())+1
    z=np.stack([(labels==k).astype(float) for k in range(K)],axis=1)
    A=np.sum(z*a,axis=2);B=np.sum(z*b,axis=2)
    return np.sum(phi(A,B),axis=1)
def partitions(m):
    M=1<<m;t=np.arange(M);pop=np.array([k.bit_count() for k in range(M)])
    parity=np.array([[((s&p).bit_count()&1) for s in range(M)] for p in range(M)])
    meets=np.array([((t&p)!=0).astype(int) for p in range(M)])
    counts=np.array([pop[t&p] for p in range(M)])
    both=(parity[:,None,:]+2*meets[None,:,:]).reshape(-1,M)
    return [parity,meets,both,pop,counts]
PART={n:partitions(n-1) for n in range(1,7)}
def direct(f):
    n=len(f).bit_length()-1;mu=hat(f)**2;I=sum(s.bit_count()*v for s,v in enumerate(mu));H=-sum(v*math.log2(v) for v in mu if v)
    totals=np.zeros(7)
    for i in range(n):
        inds=np.array([s for s in range(1<<n) if not s>>i&1]);a,b=mu[inds],mu[inds|(1<<i)]
        totals[0]+=phi(a,b).sum();costs=[float(cond(a,b,l).min()) for l in PART[n]]
        totals[1:6]+=costs;totals[6]+=min(costs)
    return np.array([I,H,*totals])
def main():
    start=time.time();rng=np.random.default_rng(141429);errors=np.zeros(9);count=0;slack=0;invariance=0
    cases=[]
    for n in range(1,5):
        reps=np.fromfile(f'../FEIB12/npn{n}.bin',dtype='<u4')
        cases += [unpack(hex(int(t)),n) for t in reps]
    for n in [5,6]:
        cases += [rng.choice([-1,1],1<<n).astype(np.int8) for _ in range(64)]
    for r in json.loads(Path('census_extrema.json').read_text())['rows']:cases.append(unpack(r['tt'],r['n']))
    for f in cases:
        o,p=calc(f);d=direct(f);errors=np.maximum(errors,abs(d-np.array([o[k] for k in KEYS])));count+=1
        slack=max(slack,o['Hm']-o['H'],o['Hm']-o['union'],o['countN']-o['parity'],o['countN']-o['size'],o['both']-o['meets'],o['both']-o['parity'])
        if count%31==0:
            n=len(f).bit_length()-1;perm=rng.permutation(n);mask=int(rng.integers(1<<n));idx=np.array([sum(((x>>i)&1)<<int(perm[i]) for i in range(n))^mask for x in range(1<<n)])
            q,_=calc(-f[idx]);invariance=max(invariance,max(abs(q[k]-o[k]) for k in KEYS))
    # Degree support lemma and constant witness on every n<=5 NPN class.
    degree_count=0;degree_margin=0;support_margin=0
    for n in range(1,6):
        reps=np.fromfile(f'../FEIB12/npn{n}.bin',dtype='<u4');L=1<<n;pop=np.array([s.bit_count() for s in range(L)])
        for off in range(0,len(reps),8192):
            t=reps[off:off+8192];f=(1-2*((t[:,None]>>np.arange(L,dtype=np.uint32))&1).astype(float));v=f.copy()
            for h in [1<<i for i in range(n)]:
                z=v.reshape(len(t),-1,2*h);a=z[...,:h].copy();b=z[...,h:].copy();z[...,:h]=a+b;z[...,h:]=a-b
            mu=(v/L)**2;d=np.max((mu>0)*pop,axis=1);I=np.sum(mu*pop,axis=1);Q=np.stack([mu[:,(np.arange(L)&(1<<i))!=0].sum(axis=1) for i in range(n)],axis=1)
            h=-(Q*np.log2(np.maximum(Q,1e-300))+(1-Q)*np.log2(np.maximum(1-Q,1e-300)))
            rho=2.**(1-np.maximum(d,1));C=-(rho*np.log2(rho)+(1-rho)*np.log2(np.maximum(1-rho,1e-300)))/rho
            degree_margin=max(degree_margin,float(np.max(h.sum(axis=1)-C*I)))
            support_margin=max(support_margin,float(np.max(np.where(Q>0,rho[:,None]-Q,0))))
            degree_count+=len(t)
    files={f'npn{n}.bin':dict(source=f'../FEIB12/npn{n}.bin',sha256=hashlib.sha256(Path(f'../FEIB12/npn{n}.bin').read_bytes()).hexdigest(),count=Path(f'../FEIB12/npn{n}.bin').stat().st_size//4) for n in range(1,6)}
    result=dict(direct_cases=count,maximum_absolute_errors=dict(zip(KEYS,map(float,errors))),inequality_violation_bits=slack,NPN_invariance_error_bits=invariance,degree_census_count=degree_count,degree_bound_violation_bits=degree_margin,support_lemma_violation=support_margin,inputs=files,elapsed_seconds=time.time()-start,maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1)
    assert max(errors)<1e-10 and slack<1e-10 and invariance<1e-10 and degree_margin<1e-10 and support_margin<1e-10
    Path('audit.json').write_text(json.dumps(result,indent=2)+'\n');print('AUDIT PASS',json.dumps(result))
if __name__=='__main__':main()
