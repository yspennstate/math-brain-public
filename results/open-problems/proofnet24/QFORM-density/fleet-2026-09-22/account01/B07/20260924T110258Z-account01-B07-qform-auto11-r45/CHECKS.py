import itertools
import math
import numpy as np

THRESH=1/24

def make_block_U(a):
    # Three disjoint-support columns. Heavy energy a_j is split into pieces 0.05
    # except for harmless final remainders >1/24; light energy is split into <=0.03.
    cols=[]
    rows=[]
    total_n=0
    specs=[]
    for aj in a:
        # choose equal heavy pieces, each >1/24
        mh=max(1,int(math.floor(aj/0.05+1e-12)))
        while aj/mh <= THRESH:
            mh-=1
        # choose light count so each light leverage <=0.03
        rem=1-aj
        ml=max(1,int(math.ceil(rem/0.03))) if rem>0 else 0
        specs.append((mh,ml,aj,rem))
        total_n+=mh+ml
    U=np.zeros((total_n,3))
    p=0
    for j,(mh,ml,aj,rem) in enumerate(specs):
        U[p:p+mh,j]=math.sqrt(aj/mh)
        p+=mh
        if ml:
            U[p:p+ml,j]=math.sqrt(rem/ml)
            p+=ml
    assert np.allclose(U.T@U,np.eye(3),atol=1e-13)
    return U

def packet_coefficients(U):
    ell=np.sum(U*U,axis=1)
    K=set(np.where(ell>THRESH)[0].tolist())
    G=U[list(K)].T@U[list(K)] if K else np.zeros((3,3))
    eig=np.linalg.eigvalsh(G)[::-1]
    cs=np.zeros(4)
    for I in itertools.combinations(range(U.shape[0]),3):
        k=sum(i in K for i in I)
        d=np.linalg.det(U[list(I),:])
        cs[k]+=d*d
    c0=np.prod(1-eig)
    c1=sum(eig[i]*np.prod([1-eig[j] for j in range(3) if j!=i]) for i in range(3))
    c2=sum((1-eig[i])*np.prod([eig[j] for j in range(3) if j!=i]) for i in range(3))
    c3=np.prod(eig)
    return eig,cs,np.array([c0,c1,c2,c3]),G,K

families={
    "diffuse_restriction":(0.40,0.30,0.20),
    "heavy_triple":(0.60,0.40,0.30),
    "heavy_pair_leaf":(0.60,0.30,0.10),
    "heavy_singleton_twoleaf":(0.60,0.20,0.10),
}

maxerr=0.0
for name,a in families.items():
    U=make_block_U(a)
    eig,cs,cf,G,K=packet_coefficients(U)
    err=float(np.max(np.abs(cs-cf)))
    maxerr=max(maxerr,err)
    print(name,"eigG",[float(x) for x in eig],"c",[float(x) for x in cs],"err",err,"|K|",len(K))
    if name=="diffuse_restriction":
        assert eig[0] <= 0.5+1e-12
        L=[i for i in range(U.shape[0]) if i not in K]
        GL=np.eye(3)-G
        inv=np.linalg.inv(GL)
        delta=max(float(U[i]@inv@U[i]) for i in L)
        print("  light_restriction_max_leverage",delta)
        assert delta <=1/12+1e-12
    elif name=="heavy_triple":
        assert eig[2]>=0.25-1e-12 and cs[3]>=1/32-1e-12
    elif name=="heavy_pair_leaf":
        assert eig[2]<0.25+1e-12 and eig[1]>=0.25-1e-12 and cs[2]>=3/32-1e-12
    else:
        assert eig[1]<0.25+1e-12 and cs[1]>=9/32-1e-12

print("max_coefficient_error",maxerr)
print("C72_3",math.comb(72,3),"heavy_triple_denominator",32*math.comb(72,3))
print("C72_2",math.comb(72,2),"heavy_pair_leaf_denominator",(32*math.comb(72,2))//3)
print("heavy_singleton_twoleaf_denominator",256)
print("PASS")
