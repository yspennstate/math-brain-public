import numpy as np

def fwht(a):
    a=np.array(a,dtype=np.float64,copy=True)
    n=a.shape[-1]; h=1
    while h<n:
        b=a.reshape(*a.shape[:-1],-1,2*h)
        x=b[...,:h].copy(); y=b[...,h:].copy()
        b[...,:h]=x+y; b[...,h:]=x-y
        h*=2
    return a

def entropy(p):
    p=np.asarray(p); safe=np.where(p>0,p,1)
    return -(p*np.log2(safe)).sum(axis=-1)

def metrics(f):
    a=fwht(f)/len(f); p=a*a; n=(len(f)).bit_length()-1
    H=entropy(p); weights=np.array([s.bit_count() for s in range(len(f))]); I=p@weights
    B=K=0.; Bs=[]; Is=[]; ov=[]; d=[]
    for i in range(n):
        ids=np.array([s for s in range(len(f)) if not s>>i&1]); r=p[ids]; t=p[ids+(1<<i)]
        bi=entropy(r)+entropy(t)-entropy(r+t)
        B+=bi; Bs.append(bi); Is.append(t.sum()); ov.append(np.sqrt(r*t).sum())
        mask=(r>0)&(t>0)
        K+=(np.minimum(r[mask],t[mask])*np.abs(np.log2(r[mask]/t[mask]))).sum()
        hp=entropy((a[ids]+a[ids+(1<<i)])**2); hm=entropy((a[ids]-a[ids+(1<<i)])**2)
        d.append(H-(hp+hm)/2)
    return dict(H=float(H),I=float(I),B=float(B),K=float(K),Bs=Bs,Is=Is,overlap=ov,delta=d)

if __name__=='__main__':
    rng=np.random.default_rng(20260920)
    maxima={k:(0,None) for k in ['B/I','K/I','min_delta/Ii']}
    compression_bad=None
    for n in [2,3,4,5,6,7,8]:
        count=2**(2**n) if n<=3 else 4000
        for z in range(count):
            if n<=3: f=1-2*((z>>np.arange(2**n))&1)
            else: f=1-2*(rng.random(2**n)<rng.choice([.01,.05,.2,.5]))
            m=metrics(f)
            if not m['I']:continue
            vals={'B/I':m['B']/m['I'],'K/I':m['K']/m['I'],'min_delta/Ii':min(dd/t for dd,t in zip(m['delta'],m['Is']) if t>0)}
            for k,v in vals.items():
                if v>maxima[k][0]:maxima[k]=(v,(n,f.tolist(),m))
            if compression_bad is None:
                fc=f.copy()
                for s in range(0,len(f),2):fc[s],fc[s+1]=min(f[s],f[s+1]),max(f[s],f[s+1])
                mc=metrics(fc)
                if mc['H']<m['H']-1e-9 and mc['I']<=m['I']+1e-9:
                    compression_bad=(f.tolist(),fc.tolist(),m,mc)
        print(n,{k:(v[0],None if v[1] is None else v[1][0]) for k,v in maxima.items()},flush=True)
    import json
    print(json.dumps({'maxima':maxima,'compression_bad':compression_bad},indent=2))
