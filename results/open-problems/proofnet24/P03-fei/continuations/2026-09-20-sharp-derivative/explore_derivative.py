"""Floating-point discovery only; no universal conclusion follows from this script."""
import numpy as np, json

def fwht(a):
    a=np.array(a,copy=True)
    n=a.shape[-1]; h=1
    while h<n:
        b=a.reshape(*a.shape[:-1],-1,2*h)
        x=b[...,:h].copy(); y=b[...,h:].copy()
        b[...,:h]=x+y; b[...,h:]=x-y; h*=2
    return a

def entropy(p):
    return -(p*np.log2(np.where(p>0,p,1))).sum(axis=-1)

def affine_min(f):
    N=len(f); n=N.bit_length()-1
    aa=fwht(f.astype(np.int64))
    corr=fwht(aa*aa)//N
    cost=(N-np.abs(corr))//2
    basis=[0]*n; rank=0; total=0
    for v in np.argsort(cost):
        if v==0:continue
        w=int(v)
        while w:
            j=w.bit_length()-1
            if basis[j]:w^=basis[j]
            else:
                basis[j]=w;rank+=1;total+=int(cost[v]);break
        if rank==n:break
    return total/N

def measure(f):
    N=len(f); labels=np.arange(N); n=N.bit_length()-1
    a=fwht(f)/N; p=a*a; H=entropy(p)
    der=f[None,:]*f[np.bitwise_xor(labels[:,None],labels[None,:])]
    ad=fwht(der)/N
    Hd=entropy(ad*ad).mean()
    M=affine_min(f)
    return float(H),float(Hd),M,float((2*H-Hd)/M) if M else 0

def main():
    rng=np.random.default_rng(20260920)
    best=(0,None); counts={}
    for n in range(1,5):
        N=1<<n; mx=0
        for start in range(0,1<<(N-1),128):
            codes=np.arange(start,min(start+128,1<<(N-1)),dtype=np.int64)
            fs=(1-2*((codes[:,None]>>np.arange(N))&1)).astype(np.int64)
            a=fwht(fs)/N; H=entropy(a*a)
            labels=np.arange(N); der=fs[:,None,:]*fs[:,np.bitwise_xor(labels[:,None],labels[None,:])]
            ad=fwht(der)/N; HD=entropy(ad*ad).mean(axis=-1)
            for f,h,hd in zip(fs,H,HD):
                m=affine_min(f); r=float((2*h-hd)/m) if m else 0
                mx=max(mx,r)
                if r>best[0]+1e-10:best=(r,{'n':n,'f':f.tolist(),'H':float(h),'EHder':float(hd),'M':m})
        counts[str(n)]=1<<(N-1)
        print('exhaustive',n,mx,flush=True)
    for n in range(5,10):
        N=1<<n
        for k in range(150):
            f=(1-2*(rng.random(N)<rng.choice([.015,.03,.1,.25,.5]))).astype(np.int64)
            h,hd,m,r=measure(f)
            if r>best[0]+1e-10:best=(r,{'n':n,'f':f.tolist(),'H':h,'EHder':hd,'M':m})
        print('sampled',n,best[0],flush=True)
    print(json.dumps({'best':best,'canonical_exhaustive_counts':counts,'scope':'floating-point exploratory test, not a proof'},indent=2))

if __name__=='__main__':main()
