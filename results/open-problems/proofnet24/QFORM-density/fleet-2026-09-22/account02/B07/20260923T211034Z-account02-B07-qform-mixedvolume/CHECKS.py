import itertools, math
import numpy as np


def e2(G):
    return (np.trace(G)**2 - np.trace(G @ G))/2


def H2(G):
    return G @ G - np.trace(G)*G + e2(G)*np.eye(G.shape[0])


def ek_gram(M,k):
    s=np.linalg.svd(M,compute_uv=False)**2
    ans=0.0
    for I in itertools.combinations(range(len(s)),k):
        p=1.0
        for i in I: p*=s[i]
        ans+=p
    return ans

rng=np.random.default_rng(20260923)
nL,nR=6,4
K=rng.normal(size=(nL,nR))
C=rng.normal(size=(nL,nL)); C=(C+C.T)/2
np.fill_diagonal(C,0.0)

F=[]
for i in range(nL):
    rows=[j for j in range(nL) if j!=i]
    Ki=K[rows,:]
    ci=C[rows,i]
    F.append(float(ci @ H2(Ki@Ki.T) @ ci))
Fsum=sum(F)

avg=0.0
best=0.0
for mask in range(1<<nL):
    I=[i for i in range(nL) if (mask>>i)&1]
    J=[i for i in range(nL) if not ((mask>>i)&1)]
    if len(I)>=3:
        M=np.concatenate([K[I,:],C[np.ix_(I,J)]],axis=1) if J else K[I,:]
        z=ek_gram(M,3) if min(M.shape)>=3 else 0.0
    else:
        z=0.0
    avg+=z/(1<<nL)
    best=max(best,z)
assert avg+1e-10 >= Fsum/16
print("mixed-volume Fsum",Fsum)
print("colour-average E3",avg)
print("Fsum/16",Fsum/16)
print("best physicalized E3",best)

# Three-bank exact stress.  Its six nonzero eigenvalues are those of this
# macro matrix for every bank size m.
gamma=0.25
B=np.ones((3,3))-np.eye(3)
macro=np.block([[gamma*B,2*np.eye(3)],[2*np.eye(3),np.zeros((3,3))]])
ev=np.linalg.eigvalsh(macro)
assert np.min(np.abs(ev))>1
assert abs(np.prod(np.abs(ev))-64)<1e-10
print("three-bank macro eigenvalues",ev)
print("absolute eigenvalue product",np.prod(np.abs(ev)))

for m in [2,3,8,16,64]:
    lam=np.array([4.0,4.0,4.0*(1-1/m)])
    Z=sum(lam[a]*lam[b] for a in range(3) for b in range(a+1,3))
    alpha=lam*(lam.sum()-lam)/Z
    assert alpha[0]>2/3 and alpha[1]>2/3 and alpha[2]<2/3
    mu=(48-Z)/48
    assert abs(mu-2/(3*m))<1e-12
    print("m",m,"Z_i",Z,"alphas",alpha,"mu_i",mu)

h=(2*math.sqrt(2)-1)/1572864
Z0=854675.100194511
z3coef=Z0/(144*1024**2)
C3=3*2**(4/3)*math.e**(1/3)
Dprime=9*math.sqrt(3*math.e)
print("live mixed-E3 coefficient",z3coef)
print("marginal-free density coefficient times h^-1",C3*z3coef**(-1/6))
print("pinned-Dprime coefficient times h^-1",Dprime*z3coef**(-1/6))
print("STATUS=PASS")
