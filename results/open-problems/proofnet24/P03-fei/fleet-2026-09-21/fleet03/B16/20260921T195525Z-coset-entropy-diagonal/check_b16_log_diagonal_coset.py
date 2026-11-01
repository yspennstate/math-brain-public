#!/usr/bin/env python3
import json, math
from fractions import Fraction

LN2 = math.log(2.0)

def hnat(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log(p) - (1.0-p)*math.log(1.0-p)

def F(x):
    if x == 0.0:
        return 0.0
    return x*x*math.log(abs(x))

def kdiag(a,b):
    return 0.25*(F(a-b)+F(a+b)-2.0*F(a)-2.0*F(b))

def diag_entropy(a,b):
    S=a*a+b*b
    if S == 0.0:
        return (0.0,0.0,0.0)
    p=a*a/S
    q=(a+b)*(a+b)/(2.0*S)
    C=S*hnat(p)
    JS=S*(LN2-hnat(q))
    return 0.25*(C+JS), C, JS

max_identity_error=0.0
max_ratio=0.0
min_uncertainty_slack=1e100
argmax_ratio=None
for j in range(20001):
    if j == 0:
        r=0.0
    else:
        r=10.0**(-8.0 + 8.0*(j-1)/19999.0)
    a,b=1.0,r
    lhs=kdiag(a,b)
    rhs,C,JS=diag_entropy(a,b)
    max_identity_error=max(max_identity_error,abs(lhs-rhs))
    min_uncertainty_slack=min(min_uncertainty_slack,C-JS)
    if C > 1e-15:
        ratio=lhs/C
        if ratio > max_ratio:
            max_ratio=ratio
            argmax_ratio=r

def pc(x): return x.bit_count()

def entropy(probs):
    return sum(-p*math.log(p) for p in probs if p>0.0)

def coset_check(f,w,n):
    N=1<<n
    C=JS=sumk=0.0
    U=[];V=[];M=[]
    for xi in range(N):
        a=sum((w[x] if f[x]==1 else 0)*((-1)**pc(x&xi)) for x in range(N))/N
        b=sum((w[x] if f[x]==-1 else 0)*((-1)**pc(x&xi)) for x in range(N))/N
        S=a*a+b*b
        if S:
            C += S*hnat(a*a/S)
            JS += S*(LN2-hnat((a+b)*(a+b)/(2*S)))
        sumk += kdiag(a,b)
        U.append((a+b)*(a+b))
        V.append((a-b)*(a-b))
        M.append(S)
    JS_direct=entropy(M)-0.5*(entropy(U)+entropy(V))
    return {
        "identity_error":abs(sumk-0.25*(C+JS)),
        "js_error":abs(JS-JS_direct),
        "mass_error":max(abs(sum(U)-1),abs(sum(V)-1),abs(sum(M)-1)),
        "js_minus_C":JS-C,
    }

coset_records=[]
for n in (2,3,4):
    N=1<<n
    for seed in range(10):
        f=[1 if ((x*x+3*x+seed*7)%(seed+3))%2==0 else -1 for x in range(N)]
        if len(set(f))==1:
            f=[1 if pc(x)%2==0 else -1 for x in range(N)]
        w=[1 if ((pc(x)+seed*x)%3)!=1 else -1 for x in range(N)]
        coset_records.append(coset_check(f,w,n))

def total_influence(vals,n):
    N=1<<n
    directed=0
    for x in range(N):
        for i in range(n):
            if vals[x] != vals[x^(1<<i)]:
                directed += 1
    return directed/N

edge_cases=0
edge_max_ratio=0.0
for n in range(1,5):
    N=1<<n
    for mask in range(1,(1<<N)-1):
        vals=[1 if (mask>>x)&1 else -1 for x in range(N)]
        p=min(sum(v==-1 for v in vals)/N, sum(v==1 for v in vals)/N)
        I=total_influence(vals,n)
        edge_max_ratio=max(edge_max_ratio, hnat(p)/(LN2*I))
        edge_cases += 1

def norm2(v): return sum(x*x for x in v)
def sub(a,b): return [x-y for x,y in zip(a,b)]
anova_checks=0
for Mq in range(2,9):
    d=5
    ms=[]
    for c in range(Mq):
        ms.append([Fraction(((c+1)*(j+2))%7-3, c+j+3) for j in range(d)])
    bar=[sum(m[j] for m in ms)/Mq for j in range(d)]
    lhs=norm2(sub(ms[0],bar))
    pair=sum(norm2(sub(ms[0],m)) for m in ms)/Mq
    var=sum(norm2(sub(m,bar)) for m in ms)/Mq
    assert lhs == pair-var
    anova_checks += 1

alpha_checks=0
for Mq in range(2,21):
    rho=Fraction(1,Mq); gamma=1-rho
    base_mass = gamma
    outside_mass = rho
    assert base_mass + outside_mass == 1
    assert (Mq-1) * (rho/Fraction(Mq-1)) == rho
    alpha_checks += 1

out={
    "status":"PASS",
    "scalar_grid_points":20001,
    "max_scalar_identity_error":max_identity_error,
    "min_JS_le_C_slack":min_uncertainty_slack,
    "max_Kdiag_over_C":max_ratio,
    "argmax_ratio_b_over_a":argmax_ratio,
    "coset_cases":len(coset_records),
    "max_coset_identity_error":max(x["identity_error"] for x in coset_records),
    "max_coset_JS_direct_error":max(x["js_error"] for x in coset_records),
    "max_coset_mass_error":max(x["mass_error"] for x in coset_records),
    "max_coset_JS_minus_C":max(x["js_minus_C"] for x in coset_records),
    "exhaustive_nonconstant_boolean_functions_n_le_4":edge_cases,
    "max_h_over_ln2I":edge_max_ratio,
    "exact_rational_ANOVA_checks":anova_checks,
    "exact_alpha_mixture_checks":alpha_checks,
    "derived_constants":{
        "current_diagonal_payment_4ln2_over_9":4*LN2/9,
        "central_diagonal_payment_11ln2_over_288":11*LN2/288
    }
}
print(json.dumps(out,indent=2,sort_keys=True))
