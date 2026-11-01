#!/usr/bin/env python3
import math, json, time, hashlib, heapq
import numpy as np

C0 = math.log(2.0)/2.0
CREC = 2.0/math.log(2.0)
LAMBDAS = (0.25,0.5,1.0)

def fwht(vals):
    a=np.asarray(vals,dtype=float).copy()
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y; a[i+h:i+2*h]=x-y
        h*=2
    return a/len(a)

def spectrum(vals):
    c=fwht(vals)
    p=c*c
    return p

def Hprob(p):
    p=np.asarray(p,float)
    return float((-p*np.log2(np.where(p>0,p,1.0))).sum())

def Tq(p,q):
    p=np.asarray(p,float)
    return float((np.power(p,q).sum()-1.0)/((1.0-q)*math.log(2.0)))

def marginal(p,n,coords):
    coords=list(coords)
    q=np.zeros(1<<len(coords),float)
    for s,ps in enumerate(p):
        key=0
        for r,i in enumerate(coords):
            key |= ((s>>i)&1)<<r
        q[key]+=ps
    return q

def child(vals,n,i,bit):
    rem=[j for j in range(n) if j!=i]
    out=np.empty(1<<(n-1),dtype=np.int8)
    for z in range(1<<(n-1)):
        x=bit<<i
        for r,j in enumerate(rem):
            x |= ((z>>r)&1)<<j
        out[z]=vals[x]
    return out,rem

def restrict(vals,n,fixed,assign):
    fixed=list(fixed)
    rem=[i for i in range(n) if i not in fixed]
    out=np.empty(1<<len(rem),dtype=np.int8)
    for z in range(1<<len(rem)):
        x=0
        for r,i in enumerate(rem):
            x |= ((z>>r)&1)<<i
        for r,i in enumerate(fixed):
            x |= ((assign>>r)&1)<<i
        out[z]=vals[x]
    return out,rem

def infs(vals):
    vals=np.asarray(vals)
    n=len(vals).bit_length()-1
    idx=np.arange(len(vals))
    return np.array([np.mean(vals != vals[idx^(1<<i)]) for i in range(n)],float)

def js(P,Q):
    M=.5*(P+Q)
    return Hprob(M)-.5*(Hprob(P)+Hprob(Q))

def Kcoef(n,lam):
    q=1.0-lam/(2.0*n)
    r=1.0-q
    b=(2.0**r-1.0)/(r*math.log(2.0))
    return (2.0**(lam*(n-1.0)/n))*b

def phi_projected(vals,ambient_n,A,lam):
    p=spectrum(vals)
    pp=marginal(p,ambient_n,A)
    q=1.0-lam/(2.0*ambient_n)
    return C0*Tq(pp,q)

def g_projected(vals,ambient_n,A,lam):
    p=spectrum(vals)
    pp=marginal(p,ambient_n,A)
    return phi_projected(vals,ambient_n,A,lam)-C0*Hprob(pp)

def vals_from_mask(mask,n):
    N=1<<n
    vals=np.ones(N,dtype=np.int8)
    for x in range(1,N): # canonicalize global sign with f(0)=+1
        if (mask>>(x-1))&1: vals[x]=-1
    return vals

def exhaustive_projected(max_n=4):
    out={}
    max_dp=0.0; max_phi=0.0; max_g=0.0; max_js=0.0
    total=0
    t0=time.time()
    for n in range(2,max_n+1):
        N=1<<n
        M=1<<(N-1)
        local_total=0
        local_dp=local_phi=local_g=local_js=0.0
        for mask in range(M):
            vals=vals_from_mask(mask,n)
            I=infs(vals)
            for i in range(n):
                g,rem=child(vals,n,i,0)
                h,_=child(vals,n,i,1)
                P=spectrum(g); Q=spectrum(h)
                fulljs=js(P,Q)
                ji=min(float(I[i]),1.0-float(I[i]))
                for Amask in range(1,1<<(n-1)):
                    Achild=[r for r in range(n-1) if (Amask>>r)&1]
                    PA=marginal(P,n-1,Achild); QA=marginal(Q,n-1,Achild)
                    MPA=.5*(PA+QA)
                    jsa=js(PA,QA)
                    local_js=max(local_js,jsa-fulljs)
                    for lam in LAMBDAS:
                        qn=1.0-lam/(2.0*n)
                        qc=1.0-lam/(2.0*(n-1))
                        tqgap=Tq(MPA,qn)-.5*(Tq(PA,qc)+Tq(QA,qc))
                        dphi=C0*tqgap
                        dg=dphi-C0*jsa
                        K=Kcoef(n,lam)
                        local_phi=max(local_phi,dphi-K*ji)
                        local_g=max(local_g,dg-(K-1.0)*ji)
                        # frozen Tsallis data processing + atom-floor comparison
                        jtA=Tq(MPA,qn)-.5*(Tq(PA,qn)+Tq(QA,qn))
                        jtF=Tq(.5*(P+Q),qn)-.5*(Tq(P,qn)+Tq(Q,qn))
                        local_dp=max(local_dp,jtA-jtF)
                    local_total+=1
        out[str(n)]={"canonical_functions":M,"query_target_cases":local_total}
        total+=local_total
        max_dp=max(max_dp,local_dp); max_phi=max(max_phi,local_phi)
        max_g=max(max_g,local_g); max_js=max(max_js,local_js)
    return {
        "dimensions":out,
        "query_target_cases":total,
        "max_projected_tsallis_data_processing_violation":max_dp,
        "max_projected_js_data_processing_violation":max_js,
        "max_adaptive_projected_phi_payment_violation":max_phi,
        "max_adaptive_projected_G_payment_violation":max_g,
        "seconds":time.time()-t0
    }

def block_transverse(vals,A,lam):
    n=len(vals).bit_length()-1
    A=list(A); Y=[i for i in range(n) if i not in A]
    root_phi=phi_projected(vals,n,A,lam)
    root_g=g_projected(vals,n,A,lam)
    leaf_phi=[]; leaf_g=[]
    for y in range(1<<len(Y)):
        sec,rem=restrict(vals,n,Y,y)
        d=len(A)
        leaf_phi.append(phi_projected(sec,d,range(d),lam))
        leaf_g.append(g_projected(sec,d,range(d),lam))
    dphi=root_phi-float(np.mean(leaf_phi))
    dg=root_g-float(np.mean(leaf_g))
    I=infs(vals); IY=float(I[Y].sum())
    return {"DeltaPhi":dphi,"DeltaG":dg,"IY":IY,
            "phi_ratio":dphi/IY if IY>1e-14 else None,
            "G_ratio":dg/IY if IY>1e-14 else None,
            "phi_bound":2.0**lam,"G_bound":2.0**lam-1.0}

def section_entropy(vals,n,fixed):
    fixed=list(fixed)
    total=0.0
    for a in range(1<<len(fixed)):
        sec,_=restrict(vals,n,fixed,a)
        total += Hprob(spectrum(sec))
    return total/(1<<len(fixed))

def cut_check(vals,A):
    n=len(vals).bit_length()-1
    A=list(A); B=[i for i in range(n) if i not in A]
    p=spectrum(vals); H=Hprob(p)
    pA=marginal(p,n,A); pB=marginal(p,n,B)
    MI=Hprob(pA)+Hprob(pB)-H
    EA=section_entropy(vals,n,B) # sections on A
    EB=section_entropy(vals,n,A) # sections on B
    I=infs(vals)
    rhs=EA+EB+CREC*float(I.sum())-MI
    return H,MI,rhs,rhs-H

def balanced_tree(coords):
    coords=list(coords)
    if len(coords)<=1: return coords[0] if coords else None
    k=len(coords)//2
    return (balanced_tree(coords[:k]),balanced_tree(coords[k:]))

def leaves(tree):
    if isinstance(tree,int): return [tree]
    return leaves(tree[0])+leaves(tree[1])

def dependency_bank(vals,tree):
    n=len(vals).bit_length()-1
    allcoords=set(range(n))
    def rec(node):
        U=leaves(node)
        if len(U)==1: return 0.0
        L=leaves(node[0]); R=leaves(node[1])
        outside=sorted(allcoords-set(U))
        total=0.0
        for a in range(1<<len(outside)):
            sec,rem=restrict(vals,n,outside,a)
            # map original coords in U to sec indices
            pos={orig:k for k,orig in enumerate(rem)}
            p=spectrum(sec); d=len(rem)
            PL=marginal(p,d,[pos[x] for x in L])
            PR=marginal(p,d,[pos[x] for x in R])
            total += Hprob(PL)+Hprob(PR)-Hprob(p)
        total /= (1<<len(outside))
        return total+rec(node[0])+rec(node[1])
    return rec(tree)

def depths(tree,d=0,out=None):
    if out is None: out={}
    if isinstance(tree,int):
        out[tree]=d
    else:
        depths(tree[0],d+1,out); depths(tree[1],d+1,out)
    return out

def huffman_depths(weights):
    active=[(float(w),[i]) for i,w in enumerate(weights) if w>1e-15]
    if len(active)<=1:
        return {active[0][1][0]:0} if active else {}
    heap=[]; serial=0
    dep={i:0 for _,ls in active for i in ls}
    for w,ls in active:
        heapq.heappush(heap,(w,serial,ls)); serial+=1
    while len(heap)>1:
        w1,_,l1=heapq.heappop(heap); w2,_,l2=heapq.heappop(heap)
        for i in l1+l2: dep[i]+=1
        heapq.heappush(heap,(w1+w2,serial,l1+l2)); serial+=1
    return dep

def profile_stats(vals):
    n=len(vals).bit_length()-1
    I=infs(vals); It=float(I.sum()); H=Hprob(spectrum(vals))
    tree=balanced_tree(range(n)); dep=depths(tree)
    bank=dependency_bank(vals,tree)
    cost=CREC*sum(dep[i]*I[i] for i in range(n))
    hdep=huffman_depths(I)
    hcost=CREC*sum(hdep.get(i,0)*I[i] for i in range(n))
    if It>0:
        w=I/It; nz=w[w>1e-15]
        Hp=float((-nz*np.log2(nz)).sum())
    else: Hp=0.0
    return {
        "n":n,"H":H,"I":It,"H_over_I":H/It if It else 0.0,
        "balanced_dependency_bank":bank,
        "balanced_depth_cost":cost,
        "balanced_bound_after_bank_over_I":(cost-bank)/It if It else 0.0,
        "balanced_identity_slack":cost-bank-H,
        "huffman_depth_cost_over_I":hcost/It if It else 0.0,
        "influence_profile_entropy":Hp,
        "profile_corollary_over_I":CREC*(Hp+1.0) if It else 0.0
    }

def one_point(n):
    return np.array([-1]+[1]*((1<<n)-1),dtype=np.int8)
def majority_signs(ss): return 1 if sum(ss)>=0 else -1
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
        for j in range(0,m,2): q ^= xb[j]&xb[j+1]
        b=-1 if q else 1
        cc=-b if all(v==0 for v in xb) else b
        F=b if t==0 else cc
        z=(X>>(1+m))&((1<<k)-1)
        w=-1 if z==0 else 1
        vals.append(F*w)
    return np.array(vals,dtype=np.int8)

def random_cut_tests(trials=500,seed=20260920):
    rng=np.random.default_rng(seed)
    min_slack=1e100
    for _ in range(trials):
        n=int(rng.integers(2,8)); N=1<<n
        vals=np.where(rng.integers(0,2,size=N)==0,1,-1).astype(np.int8)
        k=int(rng.integers(1,n))
        A=sorted(rng.choice(n,size=k,replace=False).tolist())
        *_,slack=cut_check(vals,A)
        min_slack=min(min_slack,slack)
    return {"trials":trials,"min_bidirectional_cut_slack":min_slack}

def random_tsallis_coarsegrain(trials=3000,seed=20260921):
    rng=np.random.default_rng(seed)
    maxvio=0.0
    for _ in range(trials):
        m=int(rng.integers(2,10))
        P=rng.random(m); Q=rng.random(m); P/=P.sum(); Q/=Q.sum()
        groups=rng.integers(0,max(1,m//2),size=m)
        ng=int(groups.max())+1
        Pc=np.zeros(ng); Qc=np.zeros(ng)
        for i,g in enumerate(groups): Pc[g]+=P[i]; Qc[g]+=Q[i]
        for lam in LAMBDAS:
            q=1-lam/8.0 # arbitrary q in (0,1), enough as a numerical stress
            fine=Tq(.5*(P+Q),q)-.5*(Tq(P,q)+Tq(Q,q))
            coarse=Tq(.5*(Pc+Qc),q)-.5*(Tq(Pc,q)+Tq(Qc,q))
            maxvio=max(maxvio,coarse-fine)
    return {"trials":trials,"max_coarse_minus_fine":maxvio}

def main():
    ex=exhaustive_projected(3)
    named_vals={
        "one_point_w6":(one_point(6),[0,1,2]),
        "addressing_2_to_4_n6":(addressing2(),[2,3,4,5]),
        "bent_quadratic_n4":(bent4(),[0,1]),
        "tensor_w3_w3_n6":(tensor_w3(),[0,1,2]),
        "majority5":(majority(5),[0,1]),
        "majority3_of_majority3_n9":(majority_of_majority(),[0,1,2]),
        "Gamma3_Maj3_n6":(gamma3_maj3(),[3,4,5]),
        "padded_bent_marker_m4_k3_n8":(padded_bent_marker(4,3),[1,2,3,4])
    }
    named={}
    for name,(vals,A) in named_vals.items():
        n=len(vals).bit_length()-1
        cut=cut_check(vals,A)
        rec={
            "profile":profile_stats(vals),
            "cut":{"A":A,"MI":cut[1],"rhs":cut[2],"slack":cut[3]},
            "transverse_lambda":{str(lam):block_transverse(vals,A,lam) for lam in LAMBDAS}
        }
        named[name]=rec
    result={
        "status":"PASS",
        "executed_checker_source_sha256":hashlib.sha256(open(__file__,"rb").read()).hexdigest(),
        "full_FEI_proved":False,
        "constants":{"2_over_ln2":CREC,"ln2_over_2":C0},
        "theorems_tested":[
            "projected Tsallis Jensen divergence contracts under coarse graining",
            "adaptive projected Phi transverse charge <= K_{n,lambda} j_i < 2^lambda j_i",
            "adaptive projected debiased G transverse charge <= (K_{n,lambda}-1) j_i < (2^lambda-1) j_i",
            "bidirectional cut: H+MI <= E_B H(section A)+E_A H(section B)+(2/ln2)I",
            "partition dependency-bank: H+M_T <= (2/ln2) sum_i d_i Inf_i"
        ],
        "exhaustive_small_boolean":ex,
        "random_cut":random_cut_tests(),
        "random_tsallis_coarsegrain":random_tsallis_coarsegrain(),
        "named_stress":named,
        "coded_F8":{
            "physical_inputs":2040,
            "status":"UNVERIFIED",
            "reason":"No bounded truth-table enumeration or new compressed projected-bank certificate was available in this run."
        },
        "limitations":[
            "Floating-point executable checks are self-checks, not proof, independent validation, Lean/formal verification, or publication-priority clearance.",
            "The analytic proof, not finite testing, carries the all-dimensional claims.",
            "The projected transverse theorem does not pay orientation/conditional allocation inside the retained spectral block.",
            "The dependency-bank Huffman corollary retains influence-profile entropy and is therefore not a dimension-free FEI bound.",
            "The archived coded F_8 stress case is not computationally verified here."
        ]
    }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
