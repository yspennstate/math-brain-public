import math
import numpy as np

rng=np.random.default_rng(20260923)

# 1. Cauchy-Binet overlap identity for symmetric zero-diagonal F.
for n in range(4,10):
    for _ in range(80):
        F=rng.normal(size=(n,n)); F=(F+F.T)/2; np.fill_diagonal(F,0.0)
        sv=np.linalg.svd(F,compute_uv=False)
        V2=sum((sv[i]*sv[j])**2 for i in range(n) for j in range(i+1,n))
        q=np.sum(F*F,axis=1)
        P=sum(F[i,j]**4 for i in range(n) for j in range(i+1,n))
        W=0.0
        for i in range(n):
            for j in range(i+1,n):
                I={i,j}
                for k in range(n):
                    for l in range(k+1,n):
                        J={k,l}
                        if I.isdisjoint(J):
                            W += np.linalg.det(F[np.ix_([i,j],[k,l])])**2
        assert abs(V2-(W+np.sum(q*q)-P)) <= 2e-8*max(1,V2)
        assert V2/np.sum(F*F) + 1e-12 >= sv[1]**2/2

# 2. Rank-one lift inequality on exact rank-two cores.
for m,n in [(5,6),(7,5),(8,9)]:
    for _ in range(150):
        L,_=np.linalg.qr(rng.normal(size=(m,2)))
        R,_=np.linalg.qr(rng.normal(size=(n,2)))
        s=np.sort(rng.uniform(.2,3,size=2))[::-1]
        F0=L@np.diag(s)@R.T
        u=rng.normal(size=m); v=rng.normal(size=n)
        alpha=np.linalg.norm(u-L@(L.T@u))
        beta=np.linalg.norm(v-R@(R.T@v))
        K=np.linalg.norm(u)*np.linalg.norm(v)+s[0]
        M=np.outer(u,v)-F0
        sm=np.linalg.svd(M,compute_uv=False)
        rhs=alpha*beta*s[0]*s[1]/K**2
        assert sm[2]+2e-11 >= rhs

# 3. Pure-star determinant identity and mixed-Fresnel constants.
for _ in range(200):
    u0=rng.normal(); u=rng.normal(size=5); b=rng.normal(size=5)
    w=np.r_[u0,u]
    e=np.zeros(6); e[0]=1
    be=np.r_[0,b]
    A=np.outer(w,w)-np.outer(e,be)-np.outer(be,e)
    eig=np.linalg.eigvalsh(A)
    nz=eig[np.abs(eig)>1e-9]
    Delta=np.dot(u,u)*np.dot(b,b)-np.dot(u,b)**2
    if Delta>1e-8:
        assert len(nz)==3
        assert abs(np.prod(nz)+Delta) <= 2e-8*max(1,Delta)

C_MF=3*2**(4/3)
C_PARTNER=6*math.sqrt(math.pi)/(math.sqrt(15)/2-1)
assert C_MF < 7.56
assert C_PARTNER < 4*math.pi
print('C_MF =',repr(C_MF))
print('C_PARTNER =',repr(C_PARTNER))
print('FOUR_PI =',repr(4*math.pi))
print('QFORM_B11_R24_DEFECT_STAR_CHECK_PASS')
