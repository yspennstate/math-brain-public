import json, math
import numpy as np
from scipy.optimize import minimize

SEED=20260916143900
rng=np.random.default_rng(SEED)

def adj3(A):
    return A@A-np.trace(A)*A+0.5*(np.trace(A)**2-np.trace(A@A))*np.eye(3,dtype=complex)

def atoms(K):
    out=[]
    for mask in range(8):
        D=np.diag([0.0 if ((mask>>i)&1) else 1.0 for i in range(3)])
        Q=K-D
        out.append(float(np.real(((-1)**(3-mask.bit_count()))*np.linalg.det(Q))))
    return np.array(out)

def score(K):
    p=atoms(K)
    if not np.all(np.isfinite(p)) or p.min()<=1e-13:
        return None
    c=np.array([
        math.log(p[2]*p[4]/(p[0]*p[6])),
        math.log(p[1]*p[4]/(p[0]*p[5])),
        math.log(p[1]*p[2]/(p[0]*p[3]))])
    tau=math.log(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
    M=np.diag(c)+tau*K
    d=float(np.real(np.linalg.det(M)))
    if not np.isfinite(d) or d<=1e-11: return None
    Es=[]
    for mask in range(1,8):
        D=np.diag([0.0 if ((mask>>i)&1) else 1.0 for i in range(3)])
        Q=K-D
        Es.append(((-1)**(3-mask.bit_count()))*adj3(Q))
    pp=p[1:]
    V=np.diag(pp)-np.outer(pp,pp)
    T=np.array([[np.real(np.trace(M@Es[i]@M@Es[j])) for j in range(7)] for i in range(7)])
    v=np.array([np.real(np.trace(M@e)) for e in Es])
    C=T+d*V
    try: a=np.linalg.solve(C,v)
    except np.linalg.LinAlgError: return None
    s=float(v@a); detC=float(np.real(np.linalg.det(C)))
    if not np.isfinite(s) or detC<=0: return None
    return dict(margin=s-2.0,phi=detC*(s-2.0),detC=detC,
                atoms=p.tolist(),eigenvalues=np.linalg.eigvalsh(K).tolist(),
                tau=tau,c=c.tolist(),d=d)

def params_to_K(x):
    # Positive odds L=T T*, then K=L(I+L)^-1. This automatically stays 0<K<I.
    T=np.zeros((3,3),dtype=complex)
    T[0,0]=math.exp(x[0]); T[1,1]=math.exp(x[1]); T[2,2]=math.exp(x[2])
    T[1,0]=x[3]+1j*x[4]; T[2,0]=x[5]+1j*x[6]; T[2,1]=x[7]+1j*x[8]
    L=T@T.conj().T
    return np.linalg.solve(np.eye(3)+L,L).T.conj()

def K_to_params(K):
    L=K@np.linalg.inv(np.eye(3)-K)
    L=(L+L.conj().T)/2
    T=np.linalg.cholesky(L)
    return np.array([math.log(T[0,0].real),math.log(T[1,1].real),math.log(T[2,2].real),
                     T[1,0].real,T[1,0].imag,T[2,0].real,T[2,0].imag,
                     T[2,1].real,T[2,1].imag])

def objective(x):
    try:r=score(params_to_K(x))
    except Exception:return 1e3
    if r is None:return 1e3
    return r['margin']

# Prior exact PROB20 witness, searched in both orientations.
K0=np.array([
[.3898,-.2921-.1627j,.0521-.3138j],
[-.2921+.1627j,.4515,-.0975+.0809j],
[.0521+.3138j,-.0975-.0809j,.6657]],complex)
seeds=[K_to_params(K0),K_to_params(np.eye(3)-K0)]
for i in range(14):
    base=seeds[i%2]
    seeds.append(base+rng.normal(0,0.8,size=9))

best=None; local=[]
for idx,x0 in enumerate(seeds):
    x0=np.clip(x0,-8.5,8.5)
    res=minimize(objective,x0,method='Powell',bounds=[(-9,9)]*9,
                 options={'maxiter':500,'xtol':1e-7,'ftol':1e-10,'disp':False})
    rec=score(params_to_K(res.x))
    if rec is not None:
        local.append({'start':idx,'success':bool(res.success),'nfev':int(res.nfev),
                      'margin':rec['margin'],'phi':rec['phi'],
                      'eigenvalues':rec['eigenvalues'],'min_atom':min(rec['atoms'])})
        if best is None or rec['margin']<best['margin']: best=rec

neg=[]; used=0
for _ in range(5000):
    x=np.r_[rng.uniform(-4,4,3),rng.normal(0,2,6)]
    r=score(params_to_K(x))
    if r is None: continue
    used+=1
    if best is None or r['margin']<best['margin']: best=r
    if r['margin'] < -1e-8: neg.append(r)

out={'status':'NUMERICAL_DIAGNOSTIC_ONLY','seed':SEED,
     'sampler':'odds Cholesky; 16 Powell starts + 5000 broad draws; distinct from P11 eigenvalue+Haar probe',
     'accepted_broad':used,'negative_count':len(neg),'best':best,
     'local_runs':local,'global_certificate':False}
print(json.dumps(out,indent=2))
