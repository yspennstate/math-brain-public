#!/usr/bin/env python3
from __future__ import annotations
import json, math

RUN = "PROB10-01"
STAMP = "2026-09-20T08-36-07Z"

def fwht_int(vals):
    a=list(vals); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def restrict(vals,i,b):
    n=len(vals).bit_length()-1
    out=[]
    for y in range(1<<(n-1)):
        x=0; k=0
        for j in range(n):
            bit=b if j==i else ((y>>k)&1)
            x |= bit<<j
            if j!=i: k+=1
        out.append(vals[x])
    return out

def influence(vals,i):
    N=len(vals)
    return sum(vals[x]!=vals[x^(1<<i)] for x in range(N))/N

def entropy(vals):
    W=fwht_int(vals); N=len(vals); ans=0.0
    for w in W:
        if w:
            p=(w/N)**2
            ans -= p*math.log2(p)
    return ans

def M_s(vals,s):
    W=fwht_int(vals); N=len(vals)
    return sum((abs(w)/N)**s for w in W if w)

def Phi(vals):
    n=len(vals).bit_length()-1
    if n==0: return 0.0
    return n*(M_s(vals,2-1/n)-1)

def adaptive_charge(vals,i):
    return Phi(vals)-0.5*(Phi(restrict(vals,i,0))+Phi(restrict(vals,i,1)))

def c_upper(n):
    if n<=1: return 0.0
    t=1-1/n
    return (2**t-1)/(2*t)

def one_point(n):
    return [-1]+[1]*((1<<n)-1)

def majority(n):
    return [1 if x.bit_count()<=n//2 else -1 for x in range(1<<n)]

def majority_substitution_9():
    out=[]
    for x in range(1<<9):
        inner=[]
        for b in range(3):
            ones=sum((x>>(3*b+j))&1 for j in range(3))
            inner.append(1 if ones<=1 else -1)
        out.append(1 if sum(z==-1 for z in inner)<=1 else -1)
    return out

def addressing6():
    out=[]
    for x in range(64):
        a=((x>>0)&1)+2*((x>>1)&1)
        bit=(x>>(2+a))&1
        out.append(1-2*bit)
    return out

def bent4():
    out=[]
    for x in range(16):
        q=(((x>>0)&1)&((x>>1)&1)) ^ (((x>>2)&1)&((x>>3)&1))
        out.append(-1 if q else 1)
    return out

def tensor(a,b):
    na=len(a).bit_length()-1
    return [a[x&((1<<na)-1)]*b[x>>na] for x in range(len(a)*len(b))]

def gamma_controls(seed,c=3):
    ns=len(seed).bit_length()-1
    out=[]
    for x in range(1<<(ns+c)):
        old=x&((1<<ns)-1); ctrl=x>>ns
        out.append(seed[old] if ctrl==0 else 1)
    return out

def onepoint_formula(n):
    N=2.0**n; s=2-1/n
    M=(1-2/N)**s+(N-1)*(2/N)**s
    ph=n*(M-1)
    if n==1: return ph,None
    Nc=N/2; sc=2-1/(n-1)
    Mc=(1-2/Nc)**sc+(Nc-1)*(2/Nc)**sc
    phc=(n-1)*(Mc-1)
    A=ph-0.5*phc
    return ph,A/(2/N)

def bent_background_formula(d):
    N=2.0**d; rho=N**-0.5; n=d+1
    def B(k,s):
        return 0.5*(1+rho)*(1-k*rho)**s+0.5*(1-rho)*(1+k*rho)**s
    def G(s): return N**(1-s/2)
    def H(s): return G(s)*B(2,s)
    def P(s): return G(s)*B(1,s)+N**(1-s)
    sn=2-1/n
    D=P(sn)-0.5*(G(sn)+H(sn))
    sd=2-1/d
    A=n*(P(sn)-1)-0.5*d*((G(sd)-1)+(H(sd)-1))
    delta=1/N
    return {"background_dimension":d,
            "same_exponent_D_over_influence":D/delta,
            "same_exponent_nD_over_influence":n*D/delta,
            "adaptive_charge":A,
            "adaptive_charge_over_influence":A/delta}

out={"status":"PASS","run":RUN,"stamp":STAMP,"exact_structural":{},
     "exhaustive_dim_le_4":{},"named_stress":{},"asymptotic_formula_diagnostics":{},
     "limitations":"Finite entropy/proxy and selector comparisons use IEEE double precision as stress tests only. The report gives the all-dimensional proofs of the dyadic entropy-proxy equivalence, adaptive telescope, and the two asymptotic families. The coded F_8 family has 2040 physical inputs and is not truth-table evaluated here. No independent audit or Lean/formal proof is claimed."}

total_functions=0; total_coordinate_cases=0
min_lower=float("inf"); min_upper=float("inf")
selector={}; allcoord={}
for n in range(1,5):
    N=1<<n
    best_worst=-float("inf"); best_witness=None
    all_worst=-float("inf"); all_witness=None
    for mask in range(1<<N):
        vals=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        W=fwht_int(vals)
        for w in W:
            if w and (w%2!=0):
                raise AssertionError(("Walsh parity",n,mask,w))
        H=entropy(vals); P=Phi(vals)
        if H:
            lo=P-(math.log(2)/2)*H
            hi=c_upper(n)*H-P if n>=2 else 0.0
            if lo < -2e-12 or hi < -2e-12:
                raise AssertionError(("proxy",n,mask,lo,hi))
            min_lower=min(min_lower,lo); min_upper=min(min_upper,hi)
        ratios=[]
        for i in range(n):
            inf=influence(vals,i)
            if inf:
                r=adaptive_charge(vals,i)/inf
                ratios.append(r); total_coordinate_cases+=1
                if r>all_worst:
                    all_worst=r; all_witness={"truth_table_mask":mask,"coordinate":i,"ratio":r}
        if ratios and min(ratios)>best_worst:
            best_worst=min(ratios); best_witness={"truth_table_mask":mask,"coordinate_ratios":ratios}
        total_functions+=1
    selector[str(n)]={"max_over_functions_of_best_coordinate_ratio":best_worst,"witness":best_witness}
    allcoord[str(n)]={"max_all_coordinate_ratio":all_worst,"witness":all_witness}

out["exact_structural"]["boolean_functions_checked_walsh_even_lattice_dim_1_to_4"]=total_functions
out["exhaustive_dim_le_4"]["nonconstant_coordinate_cases"]=total_coordinate_cases
out["exhaustive_dim_le_4"]["minimum_lower_proxy_slack_float"]=min_lower
out["exhaustive_dim_le_4"]["minimum_upper_proxy_slack_float"]=min_upper
out["exhaustive_dim_le_4"]["best_coordinate_selector"]=selector
out["exhaustive_dim_le_4"]["all_coordinate_worst"]=allcoord

named={"one_point_6":one_point(6),"majority_5":majority(5),
       "majority_substitution_9":majority_substitution_9(),"addressing_6":addressing6(),
       "bent_quadratic_4":bent4(),"tensor_w3_w3":tensor(one_point(3),one_point(3)),
       "fresh_control_gamma3_majority3":gamma_controls(majority(3),3)}
for name,vals in named.items():
    n=len(vals).bit_length()-1; rs=[]
    for i in range(n):
        inf=influence(vals,i)
        if inf: rs.append(adaptive_charge(vals,i)/inf)
    H=entropy(vals); P=Phi(vals)
    out["named_stress"][name]={"n":n,"H":H,"Phi":P,"Phi_over_H":None if H==0 else P/H,
        "best_adaptive_charge_over_influence":min(rs) if rs else None,
        "worst_adaptive_charge_over_influence":max(rs) if rs else None,
        "coordinate_ratios":rs}

out["named_stress"]["coded_F8"]={"physical_inputs":2040,"truth_table_executed":False,
    "reason":"2^2040 truth table is infeasible; only the all-dimensional analytical proxy theorem applies automatically. No claim is made that the coded family satisfies the unproved adaptive selector."}
out["asymptotic_formula_diagnostics"]["one_point"]=[
    {"n":n,"Phi":onepoint_formula(n)[0],"adaptive_charge_over_influence":onepoint_formula(n)[1]}
    for n in (3,4,5,6,8,12,16,24,32)]
out["asymptotic_formula_diagnostics"]["one_point_proved_limit"]=2.0
out["asymptotic_formula_diagnostics"]["bent_background"]=[bent_background_formula(d) for d in range(2,22,2)]
out["asymptotic_formula_diagnostics"]["bent_fixed_level_proved_slope"]=2-math.sqrt(2)
out["asymptotic_formula_diagnostics"]["bent_adaptive_charge_proved_limit"]=(math.sqrt(2)-1)-math.sqrt(2)*math.log(2)/2
print(json.dumps(out,indent=2,sort_keys=True))
