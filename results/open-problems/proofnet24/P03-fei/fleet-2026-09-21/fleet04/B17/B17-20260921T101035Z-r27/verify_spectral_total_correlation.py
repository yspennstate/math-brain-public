#!/usr/bin/env python3
"""Small-n sanity check for a Booleanity-forces-spectral-dependence inequality.

For each Boolean f on n<=4 (up to global negation), let mu(S)=hat f(S)^2,
p_i=Pr_mu[i in S], Q=product Bernoulli(p_i), and
TC=sum_i h2(p_i)-H(mu)=D_KL(mu||Q) in bits.

Checks:
  TC >= max_i p_i(1-p_i) * max(2*m_i-1,0)^2 / ln(2),
where m_i = product_{j != i} max(p_j,1-p_j).

This is a sanity check only; the report contains the analytic proof.
"""
from __future__ import annotations
import json, math

def fwht(a):
    a = a[:]
    h=1
    while h < len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def check_n(n):
    N=1<<n
    total=1<<(N-1) # fix f(0)=+1 to quotient global negation
    worst_margin=float("inf")
    max_tc=0.0
    sufficient_beta=0
    positive_deficit=0
    beta=6.4547837
    argmin=None
    for mask in range(total):
        vals=[1]
        vals += [1 if (mask>>(x-1))&1 else -1 for x in range(1,N)]
        W=fwht(vals)
        mu=[(w/N)**2 for w in W]
        p=[sum(mu[s] for s in range(N) if (s>>i)&1) for i in range(n)]
        H=-sum(q*math.log2(q) for q in mu if q>0)
        tc=sum(h2(x) for x in p)-H
        lower=0.0
        for i,x in enumerate(p):
            if x<=0.0 or x>=1.0:
                continue
            m=1.0
            for j,y in enumerate(p):
                if j!=i:
                    m*=max(y,1-y)
            b=x*(1-x)*max(2*m-1,0.0)**2/math.log(2.0)
            lower=max(lower,b)
        margin=tc-lower
        if margin < worst_margin:
            worst_margin=margin
            argmin={"mask":mask,"p":p,"tc":tc,"lower":lower}
        max_tc=max(max_tc,tc)
        deficit=sum(max(h2(x)-beta*x,0.0) for x in p)
        if deficit>1e-12:
            positive_deficit += 1
            if lower + 1e-12 >= deficit:
                sufficient_beta += 1
    return {
        "n":n,
        "functions_up_to_global_negation":total,
        "worst_margin_tc_minus_lower":worst_margin,
        "argmin":argmin,
        "max_total_correlation_bits":max_tc,
        "functions_with_positive_beta_deficit":positive_deficit,
        "functions_where_this_lower_bound_alone_pays_beta_deficit":sufficient_beta,
    }

out={
    "claim_checked":"TC(mu)>=max_i p_i(1-p_i)(2 m_i-1)_+^2/ln2 for Boolean spectral samples",
    "scope":"all Boolean functions through n=4, quotienting global negation",
    "results":[check_n(n) for n in range(1,5)]
}
print(json.dumps(out,indent=2,sort_keys=True))
