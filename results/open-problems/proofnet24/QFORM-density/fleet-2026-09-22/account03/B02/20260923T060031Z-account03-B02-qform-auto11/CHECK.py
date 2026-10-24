import numpy as np

rng = np.random.default_rng(20260923)

def E2(M):
    s = np.linalg.svd(M, compute_uv=False)
    return sum((s[i]*s[j])**2 for i in range(len(s)) for j in range(i+1,len(s)))

max_Tx=max_projx=max_Ty=max_projy=0.0
min_gapx=min_gapy=float('inf')
count=0
for _ in range(2000):
    nU=int(rng.integers(2,7)); nV=int(rng.integers(2,7))
    d,e,a=rng.normal(size=3); delta=d*e-a*a
    if abs(d)<0.15 or abs(e)<0.15 or abs(delta)<0.15:
        continue
    u=rng.normal(size=nU); c=rng.normal(size=nU)
    r=rng.normal(size=nV); v=rng.normal(size=nV)
    N=rng.normal(size=(nU,nV))
    P=np.array([[d,a],[a,e]])
    T=N-np.c_[u,c]@np.linalg.inv(P)@np.vstack([r,v])
    xi=a*u-d*c; eta=a*v-e*r

    Kx=N-np.outer(u,r)/d; w=(d*v-a*r)/d
    Tx=Kx+np.outer(xi,w)/delta
    max_Tx=max(max_Tx,float(np.linalg.norm(T-Tx)))
    if np.linalg.norm(xi)>1e-10:
        Px=np.eye(nU)-np.outer(xi,xi)/np.dot(xi,xi)
        max_projx=max(max_projx,float(np.linalg.norm(Px@Kx-Px@T)))
        Cx=np.vstack([(-xi/d)[None,:],Kx.T])
        lower=np.dot(xi,xi)/d**2*np.linalg.norm(Px@Kx,'fro')**2
        min_gapx=min(min_gapx,E2(Cx)-lower)

    Ky=N-np.outer(c,v)/e; z=(e*u-a*c)/e
    Ty=Ky+np.outer(z,eta)/delta
    max_Ty=max(max_Ty,float(np.linalg.norm(T-Ty)))
    if np.linalg.norm(eta)>1e-10:
        Py=np.eye(nV)-np.outer(eta,eta)/np.dot(eta,eta)
        max_projy=max(max_projy,float(np.linalg.norm(Ky@Py-T@Py)))
        Cy=np.vstack([(-eta/e)[None,:],Ky])
        lower=np.dot(eta,eta)/e**2*np.linalg.norm(Ky@Py,'fro')**2
        min_gapy=min(min_gapy,E2(Cy)-lower)
    count += 1

print('accepted_cases', count)
print('max_Tx_identity_error', repr(max_Tx))
print('max_x_projection_error', repr(max_projx))
print('min_E2_minus_incident_lower_x', repr(min_gapx))
print('max_Ty_identity_error', repr(max_Ty))
print('max_y_projection_error', repr(max_projy))
print('min_E2_minus_incident_lower_y', repr(min_gapy))
