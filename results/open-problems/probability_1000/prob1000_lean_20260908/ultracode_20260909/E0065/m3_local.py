# m=3: local threshold. For a given alpha, maximise the modulus of the non-Perron eigenvalue of A(p)
# (Jacobian of V at fixed point p on the tangent space is 2A(p)) over QSO P with min P >= alpha and V(p)=p.
# Reports separately the best real-negative eigenvalue and the best complex pair (Neimark-Sacker).
import numpy as np, sys, json
from scipy.optimize import minimize
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
m=3
pairs=[(i,j) for i in range(m) for j in range(i,m)]   # 6 pairs
def unpack(v):
    P=np.zeros((m,m,m))
    for t,(i,j) in enumerate(pairs):
        P[i,j,:]=v[3*t:3*t+3]; P[j,i,:]=v[3*t:3*t+3]
    p=np.array([v[18],v[19],1-v[18]-v[19]])
    return P,p
def Amat(P,p): return np.einsum('ijk,j->ki',P,p)   # A[k,i]=sum_j P_ijk p_j (column stochastic)
def V(P,x): return np.einsum('ijk,i,j->k',P,x,x)
def eigs2(P,p):
    A=Amat(P,p); w=np.linalg.eigvals(A)
    w=w[np.argsort(abs(w-1))][1:]   # drop Perron eigenvalue 1
    return w
def obj(v,kind):
    P,p=unpack(v); w=eigs2(P,p)
    if kind=='neg': return -max(-w.real)               # most negative real part
    if kind=='cx':  return -max(abs(w[abs(w.imag)>1e-9])) if (abs(w.imag)>1e-9).any() else 0.0
    return -max(abs(w))
def cons(v):
    P,p=unpack(v)
    c=[v[3*t:3*t+3].sum()-1 for t in range(6)]
    c+= list((V(P,p)-p)[:2])
    return np.array(c)
def solve(alpha,kind,nstart=25):
    best=None
    bnds=[(alpha,1-2*alpha)]*18+[(0.0,1.0)]*2
    for _ in range(nstart):
        v0=np.zeros(20)
        for t in range(6):
            d=rng.dirichlet(np.ones(3)*0.5); v0[3*t:3*t+3]=alpha+(1-3*alpha)*d
        q=rng.dirichlet(np.ones(3)); v0[18:]=q[:2]
        try:
            r=minimize(obj,v0,args=(kind,),method='SLSQP',bounds=bnds,
                       constraints=[{'type':'eq','fun':cons},{'type':'ineq','fun':lambda v:1-v[18]-v[19]}],
                       options={'maxiter':300,'ftol':1e-12})
        except Exception as e: continue
        if r.success and abs(cons(r.x)).max()<1e-8:
            if best is None or r.fun<best.fun: best=r
    return best
for kind in ['neg','cx','all']:
    lo,hi=0.02,0.17
    for it in range(14):
        mid=(lo+hi)/2
        b=solve(mid,kind)
        val=-b.fun if b is not None else 0
        # Jacobian eigenvalue = 2*eig(A): loss of stability at |eig(A)|=1/2
        if val>=0.5: lo=mid; arg=b.x
        else: hi=mid
    print(kind,"local threshold alpha_3 in [%.5f,%.5f]"%(lo,hi))
    b=solve(lo,kind,40)
    P,p=unpack(b.x)
    print(" eigs of A at fixed point:",np.round(eigs2(P,p),5)," p=",np.round(p,5))
    for t,(i,j) in enumerate(pairs): print("  P[%d%d,:]="%(i+1,j+1),np.round(b.x[3*t:3*t+3],5))
    json.dump({'alpha':lo,'x':list(b.x)},open('m3_local_%s.json'%kind,'w'))
    sys.stdout.flush()
