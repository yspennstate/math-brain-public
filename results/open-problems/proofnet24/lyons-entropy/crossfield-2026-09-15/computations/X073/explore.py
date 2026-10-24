import numpy as np
from itertools import product

def basis(n):
    B=[]
    for i in range(n):
        a=np.zeros((n,n),complex);a[i,i]=1;B.append(a)
    for i in range(n):
        for j in range(i+1,n):
            a=np.zeros((n,n),complex);a[i,j]=a[j,i]=1;B.append(a)
            a=np.zeros((n,n),complex);a[i,j]=1j;a[j,i]=-1j;B.append(a)
    return np.array(B)

def tables(K):
    n=len(K);B=basis(n);xs=list(product([0,1],repeat=n));p=[];J=[];T=[]
    for x in xs:
        M=K-np.diag(1-np.array(x));R=np.linalg.inv(M)
        px=np.linalg.det(M).real*(-1)**(n-sum(x))
        RB=np.einsum('ij,bjk->bik',R,B);tr=np.trace(RB,axis1=1,axis2=2).real
        p.append(px);J.append(px*tr)
        T.append(px*(np.outer(tr,tr)-np.einsum('bij,cji->bc',RB,RB).real))
    return np.array(p),np.array(J),np.array(T),xs

def curvatures(K):
    p,J,T,xs=tables(K);Q=J.T@(J/p[:,None])+np.einsum('x,xij->ij',np.log(p),T)
    D=np.zeros_like(Q)
    for a,x in enumerate(xs):
        for i in range(len(K)):
            if x[i]:continue
            y=list(x);y[i]=1;b=xs.index(tuple(y));u,v=p[a],p[b]
            z=J[a]/u-J[b]/v
            D+=.5*((u+v)*np.outer(z,z)+(np.log(u/v)+1-v/u)*T[a]+(np.log(v/u)+1-u/v)*T[b])
    return Q,D

if __name__=='__main__':
    examples=[np.array([[.2,.1,(1+1j)/20],[.1,.6,.1],[(1-1j)/20,.1,.8]]),
              np.array([[.5,.15,.15j],[.15,.5,.15],[-.15j,.15,.5]]),
              np.array([[.1,.09,.01],[.09,.1,0],[.01,0,.9]]),
              np.array([[.2,.1],[.1,.7]])]
    for K in examples:
        Q,D=curvatures(K)
        print('spectrum K',np.linalg.eigvalsh(K),'Q',np.linalg.eigvalsh(Q),'forcing',np.linalg.eigvalsh(D))
    rng=np.random.default_rng(73)
    worst=(0,None)
    for j in range(300):
        Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));U=np.linalg.qr(Z)[0]
        K=U@np.diag(rng.uniform(.001,.999,3))@U.conj().T
        Q,D=curvatures(K);val=np.linalg.eigvalsh(D)[0]
        if val<worst[0]:worst=(val,K)
    print('minimum forcing',worst)
