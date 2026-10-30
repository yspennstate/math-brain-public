import numpy as np, math, itertools

def H(n):
    a=np.array([[1.0]])
    while len(a)<n:
        a=np.block([[a,a],[a,-a]])
    return a/math.sqrt(n)

for m in (4,8,16):
    h=H(m); u1,u2=h[:,0],h[:,1]; v1,v2=h[:,0],h[:,1]
    w=np.ones(m)/math.sqrt(m); r=w.copy()
    K=np.outer(u1,v1)+np.outer(u2,v2)
    A=np.zeros((4*m,4*m))
    A[:m,m:2*m]=K; A[m:2*m,:m]=K.T
    A[2*m:3*m,3*m:]=np.outer(w,r); A[3*m:,2*m:3*m]=np.outer(r,w)
    eig=np.linalg.eigvalsh(A); nz=eig[np.abs(eig)>1e-9]
    md=max(abs(A[i,i]*A[j,j]-A[i,j]**2) for i,j in itertools.combinations(range(4*m),2))
    sv=np.linalg.svd(K,compute_uv=False)
    print('m',m,'nonzero_eigs',np.round(nz,12).tolist(),'cross_sv',np.round(sv[:2],12).tolist(),'max_pair_det',md)
    assert np.allclose(nz,[-1,-1,-1,1,1,1])
    assert np.allclose(sv[:2],[1,1])
    assert md <= 4/m**2 + 1e-12
print('new_bound',6.0)
print('Theorem_D_bound',6*math.sqrt(math.e))
print('scalar_cap1_bound',3*2**(2/3))
for eps in (1.0,0.1,0.001):
    A=np.zeros((8,8)); A[0,4]=A[4,0]=1; A[1,5]=A[5,1]=1; A[2,2]=A[3,3]=eps; A[6,7]=A[7,6]=1
    pe=3*(math.pi/2)**(1/3)*eps**(-1/3)
    print('eps',eps,'eigs',np.linalg.eigvalsh(A).tolist(),'partner_bound',pe)
print('STATUS=PASS')
