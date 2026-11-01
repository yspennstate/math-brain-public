#!/usr/bin/env python3
# NUMERICAL_DIAGNOSTIC_ONLY. This is not a global certificate.
import numpy as np, math

SEED=20260916173934
rng=np.random.default_rng(SEED)
NONEMPTY=list(range(1,8))
W=np.array([
    [1 if (S&1) else 0 for S in NONEMPTY],
    [1 if (S&2) else 0 for S in NONEMPTY],
    [1 if (S&4) else 0 for S in NONEMPTY],
    [-1 for S in NONEMPTY],
    [1 if S==7 else 0 for S in NONEMPTY],
    [1 if (S&3)==3 else 0 for S in NONEMPTY],
    [1 if (S&5)==5 else 0 for S in NONEMPTY],
], dtype=float)

def adjugate3(A):
    out=np.empty((3,3),dtype=complex)
    for i in range(3):
        for j in range(3):
            rows=[r for r in range(3) if r!=j]
            cols=[c for c in range(3) if c!=i]
            out[i,j]=((-1)**(i+j))*np.linalg.det(A[np.ix_(rows,cols)])
    return out

def atom_and_E(K):
    ps=[]; Es={}
    for S in range(8):
        A=K.copy()
        for i in range(3):
            if not (S&(1<<i)):
                A[i,i]-=1
        sign=(-1)**(3-bin(S).count("1"))
        ps.append((sign*np.linalg.det(A)).real)
        if S:
            Es[S]=sign*adjugate3(A)
    return np.array(ps), Es

def x095_eval(K):
    ps,Es=atom_and_E(K)
    if np.min(ps)<=1e-12 or abs(ps.sum()-1)>1e-7:
        return None
    p0,p1,p2,p12,p3,p13,p23,p123=ps
    c=np.array([
        math.log(p2*p3/(p0*p23)),
        math.log(p1*p3/(p0*p13)),
        math.log(p1*p2/(p0*p12)),
    ])
    tau=math.log(p0*p12*p13*p23/(p1*p2*p3*p123))
    M=np.diag(c).astype(complex)+tau*K
    d=np.linalg.det(M).real
    if d<=1e-12:
        return None
    E=[Es[S] for S in NONEMPTY]
    v=np.array([np.trace(M@e).real for e in E])
    T=np.array([[np.trace(M@ea@M@eb).real for eb in E] for ea in E])
    pn=ps[1:]
    V=np.diag(pn)-np.outer(pn,pn)
    C=T+d*V
    C=(C+C.T)/2
    try:
        if np.linalg.eigvalsh(C)[0]<=1e-10:
            return None
        s=float(v@np.linalg.solve(C,v))
        Ct=W@C@W.T
        vt=W@v
        A=Ct[:5,:5]
        if np.linalg.eigvalsh((A+A.T)/2)[0]<=1e-10:
            return None
        a5=float(vt[:5]@np.linalg.solve(A,vt[:5]))
    except np.linalg.LinAlgError:
        return None
    return float(s-2), float(a5), float(np.min(ps))

def random_unitary():
    Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    Q,R=np.linalg.qr(Z)
    phases=np.diag(R)
    phases=np.where(np.abs(phases)>0,phases/np.abs(phases),1)
    return Q@np.diag(np.conj(phases))

def eigs(regime):
    if regime=="generic":
        return rng.uniform(0.005,0.995,size=3)
    z=rng.uniform(-11,11,size=3)
    return np.clip(1/(1+np.exp(-z)),1e-7,1-1e-7)

def run(regime,n):
    acc=rej=neg=fail5=0
    min_margin=(float("inf"),None,None)
    min_a5=(float("inf"),None,None)
    for _ in range(n):
        lam=eigs(regime)
        U=random_unitary()
        K=U@np.diag(lam)@U.conj().T
        out=x095_eval(K)
        if out is None:
            rej+=1
            continue
        margin,a5,minatom=out
        acc+=1
        neg += int(margin < -1e-8)
        fail5 += int(a5 < 2-1e-8)
        if margin < min_margin[0]:
            min_margin=(margin,lam.copy(),minatom)
        if a5 < min_a5[0]:
            min_a5=(a5,lam.copy(),minatom)
    print("regime="+regime)
    print("requested="+str(n))
    print("accepted="+str(acc))
    print("rejected_conditioning="+str(rej))
    print("robust_negative_Phi_directions="+str(neg))
    print("five_feature_failures="+str(fail5))
    print("min_s_minus_2="+repr(min_margin[0]))
    print("min_s_eigenvalues="+repr(min_margin[1].tolist()))
    print("min_s_min_atom="+repr(min_margin[2]))
    print("min_five_feature_s="+repr(min_a5[0]))
    print("min_five_feature_eigenvalues="+repr(min_a5[1].tolist()))
    print("min_five_feature_min_atom="+repr(min_a5[2]))

print("NUMERICAL_DIAGNOSTIC_ONLY")
print("GLOBAL_CERTIFICATE=false")
print("seed="+str(SEED))
run("generic",20000)
run("boundary_logit",30000)
print("NEGATIVE_CANDIDATES_FOR_EXACT_FOLLOWUP=0")
