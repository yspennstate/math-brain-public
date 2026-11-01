import json, math
import numpy as np

SEED=20260916164025
rng=np.random.default_rng(SEED)

def adj3(A):
    out=np.zeros((3,3),dtype=complex)
    for i in range(3):
        for j in range(3):
            minor=np.delete(np.delete(A,j,axis=0),i,axis=1)
            out[i,j]=((-1)**(i+j))*np.linalg.det(minor)
    return out

def atoms(K):
    p=[]
    for mask in range(8):
        D=np.diag([0.0 if (mask>>i)&1 else 1.0 for i in range(3)])
        Q=K-D
        p.append(float(np.real(((-1)**(3-mask.bit_count()))*np.linalg.det(Q))))
    return np.array(p)

def score(K):
    p=atoms(K)
    if p.min() <= 1e-14:
        return None
    c=np.array([
      math.log(p[2]*p[4]/(p[0]*p[6])),
      math.log(p[1]*p[4]/(p[0]*p[5])),
      math.log(p[1]*p[2]/(p[0]*p[3]))])
    tau=math.log(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
    M=np.diag(c)+tau*K
    d=float(np.real(np.linalg.det(M)))
    if d <= 1e-12:
        return None
    Es=[]
    for mask in range(1,8):
        D=np.diag([0.0 if (mask>>i)&1 else 1.0 for i in range(3)])
        Q=K-D
        Es.append(((-1)**(3-mask.bit_count()))*adj3(Q))
    pp=p[1:]
    V=np.diag(pp)-np.outer(pp,pp)
    T=np.array([[np.real(np.trace(M@Es[i]@M@Es[j])) for j in range(7)] for i in range(7)])
    v=np.array([np.real(np.trace(M@e)) for e in Es])
    C=T+d*V
    try:
        a=np.linalg.solve(C,v)
    except np.linalg.LinAlgError:
        return None
    s=float(v@a)
    detC=float(np.real(np.linalg.det(C)))
    return {'margin':s-2.0,'phi':detC*(s-2.0),'detC':detC,'atoms':p.tolist(),'c':c.tolist(),'tau':tau,'d':d}

def randU():
    Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    Q,R=np.linalg.qr(Z)
    ph=np.diag(R)
    ph=np.where(np.abs(ph)>0,ph/np.abs(ph),1.0)
    return Q@np.diag(np.conjugate(ph))

def run(mode,n):
    best=None; used=0; negatives=[]
    for _ in range(n):
        if mode=='generic':
            lam=rng.uniform(0.01,0.99,3)
        else:
            z=rng.normal(0,3.8,3)
            lam=1/(1+np.exp(-z))
            lam=np.clip(lam,1e-7,1-1e-7)
        U=randU(); K=U@np.diag(lam)@U.conj().T
        r=score(K)
        if r is None: continue
        used+=1
        rec={'eigenvalues':np.linalg.eigvalsh(K).tolist(),**r}
        if best is None or rec['margin']<best['margin']: best=rec
        if rec['margin'] < -1e-9: negatives.append(rec)
    return {'requested':n,'used':used,'negative_count':len(negatives),'best':best,'negatives':negatives[:20]}

out={'status':'NUMERICAL_DIAGNOSTIC_ONLY','seed':SEED,
     'formula':'X095 normalized margin s-2 where Phi=det(C)*(s-2) and det(C)>0 on the strict connected domain',
     'generic':run('generic',10000),'boundary_biased':run('boundary',10000),
     'global_certificate':False}
print(json.dumps(out,indent=2))
