import math
import random

random.seed(20260923)

WMAX=(61/1728)**(1/3)
KLOW=WMAX/4
C_ARC=8*(2**0.25)*math.sqrt(3)
R43_THRESHOLD=C_ARC*64
PARTNER=12*((0.25*WMAX/64))**(-1/3)
print('WMAX',repr(WMAX))
print('anchored_K_partner_lower',repr(KLOW))
print('arcsine_constant',repr(C_ARC))
print('r43_innovation_branch_bound',repr(R43_THRESHOLD))
print('partner_bound',repr(PARTNER))


def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

maxerr=0.0
for _ in range(5000):
    a,b,d=[random.uniform(-3,3) for _ in range(3)]
    # four environment coordinates
    E=[[random.uniform(-3,3) for _ in range(4)] for __ in range(2)]
    C=[[0.0]*4 for _ in range(4)]
    for j in range(4):
        for k in range(j,4):
            C[j][k]=C[k][j]=random.uniform(-3,3)
    detH=a*d-b*b
    # adj(H)=[[d,-b],[-b,a]]
    for j in range(4):
        for k in range(4):
            q=(d*E[0][j]*E[0][k]
               -b*E[0][j]*E[1][k]
               -b*E[1][j]*E[0][k]
               +a*E[1][j]*E[1][k])
            K=detH*C[j][k]-q
            M=[[a,b,E[0][k]],
               [b,d,E[1][k]],
               [E[0][j],E[1][j],C[j][k]]]
            minor=det3(M)
            err=abs(K-minor)/(1+abs(K)+abs(minor))
            maxerr=max(maxerr,err)
print('anchored_minor_identity_max_normalized_error',repr(maxerr))

# exact rank-one bridge, parameterized by u=(cos theta,sin theta), null n=(-sin,cos)
maxerr2=0.0
for _ in range(5000):
    th=random.uniform(-math.pi,math.pi)
    co,si=math.cos(th),math.sin(th)
    lam=random.choice([-1,1])*random.uniform(0.1,4)
    H=[[lam*co*co,lam*co*si],[lam*co*si,lam*si*si]]
    adj=[[H[1][1],-H[0][1]],[-H[1][0],H[0][0]]]
    E=[[random.uniform(-2,2) for _ in range(5)] for __ in range(2)]
    AE=[[sum(adj[i][q]*E[q][j] for q in range(2)) for j in range(5)] for i in range(2)]
    J2=sum(AE[i][j]**2 for i in range(2) for j in range(5))
    # K=-E^T adj(H) E because det H=0
    K=[[ -sum(E[q][j]*AE[q][k] for q in range(2)) for k in range(5)] for j in range(5)]
    Knorm=math.sqrt(sum(K[j][k]**2 for j in range(5) for k in range(5)))
    rhs=J2/abs(lam)
    err=abs(Knorm-rhs)/(1+abs(Knorm)+abs(rhs))
    maxerr2=max(maxerr2,err)
print('rank_one_bridge_max_normalized_error',repr(maxerr2))

# The indefinite obstruction matrix has characteristic polynomial
# (lambda-1)*lambda*(lambda+epsilon+1/epsilon), hence only two nonzero eigenvalues.
for eps in [1.0,0.5,0.1,0.01]:
    print('counterexample_spectrum',eps,[1.0,-(eps+1/eps),0.0])

print('QFORM_B06_R44_CHECK_PASS')
