import numpy as np
rng=np.random.default_rng(7007017)
def trans_hess(p,n):
    arr=p.reshape((2,)*n);ds=[]
    for i in range(n):
        mar=arr.sum(axis=i,keepdims=True);ds.append(np.concatenate([-mar,mar],axis=i))
    ds=np.array(ds).reshape(n,-1);Q=(ds/p)@ds.T
    for i in range(n):
        for j in range(i+1,n):
            mar=arr.sum(axis=(i,j),keepdims=True);v=np.concatenate([-mar,mar],axis=i);v=np.concatenate([-v,v],axis=j)
            v=np.sum(v*np.log(arr));Q[i,j]+=v;Q[j,i]+=v
    return Q
for n in range(2,8):
    mn=(np.inf,None)
    for k in range(2000):
        p=rng.dirichlet(np.full(2**n,10**rng.uniform(-.7,1.3)));p=np.maximum(p,1e-80);p/=p.sum()
        Q=trans_hess(p,n);ev=np.linalg.eigh(Q)
        if ev[0][0]<mn[0]:mn=(ev[0][0],p)
        if ev[0][0]<-1e-7:
            print('NEGATIVE',n,k,ev[0],p,ev[1][:,0],flush=True);break
    print(n,mn[0],flush=True)
