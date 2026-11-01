import itertools, math, json
from collections import Counter

TOL=2e-11
KSTAR=7.0/6.0+(5.0/6.0)*((-0.2*math.log2(0.2)-0.8*math.log2(0.8))+(-0.1*math.log2(0.1)-0.9*math.log2(0.9)))

def fwht_int(vals):
    a=list(map(int,vals)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def marg_q(q,coords):
    coords=tuple(coords); out=[0]*(1<<len(coords))
    for s,qs in enumerate(q):
        t=0
        for k,i in enumerate(coords):
            if (s>>i)&1: t|=1<<k
        out[t]+=qs
    return out

def independent_cut(q,A,n):
    A=tuple(sorted(A)); B=tuple(i for i in range(n) if i not in A)
    qA=marg_q(q,A); qB=marg_q(q,B); Q=sum(q)
    for s,qs in enumerate(q):
        a=b=0
        for k,i in enumerate(A):
            if (s>>i)&1: a|=1<<k
        for k,i in enumerate(B):
            if (s>>i)&1: b|=1<<k
        if qs*Q != qA[a]*qB[b]: return False,qA,qB
    return True,qA,qB

def entropy_int_weights(q):
    Q=sum(q); ans=0.0
    for w in q:
        if w:
            p=w/Q; ans-=p*math.log2(p)
    return ans

def mean_level(q):
    Q=sum(q)
    return sum(s.bit_count()*w for s,w in enumerate(q))/Q

def B_i(vs,d,i):
    W=fwht_int(vs); Q=sum(w*w for w in W); ans=0.0
    for r in range(1<<(d-1)):
        low=r & ((1<<i)-1); high=r>>i
        s0=low | (high<<(i+1)); s1=s0 | (1<<i)
        a=W[s0]*W[s0]; b=W[s1]*W[s1]; z=a+b
        if a and b:
            p=a/z
            ans += (z/Q)*(-p*math.log2(p)-(1-p)*math.log2(1-p))
    return ans

def restrict_local(vs,d,i,bit):
    return [vs[x] for x in range(1<<d) if ((x>>i)&1)==bit]

def prefix_R(vs,n,order):
    def rec(cur,coords,ordr):
        if not ordr: return 0.0
        orig=ordr[0]; i=coords.index(orig)
        root=B_i(cur,len(coords),i)
        nc=coords[:i]+coords[i+1:]
        return root+0.5*rec(restrict_local(cur,len(coords),i,0),nc,ordr[1:])+0.5*rec(restrict_local(cur,len(coords),i,1),nc,ordr[1:])
    return rec(vs,list(range(n)),list(order))

def integer_rigidity(max_entry=20):
    tested=0; qualifying=0
    for t in range(1,5):
        for vec in itertools.combinations_with_replacement(range(1,max_entry+1),t):
            g=0
            for x in vec: g=math.gcd(g,x)
            if g!=1: continue
            tested+=1
            N=sum(x*x for x in vec)
            if N & (N-1): continue
            qualifying+=1
            if not (all(x==1 for x in vec) and t in (1,2,4)):
                raise AssertionError(("rigidity",vec,N))
    return {"primitive_vectors_tested":tested,"power2_norm_vectors":qualifying,"max_entry":max_entry}

def exhaustive(max_n=4):
    out={"functions_mod_sign":0,"proper_cuts":0,"independent_sparse_cuts":0,
         "support_counts":Counter(),"star_cuts":0,"max_uniformity_spread":0,
         "max_prefix_minus_bound":-1e100,"max_block_entropy_minus_8over3_I":-1e100,
         "max_prefix_ratio":0.0}
    for n in range(1,max_n+1):
        N=1<<n
        for mask in range(1<<(N-1)):
            vals=[1]+[1 if ((mask>>(x-1))&1)==0 else -1 for x in range(1,N)]
            W=fwht_int(vals); q=[w*w for w in W]
            out["functions_mod_sign"]+=1
            if n==1: continue
            for Amask in range(1,(1<<n)-1):
                A=[i for i in range(n) if (Amask>>i)&1]
                out["proper_cuts"]+=1
                ok,qA,qB=independent_cut(q,A,n)
                supp=[s for s,w in enumerate(qA) if w]
                if not ok or len(supp)>4: continue
                out["independent_sparse_cuts"]+=1; out["support_counts"][str(len(supp))]+=1
                pos=[qA[s] for s in supp]
                spread=max(pos)-min(pos)
                out["max_uniformity_spread"]=max(out["max_uniformity_spread"],spread)
                if spread!=0: raise AssertionError(("nonuniform marginal",n,mask,A,qA,qB,W))
                HA=entropy_int_weights(qA); IA=mean_level(qA)
                out["max_block_entropy_minus_8over3_I"]=max(out["max_block_entropy_minus_8over3_I"],HA-(8.0/3.0)*IA)
                if HA>(8.0/3.0)*IA+TOL: raise AssertionError(("block entropy",n,mask,A,HA,IA,qA))
                total_weight=sum(s.bit_count() for s in supp)
                if len(supp)==4 and total_weight==3:
                    out["star_cuts"]+=1
                    singles=[s for s in supp if s and (s&(s-1))==0]
                    if 0 not in supp or len(singles)!=3:
                        raise AssertionError(("star geometry",A,supp))
                    first_local=(singles[0].bit_length()-1)
                    order=[A[first_local]]+[x for x in A if x!=A[first_local]]
                else:
                    order=A
                R=prefix_R(vals,n,order)
                out["max_prefix_minus_bound"]=max(out["max_prefix_minus_bound"],R-KSTAR*IA)
                if IA>0: out["max_prefix_ratio"]=max(out["max_prefix_ratio"],R/IA)
                if R>KSTAR*IA+TOL:
                    raise AssertionError(("prefix theorem",n,mask,A,supp,R,IA,KSTAR))
    out["support_counts"]=dict(out["support_counts"])
    return out

def sharp_star_example():
    # A=(x1,x2,x3), B=(y1,y2). In F2 notation the four B-sections are
    # 00: chi_{x3}; 10: -chi_{x1}; 01: -chi_{x2}; 11: 1.
    vals=[]
    for z in range(32):
        x1,x2,x3,y1,y2=[(z>>i)&1 for i in range(5)]
        if (y1,y2)==(0,0): v=(-1)**x3
        elif (y1,y2)==(1,0): v=-((-1)**x1)
        elif (y1,y2)==(0,1): v=-((-1)**x2)
        else: v=1
        vals.append(v)
    W=fwht_int(vals); q=[w*w for w in W]
    ok,qA,qB=independent_cut(q,[0,1,2],5)
    if not ok: raise AssertionError("sharp example not independent")
    supp=[s for s,w in enumerate(qA) if w]
    if supp != [0,1,2,4] or len(set(qA[s] for s in supp))!=1:
        raise AssertionError(("sharp support",supp,qA))
    HA=entropy_int_weights(qA); IA=mean_level(qA)
    if abs(HA/IA-8/3)>TOL: raise AssertionError((HA,IA))
    R=min(prefix_R(vals,5,o) for o in itertools.permutations([0,1,2]))
    if R>KSTAR*IA+TOL: raise AssertionError(("sharp prefix",R,IA))
    return {"walsh_nonzero_count":sum(w!=0 for w in W),"walsh_abs_values":sorted(set(abs(w) for w in W if w)),
            "A_support":supp,"H_SA":HA,"I_A":IA,"H_SA_over_I_A":HA/IA,
            "best_fixed_A_prefix_R":R,"best_prefix_ratio":R/IA,
            "proved_prefix_constant":KSTAR,"proved_prefix_bound":KSTAR*IA,
            "exact_star_prefix_formula":7.0/8.0+(5.0/8.0)*((-0.2*math.log2(0.2)-0.8*math.log2(0.8))+(-0.1*math.log2(0.1)-0.9*math.log2(0.9)))}

def support5_arithmetic_obstruction():
    vec=(5,2,1,1,1); N=sum(x*x for x in vec)
    if N!=32 or math.gcd(*vec)!=1: raise AssertionError(vec)
    ps=[x*x/N for x in vec]
    H=-sum(p*math.log2(p) for p in ps)
    # Put the largest atom at the empty set and the four others at singleton labels.
    I=1-max(ps)
    return {"primitive_vector":list(vec),"squared_norm":N,"entropy_if_empty_gets_largest":H,
            "mean_level_if_others_singletons":I,"ratio":H/I}

if __name__=='__main__':
    out={"status":"PASS","Kstar":KSTAR,"integer_rigidity":integer_rigidity(),
         "exhaustive":exhaustive(),"sharp_star_example":sharp_star_example(),
         "support5_arithmetic_obstruction":support5_arithmetic_obstruction()}
    print(json.dumps(out,indent=2,sort_keys=True))
