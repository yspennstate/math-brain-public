import numpy as np
from itertools import product
rng=np.random.default_rng(7007016)
def hess_channel(weights,xs,a,b):
    n=xs.shape[1];ys=np.array(list(product([0,1],repeat=n)))
    p=np.zeros(len(ys));dp=np.zeros((len(ys),2));dd=np.zeros((len(ys),2,2))
    for w,x in zip(weights,xs):
        q=np.where(x,a,b)
        f=np.where(ys,q,1-q)
        prod=f.prod(axis=1)
        z=np.where(ys,1.,-1.)/f
        score=np.stack([z[:,x==1].sum(axis=1),z[:,x==0].sum(axis=1)],axis=1)
        p+=w*prod;dp+=w*prod[:,None]*score
        dlog=np.stack([(z[:,x==1]**2).sum(axis=1),(z[:,x==0]**2).sum(axis=1)],axis=1)
        for i in range(2):
            for j in range(2):
                dd[:,i,j]+=w*prod*(score[:,i]*score[:,j]-(dlog[:,i] if i==j else 0))
    return -np.einsum('yi,yj,y->ij',dp,dp,1/p)-np.einsum('yij,y->ij',dd,np.log(p))
for n in [3,4,5,6]:
    xs=np.array([x for x in product([0,1],repeat=n) if sum(x)==1])
    mn=1e9;best=None
    for k in range(200):
        w=rng.dirichlet(np.ones(n)*.7);a,b=rng.uniform(.02,.98,size=2)
        h=hess_channel(w,xs,a,b);hu=hess_channel(np.ones(n)/n,xs,a,b)
        low=np.linalg.eigvalsh(hu-h)[0]
        if low<mn:mn=low;best=[w.tolist(),a,b,h.tolist(),hu.tolist()]
    print(n,'minimum convexity gap',mn,'sample',best,flush=True)
