import numpy as np, json, math

def fwht(x):
    a=np.array(x,dtype=float,copy=True)
    h=1
    while h<a.shape[-1]:
        v=a.reshape(*a.shape[:-1],-1,2*h)
        u=v[...,:h].copy(); w=v[...,h:].copy()
        v[...,:h]=u+w;v[...,h:]=u-w
        h*=2
    return a

def entropy(p):
    return -(p*np.log2(np.maximum(p,1e-300))).sum(axis=-1)

def metrics(f):
    N=f.shape[-1];n=N.bit_length()-1
    a=fwht(f)/N;p=a*a
    bits=((np.arange(N)[None,:]>>np.arange(n)[:,None])&1)
    alpha=p@bits.T
    q=np.ones_like(p)
    for i in range(n):q*=np.where(bits[i],alpha[...,i,None],1-alpha[...,i,None])
    mask=p>0
    mass=(q*mask).sum(axis=-1)
    qcond=q*mask/np.maximum(mass[...,None],1e-300)
    b=np.sign(a)*np.sqrt(qcond)
    c=fwht(fwht(b)**2)/N
    v=np.minimum(c*c,1)
    Z=v.sum(axis=-1)
    L=entropy(v)
    H=entropy(p)
    K=(p*np.log2(np.maximum(p,1e-300)/np.maximum(q,1e-300))).sum(axis=-1)
    Kshape=K+np.log2(mass)
    I=np.minimum(alpha,1-alpha).sum(axis=-1)
    score=(L/Z/4-Kshape)/np.maximum(I,1e-300)
    return score, L/Z, Kshape, I, Z, mass

if __name__=='__main__':
    out=[]
    rng=np.random.default_rng(20260930)
    for n in range(1,11):
        N=1<<n;best=(-float('inf'),None);count=0
        batches=range(0,1<<N,512) if n<=4 else range(0,10000,256)
        for start in batches:
            if n<=4:
                ids=np.arange(start,min(start+512,1<<N),dtype=np.uint64)
                f=1-2*((ids[:,None]>>np.arange(N,dtype=np.uint64))&1).astype(float)
            else:
                size=min(256,10000-start)
                bias=rng.choice([.5,.01,.05,.1,.2,.35,.45],size=(size,1))
                f=np.where(rng.random((size,N))<bias,-1.,1.)
            m=metrics(f);idx=int(np.argmax(m[0]));count+=len(f)
            if m[0][idx]>best[0]:best=(float(m[0][idx]),{'truth_negative':[int(x) for x in np.flatnonzero(f[idx]<0)],'metrics':[float(z[idx]) for z in m]})
        out.append({'n':n,'count':count,'maximum':best[0],'witness':best[1]})
        print(json.dumps(out[-1]),flush=True)
    with open('exploration.json','w') as g:json.dump(out,g,indent=2)
