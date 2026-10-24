import numpy as np, math, json, time
rng=np.random.default_rng(20260916180932)

def adj3(A):
    a,b,c=A[0]; d,e,f=A[1]; g,h,i=A[2]
    return np.array([[e*i-f*h, c*h-b*i, b*f-c*e],
                     [f*g-d*i, a*i-c*g, c*d-a*f],
                     [d*h-e*g, b*g-a*h, a*e-b*d]], dtype=complex)

def atom_data(K):
    p=np.empty(8); Es=[]
    for mask in range(8):
        D=np.diag([0.0 if (mask>>j)&1 else 1.0 for j in range(3)])
        Q=K-D
        sign=(-1)**(3-int(mask).bit_count())
        p[mask]=float(np.real(sign*np.linalg.det(Q)))
        if mask: Es.append(sign*adj3(Q))
    return p,Es

def score(K):
    ev=np.linalg.eigvalsh(K)
    if ev[0] <= 1e-12 or ev[-1] >= 1-1e-12: return None
    p,Es=atom_data(K)
    if p.min() <= 2e-13: return None
    c=np.array([
        math.log(p[2]*p[4]/(p[0]*p[6])),
        math.log(p[1]*p[4]/(p[0]*p[5])),
        math.log(p[1]*p[2]/(p[0]*p[3]))])
    tau=math.log(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
    M=np.diag(c)+tau*K
    d=float(np.real(np.linalg.det(M)))
    if d <= 1e-14: return None
    pp=p[1:]; V=np.diag(pp)-np.outer(pp,pp)
    T=np.empty((7,7)); v=np.empty(7)
    for i,E in enumerate(Es):
        v[i]=float(np.real(np.trace(M@E)))
        for j,F in enumerate(Es):
            T[i,j]=float(np.real(np.trace(M@E@M@F)))
    C=(T+T.T)/2+d*V
    try:
        if np.linalg.eigvalsh(C)[0] <= 1e-13: return None
        a=np.linalg.solve(C,v)
    except np.linalg.LinAlgError:
        return None
    margin=float(v@a)-2.0
    detC=float(np.linalg.det(C))
    return {'margin':margin,'phi':detC*margin,'detC':detC,'tau':tau,
            'eigenvalues':ev.tolist(),'atoms':p.tolist()}

def randU():
    Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    Q,R=np.linalg.qr(Z)
    ph=np.diag(R); ph=np.where(np.abs(ph)>0,ph/np.abs(ph),1)
    return Q@np.diag(np.conjugate(ph))

def run(mode,n=10000):
    best=None; accepted=0; neg=[]
    for _ in range(n):
        if mode=='generic':
            lam=rng.uniform(0.002,0.998,3)
        elif mode=='boundary':
            z=rng.normal(0,5.0,3)
            lam=1/(1+np.exp(-z)); lam=np.clip(lam,2e-10,1-2e-10)
        else:
            lam=np.array([10**rng.uniform(-9,-2), rng.uniform(0.01,0.99),
                          1-10**rng.uniform(-9,-2)])
        U=randU(); K=U@np.diag(lam)@U.conj().T
        r=score(K)
        if r is None: continue
        accepted+=1
        rec={'K':[[[float(z.real),float(z.imag)] for z in row] for row in K],**r}
        if best is None or rec['margin']<best['margin']: best=rec
        if rec['margin'] < -1e-8:
            neg.append(rec)
            if len(neg)>=20: break
    return {'requested':n,'accepted':accepted,'negative_count':len(neg),'best':best,'negatives':neg}

t0=time.time()
out={'status':'NUMERICAL_DIAGNOSTIC_ONLY','seed':20260916180932,
     'formula':'X095 normalized margin s-2, Phi=det(C)*(s-2)',
     'global_certificate':False,
     'generic':run('generic'), 'boundary_biased':run('boundary'),
     'mixed_boundary':run('mixed')}
out['seconds']=time.time()-t0
print(json.dumps(out,indent=2))
