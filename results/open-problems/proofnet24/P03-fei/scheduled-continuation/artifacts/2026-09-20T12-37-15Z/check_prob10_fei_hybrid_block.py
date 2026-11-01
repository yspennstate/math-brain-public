#!/usr/bin/env python3
import numpy as np, math, json
from functools import lru_cache

def hadamard(n):
    N=1<<n
    W=np.ones((N,N),dtype=float)
    for s in range(N):
        for x in range(N):
            if ((s & x).bit_count() & 1):
                W[s,x]=-1.0
    return W

@lru_cache(None)
def all_tables_data(n):
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
    Phi = np.zeros(M) if n==0 else n*((np.abs(coeff)**(2-1/n)).sum(axis=1)-1.0)
    infl=np.empty((M,n),float)
    idx=np.arange(N)
    for i in range(n):
        infl[:,i]=(signs != signs[:,idx^(1<<i)]).mean(axis=1)
    return signs,coeff,p,H,Phi,infl

def entropy_p(p):
    p=np.asarray(p,float)
    return float((-p*np.log2(np.where(p>0,p,1))).sum())

def spec_vec(vals):
    vals=np.asarray(vals,float)
    n=len(vals).bit_length()-1
    c=vals @ hadamard(n).T / len(vals)
    return c,c*c

def H_vals(vals):
    return entropy_p(spec_vec(vals)[1])

def Phi_vals(vals):
    n=len(vals).bit_length()-1
    if n==0: return 0.0
    c,_=spec_vec(vals)
    return float(n*(np.abs(c)**(2-1/n)).sum()-n)

def Inf_vals(vals):
    vals=np.asarray(vals)
    n=len(vals).bit_length()-1
    idx=np.arange(len(vals))
    return np.array([np.mean(vals != vals[idx^(1<<i)]) for i in range(n)],float)

def restrict_general(vals,A,assign):
    n=len(vals).bit_length()-1
    A=list(A); comp=[i for i in range(n) if i not in A]
    inds=[]
    for y in range(1<<len(comp)):
        x=0
        for r,i in enumerate(comp):
            x |= ((y>>r)&1)<<i
        for r,i in enumerate(A):
            x |= ((assign>>r)&1)<<i
        inds.append(x)
    return np.asarray(vals)[inds]

def block_hybrid(vals,A):
    n=len(vals).bit_length()-1
    A=list(A); comp=[i for i in range(n) if i not in A]
    c,p=spec_vec(vals)
    H=entropy_p(p)
    marg=np.zeros(1<<len(comp))
    for s,ps in enumerate(p):
        key=sum(((s>>i)&1)<<r for r,i in enumerate(comp))
        marg[key]+=ps
    B=H-entropy_p(marg)
    AA=Phi_vals(vals)-np.mean([Phi_vals(restrict_general(vals,A,a)) for a in range(1<<len(A))])
    IA=float(Inf_vals(vals)[A].sum())
    ratio=(B+AA)/IA if IA>1e-15 else math.inf
    return B,AA,IA,ratio

def exhaustive_small():
    out={}
    budget_err=0.0
    for n in range(2,5):
        signs,coeff,p,H,Phi,infl=all_tables_data(n)
        M=len(signs)
        relevant=infl.sum(axis=1)>1e-15
        best_single=np.full(M,np.inf)
        best_block=np.full(M,np.inf)
        best_single_A=np.full(M,-1,int)
        best_block_A=np.full(M,-1,int)
        cases=0
        for Amask in range(1,(1<<n)-1):
            A=[i for i in range(n) if (Amask>>i)&1]
            comp=[i for i in range(n) if i not in A]
            marg=np.zeros((M,1<<len(comp)),float)
            for s in range(1<<n):
                key=sum(((s>>i)&1)<<r for r,i in enumerate(comp))
                marg[:,key]+=p[:,s]
            Hm=(-marg*np.log2(np.where(marg>0,marg,1))).sum(axis=1)
            B=H-Hm
            IA=infl[:,A].sum(axis=1)
            k=len(A); d=n-k
            childphis=np.zeros(M,float)
            childI=np.zeros(M,float)
            _,_,_,_,Phi_d,Inf_d=all_tables_data(d)
            for assign in range(1<<k):
                inds=[]
                for y in range(1<<d):
                    x=0
                    for r,i in enumerate(comp): x |= ((y>>r)&1)<<i
                    for r,i in enumerate(A): x |= ((assign>>r)&1)<<i
                    inds.append(x)
                ch=signs[:,inds].copy()
                neg=ch[:,0]<0
                ch[neg]*=-1
                cm=np.zeros(M,dtype=np.int64)
                for j in range(1,1<<d):
                    cm += (ch[:,j]<0).astype(np.int64) << (j-1)
                childphis += Phi_d[cm]/(1<<k)
                childI += Inf_d[cm].sum(axis=1)/(1<<k)
            AA=Phi-childphis
            budget_err=max(budget_err,float(np.max(np.abs(infl.sum(axis=1)-(IA+childI)))))
            ratio=np.full(M,np.inf)
            pos=IA>1e-15
            ratio[pos]=(B[pos]+AA[pos])/IA[pos]
            improve=ratio<best_block
            best_block[improve]=ratio[improve]; best_block_A[improve]=Amask
            if len(A)==1:
                improve=ratio<best_single
                best_single[improve]=ratio[improve]; best_single_A[improve]=Amask
            cases+=M
        rix=np.where(relevant)[0]
        ws=rix[np.argmax(best_single[rix])]
        wb=rix[np.argmax(best_block[rix])]
        out[str(n)]={
            "functions_up_to_global_sign":int(M),
            "proper_block_cases":int(cases),
            "worst_best_singleton_hybrid_ratio":float(best_single[ws]),
            "witness_singleton_canonical_mask":int(ws),
            "witness_singleton_block_mask":int(best_single_A[ws]),
            "worst_best_proper_block_hybrid_ratio":float(best_block[wb]),
            "witness_proper_canonical_mask":int(wb),
            "witness_proper_block_mask":int(best_block_A[wb]),
        }
    return out,budget_err

def one_point(n):
    return np.array([-1]+[1]*((1<<n)-1),dtype=np.int8)

def majority_signs(signs):
    return 1 if sum(signs)>=0 else -1

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
    assert m%2==0
    vals=[]
    n=1+m+k
    for X in range(1<<n):
        t=X&1
        xb=[(X>>(1+i))&1 for i in range(m)]
        q=0
        for j in range(0,m,2): q ^= xb[j]&xb[j+1]
        b=-1 if q else 1
        c=-b if all(v==0 for v in xb) else b
        F=b if t==0 else c
        z=(X>>(1+m))&((1<<k)-1)
        w=-1 if z==0 else 1
        vals.append(F*w)
    return np.array(vals,dtype=np.int8)

def tested_blocks(n,structural):
    masks=set(1<<i for i in range(n))
    for i in range(n):
        for j in range(i+1,n):
            masks.add((1<<i)|(1<<j))
    for i in range(n): masks.add(((1<<n)-1)^(1<<i))
    masks.update(structural)
    masks.discard(0); masks.discard((1<<n)-1)
    return sorted(masks)

def named_case(name,vals,structural):
    n=len(vals).bit_length()-1
    records=[]
    for mask in tested_blocks(n,structural):
        A=[i for i in range(n) if (mask>>i)&1]
        B,AA,IA,r=block_hybrid(vals,A)
        if IA>1e-15:
            records.append((r,mask,B,AA,IA))
    singles=[r for r in records if (r[1]&(r[1]-1))==0]
    bests=min(singles,key=lambda z:z[0])
    best=min(records,key=lambda z:z[0])
    return {
        "n":n,"H":H_vals(vals),"I":float(Inf_vals(vals).sum()),"Phi":Phi_vals(vals),
        "tested_proper_blocks":len(records),
        "best_singleton_hybrid_ratio":bests[0],"best_singleton_mask":bests[1],
        "max_singleton_hybrid_ratio":max(z[0] for z in singles),
        "best_tested_proper_hybrid_ratio":best[0],"best_tested_proper_mask":best[1],
        "best_tested_components":{"B":best[2],"A":best[3],"I_A":best[4]},
    }

small,budget_err=exhaustive_small()
named={}
named["one_point_w6"]=named_case("one",one_point(6),{0b111,0b111000})
named["addressing_2_to_4_n6"]=named_case("addr",addressing2(),{0b11,0b111100})
named["bent_quadratic_n4"]=named_case("bent",bent4(),{0b0011,0b1100})
named["tensor_w3_w3_n6"]=named_case("tensor",tensor_w3(),{0b000111,0b111000})
named["majority5"]=named_case("maj5",majority(5),set())
named["majority3_of_majority3_n9"]=named_case("mom",majority_of_majority(),{0b000000111,0b000111000,0b111000000,0b000111111,0b111111000})
named["Gamma3_Maj3_n6"]=named_case("gamma",gamma3_maj3(),{0b000111,0b111000})
named["padded_bent_marker_m4_k3_n8"]=named_case("pad",padded_bent_marker(4,3),{0b00000110,0b00011000,0b11100000,0b00011110,0b11100001})

op={}
for n in range(2,13):
    vals=one_point(n)
    B,A,II,r=block_hybrid(vals,[0])
    op[str(n)]={"B_over_Inf":B/II,"A_over_Inf":A/II,"hybrid_over_Inf":r}

result={
  "status":"PASS",
  "full_FEI_proved":False,
  "independent_audit":False,
  "proof_assistant_used":False,
  "hybrid_quantity":"B_A(f)+A_A(f), A_A=Phi_n(f)-2^(-|A|) sum_a Phi_(n-|A|)(f_{A=a})",
  "Phi":"Phi_n(f)=n(sum_S |fhat(S)|^(2-1/n)-1)",
  "exhaustive_small_boolean":small,
  "max_abs_block_influence_budget_error":budget_err,
  "named_stress":named,
  "one_point_singleton_sequence":op,
  "coded_F8":{
    "physical_inputs":2040,
    "truth_table_enumerated":False,
    "reason":"2^2040 truth table unavailable in a bounded run; no compressed certificate for the new hybrid selector is proved.",
    "hybrid_selector_status":"UNVERIFIED"
  },
  "limitations":[
    "Floating-point Walsh/entropy calculations are finite self-checks, not proof.",
    "Named cases use all singleton, all pair, all-but-one, and listed structural blocks, not every proper block when dimension exceeds four.",
    "No inference to the universal existential proper-block selector is made."
  ]
}
print(json.dumps(result,indent=2,sort_keys=True))
