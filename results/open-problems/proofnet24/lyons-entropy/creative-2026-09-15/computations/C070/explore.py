import numpy as np
from itertools import product
rng=np.random.default_rng(7007015)

def common_shift(p,n):
    arr=p.reshape((2,)*n)
    ds=[]
    for i in range(n):
        mar=arr.sum(axis=i,keepdims=True)
        ds.append(np.concatenate([-mar,mar],axis=i))
    dp=sum(ds)
    dd=np.zeros_like(arr)
    for i in range(n):
        for j in range(i+1,n):
            mar=arr.sum(axis=(i,j),keepdims=True)
            v=np.concatenate([-mar,mar],axis=i)
            v=np.concatenate([-v,v],axis=j)
            dd+=2*v
    return -np.sum(dp*dp/arr)-np.sum(dd*np.log(arr))
for n in range(2,9):
    mx=(-1e90,None)
    for k in range(1000):
        p=rng.dirichlet(np.full(2**n,10**rng.uniform(-1,1)))
        p=np.maximum(p,1e-90);p/=sum(p)
        h=common_shift(p,n)
        if h>mx[0]: mx=h,p
    print(n,mx[0],flush=True)
    if mx[0]>0:
        np.savez('computations/C070/universal_counter.npz',p=mx[1],n=n,h=mx[0]);break
