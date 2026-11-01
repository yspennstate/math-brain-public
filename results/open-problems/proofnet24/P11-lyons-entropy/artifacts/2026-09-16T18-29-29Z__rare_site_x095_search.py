#!/usr/bin/env python3
# NUMERICAL_DIAGNOSTIC_ONLY. This is not a global certificate.
import numpy as np, math
rng=np.random.default_rng(20260916181406)
NONEMPTY=list(range(1,8))

def adj3(A):
    out=np.empty((3,3),complex)
    for i in range(3):
      for j in range(3):
        rows=[r for r in range(3) if r!=j]; cols=[c for c in range(3) if c!=i]
        out[i,j]=((-1)**(i+j))*np.linalg.det(A[np.ix_(rows,cols)])
    return out

def evalx(K):
    ps=[]; Es=[]
    for S in range(8):
      A=K.copy()
      for i in range(3):
        if not (S>>i)&1: A[i,i]-=1
      sg=(-1)**(3-S.bit_count())
      ps.append((sg*np.linalg.det(A)).real)
      if S: Es.append(sg*adj3(A))
    ps=np.array(ps)
    if ps.min()<1e-13 or abs(ps.sum()-1)>1e-7: return None
    p0,p1,p2,p12,p3,p13,p23,p123=ps
    try:
      cs=np.array([math.log(p2*p3/(p0*p23)),math.log(p1*p3/(p0*p13)),math.log(p1*p2/(p0*p12))])
      tau=math.log(p0*p12*p13*p23/(p1*p2*p3*p123))
      M=np.diag(cs).astype(complex)+tau*K
      d=np.linalg.det(M).real
      if d<=1e-15: return None
      v=np.array([np.trace(M@E).real for E in Es])
      T=np.array([[np.trace(M@Ea@M@Eb).real for Eb in Es] for Ea in Es])
      pn=ps[1:]; V=np.diag(pn)-np.outer(pn,pn)
      C=(T+d*V); C=(C+C.T)/2
      ev=np.linalg.eigvalsh(C)
      if ev[0]<=1e-15: return None
      s=float(v@np.linalg.solve(C,v))
      return s-2,ps.min(),np.linalg.eigvalsh(K)
    except Exception: return None

def random_B():
    lam=np.sort(rng.uniform(.08,.92,2))
    th=rng.uniform(0,np.pi/2); ph=rng.uniform(0,2*np.pi)
    U=np.array([[np.cos(th),-np.sin(th)*np.exp(1j*ph)],[np.sin(th)*np.exp(-1j*ph),np.cos(th)]])
    return U@np.diag(lam)@U.conj().T

mins=(1e9,None); acc=neg=0
for _ in range(5000):
    B=random_B()
    if abs(B[0,1])<1e-3: continue
    a=rng.uniform(.15,1.5)
    vals,U=np.linalg.eigh(B)
    Bs=U@np.diag(np.sqrt(vals))@U.conj().T
    vv=rng.normal(size=2)+1j*rng.normal(size=2); vv/=np.linalg.norm(vv)
    theta=rng.uniform(.02,.75)
    z=np.sqrt(a*theta)*(Bs@vv)
    X=np.outer(z,z.conj())/a
    if np.linalg.eigvalsh(B-X)[0]<1e-4: continue
    eps=10**rng.uniform(-7,-1.2)
    K=np.block([[np.array([[eps*a]]), np.sqrt(eps)*z.conj()[None,:]], [np.sqrt(eps)*z[:,None],B]])
    ev=np.linalg.eigvalsh(K)
    if ev[0]<=0 or ev[-1]>=1: continue
    out=evalx(K)
    if out is None: continue
    acc+=1; margin=out[0]
    if margin < -1e-8: neg+=1
    if margin<mins[0]: mins=(margin,(eps,a,B,z,out[1],out[2]))
print('NUMERICAL_DIAGNOSTIC_ONLY')
print('GLOBAL_CERTIFICATE=false')
print('seed=20260916181406')
print('accepted=',acc)
print('robust_negative_s_minus_2=',neg)
print('min_s_minus_2=',repr(mins[0]))
if mins[1]:
    eps,a,B,z,minatom,eigs=mins[1]
    print('min_eps=',repr(eps));print('min_a=',repr(a));print('min_B=',repr(B.tolist()));print('min_z=',repr(z.tolist()));print('min_atom=',repr(minatom));print('min_K_eigs=',repr(eigs.tolist()))
