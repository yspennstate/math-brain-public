#!/usr/bin/env python3
"""Finite sanity check for B14 crossing-amplified corrected-erasure identities.

This is not a proof.  It exhausts global-output-sign classes through n=3,
selects a physical-descendant maximizer of F/J, recenters it by a character,
and checks the analytic identities/inequalities used in REPORT.md.
"""
import itertools, json, math

TOL = 5e-12

def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]

def ent(ps):
    return -sum(p*math.log2(p) for p in ps if p > 1e-15)

def jfun(p):
    q = min(max(p, 0.0), 1.0)
    q = min(q, 1.0-q)
    y = 0.5 + math.sqrt(max(0.0, q*(1.0-q)))
    h = 0.0 if y <= 0.0 or y >= 1.0 else -(y*math.log2(y)+(1-y)*math.log2(1-y))
    return 1.0-h

def stats(f, n):
    a = fwht(f)
    mu = [x*x for x in a]
    H = ent(mu)
    p = [sum(mu[s] for s in range(1<<n) if (s>>i)&1) for i in range(n)]
    I = sum(p)
    J = sum(min(x, 1.0-x) for x in p)
    P = sum(jfun(x) for x in p)
    return {"H":H, "I":I, "J":J, "P":P, "F":H-P, "p":p, "mu":mu}

def restrict_f(f, n, A, ass):
    A = tuple(sorted(A))
    rem = [i for i in range(n) if i not in A]
    amap = dict(zip(A, ass))
    out = []
    for y in range(1<<len(rem)):
        x = 0
        for i,b in amap.items():
            if b: x |= 1<<i
        for k,i in enumerate(rem):
            if (y>>k)&1: x |= 1<<i
        out.append(f[x])
    return out, len(rem), rem

def recenter(f, n):
    s = stats(f,n)
    flip = [i for i,p in enumerate(s["p"]) if p > 0.5+1e-12]
    if not flip:
        return list(f)
    out=[]
    for x,v in enumerate(f):
        parity = sum((x>>i)&1 for i in flip) & 1
        out.append(-v if parity else v)
    return out

def descendants(f,n):
    for r in range(n+1):
        for A in itertools.combinations(range(n),r):
            for ass in itertools.product([0,1], repeat=r):
                g,gn,_ = restrict_f(f,n,A,ass)
                if len(set(g)) > 1:
                    yield g,gn

def B_A(f,n,A):
    s=stats(f,n); A=set(A)
    rem=[i for i in range(n) if i not in A]
    marg={}
    for mask,prob in enumerate(s["mu"]):
        key=tuple((mask>>i)&1 for i in rem)
        marg[key]=marg.get(key,0.0)+prob
    return s["H"]-ent(marg.values())

def block(f,n,A):
    # f is centered.
    s=stats(f,n); A=tuple(sorted(A))
    rem=[i for i in range(n) if i not in A]
    r=len(A); den=2**r
    Hc=Pc=Fc=Jc=0.0
    childp={j:[] for j in rem}
    for ass in itertools.product([0,1], repeat=r):
        g,gn,_=restrict_f(f,n,A,ass)
        sg=stats(g,gn)
        Hc += sg["H"]/den
        Pc += sg["P"]/den
        Fc += sg["F"]/den
        Jc += sg["J"]/den
        for k,j in enumerate(rem):
            childp[j].append(sg["p"][k])
    dH=s["H"]-Hc
    B=B_A(f,n,A)
    JS=dH-B
    IA=sum(s["p"][i] for i in A)
    C=sum(sum(max(2*x-1,0.0) for x in childp[j])/den for j in rem)
    G=sum(jfun(s["p"][j])-sum(jfun(x) for x in childp[j])/den for j in rem)
    PhiA=sum(jfun(s["p"][i]) for i in A)
    R=PhiA-JS
    Q=G+R
    return {
        "B":B,"JS":JS,"IA":IA,"C":C,"G":G,"R":R,"Q":Q,
        "dJ":s["J"]-Jc,"dF":s["F"]-Fc
    }

max_dj=0.0
max_df=0.0
max_critical_violation=0.0
max_fixed_lower_violation=0.0
max_fixed_upper_violation=0.0
max_selector_violation=0.0
max_ratio_loss_identity=0.0
max_surviving_j_identity=0.0
critical_cores=0
fixed_cases=0

for n in range(1,4):
    # Fix f(0)=+1 to quotient global output sign.
    for mask in range(1<<((1<<n)-1)):
        f=[1]+[1 if (mask>>(k-1))&1 else -1 for k in range(1,1<<n)]
        cand=[]
        for g,gn in descendants(f,n):
            sg=stats(g,gn)
            if sg["J"]>1e-12:
                cand.append((sg["F"]/sg["J"],g,gn))
        if not cand:
            continue
        _,g,gn=max(cand,key=lambda x:x[0])
        g=recenter(g,gn)
        s=stats(g,gn)
        rho=s["F"]/s["J"]
        assert all(p <= 0.5+TOL for p in s["p"])
        critical_cores += 1

        blocks_by_m={}
        for r in range(gn+1):
            rows=[]
            for A in itertools.combinations(range(gn),r):
                q=block(g,gn,A)
                max_dj=max(max_dj,abs(q["dJ"]-(q["IA"]+q["C"])))
                max_df=max(max_df,abs(q["dF"]-(q["B"]-q["Q"])))
                max_critical_violation=max(
                    max_critical_violation,
                    rho*q["dJ"]-q["dF"]
                )
                rows.append((A,q))
            blocks_by_m[r]=rows

        for m in range(1,gn):
            rows=blocks_by_m[m]
            k=len(rows)
            avgB=sum(q["B"] for _,q in rows)/k
            Aq=(m/gn)*s["H"]-avgB
            Cav=sum(q["C"] for _,q in rows)/k
            Gav=sum(q["G"] for _,q in rows)/k
            JSav=sum(q["JS"] for _,q in rows)/k
            Qav=sum(q["Q"] for _,q in rows)/k
            lhs=Aq+Gav+rho*Cav
            rhs=(m/gn)*s["P"]
            max_fixed_lower_violation=max(max_fixed_lower_violation,lhs-JSav)
            max_fixed_upper_violation=max(max_fixed_upper_violation,JSav-rhs)

            bound=s["P"]/s["I"]-(gn*Aq)/(m*s["I"])
            ratios=[(rho*q["C"]+q["Q"])/q["IA"] for _,q in rows if q["IA"]>1e-12]
            if ratios:
                max_selector_violation=max(max_selector_violation,min(ratios)-bound)

            # Exact J-size-biased descendant ratio-loss identity.
            weighted_loss=0.0
            childJ=0.0
            childF=0.0
            for A,_ in rows:
                for ass in itertools.product([0,1], repeat=m):
                    child,cn,_=restrict_f(g,gn,A,ass)
                    sc=stats(child,cn)
                    w=1.0/(k*(2**m))
                    childJ += w*sc["J"]
                    childF += w*sc["F"]
                    if sc["J"]>1e-12:
                        weighted_loss += w*sc["J"]*(rho-sc["F"]/sc["J"])
            residual=JSav-Aq-Gav-rho*Cav
            max_ratio_loss_identity=max(max_ratio_loss_identity,abs(residual-weighted_loss))
            expected_childJ=(1-m/gn)*s["I"]-Cav
            max_surviving_j_identity=max(max_surviving_j_identity,abs(expected_childJ-childJ))
            if childJ>1e-12:
                max_ratio_loss_identity=max(
                    max_ratio_loss_identity,
                    abs((rho-childF/childJ)-residual/childJ)
                )
            fixed_cases += 1

out={
  "scope":"global-output-sign classes through n=3; analytic theorem does not depend on enumeration",
  "critical_cores_checked":critical_cores,
  "fixed_cardinality_cases_checked":fixed_cases,
  "max_abs_folded_J_drift_identity_error":max_dj,
  "max_abs_corrected_entropy_identity_error":max_df,
  "max_criticality_violation":max_critical_violation,
  "max_fixed_lower_sandwich_violation":max_fixed_lower_violation,
  "max_fixed_upper_sandwich_violation":max_fixed_upper_violation,
  "max_mass_weighted_selector_violation":max_selector_violation,
  "max_abs_ratio_loss_identity_error":max_ratio_loss_identity,
  "max_abs_surviving_J_identity_error":max_surviving_j_identity,
}
print(json.dumps(out,indent=2,sort_keys=True))
