import itertools, math
import numpy as np

C = 16*(math.e/3)**0.25
print(f"lift_constant={C:.15f}")

for r in (2,3,5,10):
    m=2*r
    U=np.zeros((m,2)); V=np.zeros((m,2))
    U[:r,0]=1/math.sqrt(r); U[r:,1]=1/math.sqrt(r)
    V[:r,0]=1/math.sqrt(r); V[r:,1]=1/math.sqrt(r)
    M=U@V.T

    E2=0.0
    roww=np.zeros(m)
    maxdet=0.0
    for P in itertools.combinations(range(m),2):
        for T in itertools.combinations(range(m),2):
            d=float(np.linalg.det(M[np.ix_(P,T)]))
            w=d*d
            E2 += w
            roww[list(P)] += w
            maxdet=max(maxdet, abs(d))
    q=roww/E2

    A=np.zeros((1+2*m,1+2*m))
    A[0,0]=1
    A[1:1+m,1+m:]=M
    A[1+m:,1:1+m]=M.T
    eig=np.linalg.eigvalsh(A)
    nz=eig[np.abs(eig)>1e-9]

    print(f"r={r} E2={E2:.15g} qmax={q.max():.15g} maxdet={maxdet:.15g} eig={nz.tolist()}")
    assert abs(E2-1)<1e-10
    assert q.max() <= 0.5+1e-10
    assert abs(maxdet-r**-2)<1e-10
    assert np.allclose(nz,[-1,-1,1,1,1],atol=1e-9)

print("STATUS=PASS")
