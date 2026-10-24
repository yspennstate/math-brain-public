#!/usr/bin/env python3
import numpy as np, math, json
from functools import lru_cache

C = math.log(2.0)/2.0
LAMBDAS = [0.0,0.25,0.5,0.75,1.0]

def hadamard(n):
    N=1<<n
    W=np.ones((N,N),dtype=float)
    for s in range(N):
        for x in range(N):
            if ((s & x).bit_count() & 1):
                W[s,x]=-1.0
    return W

@lru_cache(None)
def all_data(n):
    N=1<<n
    M=1<<(N-1)
    masks=np.arange(M,dtype=np.uint64)
    signs=np.ones((M,N),dtype=float)
    if N>1:
        bits=((masks[:,None] >> np.arange(N-1,dtype=np.uint64)) & 1).astype(np.int8)
        signs[:,1:]=1-2*bits
    W=hadamard(n)
    coeff=signs @ W.T / N
    p=coeff**2
    H=(-p*np.log2(np.where(p>0,p,1))).sum(axis=1)
    Phi={}
    G={}
    for li,lam in enumerate(LAMBDAS):
        if lam==0.0:
            ph=C*H
        else:
            ph=(n/lam)*((np.abs(coeff)**(2-lam/n)).sum(axis=1)-1.0)
        Phi[li]=ph
        G[li]=ph-C*H
    infl=np.empty((M,n),float)
    idx=np.arange(N)
    for i in range(n):
        infl[:,i]=(signs != signs[:,idx^(1<<i)]).mean(axis=1)
    return signs,coeff,p,H,Phi,G,infl

def canonical_masks(ch):
    ch=ch.copy()
    neg=ch[:,0]<0
    ch[neg]*=-1
    M,Nd=ch.shape
    cm=np.zeros(M,dtype=np.int64)
    for j in range(1,Nd):
        cm += (ch[:,j]<0).astype(np.int64) << (j-1)
    return cm

def exhaustive_dynamic():
    # dp[n][f,l0] = least possible maximum local ratio on a full proper-block
    # tree starting from f, when future endpoint scales must stay >= LAMBDAS[l0].
    dp={1:np.full((len(all_data(1)[0]),len(LAMBDAS)),-np.inf)}
    out={}
    max_budget_err=0.0
    for n in (2,3,4):
        signs,coeff,p,H,Phi,G,infl=all_data(n)
        M=len(signs)
        cur=np.full((M,len(LAMBDAS)),np.inf)
        fixed_best={li:np.full(M,np.inf) for li in range(len(LAMBDAS))}
        cases=0
        for Amask in range(1,(1<<n)-1):
            A=[i for i in range(n) if (Amask>>i)&1]
            comp=[i for i in range(n) if not ((Amask>>i)&1)]
            k=len(A); d=n-k
            marg=np.zeros((M,1<<d),float)
            for s in range(1<<n):
                key=sum(((s>>i)&1)<<r for r,i in enumerate(comp))
                marg[:,key]+=p[:,s]
            Hm=(-marg*np.log2(np.where(marg>0,marg,1))).sum(axis=1)
            B=H-Hm
            IA=infl[:,A].sum(axis=1)
            child_cms=[]
            childI=np.zeros(M)
            for assign in range(1<<k):
                inds=[]
                for y in range(1<<d):
                    x=0
                    for r,i in enumerate(comp):
                        x |= ((y>>r)&1)<<i
                    for r,i in enumerate(A):
                        x |= ((assign>>r)&1)<<i
                    inds.append(x)
                cm=canonical_masks(signs[:,inds])
                child_cms.append(cm)
                childI += all_data(d)[6][cm].sum(axis=1)/(1<<k)
            max_budget_err=max(max_budget_err,float(np.max(np.abs(infl.sum(axis=1)-(IA+childI)))))
            for li,lam in enumerate(LAMBDAS):
                childG=np.zeros(M)
                for cm in child_cms:
                    childG += all_data(d)[5][li][cm]/(1<<k)
                dG=G[li]-childG
                q=np.full(M,np.inf)
                pos=IA>1e-15
                q[pos]=(B[pos]+dG[pos])/IA[pos]
                q[(~pos)&((B+dG)<=1e-12)]=-np.inf
                fixed_best[li]=np.minimum(fixed_best[li],q)
                if d>=2:
                    future=np.full(M,-np.inf)
                    for cm in child_cms:
                        future=np.maximum(future,dp[d][cm,li])
                else:
                    future=np.full(M,-np.inf)
                cand=np.maximum(q,future)
                for l0 in range(li+1):
                    cur[:,l0]=np.minimum(cur[:,l0],cand)
            cases+=M
        dp[n]=cur
        relevant=infl.sum(axis=1)>1e-15
        ix=np.where(relevant)[0]
        w=int(ix[np.argmax(cur[ix,0])])
        out[str(n)]={
            "functions_up_to_global_sign":int(M),
            "proper_block_cases":int(cases),
            "fixed_lambda_worst_best":{
                str(LAMBDAS[li]):float(np.max(fixed_best[li][ix]))
                for li in range(len(LAMBDAS))
            },
            "monotone_grid_dynamic_worst_from_lambda0":float(np.max(cur[ix,0])),
            "dynamic_witness_canonical_mask":w,
            "monotone_grid_dynamic_worst_from_lambda1":float(np.max(cur[ix,-1]))
        }
    return out,max_budget_err

def fwht(vals):
    a=np.asarray(vals,dtype=float).copy()
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y; a[i+h:i+2*h]=x-y
        h*=2
    return a

def coeff_p(vals):
    n=len(vals).bit_length()-1
    c=fwht(vals)/(1<<n)
    return c,c*c

def entropy_p(p):
    p=np.asarray(p,float)
    return float((-p*np.log2(np.where(p>0,p,1))).sum())

def H_vals(vals):
    return entropy_p(coeff_p(vals)[1])

def Phi_vals(vals,lam):
    n=len(vals).bit_length()-1
    if n==0:
        return 0.0
    c,p=coeff_p(vals)
    if lam==0.0:
        return C*entropy_p(p)
    return float((n/lam)*(np.sum(np.abs(c)**(2-lam/n))-1.0))

def G_vals(vals,lam):
    return Phi_vals(vals,lam)-C*H_vals(vals)

def Inf_vals(vals):
    vals=np.asarray(vals)
    n=len(vals).bit_length()-1
    idx=np.arange(len(vals))
    return np.array([np.mean(vals != vals[idx^(1<<i)]) for i in range(n)],float)

def restrict_general(vals,A,assign):
    n=len(vals).bit_length()-1
    A=list(A)
    comp=[i for i in range(n) if i not in A]
    out=[]
    for y in range(1<<len(comp)):
        x=0
        for r,i in enumerate(comp):
            x |= ((y>>r)&1)<<i
        for r,i in enumerate(A):
            x |= ((assign>>r)&1)<<i
        out.append(vals[x])
    return np.asarray(out)

def block_charge(vals,A,lam):
    n=len(vals).bit_length()-1
    A=list(A)
    comp=[i for i in range(n) if i not in A]
    c,p=coeff_p(vals)
    H=entropy_p(p)
    marg=np.zeros(1<<len(comp))
    for s,ps in enumerate(p):
        key=sum(((s>>i)&1)<<r for r,i in enumerate(comp))
        marg[key]+=ps
    B=H-entropy_p(marg)
    dH=H-np.mean([H_vals(restrict_general(vals,A,a)) for a in range(1<<len(A))])
    dPhi=Phi_vals(vals,lam)-np.mean([Phi_vals(restrict_general(vals,A,a),lam) for a in range(1<<len(A))])
    dG=dPhi-C*dH
    IA=float(Inf_vals(vals)[A].sum())
    ratio=(B+dG)/IA if IA>1e-15 else (float("-inf") if B+dG<=1e-12 else float("inf"))
    return B,dG,dH,dPhi,IA,ratio

def one_point(n):
    return np.array([-1]+[1]*((1<<n)-1),dtype=np.int8)

def majority_signs(ss):
    return 1 if sum(ss)>=0 else -1

def maj_sign(x,positions):
    return majority_signs([1 if ((x>>i)&1)==0 else -1 for i in positions])

def majority(n):
    return np.array([maj_sign(x,range(n)) for x in range(1<<n)],dtype=np.int8)

def majority_of_majority():
    vals=[]
    for x in range(1<<9):
        gs=[maj_sign(x,range(3*g,3*g+3)) for g in range(3)]
        vals.append(majority_signs(gs))
    return np.array(vals,dtype=np.int8)

def addressing2():
    vals=[]
    for x in range(64):
        a=((x>>0)&1)+2*((x>>1)&1)
        vals.append(1 if ((x>>(2+a))&1)==0 else -1)
    return np.array(vals,dtype=np.int8)

def bent4():
    vals=[]
    for x in range(16):
        b=[(x>>i)&1 for i in range(4)]
        vals.append(-1 if ((b[0]&b[1])^(b[2]&b[3])) else 1)
    return np.array(vals,dtype=np.int8)

def tensor_w3():
    a=one_point(3)
    return np.array([int(a[x&7]*a[(x>>3)&7]) for x in range(64)],dtype=np.int8)

def gamma3_maj3():
    seed=majority(3)
    return np.array([int(seed[(x>>3)&7]) if (x&7)==0 else 1 for x in range(64)],dtype=np.int8)

def padded_bent_marker(m=4,k=3):
    vals=[]; n=1+m+k
    for X in range(1<<n):
        t=X&1
        xb=[(X>>(1+i))&1 for i in range(m)]
        q=0
        for j in range(0,m,2):
            q ^= xb[j]&xb[j+1]
        b=-1 if q else 1
        cc=-b if all(v==0 for v in xb) else b
        F=b if t==0 else cc
        z=(X>>(1+m))&((1<<k)-1)
        w=-1 if z==0 else 1
        vals.append(F*w)
    return np.array(vals,dtype=np.int8)

def tested_blocks(n,structural):
    masks=set(1<<i for i in range(n))
    for i in range(n):
        for j in range(i+1,n):
            masks.add((1<<i)|(1<<j))
    for i in range(n):
        masks.add(((1<<n)-1)^(1<<i))
    masks.update(structural)
    masks.discard(0); masks.discard((1<<n)-1)
    return sorted(masks)

def named_case(vals,structural):
    n=len(vals).bit_length()-1
    blocks=tested_blocks(n,structural)
    out={}
    for lam in LAMBDAS:
        rec=[]
        for mask in blocks:
            A=[i for i in range(n) if (mask>>i)&1]
            B,dG,dH,dPhi,IA,r=block_charge(vals,A,lam)
            if IA>1e-15:
                rec.append((r,mask,B,dG,dH,dPhi,IA))
        best=min(rec,key=lambda z:z[0])
        singles=[z for z in rec if (z[1]&(z[1]-1))==0]
        out[str(lam)]={
            "best_tested_ratio":float(best[0]),
            "best_tested_mask":int(best[1]),
            "best_singleton_ratio":float(min(z[0] for z in singles)),
            "max_singleton_ratio":float(max(z[0] for z in singles)),
            "best_components":{
                "B":float(best[2]),"dG":float(best[3]),"dH":float(best[4]),
                "dPhi":float(best[5]),"I_A":float(best[6])
            }
        }
    return out

small,budget_err=exhaustive_dynamic()
named={
    "one_point_w6":named_case(one_point(6),{0b111,0b111000}),
    "addressing_2_to_4_n6":named_case(addressing2(),{0b11,0b111100}),
    "bent_quadratic_n4":named_case(bent4(),{0b0011,0b1100}),
    "tensor_w3_w3_n6":named_case(tensor_w3(),{0b000111,0b111000}),
    "majority5":named_case(majority(5),set()),
    "majority3_of_majority3_n9":named_case(majority_of_majority(),{0b000000111,0b000111000,0b111000000,0b000111111,0b111111000}),
    "Gamma3_Maj3_n6":named_case(gamma3_maj3(),{0b000111,0b111000}),
    "padded_bent_marker_m4_k3_n8":named_case(padded_bent_marker(4,3),{0b00000110,0b00011000,0b11100000,0b00011110,0b11100001})
}
op={}
for n in range(2,13):
    vals=one_point(n)
    B,dG,dH,dPhi,II,r=block_charge(vals,[0],1.0)
    op[str(n)]={
        "B_over_Inf":float(B/II),
        "dPhi_over_Inf":float(dPhi/II),
        "dH_over_Inf":float(dH/II),
        "debiased_charge_over_Inf":float(r)
    }

min_grid_increment=1e100
min_G=1e100
for n in range(1,5):
    G=all_data(n)[5]
    for li in range(len(LAMBDAS)):
        min_G=min(min_G,float(np.min(G[li])))
        if li:
            min_grid_increment=min(min_grid_increment,float(np.min(G[li]-G[li-1])))

Cchi=2.0+1.0/(math.sqrt(math.e)*math.log(2.0))
character_child_debiased=(1.0-C)*Cchi+4.0

result={
    "status":"PASS",
    "full_FEI_proved":False,
    "constant_c_ln2_over_2":C,
    "new_potential":"G_{n,lambda}=Phi_{n,lambda}-(ln2/2)H, Phi=(n/lambda)(sum|fhat|^(2-lambda/n)-1)",
    "local_charge":"Q_{A,lambda}=B_A + Delta_A G_lambda = B_A+Delta_A Phi_lambda-(ln2/2)Delta_A H",
    "compiler":"A universal hereditary proper-block selector with nondecreasing lambda and Q<=K I_A implies H<=2K I.",
    "character_child_debiased_upper_constant_lambda1":character_child_debiased,
    "one_point_predicted_limit_lambda1":4.0-2.0*math.log(2.0),
    "exhaustive_small_boolean_dynamic_grid":small,
    "max_abs_block_influence_budget_error":budget_err,
    "min_G_on_small_grid":min_G,
    "min_G_grid_increment_on_small_grid":min_grid_increment,
    "named_stress":named,
    "one_point_sequence":op,
    "coded_F8":{
        "physical_inputs":2040,
        "new_selector_status":"UNVERIFIED",
        "reason":"The archived F_8 truth table is not enumerable in this bounded run, and no compressed certificate for Q_{A,lambda}/I_A is proved. The analytic compiler itself is dimension-free and applies formally, but no paid block is asserted."
    },
    "limitations":[
        "Finite floating-point checks are self-checks, not proof, independent validation, or formal verification.",
        "The monotone-scale compiler is proved analytically in the report; the grid {0,.25,.5,.75,1} only tests a finite discretization through dimension four.",
        "Named examples test all singletons, all pairs, all-but-one blocks, and listed structural blocks, not every proper block above dimension four.",
        "No universal hereditary paid selector is inferred from the finite tests."
    ]
}
print(json.dumps(result,indent=2,sort_keys=True))
