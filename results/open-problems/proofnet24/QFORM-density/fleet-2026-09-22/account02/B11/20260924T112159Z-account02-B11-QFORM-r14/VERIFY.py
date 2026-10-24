import itertools
import math
import numpy as np

rng=np.random.default_rng(1411)

# Check the averaged disjoint-Pluecker identity on a generic 7x3 Parseval frame.
X=rng.normal(size=(7,3))
R=np.linalg.qr(X)[0][:,:3]
triples=list(itertools.combinations(range(7),3))
w={S: float(np.linalg.det(R[list(S),:])**2) for S in triples}
assert abs(sum(w.values())-1)<1e-12
eta=sum(w[S]*w[T] for S in triples for T in triples if set(S).isdisjoint(T))
avg=0.0
mx=0.0
for mask in range(1<<7):
    I=[i for i in range(7) if (mask>>i)&1]
    J=[i for i in range(7) if not ((mask>>i)&1)]
    GI=R[I,:].T@R[I,:] if I else np.zeros((3,3))
    GJ=R[J,:].T@R[J,:] if J else np.zeros((3,3))
    v=float(np.linalg.det(GI)*np.linalg.det(GJ))
    avg += v/(1<<7)
    mx=max(mx,v)
assert abs(avg-eta/64)<2e-14
assert mx+1e-14>=eta/64

# Check the exact coloop family A_m = 1 direct_sum J_m/m direct_sum -J_m/m.
for m in [1,2,3,5,10]:
    Jm=np.ones((m,m))/m
    A=np.zeros((1+2*m,1+2*m))
    A[0,0]=1
    A[1:1+m,1:1+m]=Jm
    A[1+m:,1+m:]=-Jm
    nz=np.linalg.eigvalsh(A)
    nz=nz[np.abs(nz)>1e-10]
    assert np.max(np.abs(np.sort(nz)-np.array([-1.,1.,1.])))<1e-10
    md=0.0
    for S in itertools.combinations(range(1+2*m),3):
        md=max(md,abs(float(np.linalg.det(A[np.ix_(S,S)]))))
    assert abs(md-m**-2)<1e-10

print('eta_random =',repr(eta))
print('average_detGI_detGJ =',repr(avg))
print('eta_over_64 =',repr(eta/64))
print('max_partition_product =',repr(mx))
print('DET49_line_exception_constant =',repr(49*40**(1/3)))
print('partner_coloop_family_constant =',repr(44*2**(2/3)))
print('QFORM_B11_R14_PLUCKER_CHECK_PASS')
