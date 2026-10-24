#!/usr/bin/env python3
"""
PROB20-16 fixed-leaf path theorem checker.
Proof is analytic; this script verifies exact algebraic identities and runs deterministic diagnostics.
"""
import itertools, math, cmath, json
import numpy as np
import sympy as sp

SEED = 20260916
NPAIRS = 2000

def p2_atoms(d, c, sy):
    # sy = |y|^2
    return {
        (0,0):(1-d)*(1-c)-sy,
        (1,0):d*(1-c)+sy,
        (0,1):(1-d)*c+sy,
        (1,1):d*c-sy,
    }

def exact_symbolic_checks():
    a,b,c,X,Y = sp.symbols('a b c X Y', positive=True)
    # Three-site path exact atoms in bit order (x1,x2,x3), from inclusion-exclusion.
    p3 = {
        (0,0,0): -a*b*c+a*b+a*c+a*Y-a+b*c-b+c*X-c-X-Y+1,
        (1,0,0): a*b*c-a*b-a*c-a*Y+a-c*X+X,
        (0,1,0): a*b*c-a*b-a*Y-b*c+b-c*X+X+Y,
        (0,0,1): a*b*c-a*c-a*Y-b*c-c*X+c+Y,
        (1,1,0): -a*b*c+a*b+a*Y+c*X-X,
        (1,0,1): -a*b*c+a*c+a*Y+c*X,
        (0,1,1): -a*b*c+a*Y+b*c+c*X-Y,
        (1,1,1): a*b*c-a*Y-c*X,
    }
    d1 = b-X/a
    d0 = b+X/(1-a)
    # Conditional 2-site atoms on sites (2,3).
    q1 = p2_atoms(d1,c,Y)
    q0 = p2_atoms(d0,c,Y)
    residuals=[]
    for i2 in (0,1):
        for i3 in (0,1):
            residuals.append(sp.factor(p3[(1,i2,i3)] - a*q1[(i2,i3)]))
            residuals.append(sp.factor(p3[(0,i2,i3)] - (1-a)*q0[(i2,i3)]))
    assert all(r==0 for r in residuals), residuals

    # Exact squared-norm convexity identity for a complex affine edge.
    t=sp.symbols('t', real=True)
    xr0,xi0,xr1,xi1=sp.symbols('xr0 xi0 xr1 xi1', real=True)
    X0=xr0**2+xi0**2
    X1=xr1**2+xi1**2
    Xt=((1-t)*xr0+t*xr1)**2+((1-t)*xi0+t*xi1)**2
    defect=sp.factor((1-t)*X0+t*X1-Xt - t*(1-t)*((xr1-xr0)**2+(xi1-xi0)**2))
    assert defect==0
    return {"conditional_atom_identities": 8, "strength_defect_identity": True}

def principal_det(K,S):
    if len(S)==0:
        return 1.0
    return float(np.linalg.det(K[np.ix_(S,S)]).real)

def dpp_atoms(K):
    n=K.shape[0]
    q={}
    for r in range(n+1):
        for S in itertools.combinations(range(n),r):
            q[S]=principal_det(K,list(S))
    p={}
    universe=set(range(n))
    for r in range(n+1):
        for S in itertools.combinations(range(n),r):
            Ss=set(S); rest=sorted(universe-Ss)
            val=0.0
            for rr in range(len(rest)+1):
                for U in itertools.combinations(rest,rr):
                    T=tuple(sorted(Ss|set(U)))
                    val += (-1)**len(U)*q[T]
            p[S]=val
    return p

def entropy_K(K):
    vals=np.array(list(dpp_atoms(K).values()),dtype=float)
    if vals.min() < -1e-10:
        raise AssertionError(("negative atom",float(vals.min())))
    vals=np.maximum(vals,0.0)
    return float(-sum(v*math.log(v) for v in vals if v>0))

def hbin(a):
    if a==0 or a==1:
        return 0.0
    return -a*math.log(a)-(1-a)*math.log(1-a)

def is_strict(K,eps=1e-7):
    ev=np.linalg.eigvalsh(K)
    return bool(ev.min()>eps and ev.max()<1-eps)

def H2(d,c,y):
    M=np.array([[d,y],[np.conjugate(y),c]],dtype=complex)
    return entropy_K(M)

def chain_value(K):
    a=float(K[0,0].real); x=K[0,1]
    b=float(K[1,1].real); y=K[1,2]; c=float(K[2,2].real)
    F1=np.array([[b-abs(x)**2/a,y],[np.conjugate(y),c]],dtype=complex)
    F0=np.array([[b+abs(x)**2/(1-a),y],[np.conjugate(y),c]],dtype=complex)
    return hbin(a)+a*entropy_K(F1)+(1-a)*entropy_K(F0)

def random_path_with_a(rng,a):
    for _ in range(10000):
        b=float(rng.uniform(.05,.95)); c=float(rng.uniform(.05,.95))
        mx=.28*math.sqrt(min(a*b,(1-a)*(1-b)))
        my=.28*math.sqrt(min(b*c,(1-b)*(1-c)))
        rx=float(rng.uniform(0,mx)); ry=float(rng.uniform(0,my))
        x=rx*cmath.exp(1j*float(rng.uniform(-math.pi,math.pi)))
        y=ry*cmath.exp(1j*float(rng.uniform(-math.pi,math.pi)))
        K=np.array([[a,x,0],[np.conjugate(x),b,y],[0,np.conjugate(y),c]],dtype=complex)
        if is_strict(K,1e-5):
            return K
    raise RuntimeError("path sampler failed")

def phi(a,b,c,y,u):
    return a*H2(b-(1-a)*u,c,y)+(1-a)*H2(b+a*u,c,y)

def dH2_dd(d,c,y):
    sy=abs(y)**2
    p=[
        (1-d)*(1-c)-sy,
        d*(1-c)+sy,
        (1-d)*c+sy,
        d*c-sy,
    ]
    dp=[-(1-c),(1-c),-c,c]
    if min(p)<=0:
        raise AssertionError(("non-strict 2-site atom",min(p)))
    return -sum(di*math.log(pi) for di,pi in zip(dp,p)

def diagnostics():
    rng=np.random.default_rng(SEED)
    max_chain_res=0.0
    min_full_gap=float("inf")
    min_phi_gap=float("inf")
    min_strength_defect=float("inf")
    max_du=-float("inf")
    for _ in range(NPAIRS):
        a=float(rng.uniform(.05,.95))
        K0=random_path_with_a(rng,a)
        K1=random_path_with_a(rng,a)
        t=float(rng.uniform(.02,.98))
        Kt=(1-t)*K0+t*K1
        H0,H1,Ht=entropy_K(K0),entropy_K(K1),entropy_K(Kt)
        min_full_gap=min(min_full_gap,Ht-(1-t)*H0-t*H1)
        max_chain_res=max(max_chain_res,abs(Ht-chain_value(Kt)))

        def pars(K):
            b=float(K[1,1].real); c=float(K[2,2].real)
            x=K[0,1]; y=K[1,2]
            u=abs(x)**2/(a*(1-a))
            return b,c,y,u,x
        b0,c0,y0,u0,x0=pars(K0)
        b1,c1,y1,u1,x1=pars(K1)
        bt,ct,yt,ut,xt=pars(Kt)
        ubar=(1-t)*u0+t*u1
        min_strength_defect=min(min_strength_defect,ubar-ut)
        min_phi_gap=min(min_phi_gap,phi(a,bt,ct,yt,ubar)-((1-t)*phi(a,b0,c0,y0,u0)+t*phi(a,b1,c1,y1,u1)))

        d1=bt-(1-a)*ut
        d0=bt+a*ut
        du=a*(1-a)*(dH2_dd(d0,ct,yt)-dH2_dd(d1,ct,yt))
        max_du=max(max_du,du)

    # Exact-entry example from the report.
    K0=np.array([[.5,.1,0],[.1,.4,1j/12],[0,-1j/12,.6]],dtype=complex)
    K1=np.array([[.5,1j/8,0],[-1j/8,.6,.1],[0,.1,.4]],dtype=complex)
    Km=(K0+K1)/2
    ex_gap=entropy_K(Km)-.5*(entropy_K(K0)+entropy_K(K1))
    return {
        "seed":SEED,
        "pairs":NPAIRS,
        "max_chain_rule_abs_residual":max_chain_res,
        "min_full_jensen_gap":min_full_gap,
        "min_auxiliary_phi_jensen_gap_at_affine_u":min_phi_gap,
        "min_strength_defect_ubar_minus_u":min_strength_defect,
        "max_observed_partial_u_phi":max_du,
        "example_midpoint_gap":ex_gap,
        "example_eigenvalues_Q0":np.linalg.eigvalsh(K0).tolist(),
        "example_eigenvalues_Q1":np.linalg.eigvalsh(K1).tolist(),
        "example_eigenvalues_midpoint":np.linalg.eigvalsh(Km).tolist(),
    }

if __name__=="__main__":
    result={"exact":exact_symbolic_checks(),"diagnostics":diagnostics()}
    print(json.dumps(result,indent=2,sort_keys=True))
