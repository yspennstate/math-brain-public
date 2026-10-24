#!/usr/bin/env python3
# P11 Lyons handoff checks: exact peer-audit algebra + numerical X095 counterexample diagnostic.
# NUMERICAL SEARCH IS NOT A GLOBAL CERTIFICATE.
import math
import numpy as np
import sympy as sp

# --- exact audit of PROB20-16 Lemma 6.1 ---
x,y,s,u,v = sp.symbols('x y s u v', real=True)
p00=(1-x)*(1-y)-s
p10=x*(1-y)+s
p01=(1-x)*y+s
p11=x*y-s
checks = {
    'A_derivative': sp.simplify(sp.diff(sp.log(p00/p01),x) + s/(p00*p01)),
    'B_derivative': sp.simplify(sp.diff(sp.log(p10/p11),x) + s/(p10*p11)),
    'E_derivative': sp.simplify(sp.diff(sp.log(p10/p01),x) - ((1-y)/p10 + y/p01)),
    'det_atom_decomposition': sp.simplify(
        ((1-y)*u+y*v)*((1-x)*u+x*v)-s*(u-v)**2
        -(p00*u**2+(p10+p01)*u*v+p11*v**2)
    ),
}
assert all(val == 0 for val in checks.values())
print('PEER_AUDIT_EXACT_ALGEBRA=PASS')
for k,val in checks.items(): print(k, '=', val)

# --- retained X095 numerical evaluator ---
rng=np.random.default_rng(202609162315)

def adj3(A):
    out=np.empty((3,3),complex)
    for i in range(3):
        for j in range(3):
            rows=[r for r in range(3) if r!=j]
            cols=[c for c in range(3) if c!=i]
            out[i,j]=((-1)**(i+j))*np.linalg.det(A[np.ix_(rows,cols)])
    return out

def eval_x095(K):
    ps=[]; Es=[]
    for S in range(8):
        A=K.copy()
        for i in range(3):
            if not (S>>i)&1: A[i,i]-=1
        sg=(-1)**(3-int(S).bit_count())
        ps.append((sg*np.linalg.det(A)).real)
        if S: Es.append(sg*adj3(A))
    ps=np.array(ps)
    if ps.min()<1e-12 or abs(ps.sum()-1)>1e-7: return None
    p0,p1,p2,p12,p3,p13,p23,p123=ps
    try:
        cs=np.array([
            math.log(p2*p3/(p0*p23)),
            math.log(p1*p3/(p0*p13)),
            math.log(p1*p2/(p0*p12)),
        ])
        tau=math.log(p0*p12*p13*p23/(p1*p2*p3*p123))
        M=np.diag(cs).astype(complex)+tau*K
        d=np.linalg.det(M).real
        if d<=1e-14: return None
        vv=np.array([np.trace(M@E).real for E in Es])
        T=np.array([[np.trace(M@Ea@M@Eb).real for Eb in Es] for Ea in Es])
        pn=ps[1:]
        V=np.diag(pn)-np.outer(pn,pn)
        C=(T+d*V); C=(C+C.T)/2
        evC=np.linalg.eigvalsh(C)
        if evC[0]<=1e-13: return None
        sval=float(vv@np.linalg.solve(C,vv))
        return sval-2, ps.min(), np.linalg.eigvalsh(K), tau, cs, evC[0]
    except (ValueError, FloatingPointError, np.linalg.LinAlgError):
        return None

def rand_unitary():
    Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    Q,R=np.linalg.qr(Z)
    diag=np.diag(R)
    Q=Q*(diag/np.abs(diag)).conj()
    return Q

print('NUMERICAL_DIAGNOSTIC_ONLY')
print('GLOBAL_CERTIFICATE=false')
print('seed=202609162315')
all_acc=all_neg=0
for mode,n in [('generic',6000),('rank2',6000),('double_small',6000),('near1',6000)]:
    best=(float('inf'),None); acc=neg=0
    for _ in range(n):
        U=rand_unitary()
        if mode=='generic':
            lam=np.sort(rng.uniform(0.03,0.97,3))
        elif mode=='rank2':
            lam=np.sort(np.array([10**rng.uniform(-8,-2), rng.uniform(.03,.8), rng.uniform(.2,.97)]))
        elif mode=='double_small':
            lam=np.sort(np.array([10**rng.uniform(-8,-3),10**rng.uniform(-8,-3),rng.uniform(.15,.98)]))
        else:
            lam=np.sort(1-np.array([10**rng.uniform(-8,-3),rng.uniform(.03,.8),rng.uniform(.2,.97)]))
        K=U@np.diag(lam)@U.conj().T
        out=eval_x095(K)
        if out is None: continue
        acc+=1; margin=out[0]
        if margin < -1e-8: neg+=1
        if margin < best[0]: best=(margin,out)
    all_acc += acc; all_neg += neg
    print(f'mode={mode} accepted={acc} robust_negative={neg} min_s_minus_2={best[0]!r}')
    if best[1] is not None:
        print('  min_atom=',repr(float(best[1][1])))
        print('  min_K_eigs=',repr([float(z) for z in best[1][2]]))
        print('  min_tau=',repr(float(best[1][3])))
        print('  min_C_eig=',repr(float(best[1][5])))
print('accepted_total=',all_acc)
print('robust_negative_total=',all_neg)
print('NEGATIVE_CANDIDATES_REQUIRING_EXACT_OR_INTERVAL_VERIFICATION=',all_neg)
