#!/usr/bin/env python3
from __future__ import annotations
import json, math

RUN="PROB10-01"
STAMP="2026-09-20T10-30-50Z"
LAMBDAS=(0.25,0.5,1.0)

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

def probs(vals):
    W=fwht_int(vals); N=len(vals)
    return [(w/N)**2 for w in W if w]

def entropy_bits(vals):
    return -sum(p*math.log2(p) for p in probs(vals))

def entropy_nat(vals):
    return math.log(2)*entropy_bits(vals)

def R(vals,t):
    return sum(p**(1-t) for p in probs(vals))

def Phi(vals,lam=1.0):
    n=len(vals).bit_length()-1
    if n==0: return 0.0
    return n/lam*(R(vals,lam/(2*n))-1)

def adaptive_charge(vals,i,lam=1.0):
    return Phi(vals,lam)-0.5*(Phi(restrict(vals,i,0),lam)+Phi(restrict(vals,i,1),lam))

def tensor(a,b):
    na=len(a).bit_length()-1
    return [a[x&((1<<na)-1)]*b[x>>na] for x in range(len(a)*len(b))]

def tensor_power(f,k):
    out=list(f)
    for _ in range(1,k): out=tensor(out,f)
    return out

def one_point(n): return [-1]+[1]*((1<<n)-1)

def majority(n): return [1 if x.bit_count()<=n//2 else -1 for x in range(1<<n)]

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

def pad_dummy(f,d):
    m=len(f).bit_length()-1
    return [f[x&((1<<m)-1)] for x in range(1<<(m+d))]

def h2(x):
    if x==0 or x==1: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def shannon_drop(vals,i):
    return entropy_bits(vals)-0.5*(entropy_bits(restrict(vals,i,0))+entropy_bits(restrict(vals,i,1)))

def branch_components(vals,i):
    n=len(vals).bit_length()-1
    W=fwht_int(vals); N=len(vals)
    alpha=HB=JS=dot=0.0
    for T in range(1<<n):
        if (T>>i)&1: continue
        a=W[T]/N; b=W[T|(1<<i)]/N
        dot += a*b
        q=a*a+b*b
        alpha += b*b
        if q==0: continue
        r=b*b/q
        HB += q*h2(r)
        z=(a+b)**2/(2*q)
        JS += q*(1-h2(z))
    return alpha,HB,JS,dot

allfuncs={}; even_lattice_cases=0; proxy={}
for n in range(1,5):
    N=1<<n; fs=[]
    for mask in range(1<<N):
        vals=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        fs.append(vals)
        for w in fwht_int(vals):
            if w and w%2: raise AssertionError(("dyadic_lattice_parity",n,mask,w))
        even_lattice_cases += 1
    allfuncs[n]=fs
    for lam in LAMBDAS:
        lower=float("inf"); upper=float("inf"); nontrivial=0
        for vals in fs:
            H=entropy_bits(vals); P=Phi(vals,lam)
            if H<=1e-15: continue
            nontrivial+=1
            lower=min(lower,P-(math.log(2)/2)*H)
            if n>1:
                c=(2**(lam*(1-1/n))-1)/(2*lam*(1-1/n))
                upper=min(upper,c*H-P)
                if P>c*H+1e-10: raise AssertionError(("proxy_upper",n,lam,P,H,c))
            if P<(math.log(2)/2)*H-1e-10: raise AssertionError(("proxy_lower",n,lam,P,H))
        proxy[f"n={n},lambda={lam}"]={
            "nontrivial_functions":nontrivial,
            "minimum_lower_slack_float":None if nontrivial==0 else lower,
            "minimum_upper_slack_float":None if n==1 or nontrivial==0 else upper,
        }

branch_cases=0; max_identity_error=0.0; max_drop_over_h2=-1.0; max_witness=None
min_js_payment_slack=float("inf"); max_dot_abs=0.0
for n in range(1,5):
    for mask,vals in enumerate(allfuncs[n]):
        for i in range(n):
            alpha=influence_i(vals,i)
            if alpha==0: continue
            D=shannon_drop(vals,i)
            a,HB,JS,dot=branch_components(vals,i)
            max_identity_error=max(max_identity_error,abs(D-(HB+JS)),abs(a-alpha))
            max_dot_abs=max(max_dot_abs,abs(dot))
            if abs(dot)>1e-10: raise AssertionError(("pair_orthogonality",n,mask,i,dot))
            if JS>h2(alpha)+1e-10: raise AssertionError(("JS_payment",n,mask,i,JS,alpha))
            if D>2*h2(alpha)+1e-10: raise AssertionError(("branch_payment",n,mask,i,D,alpha))
            ratio=D/h2(alpha) if h2(alpha)>0 else 0.0
            if ratio>max_drop_over_h2:
                max_drop_over_h2=ratio
                max_witness={"n":n,"mask":mask,"coordinate":i,"influence":alpha,
                             "drop_bits":D,"orientation_bits":HB,"JS_bits":JS}
            min_js_payment_slack=min(min_js_payment_slack,h2(alpha)-JS)
            branch_cases+=1

tensor_out={}
for lam in LAMBDAS:
    cases=0; min_slack=float("inf"); max_ratio_violation=-float("inf")
    for m in range(1,4):
        for k in range(1,4):
            if m+k>4: continue
            for f in allfuncs[m]:
                pf=Phi(f,lam); If=influence(f)
                for g in allfuncs[k]:
                    pg=Phi(g,lam); Ig=influence(g)
                    fg=tensor(f,g); lhs=Phi(fg,lam); rhs=pf+pg
                    slack=rhs-lhs
                    if slack < -1e-10: raise AssertionError(("tensor_subadditivity",lam,m,k,slack))
                    min_slack=min(min_slack,slack)
                    It=If+Ig; rr=[]
                    if If>0: rr.append(pf/If)
                    if Ig>0: rr.append(pg/Ig)
                    if It>0 and rr:
                        violation=lhs/It-max(rr)
                        max_ratio_violation=max(max_ratio_violation,violation)
                        if violation>1e-10: raise AssertionError(("tensor_ratio",lam,m,k,violation))
                    cases+=1
    tensor_out[str(lam)]={
        "ordered_pairs_total_dimension_at_most_4":cases,
        "minimum_rhs_minus_lhs_float":min_slack,
        "maximum_ratio_bound_violation_float":max_ratio_violation,
    }

w2=one_point(2); h=entropy_nat(w2); m=2; alpha=influence_i(w2,0)
D_nat=h-0.5*(entropy_nat(restrict(w2,0,0))+entropy_nat(restrict(w2,0,1)))
lam=1.0; u=lam*h/(2*m)
local_limit=(math.exp(u)-1)/lam+math.exp(u)*(D_nat/2-h/(2*m))
local_ratio_limit=local_limit/alpha
global_ratio_limit=m/(lam*influence(w2))*(math.exp(u)-1)
tensor_power_rows=[]
for k in range(1,8):
    vals=tensor_power(w2,k)
    tensor_power_rows.append({
        "k":k,"dimension":2*k,
        "local_charge_over_influence":adaptive_charge(vals,0,1.0)/influence_i(vals,0),
        "Phi_over_I":Phi(vals,1.0)/influence(vals),
    })
if abs(tensor_power_rows[-1]["Phi_over_I"]-global_ratio_limit)>1e-10: raise AssertionError("w2_global_tensor_limit_formula")
if abs(tensor_power_rows[-1]["local_charge_over_influence"]-local_ratio_limit)>0.02: raise AssertionError("w2_local_tensor_limit_convergence")

dummy_rows=[]
for d in (0,1,2,4,6,8,10):
    vals=pad_dummy(w2,d)
    dummy_rows.append({
        "dummy_variables":d,"dimension":2+d,
        "local_charge":adaptive_charge(vals,0,1.0),
        "local_charge_over_influence":adaptive_charge(vals,0,1.0)/influence_i(vals,0),
        "Phi":Phi(vals,1.0),
    })
dummy_charge_limit=D_nat/2; phi_padding_limit=h/2
if abs(dummy_rows[-1]["local_charge"]-dummy_charge_limit)>0.03: raise AssertionError("dummy_padding_charge_convergence")

named={
    "one_point_8":one_point(8),"majority_5":majority(5),
    "majority_substitution_9":majority_substitution_9(),"addressing_6":addressing6(),
    "bent_quadratic_4":bent4(),"tensor_w3_w3":tensor(one_point(3),one_point(3)),
    "fresh_control_gamma3_majority3":gamma_controls(majority(3),3),
}
stress={}
for name,vals in named.items():
    n=len(vals).bit_length()-1
    row={"dimension":n,"H":entropy_bits(vals),"I":influence(vals)}
    for lam in (0.5,1.0):
        ratios=[]
        for i in range(n):
            ii=influence_i(vals,i)
            if ii: ratios.append(adaptive_charge(vals,i,lam)/ii)
        row[f"Phi_lambda_{lam}"]=Phi(vals,lam)
        row[f"best_charge_ratio_lambda_{lam}"]=None if not ratios else min(ratios)
        row[f"worst_charge_ratio_lambda_{lam}"]=None if not ratios else max(ratios)
    stress[name]=row

out={
    "status":"PASS","run":RUN,"stamp":STAMP,
    "dyadic_lattice":{"boolean_functions_through_dimension_4":even_lattice_cases},
    "endpoint_scale_proxy":proxy,
    "dependent_branch_recombination":{
        "coordinate_cases_through_dimension_4":branch_cases,
        "maximum_identity_error_float":max_identity_error,
        "maximum_D_over_h2_influence":max_drop_over_h2,
        "maximizing_witness":max_witness,
        "minimum_h2_minus_JS_slack_float":min_js_payment_slack,
        "maximum_abs_pair_dot_product_float":max_dot_abs,
    },
    "tensor_subadditivity":tensor_out,
    "w2_tensor_power":{
        "rows":tensor_power_rows,"proved_local_charge_limit":local_limit,
        "proved_local_charge_over_influence_limit":local_ratio_limit,
        "proved_global_Phi_over_I_limit":global_ratio_limit,
    },
    "w2_dummy_padding":{"rows":dummy_rows,"proved_local_charge_limit":dummy_charge_limit,"proved_Phi_limit":phi_padding_limit},
    "named_stress":stress,
    "coded_F8":{"physical_inputs":2040,"truth_table_executed":False,
        "statement":"No selector claim is inferred for F_8; the tensor theorem applies only after an actual disjoint tensor decomposition is proved."},
    "limitations":"All finite entropy/Renyi comparisons use IEEE double precision and are self-checks only. The all-dimensional statements require the report proofs. No independent audit, Lean/formal verification, high-dimensional exhaustive Boolean census, publication-priority clearance, or FEI closure is claimed."
}
print(json.dumps(out,indent=2,sort_keys=True))
