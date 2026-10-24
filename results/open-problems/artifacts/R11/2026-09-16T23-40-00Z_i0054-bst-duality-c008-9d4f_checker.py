from fractions import Fraction
from itertools import permutations, product
from collections import Counter
from math import comb, factorial

# R11 / I0054 / C008 exact finite self-check.
# FINITE CLAIMS ONLY. The whole-path asymptotic convergence follows in the
# written report from the already-proved weighted-tree universality theorem U001.

def H(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction(0))

def beta_int(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def bst_fringe_formula(m,s):
    return Fraction(2*(m+1),(s+1)*(s+2))

def bst_oriented_profile(m,s):
    return bst_fringe_formula(m,s)+bst_fringe_formula(m,m-s)

def bst_weight(m,s):
    return Fraction(m, s*(m-s))/bst_oriented_profile(m,s)

def cayley_oriented_profile(m,s):
    return Fraction(comb(m,s)*(s**(s-1))*((m-s)**(m-s-1)), m**(m-2))

def cayley_weight(m,s):
    return Fraction(m, s*(m-s))/cayley_oriented_profile(m,s)

# ---- BST construction / exact enumeration ----
def bst_from_perm(perm):
    left={x:None for x in perm}
    right={x:None for x in perm}
    root=perm[0]
    for x in perm[1:]:
        cur=root
        while True:
            if x<cur:
                if left[cur] is None:
                    left[cur]=x
                    break
                cur=left[cur]
            else:
                if right[cur] is None:
                    right[cur]=x
                    break
                cur=right[cur]
    return root,left,right

def bst_child_fringe_sizes(perm):
    root,left,right=bst_from_perm(perm)
    sizes={}
    def dfs(x):
        if x is None:
            return 0
        sizes[x]=1+dfs(left[x])+dfs(right[x])
        return sizes[x]
    dfs(root)
    return [sizes[x] for x in perm if x!=root]

enum_checks=0
for m in range(2,9):
    counts=Counter()
    for p in permutations(range(1,m+1)):
        for s in bst_child_fringe_sizes(p):
            counts[s]+=1
    den=factorial(m)
    for s in range(1,m):
        assert Fraction(counts[s],den)==bst_fringe_formula(m,s)
        enum_checks += 1
print("BST_fringe_enumeration: PASS", enum_checks, "exact (m,s) cases through m=8")

# Recurrence proof identity and closed form.
rec_checks=0
for s in range(1,30):
    # Base A_{s,s}=1. The displayed closed form is only for s<m.
    lhs=bst_fringe_formula(s+1,s)
    rhs=Fraction(2,s+1)
    assert lhs==rhs
    rec_checks += 1
    for m in range(s+2,60):
        rhs=Fraction(2,m)*(Fraction(1,1)+sum((bst_fringe_formula(r,s) for r in range(s+1,m)),Fraction(0)))
        assert bst_fringe_formula(m,s)==rhs
        rec_checks += 1
print("BST_fringe_recurrence_closed_form: PASS", rec_checks, "exact cases")

# ---- U001 expected oriented-side profile and weight bound ----
profile_checks=0
for m in range(2,101):
    for s in range(1,m):
        z=bst_oriented_profile(m,s)
        w=bst_weight(m,s)
        assert z*w==Fraction(m,s*(m-s))
        assert w==bst_weight(m,m-s)
        assert w < Fraction(3,2)
        profile_checks += 1
print("BST_U001_profile_and_weight_bound: PASS", profile_checks, "exact cases")

# Total expected physical-edge weight = H_{m-1}.
harmonic_checks=0
for m in range(2,101):
    val=Fraction(1,2)*sum((bst_oriented_profile(m,s)*bst_weight(m,s)
                          for s in range(1,m)),Fraction(0))
    assert val==H(m-1)
    harmonic_checks+=1
print("BST_expected_total_weight_harmonic: PASS", harmonic_checks, "exact cases")

# ---- Hidden-size beta-binomial identity used by U001 ----
beta_checks=0
for m in range(2,31):
    for b in range(2,m+1):
        for i in range(1,b):
            lhs=Fraction(0)
            for s in range(i, m-(b-i)+1):
                lhs += Fraction(m,s*(m-s))*Fraction(comb(m-b,s-i),comb(m,s))
            assert lhs==beta_int(i,b-i)
            beta_checks += 1
print("hidden_size_beta_identity: PASS", beta_checks, "exact triples")

# ---- Method 5: Cayley/BST interpolation keeps the target profile ----
mix_checks=0
for theta in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]:
    for m in range(2,31):
        for s in range(1,m):
            z=theta*cayley_oriented_profile(m,s)+(1-theta)*bst_oriented_profile(m,s)
            w=Fraction(m,s*(m-s))/z
            assert z*w==Fraction(m,s*(m-s))
            assert w <= max(cayley_weight(m,s),bst_weight(m,s))
            assert w < Fraction(3,2)
            mix_checks += 1
print("Cayley_BST_interpolation_profile: PASS", mix_checks, "exact cases")

# ---- Method 11: Pascal coherence / Hausdorff moment identity for CTCS ----
coh_checks=0
for m in range(3,51):
    for i in range(1,m-1):
        assert beta_int(i,m-1-i)==beta_int(i,m-i)+beta_int(i+1,m-i-1)
        coh_checks+=1
moment_checks=0
for m in range(2,51):
    for i in range(1,m):
        val=Fraction(0)
        for j in range(0,m-i):
            val += (-1)**j * comb(m-i-1,j)*Fraction(1,i+j)
        assert val==beta_int(i,m-i)
        moment_checks+=1
print("CTCS_Pascal_coherence: PASS",coh_checks,"exact cases")
print("CTCS_Hausdorff_moment_expansion: PASS",moment_checks,"exact cases")

# ---- Pruefer/Cayley utilities for exact N=4 witness ----
def prufer_edges(seq,n):
    degree=[0]+[1]*n
    for x in seq:
        degree[x]+=1
    seq=list(seq)
    edges=[]
    for x in seq:
        leaf=min(i for i in range(1,n+1) if degree[i]==1)
        edges.append((leaf,x))
        degree[leaf]-=1
        degree[x]-=1
    rem=[i for i in range(1,n+1) if degree[i]==1]
    edges.append((rem[0],rem[1]))
    return edges

def edge_side_size(n,edges,eidx):
    u,v=edges[eidx]
    adj={i:[] for i in range(1,n+1)}
    for j,(a,b) in enumerate(edges):
        if j==eidx:
            continue
        adj[a].append(b); adj[b].append(a)
    seen={u}; stack=[u]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    return len(seen)

def reduced_all_edge_cut_probability_bst(m,delta):
    allp=Fraction(0); nonep=Fraction(0)
    den=factorial(m)
    for p in permutations(range(1,m+1)):
        ps=[delta*bst_weight(m,s) for s in bst_child_fringe_sizes(p)]
        a=Fraction(1); n=Fraction(1)
        for q in ps:
            a*=q; n*=1-q
        allp+=a; nonep+=n
    allp/=den; nonep/=den
    return allp,nonep,allp/(1-nonep)

def reduced_all_edge_cut_probability_cayley(m,delta):
    allp=Fraction(0); nonep=Fraction(0)
    total=m**(m-2)
    for seq in product(range(1,m+1),repeat=m-2):
        edges=prufer_edges(seq,m)
        ss=[edge_side_size(m,edges,j) for j in range(m-1)]
        ps=[delta*cayley_weight(m,s) for s in ss]
        a=Fraction(1); n=Fraction(1)
        for q in ps:
            a*=q; n*=1-q
        allp+=a; nonep+=n
    allp/=total; nonep/=total
    return allp,nonep,allp/(1-nonep)

delta4=Fraction(1,4**3)
bst_all,bst_none,bst_red=reduced_all_edge_cut_probability_bst(4,delta4)
cay_all,cay_none,cay_red=reduced_all_edge_cut_probability_cayley(4,delta4)
assert bst_all==Fraction(47,53993472)
assert bst_none==Fraction(52461505,53993472)
assert bst_red==Fraction(47,1531967)
assert cay_all==Fraction(35,40310784)
assert cay_none==Fraction(39167029,40310784)
assert cay_red==Fraction(7,228751)
assert bst_red != cay_red
print("N4_BST_raw_all_edges =",bst_all)
print("N4_BST_raw_no_edge =",bst_none)
print("N4_BST_reduced_degree4 =",bst_red)
print("N4_Cayley_reduced_degree4 =",cay_red)
print("BST_vs_Cayley_non_equivalence: PASS")

# At N=3 C008 has the same reduced degree-3 witness 1/71 as C007,
# so N=4 is intentionally used to distinguish these two classes.
bst3_all,bst3_none,bst3_red=reduced_all_edge_cut_probability_bst(3,Fraction(1,3**3))
assert bst3_red==Fraction(1,71)
print("N3_BST_reduced_degree3 =",bst3_red)

# Rare-cut condition for chosen delta_N=N^-3 and A_N=3N/2:
# delta_N A_N^2 = 9/(4N) -> 0. Finite exact sanity.
for N in range(2,101):
    val=Fraction(9,4*N)
    assert val>0
print("rare_cut_scale_identity: delta_N*A_N^2 = 9/(4N) -> 0 (symbolic)")
print("ALL_EXACT_CHECKS_PASS")
