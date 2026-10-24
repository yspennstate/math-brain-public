#!/usr/bin/env python3
import json, math
import numpy as np

TOL=3e-10
TAU=0.25
R=1.0

def fwht(a):
    a=np.array(a,dtype=float).copy()
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y
            a[i+h:i+2*h]=x-y
        h*=2
    return a/n

def entropy_probs(p):
    p=np.asarray(p,float)
    q=p[p>0]
    return float(-np.sum(q*np.log2(q)))

def fourier_entropy(vals):
    a=fwht(vals)
    return entropy_probs(a*a)

def influences(vals):
    vals=np.asarray(vals,float); N=len(vals); n=(N.bit_length()-1)
    out=[]
    for i in range(n):
        bit=1<<i
        idx=np.arange(N)
        out.append(float(np.mean(vals != vals[idx^bit])))
    return out

def fold_char(vals):
    vals=np.asarray(vals,float).copy()
    al=influences(vals); n=len(al)
    mask=sum((1<<i) for i,x in enumerate(al) if x>0.5)
    if mask:
        for x in range(len(vals)):
            if (x & mask).bit_count() & 1:
                vals[x]*=-1
    return vals, mask

def h2(t):
    if t<=0 or t>=1:
        return 0.0 if t in (0,1) else float('nan')
    return -t*math.log2(t)-(1-t)*math.log2(1-t)

def Psi(t):
    if t<=0: return 0.0
    if t>=0.5: return 2.0
    q=0.5+math.sqrt(t*(1-t))
    return h2(t)+1-h2(q)

def children(vals,i):
    vals=np.asarray(vals,float); N=len(vals); n=N.bit_length()-1
    c0=[]; c1=[]
    for y in range(1<<(n-1)):
        lo=y & ((1<<i)-1)
        hi=y>>i
        x0=lo | (hi<<(i+1))
        c0.append(vals[x0])
        c1.append(vals[x0 | (1<<i)])
    return np.array(c0), np.array(c1)

def deltaH(vals,i):
    c0,c1=children(vals,i)
    return fourier_entropy(vals)-0.5*(fourier_entropy(c0)+fourier_entropy(c1))

def conditional_allocation_B(vals,i):
    a=fwht(vals); p=a*a; n=(len(vals).bit_length()-1)
    bit=1<<i; B=0.0
    for s in range(len(vals)):
        if s&bit: continue
        x=p[s]; y=p[s|bit]; z=x+y
        if z>0 and x>0 and y>0:
            B += z*h2(y/z)
    return B

def phi(vals):
    n=len(vals).bit_length()-1
    if n<=1:
        return 0.0
    a=np.abs(fwht(vals))
    return n*(float(np.sum(a**(2-1/n)))-1.0)

def endpoint_E(vals,i):
    c0,c1=children(vals,i)
    return phi(vals)-0.5*(phi(c0)+phi(c1))

def profile_entropy(vals, folded=True):
    v=vals
    if folded:
        v,_=fold_char(vals)
    al=np.array(influences(v),float)
    I=float(np.sum(al))
    if I<=TOL: return 0.0, al.tolist()
    w=al[al>TOL]/I
    return entropy_probs(w), al.tolist()

def split_local(vals,i):
    return children(vals,i)

def prune(vals,tau=TAU,weight=1.0,stats=None):
    if stats is None:
        stats={"queried_cost":0.0,"entropy_drops":0.0,"leaf_I":0.0,"leaf_H":0.0,
               "nodes":0,"leaves":0,"max_cap_violation":-1e9}
    stats["nodes"]+=1
    al=influences(vals)
    js=[min(x,1-x) for x in al]
    choices=[i for i,x in enumerate(js) if x+1e-15>=tau]
    if not choices:
        stats["leaves"]+=1
        stats["leaf_I"] += weight*sum(al)
        stats["leaf_H"] += weight*fourier_entropy(vals)
        return stats
    i=max(choices,key=lambda k:js[k])
    d=deltaH(vals,i)
    cap=Psi(js[i])
    stats["max_cap_violation"]=max(stats["max_cap_violation"],d-cap)
    stats["queried_cost"] += weight*al[i]
    stats["entropy_drops"] += weight*d
    c0,c1=split_local(vals,i)
    prune(c0,tau,weight/2,stats)
    prune(c1,tau,weight/2,stats)
    return stats

def vals_from_mask(n,mask):
    N=1<<n
    return np.array([1.0 if ((mask>>x)&1)==0 else -1.0 for x in range(N)])

def onepoint(n):
    v=np.ones(1<<n); v[0]=-1; return v

def bent4():
    return np.array([(-1.0)**((((x>>0)&1)*((x>>1)&1)) ^ (((x>>2)&1)*((x>>3)&1))) for x in range(16)])

def bit_sign(x,i):
    return 1.0 if ((x>>i)&1)==0 else -1.0

def majority_signs(signs):
    return 1.0 if sum(signs)>0 else -1.0

def majority(n):
    return np.array([majority_signs([bit_sign(x,i) for i in range(n)]) for x in range(1<<n)])

def maj3_of_maj3():
    n=9; out=[]
    for x in range(1<<n):
        inner=[]
        for b in range(3):
            inner.append(majority_signs([bit_sign(x,3*b+j) for j in range(3)]))
        out.append(majority_signs(inner))
    return np.array(out)

def addressing6():
    out=[]
    for x in range(64):
        a=((x>>0)&1)+2*((x>>1)&1)
        out.append(bit_sign(x,2+a))
    return np.array(out)

def tensor(v,w):
    return np.kron(w,v)

def gamma_c(base,c):
    nb=len(base).bit_length()-1
    N=1<<(nb+c); out=np.ones(N)
    for x in range(N):
        y=x & ((1<<nb)-1)
        z=x>>nb
        if z==0:
            out[x]=base[y]
    return out

def summarize(vals):
    al=influences(vals); js=[min(x,1-x) for x in al]
    folded,_=fold_char(vals)
    fal=influences(folded)
    Hp=profile_entropy(vals,True)[0]
    return {
        "n":len(al),"H":fourier_entropy(vals),"I":sum(al),"J":sum(js),
        "H_over_I": fourier_entropy(vals)/sum(al) if sum(al)>TOL else 0,
        "influences":al,"folded_influences":fal,
        "max_j":max(js) if js else 0,
        "profile_entropy_after_fold":Hp,
        "hard_core_tau_quarter_R1": bool(max(fal,default=0)<TAU-1e-12 and Hp>R+1e-12)
    }

kappa=Psi(TAU)/TAU
cstar=2/math.log(2)
assert abs(kappa-5.8267968871755)<5e-12

census={}
aggregate={}
max_restriction_cap_violation=-1e9
max_fold_error=0.0
max_budget_error=0.0
max_entropy_telescope_error=0.0
for n in range(1,5):
    N=1<<n
    full_lim=1<<(N-1)
    if n<=3:
        masks=list(range(full_lim))
        mode="exhaustive"
    else:
        sample_count=4096
        masks=[(k*8191) % full_lim for k in range(sample_count)]
        mode="deterministic_stride_sample"
    maxagg=(-1,None)
    hard=0
    for m in masks:
        vals=np.ones(N)
        for x in range(1,N):
            if (m>>(x-1))&1: vals[x]=-1
        H=fourier_entropy(vals); al=influences(vals); I=sum(al)
        for i,a in enumerate(al):
            j=min(a,1-a)
            max_restriction_cap_violation=max(max_restriction_cap_violation,deltaH(vals,i)-Psi(j))
        fv,_=fold_char(vals)
        fal=influences(fv)
        max_fold_error=max(max_fold_error,max((abs(fal[i]-min(al[i],1-al[i])) for i in range(n)),default=0))
        st=prune(vals)
        max_budget_error=max(max_budget_error,abs(I-(st["queried_cost"]+st["leaf_I"])))
        max_entropy_telescope_error=max(max_entropy_telescope_error,abs(H-(st["entropy_drops"]+st["leaf_H"])))
        if I>TOL and n>=2:
            agg=sum(conditional_allocation_B(vals,i)+endpoint_E(vals,i) for i in range(n))/I
            if agg>maxagg[0]: maxagg=(agg,m)
        Hp,_=profile_entropy(vals,True)
        if max(fal,default=0)<TAU-1e-12 and Hp>R+1e-12 and H>TOL:
            hard+=1
    census[str(n)]={"cases_checked":len(masks),"full_class_size_up_to_global_sign":full_lim,"mode":mode,"hard_core_count":hard}
    if n>=2:
        aggregate[str(n)]={"max_sum_B_plus_E_over_I":maxagg[0],"witness_mask_fixed_f0":maxagg[1]}

assert max_restriction_cap_violation < 1e-8
assert max_fold_error < 1e-10
assert max_budget_error < 1e-10
assert max_entropy_telescope_error < 1e-9

named={
    "one_point_n6": onepoint(6),
    "addressing6": addressing6(),
    "bent_quadratic4": bent4(),
    "tensor_w3_w3": tensor(onepoint(3),onepoint(3)),
    "majority5": majority(5),
    "maj3_of_maj3": maj3_of_maj3(),
    "fresh_control_Gamma3_Maj3": gamma_c(majority(3),3),
}
named_summary={k:summarize(v) for k,v in named.items()}

m=8
a=2**(1-m)
coded_j=a*(1+(1-2*a)/m)
coded_n=m*(2**m-1)
coded_profile=math.log2(coded_n)
coded={
    "physical_inputs":coded_n,
    "per_coordinate_influence_exact_formula":"a*(1+(1-2a)/m), a=2^(1-m), m=8",
    "per_coordinate_influence":coded_j,
    "profile_entropy_uniform":coded_profile,
    "hard_core_tau_quarter_R1": coded_j<TAU and coded_profile>R,
    "truth_table_executed":False,
    "limitation":"Classification uses the archived exact influence formula only; no 2^2040 truth table or new FEI certificate was attempted."
}

out={
    "status":"PASS",
    "full_FEI_proved":False,
    "tau":TAU,"R":R,
    "Psi_tau_over_tau":kappa,
    "profile_coefficient_2_over_ln2_times_Rplus1":cstar*(R+1),
    "localization_threshold_C0":max(kappa,cstar*(R+1)),
    "balanced_R_at_tau_quarter":kappa/cstar-1,
    "exhaustive_census":census,
    "max_restriction_cap_violation":max_restriction_cap_violation,
    "max_character_fold_influence_error":max_fold_error,
    "max_pruning_influence_budget_error":max_budget_error,
    "max_pruning_entropy_telescope_error":max_entropy_telescope_error,
    "aggregate_hybrid_evidence_only":aggregate,
    "named_stress":named_summary,
    "coded_F8":coded,
    "limitations":[
        "Finite exhaustive checks cover all Boolean functions through dimension three up to global sign; dimension four uses a deterministic 4096-function stride sample.",
        "Aggregate hybrid ratios are numerical evidence only and no all-dimensional aggregate payment is claimed.",
        "The hard-core localization theorem is proved analytically in the report from inherited all-dimensional inequalities; this checker only stress-tests its ingredients.",
        "The coded F8 classification uses its archived exact per-coordinate influence formula and uniformity, not truth-table enumeration."
    ]
}
print(json.dumps(out,indent=2,sort_keys=True))
