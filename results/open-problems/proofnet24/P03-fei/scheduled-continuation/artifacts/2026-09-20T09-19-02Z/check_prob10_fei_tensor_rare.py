#!/usr/bin/env python3
from __future__ import annotations
import json, math

RUN = "PROB10-01"
STAMP = "2026-09-20T09-19-02Z"

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

def influence_i(vals,i):
    N=len(vals)
    return sum(vals[x]!=vals[x^(1<<i)] for x in range(N))/N

def influence(vals):
    n=len(vals).bit_length()-1
    return sum(influence_i(vals,i) for i in range(n))

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

def tensor(a,b):
    na=len(a).bit_length()-1
    return [a[x&((1<<na)-1)]*b[x>>na] for x in range(len(a)*len(b))]

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

def gamma_controls(seed,c=3):
    ns=len(seed).bit_length()-1
    out=[]
    for x in range(1<<(ns+c)):
        old=x&((1<<ns)-1); ctrl=x>>ns
        out.append(seed[old] if ctrl==0 else 1)
    return out

# New theorem 1 self-check: Phi is subadditive under disjoint tensor products.
allfuncs={}
for n in range(1,4):
    N=1<<n
    allfuncs[n]=[
        [-1 if (mask>>x)&1 else 1 for x in range(N)]
        for mask in range(1<<N)
    ]

tensor_cases=0
min_tensor_slack=float("inf")
max_ratio_violation=-float("inf")
for m in range(1,4):
    for k in range(1,4):
        if m+k>4: continue
        for f in allfuncs[m]:
            pf=Phi(f); If=influence(f)
            for g in allfuncs[k]:
                pg=Phi(g); Ig=influence(g)
                fg=tensor(f,g)
                lhs=Phi(fg); rhs=pf+pg
                slack=rhs-lhs
                min_tensor_slack=min(min_tensor_slack,slack)
                if slack < -1e-10:
                    raise AssertionError(("tensor_subadditivity",m,k,slack))
                It=If+Ig
                if It>0:
                    factor_ratios=[]
                    if If>0: factor_ratios.append(pf/If)
                    if Ig>0: factor_ratios.append(pg/Ig)
                    bound=max(factor_ratios)
                    violation=lhs/It-bound
                    max_ratio_violation=max(max_ratio_violation,violation)
                    if violation>1e-10:
                        raise AssertionError(("tensor_ratio",m,k,lhs/It,bound))
                tensor_cases += 1

# New theorem 2 self-check: arbitrary exponentially biased functions.
rare_cases=0
min_iso_slack=float("inf")
min_phi_bound_slack=float("inf")
max_checked_rare_ratio=0.0
for n in range(2,5):
    N=1<<n
    for mask in range(1<<N):
        vals=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        neg=sum(v==-1 for v in vals)
        delta=min(neg,N-neg)/N
        if delta==0 or delta>0.25: continue
        I=influence(vals); P=Phi(vals)
        L=math.log2(1/delta)/n
        iso=2*delta*math.log2(1/delta)
        iso_slack=I-iso
        if iso_slack < -1e-10:
            raise AssertionError(("edge_isoperimetry",n,mask,delta,I,iso))
        coeff=2*(2**((1+L)/2)-1)/L + 2/(n*L)
        bound=coeff*I
        if P>bound+1e-10:
            raise AssertionError(("rare_phi_bound",n,mask,P,bound))
        rare_cases+=1
        min_iso_slack=min(min_iso_slack,iso_slack)
        min_phi_bound_slack=min(min_phi_bound_slack,bound-P)
        max_checked_rare_ratio=max(max_checked_rare_ratio,P/I)

# A false stronger idea: local adaptive charge does not tensor-monotonically.
w2=one_point(2); w2w2=tensor(w2,w2)
w2_ratio=adaptive_charge(w2,0)/influence_i(w2,0)
product_ratio=adaptive_charge(w2w2,0)/influence_i(w2w2,0)
analytic_w2=4*(math.sqrt(2)-1)
analytic_product=2*(4*(math.sqrt(2)-1)-3*(2**(1/3)-1))
if abs(w2_ratio-analytic_w2)>1e-12 or abs(product_ratio-analytic_product)>1e-12:
    raise AssertionError("closed_form_local_tensor_obstruction")
if not product_ratio>w2_ratio:
    raise AssertionError("local_tensor_monotonicity_was_not_refuted")

# Mechanism calibration from the repository-recorded published Hod lower-bound input.
hod_H_over_I=6.454784
derived_phi_over_I=(math.log(2)/2)*hod_H_over_I
if not derived_phi_over_I>2:
    raise AssertionError("constant_two_calibration")

# Mandatory named stress families for the new potential/mechanisms.
named={
    "one_point_8":one_point(8),
    "majority_5":majority(5),
    "majority_substitution_9":majority_substitution_9(),
    "addressing_6":addressing6(),
    "bent_quadratic_4":bent4(),
    "tensor_w3_w3":tensor(one_point(3),one_point(3)),
    "fresh_control_gamma3_majority3":gamma_controls(majority(3),3),
}
stress={}
for name,vals in named.items():
    n=len(vals).bit_length()-1
    I=influence(vals); P=Phi(vals); H=entropy(vals)
    ratios=[]
    for i in range(n):
        ii=influence_i(vals,i)
        if ii: ratios.append(adaptive_charge(vals,i)/ii)
    stress[name]={
        "n":n, "H":H, "Phi":P, "I":I,
        "H_over_I":None if I==0 else H/I,
        "Phi_over_I":None if I==0 else P/I,
        "best_adaptive_charge_over_influence":None if not ratios else min(ratios),
        "worst_adaptive_charge_over_influence":None if not ratios else max(ratios),
    }

def beta_constant(beta):
    return 1+2*(2**((1+beta)/2)-1)/beta

out={
    "status":"PASS",
    "run":RUN,
    "stamp":STAMP,
    "tensor_subadditivity":{
        "exhaustive_ordered_pairs_total_dimension_le_4":tensor_cases,
        "minimum_rhs_minus_lhs_float":min_tensor_slack,
        "maximum_ratio_bound_violation_float":max_ratio_violation,
        "local_tensor_charge_monotonicity_obstruction":{
            "w2_ratio":w2_ratio,
            "w2_tensor_w2_ratio":product_ratio,
            "analytic_w2_ratio":analytic_w2,
            "analytic_product_ratio":analytic_product,
        },
    },
    "rare_bias":{
        "exhaustive_functions_with_minority_density_in_0_to_1_4_dim_2_to_4":rare_cases,
        "minimum_edge_isoperimetry_slack_float":min_iso_slack,
        "minimum_phi_bound_slack_float":min_phi_bound_slack,
        "maximum_Phi_over_I_in_checked_rare_cases":max_checked_rare_ratio,
        "beta_corollary_constants":{
            str(beta):beta_constant(beta) for beta in (0.1,0.25,0.5,0.75,1.0)
        },
    },
    "hod_mechanism_calibration":{
        "published_H_over_I_input_gt":hod_H_over_I,
        "derived_Phi_over_I_lower_gt":derived_phi_over_I,
        "meaning":"Uses Phi >= (ln 2)/2 H and the repository-recorded published Hod lower-bound input; this is not an independent verification of Hod.",
    },
    "named_stress":stress,
    "coded_F8":{
        "physical_inputs":2040,
        "truth_table_executed":False,
        "statement":"No selector or direct bound is inferred computationally for F_8. Tensor subadditivity applies to a product only after an actual product decomposition is proved.",
    },
    "limitations":"Finite numerical comparisons use IEEE double precision and are self-checks only. The report supplies the all-dimensional tensor-subadditivity and rare-bias proofs. No independent audit, Lean/formal verification, exhaustive high-dimensional Boolean census, novelty clearance, or full FEI closure is claimed.",
}
print(json.dumps(out,indent=2,sort_keys=True))
