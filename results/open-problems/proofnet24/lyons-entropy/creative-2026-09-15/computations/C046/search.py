import json, numpy as np
from pathlib import Path
rng=np.random.default_rng(460915)
n=3
E=[]
for i in range(n):
    a=np.zeros((n,n),complex); a[i,i]=1; E.append(a)
for i in range(n):
    for j in range(i+1,n):
        a=np.zeros((n,n),complex); a[i,j]=a[j,i]=1; E.append(a)
        a=np.zeros((n,n),complex); a[i,j]=1j; a[j,i]=-1j; E.append(a)
E=np.array(E)
def jets(K):
    p=[]; g=[]; h=[]; mu=[]
    d=K.diagonal().real
    for mask in range(8):
        out=np.array([not(mask>>i&1) for i in range(3)])
        Q=K-np.diag(out.astype(int)); z=(-1)**sum(out)*np.linalg.det(Q).real
        R=np.linalg.inv(Q); V=R@E; score=np.trace(V,axis1=1,axis2=2).real
        Hess=z*(np.outer(score,score)-np.einsum('aij,bji->ab',V,V).real)
        p.append(z);g.append(z*score);h.append(Hess)
        mu.append(np.prod(np.where(out,1-d,d)))
    return np.array(p),np.array(g),np.array(h),np.array(mu)
def forms(K,s):
    p,g,h,mu=jets(K); r=p/mu
    U=np.einsum('si,sj,s->ij',g,g,1/mu/(r+s)**2)-np.einsum('sij,s->ij',h,1/(r+s))
    return U
best=(0,None)
# First structured exchangeable real kernels, then small fixed random search.
count=0
for d in np.linspace(.05,.95,19):
    for b in np.linspace(-.45,.45,37):
        K=(d-b)*np.eye(3)+b*np.ones((3,3))
        if np.linalg.eigvalsh(K).min()<=.0001 or np.linalg.eigvalsh(K).max()>=.9999: continue
        p,g,h,mu=jets(K);r=p/mu
        for s in [0,.01,.1,1,10,100,1e5]:
            U=np.einsum('si,sj,s->ij',g,g,1/mu/(r+s)**2)-np.einsum('sij,s->ij',h,1/(r+s))
            w,v=np.linalg.eigh(U*(1+s)**2)
            count+=1
            if w[0]<best[0]:
                best=(w[0],{'d':d,'b':b,'K_re':K.tolist(),'K_im':np.zeros((3,3)).tolist(),'s':s,'eigenvalue_scaled':w[0],'direction':v[:,0].tolist()})
print('structured',count,best)
if best[0]<-1e-6:
    Path('computations/C046/search_result.json').write_text(json.dumps(best[1],indent=2))
else:
    for it in range(500):
        q,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
        vals=rng.beta(.5,.5,3)*.999+.0005
        K=q@np.diag(vals)@q.conj().T
        p,g,h,mu=jets(K);r=p/mu
        for s in [.01,.1,1,10,100,1e5]:
            U=np.einsum('si,sj,s->ij',g,g,1/mu/(r+s)**2)-np.einsum('sij,s->ij',h,1/(r+s))
            w,v=np.linalg.eigh(U*(1+s)**2)
            if w[0]<best[0]:
                best=(w[0],{'K_re':K.real.tolist(),'K_im':K.imag.tolist(),'s':s,'eigenvalue_scaled':w[0],'direction':v[:,0].tolist(),'vals':vals.tolist(),'iteration':it})
        if best[0]<-1e-4: break
    print('random',it,best)
    if best[1]: Path('computations/C046/search_result.json').write_text(json.dumps(best[1],indent=2))
