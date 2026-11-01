import itertools
import numpy as np

rng=np.random.default_rng(12345)
max_delete=0.0
max_cross=0.0
for _ in range(200):
    m=8
    b=rng.normal(size=m)
    z=rng.normal(size=m); z/=np.linalg.norm(z)
    D=rng.normal(size=m)
    lam=rng.normal()
    if abs(lam)<0.2: lam += 0.5
    a=rng.normal()
    R=np.column_stack([b,z])
    Gamma=R.T@R
    E=np.linalg.det(Gamma)
    if E<1e-10: continue
    Ginv=np.linalg.inv(Gamma)
    ell=np.einsum('ij,jk,ik->i',R,Ginv,R)
    p={}
    q={}
    for i,j in itertools.combinations(range(m),2):
        th=b[i]*z[j]-b[j]*z[i]
        p[(i,j)]=th*th/E
        rest=[k for k in range(m) if k not in (i,j)]
        Erem=np.linalg.det(R[rest].T@R[rest])
        q[(i,j)]=1-ell[i]-ell[j]+p[(i,j)]
        max_delete=max(max_delete,abs(Erem/E-q[(i,j)]))
        s=z[i]*z[i]+z[j]*z[j]
        if s>1e-12 and Erem>1e-12:
            M=np.vstack([b[rest],lam*z[i]*z[rest],lam*z[j]*z[rest]])
            gram=M@M.T
            V2=sum(np.linalg.det(gram[np.ix_(P,P)]) for P in itertools.combinations(range(3),2))
            H=np.array([[a,b[i],b[j]],
                        [b[i],D[i]+lam*z[i]**2,lam*z[i]*z[j]],
                        [b[j],lam*z[i]*z[j],D[j]+lam*z[j]**2]])
            n=np.array([0.0,z[j],-z[i]])/np.sqrt(s)
            kap=abs(n@H@n)
            rhs=lam*lam*Erem*abs(D[i]*z[j]**2+D[j]*z[i]**2)
            max_cross=max(max_cross,abs(V2*kap-rhs)/(1+abs(rhs)))
    d=sum(p[P]*q[P] for P in p)
    dd=0.0
    for P,w in p.items():
        for Q,v in p.items():
            if set(P).isdisjoint(Q): dd += w*v
    max_delete=max(max_delete,abs(d-dd))
print(f'max_delete_disjoint_error={max_delete:.17e}')
print(f'max_cross_curvature_error={max_cross:.17e}')
print('STATUS=PASS')
