#!/usr/bin/env python3
"""Calibration for the B18 scalar-frontier tangent-defect stability theorem.

The theorem in REPORT.md is analytic. This script only reproduces the current
r-calibration, samples the tangent defect G_r(q), and prints finite-degree
top-chain lower-bound factors. It is not an FEI proof or interval certificate.
"""
import json, math

LN2 = math.log(2.0)

def h(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q*math.log2(q) - (1.0-q)*math.log2(1.0-q)

def j(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    y = 2.0*math.sqrt(q*(1.0-q))
    return 1.0 - h((1.0+y)/2.0)

def beta(q):
    return h(q)/q

def kappa(q):
    return (h(q)+j(q))/q

def jprime(q):
    y = 2.0*math.sqrt(q*(1.0-q))
    return (2.0*(1.0-2.0*q)/(y*LN2))*math.atanh(y)

def lam(q):
    hp = math.log2((1.0-q)/q)
    P = h(q)-q*hp
    Q = j(q)-q*jprime(q)
    return P/(P+Q)

def tau_of_r(r):
    lo, hi = 1e-14, 0.5
    for _ in range(160):
        mid=(lo+hi)/2.0
        if kappa(mid) > r:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

def run(r):
    tau=tau_of_r(r)
    b=beta(tau)
    la=lam(tau)
    d=la*r-b

    def G(q):
        return beta(q)-b-la*(kappa(q)-r)

    qs=[]
    lo=1e-8
    split=max(1e-5,tau/8.0)
    for k in range(6000):
        u=k/5999.0
        qs.append(lo*(split/lo)**u)
    for k in range(40001):
        q=split+(1.0-split)*k/40000.0
        qs.append(q)

    min_G=(float("inf"),None)
    min_quad=(float("inf"),None)
    for q in qs:
        g=G(q)
        if g < min_G[0]:
            min_G=(g,q)
        if abs(q-tau)>1e-7:
            ratio=g/((q-tau)**2)
            if ratio < min_quad[0]:
                min_quad=(ratio,q)

    degrees={}
    for deg in (2,5,15,30,100):
        qd=1.0/(1.0+2.0**(2.0-2.0/deg))
        factor=(4.0**(1-deg))*max(qd-tau,0.0)**2
        degrees[str(deg)]={"q_d":qd,"raw_top_chain_factor":factor}

    return {
        "r":r,
        "tau":tau,
        "b":b,
        "lambda":la,
        "d=lambda*r-b":d,
        "endpoint_quadratic_candidate_d_over_(1-tau)^2":d/((1.0-tau)**2),
        "sampled_min_G":min_G[0],
        "sampled_min_G_q":min_G[1],
        "sampled_min_G_over_square":min_quad[0],
        "sampled_min_G_over_square_q":min_quad[1],
        "finite_degree_raw_factors_before_c_r":degrees,
        "classification":"NUMERICAL_CALIBRATION_ONLY"
    }

if __name__=="__main__":
    print(json.dumps(run(6.521845710923046575), indent=2, sort_keys=True))
