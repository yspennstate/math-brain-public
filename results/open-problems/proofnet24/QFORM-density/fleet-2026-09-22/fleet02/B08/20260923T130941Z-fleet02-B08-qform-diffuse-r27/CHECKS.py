import math
import numpy as np


def sylvester(n):
    H=np.array([[1.0]])
    while H.shape[0]<n:
        H=np.block([[H,H],[H,-H]])
    return H/math.sqrt(n)

beta=3/16*math.sqrt(3/5)
c=0.5*math.sqrt(3/5)
gamma=beta/64
Ctail=9*math.sqrt(3)*math.e/2
assert abs(4*Ctail/beta-480*math.e/math.sqrt(5))<1e-12
assert 4*Ctail/beta<584
C11=3*4**(2/3)
assert C11*c**(-1/3)*(beta/2)**(-2/3)<60
C21=(20/3)*2**(-4/5)
assert C21<3.829

for m in (8,16,32,64):
    U=sylvester(m)[:,:3]
    u1,u2,u3=U[:,0],U[:,1],U[:,2]

    # High-leverage actual k=1 target paid by fleet03/B08 r37.
    C=np.column_stack([u2,u3])
    A_hub=np.block([[np.diag([1.,0.]),C.T],[C,np.outer(u1,u1)]])
    nz=np.linalg.eigvalsh(A_hub)
    nz=nz[np.abs(nz)>1e-9]
    expected=np.array([-1.,(1-math.sqrt(5))/2,1.,1.,(1+math.sqrt(5))/2])
    assert np.max(np.abs(np.sort(nz)-np.sort(expected)))<1e-10
    assert np.max(np.abs(np.linalg.svd(C,compute_uv=False)-np.array([1.,1.])))<1e-10
    assert np.max(np.sum(U**2,axis=1)) <= 0.5+1e-12

    # Exact rank-two diffuse hybrid.
    B=np.outer(u2,u2)+np.outer(u3,u3)
    A_diff=np.block([[np.outer(u1,u1),B],[B,np.outer(u1,u1)]])
    nz2=np.linalg.eigvalsh(A_diff)
    nz2=nz2[np.abs(nz2)>1e-9]
    assert np.max(np.abs(np.sort(nz2)-np.array([-1.,-1.,1.,1.,1.,1.])))<1e-10
    assert np.max(np.diag(np.column_stack([u2,u3])@np.column_stack([u2,u3]).T)) <= 0.5+1e-12

    # Natural one-hub r37 certificate: G=2/m and exact bound 6 m^(1/3).
    g=B[:,0]
    G1=float(g@g)
    assert abs(G1-2/m)<1e-12
    lev1=np.max((g/math.sqrt(G1))**2+u1**2)
    assert lev1<=0.5+1e-12
    b1=C11*G1**(-1/3)
    assert abs(b1-6*m**(1/3))<1e-10

    # An independent two-hub choice has det G=4/m^2 and augmented leverage 3/m.
    found=False
    for i in range(m):
        for j in range(i+1,m):
            Cp=B[:,[i,j]]
            G=Cp.T@Cp
            if np.linalg.det(G)>1e-12:
                detG=float(np.linalg.det(G))
                assert abs(detG-4/m**2)<1e-10
                w,V=np.linalg.eigh(G)
                Ug=Cp@(V@np.diag(w**-0.5)@V.T)
                lev2=np.max(np.sum(Ug**2,axis=1)+u1**2)
                assert abs(lev2-3/m)<1e-10
                found=True
                break
        if found:
            break
    assert found

print('beta=',repr(beta))
print('c=',repr(c))
print('gamma=',repr(gamma))
print('tail_router_constant=',repr(4*Ctail/beta))
print('heavy_row_partner_constant=',repr(C11*c**(-1/3)*(beta/2)**(-2/3)))
print('two_hub_target_partner_constant=',repr(C21))
print('QFORM_B08_R27_CHECK_PASS')
