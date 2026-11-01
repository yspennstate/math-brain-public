"""A bounded diagnostic of the proposed aggregate gradient-only sign."""
import numpy as np

def grad(J):
    g=np.zeros_like(J)
    for m in range(4):
        M=J-np.diag([1-((m>>j)&1) for j in range(2)])
        p=(-1)**(2-m.bit_count())*np.linalg.det(M)
        g-=p*np.log(p)*np.linalg.inv(M)
    return g

def joint(K):
    edges=[(0,1),(0,2),(1,2)]
    V=np.zeros((3,3))
    for k in range(3):
        rr=[j for j in range(3) if j!=k]
        a=K[k,k];v=K[rr,k];R=K[np.ix_(rr,rr)]
        G=grad(R-np.outer(v,v)/a)-grad(R+np.outer(v,v)/(1-a))
        B=np.zeros((2,3))
        for j,r in enumerate(rr):B[j,edges.index(tuple(sorted((k,r))))]=1
        V+=B.T@G@B
    return V

rng=np.random.default_rng(71)
smallest=(float('inf'),None)
for n in range(80):
    U,_=np.linalg.qr(rng.normal(size=(3,3)))
    lam=np.array([.002,.15,.998]) if n%2 else rng.uniform(.02,.98,3)
    K=U@np.diag(lam)@U.T
    val=np.linalg.eigvalsh(joint(K))[0]
    if val<smallest[0]:smallest=(val,K)
    if val < -1e-8:
        print('Joint gradient-only sign fails numerically.',val)
        print(K)
        break
else:
    print('No counterexample in 80 fixed-seed diagnostics; not a proof.')
print('minimum',smallest[0])
