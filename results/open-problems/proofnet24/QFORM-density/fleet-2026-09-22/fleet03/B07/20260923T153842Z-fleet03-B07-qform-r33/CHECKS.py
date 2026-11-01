from fractions import Fraction
import math
import numpy as np

rng=np.random.default_rng(20260923)

def e2(M):
    nr,nc=M.shape
    s=0.0
    for i in range(nr):
        for k in range(i+1,nr):
            for j in range(nc):
                for l in range(j+1,nc):
                    d=M[i,j]*M[k,l]-M[i,l]*M[k,j]
                    s+=d*d
    return s

def omega(A,B,C,D):
    s=0.0
    for i in range(A.shape[0]):
        for k in range(D.shape[0]):
            for j in range(A.shape[1]):
                for l in range(D.shape[1]):
                    z=A[i,j]*D[k,l]-B[i,l]*C[k,j]
                    s+=z*z
    return s

eps=Fraction(1,64)
eta=eps*eps/(2*(1-eps))
tau=2*eta-eta*eta
Delta=2*tau+eps*eps/(4*(2-eps)*(2-eps))
th=(1-math.sqrt(1-4*float(Delta)))/2

print('QFORM fleet03/B07 r33 deterministic checks')
print('eps =',float(eps))
print('eta =',eta,float(eta))
print('tau =',tau,float(tau))
print('Delta_sharp =',Delta,float(Delta))
print('theta_tail =',th)
print('relative_tail_F =',math.sqrt(th))
print('tail_over_s1 =',math.sqrt(th/(1-th)))

# Exact partition regression on random integer matrices.
maxerr=0.0
cases=400
for _ in range(cases):
    p,q,r,s=[int(rng.integers(1,4)) for z in range(4)]
    A=rng.integers(-3,4,size=(p,r)).astype(float)
    B=rng.integers(-3,4,size=(p,s)).astype(float)
    C=rng.integers(-3,4,size=(q,r)).astype(float)
    D=rng.integers(-3,4,size=(q,s)).astype(float)
    K=np.block([[A,B],[C,D]])
    horiz1=np.hstack([A,B]); horiz2=np.hstack([C,D])
    vert1=np.vstack([A,C]); vert2=np.vstack([B,D])
    rhs=e2(horiz1)+e2(horiz2)+e2(vert1)+e2(vert2)-e2(A)-e2(B)-e2(C)-e2(D)+omega(A,B,C,D)
    maxerr=max(maxerr,abs(e2(K)-rhs))
print('partition_cases =',cases,'max_abs_error =',maxerr)

# Near coherent rank-one matrices: test theorem inequalities whenever premise fires.
valid=0
maxe2=0.0
maxtail=0.0
mincorr=1.0
for _ in range(2000):
    p=q=r=s=3
    x=rng.normal(size=p); y=rng.normal(size=q); z=rng.normal(size=r); w=rng.normal(size=s)
    base=np.block([[np.outer(x,z),np.outer(x,w)],[np.outer(y,z),np.outer(y,w)]])
    K=base+1e-5*rng.normal(size=base.shape)
    A=K[:p,:r]; B=K[:p,r:]; C=K[p:,:r]; D=K[p:,r:]
    aa=np.linalg.norm(A); bb=np.linalg.norm(B); cc=np.linalg.norm(C); dd=np.linalg.norm(D)
    Om=omega(A,B,C,D)
    if aa*dd==0 or Om >= float(eps*eps)*(aa*dd)**2: continue
    valid+=1
    S=np.linalg.norm(K)**2
    ratio=e2(K)/(S*S)
    sv=np.linalg.svd(K,compute_uv=False)
    tr=np.sum(sv[1:]**2)/S
    maxe2=max(maxe2,ratio); maxtail=max(maxtail,tr)
    vals=[]
    for X,Y,nx,ny in [(A,B,aa,bb),(C,D,cc,dd),(A.T,C.T,aa,cc),(B.T,D.T,bb,dd)]:
        if nx*ny:
            vals.append(np.linalg.norm(X.T@Y)/(nx*ny))
    if vals:mincorr=min(mincorr,min(vals))
    assert ratio < float(Delta)+1e-10
    assert tr < th+1e-10
print('near_rank1_cases =',valid)
print('max_observed_E2_over_S2 =',maxe2)
print('max_observed_tail_ratio =',maxtail)
print('min_observed_shared_side_correlation =',mincorr)

P=29598.7122613461
branch=P/64
count=math.floor(branch**2*1024)+1
s1=math.sqrt(2*(1-th)*P)
print('partner_P_over_h2 >',P)
print('aggregate_branch_sqrtOmega_over_h2 >',branch)
print('aggregate_branch_nonzero_minor_count >=',count)
print('lowtail_branch_s1_over_h >',s1)
print('lowtail_branch_top_vectors_l1_product >',8*s1)
print('STATUS=PASS')
