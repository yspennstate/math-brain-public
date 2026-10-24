#!/usr/bin/env python3
"""Checks for B17 independent-contamination short-circuit theorem.

This is regression evidence for an analytic theorem, not a proof of full FEI.
Only Python standard library is used.
"""
from math import log2, log
from itertools import product
from decimal import Decimal, getcontext

getcontext().prec = 220
DD=Decimal
DLN2=DD(2).ln()

LN2 = log(2.0)

def fwht(a):
    a = list(map(float, a))
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]

def entropy(vals):
    return sum(-p*log2(p) for c in fwht(vals) for p in [c*c] if p > 0.0)

def influence(vals, i):
    n = len(vals)
    mask = 1 << i
    return sum(vals[x] != vals[x ^ mask] for x in range(n)) / n

def folded_J(vals):
    d = (len(vals)).bit_length()-1
    return sum(min(influence(vals,i), 1-influence(vals,i)) for i in range(d))

def phi(t):
    out = 0.0
    for p in ((1-t)**2, t*t):
        if p:
            out += p*log2(1/p)
    return out

def formula_delta_H(r, a):
    q = 2.0**(-r)
    p = q + (1-q)*a
    n = 2**r
    C = (1-q)**2*log2(1/(1-q)**2) + (n-1)*q*q*log2(1/(q*q))
    u=q*q*(1-a)**2
    Q = 0.0 if u == 0.0 else 2*(n-1)*u*log2(1/u)
    return phi(p) - (1-q)*phi(a) + 2*a*(1-a)*C + Q

def formula_D(r,a):
    q=2.0**(-r)
    return q*(r*(1-a)+1)

def F_root(r,m,A):
    out=[]
    for idx in range(1 << (1+r+m)):
        x=(idx>>0)&1
        z=(idx>>1)&((1<<r)-1)
        w=(idx>>(1+r))&((1<<m)-1)
        X=1 if x==0 else -1
        out.append(X if (z==0 or w in A) else 1)
    return out

def F_A(m,A):
    out=[]
    for idx in range(1 << (1+m)):
        x=idx&1
        w=idx>>1
        X=1 if x==0 else -1
        out.append(X if w in A else 1)
    return out

def exact_leaf_average_J(r,m,A):
    # first mismatch at t has leaf F_A plus r-t dummy z bits;
    # all-match leaf is chi_x. Dummies contribute zero.
    return (1-2.0**(-r))*folded_J(F_A(m,A))

def check_small_exhaustive():
    worst_H = worst_D = 0.0
    hcases=dcases=0
    for r in (2,3,4):
        for m in (1,2,3):
            nw=1<<m
            for mask in range(1<<nw):
                A={w for w in range(nw) if (mask>>w)&1}
                a=len(A)/nw
                root=F_root(r,m,A)
                leaf=F_A(m,A)
                q=2.0**(-r)
                dH=entropy(root)-(1-q)*entropy(leaf)
                worst_H=max(worst_H,abs(dH-formula_delta_H(r,a)))
                hcases+=1
                amax=q/(16*(1-q))
                if a <= amax + 1e-15:
                    dJ=folded_J(root)-exact_leaf_average_J(r,m,A)
                    worst_D=max(worst_D,abs(dJ-formula_D(r,a)))
                    dcases+=1
    return hcases,dcases,worst_H,worst_D

def check_targeted_admissible():
    rows=[]
    max_h=max_d=0.0
    for r in (2,3,4):
        m=r+4
        A={0}
        a=1/(1<<m)
        root=F_root(r,m,A)
        leaf=F_A(m,A)
        q=2.0**(-r)
        dH=entropy(root)-(1-q)*entropy(leaf)
        dJ=folded_J(root)-exact_leaf_average_J(r,m,A)
        max_h=max(max_h,abs(dH-formula_delta_H(r,a)))
        max_d=max(max_d,abs(dJ-formula_D(r,a)))
        rows.append((r,m,a,dH/dJ))
    return rows,max_h,max_d

def dlog2(x):
    return x.ln()/DLN2

def dh2(t):
    if t == 0 or t == 1:
        return DD(0)
    return -t*dlog2(t)-(DD(1)-t)*dlog2(DD(1)-t)

def dphi(t):
    one=DD(1)
    out=DD(0)
    for p in ((one-t)**2,t*t):
        if p:
            out += p*dlog2(one/p)
    return out

def d_delta_H(r,a):
    one=DD(1); two=DD(2)
    q=two**(-r)
    p=q+(one-q)*a
    n=two**r
    C=(one-q)**2*dlog2(one/(one-q)**2)+(n-one)*q*q*dlog2(one/(q*q))
    u=q*q*(one-a)**2
    Q=DD(0) if not u else two*(n-one)*u*dlog2(one/u)
    return dphi(p)-(one-q)*dphi(a)+two*a*(one-a)*C+Q

def check_scalar_grid():
    worst_slack=None
    worst_cert=None
    worst_gamma=None
    arg=None
    cert_arg=None
    gamma_arg=None
    cases=0
    fractions=[DD(0),DD(1)/64,DD(1)/32,DD(1)/16,DD(1)/8,DD(1)/4,DD(1)/2,DD(3)/4,DD(1)]
    for r in range(2,513):
        q=DD(2)**(-r)
        amax=q/(DD(16)*(DD(1)-q))
        for f in fractions:
            a=amax*f
            dH=d_delta_H(r,a)
            D=q*(DD(r)*(DD(1)-a)+DD(1))
            slack=DD(4)*D-dH
            pden=q+(DD(1)-q)*a
            cert=(DD(32)/DD(5))*dh2(pden)-dH
            gamma=(DD(1)-(DD(16)/DD(17))*(pden/q)) if q else DD(0)
            if worst_slack is None or slack<worst_slack:
                worst_slack=slack
                arg=(r,str(a),str(dH/D if D else DD(0)))
            if worst_cert is None or cert<worst_cert:
                worst_cert=cert
                cert_arg=(r,str(a),str(dH/dh2(pden) if pden else DD(0)))
            if worst_gamma is None or gamma<worst_gamma:
                worst_gamma=gamma
                gamma_arg=(r,str(a))
            cases+=1
    return cases,worst_slack,arg,worst_cert,cert_arg,worst_gamma,gamma_arg

def named_event_densities():
    # The theorem depends only on density, so record admissible examples.
    rows=[]
    for r in (2,3,4,6,8):
        q=2.0**(-r)
        # sparse point on m=r+4 bits: a=q/16
        a_sparse=2.0**(-(r+4))
        rows.append(("sparse-point",r,a_sparse,formula_delta_H(r,a_sparse)/formula_D(r,a_sparse)))
        # rare-gated addressing / tribes may be any event behind a rare gate;
        # use the admissible density q/32 as a representative density.
        a_gate=q/32
        rows.append(("rare-gated-addressing-density",r,a_gate,formula_delta_H(r,a_gate)/formula_D(r,a_gate)))
        rows.append(("rare-gated-tribes-density",r,a_gate,formula_delta_H(r,a_gate)/formula_D(r,a_gate)))
    return rows

def main():
    hcases,dcases,herr,derr=check_small_exhaustive()
    targeted,therr,tderr=check_targeted_admissible()
    scases,slack,arg,cert,cert_arg,gamma,gamma_arg=check_scalar_grid()
    print("small_exhaustive_entropy_cases",hcases)
    print("small_exhaustive_admissible_drift_cases",dcases)
    print("max_exact_DeltaH_formula_error",repr(herr))
    print("max_exact_D_formula_error",repr(derr))
    print("targeted_admissible_rows",targeted)
    print("targeted_max_DeltaH_formula_error",repr(therr))
    print("targeted_max_D_formula_error",repr(tderr))
    print("scalar_admissible_cases",scases)
    print("minimum_4D_minus_DeltaH",repr(slack))
    print("minimum_slack_arg_r_a_ratio",arg)
    print("minimum_(32/5)h2(p)-DeltaH",repr(cert))
    print("minimum_certificate_arg_r_a_DeltaH_over_h2p",cert_arg)
    print("minimum_1-(16/17)(p/q)",repr(gamma))
    print("minimum_gamma_arg",gamma_arg)
    print("named_density_stress_tests")
    for row in named_event_densities():
        print(row)
    if max(herr,derr,therr,tderr)>2e-10 or slack < DD(0) or cert < DD(0) or gamma < -DD('1e-190'):
        raise SystemExit("FAIL")
    print("PASS")

if __name__ == "__main__":
    main()
