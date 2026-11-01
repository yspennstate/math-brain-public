import math, itertools, json, random
import numpy as np
from functools import lru_cache

RHO = 2.0 / math.log(2.0)
TOL = 2e-9

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def fwht(vals):
    a = np.asarray(vals, dtype=float).copy()
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            x = a[i:i+h].copy(); y = a[i+h:i+2*h].copy()
            a[i:i+h] = x+y
            a[i+h:i+2*h] = x-y
        h *= 2
    a /= n
    return a

def entropy_probs(p):
    p = np.asarray(p, dtype=float)
    q = p[p > 1e-18]
    return float(-(q*np.log2(q)).sum())

def spectral_probs(vals):
    w = fwht(vals)
    return w*w

def coord_bit(m, pos):
    return 1 << (m-1-pos)

def influences(vals, coords):
    m = len(coords)
    ten = np.asarray(vals).reshape([2]*m)
    out = {}
    for pos,c in enumerate(coords):
        a = np.take(ten,0,axis=pos)
        b = np.take(ten,1,axis=pos)
        out[c] = float(np.mean(a != b))
    return out

def B_coord(vals, coords, c):
    m = len(coords); pos = coords.index(c); bit = coord_bit(m,pos)
    p = spectral_probs(vals)
    total = 0.0
    for mask in range(1<<m):
        if mask & bit: continue
        a = p[mask]; b = p[mask|bit]; s=a+b
        if s > 1e-18:
            total += s*h2(b/s)
    return total

def restrict_fixed(vals, coords, fixed):
    m=len(coords)
    ten=np.asarray(vals).reshape([2]*m)
    sl=[]; new=[]
    for c in coords:
        if c in fixed: sl.append(fixed[c])
        else: sl.append(slice(None)); new.append(c)
    arr=np.asarray(ten[tuple(sl)]).reshape(-1)
    return arr, tuple(new)

def all_sections(vals, coords, block):
    block=tuple(block)
    for bits in itertools.product([0,1], repeat=len(block)):
        fixed=dict(zip(block,bits))
        yield restrict_fixed(vals, coords, fixed)

def tree_leaves(t):
    if isinstance(t,int): return (t,)
    return tree_leaves(t[0])+tree_leaves(t[1])

def coeff_maps(t):
    # direct and hereditary coefficient maps relative to this partition subtree,
    # singleton leaves use exact C=K=0.
    if isinstance(t,int):
        return {t:0.0},{t:0.0}
    c0,k0=coeff_maps(t[0]); c1,k1=coeff_maps(t[1])
    c={}; k={}
    for childc, childk in [(c0,k0),(c1,k1)]:
        for i in childc:
            c[i]=childc[i]+RHO
            k[i]=0.5*(childc[i]+childk[i]+RHO)
    return c,k

def mutual_info_cut(vals, coords, A, B):
    m=len(coords); p=spectral_probs(vals)
    pos={c:j for j,c in enumerate(coords)}
    ma={}; mb={}
    for mask,pm in enumerate(p):
        if pm < 1e-18: continue
        ka=tuple((mask >> (m-1-pos[c])) & 1 for c in A)
        kb=tuple((mask >> (m-1-pos[c])) & 1 for c in B)
        ma[ka]=ma.get(ka,0.0)+pm
        mb[kb]=mb.get(kb,0.0)+pm
    return entropy_probs(list(ma.values()))+entropy_probs(list(mb.values()))-entropy_probs(p)

def dependency_bank(vals, coords, t):
    if isinstance(t,int): return 0.0
    A=tree_leaves(t[0]); B=tree_leaves(t[1])
    mi=mutual_info_cut(vals, coords, A, B)
    ea=0.0
    for arr,newc in all_sections(vals, coords, B):
        ea += dependency_bank(arr,newc,t[0])/(2**len(B))
    eb=0.0
    for arr,newc in all_sections(vals, coords, A):
        eb += dependency_bank(arr,newc,t[1])/(2**len(A))
    return mi+ea+eb

def prefix_then(vals, coords, order, cont_tree):
    if not order:
        return compile_R(vals, coords, cont_tree)
    i=order[0]
    b=B_coord(vals,coords,i)
    total=b
    desc=0.0
    for val in [0,1]:
        arr,newc=restrict_fixed(vals,coords,{i:val})
        desc += 0.5*prefix_then(arr,newc,order[1:],cont_tree)
    return total+desc

def compile_R(vals, coords, t):
    if isinstance(t,int):
        # querying final one-bit section has B=0 for Boolean signs.
        return 0.0
    A=tree_leaves(t[0]); B=tree_leaves(t[1])
    inf=influences(vals,coords)
    cA,kA=coeff_maps(t[0]); cB,kB=coeff_maps(t[1])
    boundA=sum(cA[i]*inf[i] for i in A)+sum((kB[j]+RHO)*inf[j] for j in B)
    boundB=sum((kA[i]+RHO)*inf[i] for i in A)+sum(cB[j]*inf[j] for j in B)
    if boundA <= boundB:
        return prefix_then(vals,coords,tuple(sorted(A)),t[1])
    return prefix_then(vals,coords,tuple(sorted(B)),t[0])

def all_binary_trees(labels):
    labels=tuple(labels)
    if len(labels)==1:
        return [labels[0]]
    # unordered root split, canonical by requiring first label in A
    first=labels[0]; rest=labels[1:]
    out=[]
    for r in range(0,len(rest)):
        for sub in itertools.combinations(rest,r):
            A=(first,)+sub
            B=tuple(x for x in labels if x not in A)
            if not B: continue
            for ta in all_binary_trees(A):
                for tb in all_binary_trees(B):
                    out.append((ta,tb))
    return out

def theorem_rhs(vals,coords,t):
    inf=influences(vals,coords); c,k=coeff_maps(t)
    return sum(k[i]*inf[i] for i in coords)

def check_function(vals,coords,trees):
    worst=-1e99; rec=None
    for t in trees:
        rhs=theorem_rhs(vals,coords,t)
        R=compile_R(vals,coords,t)
        M=dependency_bank(vals,coords,t)
        v=R+M-rhs
        if v>worst:
            worst=v; rec=(R,M,rhs,t)
    return worst,rec

def anchored_mux(k):
    n=k+(1<<k)
    vals=[]
    for x in itertools.product([0,1], repeat=n):
        a=x[:k]; y=x[k:]
        idx=0
        for bit in a: idx=(idx<<1)|bit
        phase=y[idx] ^ (y[0]&y[1])
        vals.append(1 if phase==0 else -1)
    return np.array(vals,dtype=int)

def signed_translation_nontrivial(vals):
    N=len(vals); n=int(round(math.log2(N)))
    arr=np.asarray(vals)
    bad=[]
    for t in range(1,N):
        shifted=np.empty(N,dtype=int)
        for x in range(N): shifted[x]=arr[x^t]
        prod=arr*shifted
        if np.all(prod==prod[0]): bad.append((t,int(prod[0])))
    return bad

def mux_formula(k):
    D=k+4-2**(2-k)
    I=D/2.0
    H=math.log2(D)+((2-2**(2-k))*(k-1))/D
    coll=(k+2+2**(2-k)-2**(3-2*k))/(D*D)
    return D,I,H,coll,RHO*(H+coll)

summary={"rho":RHO,"tests":{}}
# exhaustive n<=3 modulo global sign, all labeled binary coordinate trees
for n in [2,3]:
    coords=tuple(range(n)); trees=all_binary_trees(coords)
    N=1<<n; worst=-1e99; count=0; worstrec=None
    # fix vals[0]=+1 to quotient global sign
    for tail in itertools.product([1,-1], repeat=N-1):
        vals=np.array((1,)+tail,dtype=int)
        v,rec=check_function(vals,coords,trees)
        count += len(trees)
        if v>worst: worst=v; worstrec=rec
    summary["tests"][f"exhaustive_n{n}"]={"tree_function_cases":count,"num_trees":len(trees),"max_R_plus_M_minus_rhs":worst,
                                                       "worst_R_M_rhs":None if worstrec is None else [worstrec[0],worstrec[1],worstrec[2]]}
    if worst>TOL: raise SystemExit(f"FAIL n={n} {worst}")

# deterministic n=4 sample, all labeled binary trees
n=4; coords=tuple(range(n)); trees=all_binary_trees(coords); N=1<<n
rng=random.Random(202609201808)
worst=-1e99; count=0; worstrec=None
for s in range(220):
    vals=np.array([1]+[1 if rng.getrandbits(1)==0 else -1 for _ in range(N-1)],dtype=int)
    v,rec=check_function(vals,coords,trees)
    count += len(trees)
    if v>worst: worst=v; worstrec=rec
summary["tests"]["sample_n4"]={"functions":220,"num_trees":len(trees),"tree_function_cases":count,"max_R_plus_M_minus_rhs":worst,
                                  "worst_R_M_rhs":None if worstrec is None else [worstrec[0],worstrec[1],worstrec[2]]}
if worst>TOL: raise SystemExit(f"FAIL n4 {worst}")

# anchored multiplexer exact influence / rigidity checks for k=2,3
mux=[]
for k in [2,3]:
    vals=anchored_mux(k); n=k+(1<<k); coords=tuple(range(n)); inf=influences(vals,coords)
    D,I,H,coll,profile_bound=mux_formula(k)
    expected=[]
    for i in range(n):
        if i<k or i in [k,k+1]: expected.append(0.5)
        else: expected.append(2**(-k))
    max_inf_err=max(abs(inf[i]-expected[i]) for i in range(n))
    bad=signed_translation_nontrivial(vals)
    mux.append({"k":k,"n":n,"total_influence_bruteforce":sum(inf.values()),"total_influence_formula":I,
                "max_coordinate_influence_error":max_inf_err,"nontrivial_signed_translations":bad,
                "profile_entropy_formula":H,"collision_formula":coll,"hereditary_profile_constant":profile_bound})
    if abs(sum(inf.values())-I)>TOL or max_inf_err>TOL or bad:
        raise SystemExit(f"FAIL mux k={k}")
summary["tests"]["anchored_multiplexer"]=mux

# compare asymptotic constants against newest balanced-block K_L
comp=[]
for k in [3,4,6,8,12,20,40,80]:
    n=k+(1<<k)
    L=math.ceil(math.log2(n))
    Kbal=2+(L-2)*RHO+(RHO-1)*(2**(1-L))
    D,I,H,coll,Kprof=mux_formula(k)
    comp.append({"k":k,"ambient_n":n,"balanced_L":L,"K_balanced":Kbal,"K_profile":Kprof,"gain_factor":Kbal/Kprof})
summary["tests"]["balanced_vs_profile"]=comp
summary["status"]="PASS"

with open('/mnt/data/hereditary_dependency_routing_output.json','w') as f:
    json.dump(summary,f,indent=2,sort_keys=True)
print(json.dumps(summary,indent=2,sort_keys=True))
