import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import json,math,time,resource
from pathlib import Path
import numpy as np
from experiments import signs,hex_tt
def fw(f):
    a=np.array(f,dtype=float);L=len(a)
    for i in range(L.bit_length()-1):
        h=1<<i;b=a.reshape(-1,2*h);p=b[:,:h].copy();q=b[:,h:].copy();b[:,:h]=p+q;b[:,h:]=p-q
    return a/L
def ph(a,b):
    def ell(x):return x*np.log2(np.maximum(x,1e-300))
    return ell(a+b)-ell(a)-ell(b)
def erasures(mu,n):
    return np.array([np.sum(ph(mu[[t for t in range(1<<n) if not t>>i&1]],mu[[t|(1<<i) for t in range(1<<n) if not t>>i&1]])) for i in range(n)])
def conditional(mu,i,blocks):
    n=len(mu).bit_length()-1;groups={}
    for t in range(1<<n):
        if t>>i&1:continue
        label=tuple(bool(t&b) for b in blocks);a,b=groups.get(label,(0.,0.));groups[label]=(a+mu[t],b+mu[t|(1<<i)])
    return sum(ph(a,b) for a,b in groups.values())
def main():
    start=time.time();rng=np.random.default_rng(141430);maxcoeff=maxE=maxI=maxpath=0.;cases=0;records=[]
    for trial in range(384):
        m=int(rng.integers(2,5));sizes=rng.integers(1,4,m);n=int(sum(sizes))
        if n>10:continue
        children=[]
        for k in sizes:
            while True:
                c=rng.choice([-1,1],1<<int(k)).astype(np.int8)
                if abs(c.mean())<1:break
            children.append(c)
        g=rng.choice([-1,1],1<<m).astype(np.int8);eta=np.array([c.mean() for c in children]);v=1-eta**2;Y=signs(m)
        prob=np.prod((1+Y*eta)/2,axis=1);basis=(Y-eta)/np.sqrt(v)
        alpha=np.array([np.sum(prob*g*np.prod(basis[:,[j for j in range(m) if A>>j&1]],axis=1)) for A in range(1<<m)]);lam=alpha**2
        mu=[fw(c)**2 for c in children];bet=np.array([sum(lam[A] for A in range(1<<m) if A>>j&1) for j in range(m)])
        X=np.arange(1<<n);index=np.zeros(1<<n,dtype=int);off=0
        for j,k in enumerate(sizes):index|=((children[j][(X>>off)&((1<<int(k))-1)]<0).astype(int)<<j);off+=int(k)
        f=g[index];actual=fw(f);muF=actual**2;expected=np.zeros(1<<n);E=[];offset=0
        for S in range(1<<n):
            A=0;fac=1;off=0
            for j,k in enumerate(sizes):
                T=(S>>off)&((1<<int(k))-1);off+=int(k)
                if T:A|=1<<j;fac*=fw(children[j])[T]/math.sqrt(v[j])
            expected[S]=alpha[A]*fac
        maxcoeff=max(maxcoeff,float(np.max(abs(actual-expected))))
        actualE=erasures(muF,n)
        for j,k in enumerate(sizes):
            ej=erasures(mu[j],int(k));b0=mu[j][0]
            for i in range(int(k)):
                r=mu[j][1<<i]/v[j]
                correction=sum(ph(lam[A],r*lam[A|(1<<j)]) for A in range(1<<m) if not A>>j&1)
                val=bet[j]/v[j]*(ej[i]-ph(b0,mu[j][1<<i]))+correction
                E.append(val)
                inf=muF[(X&(1<<(offset+i)))!=0].sum();rhs=bet[j]/v[j]*mu[j][(np.arange(1<<int(k))&(1<<i))!=0].sum();maxI=max(maxI,abs(inf-rhs))
            offset+=int(k)
        maxE=max(maxE,float(np.max(abs(np.array(E)-actualE))));cases+=1
        if trial<12:records.append(dict(n=n,children=[hex_tt(c) for c in children],sizes=list(map(int,sizes)),outer=hex_tt(g),tt=hex_tt(f)))
    # Random formula gates, with literal leaves. Every sibling's variable set is disjoint.
    for trial in range(256):
        n=int(rng.integers(2,11));X=signs(n);pool=[dict(f=X[:,i],mask=1<<i,paths={i:[]}) for i in range(n)]
        while len(pool)>1:
            rng.shuffle(pool);arity=min(int(rng.integers(2,5)),len(pool));children=pool[:arity];pool=pool[arity:]
            g=rng.choice([-1,1],1<<arity);idx=sum((c['f']<0).astype(int)<<j for j,c in enumerate(children));paths={}
            for j,c in enumerate(children):
                for i,p in c['paths'].items():paths[i]=p+[d['mask'] for l,d in enumerate(children) if l!=j]
            pool.append(dict(f=g[idx],mask=sum(c['mask'] for c in children),paths=paths))
        F=pool[0];mu=fw(F['f'])**2;ex=erasures(mu,n)
        for i,p in F['paths'].items():maxpath=max(maxpath,abs(conditional(mu,i,p)-ex[i]))
    z=dict(composition_cases=cases,path_witness_cases=256,coefficient_residual=maxcoeff,erasure_residual_bits=maxE,influence_residual=maxI,path_sufficiency_residual_bits=maxpath,examples=records,seed=141430,elapsed_seconds=time.time()-start,maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1)
    assert max(maxcoeff,maxE,maxI,maxpath)<1e-10
    Path('composition.json').write_text(json.dumps(z,indent=2)+'\n');print('COMPOSITION PASS',json.dumps(z))
if __name__=='__main__':main()
