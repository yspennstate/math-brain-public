#!/usr/bin/env python3
"""
ProofNet24 P17 M32 certificate for the historical nearest-neighbor
Example 4.3.3 rational Hamiltonian at (97/153, 87/148), r=0.4.

The code validates the periodic/antiperiodic Jacobi endpoint eigenvalues
on an N=8 hull-phase grid by:
  1. interval-enclosing the exact trigonometric/exponential hopping weights;
  2. treating NumPy's returned Q,D only as approximate dyadic data;
  3. bounding the exact Gram defect ||Q^T Q-I|| and residual ||AQ-QD||;
  4. passing to the exact orthogonal polar factor S=Q(Q^TQ)^(-1/2);
  5. using Weyl's Hermitian eigenvalue perturbation theorem.

The resulting band endpoint enclosures, plus the analytic hull interpolation
budget from P17-M31, certify the four rational C*-spectral gaps
[-1.18,-1.00], [-0.44,-0.33], [0.33,0.44], [1.00,1.18].

Requires numpy and mpmath.
"""
import math
import numpy as np
import mpmath as mp
from mpmath.libmp import to_float

mp.iv.dps = 60
U = 2.0**-53
R = 0.4
NGRID = 8

def gamma(k):
    return (k*U)/(1-k*U)

def jacobi(Q,p,alpha,beta_sign):
    """Binary64 midpoint matrix used only to generate an approximate Q,D."""
    theta=p/Q
    phi=alpha/Q
    n=np.arange(Q)
    t=np.exp(-(1 + R*(
        np.sin(2*np.pi*((n+1)*theta+phi))
        -np.sin(2*np.pi*(n*theta+phi)))))
    H=np.zeros((Q,Q),dtype=float)
    for j in range(Q-1):
        H[j,j+1]=t[j]
        H[j+1,j]=t[j]
    H[Q-1,0]=beta_sign*t[Q-1]
    H[0,Q-1]=beta_sign*t[Q-1]
    return H,t

def exact_weight_intervals(Q,p,alpha_num,alpha_den):
    rr=mp.iv.mpf(2)/5
    theta=mp.iv.mpf(p)/Q
    phi=(mp.iv.mpf(alpha_num)/alpha_den)/Q
    twopi=2*mp.iv.pi
    out=[]
    for n in range(Q):
        s1=mp.iv.sin(twopi*(mp.iv.mpf(n+1)*theta+phi))
        s0=mp.iv.sin(twopi*(mp.iv.mpf(n)*theta+phi))
        out.append(mp.iv.exp(-(1+rr*(s1-s0))))
    return out

def max_weight_midpoint_error(Q,p,alpha_num,alpha_den,tfloat):
    tiv=exact_weight_intervals(Q,p,alpha_num,alpha_den)
    out=0.0
    for tf,ti in zip(tfloat,tiv):
        lo=to_float(ti._mpi_[0])
        hi=to_float(ti._mpi_[1])
        out=max(out,max(abs(tf-lo),abs(tf-hi))*(1+4*U)+1e-30)
    return out

def validated_eigh(Q,p,alpha_num,alpha_den,beta_sign):
    """
    Return approximate ordered eigenvalues and a rigorous common error eta
    such that |lambda_k(A_exact)-D_k| <= eta for all k.

    Let G=Q^TQ and S=Q G^{-1/2}. If delta=||G-I||<1 then S is orthogonal and

      A S - S D
        = (A Q-QD)G^{-1/2} + Q[D,G^{-1/2}].

    Hence
      ||A-SDS^T||
      <= ||R||/sqrt(1-delta)
         + 2 sqrt(1+delta)||D||((1-delta)^(-1/2)-1).

    Weyl then yields the ordered-eigenvalue bound.
    """
    H,tfloat=jacobi(Q,p,alpha_num/alpha_den,beta_sign)
    D,Qm=np.linalg.eigh(H)

    gd=gamma(2*Q+2)
    g2=0.0
    for a in range(Q):
        for b in range(Q):
            s=0.0
            asum=0.0
            for j in range(Q):
                prod=Qm[j,a]*Qm[j,b]
                s += prod
                asum += abs(prod)
            ub=abs(s-(1.0 if a==b else 0.0))+gd*asum+4*U
            g2 += ub*ub
    delta=math.sqrt(g2)
    assert delta < 1.0

    gr=gamma(8)
    r2=0.0
    for a,lam in enumerate(D):
        v=Qm[:,a]
        for j in range(Q):
            jm=(j-1)%Q
            jp=(j+1)%Q
            left=tfloat[jm]*(beta_sign if j==0 else 1)
            right=tfloat[j]*(beta_sign if j==Q-1 else 1)
            x1=left*v[jm]
            x2=right*v[jp]
            x3=lam*v[j]
            rf=(x1+x2)-x3
            er=gr*(abs(x1)+abs(x2)+abs(x3))+4*U
            r2 += (abs(rf)+er)**2
    rmid=math.sqrt(r2)

    wt_err=max_weight_midpoint_error(
        Q,p,alpha_num,alpha_den,tfloat)
    dA=2*wt_err

    qfro=math.sqrt(Q*(1+delta))
    rF=rmid+dA*qfro

    invsqrt=1/math.sqrt(1-delta)
    qnorm=math.sqrt(1+delta)
    polar_dev=invsqrt-1
    dnorm=max(abs(D[0]),abs(D[-1]))
    eta=rF*invsqrt+2*qnorm*dnorm*polar_dev
    return D,eta,delta,rF,dA

def merge(intervals):
    out=[]
    for a,b in sorted(intervals):
        if not out or a>out[-1][1]:
            out.append([a,b])
        else:
            out[-1][1]=max(out[-1][1],b)
    return [(a,b) for a,b in out]

def factor_grid_cover(Q,p):
    intervals=[]
    stats=[]
    for k in range(NGRID):
        dp,ep,gp,rp,ap=validated_eigh(Q,p,k,NGRID,+1)
        da,ea,ga,ra,aa=validated_eigh(Q,p,k,NGRID,-1)
        eta=max(ep,ea)
        stats.extend([(ep,gp,rp,ap),(ea,ga,ra,aa)])
        endpoints=np.sort(np.concatenate([dp,da]))
        for j in range(Q):
            intervals.append(
                (float(endpoints[2*j]-eta),
                 float(endpoints[2*j+1]+eta)))
    return merge(intervals),stats

def interval_distance(G,Uset):
    a,b=G
    ans=float("inf")
    for c,d in Uset:
        if d>=a and c<=b:
            return 0.0
        if d<a:
            ans=min(ans,a-d)
        elif c>b:
            ans=min(ans,c-b)
    return ans

def main():
    U1,s1=factor_grid_cover(153,97)
    U2,s2=factor_grid_cover(148,87)

    full_grid=merge(
        [(a+c,b+d) for a,b in U1 for c,d in U2])

    c=4*math.pi*R*math.exp(-(1-2*R))
    delta1=c/(153*NGRID)
    delta2=c/(148*NGRID)
    hull=delta1+delta2

    targets=[
        (-1.18,-1.00),
        (-0.44,-0.33),
        ( 0.33, 0.44),
        ( 1.00, 1.18),
    ]

    print("factor1 max eta =",max(x[0] for x in s1))
    print("factor2 max eta =",max(x[0] for x in s2))
    print("factor1 max Gram defect bound =",max(x[1] for x in s1))
    print("factor2 max Gram defect bound =",max(x[1] for x in s2))
    print("hull interpolation budget =",hull)
    print()
    for G in targets:
        d=interval_distance(G,full_grid)
        print(
            "target",G,
            "grid distance >=",repr(d),
            "post-hull margin >=",repr(d-hull))
        assert d > hull

    d1,e1,*_=validated_eigh(153,97,0,NGRID,+1)
    d2,e2,*_=validated_eigh(148,87,0,NGRID,+1)
    sums=np.sort((d1[:,None]+d2[None,:]).ravel())
    eta=e1+e2
    for E in (-1.1,-0.38,0.38,1.1):
        rank=int(np.searchsorted(sums,E,side="left"))
        nearest=min(
            abs(sums[rank-1]-E) if rank else float("inf"),
            abs(sums[rank]-E) if rank<len(sums) else float("inf"))
        print(
            "E",E,"rank",rank,
            "nearest approximate eigenvalue distance",nearest,
            "validated sum error",eta)
        assert nearest > eta

if __name__ == "__main__":
    main()
