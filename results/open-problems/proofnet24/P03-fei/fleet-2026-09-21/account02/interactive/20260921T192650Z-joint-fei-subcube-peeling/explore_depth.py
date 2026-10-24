from __future__ import annotations
import numpy as np, math, json

def walsh(x):
    a=np.asarray(x,dtype=np.int64).copy(); N=a.shape[-1]; h=1
    while h<N:
        v=a.reshape(*a.shape[:-1],-1,2,h);u=v[...,0,:].copy();w=v[...,1,:].copy()
        v[...,0,:]=u+w;v[...,1,:]=u-w;h*=2
    return a

def measures(v):
    v=np.atleast_2d(v);N=v.shape[-1];n=N.bit_length()-1;W=walsh(v)
    deg=np.array([s.bit_count() for s in range(N)])
    bits=np.array([[(s>>i)&1 for i in range(n)] for s in range(N)])
    p=W.astype(float)**2/N**2;infs=p@bits;fold=(infs>.5).astype(np.int64)@(1<<np.arange(n))
    p=np.take_along_axis(p,np.arange(N)[None,:]^fold[:,None],axis=1)
    j=p@bits;I=j.sum(axis=1);I2=p@(deg*(deg-1))
    h=-np.sum(p*np.log2(np.where(p>0,p,1)),axis=1)
    L=-np.sum(j*np.log2(np.where(j>0,j,1)),axis=1)
    D=I2-.5*L
    return {'H':h,'I':I,'D':D,'D_by_I':np.divide(D,I,out=np.zeros_like(I),where=I>0),
      'excess':h-4*I-2*D,'jmax':j.max(axis=1) if n else np.zeros(len(v)),
      'I2':I2,'ratio':np.divide(h,I,out=np.zeros_like(I),where=I>0)}

def main():
    out=[];rng=np.random.default_rng(2026092119)
    for n,trials in [(4,None),(5,10000),(6,5000),(7,3000),(8,2000),(9,500),(10,200)]:
        N=1<<n
        if trials is None:
            ids=np.arange(1<<N,dtype=np.uint64)
            v=1-2*((ids[:,None]>>np.arange(N,dtype=np.uint64))&1).astype(np.int64)
        else:v=rng.choice(np.array([-1,1]),(trials,N))
        m=measures(v); idx=int(np.argmax(m['excess']));out.append({'n':n,'num':len(v),'max_excess':float(m['excess'][idx]),'max_ratio':float(m['ratio'].max()),'max_data':{k:float(x[idx]) for k,x in m.items()}})
    for n in range(2,15):
        N=1<<n;pop=np.array([s.bit_count() for s in range(N)])
        v=[];names=[]
        for k in range(n):
            v.append(np.where(pop<=k,-1,1));names.append(f'threshold{n}_{k}')
        m=measures(v);idx=int(np.argmax(m['excess']));out.append({'family':'threshold','n':n,'name':names[idx],'max_excess':float(m['excess'][idx]),'max_data':{k:float(x[idx]) for k,x in m.items()}})
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
