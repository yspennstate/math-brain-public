import numpy as np
import math


def nested_mass(x,y,u,v,c,N):
    P=0.0
    for r in range(len(c)):
        for b in range(len(u)):
            for d in range(b+1,len(u)):
                A=np.array([[x,u[b],u[d]],
                            [y,v[b],v[d]],
                            [c[r],N[r,b],N[r,d]]],dtype=float)
                P+=np.linalg.det(A)**2
    return P


def resources(x,y,u,v,c,N):
    Av=float(v@v*np.sum(N*N)-(N@v)@(N@v))
    Au=float(u@u*np.sum(N*N)-(N@u)@(N@u))
    Delta2=float((u@u)*(v@v)-(u@v)**2)
    return max(0.0,Av),max(0.0,Au),max(0.0,Delta2)


def best_cross_split(v,N):
    q=len(v)
    best=0.0
    for mask in range(1,2**q-1):
        C1=[j for j in range(q) if (mask>>j)&1]
        C2=[j for j in range(q) if not ((mask>>j)&1)]
        S=0.0
        for r in range(N.shape[0]):
            for b in C1:
                for d in C2:
                    S+=(v[b]*N[r,d]-v[d]*N[r,b])**2
        best=max(best,S)
    return best


def area_scalar_split(u,v):
    q=len(u)
    Delta2=float((u@u)*(v@v)-(u@v)**2)
    bestS=-1.0
    best=None
    for mask in range(1,2**q-1):
        C1=np.array([(mask>>j)&1 for j in range(q)],dtype=bool)
        C2=~C1
        S=0.0
        for b in np.where(C1)[0]:
            for d in np.where(C2)[0]:
                S+=(u[b]*v[d]-v[b]*u[d])**2
        if S>bestS:
            bestS=S
            best=(C1,C2)
    C1,C2=best
    G1=np.array([[u[C1]@u[C1],u[C1]@v[C1]],
                 [u[C1]@v[C1],v[C1]@v[C1]]],dtype=float)
    G2=np.array([[u[C2]@u[C2],u[C2]@v[C2]],
                 [u[C2]@v[C2],v[C2]@v[C2]]],dtype=float)
    J=np.array([[0.0,1.0],[-1.0,0.0]])
    H=J@G2@J.T
    vals,Q=np.linalg.eigh(G1)
    prod=max((Q[:,j]@G1@Q[:,j])*(Q[:,j]@H@Q[:,j]) for j in range(2))
    return Delta2,bestS,float(prod)


count=0
worst_nested=float('inf')
worst_cross=float('inf')
worst_scalar=float('inf')
for seed in range(200):
    rng=np.random.default_rng(seed)
    q=int(rng.integers(2,7))
    m=int(rng.integers(1,6))
    x,y=rng.integers(-3,4,size=2).astype(float)
    u=rng.integers(-3,4,size=q).astype(float)
    v=rng.integers(-3,4,size=q).astype(float)
    c=rng.integers(-3,4,size=m).astype(float)
    N=rng.integers(-3,4,size=(m,q)).astype(float)

    P=nested_mass(x,y,u,v,c,N)
    Av,Au,Delta2=resources(x,y,u,v,c,N)
    rhs=3.0*(x*x*Av+y*y*Au+(c@c)*Delta2)
    assert P<=rhs+1e-7
    if P>1e-12:
        worst_nested=min(worst_nested,rhs/P)

    if Av>1e-12:
        best=best_cross_split(v,N)
        assert best+1e-7>=Av/2.0
        worst_cross=min(worst_cross,best/(Av/2.0))

    if Delta2>1e-12:
        D,S,prod=area_scalar_split(u,v)
        assert S+1e-7>=D/2.0
        assert prod+1e-7>=S/2.0
        worst_scalar=min(worst_scalar,prod/(D/4.0))
    count+=1


theta=1/16
kappa=1/(256*math.sqrt(3))
edge_floor=theta*kappa**3/(36*math.sqrt(2))
scalar_floor=theta*kappa**3/36
partner_cap=72*math.sqrt(2)/(theta*kappa**3)

print('QFORM_B07_R25_CHECK_PASS')
print('cases',count)
print('min_nested_rhs_over_P',worst_nested)
print('min_crosssplit_over_Av_half',worst_cross)
print('min_scalar_product_over_Delta2_quarter',worst_scalar)
print('theta_1_16_kappa',kappa)
print('edge_star_core_floor',edge_floor)
print('three_scalar_floor',scalar_floor)
print('partner_joint_cap',partner_cap)
